# Populuxe — Implementation Spec

*Aliases:* atomic populuxe, jet-age consumer style, boomerang modern  
*Slug:* `populuxe` · *Category:* historical · *Era:* 1950s–early 1960s

**Origin.** Term coined by journalist Thomas Hine to describe postwar American consumer design — the optimistic, mass-market graphic and product language of appliance ads, diner menus, and car showrooms during the atomic-age economic boom.

**Reference example.** 1950s Frigidaire and Chevrolet print ads; Googie coffee-shop signage photographed in period brochures; boomerang-pattern Formica countertops.

## Signature move(s)

Two-tone pastel color blocking (turquoise + pink, or coral + mint) set against warm cream, trimmed in bright chrome-silver linework, with atomic starburst and boomerang shapes scattered as optimistic punctuation — never as a dense pattern, always as a handful of confident accents pointing toward "the future is now." Display type is bold, italicized, and slightly wedge-shaped, like a car's tailfin caught mid-motion.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Two-tone pastel blocking (turquoise/pink/coral/mint) on warm cream, trimmed in chrome silver
- Atomic starburst and boomerang accent shapes, used sparingly as optimistic punctuation
- Bold italic wedge-shaped display type evoking tailfins and forward motion
- Gold accent for "premium" consumer-goods moments (appliance badges, price tags)

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/populuxe.css`.)

```css
/* Populuxe — design tokens (generated from style_catalog.json) */
/* 1950s–early 1960s | Two-tone pastel-and-chrome atomic-age consumer optimism. */
:root {
  /* color */
  --color-bg: #f4ede0;
  --color-surface: #fffaf3;
  --color-surface-2: #ffe3ec;
  --color-text: #2b2320;
  --color-text-muted: #6b5f56;
  --color-primary: #ff6f61;
  --color-accent: #1fb5a3;
  --color-chrome: #c8ccd0;
  --color-gold: #d4af37;
  /* radius */
  --radius-sm: 4px;
  --radius-md: 10px;
  --radius-lg: 20px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-chrome: 0 0 0 1px #ffffff, 0 0 0 2px var(--color-chrome), 0 8px 20px rgba(43,35,32,0.18);
  --shadow-starburst: 0 10px 24px rgba(255,111,97,0.25);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Futura', 'Century Gothic', 'Trebuchet MS', sans-serif;
  --font-display: 'Futura', 'Century Gothic', sans-serif;
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
  /* extra (starburst motif, boomerang sweep, chrome trim) */
  --starburst: conic-gradient(from 0deg, var(--color-primary) 0 6deg, transparent 6deg 30deg, var(--color-accent) 30deg 36deg, transparent 36deg 60deg, var(--color-gold) 60deg 66deg, transparent 66deg 90deg);
  --boomerang-sweep: linear-gradient(100deg, var(--color-surface-2) 0 38%, transparent 38% 62%, rgba(31,181,163,0.16) 62% 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Populuxe — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f4ede0",
        "surface": "#fffaf3",
        "surface-2": "#ffe3ec",
        "text": "#2b2320",
        "text-muted": "#6b5f56",
        "primary": "#ff6f61",
        "accent": "#1fb5a3",
        "chrome": "#c8ccd0",
        "gold": "#d4af37",
      },
      borderRadius: {
        "sm": "4px",
        "md": "10px",
        "lg": "20px",
        "pill": "999px",
      },
      boxShadow: {
        "chrome": "0 0 0 1px #ffffff, 0 0 0 2px #c8ccd0, 0 8px 20px rgba(43,35,32,0.18)",
        "starburst": "0 10px 24px rgba(255,111,97,0.25)",
      },
      fontFamily: {
        "sans": ["'Futura'", "'Century Gothic'", "'Trebuchet MS'", "sans-serif"],
        "display": ["'Futura'", "'Century Gothic'", "sans-serif"],
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
//   --starburst: conic-gradient(from 0deg, #ff6f61 0 6deg, transparent 6deg 30deg, #1fb5a3 30deg 36deg, transparent 36deg 60deg, #d4af37 60deg 66deg, transparent 66deg 90deg);
//   --boomerang-sweep: linear-gradient(100deg, #ffe3ec 0 38%, transparent 38% 62%, rgba(31,181,163,0.16) 62% 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Coral pill fill with a chrome double-ring border (`--shadow-chrome`); bold italic wedge label. |
| **Input** | Cream well trimmed with a thin chrome border; focus state adds a turquoise underline sweep. |
| **Card** | Pink or mint surface-2 block with a `--boomerang-sweep` diagonal wash and a small gold starburst in one corner. |
| **Nav** | Cream bar with a chrome bottom trim line and one small starburst mark beside the wordmark. |
| **Modal** | Two-tone panel: cream body, turquoise header band with a chrome trim seam between them. |
| **Table** | Alternating pink/mint tinted rows; header row in solid coral with chrome trim underneath. |
| **Tooltip** | Small chrome-trimmed pill, coral fill, boomerang-shaped tail instead of a plain triangle. |
| **Badge** | Starburst-shaped chip (or pill with a tiny starburst glyph) in gold for "new/premium" callouts. |
| **Toggle** | Chrome-trimmed track; knob is a gold starburst disc when on, plain chrome disc when off. |
| **Loading** | Rotating starburst rays (`--starburst`), like a spinning atomic emblem. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `--color-text` (#2b2320) on `--color-bg` (#f4ede0): approximate contrast is roughly 11:1 — passes WCAG AA and AAA comfortably.
- Pastel-on-pastel is the real risk: never set body text directly on `--color-surface-2` (pink) without checking — prefer `--color-text` there too, which still clears ~9:1 against #ffe3ec.
- Chrome trim and starburst accents are decorative; buttons and links must carry contrast from fill/label color, not from the chrome ring alone.
- Coral `--color-primary` (#ff6f61) as a text color on cream fails AA for small text (~2.8:1) — reserve coral for large display headlines (≥24px bold) or fills with dark/white label text, never for small body copy.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep starburst/boomerang motifs sparse — 1–2 per composition reads as confident, more than that reads as pattern noise.
- ✅ Use chrome trim as a thin double-line accent, not a heavy 3D bevel — populuxe chrome is a bright line, not a skeuomorphic knob.
- ✅ Let cream carry most of the background; pastels are accent blocks, not the whole canvas.

## Don't

- ❌ Confuse this with Googie's architectural angularity or streamline-moderne's aerodynamic curves — populuxe is graphic/product-ad styling, softer and more pastel.
- ❌ Use coral or turquoise as small body-text color on light backgrounds — check contrast first.
- ❌ Over-skeuomorph the chrome into heavy 3D bevels; keep it a flat bright trim line.

## Don't confuse this with…

*Commonly confused neighbors:* googie, streamline-moderne, mid-century-modern.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
