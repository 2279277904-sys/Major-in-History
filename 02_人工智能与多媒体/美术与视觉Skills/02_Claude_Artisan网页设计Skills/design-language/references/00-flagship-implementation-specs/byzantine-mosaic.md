# Byzantine Mosaic — Implementation Spec

*Aliases:* Byzantine art, gold-ground mosaic, tesserae mosaic  
*Slug:* `byzantine-mosaic` · *Category:* historical · *Era:* 4th–15th century

**Origin.** Eastern Roman (Byzantine) Empire; sacred mosaic decoration of churches from Ravenna to Constantinople.

**Reference example.** San Vitale mosaics, Ravenna; Hagia Sophia apse mosaics.

## Signature move(s)

Small glass tesserae, each catching light at a slightly different angle, build up jewel-toned fields of sapphire, emerald, and ruby that sit inside — or beside — a luminous gold ground rendered as a shimmering diagonal gradient sweep, never a flat fill. Figures and content blocks stay rigid and frontal, bounded by tight geometric tessellated borders (a repeating diagonal tile pattern), giving every surface the sacred, iconic weight of a wall meant to be seen from a distance in candlelight.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Gold-ground tesserae backgrounds with luminous, shimmering fields
- Jewel-toned glass tile colors: deep sapphire, emerald, ruby
- Rigid, frontal, hieratic figures with almond eyes
- Geometric tessellated borders framing every panel

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/byzantine-mosaic.css`.)

```css
/* Byzantine Mosaic — design tokens (generated from style_catalog.json) */
/* 4th–15th century | Eastern Roman (Byzantine) Empire sacred mosaic decoration. */
:root {
  /* color */
  --color-bg: #0d1b3d;
  --color-surface: #142a5c;
  --color-surface-2: #1c3a7a;
  --color-text: #f5e6b8;
  --color-text-muted: #c9b57a;
  --color-primary: #d4af37;
  --color-accent: #7a1f3d;
  --color-emerald-tile: #1f6b4a;
  --color-gold-ground: #caa036;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-gold-glow: 0 0 20px rgba(212,175,55,0.40), 0 8px 20px rgba(0,0,0,0.45);
  --shadow-tile: 0 2px 0 rgba(0,0,0,0.35);
  /* font */
  --font-sans: 'Cormorant Garamond', 'EB Garamond', serif;
  --font-display: 'Cinzel', 'Cormorant Garamond', serif;
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
  --ease-standard: cubic-bezier(0.3, 0, 0.2, 1);
  /* extra (signature gradients, composite borders, filters) */
  --tesserae-gradient: linear-gradient(135deg, #caa036 0%, #d4af37 20%, #b8860b 40%, #d4af37 60%, #caa036 80%, #b8860b 100%);
  --tile-grid: repeating-linear-gradient(45deg, rgba(0,0,0,0.12) 0 2px, transparent 2px 8px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Byzantine Mosaic — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#0d1b3d",
        "surface": "#142a5c",
        "surface-2": "#1c3a7a",
        "text": "#f5e6b8",
        "text-muted": "#c9b57a",
        "primary": "#d4af37",
        "accent": "#7a1f3d",
        "emerald-tile": "#1f6b4a",
        "gold-ground": "#caa036",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "8px",
        "pill": "999px",
      },
      boxShadow: {
        "gold-glow": "0 0 20px rgba(212,175,55,0.40), 0 8px 20px rgba(0,0,0,0.45)",
        "tile": "0 2px 0 rgba(0,0,0,0.35)",
      },
      fontFamily: {
        "sans": ["'Cormorant Garamond'", "'EB Garamond'", "serif"],
        "display": ["'Cinzel'", "'Cormorant Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.3, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --tesserae-gradient: linear-gradient(135deg, #caa036 0%, #d4af37 20%, #b8860b 40%, #d4af37 60%, #caa036 80%, #b8860b 100%);
//   --tile-grid: repeating-linear-gradient(45deg, rgba(0,0,0,0.12) 0 2px, transparent 2px 8px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Gold `--tesserae-gradient` fill over `--tile-grid` texture, near-square radius, deep-navy label text for contrast. |
| **Input** | Sapphire surface field with a thin gold-ground border; focus adds the gold-glow shadow. |
| **Card** | Deep sapphire panel bordered by a tessellated gold-ground frame (`--tile-grid` on the edge), ruby or emerald accent corner. |
| **Nav** | Sapphire bar with a gold tesserae strip along the bottom, wordmark set in the display serif. |
| **Modal** | Panel is bordered on all sides by the tessellated gold frame; backdrop dims to near-black. |
| **Table** | Header row in gold-ground gradient; body rows alternate sapphire surfaces with hairline tile-grid dividers. |
| **Tooltip** | Small ruby or emerald bubble with a thin gold rule, no soft blur — mosaics are crisp-edged. |
| **Badge** | Small tile-grid-textured pill in emerald or ruby with a gold hairline border. |
| **Toggle** | Track as a gold tesserae strip; knob is a solid jewel-tone (ruby/emerald) tile. |
| **Loading** | A ring of small gold tesserae blocks lighting up in sequence, like tiles catching candlelight. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#f5e6b8, warm gold-white) on `--color-bg` (#0d1b3d, deep sapphire) — verify with `contrast_check.py`; this pairing is comfortably above AA (well over 7:1).
- The gold-on-gold gradient button needs a deep navy or near-black label color, not the light `--color-text` value, or contrast collapses against the bright gold fill.
- `--color-text-muted` (#c9b57a) on `--color-surface-2` (#1c3a7a) should be checked directly — muted gold on mid-blue is the tightest pairing in this palette.
- Keep the tessellated tile-grid texture purely decorative behind text, never layered as a busy pattern directly under body copy at full opacity.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep the ground luminous gold via a diagonal shimmer gradient, never a flat solid gold fill.
- ✅ Bound every panel in the tessellated tile-grid border — it's the connective tissue of the style.
- ✅ Reserve jewel tones (sapphire, emerald, ruby) for large fields; use gold as the connective frame and accent.

## Don't

- ❌ Round corners generously — mosaics are geometric and tessellated, not soft; keep radii small.
- ❌ Blur or feather edges — every tile edge is crisp, unlike lunarpunk's soft glow language.
- ❌ Overload the palette with pastels or neon — jewel tones and gold only, nothing candy-colored.

## Don't confuse this with…

*Commonly confused neighbors:* persian-miniature, art-nouveau, maximalism.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
