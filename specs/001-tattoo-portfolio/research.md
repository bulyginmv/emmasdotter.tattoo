# Research: Minimalist Tattoo Artist Portfolio Website

**Feature Branch**: `001-tattoo-portfolio`
**Date**: 2025-12-04

## Technology Decisions

### Flask Framework Selection

**Decision**: Flask 3.x with Jinja2 templating

**Rationale**:
- Lightweight and minimal - perfect for a simple portfolio site
- Jinja2 template inheritance enables DRY base layout
- No ORM needed since we're using file-based storage
- Easy deployment on any Python-capable hosting
- Extensive documentation and community support

**Alternatives Considered**:
- Django: Too heavyweight for 4-page static site, brings unnecessary complexity (admin, ORM, migrations)
- FastAPI: Designed for APIs, not server-rendered HTML sites
- Static site generators (Hugo, Jekyll): Would require additional tooling, less flexible for future dynamic features

### CSS Masonry Layout Approach

**Decision**: CSS Grid with auto-placement for masonry-like effect

**Rationale**:
- Native CSS solution - no JavaScript required for layout
- `grid-template-columns: repeat(auto-fill, minmax(250px, 1fr))` handles responsive columns
- Works without JavaScript (graceful degradation requirement)
- Simpler than true masonry (which requires JS for optimal packing)
- Sufficient for portfolio presentation - images don't need pixel-perfect masonry

**Alternatives Considered**:
- CSS Columns: Creates vertical flow (top-to-bottom) which is less intuitive for portfolio viewing
- JavaScript Masonry.js: Adds dependency, fails without JS
- CSS native masonry (grid-template-rows: masonry): Not yet widely supported

### Lightbox Implementation

**Decision**: Custom vanilla JavaScript lightbox

**Rationale**:
- No external dependencies - keeps bundle lightweight
- Full control over styling to match minimalist aesthetic
- Estimated ~100 lines of JS
- Keyboard navigation (Escape to close) easy to implement
- Touch-friendly close interactions achievable

**Alternatives Considered**:
- Lightbox2, GLightbox, etc.: External dependencies, often over-featured for this use case
- CSS-only lightbox: Limited functionality, poor UX (no keyboard support)
- Fancybox: jQuery dependency, too heavy

### Color Scheme

**Decision**: Light neutral theme with high contrast for images

**Rationale**:
- Matches minimalist portfolio aesthetic (reference sites use light themes)
- White/off-white backgrounds let tattoo artwork stand out
- Neutral grays for text and UI elements
- Black/dark accents for emphasis
- High contrast improves accessibility

**Color Palette**:
- Background: `#fafafa` (off-white)
- Primary text: `#1a1a1a` (near-black)
- Secondary text: `#666666` (medium gray)
- Accent/links: `#333333` (dark gray)
- Borders/dividers: `#e0e0e0` (light gray)
- Lightbox overlay: `rgba(0, 0, 0, 0.9)`

### Typography

**Decision**: System font stack with elegant fallbacks

**Rationale**:
- No external font loading - faster initial paint
- System fonts are well-optimized for each platform
- Maintains minimalist approach
- Accessibility-friendly with good default sizing

**Font Stack**:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
             'Helvetica Neue', Arial, sans-serif;
```

### Image Handling Strategy

**Decision**: Store images in `/static/portfolio/` with gallery metadata in Python file

**Rationale**:
- Simple file-based approach aligns with project simplicity
- `gallery_data.py` acts as single source of truth for image metadata
- Easy for non-technical user to add images (copy file + add dict entry)
- No database overhead
- Can be migrated to database later if needed

**Structure**:
```python
# gallery_data.py
PORTFOLIO_IMAGES = [
    {"filename": "tattoo1.jpg", "title": "Floral Arm Piece"},
    {"filename": "tattoo2.jpg", "title": "Blackwork Mandala"},
    # Future extensibility:
    # {"filename": "x.jpg", "title": "Y", "category": "floral", "date": "2024-01"}
]
```

## Best Practices Applied

### Mobile-First Responsive Design

- Base styles target mobile (320px+)
- Media queries add complexity for larger screens
- Touch-friendly tap targets (minimum 44x44px)
- Responsive images with proper sizing

### Accessibility Considerations

- Semantic HTML5 elements (`<nav>`, `<main>`, `<article>`, `<footer>`)
- Alt text for all images (using title field)
- Keyboard navigation support in lightbox
- Sufficient color contrast (WCAG AA)
- Focus indicators on interactive elements

### Progressive Enhancement

- Site fully functional without JavaScript
- Lightbox enhances but doesn't gate content
- CSS Grid degrades gracefully to simpler layouts
- No critical functionality depends on JavaScript

### Performance Optimization

- No external CSS/JS frameworks
- System fonts (no font loading)
- Lazy loading for portfolio images
- Minimal HTTP requests
- Image optimization recommendations in quickstart

## Resolved Clarifications

All technical decisions resolved. No blocking clarifications remain.

| Area | Resolution |
|------|------------|
| Layout approach | CSS Grid (not masonry.js) |
| Lightbox | Custom vanilla JS |
| Color theme | Light neutral |
| Font loading | System fonts |
| Image storage | File-based with Python metadata |
