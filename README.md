# Brut Natur Daily — Automated News Digest

Automated daily news digest for Brut Natur, Swedish high-end turnkey holiday homes. Fetches architecture and design news from Nordic and international sources, curates with Claude AI, and sends via email.

## Quick Start

### 1. Create GitHub Repository

```bash
# Create a new repo on GitHub (https://github.com/new)
# Then push this code:

git remote add origin https://github.com/YOUR_USERNAME/brut-natur-daily.git
git branch -M main
git push -u origin main
```

### 2. Configure GitHub Secrets

In your GitHub repo:
- Go to **Settings → Secrets and variables → Actions**
- Click **New repository secret**
- Add these three secrets:

| Secret Name | Value | Where to get |
|-------------|-------|--------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | https://console.anthropic.com/ |
| `RECIPIENT_EMAIL` | Email to receive digest | e.g., `fia.fjelde@gmail.com` |
| `GMAIL_SERVICE_ACCOUNT_JSON` | (Optional) Gmail service account JSON | Google Cloud Console (see docs) |

### 3. Enable GitHub Actions

- Go to **Actions** tab in your repo
- You should see "Brut Natur Daily Digest" workflow
- It will run automatically at 08:00 UTC every day
- Or run manually via "Run workflow" button

## What It Does

Each day at 08:00 UTC:

1. **Fetches RSS feeds** from:
   - Arkitekten.se (Nordic architecture)
   - Residence Magazine (Nordic holiday homes)
   - ArchDaily (International architecture)
   - Designboom (Design trends)

2. **Performs web searches** for:
   - Nordic cabin architecture 2026
   - Nordic interior design trends
   - Holiday homes market insights

3. **Curates with Claude AI**:
   - Filters for relevance to Brut Natur
   - Scores articles (1-5 on relevance, credibility, action potential)
   - Includes global spotlights from Dezeen & ArchDaily
   - Analyzes industry trends

4. **Sends HTML email** with:
   - Nordic news highlights
   - Global architectural inspirations
   - Design trend analysis
   - Professional Swedish formatting

## File Structure

```
.github/workflows/
├── brut-natur-daily.yml       # GitHub Actions workflow (committed)
scripts/
├── generate_digest.py          # Main digest generation script (committed)
.env.example                    # Configuration template (committed)
.env                            # Local config (NOT committed, in .gitignore)
.gitignore                      # Git configuration
CLAUDE.md                        # Detailed project documentation
README.md                        # This file
requirements.txt                # Python dependencies
```

## Local Development

### Run locally (for testing)

**1. Copy .env template:**
```bash
cp .env.example .env
```

**2. Edit `.env` with your values:**
```bash
nano .env
# Add your ANTHROPIC_API_KEY and RECIPIENT_EMAIL
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the script:**
```bash
python scripts/generate_digest.py
```

### Security Notes
- `.env` is in `.gitignore` — never committed to Git
- `.env.example` is a template — safe to commit
- Never share your `.env` file or API keys
- GitHub Actions uses GitHub Secrets instead (more secure)

## Customization

### Change timing
Edit `.github/workflows/brut-natur-daily.yml`:
```yaml
schedule:
  - cron: '0 8 * * *'  # Change this to your preferred time
```

Cron format: `minute hour day month day-of-week`
- `0 8 * * *` = 08:00 every day
- `0 9 * * 1` = 09:00 every Monday
- `0 12 * * *` = 12:00 every day

### Change RSS feeds
Edit `scripts/generate_digest.py`:
```python
RSS_FEEDS = [
    "your_feed_url_1",
    "your_feed_url_2",
]
```

### Change search queries
Edit `scripts/generate_digest.py`:
```python
WEB_SEARCHES = [
    "your_search_query_1",
    "your_search_query_2",
]
```

### Modify email recipient
Update the `RECIPIENT_EMAIL` GitHub Secret

## Monitoring

### View execution logs
1. Go to **Actions** tab in GitHub repo
2. Click on latest workflow run
3. Click on "Generate and send Brut Natur Daily" step
4. View full logs

### Download logs
Logs are also saved as GitHub artifacts:
1. Click workflow run
2. Scroll down to "Artifacts"
3. Download `.log` file

## Troubleshooting

### Workflow not running
- Check that GitHub Actions is enabled in repo settings
- Verify all secrets are configured
- Check if repo is public (free tier requires public repo for Actions)

### Email not sending
- Verify `RECIPIENT_EMAIL` is set correctly
- If using Gmail service account, ensure JSON is properly formatted
- Check logs for API errors

### API rate limits
- Anthropic: Default 3.5K requests/minute
- RSS feeds: No rate limits typically
- Adjust frequency or caching as needed

## For More Details

See **[CLAUDE.md](CLAUDE.md)** for comprehensive documentation on:
- Content curation criteria
- Email formatting & styling
- Brut Natur brand guidelines
- Architecture & setup details
- Maintenance procedures

## License

This project is proprietary to Brut Natur.

---

**Created:** April 14, 2026  
**Status:** Ready for GitHub deployment
