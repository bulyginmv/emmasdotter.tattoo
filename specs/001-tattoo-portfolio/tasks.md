# Tasks: Minimalist Tattoo Artist Portfolio Website

**Input**: Design documents from `/specs/001-tattoo-portfolio/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/routes.md, research.md, quickstart.md

**Tests**: No automated tests requested in specification. Manual browser testing per quickstart.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md, this is a Flask monolith with the following structure:
- Application entry: `app.py`
- Data configuration: `gallery_data.py`
- Templates: `templates/`
- Static assets: `static/css/`, `static/js/`, `static/portfolio/`, `static/images/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, dependencies, and base structure

- [x] T001 Create project directory structure per plan.md (static/, templates/, tests/)
- [x] T002 Create requirements.txt with Flask dependency
- [x] T003 [P] Create gallery_data.py with sample PORTFOLIO_IMAGES list
- [x] T004 [P] Add placeholder images to static/portfolio/ (at least 6 sample images)
- [x] T005 [P] Add placeholder hero image and artist portrait to static/images/

---

## Phase 2: Foundational (Base Template & Styling)

**Purpose**: Core infrastructure that ALL pages depend on - navigation, footer, and base styling

**CRITICAL**: No user story pages can be completed until base.html and styles.css provide the foundation

- [x] T006 Create templates/base.html with navigation header, main content block, and footer
- [x] T007 Create static/css/styles.css with CSS reset and base typography (mobile-first)
- [x] T008 Add navigation styles to static/css/styles.css (responsive nav with hamburger for mobile)
- [x] T009 Add footer styles to static/css/styles.css
- [x] T010 Create app.py with Flask app initialization and configuration constants (SITE_CONFIG, ARTIST, CONTACT)
- [x] T011 Add nav active state logic using current_page variable in templates/base.html

**Checkpoint**: Base template renders with working navigation and footer. Ready for page implementation.

---

## Phase 3: User Story 1 - Browse Tattoo Portfolio (Priority: P1)

**Goal**: Visitors can browse tattoo images in a gallery with lightbox functionality

**Independent Test**: Navigate to /portfolio, see grid of images, click any image to open lightbox, close lightbox

### Implementation for User Story 1

- [x] T012 [US1] Add /portfolio route to app.py that renders portfolio.html with images from gallery_data
- [x] T013 [US1] Create templates/portfolio.html extending base.html with gallery grid container
- [x] T014 [US1] Add gallery grid styles to static/css/styles.css (CSS Grid masonry-like layout)
- [x] T015 [US1] Add responsive gallery styles for mobile (1-2 columns) and desktop (3-4 columns)
- [x] T016 [US1] Create static/js/lightbox.js with lightbox open/close functionality
- [x] T017 [US1] Add lightbox styles to static/css/styles.css (overlay, centered image, close button)
- [x] T018 [US1] Add keyboard support (Escape to close) to static/js/lightbox.js
- [x] T019 [US1] Add title display in lightbox from data-title attribute in static/js/lightbox.js
- [x] T020 [US1] Add image hover animation styles to static/css/styles.css
- [x] T021 [US1] Handle empty portfolio state in templates/portfolio.html ("Portfolio coming soon")

**Checkpoint**: Portfolio page fully functional - grid displays images, lightbox works with keyboard/mouse/touch

---

## Phase 4: User Story 2 - Discover the Artist (Priority: P2)

**Goal**: Visitors can learn about the artist through biography and portrait

**Independent Test**: Navigate to /about, see artist portrait and biography text, verify responsive layout

### Implementation for User Story 2

- [x] T022 [US2] Add /about route to app.py that renders about.html with artist data
- [x] T023 [US2] Create templates/about.html extending base.html with portrait and bio layout
- [x] T024 [US2] Add about page styles to static/css/styles.css (side-by-side on desktop, stacked on mobile)
- [x] T025 [US2] Add placeholder bio text to ARTIST config in app.py

**Checkpoint**: About page displays portrait and bio with responsive layout

---

## Phase 5: User Story 3 - Get Contact Information (Priority: P2)

**Goal**: Visitors can find contact details to reach the artist

**Independent Test**: Navigate to /contact, see email (clickable), Instagram link, location info

### Implementation for User Story 3

- [x] T026 [US3] Add /contact route to app.py that renders contact.html with contact data
- [x] T027 [US3] Create templates/contact.html extending base.html with contact details layout
- [x] T028 [US3] Add contact page styles to static/css/styles.css (centered, minimal layout)
- [x] T029 [US3] Add mailto: link for email and external link for Instagram in templates/contact.html
- [x] T030 [US3] Add TODO comment placeholder for future contact form in templates/contact.html

**Checkpoint**: Contact page displays all contact information with working links

---

## Phase 6: User Story 4 - First Impression via Homepage (Priority: P3)

**Goal**: Visitors see an engaging homepage with hero image and CTA to portfolio

**Independent Test**: Navigate to /, see hero image, artist intro, and working CTA button to portfolio

### Implementation for User Story 4

- [x] T031 [US4] Add / (home) route to app.py that renders home.html with site config data
- [x] T032 [US4] Create templates/home.html extending base.html with hero section
- [x] T033 [US4] Add hero section styles to static/css/styles.css (full-width image, overlay text)
- [x] T034 [US4] Add artist intro section below hero in templates/home.html
- [x] T035 [US4] Add CTA button/link to portfolio in templates/home.html
- [x] T036 [US4] Add responsive hero styles for mobile in static/css/styles.css

**Checkpoint**: Homepage displays hero, intro, and CTA - all responsive and linking to portfolio

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements, documentation, and future-proofing

- [x] T037 [P] Add TODO comments for future features (blog, booking, categories) in app.py
- [x] T038 [P] Add TODO comments for future routes in app.py (see contracts/routes.md Future Routes)
- [x] T039 Add 404 error handler to app.py with friendly error page
- [x] T040 [P] Create README.md with project overview and link to quickstart
- [x] T041 Verify all pages render correctly at 320px, 768px, 1024px, 1920px viewports
- [x] T042 Test lightbox on touch device (or touch simulation in browser)
- [x] T043 Verify site works with JavaScript disabled (graceful degradation)
- [x] T044 Run quickstart.md validation (start app, add image, verify it appears)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on T002 (requirements.txt) - BLOCKS all user stories
- **User Stories (Phases 3-6)**: All depend on Phase 2 completion (base.html, styles.css, app.py init)
  - User stories can proceed in priority order (P1 → P2 → P2 → P3)
  - Or in parallel if multiple developers available
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Phase 2 only - no dependencies on other stories
- **User Story 2 (P2)**: Depends on Phase 2 only - independent of US1
- **User Story 3 (P2)**: Depends on Phase 2 only - independent of US1, US2
- **User Story 4 (P3)**: Depends on Phase 2 only - independent but benefits from US1 (portfolio link)

### Within Each User Story

- Route in app.py before template
- Template before page-specific styles
- Core functionality before enhancements

### Parallel Opportunities

**Phase 1 (Setup)**:
```
T003, T004, T005 can all run in parallel (different files)
```

**Phase 2 (Foundational)**:
```
After T006 (base.html) and T007 (styles.css base):
- T008, T009 can run in parallel (different style sections)
```

**After Phase 2 completes - User Stories can run in parallel**:
```
# Different developers can work on different stories:
Developer A: T012-T021 (US1 - Portfolio)
Developer B: T022-T025 (US2 - About)
Developer C: T026-T030 (US3 - Contact)
Developer D: T031-T036 (US4 - Homepage)
```

**Phase 7 (Polish)**:
```
T037, T038, T040 can all run in parallel (different files)
```

---

## Parallel Example: User Story 1

```bash
# After US1 route (T012) is complete, these can run in parallel:
Task: "Create templates/portfolio.html extending base.html"
Task: "Add gallery grid styles to static/css/styles.css"

# After template and styles exist, lightbox tasks can proceed:
Task: "Create static/js/lightbox.js with lightbox functionality"
Task: "Add lightbox styles to static/css/styles.css"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (base template, nav, footer, app init)
3. Complete Phase 3: User Story 1 (Portfolio with gallery + lightbox)
4. **STOP and VALIDATE**: Test portfolio page independently
5. Deploy/demo - visitors can browse all tattoo work

### Incremental Delivery

1. Setup + Foundational → Base site structure ready
2. Add User Story 1 → Portfolio works → Deploy (MVP!)
3. Add User Story 2 → About page works → Deploy
4. Add User Story 3 → Contact page works → Deploy
5. Add User Story 4 → Homepage polished → Deploy
6. Polish phase → Documentation, edge cases, testing

### Single Developer Strategy (Recommended)

Execute in strict priority order:
1. Phase 1 → Phase 2 → Phase 3 (MVP)
2. Validate MVP thoroughly
3. Phase 4 → Phase 5 → Phase 6 → Phase 7

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- No automated tests - manual browser testing per spec requirements
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All pages share base.html navigation - test nav links after each page added
