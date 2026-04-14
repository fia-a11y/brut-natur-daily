# Brut Natur Daily — News Digest Automation

## Projektöversikt
Automated daily news digest för Brut Natur, Swedish high-end turnkey holiday homes. Hämtar, kurerar och skickar relevant arkitektur- och designnyheter från nordiska och internationella källor varje morgon kl 08:00.

**Mottagare:** fia.fjelde@gmail.com  
**Frekvens:** Dagligen  
**Tid:** 08:00 (svensk tid)  
**CronJob ID:** 610a8ddb  

---

## Konfiguration

### Skickningstid
- **Tid:** 08:00 varje dag
- **Frekvens:** Daglig, återkommande
- **Durable:** Ja (sparas vid sessionsslut)
- **Auto-expire:** Efter 7 dagar

### Email-format
- **Till:** fia.fjelde@gmail.com
- **Ämne:** Brut Natur Daily [DATUM] — X nyheter och trender
- **Språk:** Svenska
- **Ton:** Professionell men varm, ingen budget-fokus, inga utropstecken
- **Format:** HTML med elegant layout (gradient header, färgkodade kategorier)

---

## Innehållskällor

### RSS-Feeds
1. **Arkitekten.se** — https://arkitekten.se/feed/
   - Focus: Nordisk arkitektur, design, bygglov
   - Filter: Senaste 7 dagar

2. **Residence Magazine** — https://www.residencemagazine.se/rss/
   - Focus: Nordiska fritidshus, design, renovering
   - Filter: Senaste 7 dagar

3. **ArchDaily** — http://feeds.feedburner.com/Archdaily
   - Focus: Internationell arkitektur, featured projects
   - Filter: Senaste trender, global relevans

4. **Designboom** — https://www.designboom.com/feed/
   - Focus: Design trends, installations, exhibitions
   - Filter: Senaste 7 dagar

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

### CronJob
- **Kommando för att visa jobb:** `CronList`
- **Kommando för att stoppa:** `CronDelete 610a8ddb`
- **Auto-expire:** 7 dagar från skapandet
- **För förnyelse:** Skapa nytt CronCreate-jobb

### Framtida Uppdateringar
Om du vill uppdatera:
- Skickningstid → använd `CronDelete` och ny `CronCreate`
- Email-mottagare → uppdatera i CronCreate-promten
- Innehålls-kriterier → uppdatera denna CLAUDE.md + CronCreate-prompt
- RSS-sources → uppdatera denna CLAUDE.md + CronCreate-prompt

---

## Teknisk Implementation

### Tools Used
- `WebFetch` — Hämtar RSS-feeds
- `WebSearch` — Söker efter specifika trender
- `mcp__claude_ai_Gmail__create_draft` — Skapar email-utkast
- `CronCreate` — Schemalägger daglig körning

### Prompt Structure
CronCreate-promten innehåller:
1. Instruktioner för RSS-hämtning
2. Search-queries
3. Kurerings-kriterier
4. Email-struktur-specifikation
5. HTML-formatting instruktioner
6. Sending-instruktioner via Gmail

---

## Anteckningar för Framtida Sessions

- Detta är en **durable** jobb som överlevar sessionsslut
- **Auto-expires efter 7 dagar** — planera förnyelse innan dess
- Email-draften **skapas men skickas inte automatiskt** genom systemet än (behöver manuell review/send eller mer avancerad integration)
- För **full automation** (auto-send) krävs eventuellt ytterligare API-konfiguration
- **Layout är responsiv** och fungerar i de flesta email-klienter

---

## GitHub Actions Setup

### Fil-struktur
```
.github/workflows/
├── brut-natur-daily.yml      # Workflow definition
scripts/
├── generate_digest.py         # Main digest generation script
requirements.txt              # Python dependencies
CLAUDE.md                      # This file
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
- Värde: fia.fjelde@gmail.com (eller annan mottagaradress)

**Secret 3: GMAIL_SERVICE_ACCOUNT_JSON** (optional, för auto-send)
- Värde: Service account JSON för Gmail (se nedan)

#### 3. Gmail Integration (optional)
För full automation av email-skickande:
1. Gå till [Google Cloud Console](https://console.cloud.google.com/)
2. Skapa ett projekt
3. Enable "Gmail API"
4. Skapa en Service Account
5. Download JSON-nyckeln
6. Koda den som base64 eller kopiera direkt
7. Lägg den i GitHub Secret `GMAIL_SERVICE_ACCOUNT_JSON`

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

**Senast uppdaterad:** 14 april 2026  
**Status:** Aktiv — GitHub Actions setup, ej ännu aktiverad på GitHub
