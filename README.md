# Minimalist Tattoo Artist Portfolio

A clean, elegant portfolio website for tattoo artists built with Flask.

## Features

- **Homepage** with hero image and artist introduction
- **Portfolio Gallery** with masonry-style layout and lightbox
- **About Page** with artist bio and portrait
- **Contact Page** with contact information
- Mobile-first responsive design
- Custom lightbox with keyboard navigation
- No external JavaScript/CSS frameworks

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
├── app.py                  # Flask application
├── gallery_data.py         # Portfolio image configuration
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/styles.css      # Stylesheet
│   ├── js/lightbox.js      # Lightbox functionality
│   ├── portfolio/          # Tattoo images
│   └── images/             # Site images (hero, portrait)
└── templates/
    ├── base.html           # Base template
    ├── home.html           # Homepage
    ├── portfolio.html      # Gallery page
    ├── about.html          # About page
    └── contact.html        # Contact page
```

## Customization

### Adding Portfolio Images

1. Add images to `static/portfolio/`
2. Edit `gallery_data.py`:

```python
PORTFOLIO_IMAGES = [
    {"filename": "new-image.jpg", "title": "Image Title"},
]
```

### Updating Content

Edit the configuration in `app.py`:

- `SITE_CONFIG` - Site name, tagline, hero image
- `ARTIST` - Name, bio, portrait
- `CONTACT` - Email, Instagram, location, hours

## Documentation

See `specs/001-tattoo-portfolio/quickstart.md` for detailed setup and customization instructions.

## License

All rights reserved.
