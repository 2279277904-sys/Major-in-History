# Batik — Implementation Spec

*Aliases:* wax-resist dyeing, tulis, cap batik  
*Slug:* `batik` · *Category:* texture · *Era:* 6th century–present

**Origin.** Wax-resist textile dyeing practiced across Indonesia (especially Java), Malaysia, and West Africa (notably via Dutch-introduced wax-print traditions), among other regions. Molten wax is applied to cloth with a canting pen or copper stamp (cap), the cloth is dyed, and the wax is boiled away to reveal the resisted pattern — repeated across multiple dye baths for multicolor cloth.

**Reference example.** Javanese tulis (hand-drawn) batik sarongs; Yogyakarta and Solo court batik patterns; West African wax-print (Ankara/Dutch wax) cloth.

## Signature move(s)

An intricate, repeating organic pattern (florals, birds, geometric parang/kawung motifs) covers the surface edge to edge, but every filled shape carries fine, irregular crackle/veining lines — the fossilized trace of the wax coating cracking during the dye bath, letting dye seep into hairline fractures. The palette stays warm and earthy: indigo, rust, and ochre dyes layered on a natural, slightly warm cloth ground, never a bright synthetic color.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Intricate repeating organic/geometric pattern (florals, parang, kawung motifs)
- Fine crackle/veining lines from wax-resist cracking during dyeing
- Warm indigo/rust/ochre dye palette on a natural cloth ground
- Motifs applied edge-to-edge, not as an isolated decorative accent

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/batik.css`.)

```css
/* Batik — design tokens (generated from style_catalog.json) */
/* 6th century–present | Wax-resist textile dyeing across Indonesia, Malaysia, West Africa. */
:root {
  /* color */
  --color-bg: #f3e6cd;
  --color-surface: #faf1de;
  --color-surface-2: #e7d3ab;
  --color-text: #2b1c12;
  --color-text-muted: #6b5335;
  --color-primary: #2c4a6e;
  --color-accent: #b5501f;
  --color-ochre: #c68a2e;
  --color-indigo-deep: #1c3350;
  /* radius */
  --radius-sm: 6px;
  --radius-md: 14px;
  --radius-lg: 26px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-cloth: 0 10px 26px rgba(43,28,18,0.18);
  --shadow-cloth-sm: 0 4px 12px rgba(43,28,18,0.14);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Cormorant Garamond', 'Marcellus', system-ui, serif;
  --font-display: 'Marcellus', 'Cormorant Garamond', serif;
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
  --ease-standard: cubic-bezier(0.33, 0.0, 0.2, 1);
  /* extra (signature gradients, composite borders, filters) */
  --crackle-veins: repeating-conic-gradient(from 20deg at 30% 40%, rgba(43,28,18,0.05) 0deg 4deg, transparent 4deg 26deg);
  --motif-border: repeating-linear-gradient(90deg, #2c4a6e 0 6px, #c68a2e 6px 8px, transparent 8px 22px);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Batik — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f3e6cd",
        "surface": "#faf1de",
        "surface-2": "#e7d3ab",
        "text": "#2b1c12",
        "text-muted": "#6b5335",
        "primary": "#2c4a6e",
        "accent": "#b5501f",
        "ochre": "#c68a2e",
        "indigo-deep": "#1c3350",
      },
      borderRadius: {
        "sm": "6px",
        "md": "14px",
        "lg": "26px",
        "pill": "999px",
      },
      boxShadow: {
        "cloth": "0 10px 26px rgba(43,28,18,0.18)",
        "cloth-sm": "0 4px 12px rgba(43,28,18,0.14)",
      },
      fontFamily: {
        "sans": ["'Cormorant Garamond'", "'Marcellus'", "system-ui", "serif"],
        "display": ["'Marcellus'", "'Cormorant Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.33, 0.0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --crackle-veins: repeating-conic-gradient(from 20deg at 30% 40%, rgba(43,28,18,0.05) 0deg 4deg, transparent 4deg 26deg);
//   --motif-border: repeating-linear-gradient(90deg, #2c4a6e 0 6px, #c68a2e 6px 8px, transparent 8px 22px);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Cloth-toned fill with a soft crackle texture and a warm dye-shadow (`--shadow-cloth-sm`); indigo primary fill for the CTA. |
| **Input** | Cream field with a thin ochre border, no crackle inside (keeps typed text crisp). |
| **Card** | Cream surface washed in `--crackle-veins`, topped with a thick accent-color border like a cloth's woven edge. |
| **Nav** | Warm surface bar with a deep-indigo rule beneath, evoking a dyed border strip. |
| **Modal** | Panel eases in like cloth settling, soft warm shadow, crackle texture visible across the field. |
| **Table** | Header row in ochre, row dividers as thin indigo hairlines, body rows carry a faint crackle wash. |
| **Tooltip** | Small cream chip, thin ochre border, no crackle (stays legible at small size). |
| **Badge** | Ochre pill with an accent-color border, reads like a small dye-stamped label. |
| **Toggle** | Track rendered with `--motif-border` repeating pattern; knob is a solid indigo dot. |
| **Loading** | A ring built from the repeating motif border slowly rotating, like cloth turning in a dye vat. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Deep brown-black text (`--color-text: #2b1c12`) on the warm cream ground (`--color-bg: #f3e6cd`) measures roughly 13.3:1 — verify every pairing with `contrast_check.py`, and re-check `--color-text-muted` on `--color-surface-2` (~5.8:1) if either value shifts.
- Keep `--crackle-veins` and `--motif-border` restricted to decorative backgrounds/borders — never place body text directly over a busy repeating motif without a clean text layer underneath.
- The deep indigo primary (`--color-primary`) on cream passes AA for buttons/links; confirm the reverse (cream text on indigo fill) too before shipping the primary button.
- Keep focus rings solid and high-contrast (indigo) — decorative crackle texture must never substitute for a visible focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Treat batik as a specific, respected craft technique — indigo/rust/ochre on natural cloth, not a generic "ethnic pattern" filler.
- ✅ Let the crackle-vein texture repeat consistently across every filled surface.
- ✅ Keep the repeating motif dense and edge-to-edge — batik patterns rarely leave large empty fields.

## Don't

- ❌ Flatten the palette into bright, saturated synthetic colors — batik dye colors are warm, earthy, and slightly muted.
- ❌ Use the pattern as a one-off decorative sticker; it should read as continuous cloth.
- ❌ Caricature or generalize the motifs — reference real parang/kawung-style repeating patterns, not invented "tribal" clichés.

## Don't confuse this with…

*Commonly confused neighbors:* textile-knit-embroidery, terrazzo, marble.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
