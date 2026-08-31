# Nautical / Maritime — Implementation Spec

*Aliases:* yacht club style, sailing aesthetic, naval design  
*Slug:* `nautical-maritime` · *Category:* niche · *Era:* 1850s–present

**Origin.** Visual language of sailing and coastal life: naval uniform stripes, signal-flag systems, rope craft, and brass ship fittings, later adopted by New England yacht clubs and coastal resort branding.

**Reference example.** International maritime signal flags; brass ship instruments and portholes; New England yacht club burgees and uniforms.

## Signature move(s)

Crisp navy-and-white stripe fields anchor every composition, bordered by a rope-texture edge treatment (a twisted or whipped-rope pattern, never a plain line), with brass and rope-tan as the only warm accents. Anchor and signal-flag iconography appears as considered detail, not clutter — the overall feeling is deck-of-a-ship confidence: clean, ordered, disciplined.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Navy and white stripe fields as the primary pattern language
- Rope-texture borders (twisted/whipped rope, not a plain rule)
- Brass and rope-tan as the sole warm accent colors
- Anchor and signal-flag iconography, crisp deck-of-a-ship precision

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/nautical-maritime.css`.)

```css
/* Nautical / Maritime — design tokens (generated from style_catalog.json) */
/* 1850s–present | Sailing and coastal visual tradition: navy stripes, rope, brass. */
:root {
  /* color */
  --color-bg: #f4f6f8;
  --color-surface: #ffffff;
  --color-surface-2: #e4e9ee;
  --color-text: #0b1f38;
  --color-text-muted: #51667e;
  --color-primary: #0b1f38;
  --color-accent: #b3391f;
  --color-brass: #b8873a;
  --color-rope-tan: #d9c49a;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 6px;
  --radius-lg: 12px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-deck: 0 8px 20px rgba(11,31,56,0.14);
  --shadow-deck-sm: 0 3px 10px rgba(11,31,56,0.12);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Inter', 'Helvetica Neue', system-ui, sans-serif;
  --font-display: 'Oswald', 'Helvetica Neue', sans-serif;
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
  --ease-standard: cubic-bezier(0.2, 0, 0.1, 1);
  /* extra (signature gradients, composite borders, filters) */
  --stripe-field: repeating-linear-gradient(90deg, #0b1f38 0 14px, #ffffff 14px 28px);
  --rope-border: repeating-linear-gradient(135deg, #b8873a 0 3px, #d9c49a 3px 6px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Nautical / Maritime — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f4f6f8",
        "surface": "#ffffff",
        "surface-2": "#e4e9ee",
        "text": "#0b1f38",
        "text-muted": "#51667e",
        "primary": "#0b1f38",
        "accent": "#b3391f",
        "brass": "#b8873a",
        "rope-tan": "#d9c49a",
      },
      borderRadius: {
        "sm": "2px",
        "md": "6px",
        "lg": "12px",
        "pill": "999px",
      },
      boxShadow: {
        "deck": "0 8px 20px rgba(11,31,56,0.14)",
        "deck-sm": "0 3px 10px rgba(11,31,56,0.12)",
      },
      fontFamily: {
        "sans": ["'Inter'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Oswald'", "'Helvetica Neue'", "sans-serif"],
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
        "standard": "cubic-bezier(0.2, 0, 0.1, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --stripe-field: repeating-linear-gradient(90deg, #0b1f38 0 14px, #ffffff 14px 28px);
//   --rope-border: repeating-linear-gradient(135deg, #b8873a 0 3px, #d9c49a 3px 6px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | White fill, sharp 2px navy border, minimal square-ish radius; primary button in solid navy with white text. |
| **Input** | White field with a crisp 2px navy border, no decoration — deck-clean. |
| **Card** | White surface with a thick navy top edge (like a stripe band) and a clean drop shadow, no texture inside. |
| **Nav** | Solid navy bar, brass rule beneath, white/rope-tan link text — like a ship's bridge signage. |
| **Modal** | Panel slides in cleanly (no bounce), navy border, deck shadow. |
| **Table** | Header row in navy with white uppercase text; row dividers as thin brass hairlines. |
| **Tooltip** | Small white chip with a thin navy border, crisp corners, no glow or blur. |
| **Badge** | Brass pill with a navy border and navy uppercase text, evokes a small brass plaque. |
| **Toggle** | Track rendered as a mini navy/white stripe field; knob is a solid brass circle. |
| **Loading** | A rope-knot spinner: the `--rope-border` pattern rotating steadily, no easing overshoot. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Deep navy text (`--color-text: #0b1f38`) on the crisp off-white ground (`--color-bg: #f4f6f8`) measures roughly 15.3:1 — verify every pairing with `contrast_check.py`, and re-check `--color-text-muted` on `--color-surface-2` (~5.5:1) if either value shifts.
- Brass (`--color-brass`) is a mid-value gold and fails AA for body text on white; use it only for borders, badges (with a navy border and navy text, not brass text), or thick decorative rules.
- Never render text directly on the raw `--stripe-field` pattern — restrict it to thin decorative bars, never a text-bearing surface.
- Keep focus rings a solid, high-contrast accent (the burnt-red `--color-accent`) so they read distinctly against both navy and white stripe fields.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep stripes crisp and evenly spaced — no soft, blurred, or hand-wavy edges.
- ✅ Reserve brass for accents and small hardware-like details, not large fills.
- ✅ Keep the overall feel disciplined and clean — this is a "polished deck," not a cluttered curio shelf.

## Don't

- ❌ Warm up the palette into orange/turquoise island tones — that drifts into tiki-tropical territory.
- ❌ Soften the rope border into a generic dashed line — it should read as an actual twisted-rope texture.
- ❌ Overload the surface with anchors, wheels, and starfish — one or two considered maritime icons beat a curio-shop pile.

## Don't confuse this with…

*Commonly confused neighbors:* tiki-tropical, americana-diner, old-west-saloon.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
