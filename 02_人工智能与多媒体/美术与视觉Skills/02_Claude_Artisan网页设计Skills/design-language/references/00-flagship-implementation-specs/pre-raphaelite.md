# Pre-Raphaelite — Implementation Spec

*Aliases:* Pre-Raphaelite Brotherhood style, PRB aesthetic  
*Slug:* `pre-raphaelite` · *Category:* historical · *Era:* 1848–1880s

**Origin.** England, the Pre-Raphaelite Brotherhood (Dante Gabriel Rossetti, John Everett Millais, William Holman Hunt, later Edward Burne-Jones) — a rejection of academic painting in favor of jewel-toned color, medieval-romantic subject matter, and minute botanical detail painted directly from nature.

**Reference example.** Rossetti's *Proserpine* and *Beata Beatrix*; Millais's *Ophelia*; Burne-Jones's *The Golden Stairs*.

## Signature move(s)

Deep saturated jewel tones (emerald, crimson, gold) built up like glazed oil paint, with a dense tangle of botanical motifs (ivy, roses, lilies) painted along edges and framing figures rather than repeating as flat pattern — the flowers are *specific and observed*, not stylized ornament. Flowing, wavy hair-like linework connects and softens hard edges, and a warm gold glaze sits over everything like varnish, giving surfaces a lit-from-within richness.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Deep saturated jewel-tone palette: emerald, crimson, gold, painted rather than flat
- Dense, specific botanical motifs framing content, not repeating as flat pattern
- Flowing organic linework (hair, vines, drapery) softening hard edges
- Medieval-romantic, painterly and figurative mood — never geometric or graphic

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/pre-raphaelite.css`.)

```css
/* Pre-Raphaelite — design tokens (generated from style_catalog.json) */
/* 1848–1880s | Jewel-toned, painterly, botanical, medieval-romantic. */
:root {
  /* color */
  --color-bg: #1a0f14;
  --color-surface: #2a151c;
  --color-surface-2: #3d1f28;
  --color-text: #f3e6d8;
  --color-text-muted: #cbb8a8;
  --color-primary: #8c1f3f;
  --color-accent: #1f6b4a;
  --color-gold: #c9a227;
  --color-ivory: #fff6e8;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 8px;
  --radius-lg: 20px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-glaze: 0 1px 0 rgba(255,246,232,0.08) inset, 0 14px 34px rgba(0,0,0,0.5);
  --shadow-gilt: 0 0 0 1px var(--color-gold), 0 10px 26px rgba(140,31,63,0.3);
  /* blur */
  --blur-soft: 4px;
  /* font */
  --font-sans: 'EB Garamond', 'Cormorant Garamond', serif;
  --font-display: 'Cormorant Garamond', 'EB Garamond', serif;
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
  --ease-standard: cubic-bezier(0.3, 0.6, 0.3, 1);
  /* extra (botanical frame, gold glaze, flowing vine border) */
  --gold-glaze: radial-gradient(circle at 30% 0%, rgba(201,162,39,0.16), transparent 55%);
  --vine-border: linear-gradient(180deg, var(--color-accent) 0 8%, transparent 8% 92%, var(--color-accent) 92% 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Pre-Raphaelite — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1a0f14",
        "surface": "#2a151c",
        "surface-2": "#3d1f28",
        "text": "#f3e6d8",
        "text-muted": "#cbb8a8",
        "primary": "#8c1f3f",
        "accent": "#1f6b4a",
        "gold": "#c9a227",
        "ivory": "#fff6e8",
      },
      borderRadius: {
        "sm": "2px",
        "md": "8px",
        "lg": "20px",
        "pill": "999px",
      },
      boxShadow: {
        "glaze": "0 1px 0 rgba(255,246,232,0.08) inset, 0 14px 34px rgba(0,0,0,0.5)",
        "gilt": "0 0 0 1px #c9a227, 0 10px 26px rgba(140,31,63,0.3)",
      },
      fontFamily: {
        "sans": ["'EB Garamond'", "'Cormorant Garamond'", "serif"],
        "display": ["'Cormorant Garamond'", "'EB Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.3, 0.6, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --gold-glaze: radial-gradient(circle at 30% 0%, rgba(201,162,39,0.16), transparent 55%);
//   --vine-border: linear-gradient(180deg, #1f6b4a 0 8%, transparent 8% 92%, #1f6b4a 92% 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Crimson fill with a thin gold gilt border (`--shadow-gilt`); ivory serif label, `--gold-glaze` warming the top edge. |
| **Input** | Deep surface well with a single emerald vine-border accent (`--vine-border`) along one side rather than a full box outline. |
| **Card** | Surface panel with `--gold-glaze` washed across the top and a botanical corner flourish (illustrated ivy/rose motif) framing one edge — never repeating as flat pattern. |
| **Nav** | Deep wine bar with a thin gold rule and a single small botanical mark beside the wordmark. |
| **Modal** | Panel bordered in gold gilt, `--gold-glaze` behind the header, content framed rather than boxed. |
| **Table** | Header row in emerald with ivory serif labels; row dividers as thin gold hairlines, not heavy gridlines. |
| **Tooltip** | Small crimson chip with a gold hairline border, ivory serif text, soft `--blur-soft` shadow. |
| **Badge** | Emerald pill with a thin gold border, serif caps label — reads like an illuminated manuscript initial. |
| **Toggle** | Track is a vine-bordered groove; knob is a small gold disc, glazed. |
| **Loading** | A gold vine tendril drawing/curling itself in a loop, evoking hand-painted botanical linework in motion. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `--color-text` (#f3e6d8) on `--color-bg` (#1a0f14): approximate contrast is roughly 13.5:1 — passes WCAG AA and AAA comfortably.
- Gold `--color-gold` (#c9a227) as small text on the dark background clears only ~6.3:1 against `--color-bg` but drops closer to AA-minimum on `--color-surface-2` (#3d1f28, ~4.9:1) — reserve gold text for headings/labels ≥18px or verify per surface with the contrast script.
- Botanical corner flourishes and vine borders are decorative illustration; never let them overlap body text — keep a clear text-safe zone.
- Keep focus rings a solid, saturated emerald or ivory at 2px+ with offset; the gold glaze wash is too soft/low-contrast to double as a focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Treat botanical motifs as specific illustrated elements (a particular ivy leaf, a particular rose), framing content at the edges — not a repeating wallpaper pattern.
- ✅ Build color up like glazed paint — layer a soft `--gold-glaze` over flat jewel tones rather than using flat fills alone.
- ✅ Let linework flow — curved, organic dividers and borders over straight geometric rules wherever the layout allows it.

## Don't

- ❌ Turn the botanical motifs into a repeating tiled pattern — that's arts-and-crafts's (Morris-pattern) territory, not this style's.
- ❌ Use art-nouveau's continuous whiplash structural curves as the organizing grid — Pre-Raphaelite is painterly/figurative, curves are incidental (hair, vines), not the layout's backbone.
- ❌ Flatten the palette into poster-flat color blocks — the jewel tones need to read as painted/glazed, with visible depth.

## Don't confuse this with…

*Commonly confused neighbors:* art-nouveau, arts-and-crafts, victorian.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
