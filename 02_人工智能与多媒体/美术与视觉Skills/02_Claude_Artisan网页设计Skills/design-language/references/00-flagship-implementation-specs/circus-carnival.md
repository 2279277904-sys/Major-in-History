# Circus / Carnival Poster — Implementation Spec

*Aliases:* circus poster, carnival midway, big top lettering, showman advertising
*Slug:* `circus-carnival` · *Category:* niche · *Era:* 1870s–1950s (revival ongoing)

**Origin.** Vintage traveling-circus and carnival midway advertising posters and handbills, especially American circus lithography of the Strobridge / Barnum & Bailey era.

**Reference example.** Barnum & Bailey circus posters; Strobridge Lithographing Co. bills; state-fair midway signage.

## Signature move(s)

A hard barber-pole stripe of poster red and cream, wrapped or framed around a gold starburst wash, sitting behind tall theatrical condensed display lettering ("STEP RIGHT UP" bill type) — the whole thing boxed by a heavy double-line scrolled border, like a hand-set letterpress bill.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Bold red/gold/cream striped and starburst backgrounds
- Tall theatrical condensed display lettering (bill/showman type)
- Ornate double-line scrolled borders
- High-energy showman excitement — "step right up" urgency

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/circus-carnival.css`.)

```css
/* Circus / Carnival Poster — design tokens (generated from style_catalog.json) */
/* 1870s–1950s (revival ongoing) | Vintage traveling-circus and carnival midway advertising. */
:root {
  /* color */
  --color-bg: #f2e6c9;
  --color-surface: #fdf8ec;
  --color-surface-2: #e8d6a8;
  --color-text: #241812;
  --color-text-muted: #5c4429;
  --color-primary: #c81d25;
  --color-accent: #d4a017;
  --color-navy: #1c2a52;
  --color-cream: #f2e6c9;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 6px;
  --radius-lg: 14px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-poster: 0 6px 0 var(--color-navy), 0 10px 18px rgba(28,19,10,0.35);
  --shadow-poster-sm: 0 3px 0 var(--color-navy), 0 4px 10px rgba(28,19,10,0.3);
  /* font */
  --font-sans: 'Josefin Sans', 'Oswald', system-ui, sans-serif;
  --font-display: 'Bebas Neue', 'Oswald', 'Arial Narrow', sans-serif;
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
  /* extra (signature gradients, composite borders, filters) */
  --stripe-pattern: repeating-linear-gradient(135deg, var(--color-primary) 0 22px, var(--color-cream) 22px 44px);
  --starburst-gradient: radial-gradient(circle at 50% 0%, rgba(212,160,23,0.35), transparent 55%);
  --scroll-border: 3px double var(--color-navy);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Circus / Carnival Poster — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2e6c9",
        "surface": "#fdf8ec",
        "surface-2": "#e8d6a8",
        "text": "#241812",
        "text-muted": "#5c4429",
        "primary": "#c81d25",
        "accent": "#d4a017",
        "navy": "#1c2a52",
        "cream": "#f2e6c9",
      },
      borderRadius: {
        "sm": "2px",
        "md": "6px",
        "lg": "14px",
        "pill": "999px",
      },
      boxShadow: {
        "poster": "0 6px 0 #1c2a52, 0 10px 18px rgba(28,19,10,0.35)",
        "poster-sm": "0 3px 0 #1c2a52, 0 4px 10px rgba(28,19,10,0.3)",
      },
      fontFamily: {
        "sans": ["'Josefin Sans'", "'Oswald'", "system-ui", "sans-serif"],
        "display": ["'Bebas Neue'", "'Oswald'", "'Arial Narrow'", "sans-serif"],
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
//   --stripe-pattern: repeating-linear-gradient(135deg, #c81d25 0 22px, #f2e6c9 22px 44px);
//   --starburst-gradient: radial-gradient(circle at 50% 0%, rgba(212,160,23,0.35), transparent 55%);
//   --scroll-border: 3px double #1c2a52;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Cream fill with a navy keyline and a stepped "letterpress" shadow (`--shadow-poster-sm`) that lifts on hover. |
| **Input** | Cream field with a thick navy border, echoing a ticket-stub cutout. |
| **Card** | Cream surface washed with `--starburst-gradient`, boxed by the double-line `--scroll-border`. |
| **Nav** | Cream bar under a heavy double-line border, red wordmark set in the display face. |
| **Modal** | Panel drops in with a small overshoot bounce (the showman "ta-da"), framed by the scroll border. |
| **Table** | Alternating cream/surface-2 rows striped faintly, header row set in display type with letter-spacing. |
| **Tooltip** | Small cream bubble, navy keyline, pointed like a banner-ribbon tail. |
| **Badge** | Pill filled with the `--stripe-pattern` barber stripe, cream display-type label. |
| **Toggle** | Track styled as a mini scrolled banner; knob is a gold coin that slides with the bounce ease. |
| **Loading** | A spinning starburst rays motif, or a bouncing ball across three rings (juggling reference). |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#241812) on `--color-bg` (#f2e6c9) is near-black on cream — comfortably exceeds AA (~14:1); verify with `contrast_check.py`.
- `--color-text-muted` (#5c4429) on `--color-bg` measures ≈7.3:1 — passes AA for body text; re-check if you darken the cream background.
- Cream text on the primary red button (`--color-primary` #c81d25) measures close to the AA floor (~4.8:1) — keep that pairing for bold, large button labels only, and never drop to a lighter red.
- The barber-stripe pattern and starburst wash are decorative; never place body text directly over the raw stripe — keep text on a flat cream card/surface layer.
- Bounce/overshoot easing on hover and modal entrance must respect `prefers-reduced-motion` — fall back to a simple fade.
- Keep focus rings a solid navy outline with real offset; ornate borders are not a substitute for a visible focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep the ground cream/gold and reserve red for stripes, borders, and primary actions.
- ✅ Set headlines in the tall condensed display face with generous letter-spacing — that's the showman voice.
- ✅ Frame key surfaces (cards, nav, modals) with the double-line scroll border to keep the "printed bill" feel consistent.

## Don't

- ❌ Use thin, quiet sans-serif type for headlines — circus lettering is loud, condensed, and tall.
- ❌ Let the stripe or starburst pattern sit directly under body text — legibility collapses.
- ❌ Reach for airbrushed gradients or soft glass blur — this is flat letterpress/lithograph color, not a modern soft-UI texture.

## Don't confuse this with…

*Commonly confused neighbors:* wpa-poster, americana-diner, victorian.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
