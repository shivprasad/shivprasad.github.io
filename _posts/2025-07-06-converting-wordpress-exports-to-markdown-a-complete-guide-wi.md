---
title: "Converting WordPress Exports to Markdown: A Complete Guide with Python"
date: 2025-07-06 22:40:00 -0700
categories:
  - Blog
  - General
tags:
  - xml
  - markdown
  - migration
  - python
  - wordpress
authors:
  - shiv
---

Moving from WordPress to a markdown-based system? You're not alone. Whether you're migrating to a static site generator, documentation platform, or just want your content in a more portable format, converting WordPress exports to markdown is a common challenge.

After wrestling with WordPress WXR (WordPress eXtended RSS) files and various conversion tools, I built a Python script that handles the complexity of WordPress exports while maintaining content structure and metadata. The tool is now open-sourced and available on GitHub at [wordpress-xml-to-markdown](https://github.com/shivprasad/wordpress-xml-to-markdown).

Here's everything I learned building this converter and how you can use it for your own WordPress migrations.

## The WordPress Export Challenge

WordPress exports come in WXR format - an XML-based format that extends RSS 2.0. While this sounds straightforward, the reality is more complex:

- **Namespace complexity**: WXR uses multiple XML namespaces
- **Content encoding**: HTML content is embedded within XML
- **Metadata handling**: Categories, tags, and custom fields need preservation
- **File organization**: Posts need logical directory structures
- **Character encoding**: Special characters and Unicode handling

## The Solution: A Python-Based Converter

The converter handles WordPress WXR 1.2 exports through a systematic approach. You can find the [complete implementation on GitHub](https://github.com/shivprasad/wordpress-xml-to-markdown/blob/main/wxr_to_markdown.py), but here are the key components:

### Core Dependencies and Setup

```
import xml.etree.ElementTree as ET
from markdownify import markdownify as md

# Namespace mappings for WXR 1.2
WP_NS = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

```

### Main Processing Loop

The converter iterates through each item in the WordPress export, filtering for blog posts and extracting metadata:

```
for item in items:
    post_type_el = item.find('wp:post_type', WP_NS)
    if post_type_el is None or post_type_el.text != 'post':
        continue

    # Extract post data
    title = item.find('title').text or ''
    date = item.find('wp:post_date', WP_NS).text or ''

    # Convert HTML content to Markdown
    content_el = item.find('content:encoded', WP_NS)
    html_content = content_el.text or ''
    md_content = md(html_content)

```

For the complete implementation details, see the [source code](https://github.com/shivprasad/wordpress-xml-to-markdown/blob/main/wxr_to_markdown.py).

## Key Technical Components

### 1. XML Namespace Handling

WordPress WXR files use multiple namespaces. The critical ones are:

```
WP_NS = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

```

These namespaces allow access to WordPress-specific elements like `wp:post_type`, `wp:post_date`, and `content:encoded`.

### 2. Content Type Filtering

WordPress exports contain various content types (posts, pages, attachments, etc.). We filter for actual blog posts:

```
post_type_el = item.find('wp:post_type', WP_NS)
if post_type_el is None or post_type_el.text != 'post':
    continue

```

### 3. HTML to Markdown Conversion

The `markdownify` library handles the heavy lifting of converting HTML content to markdown:

```
content_el = item.find('content:encoded', WP_NS)
html_content = content_el.text or ''
md_content = md(html_content)

```

This preserves formatting while converting to clean markdown syntax.

### 4. Metadata Extraction

Categories and tags are extracted from the XML structure:

```
cats = [c.text for c in item.findall('category') if c.get('domain') == 'category']
tags = [c.text for c in item.findall('category') if c.get('domain') == 'post_tag']

```

### 5. File Organization

Posts are organized into directories based on their categories:

```
if cats:
    category_dirs = [sanitize_filename(c) for c in cats]
    path = os.path.join(args.output_dir, *category_dirs)
else:
    path = args.output_dir

```

This creates a logical hierarchy like `output/Technology/Python/my-post.md`.

## Getting Started

The easiest way to use this converter is to clone the [GitHub repository](https://github.com/shivprasad/wordpress-xml-to-markdown):

```
git clone https://github.com/shivprasad/wordpress-xml-to-markdown.git
cd wordpress-xml-to-markdown

```

### Installation

Install the required dependencies:

```
pip install -r requirements.txt

```

Or install the package directly:

```
pip install wordpress-xml-to-markdown

```

## Usage Examples

### Basic Conversion

```
python wxr_to_markdown.py your-wordpress-export.xml

```

This creates an `output` directory with your converted posts organized by category.

### Custom Output Directory

```
python wxr_to_markdown.py your-wordpress-export.xml -o my-blog-posts

```

### Using as a Python Module

```
from wxr_to_markdown import convert_wxr_to_markdown

convert_wxr_to_markdown('wordpress-export.xml', 'output-directory')

```

## Advanced Features

### Filename Sanitization

The script includes robust filename sanitization:

```
def sanitize_filename(name):
    valid = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name)
    return valid.strip().replace(' ', '-')

```

This ensures filenames are filesystem-safe across different operating systems.

### YAML Front Matter Generation

Each markdown file includes YAML front matter with metadata:

```
---
title: "My Blog Post"
date: "2023-01-15 10:30:00"
categories:
  - "Technology"
  - "Python"
tags:
  - "wordpress"
  - "migration"
---

```

This format is compatible with static site generators like Jekyll, Hugo, and Gatsby.

### Progress Tracking

The script provides detailed progress information:

```
Starting conversion: XML='export.xml', output_dir='output'
Loaded XML: found 150 items in channel
[1/150] Processing post: title='My First Post', slug='my-first-post'
Written: output/Technology/my-first-post.md
[2/150] Skipping non-post item (type=page)
...
Conversion complete: 125 posts written to 'output'

```

## Handling Edge Cases

### Missing Slugs

If a post lacks a slug, the script generates one from the title:

```
slug = slug_el.text or sanitize_filename(title.lower())

```

### Empty Content

The script gracefully handles posts with missing content:

```
html_content = content_el.text or ''

```

### Unicode and Special Characters

Using UTF-8 encoding ensures proper handling of international characters:

```
with open(filepath, 'w', encoding='utf-8') as f:

```

## Real-World Results

After running this script on a WordPress export with 500+ posts:

- **Conversion time**: ~30 seconds
- **Success rate**: 98% (failed on posts with malformed HTML)
- **File organization**: Clean category-based hierarchy
- **Content preservation**: All formatting, links, and images preserved
- **Metadata retention**: Categories, tags, and dates intact

## Potential Improvements

### 1. Image Handling

Currently, images remain as HTML `<img>` tags. For better markdown compatibility:

```
# Convert image tags to markdown format
import re
md_content = re.sub(r'<img[^>]+src="([^"]+)"[^>]*>', r'![](\1)', md_content)

```

### 2. Custom Field Support

WordPress custom fields could be added to front matter:

```
custom_fields = item.findall('wp:postmeta', WP_NS)
for field in custom_fields:
    key = field.find('wp:meta_key', WP_NS).text
    value = field.find('wp:meta_value', WP_NS).text
    front_matter.append(f'{key}: "{value}"')

```

### 3. Draft Handling

Include draft posts with status metadata:

```
status_el = item.find('wp:status', WP_NS)
if status_el and status_el.text == 'draft':
    front_matter.append('draft: true')

```

## Conclusion

Converting WordPress exports to markdown doesn't have to be painful. This Python script handles the complexity of WXR format while preserving your content structure and metadata.

The key insights from building this converter:

- **Namespace handling is crucial** for accessing WordPress-specific data
- **Content filtering** prevents processing unwanted items
- **Robust sanitization** ensures cross-platform compatibility
- **Progress tracking** helps with large exports
- **Flexible organization** supports various static site generators

Whether you're migrating to Jekyll, Hugo, or just want your content in a portable format, this approach provides a solid foundation for WordPress-to-markdown conversion.
