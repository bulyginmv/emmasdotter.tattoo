"""
Gallery data configuration for the tattoo portfolio.

Add new images by appending dictionaries to the PORTFOLIO_IMAGES list.
Each image should have:
  - filename: The image file name in static/portfolio/
  - title: Display title shown in lightbox

Future extensibility (not yet implemented):
  - category: Category tag (e.g., "floral", "blackwork", "geometric")
  - description: Extended description for SEO/accessibility
  - date: Date of creation (YYYY-MM format)
  - featured: Flag for homepage featured images
"""

PORTFOLIO_IMAGES = [
    {"filename": "tattoo1.jpg", "title": "Floral Arm Piece"},
    {"filename": "tattoo2.jpg", "title": "Blackwork Mandala"},
    {"filename": "tattoo3.jpg", "title": "Minimalist Line Art"},
    {"filename": "tattoo4.jpg", "title": "Botanical Illustration"},
    {"filename": "tattoo5.jpg", "title": "Geometric Pattern"},
    {"filename": "tattoo6.jpg", "title": "Fine Line Portrait"},
]

WANNADO_IMAGES = [
    {"filename": "wannado1.jpg", "title": "Japanese Sleeve"},
    {"filename": "wannado2.jpg", "title": "Watercolor Phoenix"},
    {"filename": "wannado3.jpg", "title": "Dotwork Mandala"},
    {"filename": "wannado4.jpg", "title": "Minimalist Mountain"},
    {"filename": "wannado5.jpg", "title": "Abstract Geometric"},
    {"filename": "wannado6.jpg", "title": "Floral Back Piece"},
    {"filename": "wannado7.jpg", "title": "Floral Back Piece"},
]
