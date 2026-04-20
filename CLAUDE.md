# Brut Natur Daily — News Digest Automation

## Projektöversikt
✅ **FULLT FUNKTIONELLT SYSTEM** — Automated daily news digest för Brut Natur, Swedish high-end turnkey holiday homes. Hämtar, kurerar och skickar relevant arkitektur- och designnyheter från nordiska och internationella källor varje morgon kl 08:00.

**Mottagare:** fia@brutcompany.com (Google Workspace)  
**Frekvens:** Varje måndag  
**Tid:** 08:00 UTC (GitHub Actions)  
**GitHub Repo:** https://github.com/fia-a11y/brut-natur-daily  
**Status:** 🟢 Aktiv & automatiserad  

---

## Konfiguration

### Automation
- **Plattform:** GitHub Actions
- **Tid:** 08:00 UTC varje måndag (kan justera cron i `.github/workflows/brut-natur-daily.yml`)
- **Körning:** Fullständigt automatiserad, ingen manuell åtgärd krävs
- **Autentisering:** OAuth2 med Google (Gmail API) + refresh token för auto-renewal

### Email-format
- **Till:** fia@brutcompany.com (Google Workspace)
- **Ämne:** Brut Natur Daily [DATUM] — X nyheter
- **Språk:** Svenska
- **Ton:** Professionell, ingen budget-fokus, inga utropstecken
- **Format:** HTML med elegant layout (gradient header)

### Content-funktioner
- **LinkedIn-drafts:** Varje artikel inkluderar en ~1200 tecken LinkedIn-post (svenska, professionell ton)
- **Kuraterad innehål:** Claude AI väljer max 10 mest relevanta artiklar
- **Industritrender:** 5-6 aktuella trender inom arkitektur/design
- **Scoring:** Varje artikel betygsatt på relevans, trovärdighet, handlingspotential

---

## Innehållskällor

### RSS-Feeds
1. **Arkitekten.se** — https://arkitekten.se/feed/
   - Focus: Nordisk arkitektur, design, bygglov
   - Artiklar per vecka: 5

2. **Residence Magazine** — https://www.residencemagazine.se/rss/
   - Focus: Nordiska fritidshus, design, renovering
   - Artiklar per vecka: **1** (limited)

3. **ArchDaily** — http://feeds.feedburner.com/Archdaily
   - Focus: Internationell arkitektur, featured projects
   - Artiklar per vecka: 5

4. **Designboom** — https://www.designboom.com/feed/
   - Focus: Design trends, installations, exhibitions
   - Artiklar per vecka: 5

5. **Rum** — https://etidning.tidskriftenrum.se/
   - Focus: Svensk arkitektur, inredning, designkultur
   - Artiklar per vecka: 5

6. **Vogue Living** — https://www.vogue.com/living/homes
   - Focus: Globala hem, interiördesign, arkitektur
   - Artiklar per vecka: 5

### Web Searches
- Nordic cabin architecture 2026
- Nordic interior design trend 2026
- Fritidshus arkitektritat 2026
- Sommarnojens nyheter 2026
- Tham Videgard projekt 2026
- Senaste hetaste projekt från Dezeen och ArchDaily

---

## Innehålls-Kriterier

### Kategoriering
**HIGH Priority:**
1. Arkitektur och material
2. Nordisk designtrend

**MEDIUM Priority:**
3. Designutställningar och priser
4. Fritidshusmarknad

### Filtreringsregler
- ✓ Senaste 7 dagar
- ✓ Relevans för arkitektur/design/fritidshus
- ✗ Inte äldre än 7 dagar
- ✗ Inte duplikater
- ✗ Inte infrastruktur-nyheter
- ✗ Inte personalnyheter
- ✗ Inte budget-segment
- ✗ Inte politik

### Geografisk fördelning
- Målsättning: Minst 60% nordiskt innehål
- Rest: Globala highlights och inspirationskällor

### Scoring (1-5)
Varje artikel betygsätts på:
- **Relevance:** Hur direkt kopplad till arkitektur/design/fritidshus
- **Credibility:** Källans trovärdighet
- **Action Potential:** Möjlighet till tillämpning för Brut Natur

Minimum 9 av 15 items bör uppfylla kriterierna.

---

## Email-Struktur

### Avsnitt
1. **Masthead**
   - Brut Natur logotyp/namn
   - "DAILY DIGEST"
   - Aktuellt datum

2. **Overview**
   - 2-3 meningar om innehållet denna vecka
   - Kort kontext om fokus

3. **Nordic News Section** (4 artiklar)
   - Per artikel:
     - Rubrik
     - Källa | Datum
     - Kategori-badge (färgkodad)
     - Sammanfattning i box (3 meningar)
     - Scoring (Relevans | Trovärdighet | Handlingspotential)
     - "För Brut Natur" – varför detta är relevant
     - LinkedIn-draft (ca 1200 tecken, Swedish, ingen exclamation)
     - "Läs artikel →" länk

4. **Global Spotlight Section**
   - 6 internationella arkitekturprojekt från Dezeen & ArchDaily
   - Per projekt:
     - Namn, arkitekt/studio, stad
     - Kort beskrivning (1-2 meningar)
     - "Insight" – relevans för Brut Natur

5. **Industritrendspaningar Section**
   - 6 huvudtrender inom design/arkitektur/marknad
   - Per trend:
     - Rubrik (uppercase)
     - Trend-beskrivning
     - "För Brut Natur" – konkret relevans

6. **Footer**
   - Brut Natur Daily presentation
   - Källhänvisning
   - brutnatur.se länk

---

## Styling & Layout

### Färger
- Primary: #2c3e50 (mörkblå)
- Secondary: #34495e (mörkgrå-blå)
- Background: #fafaf8 (off-white)
- Accent: #ede9e3 (ljus gråbrun)

### Typography
- Font-family: Segoe UI, Trebuchet MS, sans-serif
- H1: 32px, weight 300, letter-spacing 2px
- H2: 21px, weight 500
- H3: 15px, weight 600, uppercase
- Body: 13px, line-height 1.7

### Komponenter
- Gradient header (135deg, #2c3e50 → #34495e)
- Kategori-badges (farvakodade puncter)
- Boxade sammanfattningar (#f5f3f0 bakgrund)
- Scoring-boxes (#f9f9f7 bakgrund)
- LinkedIn-draft boxes (#ede9e3 italic)
- Section dividers (1px solid #ede9e3)

---

## Brut Natur Kontext

### Varumärke
- High-end turnkey holiday homes
- Fokus: Nordisk arkitektur, hållbarhet, tidlöshet
- Filosofi: Substans före trend, materialsäkerhet, långsiktighet
- Målmarknad: Högvärdiga köpare som söker autentisk arkitektonisk kvalitet

### Relevans-Riktlinjer
Nyheter väljs för att:
1. Inspirera design & arkitekturdiskussion
2. Visa marknadsförhållanden för arkitektritade fritidshus
3. Demonstrera global design-utveckling
4. Validera Brut Naturs design-filosofi
5. Ge insikter om trender och kundkrav

---

## Underhåll & Hantering

### GitHub Actions Workflow
- **Status:** ✅ Aktivt och automatiserat
- **Filplats:** `.github/workflows/brut-natur-daily.yml`
- **Körning:** Dagligen 08:00 UTC
- **Loggning:** GitHub Actions → Actions tab → senaste körning

### Framtida Uppdateringar
Om du vill uppdatera:
- **Skickningstid:** Redigera `.github/workflows/brut-natur-daily.yml` → `cron:` värde
- **Email-mottagare:** Uppdatera `RECIPIENT_EMAIL` GitHub Secret
- **Innehålls-kriterier:** Uppdatera `WEB_SEARCHES` eller prompt i `scripts/generate_digest.py`
- **RSS-sources:** Uppdatera `RSS_FEEDS` lista i `scripts/generate_digest.py`
- **API-nyckel:** Uppdatera `ANTHROPIC_API_KEY` GitHub Secret (vid rotation)

---

## Teknisk Implementation

### Arkitektur
```
GitHub Actions (08:00 UTC varje dag)
    ↓
Python Script (generate_digest.py)
    ├─ Hämtar RSS-feeds (feedparser)
    ├─ Skickar web search queries
    ├─ Genererar digest med Claude AI (claude-sonnet-4-6)
    │   └─ Parsar JSON response (med markdown code block handling)
    │   └─ Genererar LinkedIn-drafts (~1200 tecken)
    ├─ Formaterar HTML-email (EmailFormatter)
    └─ Skickar via Gmail API (OAuth2)
```

### Komponenter

**Python Script (`scripts/generate_digest.py`):**
- `FeedFetcher` — Hämtar & parsar RSS-feeds med feedparser
- `WebSearcher` — Placeholder för trend-sökning
- `DigestGenerator` — Anropar Claude API för kuraterad digest
- `EmailFormatter` — Genererar responsiv HTML-email
- `GmailSender` — Skickar via Gmail API med OAuth2-autentisering

**Autentisering:**
- Använder `google-oauth2-credentials` med `InstalledAppFlow`
- OAuth2-token sparas i `token.json` (auto-refresh vid expiry)
- Första körning öppnar browser för user-godkännande

**Claude API:**
- Model: `claude-sonnet-4-6`
- Max tokens: 8000
- Returnerar JSON med:
  - Overview (kort sammanfattning)
  - Articles array (max 10 artiklar)
    - title, source, url, summary, relevance
    - linkedin_draft (genererad LinkedIn-post)
  - Trends array (5-6 industritrender)

**JSON Extraction:**
Claude kan returnera JSON wrapped i markdown code blocks. Scriptet hanterar detta genom:
1. Försöka parse JSON direkt
2. Om det misslyckas: extrahera '{...}' från respons
3. Ta bort trailing markdown backticks
4. Parse igen med felmeddelanden

---

## Anteckningar för Framtida Sessions

- ✅ **SYSTEM ÄR FULLT AUTOMATISERAT** — Email skickas direkt via Gmail API, ingen manuell åtgärd krävs
- ✅ **OAuth2-token auto-refreshing** — Token sparas lokalt och uppdateras automatiskt vid expiry
- ✅ **LinkedIn-drafts genereras** — Varje artikel inkluderar en professionell LinkedIn-post
- ✅ **JSON-parsing robust** — Hanterar markdown code block wrapping från Claude API
- **Layout är responsiv** och fungerar i de flesta email-klienter (Gmail, Outlook, Apple Mail, etc.)
- Om OAuth-token blir ogiltig: radera `token.json` och nästa körning frågar om ny autentisering

---

## Lokal Testning

### Setup för lokal utveckling

1. **Kopiera template-filen:**
   ```bash
   cp .env.example .env
   ```

2. **Redigera `.env` med dina värden:**
   ```bash
   ANTHROPIC_API_KEY=sk-ant-xxxxx
   RECIPIENT_EMAIL=fia@brutcompany.com
   ```

3. **Installera dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Kör scriptet lokalt:**
   ```bash
   python scripts/generate_digest.py
   ```

### Säkerhet

- ✓ `.env` är i `.gitignore` — aldrig committerad
- ✓ `.env.example` är en template — säker att commita
- ✓ GitHub Actions använder GitHub Secrets — ännu säkrare
- ✗ **Dela ALDRIG `.env` eller API-nycklar**

---

## GitHub Actions Setup

### Fil-struktur
```
.github/workflows/
├── brut-natur-daily.yml      # Workflow definition (committerad)
scripts/
├── generate_digest.py         # Main digest generation script (committerad)
.env.example                   # Template för lokal setup (committerad)
.env                           # Din lokala config (INTE committerad, i .gitignore)
.gitignore                     # Git configuration
requirements.txt              # Python dependencies (committerad)
CLAUDE.md                      # This file (committerad)
README.md                      # Setup guide (committerad)
```

### Installation & Setup

#### 1. Push till GitHub
```bash
git remote add origin https://github.com/USERNAME/brut-natur-daily.git
git branch -M main
git push -u origin main
```

#### 2. Konfigurera GitHub Secrets
I ditt GitHub repo, gå till **Settings → Secrets and variables → Actions** och lägg till:

**Secret 1: ANTHROPIC_API_KEY**
- Värde: Din Anthropic API-nyckel från https://console.anthropic.com/

**Secret 2: RECIPIENT_EMAIL**
- Värde: fia@brutcompany.com (eller annan mottagaradress)

**Secret 3: GOOGLE_REFRESH_TOKEN**
- Värde: Refresh token från OAuth2-flödet (sparad från första körning)

**Secret 4: GOOGLE_CLIENT_ID**
- Värde: Client ID från credentials.json

**Secret 5: GOOGLE_CLIENT_SECRET**
- Värde: Client Secret från credentials.json

#### 3. OAuth2-autentisering (engångsprocedur)

**Första gången scriptet körs lokalt:**
1. Scriptet öppnar en browser för Google-autentisering
2. Du loggar in med ditt Google-konto
3. Du godkänner Gmail API-åtkomst
4. En token.json skapas lokalt med refresh_token
5. Kopiera refresh_token från token.json till GitHub Secret `GOOGLE_REFRESH_TOKEN`

Efter detta fungerar GitHub Actions helt automatiskt — scriptet använder refresh_token för att auto-uppdatera access_token vid varje körning.

### Körning

**Automatisk:**
- Körs varje dag kl 08:00 UTC (kan justeras i `.github/workflows/brut-natur-daily.yml`)

**Manuell:**
- Gå till GitHub repo → Actions → "Brut Natur Daily Digest" → "Run workflow"

### Loggning & Debugging

GitHub Actions sparar alla körningsloggar:
1. Gå till **Actions** i ditt repo
2. Välj senaste körning
3. Se loggar från steget "Generate and send Brut Natur Daily"

Loggar sparas också som artifacts (`.log` filer) som kan hämtas.

### Maintenance

**Uppdatera schema:**
- Redigera `.github/workflows/brut-natur-daily.yml`, ändra `cron:` värdet

**Uppdatera innehål-kriterier:**
- Redigera `scripts/generate_digest.py`, uppdatera `WEB_SEARCHES` eller prompt

**Uppdatera recipients:**
- Ändra `RECIPIENT_EMAIL` GitHub Secret

---

**Senast uppdaterad:** 16 april 2026  
**Status:** ✅ Fullt automatiserad — GitHub Actions kör varje måndag 08:00 UTC, email skickas automatiskt via Gmail API med auto-renewing OAuth2 token
