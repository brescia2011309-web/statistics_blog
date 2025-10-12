## Quick orientation for AI coding agents

This is a small static blog composed of plain HTML pages styled with Tailwind via CDN and a handful of inline CSS customizations. The guidance below focuses on immediately useful, discoverable facts so an AI agent can make safe, targeted edits and add pages consistently.

### Big picture
- Single-folder static site (no build system, no package.json). Key files: `index.html`, `homework1.html`, `homework2.html`, `README.md`.
- Styling is provided by Tailwind CSS loaded from the CDN (`<script src="https://cdn.tailwindcss.com"></script>`) and per-page inline CSS in the `<head>`.
- Pages follow a consistent layout: a top header with a link back to `index.html`, a main article section, and a footer. Visual themes use CSS variables (`--neon-color`) and utility classes like `brutal-border`, `cyber-mono`, `text-neon` defined in each file's `<style>` block.

### Where to look for examples
- Navigation / hero design: `index.html` — uses large uppercase title, neon variables and `brutal-border-hover` for links.
- Article structure: `homework1.html` and `homework2.html` — each contains a header with an index link, an author block (uppercase, monospace), and content sections using `.section-header` and `.code-block-brutal` patterns.

### Editing & extension patterns (concrete rules)
- New page template: copy `homework2.html`, keep the same `<header>` structure (link to `index.html`), `<main>` container class (`container mx-auto px-6 md:px-12 py-12`) and reuse the inline `<style>` at top to preserve theme.
- Keep author metadata format: Author line uses monospace and contains `CARLA ASSUNTA BRESCIA / MATRICOLA: 2011309` (search for this exact string when updating author info).
- Use existing CSS classes rather than inventing new utility classes unless necessary. Examples: use `brutal-border` for bordered boxes and `cyber-mono` for monospace blocks.

### Build / preview / debug
- There is no build step. To preview, open the HTML files directly in a browser or use the VS Code Live Server extension to serve the folder. For simple checks, open `index.html`.
- Debugging: use browser DevTools. Look for duplicated inline CSS across files — style changes should be propagated manually to each HTML file.

### Integration points & external deps
- External CDN deps (do not remove):
  - Tailwind CDN: `<script src="https://cdn.tailwindcss.com"></script>`
  - Google Fonts Inter: `@import url('https://fonts.googleapis.com/css2?family=Inter:...')` in the `<style>` block
- No API calls, no JS frameworks, and no server-side code discovered. Treat this repo as purely static.

### Language & content conventions
- Mixed Italian / English text is present. Keep titles and author info as uppercase monospace where present.
- Headings are often ALL CAPS and use utility/semantic classes (`text-neon`, `cyber-glow-text`). Follow the same casing and class usage when adding content.

### Safety for automated edits
- Avoid changing external CDN URLs unless explicitly requested.
- When updating styles, mirror changes across all HTML files (styles are duplicated in each file's `<head>`).

### Useful quick tasks examples
- Add a new article: duplicate `homework2.html` → rename to `homework3.html` → update `<h1>`, author block, and content sections. Add a link from `index.html` by copying the existing folder-item block and updating the `href`.
- Change theme color: update `--neon-color` value in each HTML `<style>` block (remember to edit `index.html`, `homework1.html`, `homework2.html`).

If anything is unclear (preferred page template, desired naming convention for new articles, or whether to centralize styles into a single CSS file), tell me which part to expand and I will update this file.

