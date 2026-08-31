# Daguerreotype — Implementation Spec

*Aliases:* daguerrean portrait style, early photographic plate, tintype-adjacent  
*Slug:* `daguerreotype` · *Category:* historical · *Era:* 1839–1860s

**Origin.** Earliest commercially viable photographic process, invented by Louis Daguerre; formal studio portraiture in silver-plated copper.

**Reference example.** Southworth & Hawes studio portraits; early 1840s American daguerreotype cases.

## Signature move(s)

A silvery, warm-neutral tonal range — never pure black-and-white, always leaning slightly sepia-silver — sits inside a soft radial vignette that darkens gently toward the edges, as if lit by a single studio window. Portraits and cards are held inside an oval or gilt-edge frame motif, and every surface stays formally still: no motion blur, no scratches, no film grain — this is composed stillness, the opposite of a distressed VHS or CRT texture.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Silvery monochrome tonal range with warm sepia-silver undertone
- Soft vignette falloff darkening toward the edges
- Oval or gilt-edge framing motifs around portraits and cards
- Quiet, formal stillness — no grain, scratches, or VHS/CRT artifacts

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/daguerreotype.css`.)

```css
/* Daguerreotype — design tokens (generated from style_catalog.json) */
/* 1839–1860s | Earliest commercially viable photographic process. */
:root {
  /* color */
  --color-bg: #d9d2c4;
  --color-surface: #eae5da;
  --color-surface-2: #c9c0ac;
  --color-text: #2b2621;
  --color-text-muted: #5c5347;
  --color-primary: #4a4238;
  --color-accent: #8a6d3a;
  --color-silver: #b8b2a0;
  --color-sepia: #6b5a3f;
  /* radius */
  --radius-sm: 4px;
  --radius-md: 10px;
  --radius-lg: 40px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-vignette: inset 0 0 60px rgba(20,16,10,0.45);
  --shadow-plate: 0 6px 20px rgba(20,16,10,0.30);
  /* blur */
  --blur-soft-focus: 6px;
  /* font */
  --font-sans: 'Cormorant', 'EB Garamond', serif;
  --font-display: 'Playfair Display', 'Cormorant', serif;
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
  --vignette-gradient: radial-gradient(ellipse at center, transparent 40%, rgba(20,16,10,0.55) 100%);
  --gilt-edge: 0 0 0 3px #8a6d3a, 0 0 0 5px #d9d2c4;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Daguerreotype — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#d9d2c4",
        "surface": "#eae5da",
        "surface-2": "#c9c0ac",
        "text": "#2b2621",
        "text-muted": "#5c5347",
        "primary": "#4a4238",
        "accent": "#8a6d3a",
        "silver": "#b8b2a0",
        "sepia": "#6b5a3f",
      },
      borderRadius: {
        "sm": "4px",
        "md": "10px",
        "lg": "40px",
        "pill": "999px",
      },
      boxShadow: {
        "vignette": "inset 0 0 60px rgba(20,16,10,0.45)",
        "plate": "0 6px 20px rgba(20,16,10,0.30)",
      },
      fontFamily: {
        "sans": ["'Cormorant'", "'EB Garamond'", "serif"],
        "display": ["'Playfair Display'", "'Cormorant'", "serif"],
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
//   --vignette-gradient: radial-gradient(ellipse at center, transparent 40%, rgba(20,16,10,0.55) 100%);
//   --gilt-edge: 0 0 0 3px #8a6d3a, 0 0 0 5px #d9d2c4;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Umber-silver fill, thin gilt border, subtle plate shadow; no hover glow, just a slight lift. |
| **Input** | Silvery surface field with a thin sepia underline, quiet and undecorated. |
| **Card** | Oval-radius (`--radius-lg`) surface with the vignette gradient overlaid and a `--gilt-edge` frame. |
| **Nav** | Muted silver bar, thin sepia rule beneath, wordmark in the display serif, no bright accent color. |
| **Modal** | Panel framed in `--gilt-edge`, vignette gradient darkening its corners, fades in with no motion blur. |
| **Table** | Quiet hairline rules in sepia, header row in a slightly darker silver, no zebra striping. |
| **Tooltip** | Small oval-ish bubble, thin gilt rule, soft-focus blur at the very edge only. |
| **Badge** | Small oval gilt-edged badge holding a single sepia-toned word, no bright fill. |
| **Toggle** | Track as a thin silver rail; knob is a small gilt-rimmed disc that slides without glow. |
| **Loading** | A slow single vignette pulse (brightness breathing at the center), never a spinning ring. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#2b2621, near-black warm umber) on `--color-bg` (#d9d2c4, warm silver) — verify with `contrast_check.py`; passes AA cleanly (well above 7:1).
- The vignette gradient must never sit directly under body text at full strength — reserve it for card/frame edges and image-like surfaces, not text containers.
- `--blur-soft-focus` is for decorative edge treatment only (e.g. a photo-plate corner); never apply it to interactive controls or text.
- Keep focus rings a solid, visible accent (gilt or dark umber) with real offset — the low-contrast, quiet palette makes a crisp focus ring especially necessary.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep the palette a narrow silver-to-sepia range — no saturated hues at all.
- ✅ Use the vignette and gilt-edge frame together to suggest a studio portrait plate, especially on cards and modals.
- ✅ Let transitions stay slow, quiet, and still — this style is composed calm, not kinetic energy.

## Don't

- ❌ Add scratches, dust, static, or scanline texture — that's VHS-glitch/grunge territory, not this formal studio look.
- ❌ Use saturated color accents — daguerreotype is a monochrome-plus-gilt palette only.
- ❌ Animate with bounce, glow pulses, or fast easing — stillness is the point.

## Don't confuse this with…

*Commonly confused neighbors:* vhs-glitch, vintage-print, grunge.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
