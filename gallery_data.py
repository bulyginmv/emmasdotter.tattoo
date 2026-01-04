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
    {"filename": "portfolio1.jpg"},
    {"filename": "portfolio2.jpg"},
    {"filename": "portfolio3.jpg"},
    {"filename": "portfolio4.jpg"},
    {"filename": "portfolio5.jpg"},
    {"filename": "portfolio6.jpg"},
    {"filename": "portfolio7.jpg"},
    {"filename": "portfolio8.jpg"},
    {"filename": "portfolio9.jpg"},
    {"filename": "portfolio10.jpg"},
    {"filename": "portfolio11.jpg"},
    {"filename": "portfolio12.jpg"},
    {"filename": "portfolio13.jpg"},
    {"filename": "portfolio14.jpg"},
    {"filename": "portfolio15.jpg"},
    {"filename": "portfolio16.jpg"},
    {"filename": "portfolio17.jpg"}
]

WANNADO_IMAGES = [
    {"drawing": "design1.jpg", "applied": ["applied_1_1.jpg", "applied_1_2.jpg"]},
    {"drawing": "design2.jpg", "applied": ["applied_2_1.jpg", "applied_2_2.jpg"]},
    {"drawing": "design3.jpg", "applied": ["applied_3_1.jpg", "applied_3_2.jpg"]},
    {"drawing": "design4.jpg", "applied": ["applied_4_1.jpg"]},
    {"drawing": "design5.jpg", "applied": ["applied_5_1.jpg", "applied_5_2.jpg"]},
    {"drawing": "design6.jpg", "applied": ["applied_6_1.jpg"]},
    {"drawing": "design7.jpg", "applied": ["applied_7_1.jpg"]},
    {"drawing": "design8.jpg", "applied": ["applied_8_1.jpg"]},
    {"drawing": "design9.jpg", "applied": ["applied_9_1.jpg"]},
    {"drawing": "design10.jpg", "applied": ["applied_10_1.jpg"]},
    {"drawing": "design11.jpg", "applied": ["applied_11_1.jpg", "applied_11_2.jpg"]},
    {"drawing": "design12.jpg", "applied": ["applied_12_1.jpg"]},
    {"drawing": "design_13.jpg", "applied": ["applied_13_1.jpg"]},
    {"drawing": "design15.jpg", "applied": []},
    {"drawing": "design16.jpg", "applied": ["applied_16_1.jpg"]},
    {"drawing": "design17.jpg", "applied": ["applied_17_1.jpg"]},
    {"drawing": "design18.jpg", "applied": []},
    {"drawing": "design19.jpg", "applied": []},
    {"drawing": "design22.jpg", "applied": ["applied_22_1.jpg"]},
    {"drawing": "design23.jpg", "applied": []},
    {"drawing": "design24.jpg", "applied": []},
    {"drawing": "design25.jpg", "applied": ["applied_25_1.jpg"]},
    {"drawing": "design26.jpg", "applied": []},
    {"drawing": "design27.jpg", "applied": ["applied_27_1.jpg"]},
]
