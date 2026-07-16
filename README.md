# LikePion Backlink Playbook

A clean public playbook for preparing backlink campaign data for LikePion-style workflows.

This repo is designed for SEO operators who need a repeatable way to turn a target URL, keyword set, and business entity information into structured inputs for:

- Podcast Backlink
- Blog20 Backlink
- Google Stacking
- Profile Backlink

The templates focus on consistent NAP data, short usernames, keyword coverage, and Spintax-ready descriptions.

## What This Is For

Use this when you need to brief another AI assistant, VA, SEO teammate, or internal operator on how to prepare backlink campaign inputs without re-explaining the rules every time.

Good fit:

- Local SEO campaigns
- Entity-building campaigns
- Branded profile creation
- Google Stacking preparation
- Podcast/profile backlink data preparation

Not a fit:

- Hiding ownership or impersonating unrelated brands
- Publishing false business information
- Mass spam campaigns on irrelevant sites
- Storing passwords, 2FA seeds, or app passwords in this repo

## Core Rules

1. Username must be under 13 characters.
2. Profile Backlink v1.0.2 requires one plain username; use Username Spintax only where the current module accepts it.
3. Use Spintax for titles and About fields.
4. Keep NAP data consistent across tabs: business name, phone, address, city.
5. Include all target keywords naturally across the About fields.
6. Keep public examples generic. Do not commit real credentials.
7. For local SEO, include city, nearby suburbs, map/search intent, and service relevance.

## Points Calculator

LikePion v1.0.2 completed transactions show this planning formula:

```text
planned charge = requested quantity * bidding
remaining = available points - planned charge
maximum request = floor(available points / bidding)
available points = deposited points - used points
```

Observed examples:

- Podcast: 200 requested x 45 = 9,000 points
- Profile: 300 requested x 30 = 9,000 points; report returned 279 links
- Profile: 100 requested x 30 = 3,000 points; report returned 114 links
- Blog 2.0: 20 accounts x 50 = 1,000 points
- Google Stacking: 10 links x 30 = 300 points

Do not calculate the rate from the delivered link count shown in the transaction description. Delivered links can differ from the requested limit. Refresh Billings after another campaign runs, and treat a checkout shortfall message as the immediate balance requirement because the app may reserve extra points.

## Quick Start

Copy the sample campaign:

```bash
cp templates/campaign.example.yaml templates/campaign.yaml
```

Edit `templates/campaign.yaml` with your campaign data.

Generate the campaign output:

```bash
python3 scripts/generate_campaign.py templates/campaign.yaml
```

The script prints copy-ready sections for Podcast, Blog20, Google Stacking, and Profile Backlink.

## Files

- `SKILL.md` - installable Codex skill with field rules and points calculator.
- `MASTER_PROMPT.md` - one prompt to teach another AI how to generate LikePion campaign data.
- `templates/campaign.example.yaml` - safe example campaign input.
- `scripts/generate_campaign.py` - simple generator for structured campaign output.

## Recommended Workflow

1. Collect URL, brand, city, phone, address, and keyword list.
2. Fill in `templates/campaign.yaml`.
3. Run the generator.
4. Review keyword usage and NAP consistency.
5. Paste each section into the matching LikePion tab.
6. Keep credentials outside Git and outside public docs.

## Public Repo Safety

Before pushing anything public, check:

```bash
git status --short
rg -n "password|app password|2fa|secret|token|api[_-]?key|gho_|sk-" .
```

Never commit customer credentials, private emails, API keys, or 2FA recovery data.
