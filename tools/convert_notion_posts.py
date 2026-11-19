#!/usr/bin/env python3
"""Convert Notion-exported blog posts into Jekyll/Chirpy posts.

Usage:
    python tools/convert_notion_posts.py --dry-run
    python tools/convert_notion_posts.py --sample 5
    python tools/convert_notion_posts.py --all
"""

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Tuple

# Root of the Jekyll repo
REPO_ROOT = Path(__file__).resolve().parent.parent

# Notion export location
NOTION_DIR = Path(
    "/Volumes/DAKOO/scratchpad/notion-backup/Life is but a dream/Blog Posts"
)

# Jekyll posts output
POSTS_DIR = REPO_ROOT / "_posts"

# Map timezone abbreviations seen in Notion exports to fixed offsets.
TZ_ABBREVIATIONS = {
    "PST": timezone(timedelta(hours=-8)),
    "PDT": timezone(timedelta(hours=-7)),
    "GMT": timezone.utc,
    "UTC": timezone.utc,
    "EST": timezone(timedelta(hours=-5)),
    "EDT": timezone(timedelta(hours=-4)),
    "CST": timezone(timedelta(hours=-6)),
    "CDT": timezone(timedelta(hours=-5)),
    "MST": timezone(timedelta(hours=-7)),
    "MDT": timezone(timedelta(hours=-6)),
}

# Keyword -> [Category, Sub-category]
TAG_TO_CATEGORY = {
    # Distributed / backend
    "distributed": ("Tech", "Distributed Systems"),
    "eventual consistency": ("Tech", "Distributed Systems"),
    "microservices": ("Tech", "Microservices"),
    "hystrix": ("Tech", "Microservices"),
    "circuit breaker": ("Tech", "Microservices"),
    "resilience": ("Tech", "Microservices"),
    "queues": ("Tech", "Backend"),
    "idempotency": ("Tech", "Backend"),
    "maven": ("Tech", "Java"),
    "java": ("Tech", "Java"),
    "jvm": ("Tech", "Java"),
    "spring": ("Tech", "Java"),
    "ant": ("Tech", "Java"),
    # Containers / infrastructure
    "kubernetes": ("Tech", "Kubernetes"),
    "k8s": ("Tech", "Kubernetes"),
    "docker": ("Tech", "Containers"),
    "terraform": ("Tech", "Infrastructure"),
    # Frontend
    "javascript": ("Tech", "Frontend"),
    "typescript": ("Tech", "Frontend"),
    "react": ("Tech", "Frontend"),
    "react 18": ("Tech", "Frontend"),
    "svelte": ("Tech", "Frontend"),
    "sveltekit": ("Tech", "Frontend"),
    "css": ("Tech", "Frontend"),
    "tailwind": ("Tech", "Frontend"),
    "figma": ("Tech", "Design"),
    # Observability / testing
    "grafana": ("Tech", "Observability"),
    "logging": ("Tech", "Observability"),
    "playwright": ("Tech", "Testing"),
    # Data / AI
    "langchain": ("Tech", "AI"),
    "langgraph": ("Tech", "AI"),
    "ai": ("Tech", "AI"),
}


def slugify(value: str, max_length: int = 60) -> str:
    """Create a URL-safe slug from a title."""
    value = value.lower()
    # Replace any sequence of non-alphanumeric chars with a hyphen
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    # Collapse multiple hyphens
    value = re.sub(r"-+", "-", value)
    return value[:max_length].rstrip("-")


def parse_date(published: str) -> Tuple[datetime, str]:
    """Parse 'April 4, 2017 3:00 AM (PDT)' into an aware datetime."""
    # Capture the timezone abbreviation inside parentheses
    m = re.search(r"\(([A-Z]{2,4})\)\s*$", published.strip())
    tz = timezone.utc
    if m:
        abbr = m.group(1).upper()
        tz = TZ_ABBREVIATIONS.get(abbr, timezone.utc)
        published = published[: m.start()].strip()

    # Parse the date/time part
    for fmt in ("%B %d, %Y %I:%M %p", "%B %d, %Y"):
        try:
            naive = datetime.strptime(published, fmt)
            return naive.replace(tzinfo=tz), abbr if m else "UTC"
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date: {published}")


def infer_categories(tags: list[str], title: str) -> list[str]:
    """Infer Chirpy categories from tags and title."""
    combined = " ".join(tags).lower() + " " + title.lower()
    best_category: Optional[Tuple[str, str]] = None
    # Prefer the longest matching keyword (more specific)
    for keyword, category_pair in TAG_TO_CATEGORY.items():
        if keyword in combined:
            if best_category is None or len(keyword) > len(best_category_match):
                best_category = category_pair
                best_category_match = keyword
    if best_category:
        return list(best_category)
    return ["Blog", "General"]


def parse_post(src_path: Path) -> dict:
    """Read a Notion markdown file and extract metadata + body."""
    text = src_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    title: Optional[str] = None
    meta: dict[str, str] = {}

    # First non-empty line should be the H1 title
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        i += 1

    # Skip optional blank line(s) after the title
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    # Collect metadata lines until the next blank line
    while i < len(lines) and lines[i].strip() != "":
        line = lines[i]
        # Metadata line looks like "Key: value"
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip().lower()] = value.strip()
        i += 1

    # Skip blank lines before body
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    body_lines = lines[i:]

    # Remove duplicate H1 title from body if it matches
    if body_lines and body_lines[0].startswith("# ") and title:
        body_title = body_lines[0][2:].strip().rstrip(":")
        if body_title.lower().replace(":", "") == title.lower().replace(":", ""):
            body_lines = body_lines[1:]
            while body_lines and body_lines[0].strip() == "":
                body_lines = body_lines[1:]

    body = "\n".join(body_lines).strip()

    return {
        "title": title or src_path.stem.split(maxsplit=1)[0],
        "author": meta.get("author"),
        "tags_raw": meta.get("tags", ""),
        "published_raw": meta.get("published", ""),
        "featured": meta.get("featured", "No"),
        "body": body,
    }


def normalize_tag(tag: str) -> str:
    return tag.strip().lower().replace(" ", "-")


def convert_post(src_path: Path, dry_run: bool = False) -> Optional[Path]:
    data = parse_post(src_path)

    if not data["published_raw"]:
        print(f"⚠️  Skipping {src_path.name} — no published date", file=sys.stderr)
        return None

    dt, tz_abbr = parse_date(data["published_raw"])
    date_only = dt.strftime("%Y-%m-%d")
    date_full = dt.strftime("%Y-%m-%d %H:%M:%S %z")

    slug = slugify(data["title"])
    file_name = f"{date_only}-{slug}.md"
    dest = POSTS_DIR / file_name

    tags = [t.strip() for t in data["tags_raw"].split(",") if t.strip()]
    categories = infer_categories(tags, data["title"])

    front_matter = {
        "title": data["title"],
        "date": date_full,
        "categories": categories,
        "tags": [normalize_tag(t) for t in tags],
    }
    if data["author"]:
        front_matter["author"] = data["author"]
    if data["featured"].lower() == "yes":
        front_matter["pin"] = True

    fm_lines = ["---"]
    for key, value in front_matter.items():
        if isinstance(value, list):
            fm_lines.append(f"{key}:")
            for item in value:
                fm_lines.append(f"  - {item}")
        else:
            if isinstance(value, bool):
                fm_lines.append(f"{key}: {str(value).lower()}")
            elif key == "date":
                fm_lines.append(f"{key}: {value}")
            else:
                fm_lines.append(f'{key}: "{value}"')
    fm_lines.append("---")

    output = "\n".join(fm_lines) + "\n\n" + data["body"] + "\n"

    if dry_run:
        print(f"Would create: {dest.relative_to(REPO_ROOT)}")
        print(f"  title: {data['title']}")
        print(f"  date:  {date_full}")
        print(f"  categories: {categories}")
        print(f"  tags: {[normalize_tag(t) for t in tags]}")
        print()
        return dest

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    dest.write_text(output, encoding="utf-8")
    print(f"Created: {dest.relative_to(REPO_ROOT)}")
    return dest


def list_notion_posts(source_dir: Path) -> list[Path]:
    return sorted([p for p in source_dir.glob("*.md") if p.is_file()])


def main():
    parser = argparse.ArgumentParser(
        description="Convert Notion blog posts to Jekyll/Chirpy posts."
    )
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--sample", type=int, default=0, help="Convert this many random posts")
    parser.add_argument("--all", action="store_true", help="Convert every post")
    parser.add_argument(
        "--source",
        type=Path,
        default=NOTION_DIR,
        help="Directory containing Notion markdown exports",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific Notion markdown files to convert (overrides --sample/--all)",
    )
    args = parser.parse_args()

    posts = list_notion_posts(args.source)

    if not posts:
        print(f"No .md files found in {args.source}")
        sys.exit(1)

    print(f"Found {len(posts)} Notion posts.\n")

    if args.files:
        selected = [Path(f) for f in args.files]
    elif args.sample:
        import random

        # Only sample posts that actually have a publish date
        parseable = [p for p in posts if parse_post(p)["published_raw"]]
        if len(parseable) < args.sample:
            print(
                f"Only {len(parseable)} posts have publish dates; using all of them.",
                file=sys.stderr,
            )
        selected = random.sample(parseable, min(args.sample, len(parseable)))
    elif args.all:
        selected = posts
    else:
        print("Use --dry-run, --sample N, or --all")
        sys.exit(1)

    for src in selected:
        convert_post(src, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
