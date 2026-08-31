# Android Holo — Implementation Spec

*Aliases:* Holo, Honeycomb UI, Ice Cream Sandwich UI  
*Slug:* `android-holo` · *Category:* flat-platform · *Era:* 2011–2014

**Origin.** Google's Android 3.0 Honeycomb (2011) introduced the "Holo" design language for tablets; it carried through Ice Cream Sandwich and Jelly Bean (Android 4.x) until Material Design replaced it in 2014.

**Reference example.** Android 3.0–4.4 stock UI (Honeycomb, Ice Cream Sandwich, Jelly Bean, KitKat); Google Now on Jelly Bean; the original Holo Light/Dark system themes.

## Signature move(s)

A near-black canvas with almost no chrome, lit by exactly one accent: the glowing cyan-blue "holo" highlight (`#33b5e5` family). Every interactive state — focus, selection, active tab, checked toggle, pressed button — expresses itself as that single glow, never as a tonal fill or a drop shadow. Elevation doesn't exist as a concept; hierarchy comes from thin dividers, uppercase micro-labels, and generous negative space.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Near-black backgrounds (`#000`–`#0c0f10`), almost no surface elevation
- A single glowing cyan/holo-blue accent for all interactive highlights
- Thin geometric condensed sans type (Roboto Condensed), often uppercase for labels
- Flat chrome: 1–2px hairline dividers instead of cards or shadows
- Glow (`box-shadow` with blur, zero spread darkness) substitutes for elevation

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/android-holo.css`.)

```css
/* Android Holo — design tokens (generated from style_catalog.json) */
/* 2011–2014 | Pre-Material Android: near-black chrome, single glowing cyan accent. */
:root {
  /* color */
  --color-bg: #000000;
  --color-surface: #0c0f10;
  --color-surface-2: #171b1c;
  --color-text: #e8f7fa;
  --color-text-muted: #8a9a9d;
  --color-primary: #33b5e5;
  --color-primary-bright: #8fdce8;
  --color-divider: #2a2f30;
  --color-danger: #ff4444;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 2px;
  --radius-lg: 2px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-glow: 0 0 8px rgba(51,181,229,0.55), 0 0 1px rgba(51,181,229,0.9);
  --shadow-glow-strong: 0 0 16px rgba(51,181,229,0.75), 0 0 2px rgba(143,220,232,0.9);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Roboto Condensed', 'Droid Sans', 'Helvetica Neue', Arial, sans-serif;
  --font-display: 'Roboto Condensed', 'Droid Sans', sans-serif;
  --font-mono: 'Droid Sans Mono', ui-monospace, monospace;
  /* text */
  --text-xs: 0.6875rem;
  --text-sm: 0.8125rem;
  --text-base: 0.9375rem;
  --text-lg: 1.0625rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;
  --text-4xl: 2.75rem;
  --text-5xl: 3.5rem;
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
  --ease-standard: linear;
  /* extra (signature gradients, composite borders, filters) */
  --holo-underline: linear-gradient(90deg, transparent, #33b5e5, transparent);
  --bg-image: none;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Android Holo — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#000000",
        "surface": "#0c0f10",
        "surface-2": "#171b1c",
        "text": "#e8f7fa",
        "text-muted": "#8a9a9d",
        "primary": "#33b5e5",
        "primary-bright": "#8fdce8",
        "divider": "#2a2f30",
        "danger": "#ff4444",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "2px",
        "pill": "999px",
      },
      boxShadow: {
        "glow": "0 0 8px rgba(51,181,229,0.55), 0 0 1px rgba(51,181,229,0.9)",
        "glow-strong": "0 0 16px rgba(51,181,229,0.75), 0 0 2px rgba(143,220,232,0.9)",
      },
      fontFamily: {
        "sans": ["'Roboto Condensed'", "'Droid Sans'", "'Helvetica Neue'", "Arial", "sans-serif"],
        "display": ["'Roboto Condensed'", "'Droid Sans'", "sans-serif"],
        "mono": ["'Droid Sans Mono'", "ui-monospace", "monospace"],
      },
      fontSize: {
        "xs": "0.6875rem",
        "sm": "0.8125rem",
        "base": "0.9375rem",
        "lg": "1.0625rem",
        "xl": "1.25rem",
        "2xl": "1.5rem",
        "3xl": "2rem",
        "4xl": "2.75rem",
        "5xl": "3.5rem",
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
        "standard": "linear",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --holo-underline: linear-gradient(90deg, transparent, #33b5e5, transparent);
//   --bg-image: none;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Transparent fill, thin divider border; on hover/focus the border turns holo-cyan and the whole control gains the glow shadow — never a filled background. |
| **Input** | Underline-only field (no box); bottom border blooms cyan and glows on focus, matching Honeycomb's text field behavior. |
| **Card** | Flat surface panel with a single hairline divider border, zero shadow, zero radius beyond 2px. |
| **Nav** | Slim black action bar; the active tab gets a bottom cyan underline glow instead of a filled pill. |
| **Modal** | Near-black panel, hairline border, appears instantly (no blur/scale spring — Holo motion is linear and abrupt). |
| **Table** | Flat rows separated only by hairline dividers; the selected row's left edge glows cyan. |
| **Tooltip** | Small black bubble, 1px cyan border, no blur, no drop shadow — glow only. |
| **Badge** | Pill outline in cyan on transparent fill; text in the bright cyan variant, never a solid fill badge. |
| **Toggle** | Flat black track; the thumb and track edge glow cyan when on, dim grey divider color when off. |
| **Loading** | A thin circular cyan arc (indeterminate spinner) with a glow trail — Honeycomb's signature circular progress. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `#e8f7fa` on background `#000000` measures 19.12:1 — comfortably AA/AAA; verify with `contrast_check.py` before shipping any lighter substitution.
- The single accent color (`#33b5e5`) is relied on for every interactive state — never use color alone to convey it; pair the cyan glow with a border, underline, or icon change so colorblind users aren't dependent on hue.
- Glow shadows must not be the only focus indicator on non-text controls; keep a visible border/underline change alongside the glow so the state survives at low blur-rendering fidelity (some browsers/printers flatten box-shadow blur).
- Uppercase micro-labels reduce legibility for longer strings — keep uppercase to short single words/labels, never full sentences.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep the palette to near-black + one cyan accent — resist adding a second "accent" color.
- ✅ Use hairline dividers and glow, never card shadows or filled tonal surfaces, to express structure.
- ✅ Keep type condensed, geometric, and often uppercase for labels/tabs.

## Don't

- ❌ Add tonal surface containers or elevation shadows — that's Material Design's vocabulary, not Holo's.
- ❌ Introduce a second saturated accent color — Holo is famously monochrome-plus-cyan.
- ❌ Use spring/bounce motion — Holo transitions are linear and instantaneous, not expressive easing.

## Don't confuse this with…

*Commonly confused neighbors:* material-design, material-design-3.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
