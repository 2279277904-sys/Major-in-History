# Street Art / Graffiti — Implementation Spec

*Aliases:* graffiti art, wildstyle lettering, spray-can art, writer culture
*Slug:* `street-art-graffiti` · *Category:* niche · *Era:* 1970s–present

**Origin.** Spray-can wall art and wildstyle lettering culture, born on New York City subway cars and handball courts in the 1970s, spreading into a global writer culture of tags, throw-ups, and burners.

**Reference example.** NYC subway car pieces of the 1970s–80s; contemporary legal wall "burners" and yard productions.

## Signature move(s)

Bold, interlocking bubble or wildstyle letterforms outlined in a hard black keyline plus a thin secondary pinstripe, filled with high-contrast spray-can color and set against a gritty concrete-grey ground textured with faint spray grain and paint drips.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Bold interlocking outlined "bubble" or "wildstyle" letterforms
- Drip and spray-can grain texture
- High-contrast fill colors with hard black keyline outlines
- Energetic, tagging-inspired composition on a concrete-grey ground

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/street-art-graffiti.css`.)

```css
/* Street Art / Graffiti — design tokens (generated from style_catalog.json) */
/* 1970s–present | Spray-can wall art and wildstyle lettering culture. */
:root {
  /* color */
  --color-bg: #2b2b2b;
  --color-surface: #383838;
  --color-surface-2: #454545;
  --color-text: #f5f5f0;
  --color-text-muted: #b8b8b0;
  --color-primary: #ff3b3b;
  --color-accent: #ffd400;
  --color-cyan: #26c6da;
  --color-keyline: #0a0a0a;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 8px;
  --radius-lg: 18px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-spray: 0 0 0 4px var(--color-keyline), 0 10px 24px rgba(0,0,0,0.45);
  --shadow-drip: 0 8px 0 -2px rgba(255,59,59,0.35), 0 12px 4px -4px rgba(0,0,0,0.4);
  /* font */
  --font-sans: 'Archivo Black', 'Helvetica Neue', system-ui, sans-serif;
  --font-display: 'Titan One', 'Archivo Black', 'Impact', sans-serif;
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
  --ease-standard: cubic-bezier(0.3, 0.9, 0.4, 1.2);
  /* extra (signature gradients, composite borders, filters) */
  --spray-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.05) 0, transparent 3%), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.04) 0, transparent 4%), radial-gradient(circle at 40% 80%, rgba(255,255,255,0.04) 0, transparent 3%);
  --wildstyle-outline: 0 0 0 3px var(--color-keyline), 0 0 0 5px var(--color-accent);
  --bg-image: linear-gradient(165deg, #383838 0%, #2b2b2b 55%, #1f1f1f 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Street Art / Graffiti — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#2b2b2b",
        "surface": "#383838",
        "surface-2": "#454545",
        "text": "#f5f5f0",
        "text-muted": "#b8b8b0",
        "primary": "#ff3b3b",
        "accent": "#ffd400",
        "cyan": "#26c6da",
        "keyline": "#0a0a0a",
      },
      borderRadius: {
        "sm": "2px",
        "md": "8px",
        "lg": "18px",
        "pill": "999px",
      },
      boxShadow: {
        "spray": "0 0 0 4px #0a0a0a, 0 10px 24px rgba(0,0,0,0.45)",
        "drip": "0 8px 0 -2px rgba(255,59,59,0.35), 0 12px 4px -4px rgba(0,0,0,0.4)",
      },
      fontFamily: {
        "sans": ["'Archivo Black'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Titan One'", "'Archivo Black'", "'Impact'", "sans-serif"],
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
        "standard": "cubic-bezier(0.3, 0.9, 0.4, 1.2)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --spray-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.05) 0, transparent 3%), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.04) 0, transparent 4%), radial-gradient(circle at 40% 80%, rgba(255,255,255,0.04) 0, transparent 3%);
//   --wildstyle-outline: 0 0 0 3px #0a0a0a, 0 0 0 5px #ffd400;
//   --bg-image: linear-gradient(165deg, #383838 0%, #2b2b2b 55%, #1f1f1f 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Hard black keyline box that upgrades to a full wildstyle double-outline (`--wildstyle-outline`) on hover, with a slight tag-like tilt. |
| **Input** | Dark field with a flat black keyline box, no gradient — reads like a stencilled label. |
| **Card** | Surface textured with `--spray-texture` grain, boxed by `--shadow-spray`'s thick keyline. |
| **Nav** | Dark concrete bar under a heavy black rule with a thin accent-yellow pinstripe beneath it. |
| **Modal** | Snaps in with a slight overshoot rotation, like a sticker slapped onto the wall. |
| **Table** | Alternating concrete rows, header row in the bubble display face with a keyline underline. |
| **Tooltip** | Small accent-yellow bubble, hard black keyline, no blur — a spray-stencil callout. |
| **Badge** | Yellow pill with dark ink text and a solid black keyline, like a paint-can cap sticker. |
| **Toggle** | Track as a black-keylined capsule; knob is a spray-filled circle that snaps (not glides) between states. |
| **Loading** | A can-cap dot filling in with color as if being sprayed, or a drip trailing downward and fading. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#f5f5f0) on `--color-bg` (#2b2b2b) is off-white on mid-dark concrete grey — passes AA comfortably; verify with `contrast_check.py`.
- `--color-text-muted` (#b8b8b0) on `--color-surface`/`--color-surface-2` stays above 4.5:1 — re-check if you lighten either surface.
- Dark-ink (`--color-keyline`) labels on the accent-yellow badge/tooltip fill are intentional and pass AA; the primary red at small sizes should carry light text, never dark-on-red.
- The spray-grain texture and drip shadows are decorative; never let grain opacity climb high enough to interfere with text legibility on a card.
- Rotation/overshoot "sticker slap" animations must respect `prefers-reduced-motion` — keep the keyline styling but drop the transform.
- Keep focus rings a solid cyan outline with real offset; the wildstyle double-outline is decorative, not a substitute for a focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every filled shape wrapped in a hard black keyline — that's what reads as "outlined letterform," not flat color.
- ✅ Ground everything on a concrete-grey surface with faint spray grain, never a clean white studio background.
- ✅ Let raised elements sit slightly off-axis (a degree or two of rotation) — hand-sprayed work is never perfectly square.

## Don't

- ❌ Drop the black keyline in favor of a soft drop-shadow — that loses the stencilled, spray-outlined feel entirely.
- ❌ Use pastel or muted color fills — graffiti fills are high-contrast, saturated spray-can color.
- ❌ Arrange everything in a rigid grid with zero tilt — that reads as corporate flat design, not writer culture.

## Don't confuse this with…

*Commonly confused neighbors:* punk-zine, grunge, comic.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
