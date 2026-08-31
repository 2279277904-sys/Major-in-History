# Woodcut / Linocut — Implementation Spec

*Aliases:* relief print, block print, linocut, woodblock (Western)  
*Slug:* `woodcut-linocut` · *Category:* texture · *Era:* 15th century–present

**Origin.** Relief printmaking: an image is carved into a wood or linoleum block, the raised surface is inked, and paper is pressed onto it by hand or press. Practiced across Europe and the Americas as folk illustration, protest posters, and fine-art printmaking from the Gutenberg era onward.

**Reference example.** Albrecht Dürer's woodcut prints; WPA-era American relief posters; contemporary linocut zine and protest-poster illustration.

## Signature move(s)

Every shape is bounded by a bold, slightly irregular black outline — carved by hand, so no edge is perfectly straight or perfectly parallel. Fill areas are never flat color; they carry a visible gouge-stroke texture (parallel or cross-hatched cut marks) that reads as "carved," not "drawn." The palette stays high-contrast and limited: black ink and cream paper as the base, with at most one spot color (traditionally red) layered on top, never a full-color range.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Bold, thick, hand-carved black outlines on every shape
- Visible gouge/cut-stroke texture filling color areas instead of flat fills
- High-contrast, limited palette: black/cream plus at most one spot color
- Chunky, deliberately imperfect edges — no crisp vector-smooth curves

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/woodcut-linocut.css`.)

```css
/* Woodcut / Linocut — design tokens (generated from style_catalog.json) */
/* 15th century–present | Relief printmaking: carved block, inked, pressed to paper. */
:root {
  /* color */
  --color-bg: #f2e8d3;
  --color-surface: #f8f1e0;
  --color-surface-2: #e9dcbc;
  --color-text: #1c1712;
  --color-text-muted: #5a4a35;
  --color-primary: #1c1712;
  --color-accent: #a4271f;
  --color-cream: #f2e8d3;
  --color-carve-line: #241d16;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 2px;
  --radius-lg: 4px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-print: 6px 6px 0 rgba(28,23,18,0.9);
  --shadow-print-sm: 3px 3px 0 rgba(28,23,18,0.9);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Space Grotesk', 'Helvetica Neue', system-ui, sans-serif;
  --font-display: 'Bebas Neue', 'Anton', 'Arial Black', sans-serif;
  --font-mono: ui-monospace, monospace;
  /* text */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.375rem;
  --text-2xl: 1.75rem;
  --text-3xl: 2.25rem;
  --text-4xl: 3rem;
  --text-5xl: 4rem;
  /* space */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
  /* ease */
  --ease-standard: cubic-bezier(0.2, 0.8, 0.2, 1);
  /* extra (signature gradients, composite borders, filters) */
  --gouge-texture: repeating-linear-gradient(35deg, rgba(28,23,18,0.10) 0px, rgba(28,23,18,0.10) 2px, transparent 2px, transparent 7px);
  --ink-border: 3px solid #1c1712;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Woodcut / Linocut — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2e8d3",
        "surface": "#f8f1e0",
        "surface-2": "#e9dcbc",
        "text": "#1c1712",
        "text-muted": "#5a4a35",
        "primary": "#1c1712",
        "accent": "#a4271f",
        "cream": "#f2e8d3",
        "carve-line": "#241d16",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "print": "6px 6px 0 rgba(28,23,18,0.9)",
        "print-sm": "3px 3px 0 rgba(28,23,18,0.9)",
      },
      fontFamily: {
        "sans": ["'Space Grotesk'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Bebas Neue'", "'Anton'", "'Arial Black'", "sans-serif"],
        "mono": ["ui-monospace", "monospace"],
      },
      fontSize: {
        "xs": "0.75rem",
        "sm": "0.875rem",
        "base": "1rem",
        "lg": "1.125rem",
        "xl": "1.375rem",
        "2xl": "1.75rem",
        "3xl": "2.25rem",
        "4xl": "3rem",
        "5xl": "4rem",
      },
      spacing: {
        "1": "4px",
        "2": "8px",
        "3": "12px",
        "4": "16px",
        "6": "24px",
        "8": "32px",
        "12": "48px",
        "16": "64px",
        "24": "96px",
      },
      transitionTimingFunction: {
        "standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --gouge-texture: repeating-linear-gradient(35deg, rgba(28,23,18,0.10) 0px, rgba(28,23,18,0.10) 2px, transparent 2px, transparent 7px);
//   --ink-border: 3px solid #1c1712;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Thick black ink border, hard offset `--shadow-print-sm` (no blur), press-down shift on active. |
| **Input** | Cream fill with the same 3px ink border; no rounded corners, no soft focus ring. |
| **Card** | Cream/spot-color fill textured with `--gouge-texture`, thick border, full `--shadow-print` offset shadow. |
| **Nav** | Cream bar with a single thick ink rule along the bottom edge, no shadow. |
| **Modal** | Panel snaps in (no fade) with a heavy ink border and offset print shadow, like a stamped block. |
| **Table** | Thick ink rules between rows; header row set in the display face, uppercase, letter-spaced. |
| **Tooltip** | Small cream chip with a 2px ink border and a tiny offset shadow — no blur, no glow. |
| **Badge** | Solid spot-color fill, ink border, uppercase condensed label — reads like a stamped seal. |
| **Toggle** | Track drawn as a thick ink-bordered bar; knob is a solid ink block that snaps (no easing bounce) between states. |
| **Loading** | A hand-carved-looking spinner: a ring of short gouge marks that fill in one at a time, no smooth rotation. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Ink-black text (`--color-text: #1c1712`) on cream (`--color-bg: #f2e8d3`) measures roughly 14.6:1 — verify every pairing with `contrast_check.py`, especially `--color-text-muted` on `--color-surface-2` (still passes at ~7:1, but re-check if either value changes).
- Never let `--gouge-texture` sit directly under body text — apply it to card/button backgrounds only, and keep text on a clean color layer above it.
- The thick ink border already gives strong affordance; still add a distinct `focus-visible` outline (dashed, offset) since the default border doesn't change state on focus.
- Keep hit targets at real 44px even though the hand-carved outline can visually shrink the perceived clickable area.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every outline thick, black, and slightly irregular — no thin hairline strokes.
- ✅ Limit color to black/cream plus one spot color; resist adding a full palette.
- ✅ Texture fills with a visible gouge/cut pattern, not a flat tint.

## Don't

- ❌ Smooth the outlines into perfect vector curves — that kills the hand-carved read.
- ❌ Use soft drop shadows or blur — relief print shadows are hard-edged offsets, like a second impression.
- ❌ Reach for flat, evenly-saturated color fills — that's ukiyo-e's language, not this rougher Western/folk relief-print register.

## Don't confuse this with…

*Commonly confused neighbors:* ukiyo-e, risograph, papercut.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
