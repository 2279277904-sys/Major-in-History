# Persian Miniature — Implementation Spec

*Aliases:* Persianate manuscript painting, Timurid/Safavid miniature, Islamic manuscript illustration  
*Slug:* `persian-miniature` · *Category:* historical · *Era:* 13th–17th century

**Origin.** Persianate manuscript painting tradition across Timurid, Safavid, and Mughal courts.

**Reference example.** Shahnameh manuscript illustrations; Behzad's court scenes.

## Signature move(s)

Every panel of content sits inside an ornamental islimi floral border — a fine repeating vine-and-blossom rule in gold leaf — that frames a composition rendered with no single vanishing point: gardens, courtyards, and figures are stacked and tilted so everything stays legible at once. Fine linework carries the detail; color is applied as flat jewel-toned washes of lapis blue, vermillion, and turquoise, with gold leaf used sparingly as the connective, framing material rather than a fill.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Dense, intricate detail across flattened, multi-perspective compositions
- Jewel-toned mineral pigments: lapis blue, vermillion, gold leaf
- Ornamental floral (islimi) borders framing every panel
- Fine, precise linework and delicate figure rendering

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/persian-miniature.css`.)

```css
/* Persian Miniature — design tokens (generated from style_catalog.json) */
/* 13th–17th century | Persianate manuscript painting tradition. */
:root {
  /* color */
  --color-bg: #f6ecd2;
  --color-surface: #fbf5e4;
  --color-surface-2: #ecdcb0;
  --color-text: #2a1a3d;
  --color-text-muted: #5c4a70;
  --color-primary: #1c398e;
  --color-accent: #a61b29;
  --color-gold-leaf: #c9972c;
  --color-turquoise: #2f7d6b;
  /* radius */
  --radius-sm: 4px;
  --radius-md: 10px;
  --radius-lg: 20px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-gilt-frame: 0 0 0 3px #c9972c, 0 4px 14px rgba(42,26,61,0.25);
  --shadow-panel: 0 2px 10px rgba(42,26,61,0.18);
  /* font */
  --font-sans: 'Cormorant Garamond', 'Scheherazade New', serif;
  --font-display: 'Scheherazade New', 'Cormorant Garamond', serif;
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
  --ease-standard: cubic-bezier(0.4, 0.0, 0.2, 1);
  /* extra (signature gradients, composite borders, filters) */
  --islimi-border: repeating-linear-gradient(90deg, #c9972c 0 3px, transparent 3px 14px);
  --lapis-vermillion-wash: linear-gradient(135deg, rgba(28,57,142,0.08), rgba(166,27,41,0.08));
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Persian Miniature — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f6ecd2",
        "surface": "#fbf5e4",
        "surface-2": "#ecdcb0",
        "text": "#2a1a3d",
        "text-muted": "#5c4a70",
        "primary": "#1c398e",
        "accent": "#a61b29",
        "gold-leaf": "#c9972c",
        "turquoise": "#2f7d6b",
      },
      borderRadius: {
        "sm": "4px",
        "md": "10px",
        "lg": "20px",
        "pill": "999px",
      },
      boxShadow: {
        "gilt-frame": "0 0 0 3px #c9972c, 0 4px 14px rgba(42,26,61,0.25)",
        "panel": "0 2px 10px rgba(42,26,61,0.18)",
      },
      fontFamily: {
        "sans": ["'Cormorant Garamond'", "'Scheherazade New'", "serif"],
        "display": ["'Scheherazade New'", "'Cormorant Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.4, 0.0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --islimi-border: repeating-linear-gradient(90deg, #c9972c 0 3px, transparent 3px 14px);
//   --lapis-vermillion-wash: linear-gradient(135deg, rgba(28,57,142,0.08), rgba(166,27,41,0.08));
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Lapis-blue fill with a thin gold-leaf border, cream label text, gilt-frame shadow on hover. |
| **Input** | Cream field bounded by a thin gold hairline; focus adds the full gilt-frame double border. |
| **Card** | Parchment surface with the `--islimi-border` strip running along the top edge and a gilt-frame outline. |
| **Nav** | Parchment bar, gold hairline underneath, wordmark in the display serif with generous letter-spacing. |
| **Modal** | Panel is fully ringed by the gilt-frame border, `--lapis-vermillion-wash` tinting the header area. |
| **Table** | Header row in lapis blue with cream text; body rows on parchment, thin gold hairline dividers. |
| **Tooltip** | Small parchment bubble with a thin gold rule, fine serif type. |
| **Badge** | Small pill in vermillion or turquoise, thin gold border, no gradient fill. |
| **Toggle** | Track as a thin gold islimi-patterned rail; knob is a solid lapis or vermillion disc. |
| **Loading** | A thin gold ring tracing a slow, continuous arabesque loop rather than a plain spinner. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#2a1a3d, deep plum-black ink) on `--color-bg` (#f6ecd2, parchment) — verify with `contrast_check.py`; comfortably clears AA (well above 8:1).
- Lapis-blue (#1c398e) button fills need cream/parchment label text, not the muted plum-purple `--color-text-muted`, to stay legible.
- The dense islimi border pattern must stay confined to margins/frames — never run it directly under body text at full opacity, or legibility drops.
- Keep focus rings a solid, high-contrast color (gold-leaf or lapis) distinct from the decorative gilt-frame shadow used on hover.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Frame every panel with the islimi border or gilt-frame shadow — the ornamental border is structural, not optional trim.
- ✅ Keep color application flat and jewel-toned (lapis, vermillion, turquoise) rather than photographic or gradient-shaded.
- ✅ Use gold sparingly as connective tissue (borders, hairlines, rules), not as a large fill.

## Don't

- ❌ Use a single-point perspective grid — the whole point is flattened, simultaneous multi-perspective composition.
- ❌ Cover full backgrounds in shimmering gold — that reads as byzantine-mosaic, not persian miniature's parchment-and-border language.
- ❌ Simplify the border to a plain solid rule — the ornamental repeating floral motif is the signature, not a generic frame.

## Don't confuse this with…

*Commonly confused neighbors:* byzantine-mosaic, art-nouveau, maximalism.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
