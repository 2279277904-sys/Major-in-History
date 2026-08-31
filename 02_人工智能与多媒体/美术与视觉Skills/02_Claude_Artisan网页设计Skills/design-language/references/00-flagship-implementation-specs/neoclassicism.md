# Neoclassicism — Implementation Spec

*Aliases:* neoclassical design, Greco-Roman revival  
*Slug:* `neoclassicism` · *Category:* historical · *Era:* 1760s–1830s (revival)

**Origin.** 18th-century European revival of Greco-Roman art and architecture, prompted by the excavations of Pompeii and Herculaneum — a reaction against Baroque/Rococo excess in favor of symmetry, restraint, and classical orders.

**Reference example.** The Panthéon, Paris; Jacques-Louis David's history paintings; Wedgwood's Jasperware relief medallions.

## Signature move(s)

Strict bilateral symmetry framed by pared-down architectural motifs — a pediment-shaped header cap, thin fluted-column dividers between sections — rendered in cream marble and muted gold against deep ink, with carved-inscription serif type standing in for a stone lintel. Ornament is used the way classical architecture uses it: at the frame and the base, never scattered across the field.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Strict symmetric composition, centered layouts
- Column/pediment motifs used as structural framing, not decoration
- Cream/marble-white surfaces with muted gold and deep ink accents
- Serif type evoking carved stone inscriptions; restrained ornament

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/neoclassicism.css`.)

```css
/* Neoclassicism — design tokens (generated from style_catalog.json) */
/* 1760s–1830s | Symmetric Greco-Roman revival: marble, muted gold, ink, restraint. */
:root {
  /* color */
  --color-bg: #f2ede0;
  --color-surface: #faf7ef;
  --color-surface-2: #e3dbc7;
  --color-text: #1f2733;
  --color-text-muted: #5a5850;
  --color-primary: #8a6d3b;
  --color-accent: #2f3b52;
  --color-marble-vein: #c9c0a8;
  --color-ink: #14181f;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 2px;
  --radius-lg: 4px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-plinth: 0 1px 0 #ffffff inset, 0 10px 22px rgba(31,39,51,0.14);
  --shadow-relief: 0 1px 2px rgba(31,39,51,0.22);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Trajan Pro', 'Cinzel', 'Georgia', serif;
  --font-display: 'Cinzel', 'Trajan Pro', serif;
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
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  /* extra (pediment cap, fluted-column divider, marble veining) */
  --pediment-cap: linear-gradient(180deg, var(--color-surface-2) 0 3px, transparent 3px);
  --fluted-divider: repeating-linear-gradient(90deg, var(--color-marble-vein) 0 1px, transparent 1px 10px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Neoclassicism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2ede0",
        "surface": "#faf7ef",
        "surface-2": "#e3dbc7",
        "text": "#1f2733",
        "text-muted": "#5a5850",
        "primary": "#8a6d3b",
        "accent": "#2f3b52",
        "marble-vein": "#c9c0a8",
        "ink": "#14181f",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "plinth": "0 1px 0 #ffffff inset, 0 10px 22px rgba(31,39,51,0.14)",
        "relief": "0 1px 2px rgba(31,39,51,0.22)",
      },
      fontFamily: {
        "sans": ["'Trajan Pro'", "'Cinzel'", "'Georgia'", "serif"],
        "display": ["'Cinzel'", "'Trajan Pro'", "serif"],
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
        "standard": "cubic-bezier(0.4, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --pediment-cap: linear-gradient(180deg, #e3dbc7 0 3px, transparent 3px);
//   --fluted-divider: repeating-linear-gradient(90deg, #c9c0a8 0 1px, transparent 1px 10px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Cream fill, thin ink border, centered small-caps serif label; a hairline gold rule sits just inside the border like a plinth edge. |
| **Input** | Marble-white well with a single gold underline (not a full box) — a base, not a cage. |
| **Card** | Symmetric layout, `--pediment-cap` at the top edge, `--fluted-divider` used as a vertical rule if the card splits into two columns. |
| **Nav** | Centered wordmark, symmetric left/right link groups, thin gold rule beneath acting as an entablature line. |
| **Modal** | Framed by a simple ink border with a pediment-cap header band; content centered and symmetric. |
| **Table** | Header row in ink-on-cream small caps; fluted-divider hairlines between columns instead of heavy gridlines. |
| **Tooltip** | Small cream chip, thin ink border, no rounding, no drop shadow beyond `--shadow-relief`. |
| **Badge** | Cream pill with a thin gold border and centered serif caps label. |
| **Toggle** | Track is a fluted groove; knob is a small gold disc that reads as a coin/medallion. |
| **Loading** | A gold ring "carving itself in" clockwise around a fixed ink dot, evoking a sundial. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `--color-text` (#1f2733) on `--color-bg` (#f2ede0): approximate contrast is roughly 12.5:1 — passes WCAG AA and AAA comfortably.
- Muted gold `--color-primary` (#8a6d3b) as text on cream clears ~4.7:1 — right at the AA threshold for normal text; reserve it for large/bold headings or pair with the darker `--color-accent` for small body copy to stay safely above 4.5:1.
- Hairline gold rules and fluted dividers are structural ornament, not text — never encode meaning in a rule's presence alone.
- Keep focus rings in `--color-accent` (deep ink-blue) at 2px+ with offset against the cream surfaces; gold alone is too close to the mid-tone background to be reliably visible for low-vision users.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Center compositions and mirror left/right groupings — symmetry is the organizing principle, not an occasional flourish.
- ✅ Use column/pediment motifs as structural framing (header caps, dividers), never as scattered decoration.
- ✅ Keep ornament restrained — a single hairline gold rule communicates more here than a heavy border would.

## Don't

- ❌ Pile on ornate scrollwork, gilt frames, or asymmetric flourishes — that's baroque-rococo's territory, the style neoclassicism was reacting against.
- ❌ Use gold as a small-text color without checking contrast against the specific surface behind it.
- ❌ Break symmetry casually — an off-center layout undercuts the entire signature move.

## Don't confuse this with…

*Commonly confused neighbors:* baroque-rococo, egyptian-ancient-revival, victorian.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
