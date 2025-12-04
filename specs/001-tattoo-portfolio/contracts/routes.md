# Route Contracts: Minimalist Tattoo Artist Portfolio Website

**Feature Branch**: `001-tattoo-portfolio`
**Date**: 2025-12-04

## Overview

This document defines the HTTP routes for the Flask application. All routes return server-rendered HTML using Jinja2 templates.

## Routes

### GET /

**Description**: Homepage with hero image and artist introduction

**Template**: `home.html`

**Context Data**:
```python
{
    "site_name": str,      # From SiteConfig
    "tagline": str,        # From SiteConfig
    "hero_image": str,     # Filename for hero section
    "artist_intro": str,   # Short introduction text
    "current_page": "home" # For nav active state
}
```

**Response**: 200 OK with HTML content

**Behavior**:
- Displays hero section with featured tattoo image
- Shows brief artist introduction (1-2 sentences)
- Provides clear CTA to Portfolio page
- Navigation header shows "Home" as active

---

### GET /portfolio

**Description**: Gallery page with all portfolio images

**Template**: `portfolio.html`

**Context Data**:
```python
{
    "site_name": str,
    "images": list[dict],  # List of PortfolioImage objects from gallery_data
    "current_page": "portfolio"
}
```

**Response**: 200 OK with HTML content

**Behavior**:
- Displays masonry/grid layout of all portfolio images
- Each image is clickable (triggers lightbox via JavaScript)
- Images include title as alt text and data attribute
- If `images` list is empty, displays "Portfolio coming soon" message
- Navigation header shows "Portfolio" as active

**Image Data Structure** (each item in `images`):
```python
{
    "filename": str,  # e.g., "tattoo1.jpg"
    "title": str      # e.g., "Floral Arm Piece"
}
```

---

### GET /about

**Description**: Artist biography and portrait page

**Template**: `about.html`

**Context Data**:
```python
{
    "site_name": str,
    "artist_name": str,    # From ArtistProfile
    "artist_bio": str,     # From ArtistProfile (may contain HTML)
    "artist_portrait": str, # Portrait image filename
    "current_page": "about"
}
```

**Response**: 200 OK with HTML content

**Behavior**:
- Displays artist portrait image
- Shows biography text alongside/below portrait
- Responsive layout (side-by-side on desktop, stacked on mobile)
- Navigation header shows "About" as active

---

### GET /contact

**Description**: Contact information page

**Template**: `contact.html`

**Context Data**:
```python
{
    "site_name": str,
    "contact_email": str,   # From ContactInfo
    "contact_instagram": str | None,
    "contact_location": str | None,
    "contact_hours": str | None,
    "current_page": "contact"
}
```

**Response**: 200 OK with HTML content

**Behavior**:
- Displays contact email (as clickable mailto: link)
- Shows Instagram link if provided
- Shows location and hours if provided
- Navigation header shows "Contact" as active
- Placeholder comment for future contact form integration

---

## Static Files

### GET /static/<path:filename>

**Description**: Flask's built-in static file serving

**Paths**:
- `/static/css/styles.css` - Main stylesheet
- `/static/js/lightbox.js` - Lightbox JavaScript
- `/static/portfolio/<filename>` - Portfolio images
- `/static/images/<filename>` - Site images (hero, portrait)

**Response**: 200 OK with appropriate content type, or 404 if not found

---

## Error Handling

### 404 Not Found

**Template**: `base.html` with error content (or custom 404.html if created)

**Behavior**:
- Display friendly "Page not found" message
- Include navigation to return to home
- Maintain site styling

---

## Route Summary Table

| Method | Path | Template | Description |
|--------|------|----------|-------------|
| GET | / | home.html | Homepage with hero |
| GET | /portfolio | portfolio.html | Image gallery |
| GET | /about | about.html | Artist bio |
| GET | /contact | contact.html | Contact info |
| GET | /static/* | - | Static files |

---

## Future Routes (TODO placeholders)

These routes are not implemented in v1 but structure supports addition:

| Method | Path | Purpose |
|--------|------|---------|
| GET | /blog | Blog listing page |
| GET | /blog/<slug> | Individual blog post |
| GET | /booking | Booking calendar page |
| POST | /booking | Submit booking request |
| GET | /aftercare | Aftercare information |
| GET | /flash | Flash designs gallery |
| GET | /api/images | JSON API for images (for future JS filtering) |
