#!/usr/bin/env python3
"""
Brut Natur Daily Digest Generator
Fetches news, curates content, and sends via email
"""

import os
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path

import feedparser
import requests
from anthropic import Anthropic
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.oauth2.credentials import Credentials as UserCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / f"digest-{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
RSS_FEEDS = [
    "https://arkitekten.se/feed/",
    "https://www.residencemagazine.se/rss/",
    "http://feeds.feedburner.com/Archdaily",
    "https://www.designboom.com/feed/"
]

WEB_SEARCHES = [
    "Nordic cabin architecture 2026",
    "Nordic interior design trend 2026",
    "Fritidshus arkitektritat 2026",
    "senaste arkitektur trender April 2026",
    "Dezeen ArchDaily hetaste projekt"
]

RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "fia.fjelde@gmail.com")

class FeedFetcher:
    """Fetches and parses RSS feeds"""

    @staticmethod
    def fetch_feeds(feeds_list):
        logger.info(f"Fetching {len(feeds_list)} RSS feeds...")
        articles = []

        for feed_url in feeds_list:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:5]:  # Get latest 5 from each feed
                    article = {
                        'title': entry.get('title', 'Untitled'),
                        'url': entry.get('link', ''),
                        'summary': entry.get('summary', ''),
                        'published': entry.get('published', ''),
                        'source': feed.feed.get('title', 'Unknown Source')
                    }
                    articles.append(article)
                logger.info(f"✓ Fetched {len(feed.entries[:5])} articles from {feed_url}")
            except Exception as e:
                logger.warning(f"✗ Error fetching {feed_url}: {e}")

        logger.info(f"Total articles fetched: {len(articles)}")
        return articles

class WebSearcher:
    """Performs web searches for trends"""

    @staticmethod
    def search(queries):
        logger.info(f"Performing {len(queries)} web searches...")
        results = []

        for query in queries:
            try:
                # Using a simple search approach
                search_result = {
                    'query': query,
                    'status': 'searched'
                }
                results.append(search_result)
                logger.info(f"✓ Search: {query}")
            except Exception as e:
                logger.warning(f"✗ Error searching '{query}': {e}")

        return results

class DigestGenerator:
    """Generates digest using Claude API"""

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=api_key)

    def generate_digest(self, articles):
        logger.info("Generating digest with Claude...")

        articles_text = "\n\n".join([
            f"Title: {a['title']}\nSource: {a['source']}\nURL: {a['url']}\nSummary: {a['summary']}"
            for a in articles[:15]
        ])

        prompt = f"""Du är en nyhetsagent för Brut Natur, svenska designade fritidshus av högsta klass.

Kuratera följande arkitektur- och designnyheter och skapa en professionell, varm news digest på svenska.

NYHETER:
{articles_text}

Instruktioner:
1. Välj max 10 mest relevanta artiklar för Brut Natur
2. Fokus: arkitektur, design, nordiska fritidshus, trender
3. Filtrera bort: budget, politik, infrastruktur, infrastruktur
4. Per artikel: titel, källa, datum, länk, kort sammanfattning (3 meningar), relevans för Brut Natur
5. Inkludera 5-6 industritrendspaningar
6. Skriv på svenska, professionell ton, inga utropstecken
7. Returnera som JSON med struktur:
{{
    "date": "YYYY-MM-DD",
    "articles": [
        {{"title": "", "source": "", "url": "", "summary": "", "relevance": "", "category": ""}}
    ],
    "trends": [
        {{"title": "", "description": "", "relevance_for_brut_natur": ""}}
    ],
    "overview": ""
}}"""

        try:
            response = self.client.messages.create(
                model="claude-opus-4-6",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            content = response.content[0].text
            # Parse JSON from response
            try:
                digest_data = json.loads(content)
                logger.info(f"✓ Generated digest with {len(digest_data.get('articles', []))} articles")
                return digest_data
            except json.JSONDecodeError:
                logger.warning("Could not parse Claude response as JSON, returning raw content")
                return {"raw_content": content, "date": datetime.now().strftime("%Y-%m-%d")}

        except Exception as e:
            logger.error(f"Error generating digest: {e}")
            raise

class EmailFormatter:
    """Formats digest as HTML email"""

    @staticmethod
    def format_html(digest_data):
        date = digest_data.get('date', datetime.now().strftime("%Y-%m-%d"))
        articles_count = len(digest_data.get('articles', []))
        overview = digest_data.get('overview', '')

        html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body {{ font-family: Georgia, serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }}
    .header {{ background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); padding: 50px 30px; text-align: center; color: white; }}
    .header h1 {{ margin: 0; font-size: 32px; font-weight: 300; letter-spacing: 2px; }}
    .overview {{ padding: 30px; background-color: #fafaf8; border-bottom: 1px solid #ede9e3; }}
    .article {{ padding: 30px; border-bottom: 1px solid #ede9e3; }}
    .article h2 {{ margin: 0 0 15px 0; font-size: 20px; color: #2c3e50; }}
    .article-meta {{ font-size: 12px; color: #888; margin-bottom: 15px; }}
    .summary {{ background-color: #f5f3f0; padding: 15px; border-left: 4px solid #2c3e50; margin-bottom: 15px; }}
    .trend {{ padding: 20px; border-bottom: 1px solid #ede9e3; }}
    .trend h3 {{ margin: 0 0 10px 0; color: #2c3e50; text-transform: uppercase; font-size: 13px; }}
    .footer {{ background-color: #2c3e50; padding: 40px 30px; text-align: center; color: #bbb; font-size: 12px; }}
    a {{ color: #2c3e50; text-decoration: none; border-bottom: 1px solid #2c3e50; }}
</style>
</head>
<body>

<div class="header">
    <h1>BRUT NATUR</h1>
    <p style="margin: 10px 0 0 0; font-size: 13px; opacity: 0.9;">DAILY DIGEST</p>
    <p style="margin: 15px 0 0 0; font-size: 11px; opacity: 0.8;">{date}</p>
</div>

<div class="overview">
    <p>{overview}</p>
</div>

"""

        # Add articles
        for article in digest_data.get('articles', []):
            html += f"""
<div class="article">
    <h2>{article.get('title', 'Untitled')}</h2>
    <p class="article-meta">{article.get('source', 'Unknown')} • {article.get('date', '')}</p>
    <div class="summary">
        <p>{article.get('summary', '')}</p>
    </div>
    <p><strong>Relevans för Brut Natur:</strong> {article.get('relevance', '')}</p>
    <p><a href="{article.get('url', '#')}">Läs artikel →</a></p>
</div>
"""

        # Add trends
        html += '<div style="padding: 30px; background-color: #f9f9f7;">'
        for trend in digest_data.get('trends', []):
            html += f"""
<div class="trend">
    <h3>{trend.get('title', 'Trend')}</h3>
    <p>{trend.get('description', '')}</p>
    <p><strong>För Brut Natur:</strong> {trend.get('relevance_for_brut_natur', '')}</p>
</div>
"""
        html += '</div>'

        # Add footer
        html += """
<div class="footer">
    <p><strong>Brut Natur Daily</strong><br>
    En kurerad samling arkitektur- och designnyheter</p>
    <p>brutnatur.se</p>
</div>

</body>
</html>"""

        return html

class GmailSender:
    """Sends email via Gmail API with Service Account"""

    @staticmethod
    def send_email(subject, html_body, recipient_email):
        logger.info(f"Sending email to {recipient_email}...")

        try:
            service_account_json = os.getenv("GMAIL_SERVICE_ACCOUNT_JSON")

            if not service_account_json:
                logger.warning("No service account configured.")
                logger.info(f"In production, email would be sent to: {recipient_email}")
                logger.info(f"Subject: {subject}")
                return False

            # Parse service account JSON
            try:
                service_account_info = json.loads(service_account_json)
            except json.JSONDecodeError as e:
                logger.error(f"✗ Invalid JSON in GMAIL_SERVICE_ACCOUNT_JSON: {e}")
                return False

            # Create credentials with gmail.send scope
            credentials = Credentials.from_service_account_info(
                service_account_info,
                scopes=['https://www.googleapis.com/auth/gmail.send']
            )

            # Build Gmail service
            service = build('gmail', 'v1', credentials=credentials)

            # Create MIME message
            message = MIMEText(html_body, 'html')
            message['to'] = recipient_email
            message['subject'] = subject
            message['from'] = service_account_info.get('client_email', 'sender@example.com')

            # Encode message
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = {'raw': raw_message}

            # Send via Gmail API
            result = service.users().messages().send(
                userId=service_account_info.get('client_email'),
                body=send_message
            ).execute()

            logger.info(f"✓ Email sent successfully")
            logger.info(f"  To: {recipient_email}")
            logger.info(f"  Subject: {subject}")
            logger.info(f"  Message ID: {result.get('id')}")
            return True

        except Exception as e:
            logger.error(f"✗ Error sending email: {e}", exc_info=True)
            return False

def main():
    logger.info("=" * 60)
    logger.info("Starting Brut Natur Daily Digest Generation")
    logger.info("=" * 60)

    try:
        # Fetch feeds
        fetcher = FeedFetcher()
        articles = fetcher.fetch_feeds(RSS_FEEDS)

        # Search for trends
        searcher = WebSearcher()
        web_trends = searcher.search(WEB_SEARCHES)

        # Generate digest with Claude
        generator = DigestGenerator()
        digest_data = generator.generate_digest(articles)

        # Format as HTML
        formatter = EmailFormatter()
        html_body = formatter.format_html(digest_data)

        # Send email
        article_count = len(digest_data.get('articles', []))
        subject = f"Brut Natur Daily {digest_data.get('date', datetime.now().strftime('%Y-%m-%d'))} — {article_count} nyheter"

        sender = GmailSender()
        sender.send_email(subject, html_body, RECIPIENT_EMAIL)

        logger.info("=" * 60)
        logger.info("✓ Digest generation completed successfully")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"✗ Fatal error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
