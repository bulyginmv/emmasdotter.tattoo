"""Test WannaDo gallery template rendering and lightbox data."""
import json
import re
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from gallery_data import WANNADO_IMAGES


def test_wannado_page_renders():
    """Test that wannado page renders without errors."""
    client = app.test_client()
    response = client.get('/wannado')
    assert response.status_code == 200


def test_data_applied_attribute_present():
    """Test that data-applied attributes are present in rendered HTML."""
    client = app.test_client()
    response = client.get('/wannado')
    html = response.data.decode('utf-8')

    # Check for data-applied attribute
    assert 'data-applied=' in html, "No data-applied attributes found in HTML"


def test_data_applied_attribute_valid_json():
    """Test that data-applied attributes contain valid JSON."""
    client = app.test_client()
    response = client.get('/wannado')
    html = response.data.decode('utf-8')

    # Extract data-applied values (using single quotes now)
    matches = re.findall(r"data-applied='([^']*)'", html)

    print(f"\nFound {len(matches)} data-applied attributes")

    assert len(matches) > 0, "No data-applied attributes found"

    for i, match in enumerate(matches):
        print(f"\nRaw match {i}: {repr(match)}")

        # HTML entities should be decoded
        decoded = match.replace('&quot;', '"').replace('&amp;', '&')
        print(f"Decoded: {decoded}")

        try:
            parsed = json.loads(decoded)
            print(f"Parsed JSON: {parsed}")
            assert isinstance(parsed, list), f"Expected list, got {type(parsed)}"
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}")
            raise


def test_gallery_data_structure():
    """Test that WANNADO_IMAGES has correct structure."""
    print(f"\nWANNADO_IMAGES has {len(WANNADO_IMAGES)} items")

    for i, item in enumerate(WANNADO_IMAGES):
        print(f"Item {i}: {item}")
        assert 'drawing' in item, f"Missing 'drawing' key in item {i}"
        assert 'applied' in item, f"Missing 'applied' key in item {i}"
        assert isinstance(item['applied'], list), f"'applied' should be a list in item {i}"


def test_print_rendered_html_snippet():
    """Print a snippet of the rendered HTML for debugging."""
    client = app.test_client()
    response = client.get('/wannado')
    html = response.data.decode('utf-8')

    # Find gallery items
    start = html.find('gallery-grid')
    if start != -1:
        end = html.find('</div>', start + 500)
        snippet = html[start:end + 6]
        print(f"\n--- HTML Snippet ---\n{snippet}\n--- End Snippet ---")


if __name__ == '__main__':
    # Run tests manually for debugging
    print("Testing gallery data structure...")
    test_gallery_data_structure()

    print("\n\nTesting page renders...")
    test_wannado_page_renders()

    print("\n\nTesting data-applied attributes...")
    test_data_applied_attribute_present()

    print("\n\nTesting JSON validity...")
    test_data_applied_attribute_valid_json()

    print("\n\nPrinting HTML snippet...")
    test_print_rendered_html_snippet()

    print("\n\nAll tests passed!")
