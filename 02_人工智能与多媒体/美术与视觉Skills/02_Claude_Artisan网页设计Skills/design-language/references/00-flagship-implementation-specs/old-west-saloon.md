# Old West / Saloon — Implementation Spec

*Aliases:* wanted poster style, wild west, frontier design  
*Slug:* `old-west-saloon` · *Category:* niche · *Era:* 1860s–1900s

**Origin.** The American frontier's own visual output — wanted posters, saloon signage, trading-post notices — produced with wood type, weathered by sun and handling.

**Reference example.** 19th-century wanted posters; hand-lettered saloon signage; frontier trading-post notices printed with wood type.

## Signature move(s)

Every surface carries a distressed wood-grain or aged-paper texture — nothing here is pristine or new. Headlines are set in tall, condensed wood-type display lettering, the way a WANTED poster shouts a name, over a deep burnt-sienna and dusty-gold palette. Star badges and rope-border framing appear as recurring frontier hardware, tying the whole system back to sheriff's-office and trading-post materials.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Distressed wood-grain and aged-paper textures on every surface
- Deep burnt-sienna and dusty-gold palette
- Tall, condensed wood-type display lettering (WANTED-poster register)
- Star-badge and rope-border motifs as recurring frontier hardware

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/old-west-saloon.css`.)

```css
/* Old West / Saloon — design tokens (generated from style_catalog.json) */
/* 1860s–1900s | American frontier wanted-poster and saloon-sign aesthetic. */
:root {
  /* color */
  --color-bg: #e8d9b8;
  --color-surface: #f0e4c8;
  --color-surface-2: #d8c397;
  --color-text: #2c1608;
  --color-text-muted: #6b4a28;
  --color-primary: #7a2e17;
  --color-accent: #c99a3b;
  --color-sienna: #8a3d1f;
  --color-star: #3a3226;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-weathered: 0 8px 20px rgba(44,22,8,0.28);
  --shadow-weathered-sm: 0 3px 10px rgba(44,22,8,0.24);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Roboto Slab', 'Georgia', serif;
  --font-display: 'Rye', 'Ultra', 'Impact', 'Arial Black', serif;
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
  --paper-grain: repeating-radial-gradient(circle at 25% 30%, rgba(44,22,8,0.06) 0px, transparent 3px, transparent 9px), repeating-linear-gradient(4deg, rgba(44,22,8,0.04) 0 1px, transparent 1px 6px);
  --rope-frame: repeating-linear-gradient(135deg, #7a2e17 0 3px, #c99a3b 3px 6px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Old West / Saloon — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#e8d9b8",
        "surface": "#f0e4c8",
        "surface-2": "#d8c397",
        "text": "#2c1608",
        "text-muted": "#6b4a28",
        "primary": "#7a2e17",
        "accent": "#c99a3b",
        "sienna": "#8a3d1f",
        "star": "#3a3226",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "8px",
        "pill": "999px",
      },
      boxShadow: {
        "weathered": "0 8px 20px rgba(44,22,8,0.28)",
        "weathered-sm": "0 3px 10px rgba(44,22,8,0.24)",
      },
      fontFamily: {
        "sans": ["'Roboto Slab'", "'Georgia'", "serif"],
        "display": ["'Rye'", "'Ultra'", "'Impact'", "'Arial Black'", "serif"],
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
//   --paper-grain: repeating-radial-gradient(circle at 25% 30%, rgba(44,22,8,0.06) 0px, transparent 3px, transparent 9px), repeating-linear-gradient(4deg, rgba(44,22,8,0.04) 0 1px, transparent 1px 6px);
//   --rope-frame: repeating-linear-gradient(135deg, #7a2e17 0 3px, #c99a3b 3px 6px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Dusty-gold-bordered wood-tone fill with a hard weathered shadow; primary button in burnt-sienna with cream label. |
| **Input** | Aged-paper field with a 2px sienna border, no rounding beyond a hair. |
| **Card** | Aged-paper surface with `--paper-grain`, thick sienna border, deep weathered drop shadow — like a nailed-up notice. |
| **Nav** | Wood-tone bar with a thick burnt-sienna rule beneath, display-face wordmark. |
| **Modal** | Panel appears like a notice being tacked up — quick snap, no bounce, weathered shadow. |
| **Table** | Header row set in the display face, uppercase; row dividers as thin sienna hairlines on aged paper. |
| **Tooltip** | Small paper chip with a thin sienna border, slight grain, no blur or glow. |
| **Badge** | Dusty-gold pill with a sienna border and a small star glyph, echoing a sheriff's badge. |
| **Toggle** | Track rendered as a mini `--rope-frame` strip; knob is a solid star-dark circle. |
| **Loading** | A star-shape or rope-coil spinner rotating with a slight mechanical stutter, not smooth. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Deep brown-black text (`--color-text: #2c1608`) on the dusty-gold ground (`--color-bg: #e8d9b8`) measures roughly 12.3:1 — verify every pairing with `contrast_check.py`, and re-check `--color-text-muted` on `--color-surface-2` (~5.7:1) if either value shifts.
- Keep `--paper-grain` restricted to backgrounds/cards, never layered directly under small body text at low opacity — it can blur letterforms at small sizes.
- Condensed wood-type display faces can crush legibility at body-text sizes — reserve the display font for headlines/badges and keep paragraph copy in the slab-serif sans.
- Keep focus rings a solid, high-contrast dashed outline (star-dark) since the weathered texture can visually compete with a default browser ring.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every surface visibly weathered — grain, mild distress, uneven ink.
- ✅ Reserve the tall condensed display face for headlines and badges, not body copy.
- ✅ Let star-badge and rope-border motifs recur as a system, not a one-off illustration.

## Don't

- ❌ Reach for chrome, neon, or mid-century diner colors — that's americana-diner's 1950s register, not 1880s frontier.
- ❌ Clean up the texture into a flat, pristine surface — the aging is structural to the style.
- ❌ Overuse red/blue Americana bunting — this palette stays earthy (sienna/gold), not patriotic red-white-blue.

## Don't confuse this with…

*Commonly confused neighbors:* americana-diner, woodcut-linocut, nautical-maritime.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
