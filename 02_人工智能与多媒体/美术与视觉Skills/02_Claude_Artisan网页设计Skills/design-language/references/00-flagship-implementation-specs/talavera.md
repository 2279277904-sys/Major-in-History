# Talavera — Implementation Spec

*Aliases:* Talavera poblana, Mexican majolica, tin-glazed ceramic  
*Slug:* `talavera` · *Category:* niche · *Era:* 16th century–present

**Origin.** Hand-painted, tin-glazed (majolica-style) ceramic tradition centered in Puebla, Mexico, blending Spanish and Moorish ceramic techniques (themselves rooted in Islamic Talavera de la Reina pottery) with Indigenous Mexican craft, formalized under a protected Denominación de Origen since the 16th–17th century.

**Reference example.** Puebla's Talavera-tiled church façades and courtyards; Uriarte Talavera workshop pieces; hand-painted Talavera tableware.

## Signature move(s)

A bold cobalt-blue-and-white base carries vivid multicolor floral and geometric motifs painted with thick, confident outlines, then sealed under a glossy tin glaze that catches the light. Ornament is cheerful and maximalist, repeated edge-to-edge across the whole surface — there is no bare, undecorated field.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Bold cobalt blue and white base with vivid multicolor floral/geometric motifs
- Glossy, glazed-tile surface sheen
- Thick, confident hand-painted outlines around every motif
- Cheerful maximalist ornament repeated edge-to-edge, no empty fields

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/talavera.css`.)

```css
/* Talavera — design tokens (generated from style_catalog.json) */
/* 16th century–present | Hand-painted majolica ceramic tradition, Puebla, Mexico. */
:root {
  /* color */
  --color-bg: #f5f2ea;
  --color-surface: #ffffff;
  --color-surface-2: #e7edf2;
  --color-text: #0b2f52;
  --color-text-muted: #3d5a75;
  --color-primary: #0b2f52;
  --color-accent: #d94f2b;
  --color-yellow: #f2b705;
  --color-green: #3f7d4c;
  /* radius */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 28px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-glaze: 0 12px 28px rgba(11,47,82,0.16), inset 0 1px 0 rgba(255,255,255,0.6);
  --shadow-glaze-sm: 0 4px 12px rgba(11,47,82,0.14);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Fraunces', 'Playfair Display', system-ui, serif;
  --font-display: 'Playfair Display', 'Fraunces', serif;
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
  --ease-standard: cubic-bezier(0.34, 1.2, 0.4, 1);
  /* extra (signature gradients, composite borders, filters) */
  --glaze-sheen: linear-gradient(135deg, rgba(255,255,255,0.55) 0%, transparent 35%);
  --tile-border: repeating-linear-gradient(90deg, #0b2f52 0 4px, #f2b705 4px 8px, #d94f2b 8px 12px, #3f7d4c 12px 16px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Talavera — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f5f2ea",
        "surface": "#ffffff",
        "surface-2": "#e7edf2",
        "text": "#0b2f52",
        "text-muted": "#3d5a75",
        "primary": "#0b2f52",
        "accent": "#d94f2b",
        "yellow": "#f2b705",
        "green": "#3f7d4c",
      },
      borderRadius: {
        "sm": "8px",
        "md": "16px",
        "lg": "28px",
        "pill": "999px",
      },
      boxShadow: {
        "glaze": "0 12px 28px rgba(11,47,82,0.16), inset 0 1px 0 rgba(255,255,255,0.6)",
        "glaze-sm": "0 4px 12px rgba(11,47,82,0.14)",
      },
      fontFamily: {
        "sans": ["'Fraunces'", "'Playfair Display'", "system-ui", "serif"],
        "display": ["'Playfair Display'", "'Fraunces'", "serif"],
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
        "standard": "cubic-bezier(0.34, 1.2, 0.4, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --glaze-sheen: linear-gradient(135deg, rgba(255,255,255,0.55) 0%, transparent 35%);
//   --tile-border: repeating-linear-gradient(90deg, #0b2f52 0 4px, #f2b705 4px 8px, #d94f2b 8px 12px, #3f7d4c 12px 16px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | White fill, thick cobalt outline, subtle glaze sheen; primary button in cobalt with white text and the sheen gradient overlaid. |
| **Input** | White field with a 2px cobalt border, no glaze sheen (keeps typed text crisp). |
| **Card** | White surface with `--glaze-sheen`, thick cobalt border, bold accent-color top edge like a decorative tile band. |
| **Nav** | White bar with a thick cobalt rule beneath, echoing a tiled dado border. |
| **Modal** | Panel arrives with a slight overshoot (springy, celebratory), thick cobalt border and glaze shadow. |
| **Table** | Header row in cobalt with white text; alternating rows carry a faint `--tile-border` strip as a divider. |
| **Tooltip** | Small white chip, thin cobalt border, no glaze — stays legible at small size. |
| **Badge** | Marigold-yellow pill with a cobalt border, reads like a small hand-painted seal. |
| **Toggle** | Track rendered as a mini `--tile-border` strip; knob is a solid cobalt circle. |
| **Loading** | A ring of small floral dots (cobalt/yellow/terracotta/green) lighting up in sequence, echoing a hand-painted medallion. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Deep cobalt text (`--color-text: #0b2f52`) on the warm off-white ground (`--color-bg: #f5f2ea`) measures roughly 12.2:1 — verify every pairing with `contrast_check.py`, and re-check `--color-text-muted` on `--color-surface-2` (~6.4:1) if either value shifts.
- White text on the marigold `--color-yellow` fails AA — never set body or label text in yellow-on-white or white-on-yellow; reserve yellow for small badge/accent fills paired with a dark border and dark text.
- Keep the glossy `--glaze-sheen` overlay subtle and decorative only; never let it wash out text sitting on the same surface.
- Maintain a visible, high-contrast focus ring (accent orange or cobalt) — the busy maximalist ornament can otherwise camouflage a default browser outline.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Treat Talavera with genuine craft respect: reference real Puebla motifs (florals, pomegranates, sunbursts), not generic "Mexican pattern" clichés.
- ✅ Keep the cobalt-and-white base dominant, with the other colors (marigold, terracotta, green) as accents on top of it.
- ✅ Fill the surface — Talavera ornament is maximalist and edge-to-edge, not sparse.

## Don't

- ❌ Thin out the outlines into delicate line art — Talavera outlines are thick and confident.
- ❌ Use a matte or flat finish — the glossy glaze sheen is part of the material identity.
- ❌ Treat the palette as generic "fiesta colors" — stay rooted in the cobalt/white/marigold/terracotta/green majolica register.

## Don't confuse this with…

*Commonly confused neighbors:* terrazzo, maximalism, folk-art.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
