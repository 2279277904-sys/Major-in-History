# Cubism — Implementation Spec

*Aliases:* synthetic cubism, papier collé, faceted design  
*Slug:* `cubism` · *Category:* historical · *Era:* 1907–1920s (spec targets synthetic phase, c.1912–1919)

**Origin.** Paris, Pablo Picasso and Georges Braque, developing from analytic cubism's monochrome fracturing (1907–1912) into synthetic cubism's collaged, multi-colored planes (1912 onward) — the addition of papier collé, stenciled lettering, and flatter, bolder shapes.

**Reference example.** Picasso's *Three Musicians* and *Still Life with Chair Caning*; Braque's papier collé compositions; Juan Gris's synthetic-period still lifes.

## Signature move(s)

Overlapping, faceted planes seen from multiple angles at once, laid down like collaged paper cutouts — each plane a flat, slightly-off-register color with a thin black contour, planes intentionally overlapping their neighbors by a few pixels/degrees rather than sitting in clean isolation. Surfaces read as *assembled* rather than rendered: torn/cut paper edges, stenciled capital lettering fragments, faux-wood-grain or newsprint textures collaged in as background fill.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Fragmented, overlapping geometric planes viewed from multiple simultaneous perspectives
- Muted earthy ground (ochre, umber, black) punctuated by bolder collage color (sienna, blue)
- Thin black contour lines separating each plane, planes overlapping at odd angles
- Stenciled/fragmented lettering and collaged paper textures as period-accurate flourishes

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/cubism.css`.)

```css
/* Cubism — design tokens (generated from style_catalog.json) */
/* 1907–1920s | Fragmented multi-perspective planes, synthetic-cubism collage palette. */
:root {
  /* color */
  --color-bg: #e8dcc3;
  --color-surface: #f2e9d8;
  --color-surface-2: #d9c9a3;
  --color-text: #1c1610;
  --color-text-muted: #5c4f3a;
  --color-primary: #b5451f;
  --color-accent: #2b4c6f;
  --color-ochre: #c68a2e;
  --color-ink: #16130f;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 2px;
  --radius-lg: 4px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-facet: 3px 3px 0 var(--color-ink);
  --shadow-collage: 0 6px 18px rgba(22,19,15,0.28);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Arial', 'Helvetica Neue', sans-serif;
  --font-display: 'Georgia', 'Times New Roman', serif;
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
  /* extra (facet planes, collage paper texture) */
  --facet-gradient: linear-gradient(115deg, rgba(181,69,31,0.14) 0 32%, rgba(43,76,111,0.12) 32% 61%, rgba(198,138,46,0.16) 61% 100%);
  --collage-paper: repeating-linear-gradient(4deg, rgba(22,19,15,0.04) 0 2px, transparent 2px 6px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Cubism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#e8dcc3",
        "surface": "#f2e9d8",
        "surface-2": "#d9c9a3",
        "text": "#1c1610",
        "text-muted": "#5c4f3a",
        "primary": "#b5451f",
        "accent": "#2b4c6f",
        "ochre": "#c68a2e",
        "ink": "#16130f",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "facet": "3px 3px 0 #16130f",
        "collage": "0 6px 18px rgba(22,19,15,0.28)",
      },
      fontFamily: {
        "sans": ["'Arial'", "'Helvetica Neue'", "sans-serif"],
        "display": ["'Georgia'", "'Times New Roman'", "serif"],
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
//   --facet-gradient: linear-gradient(115deg, rgba(181,69,31,0.14) 0 32%, rgba(43,76,111,0.12) 32% 61%, rgba(198,138,46,0.16) 61% 100%);
//   --collage-paper: repeating-linear-gradient(4deg, rgba(22,19,15,0.04) 0 2px, transparent 2px 6px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Ochre or sienna fill with a hard black contour and a 3px offset facet shadow (`--shadow-facet`); label set in condensed serif caps. |
| **Input** | Cream well with a thin black contour, a faint diagonal facet gradient bleeding in from one corner. |
| **Card** | Layered "collage": base cream panel, an ochre plane and a blue plane overlapping its top-right corner at a slight rotation, each edged in black. |
| **Nav** | Flat ink bar with sienna and ochre facet fragments cut into the bottom edge instead of a straight border. |
| **Modal** | Panel assembled from 2–3 overlapping colored planes behind the content, like torn collage paper. |
| **Table** | Header row rendered as an ochre facet plane; body rows flat cream with hairline black rules. |
| **Tooltip** | Small angular sienna chip with a hard black contour, no rounding, no blur. |
| **Badge** | Faceted parallelogram (skewed rectangle) with black contour, ochre or blue fill. |
| **Toggle** | Track drawn as two overlapping facet planes; knob is a black-contoured circle that slides between them. |
| **Loading** | Sequence of 3–4 facet planes fading in/out in rotation, evoking a shifting cubist plane rather than a spinner. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `--color-text` (#1c1610) on `--color-bg` (#e8dcc3): approximate luminance contrast is roughly 12:1 — comfortably passes WCAG AA (4.5:1) and AAA (7:1) for normal text.
- Facet-plane backgrounds behind text must never drop below the same contrast ratio — place text only on the flat cream/ochre surfaces, not across a facet seam where two colors meet.
- Hard black contour lines are decorative, not a substitute for a visible focus ring; keep a distinct focus-visible outline in `--color-accent` at 2px+ with offset.
- Collage paper texture (`--collage-paper`) must stay under ~5% opacity so it never reduces effective text contrast.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Overlap planes deliberately — a few degrees of rotation and a few px of overlap is what reads as "assembled," not messy.
- ✅ Keep contour lines thin, hard, and black — they're the connective tissue that makes fragmented planes read as one object.
- ✅ Reserve the bolder sienna/blue collage colors for a minority of the surface; let muted ochre/cream carry most of the composition.

## Don't

- ❌ Round any corners — cubism's planes are cut paper, not soft shapes; that's `--radius-sm: 0`, always.
- ❌ Let facets overlap directly on top of body copy — legibility comes first, decoration second.
- ❌ Drift into full analytic-cubism monochrome grey — this spec's palette is the warmer, bolder synthetic/collage phase.

## Don't confuse this with…

*Commonly confused neighbors:* art-deco, constructivism, memphis-design.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
