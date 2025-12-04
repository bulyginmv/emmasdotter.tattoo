"""
Minimalist Tattoo Artist Portfolio Website

A Flask-based portfolio site featuring:
- Home page with hero image and artist intro
- Portfolio gallery with lightbox
- About page with artist bio
- Contact page with contact information

Run with: python app.py
"""

from flask import Flask, render_template, send_from_directory
from gallery_data import PORTFOLIO_IMAGES, WANNADO_IMAGES

app = Flask(__name__)

# =============================================================================
# Site Configuration
# =============================================================================

SITE_CONFIG = {
    "site_name": "emmasdotter.tattoo",
    "tagline": "Tattoo Artist in Lund, Sweden",
    "hero_image": "hero.jpg",
    "artist_intro": "Professional tattoo artist based in Lund, Sweden. I specialize in fine-line, illustrative tattoos at Honey Bunny Tattoo.<br>Let's create something special together!"
}

ARTIST = {
    "name": "Nicole ✨",
    "bio": """<p>Hi! I’m Nicole, a tattoo artist based in Lund, Sweden.
<br><br>
                I’ve loved tattoos since my teens — stick-and-poke tattoos included! 😊 After studying art in school, I decided in 2021 to turn my passion into a career. Dreams do come true: in 2025, I moved to Sweden and joined Honey Bunny Tattoo in Lund as a full-time artist, thanks to my amazing colleague Karin!
<br><br>

                I specialize in fine-line, illustrative tattoos with floral or abstract ornamental designs, but my favorite part is helping clients bring their tattoo ideas to life.
<br><br>

                Want to create something unique? <a href="https://ig.me/m/emmasdotter.tattoo" target="_blank" class="instagram-link">DM me on Instagram</a> or drop by Honey Bunny Tattoo in Lund to book a consultation or appointment!</p>

    </p>""",
    "portrait": "artist-portrait.jpg"
}

CONTACT = {
    "instagram": "emmasdotter.tattoo",
    "location": "Honey Bunny Tattoo, Lund, Sweden",
    "location_url": "https://maps.app.goo.gl/hCPL7QLuPCXPZhFo9",
    "hours": "By appointment"
}

# =============================================================================
# Routes
# =============================================================================

@app.route('/')
def home():
    """Homepage with hero image and artist introduction."""
    return render_template('home.html',
        site_name=SITE_CONFIG['site_name'],
        tagline=SITE_CONFIG['tagline'],
        hero_image=SITE_CONFIG['hero_image'],
        artist_intro=SITE_CONFIG['artist_intro'],
        contact_instagram=CONTACT.get('instagram'),
        current_page='home'
    )


@app.route('/portfolio')
def portfolio():
    """Gallery page with all portfolio images."""
    return render_template('portfolio.html',
        site_name=SITE_CONFIG['site_name'],
        images=PORTFOLIO_IMAGES,
        current_page='portfolio'
    )


@app.route('/wannado')
def wannado():
    """Wanna Do gallery - designs the artist wants to create."""
    return render_template('wannado.html',
        site_name=SITE_CONFIG['site_name'],
        images=WANNADO_IMAGES,
        contact_instagram=CONTACT.get('instagram'),
        current_page='wannado'
    )


@app.route('/about')
def about():
    """Artist biography and portrait page."""
    return render_template('about.html',
        site_name=SITE_CONFIG['site_name'],
        artist_name=ARTIST['name'],
        artist_bio=ARTIST['bio'],
        artist_portrait=ARTIST['portrait'],
        current_page='about'
    )


@app.route('/contact')
def contact():
    """Contact information page."""
    return render_template('contact.html',
        site_name=SITE_CONFIG['site_name'],
        contact_instagram=CONTACT.get('instagram'),
        contact_location=CONTACT.get('location'),
        contact_location_url=CONTACT.get('location_url'),
        contact_hours=CONTACT.get('hours'),
        current_page='contact'
    )


# =============================================================================
# SEO Routes
# =============================================================================

@app.route('/robots.txt')
def robots():
    """Serve robots.txt for search engines."""
    return send_from_directory('static', 'robots.txt')


@app.route('/sitemap.xml')
def sitemap():
    """Serve sitemap.xml for search engines."""
    return send_from_directory('static', 'sitemap.xml')


# =============================================================================
# Error Handlers
# =============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors with a friendly page."""
    return render_template('404.html',
        site_name=SITE_CONFIG['site_name'],
        current_page='error'
    ), 404


# =============================================================================
# Future Routes (TODO)
# =============================================================================

# TODO: Blog routes
# @app.route('/blog')
# def blog():
#     """Blog listing page."""
#     pass
#
# @app.route('/blog/<slug>')
# def blog_post(slug):
#     """Individual blog post."""
#     pass

# TODO: Booking routes
# @app.route('/booking')
# def booking():
#     """Booking calendar page."""
#     pass
#
# @app.route('/booking', methods=['POST'])
# def submit_booking():
#     """Submit booking request."""
#     pass

# TODO: Additional pages
# @app.route('/aftercare')
# def aftercare():
#     """Aftercare information page."""
#     pass
#
# @app.route('/flash')
# def flash_designs():
#     """Flash designs gallery."""
#     pass

# TODO: API endpoints for future JavaScript filtering
# @app.route('/api/images')
# def api_images():
#     """JSON API for images."""
#     pass


# =============================================================================
# Application Entry Point
# =============================================================================

if __name__ == '__main__':
    app.run(debug=True)
