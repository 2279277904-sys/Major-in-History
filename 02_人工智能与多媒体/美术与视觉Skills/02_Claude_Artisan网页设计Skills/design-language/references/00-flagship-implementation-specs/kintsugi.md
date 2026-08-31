# Kintsugi — Implementation Spec

*Aliases:* golden joinery, kintsukuroi  
*Slug:* `kintsugi` · *Category:* historical · *Era:* 15th century–present

**Origin.** Japanese art of repairing broken ceramics with gold-dusted lacquer (urushi), rooted in wabi-sabi philosophy — the break and its repair become part of the object's history, visible and celebrated rather than concealed.

**Reference example.** Muromachi-period repaired tea bowls (chawan) in the Freer Gallery and Tokyo National Museum collections; contemporary kintsugi restoration photography.

## Signature move(s)

Dark, matte ceramic-like surfaces (charcoal, near-black glaze tones) crossed by luminous gold "seams" — every place two components join, meet, or divide gets a visible gold line instead of a hidden gap or plain rule, as if the interface itself were a repaired vessel. The seam is never perfectly straight; it wanders slightly, like a real fracture line, and glows faintly warmer than a flat gold fill.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Dark matte ceramic/glaze surfaces (charcoal, near-black) as the base material
- Luminous gold seam lines marking every join, division, or repair — imperfection as a visible feature
- Warm charcoal-and-gold palette only, no cool colors
- Slightly irregular, hand-drawn seam paths rather than perfectly straight rules

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/kintsugi.css`.)

```css
/* Kintsugi — design tokens (generated from style_catalog.json) */
/* 15th century–present | Dark ceramic surfaces joined by luminous gold seams. */
:root {
  /* color */
  --color-bg: #1c1a18;
  --color-surface: #262320;
  --color-surface-2: #322d28;
  --color-text: #f0e6d2;
  --color-text-muted: #b8ab94;
  --color-primary: #d4a53d;
  --color-accent: #8a6a3a;
  --color-seam: #f0c04d;
  --color-lacquer: #100e0c;
  /* radius */
  --radius-sm: 3px;
  --radius-md: 10px;
  --radius-lg: 18px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-seam-glow: 0 0 10px rgba(240,192,77,0.45);
  --shadow-vessel: 0 10px 26px rgba(0,0,0,0.5);
  /* blur */
  --blur-soft: 6px;
  /* font */
  --font-sans: 'Noto Serif JP', 'Shippori Mincho', 'Georgia', serif;
  --font-display: 'Shippori Mincho', 'Noto Serif JP', serif;
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
  /* extra (gold seam path, crackle texture, glaze sheen) */
  --seam-gradient: linear-gradient(90deg, transparent, var(--color-seam) 15%, var(--color-primary) 50%, var(--color-seam) 85%, transparent);
  --glaze-sheen: radial-gradient(circle at 25% 0%, rgba(240,230,210,0.06), transparent 55%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Kintsugi — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1c1a18",
        "surface": "#262320",
        "surface-2": "#322d28",
        "text": "#f0e6d2",
        "text-muted": "#b8ab94",
        "primary": "#d4a53d",
        "accent": "#8a6a3a",
        "seam": "#f0c04d",
        "lacquer": "#100e0c",
      },
      borderRadius: {
        "sm": "3px",
        "md": "10px",
        "lg": "18px",
        "pill": "999px",
      },
      boxShadow: {
        "seam-glow": "0 0 10px rgba(240,192,77,0.45)",
        "vessel": "0 10px 26px rgba(0,0,0,0.5)",
      },
      fontFamily: {
        "sans": ["'Noto Serif JP'", "'Shippori Mincho'", "'Georgia'", "serif"],
        "display": ["'Shippori Mincho'", "'Noto Serif JP'", "serif"],
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
//   --seam-gradient: linear-gradient(90deg, transparent, #f0c04d 15%, #d4a53d 50%, #f0c04d 85%, transparent);
//   --glaze-sheen: radial-gradient(circle at 25% 0%, rgba(240,230,210,0.06), transparent 55%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Charcoal ceramic fill with a gold seam traced along one edge (`--seam-gradient`), glowing on hover. |
| **Input** | Dark well; the bottom border is a gold seam line that thickens and glows when focused. |
| **Card** | Charcoal panel visually "repaired" by a diagonal gold seam crossing one corner, `--glaze-sheen` washed over the surface. |
| **Nav** | Dark bar with a single gold seam running its full width at the base, standing in for a border. |
| **Modal** | Panel edges traced in gold seam instead of a flat stroke; the seam is where the modal "was broken open" from the page. |
| **Table** | Row dividers rendered as thin gold seams rather than plain grey rules. |
| **Tooltip** | Small dark chip outlined by a single gold seam, no drop shadow beyond `--shadow-seam-glow`. |
| **Badge** | Pill with a gold seam outline and no fill — the seam itself is the badge. |
| **Toggle** | Track is a dark ceramic groove; the "on" state fills the groove with a glowing gold seam. |
| **Loading** | A gold seam line drawing itself across a dark disc in a loop, like a crack being repaired live. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `--color-text` (#f0e6d2) on `--color-bg` (#1c1a18): approximate contrast is roughly 14:1 — passes WCAG AA and AAA comfortably.
- Gold seam lines are decorative wayfinding, not text — never rely on a seam alone to convey state (e.g. "error"); pair it with a text label or icon.
- `--color-primary` gold (#d4a53d) as text on `--color-bg` clears ~7.8:1, safe for body text; but gold text on `--color-surface-2` (#322d28) drops to ~6.9:1 — still AA-safe, verify with the contrast script per real usage.
- Keep focus rings a solid, opaque gold (`--color-seam`) at 2px+ with offset — the glow shadow alone is too soft to serve as the focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Let seams wander slightly off perfectly straight — a hand-drawn crack, not a ruler line.
- ✅ Treat every structural join (card edge, divider, focus state) as an opportunity for a seam, not just decoration.
- ✅ Keep the base surfaces genuinely dark and matte — the gold only reads as luminous against real darkness.

## Don't

- ❌ Add cool colors (blue, teal, violet) anywhere — kintsugi's palette is warm charcoal and gold only.
- ❌ Make every edge a seam — reserve gold for meaningful joins/dividers, or the metaphor collapses into generic gold trim.
- ❌ Round every corner into a soft pill — ceramic vessels have some hard edges; keep `--radius-sm` sharp where two flat planes meet.

## Don't confuse this with…

*Commonly confused neighbors:* zen-wabisabi, ukiyo-e, dark-academia.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
