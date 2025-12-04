/**
 * Lightbox functionality for the tattoo portfolio gallery.
 *
 * Features:
 * - Click image to open lightbox
 * - Click outside image or close button to close
 * - Press Escape key to close
 * - Display image title from data-title attribute
 * - Touch-friendly for mobile devices
 */

(function() {
    'use strict';

    // DOM Elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = lightbox.querySelector('.lightbox-image');
    const lightboxTitle = lightbox.querySelector('.lightbox-title');
    const lightboxClose = lightbox.querySelector('.lightbox-close');
    const galleryItems = document.querySelectorAll('.gallery-item');

    // Track previously focused element for accessibility
    let previouslyFocused = null;

    /**
     * Open the lightbox with the given image
     * @param {string} src - Image source URL
     * @param {string} title - Image title
     */
    function openLightbox(src, title) {
        previouslyFocused = document.activeElement;

        lightboxImage.src = src;
        lightboxImage.alt = title || 'Portfolio image';
        lightboxTitle.textContent = title || '';

        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Focus the close button for accessibility
        lightboxClose.focus();
    }

    /**
     * Close the lightbox
     */
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';

        // Clear image to prevent flash on next open
        lightboxImage.src = '';
        lightboxTitle.textContent = '';

        // Return focus to previously focused element
        if (previouslyFocused) {
            previouslyFocused.focus();
        }
    }

    // Event Listeners

    // Click on gallery item to open lightbox
    galleryItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const src = this.getAttribute('data-src');
            const title = this.getAttribute('data-title');
            openLightbox(src, title);
        });

        // Make gallery items keyboard accessible
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const src = this.getAttribute('data-src');
                const title = this.getAttribute('data-title');
                openLightbox(src, title);
            }
        });
    });

    // Click close button to close lightbox
    lightboxClose.addEventListener('click', closeLightbox);

    // Click outside image to close lightbox
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Press Escape to close lightbox
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });

    // Prevent scrolling when lightbox is open and user tries to scroll
    lightbox.addEventListener('touchmove', function(e) {
        e.preventDefault();
    }, { passive: false });

})();
