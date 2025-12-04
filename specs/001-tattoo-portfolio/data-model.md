# Data Model: Minimalist Tattoo Artist Portfolio Website

**Feature Branch**: `001-tattoo-portfolio`
**Date**: 2025-12-04

## Overview

This is a simple portfolio website with file-based storage. No database is required. Data is managed through Python data structures and static files.

## Entities

### PortfolioImage

Represents a single tattoo artwork in the portfolio gallery.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| filename | string | Yes | Image filename in `/static/portfolio/` directory |
| title | string | Yes | Display title for the artwork (shown in lightbox) |
| category | string | No | Future: Category tag (e.g., "floral", "blackwork", "geometric") |
| description | string | No | Future: Extended description for SEO/accessibility |
| date | string | No | Future: Date of creation (YYYY-MM format) |
| featured | boolean | No | Future: Flag for homepage featured images |

**Storage**: Python list of dictionaries in `gallery_data.py`

**Example**:
```python
{
    "filename": "floral-arm-01.jpg",
    "title": "Floral Arm Piece"
}
```

**Validation Rules**:
- `filename` must reference an existing file in `/static/portfolio/`
- `title` should be non-empty, max 100 characters
- Image files should be JPG/PNG, recommended max 2000px width

### ArtistProfile

Represents the tattoo artist's information displayed on the About page.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Artist's display name |
| bio | string | Yes | Biography text (HTML allowed for formatting) |
| portrait | string | Yes | Filename of portrait image in `/static/images/` |

**Storage**: Defined as constants in `app.py` or separate `artist_data.py`

**Example**:
```python
ARTIST = {
    "name": "Artist Name",
    "bio": "A passionate tattoo artist specializing in...",
    "portrait": "artist-portrait.jpg"
}
```

### ContactInfo

Represents contact information displayed on the Contact page.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Contact email address |
| instagram | string | No | Instagram handle (without @) |
| location | string | No | Studio location/city |
| hours | string | No | Working hours description |

**Storage**: Defined as constants in `app.py` or `contact_data.py`

**Example**:
```python
CONTACT = {
    "email": "artist@example.com",
    "instagram": "artisthandle",
    "location": "Stockholm, Sweden",
    "hours": "By appointment only"
}
```

### SiteConfig

Represents site-wide configuration.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| site_name | string | Yes | Website title |
| tagline | string | No | Short site description |
| hero_image | string | Yes | Filename for homepage hero image |

**Storage**: Defined as constants in `app.py`

## Relationships

```
SiteConfig (1) ─────── (1) Homepage
     │
     └── hero_image ──── references ──── static/images/

ArtistProfile (1) ──── (1) About Page
     │
     └── portrait ────── references ──── static/images/

ContactInfo (1) ────── (1) Contact Page

PortfolioImage (many) ─ (1) Portfolio Page
     │
     └── filename ────── references ──── static/portfolio/
```

## State Transitions

This application has no stateful data - all content is read-only. No state transitions apply.

## Future Extensibility

The data model is designed for easy extension:

1. **Categories/Tags**: Add `category` field to PortfolioImage, create category filter UI
2. **Multiple Galleries**: Add `gallery` field to PortfolioImage (e.g., "portfolio", "flash", "healed")
3. **Blog Posts**: New `BlogPost` entity with title, content, date, slug
4. **Booking System**: New `Appointment` entity with date, client info, status
5. **Admin Upload**: Migrate from Python file to database (SQLite → PostgreSQL)

## File Storage Structure

```
static/
├── portfolio/              # Tattoo artwork images
│   ├── tattoo1.jpg
│   ├── tattoo2.jpg
│   └── ...
├── images/                 # Site images
│   ├── hero.jpg           # Homepage hero
│   ├── artist-portrait.jpg # About page portrait
│   └── ...
├── css/
│   └── styles.css
└── js/
    └── lightbox.js
```

## Image Requirements

| Image Type | Recommended Size | Format | Notes |
|------------|------------------|--------|-------|
| Portfolio images | 1200-2000px width | JPG | Optimize for web (<500KB) |
| Hero image | 1920px width | JPG | Can be larger for retina |
| Artist portrait | 800px width | JPG/PNG | Square or 4:3 ratio |
