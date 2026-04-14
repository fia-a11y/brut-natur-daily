# Gmail Service Account Setup Guide

Följ dessa steg för att aktivera auto-send via Gmail API.

## 1. Gå till Google Cloud Console

1. Öppna https://console.cloud.google.com/
2. Klicka **Create Project**
3. Name: `Brut Natur Daily`
4. Klicka **Create**

## 2. Enable Gmail API

1. I sökningen, sök: **Gmail API**
2. Klicka **Enable**
3. Du bör se "Gmail API is now enabled"

## 3. Skapa Service Account

1. Gå till **APIs & Services → Credentials**
2. Klicka **+ Create Credentials → Service Account**
3. Fyll i:
   - **Service account name:** `brut-natur-daily`
   - **Service account ID:** (auto-generated, okej att lämna)
4. Klicka **Create and Continue**
5. Klicka **Continue** (hoppa över optional steps)
6. Klicka **Done**

## 4. Skapa & Download JSON Key

1. I **Service Accounts** lista, klicka på den service account du skapade
2. Gå till **Keys** tab
3. Klicka **Add Key → Create new key**
4. Välj **JSON**
5. Klicka **Create**
6. JSON-filen laddas ner automatiskt (spara den säkert)

## 5. Configure Gmail Delegation (VIKTIGT)

1. Gå tillbaka till Service Account details
2. Kopiera **Client ID** (långt nummer)
3. Gå till **Google Admin Console** (https://admin.google.com/)
   - (Om du inte har access, be någon med admin-behörigheter)
4. Gå till **Security → API controls → Manage third-party app access**
5. Klicka **Add app**
6. Välj **OAuth application**
7. Paste in Client ID
8. Ge tillåtelse för scope: `https://www.googleapis.com/auth/gmail.send`

**Alternativ:** Om du inte har admin access, se "Simplified Setup" nedan.

## Simplified Setup (Om ingen admin access)

Om du inte kan göra delegering via Admin Console:

1. Kopiera Client Email från service account:
   - Format: `brut-natur-daily@project-id.iam.gserviceaccount.com`

2. Gå till https://myaccount.google.com/permissions

3. Lägg till denna email som en co-owner/manager på Google Workspace account

4. Service account kan nu skicka email som denna user

## 6. Lägg JSON i GitHub Secrets

1. Öppna JSON-filen du laddade ner
2. Kopiera hela innehållet
3. Gå till ditt GitHub repo: **Settings → Secrets and variables → Actions**
4. Klicka **New repository secret**
5. **Name:** `GMAIL_SERVICE_ACCOUNT_JSON`
6. **Value:** Paste hela JSON-innehållet
7. Klicka **Add secret**

## 7. Verify Setup

JSON-filen bör innehålla detta format:
```json
{
  "type": "service_account",
  "project_id": "brut-natur-daily-xxx",
  "private_key_id": "xxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "brut-natur-daily@project-id.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/..."
}
```

## Nästa steg

1. Lägg in JSON i GitHub Secret `GMAIL_SERVICE_ACCOUNT_JSON`
2. Python-scriptet använder det automatiskt
3. GitHub Actions skickar email direkt nästa gång det körs

---

**Support:** Om något går fel, kontrollera:
- ✓ Gmail API är enabled
- ✓ Service account är skapad
- ✓ JSON är korrekt formaterad
- ✓ Service account har gmail.send permission
