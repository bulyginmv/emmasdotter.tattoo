# Implementation Plan: Minimalist Tattoo Artist Portfolio Website

**Branch**: `001-tattoo-portfolio` | **Date**: 2025-12-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-tattoo-portfolio/spec.md`

## Summary

Build a minimalist tattoo artist portfolio website using Flask (Python) with Jinja2 templates, vanilla CSS/JavaScript frontend. The site features four pages (Home, Portfolio, About, Contact), a masonry-style gallery with custom lightbox, mobile-first responsive design, and clear extensibility points for future features.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Flask 3.x, Jinja2 (included with Flask)
**Storage**: File-based (static images in `/static/portfolio/`, gallery data in Python module)
**Testing**: pytest, manual browser testing for responsive/visual verification
**Target Platform**: Web (any modern browser), Python WSGI-compatible server
**Project Type**: Web application (Flask monolith - single project with templates)
**Performance Goals**: Initial page load <2s on 3G, lightbox interaction <100ms
**Constraints**: No external JavaScript frameworks, lightweight CSS (<50KB), graceful degradation without JS
**Scale/Scope**: Single artist portfolio, ~50-100 portfolio images, <1000 daily visitors expected

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Note**: Project constitution contains template placeholders (not yet configured). Applying standard best practices:

| Principle | Status | Notes |
|-----------|--------|-------|
| Simplicity | PASS | Single Flask app, no unnecessary abstractions |
| Test Coverage | PASS | Routes testable with pytest, visual testing manual |
| Code Organization | PASS | Clear separation: routes, templates, static assets |
| Documentation | PASS | README with quickstart, code comments for extensibility |
| Maintainability | PASS | Gallery data in single location, template inheritance |

**Gate Status**: PASSED - No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-tattoo-portfolio/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (routes specification)
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
app.py                   # Flask application entry point
gallery_data.py          # Portfolio image data configuration
requirements.txt         # Python dependencies

static/
├── css/
│   └── styles.css       # Main stylesheet (mobile-first)
├── js/
│   └── lightbox.js      # Custom lightbox implementation
├── portfolio/           # Tattoo images directory
│   └── (placeholder images)
└── images/              # Other site images (hero, portrait)

templates/
├── base.html            # Base template with nav/footer
├── home.html            # Homepage with hero section
├── portfolio.html       # Gallery page
├── about.html           # Artist bio page
└── contact.html         # Contact information page

tests/
└── test_routes.py       # Route and template tests
```

**Structure Decision**: Single Flask application structure. This is appropriate for a simple portfolio site with no complex backend logic. All routes in single `app.py`, templates use Jinja2 inheritance from `base.html`, static assets organized by type.

## Complexity Tracking

No violations requiring justification. The implementation follows the simplest possible approach:
- Single Python file for routing
- Separate data file for easy content updates
- No database (file-based storage)
- No JavaScript framework (vanilla JS lightbox)
- No CSS framework (custom minimal CSS)
