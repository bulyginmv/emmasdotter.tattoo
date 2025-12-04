# Quickstart: Minimalist Tattoo Artist Portfolio Website

**Feature Branch**: `001-tattoo-portfolio`
**Date**: 2025-12-04

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## Setup

### 1. Clone and Navigate

```bash
cd christmas-project
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The site will be available at `http://localhost:5000`

## Project Structure

```
christmas-project/
├── app.py                 # Main Flask application
├── gallery_data.py        # Portfolio image configuration
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/styles.css     # Stylesheet
│   ├── js/lightbox.js     # Lightbox functionality
│   ├── portfolio/         # Tattoo images
│   └── images/            # Site images (hero, portrait)
└── templates/
    ├── base.html          # Base template
    ├── home.html          # Homepage
    ├── portfolio.html     # Gallery page
    ├── about.html         # About page
    └── contact.html       # Contact page
```

## Adding New Portfolio Images

1. Add your image file to `static/portfolio/` directory
2. Edit `gallery_data.py` and add an entry:

```python
PORTFOLIO_IMAGES = [
    # ... existing images ...
    {"filename": "your-new-image.jpg", "title": "Your Image Title"},
]
```

3. Refresh the Portfolio page - the new image appears automatically

## Customizing Content

### Update Artist Information

Edit the `ARTIST` dictionary in `app.py`:

```python
ARTIST = {
    "name": "Your Name",
    "bio": "Your biography text here...",
    "portrait": "your-portrait.jpg"  # Place in static/images/
}
```

### Update Contact Information

Edit the `CONTACT` dictionary in `app.py`:

```python
CONTACT = {
    "email": "your@email.com",
    "instagram": "your_handle",
    "location": "Your City",
    "hours": "By appointment"
}
```

### Change Hero Image

Edit the `SITE_CONFIG` dictionary in `app.py`:

```python
SITE_CONFIG = {
    "site_name": "Your Name - Tattoo Artist",
    "tagline": "Your tagline",
    "hero_image": "your-hero.jpg"  # Place in static/images/
}
```

## Image Guidelines

| Type | Recommended Size | Format |
|------|------------------|--------|
| Portfolio | 1200-2000px width | JPG, <500KB |
| Hero | 1920px width | JPG |
| Portrait | 800px width | JPG/PNG |

### Optimizing Images

For best performance, optimize images before adding:

```bash
# Using ImageMagick (if installed)
convert input.jpg -resize 1500x -quality 85 output.jpg

# Or use online tools like:
# - squoosh.app
# - tinypng.com
```

## Running Tests

```bash
pytest tests/
```

## Development Mode

For auto-reload during development:

```bash
FLASK_DEBUG=1 python app.py
```

Or set in `app.py`:
```python
app.run(debug=True)
```

## Deployment

### Option 1: Gunicorn (Recommended for Production)

```bash
pip install gunicorn
gunicorn app:app -w 4 -b 0.0.0.0:8000
```

### Option 2: Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:8000"]
```

Build and run:

```bash
docker build -t tattoo-portfolio .
docker run -p 8000:8000 tattoo-portfolio
```

## Troubleshooting

### Images Not Loading

- Check file exists in correct directory (`static/portfolio/` or `static/images/`)
- Verify filename matches exactly (case-sensitive)
- Check browser console for 404 errors

### Lightbox Not Working

- Ensure JavaScript is enabled in browser
- Check browser console for errors
- Verify `lightbox.js` loads correctly

### Styles Not Applying

- Hard refresh browser (Ctrl+Shift+R / Cmd+Shift+R)
- Check `styles.css` path is correct

## Future Enhancements

The codebase includes TODO comments for easy extension:

- **Blog**: Add routes and templates for blog posts
- **Booking**: Integrate calendar and form submission
- **Categories**: Filter portfolio by tattoo style
- **Admin**: Add authentication and image upload interface

See spec and plan documents in `specs/001-tattoo-portfolio/` for details.
