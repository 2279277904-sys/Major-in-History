# Teslapunk — Implementation Spec

*Aliases:* electropunk, wireless-age retrofuturism, arc-light futurism
*Slug:* `teslapunk` · *Category:* retrofuturism · *Era:* 1890s–1920s (imagined future, revival ongoing)

**Origin.** Retrofuturist genre built around Nikola Tesla-era electrical imagining — the turn-of-the-century dream of a "wireless electrical future" powered by high-voltage coils, arc lightning, and wireless power transmission (Wardenclyffe Tower, the Tesla coil).

**Reference example.** Tesla's Colorado Springs and Wardenclyffe experiments; period illustrations of induction coils and arc-lightning demonstrations.

## Signature move(s)

A crackling blue-white arc-lightning glow — feathered, electric, alive — radiating from polished copper and brass coil forms against a deep midnight-blue ground, lit by warm glowing filament/vacuum-tube lamps: turn-of-the-century optimism about a wireless electrical future, not a dieselpunk engine or a clockpunk gear.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Crackling blue-white arc-lightning motifs
- Polished copper and brass coil detailing
- Deep midnight-blue backgrounds
- Glowing filament/vacuum-tube light sources; wireless-electrical-future optimism

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/teslapunk.css`.)

```css
/* Teslapunk — design tokens (generated from style_catalog.json) */
/* 1890s–1920s (imagined future, revival ongoing) | Retrofuturism built on Nikola Tesla-era wireless electricity. */
:root {
  /* color */
  --color-bg: #060b1a;
  --color-surface: #0d1830;
  --color-surface-2: #142544;
  --color-text: #eaf4ff;
  --color-text-muted: #9fb8d9;
  --color-primary: #4fd8ff;
  --color-accent: #d98a3d;
  --color-brass: #c9a24b;
  --color-copper: #a8622f;
  /* radius */
  --radius-sm: 3px;
  --radius-md: 10px;
  --radius-lg: 22px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-arc: 0 0 22px rgba(79,216,255,0.45), 0 8px 22px rgba(0,0,0,0.5);
  --shadow-brass: 0 4px 12px rgba(201,162,75,0.25), inset 0 1px 0 rgba(255,255,255,0.15);
  /* blur */
  --blur-arc: 12px;
  /* font */
  --font-sans: 'Cormorant', 'EB Garamond', system-ui, serif;
  --font-display: 'Cinzel', 'Cormorant', serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
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
  --ease-standard: cubic-bezier(0.2, 0.8, 0.3, 1);
  /* extra (signature gradients, composite borders, filters) */
  --arc-gradient: radial-gradient(circle at 50% 0%, rgba(79,216,255,0.35), transparent 55%);
  --brass-trim: linear-gradient(180deg, #e7c47a 0%, #c9a24b 45%, #8a6a2c 100%);
  --bg-image: radial-gradient(140% 100% at 50% -10%, #142544 0%, #060b1a 60%, #030612 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Teslapunk — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#060b1a",
        "surface": "#0d1830",
        "surface-2": "#142544",
        "text": "#eaf4ff",
        "text-muted": "#9fb8d9",
        "primary": "#4fd8ff",
        "accent": "#d98a3d",
        "brass": "#c9a24b",
        "copper": "#a8622f",
      },
      borderRadius: {
        "sm": "3px",
        "md": "10px",
        "lg": "22px",
        "pill": "999px",
      },
      boxShadow: {
        "arc": "0 0 22px rgba(79,216,255,0.45), 0 8px 22px rgba(0,0,0,0.5)",
        "brass": "0 4px 12px rgba(201,162,75,0.25), inset 0 1px 0 rgba(255,255,255,0.15)",
      },
      fontFamily: {
        "sans": ["'Cormorant'", "'EB Garamond'", "system-ui", "serif"],
        "display": ["'Cinzel'", "'Cormorant'", "serif"],
        "mono": ["'JetBrains Mono'", "ui-monospace", "monospace"],
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
        "standard": "cubic-bezier(0.2, 0.8, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --arc-gradient: radial-gradient(circle at 50% 0%, rgba(79,216,255,0.35), transparent 55%);
//   --brass-trim: linear-gradient(180deg, #e7c47a 0%, #c9a24b 45%, #8a6a2c 100%);
//   --bg-image: radial-gradient(140% 100% at 50% -10%, #142544 0%, #060b1a 60%, #030612 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Dark surface fill with a brass keyline; hovering triggers the arc-lightning glow shadow (`--shadow-arc`). |
| **Input** | Deep surface well with a copper border that arcs blue-white on focus. |
| **Card** | Midnight surface washed with `--arc-gradient`, topped by a `--brass-trim` gradient border like a coil rim. |
| **Nav** | Slim dark bar under a solid brass rule, a faint arc-blue glow along the bottom edge. |
| **Modal** | Panel fades in through the arc-gradient wash with a soft blur, like a coil discharging. |
| **Table** | Flat dark rows; header and hovered rows pick up a faint arc-blue glow, brass rule under the header. |
| **Tooltip** | Small brass-outlined bubble with a soft arc-blue inner glow, no hard edge. |
| **Badge** | Pill with a thin brass border and a faint inner glow, no solid fill — like an engraved plate. |
| **Toggle** | Track styled as a coil form; the knob arcs blue-white when on, sits dim brass when off. |
| **Loading** | A pulsing arc-lightning spark jumping between two points, or a spinning coil glow ring. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#eaf4ff) on `--color-bg` (#060b1a) is pale blue-white on near-black midnight blue — passes AA with a very wide margin; verify with `contrast_check.py`.
- `--color-text-muted` (#9fb8d9) stays readable against `--color-surface`/`--color-surface-2` — re-check if either surface tone is lightened.
- Arc-glow shadows must never substitute for text contrast — keep body text on the flat `--color-text` value and reserve the glow for decoration around shapes, not behind text.
- The brass/copper accents are for trim and borders, not body text — dark brass on midnight blue fails AA for small text, so reserve brass tones for headings, borders, and large display type only.
- Pulsing/crackling arc animations must respect `prefers-reduced-motion` — fall back to a static glow.
- Keep focus rings a solid arc-blue outline with real offset; the ambient glow is not a substitute for a visible focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep the ground deep midnight blue-black — never atompunk's clean optimistic pastel, never dieselpunk's grimy brown.
- ✅ Feather every arc-lightning glow (blur, radial gradient) — it should crackle, not sit as a hard neon line.
- ✅ Trim structural edges (card tops, coil-like toggles) in the brass/copper gradient — that's the "polished apparatus" signature.

## Don't

- ❌ Reach for nuclear/atomic iconography (atom diagrams, radiation trefoils) — that's atompunk's 1950s language, not Tesla-era electricity.
- ❌ Add exposed gears, cogs, or clockwork trim — that's clockpunk's mechanism, not this one's induction coils and arcs.
- ❌ Use grimy brown/rust industrial texture or riveted iron plating — that's dieselpunk's engine-driven aesthetic, not wireless electricity's cleaner arc-light glow.

## Don't confuse this with…

*Commonly confused neighbors:* atompunk, dieselpunk, clockpunk.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
