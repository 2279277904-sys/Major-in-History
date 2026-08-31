# Chalkboard Lettering — Implementation Spec

*Aliases:* chalk art, cafe chalkboard style, hand-lettered chalk  
*Slug:* `chalkboard-lettering` · *Category:* historical · *Era:* 20th century–present (modern chalk-art revival)

**Origin.** Café and market chalkboard signage, revived as a hand-lettering art form in the 2010s.

**Reference example.** Dana Tanamachi chalk lettering; neighborhood café menu boards.

## Signature move(s)

A matte near-black slate ground carries hand-lettered display type built from textured chalk-white and pastel chalk-dust strokes — every letterform sits a little off true, with doodled flourishes, underlines, and swashes filling the leftover space the way a barista fills a menu board before opening. Nothing is vector-crisp: edges carry a faint grain, and shapes lean, wobble, and overlap the way a hand holding actual chalk would draw them.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Matte near-black/slate backgrounds with textured chalk-white and pastel chalk-dust strokes
- Playful hand-drawn display lettering with varied stroke weight
- Doodled flourishes, underlines, and borders framing text
- Slightly uneven, hand-drawn edges on every shape

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/chalkboard-lettering.css`.)

```css
/* Chalkboard Lettering — design tokens (generated from style_catalog.json) */
/* 20th century–present | Café/market chalkboard signage revived as hand-lettering art. */
:root {
  /* color */
  --color-bg: #1f2421;
  --color-surface: #262b27;
  --color-surface-2: #323830;
  --color-text: #f5f5f0;
  --color-text-muted: #b8bdb4;
  --color-primary: #f5f5f0;
  --color-accent: #f4a6c1;
  --color-chalk-teal: #8fd9c4;
  --color-chalk-yellow: #f5e08a;
  /* radius */
  --radius-sm: 3px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-chalk-dust: 0 2px 6px rgba(0,0,0,0.40);
  --shadow-chalk-glow: 0 0 8px rgba(245,245,240,0.18);
  /* blur */
  --blur-dust: 0.4px;
  /* font */
  --font-sans: 'Patrick Hand', 'Comic Neue', cursive;
  --font-display: 'Caveat', 'Kalam', cursive;
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
  --ease-standard: cubic-bezier(0.34, 1.2, 0.64, 1);
  /* extra (signature gradients, composite borders, filters) */
  --chalk-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.03) 0 1px, transparent 1px), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.025) 0 1px, transparent 1px);
  --wobble: rotate(-0.4deg);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Chalkboard Lettering — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1f2421",
        "surface": "#262b27",
        "surface-2": "#323830",
        "text": "#f5f5f0",
        "text-muted": "#b8bdb4",
        "primary": "#f5f5f0",
        "accent": "#f4a6c1",
        "chalk-teal": "#8fd9c4",
        "chalk-yellow": "#f5e08a",
      },
      borderRadius: {
        "sm": "3px",
        "md": "8px",
        "lg": "16px",
        "pill": "999px",
      },
      boxShadow: {
        "chalk-dust": "0 2px 6px rgba(0,0,0,0.40)",
        "chalk-glow": "0 0 8px rgba(245,245,240,0.18)",
      },
      fontFamily: {
        "sans": ["'Patrick Hand'", "'Comic Neue'", "cursive"],
        "display": ["'Caveat'", "'Kalam'", "cursive"],
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
        "standard": "cubic-bezier(0.34, 1.2, 0.64, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --chalk-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.03) 0 1px, transparent 1px), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.025) 0 1px, transparent 1px);
//   --wobble: rotate(-0.4deg);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Chalk-white hand-drawn outline on slate, label in the display cursive font, a slight `--wobble` rotation. |
| **Input** | Slate field with a single chalk-white underline stroke (not a full box) and chalk-dust texture behind it. |
| **Card** | Slate surface with `--chalk-texture` overlay and a hand-drawn doodled border/underline flourish under the title. |
| **Nav** | Near-black bar, wordmark in chalk display lettering with a hand-drawn underline swash beneath it. |
| **Modal** | Panel "chalks in" with a quick fade/scale, doodled corner flourishes, chalk-dust shadow. |
| **Table** | Hand-drawn-looking chalk rules between rows (slightly uneven), header row in pastel chalk-yellow. |
| **Tooltip** | Small slate bubble with a chalk-white hand-drawn outline and a doodled arrow instead of a clean triangle. |
| **Badge** | Circled-in-chalk pill (pastel teal or pink stroke, no fill) like a menu-board "NEW" callout. |
| **Toggle** | Track drawn as a chalk-outlined rail; knob is a filled chalk-white circle with a faint dust shadow. |
| **Loading** | A hand-drawn circular chalk stroke redrawing itself in a loop, like someone re-tracing a circle. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#f5f5f0, chalk white) on `--color-bg` (#1f2421, matte slate) — verify with `contrast_check.py`; passes AA very comfortably (well above 12:1).
- Pastel chalk accents (`--color-accent` #f4a6c1, `--color-chalk-teal` #8fd9c4, `--color-chalk-yellow` #f5e08a) are decorative strokes, not body-text colors — check each individually against slate before using it for any text, since pastels are lower contrast than the primary chalk white.
- Cursive display lettering (`--font-display`) is for headlines/short labels only; keep body copy in the more legible `--font-sans` hand-print face.
- The wobble/rotation effect must stay small (a degree or two) and never applied to focus rings or hit-testable control boundaries — keep the actual clickable box rectangular and full-size even if its drawn outline wobbles.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every stroke slightly uneven — a hairline of grain/wobble reads as "drawn by hand," not "rendered."
- ✅ Reserve the pastel chalk colors (teal, yellow, pink) for accents and doodles, keep body copy in chalk white.
- ✅ Add small hand-drawn flourishes (underlines, swashes, stars) as connective decoration between elements.

## Don't

- ❌ Use a crisp, vector-perfect sans-serif for headlines — that undercuts the entire hand-lettered premise.
- ❌ Add heavy grain, scratches, or scanline noise across the whole surface — that's grunge/VHS-glitch territory, not this clean matte-slate look.
- ❌ Overpopulate the board with unrelated flat-color illustration blocks — that drifts toward folk-art-naive; keep the visual language to chalk strokes and lettering.

## Don't confuse this with…

*Commonly confused neighbors:* folk-art-naive, grunge, punk-diy.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
