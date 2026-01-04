/**
 * Lightbox functionality for the WannaDo gallery.
 *
 * Features:
 * - Click image to open lightbox with drawing + applied images
 * - Supports 0, 1, or multiple applied images
 * - Navigate between images with arrows, swipe, or keyboard
 * - Dynamic dot indicators based on image count
 * - Touch-friendly for mobile devices
 */

(function() {
    'use strict';

    // DOM Elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = lightbox.querySelector('.lightbox-image');
    const lightboxClose = lightbox.querySelector('.lightbox-close');
    const lightboxPrev = lightbox.querySelector('.lightbox-prev');
    const lightboxNext = lightbox.querySelector('.lightbox-next');
    const lightboxIndicators = lightbox.querySelector('.lightbox-indicators');
    const galleryItems = document.querySelectorAll('.gallery-item');

    // State
    let previouslyFocused = null;
    let currentIndex = 0;
    let images = [];

    // Touch handling
    let touchStartX = 0;
    let touchEndX = 0;

    /**
     * Build full URL for applied image filename
     * @param {string} drawingUrl - Full URL of drawing image (to extract base path)
     * @param {string} filename - Filename of applied image
     * @returns {string} Full URL for applied image
     */
    function buildAppliedUrl(drawingUrl, filename) {
        // Extract base path from drawing URL (everything before the filename)
        const lastSlash = drawingUrl.lastIndexOf('/');
        const basePath = drawingUrl.substring(0, lastSlash + 1);
        return basePath + filename;
    }

    /**
     * Create dot indicators based on image count
     * @param {number} count - Number of images
     */
    function createDots(count) {
        lightboxIndicators.innerHTML = '';

        if (count <= 1) {
            return; // No dots needed for single image
        }

        for (let i = 0; i < count; i++) {
            const dot = document.createElement('span');
            dot.className = 'lightbox-dot' + (i === 0 ? ' active' : '');
            dot.setAttribute('data-index', i);
            dot.addEventListener('click', function(e) {
                e.stopPropagation();
                currentIndex = i;
                showImage(currentIndex);
            });
            lightboxIndicators.appendChild(dot);
        }
    }

    /**
     * Update navigation visibility based on image count
     * @param {number} count - Number of images
     */
    function updateNavVisibility(count) {
        const showNav = count > 1;
        lightboxPrev.style.display = showNav ? '' : 'none';
        lightboxNext.style.display = showNav ? '' : 'none';
    }

    /**
     * Open the lightbox with drawing and applied images
     * @param {string} drawingSrc - Drawing image source URL
     * @param {string[]} appliedFilenames - Array of applied image filenames
     */
    function openLightbox(drawingSrc, appliedFilenames) {
        previouslyFocused = document.activeElement;

        // Build images array: drawing first, then applied images
        images = [drawingSrc];
        appliedFilenames.forEach(function(filename) {
            images.push(buildAppliedUrl(drawingSrc, filename));
        });

        currentIndex = 0;

        createDots(images.length);
        updateNavVisibility(images.length);
        showImage(currentIndex);

        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';

        lightboxClose.focus();
    }

    /**
     * Show image at given index
     * @param {number} index - Image index
     */
    function showImage(index) {
        lightboxImage.src = images[index];
        lightboxImage.alt = index === 0 ? 'Tattoo design drawing' : 'Tattoo design applied';

        // Update dot indicators
        const dots = lightboxIndicators.querySelectorAll('.lightbox-dot');
        dots.forEach(function(dot, i) {
            dot.classList.toggle('active', i === index);
        });
    }

    /**
     * Navigate to next image
     */
    function nextImage() {
        if (images.length <= 1) return;
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }

    /**
     * Navigate to previous image
     */
    function prevImage() {
        if (images.length <= 1) return;
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
    }

    /**
     * Close the lightbox
     */
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';

        lightboxImage.src = '';
        images = [];
        currentIndex = 0;

        if (previouslyFocused) {
            previouslyFocused.focus();
        }
    }

    /**
     * Handle touch start
     */
    function handleTouchStart(e) {
        touchStartX = e.changedTouches[0].screenX;
    }

    /**
     * Handle touch end and detect swipe
     */
    function handleTouchEnd(e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }

    /**
     * Process swipe gesture
     */
    function handleSwipe() {
        if (images.length <= 1) return;

        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                nextImage();
            } else {
                prevImage();
            }
        }
    }

    // Event Listeners

    // Click on gallery item to open lightbox
    galleryItems.forEach(function(item) {
        item.addEventListener('click', function(e) {
            if (e.target.classList.contains('book-button')) {
                return;
            }
            const drawingSrc = this.getAttribute('data-drawing');
            const appliedJson = this.getAttribute('data-applied');
            const appliedFilenames = JSON.parse(appliedJson);
            openLightbox(drawingSrc, appliedFilenames);
        });

        // Make gallery items keyboard accessible
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                if (e.target.classList.contains('book-button')) {
                    return;
                }
                e.preventDefault();
                const drawingSrc = this.getAttribute('data-drawing');
                const appliedJson = this.getAttribute('data-applied');
                const appliedFilenames = JSON.parse(appliedJson);
                openLightbox(drawingSrc, appliedFilenames);
            }
        });
    });

    // Navigation arrows
    lightboxPrev.addEventListener('click', function(e) {
        e.stopPropagation();
        prevImage();
    });

    lightboxNext.addEventListener('click', function(e) {
        e.stopPropagation();
        nextImage();
    });

    // Close button
    lightboxClose.addEventListener('click', closeLightbox);

    // Click outside image to close
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (!lightbox.classList.contains('active')) return;

        switch (e.key) {
            case 'Escape':
                closeLightbox();
                break;
            case 'ArrowLeft':
                prevImage();
                break;
            case 'ArrowRight':
                nextImage();
                break;
        }
    });

    // Touch swipe support
    lightbox.addEventListener('touchstart', handleTouchStart, { passive: true });
    lightbox.addEventListener('touchend', handleTouchEnd, { passive: true });

    // Prevent scrolling when lightbox is open
    lightbox.addEventListener('touchmove', function(e) {
        e.preventDefault();
    }, { passive: false });

})();
