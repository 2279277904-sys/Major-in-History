# Folk Art / Naive Art — Implementation Spec

*Aliases:* naive art, outsider folk painting, self-taught art  
*Slug:* `folk-art-naive` · *Category:* historical · *Era:* 18th–20th century

**Origin.** Self-taught, untrained visual traditions worldwide — rural painters, sign-makers, and craftspeople outside academic art institutions.

**Reference example.** Grandma Moses farm scenes; Henri Rousseau jungle paintings; Pennsylvania Dutch hex signs.

## Signature move(s)

Everything is flattened and drawn from confident hand, not trained eye: no vanishing-point perspective, just stacked, tilted, or scaled-by-importance shapes filled with bold saturated flat color and bounded by a thick, unwavering outline. Decorative repeating motifs — flowers, birds, hearts, farm animals — border the content the way a quilt or a hex sign borders its center, and every edge sits a few degrees off true, because it was drawn by hand and nobody smoothed it out.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Flattened perspective with no attempt at photographic realism
- Bold, saturated flat color fields
- Decorative repeating motifs: flowers, animals, everyday scenes
- Thick, confident hand-drawn outlines and warm handmade charm

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/folk-art-naive.css`.)

```css
/* Folk Art / Naive Art — design tokens (generated from style_catalog.json) */
/* 18th–20th century | Self-taught, untrained visual traditions worldwide. */
:root {
  /* color */
  --color-bg: #fbf1de;
  --color-surface: #fff8ec;
  --color-surface-2: #f3e2bf;
  --color-text: #3a2317;
  --color-text-muted: #6b4a35;
  --color-primary: #d63b2f;
  --color-accent: #2f7a63;
  --color-mustard: #e0a629;
  --color-outline-ink: #2b1a10;
  /* radius */
  --radius-sm: 6px;
  --radius-md: 14px;
  --radius-lg: 24px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-outline: 0 3px 0 #2b1a10;
  --shadow-outline-sm: 0 2px 0 #2b1a10;
  /* font */
  --font-sans: 'Fredoka', 'Baloo 2', system-ui, sans-serif;
  --font-display: 'Baloo 2', 'Fredoka', sans-serif;
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
  --ease-standard: cubic-bezier(0.34, 1.56, 0.64, 1);
  /* extra (signature gradients, composite borders, filters) */
  --motif-border: repeating-linear-gradient(45deg, #d63b2f 0 6px, #e0a629 6px 12px, #2f7a63 12px 18px);
  --outline-stroke: 3px solid #2b1a10;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Folk Art / Naive Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#fbf1de",
        "surface": "#fff8ec",
        "surface-2": "#f3e2bf",
        "text": "#3a2317",
        "text-muted": "#6b4a35",
        "primary": "#d63b2f",
        "accent": "#2f7a63",
        "mustard": "#e0a629",
        "outline-ink": "#2b1a10",
      },
      borderRadius: {
        "sm": "6px",
        "md": "14px",
        "lg": "24px",
        "pill": "999px",
      },
      boxShadow: {
        "outline": "0 3px 0 #2b1a10",
        "outline-sm": "0 2px 0 #2b1a10",
      },
      fontFamily: {
        "sans": ["'Fredoka'", "'Baloo 2'", "system-ui", "sans-serif"],
        "display": ["'Baloo 2'", "'Fredoka'", "sans-serif"],
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
        "standard": "cubic-bezier(0.34, 1.56, 0.64, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --motif-border: repeating-linear-gradient(45deg, #d63b2f 0 6px, #e0a629 6px 12px, #2f7a63 12px 18px);
//   --outline-stroke: 3px solid #2b1a10;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Flat mustard or barn-red fill, thick ink outline, offset flat drop-shadow (`--shadow-outline`) that presses flush on click. |
| **Input** | Cream field with a thick hand-drawn ink border; corners slightly uneven rather than perfectly square. |
| **Card** | Flat cream surface, thick outline, a strip of `--motif-border` running along one edge like a painted quilt trim. |
| **Nav** | Barn-red bar with a mustard motif-border strip along the bottom, wordmark in the display font. |
| **Modal** | Panel pops in with a slight overshoot bounce (`--ease-standard`), thick outline, motif-border framing the top. |
| **Table** | Alternating cream/mustard-tint rows, thick ink rule under the header, no vertical cell lines. |
| **Tooltip** | Small flat-color bubble with a thick outline and a hand-drawn triangular pointer. |
| **Badge** | Pill in accent teal or mustard, thick ink outline, no gradient — flat color reads as folk craft. |
| **Toggle** | Track painted like a barn-door slat; knob is a flat painted circle with a thick outline. |
| **Loading** | A small painted sun or flower motif rotating steadily, flat-color, no blur or glow. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#3a2317) on `--color-bg` (#fbf1de) is a dark warm brown on warm cream — verify with `contrast_check.py`; it clears AA comfortably (well above 7:1).
- The barn-red primary (#d63b2f) used as a button fill needs cream or white label text, not the muted brown body text color — check that pairing separately.
- Thick outlines are decorative, not a substitute for a visible focus ring — keep a distinct focus-visible outline (e.g. offset ink-colored ring) beyond the permanent border.
- Don't let decorative motif-borders creep into the content reading area; keep them to edges/frames so they never sit behind body text.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every fill flat and saturated — no gradients or glows, folk art is opaque color.
- ✅ Let outlines wobble slightly (a hair off straight) rather than using perfectly vector-crisp lines.
- ✅ Use the repeating motif border as a structural frame, echoed consistently across nav, card, and modal edges.

## Don't

- ❌ Add photographic realism, depth-of-field, or perspective shading — naive art is deliberately flat and untrained-looking.
- ❌ Reach for pastel or muted tones — the palette is bold and saturated, not soft.
- ❌ Turn the hand-drawn wobble into full-on chalk texture or grunge grain — that's chalkboard-lettering's and grunge's territory, not this one's clean flat-color charm.

## Don't confuse this with…

*Commonly confused neighbors:* chalkboard-lettering, memphis-design, psychedelic-art.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
