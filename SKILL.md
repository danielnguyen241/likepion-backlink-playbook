# LikePion Backlink Playbook

Use this skill when the user asks to prepare, revise, teach, or generate backlink campaign data for LikePion-style workflows, especially Podcast Backlink, Blog20 Backlink, Google Stacking, and Profile Backlink.

## Required Inputs

Collect or infer these fields when available:

- Target URL
- Brand or business name
- City or service area
- Phone
- Address
- Keywords and anchor text
- Optional industry context
- Optional social links

If a required field is missing but the user expects output immediately, make a reasonable placeholder and clearly mark it as needing operator confirmation.

## Strict Rules

1. Usernames must be strictly under 13 characters.
2. Generate usernames as Spintax with 4-5 short options, for example `{brandseo|cityseo|brandloc|seocity}`.
3. Use Spintax for `Username`, `Title`, and `About`.
4. Blend all target keywords naturally. Avoid keyword stuffing.
5. Keep NAP data consistent across every tab: name, address, phone, city.
6. For local SEO, include city, nearby areas, Google Maps intent, search intent, citations, and entity signals where relevant.
7. Never invent or expose credentials. Fields such as 2FA, Email, App Password, Entity Email, or private inbox access must be marked `provided by operator`.
8. Do not recommend impersonation, false business info, or irrelevant spam.

## Output Format

When generating a campaign, return the following four sections.

### 1. Podcast Backlink

- Target -> Link SEO: target URL
- Register: System automatically handles account registration
- Config:
  - Link Limit: `200`
  - Bidding: `45`
- Content:
  - Phone: international format without spaces
  - Username: Spintax under 13 characters per option
  - Address: business address
  - About: Spintax description with keywords
  - Avatar: recommended square brand/profile image

### 2. Blog20 Backlink

- Register:
  - Name group: provided by operator
  - Title: Spintax title
  - Username: Spintax under 13 characters per option
  - 2FA: provided by operator
  - Email: provided by operator
  - App Password: provided by operator
  - Pass email project: provided by operator
  - Website: target URL
- Config:
  - Link Limit: `0`
  - Bidding: `50`
- Content:
  - About: short Spintax description
  - Avatar: recommended profile image

### 3. Google Stacking

- Target -> Website: target URL
- Config:
  - Bidding: `30`
  - Duplicate: `0`
  - Entity Connect: `All`
- Content:
  - Title: Spintax title with keywords
  - City: target city
  - Phone: business phone
  - Address: business address
  - About, Always Spin ON: advanced Spintax entity description
  - Cover: clean cover concept, no broken text, no fake logos

### 4. Profile Backlink

- Target:
  - Link SEO: target URL
  - Delete report: `OFF`
- Register:
  - Email Usage: `Many`
  - Username: Spintax under 13 characters per option
  - Entity Email: provided by operator
  - App Password: provided by operator
- Config:
  - Create Account Social: `OFF` unless operator requests it
  - Link Limit: `400`
  - Bidding: `30`
  - Entity Connect: `All`
- Content:
  - First Name / Last Name: short Spintax names
  - City / Phone / Address: local NAP fields
  - About, Always Spin ON: profile-style Spintax description
  - Twitter / Facebook / LinkedIn / YouTube: optional

## Generator Script

The repo includes a local generator:

```bash
python3 scripts/generate_campaign.py templates/campaign.example.yaml
```

Use this script when the user provides structured campaign YAML or asks to generate reusable files. For normal chat output, follow the format above directly.

## Source Files

- `MASTER_PROMPT.md` contains the full teach-another-AI prompt.
- `README.md` contains operator workflow and public repo safety checks.
- `templates/campaign.example.yaml` contains a safe input example.
- `scripts/generate_campaign.py` generates copy-ready output.
