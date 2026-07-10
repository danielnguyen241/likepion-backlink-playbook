#!/usr/bin/env python3
"""Generate LikePion-style backlink campaign fields from a YAML file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def spintax(options: list[str]) -> str:
    clean = [str(option).strip() for option in options if str(option).strip()]
    return "{" + "|".join(clean) + "}"


def compact_phone(phone: str) -> str:
    return re.sub(r"[\s().-]+", "", phone.strip())


def validate_usernames(options: list[str]) -> list[str]:
    invalid = [name for name in options if len(name) >= 13]
    if invalid:
        joined = ", ".join(invalid)
        raise ValueError(f"Username options must be under 13 characters: {joined}")
    return options


def keyword_spin(keywords: list[str]) -> str:
    if not keywords:
        return "{SEO services|digital visibility|search growth}"
    return spintax(keywords)


def render(data: dict) -> str:
    brand = data["brand"]
    target_url = data["target_url"]
    city = data["city"]
    phone = compact_phone(data["phone"])
    address = data["address"]
    service = data.get("service", "SEO")
    keywords = data.get("keywords", [])
    areas = data.get("areas", [city])
    username_options = validate_usernames(data.get("username_options", []))
    usernames = spintax(username_options)
    kw = keyword_spin(keywords)
    area_spin = spintax(areas)
    social = data.get("social_links", {}) or {}
    title_keywords = keywords[:3] or [f"{service} {city}", f"{city} {service}", "search visibility"]

    title_spin = spintax(
        [
            f"{brand} - {service} in {city}",
            f"Trusted {service} Services {city}",
            f"{brand} {city} Search Visibility",
            f"{title_keywords[0]} by {brand}",
            f"{title_keywords[1]} Experts",
            f"{title_keywords[2]} Campaign",
        ]
    )

    podcast_about = (
        f"{{{brand} helps businesses grow with|Improve local visibility with|Build search demand through}} "
        f"{kw}. We support companies across {area_spin} with practical {service} work, entity signals, "
        f"Google Maps visibility, citation consistency, and conversion-focused organic growth."
    )

    google_about = (
        f"{{{brand} is a trusted provider of|Choose {brand} for|Work with {brand} on}} {kw}. "
        f"{{Our team helps brands in {city} strengthen their local entity footprint|We improve visibility "
        f"across maps, profiles, and search results|We connect brand, location, and service relevance}} "
        f"for customers in {area_spin}."
    )

    profile_about = (
        f"{{{brand} provides|The {brand} team delivers|Partner with {brand} for}} {kw}. "
        f"{{We focus on consistent local signals, useful content, and sustainable visibility|Our process "
        f"connects business data, profiles, and location relevance|We help local customers discover the right service faster}}."
    )

    return f"""# LikePion Backlink Campaign

## 1. Podcast Backlink

Target:
- Link SEO: {target_url}

Register:
- System automatically handles account registration.

Config:
- Link Limit: 200
- Bidding: 45

Content:
- Phone: {phone}
- Username: {usernames}
- Address: {address}
- About: {podcast_about}
- Avatar: Square brand logo or clean brand profile image.

## 2. Blog20 Backlink

Register:
- Name group: provided by operator
- Title: {title_spin}
- Username: {usernames}
- 2FA: provided by operator
- Email: provided by operator
- App Password: provided by operator
- Pass email project: provided by operator
- Website: {target_url}

Config:
- Link Limit: 0
- Bidding: 50

Content:
- About: {profile_about}
- Avatar: Square brand logo or clean profile image.

## 3. Google Stacking

Target:
- Website: {target_url}

Config:
- Bidding: 30
- Duplicate: 0
- Entity Connect: All

Content:
- Title: {title_spin}
- City: {city}
- Phone: {phone}
- Address: {address}
- About, Always Spin ON: {google_about}
- Cover: Clean city/service-themed cover image with data/network overlays. Avoid text, fake logos, and distorted branding.

## 4. Profile Backlink

Target:
- Link SEO: {target_url}
- Delete report: OFF

Register:
- Email Usage: Many
- Username: {usernames}
- Entity Email: provided by operator
- App Password: provided by operator

Config:
- Create Account Social: OFF unless account creation is requested
- Link Limit: 400
- Bidding: 30
- Entity Connect: All

Content:
- First Name: {{Alex|Sam|Taylor|Jordan}}
- Last Name: {{Smith|Nguyen|Brown|Lee}}
- City: {city}
- Phone: {phone}
- Address: {address}
- About, Always Spin ON: {profile_about}
- Twitter: {social.get("twitter") or "optional"}
- Facebook: {social.get("facebook") or "optional"}
- LinkedIn: {social.get("linkedin") or "optional"}
- YouTube: {social.get("youtube") or "optional"}
"""


def parse_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_simple_yaml(path: Path) -> dict:
    """Load the small YAML subset used by templates/campaign.example.yaml."""
    data: dict = {}
    current_key: str | None = None
    current_nested: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0 and ":" in line:
            key, raw_value = line.split(":", 1)
            current_key = key.strip()
            current_nested = None
            if raw_value.strip():
                data[current_key] = parse_value(raw_value)
            else:
                data[current_key] = {}
            continue

        if indent == 2 and line.startswith("- "):
            if current_key is None:
                raise ValueError(f"List item found without parent key: {line}")
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(parse_value(line[2:]))
            continue

        if indent == 2 and ":" in line:
            if current_key is None:
                raise ValueError(f"Nested key found without parent key: {line}")
            if not isinstance(data.get(current_key), dict):
                data[current_key] = {}
            nested_key, raw_value = line.split(":", 1)
            current_nested = nested_key.strip()
            data[current_key][current_nested] = parse_value(raw_value) if raw_value.strip() else None
            continue

        if indent == 4 and line.startswith("- "):
            if current_key is None or current_nested is None:
                raise ValueError(f"Nested list item found without parent key: {line}")
            nested = data[current_key].setdefault(current_nested, [])
            nested.append(parse_value(line[2:]))
            continue

        raise ValueError(f"Unsupported YAML line: {raw_line}")

    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate LikePion backlink campaign fields.")
    parser.add_argument("campaign_yaml", type=Path, help="Path to campaign YAML file.")
    args = parser.parse_args()

    data = load_simple_yaml(args.campaign_yaml)
    print(render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
