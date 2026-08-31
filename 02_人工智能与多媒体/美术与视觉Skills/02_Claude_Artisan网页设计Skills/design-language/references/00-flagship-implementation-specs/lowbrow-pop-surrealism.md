# Lowbrow / Pop Surrealism — Implementation Spec

*Aliases:* pop surrealism, lowbrow art, kustom-kulture illustration, cartoon surrealism
*Slug:* `lowbrow-pop-surrealism` · *Category:* niche · *Era:* Late 20th century–present

**Origin.** Late-20th-century Southern California gallery art movement (the Robert Williams / Mark Ryden circle) fusing hot-rod kustom-kulture linework, underground comix, and cartoon-surrealist illustration into fine-art gallery painting.

**Reference example.** Robert Williams' *Juxtapoz*-era hot-rod paintings; Mark Ryden's candy-bright porcelain-doll surrealism.

## Signature move(s)

A hyper-detailed cartoon subject rendered with glossy airbrushed sheen, wrapped in a thick black kustom-kulture keyline, sitting in candy-bright colors that pop hard against a dark or muted ground — the juxtaposition of "cute" rendering technique against a subtly unsettling subject is the whole point.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Hyper-detailed cartoon-surrealist illustration with glossy airbrushed rendering
- Playful-but-unsettling juxtapositions (cute rendering, uncanny subject)
- Candy-bright palette against a dark or muted ground
- Kustom-kulture/hot-rod-adjacent thick black linework (keyline)

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/lowbrow-pop-surrealism.css`.)

```css
/* Lowbrow / Pop Surrealism — design tokens (generated from style_catalog.json) */
/* Late 20th century–present | Cartoon-surrealist gallery movement (Robert Williams / Mark Ryden circle). */
:root {
  /* color */
  --color-bg: #17151f;
  --color-surface: #201c2c;
  --color-surface-2: #2c2740;
  --color-text: #f4eefc;
  --color-text-muted: #b8aed0;
  --color-primary: #ff5fa2;
  --color-accent: #4fd8e0;
  --color-gold: #ffcc33;
  --color-lineweight: #0e0c14;
  /* radius */
  --radius-sm: 6px;
  --radius-md: 16px;
  --radius-lg: 32px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-glossy: 0 10px 30px rgba(255,95,162,0.25), 0 2px 0 var(--color-lineweight);
  --shadow-glossy-sm: 0 4px 14px rgba(79,216,224,0.25), 0 1px 0 var(--color-lineweight);
  /* font */
  --font-sans: 'Baloo 2', 'Nunito', system-ui, sans-serif;
  --font-display: 'Bungee', 'Baloo 2', 'Arial Rounded MT Bold', sans-serif;
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
  --ease-standard: cubic-bezier(0.34, 1.4, 0.3, 1);
  /* extra (signature gradients, composite borders, filters) */
  --candy-sheen: radial-gradient(60% 45% at 30% 20%, rgba(255,255,255,0.35), transparent 60%);
  --keyline-outline: 0 0 0 3px var(--color-lineweight);
  --bg-image: radial-gradient(120% 90% at 80% -10%, #2c2740 0%, #17151f 55%, #0e0c14 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Lowbrow / Pop Surrealism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#17151f",
        "surface": "#201c2c",
        "surface-2": "#2c2740",
        "text": "#f4eefc",
        "text-muted": "#b8aed0",
        "primary": "#ff5fa2",
        "accent": "#4fd8e0",
        "gold": "#ffcc33",
        "lineweight": "#0e0c14",
      },
      borderRadius: {
        "sm": "6px",
        "md": "16px",
        "lg": "32px",
        "pill": "999px",
      },
      boxShadow: {
        "glossy": "0 10px 30px rgba(255,95,162,0.25), 0 2px 0 #0e0c14",
        "glossy-sm": "0 4px 14px rgba(79,216,224,0.25), 0 1px 0 #0e0c14",
      },
      fontFamily: {
        "sans": ["'Baloo 2'", "'Nunito'", "system-ui", "sans-serif"],
        "display": ["'Bungee'", "'Baloo 2'", "'Arial Rounded MT Bold'", "sans-serif"],
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
        "standard": "cubic-bezier(0.34, 1.4, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --candy-sheen: radial-gradient(60% 45% at 30% 20%, rgba(255,255,255,0.35), transparent 60%);
//   --keyline-outline: 0 0 0 3px #0e0c14;
//   --bg-image: radial-gradient(120% 90% at 80% -10%, #2c2740 0%, #17151f 55%, #0e0c14 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Pill shape wrapped in the thick black `--keyline-outline`, dark surface fill, glossy sheen only on the primary variant. |
| **Input** | Rounded field with the keyline outline instead of a border-color change; sheen omitted so it stays legible. |
| **Card** | Large rounded surface washed with `--candy-sheen`, always framed by the keyline. |
| **Nav** | Dark bar with a thick keyline bottom border, gold wordmark set in the bubbly display face. |
| **Modal** | Pops in with a slight overshoot scale (like a cartoon "boing"), keyline-framed panel. |
| **Table** | Rounded-corner row groups with keyline dividers instead of hairlines, alternating dark surfaces. |
| **Tooltip** | Small accent-cyan bubble with candy sheen and a full keyline outline, cartoon speech-bubble tail. |
| **Badge** | Pill with candy sheen and keyline, dark ink label text for contrast against the bright fill. |
| **Toggle** | Track as a keyline-outlined capsule; knob is a glossy sheened dot that overshoots slightly when it lands. |
| **Loading** | A grinning cartoon-eye blink loop, or a bouncing glossy dot with keyline, never a plain bare spinner. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#f4eefc) on `--color-bg` (#17151f) is near-white on deep plum-black — passes AA with a wide margin; verify with `contrast_check.py`.
- `--color-text-muted` (#b8aed0) stays readable against both `--color-surface` and `--color-surface-2` — re-check if either surface tone is lightened.
- Dark-ink (`--color-lineweight`) labels on the bright primary/accent/gold fills are intentional and pass AA; never swap in light text on those same bright fills.
- The `--candy-sheen` highlight is decorative gloss only — keep it confined to the upper-left of a shape and never let it wash over body text.
- Overshoot "boing" animations on hover/modal-entrance must respect `prefers-reduced-motion` — fall back to a plain fade/scale without the bounce.
- Keep focus rings a solid gold outline with real offset; the keyline outline is structural, not a focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Wrap every raised surface in the thick black keyline — it's what makes flat candy color read as "painted," not flat-design.
- ✅ Keep the ground dark or muted so candy-bright fills pop; never put lowbrow color on a bright white ground.
- ✅ Let one detail per composition feel slightly uncanny — cute rendering, unsettling content is the joke.

## Don't

- ❌ Drop the keyline outline — without it this collapses into generic flat illustration or corporate-memphis blobbing.
- ❌ Play it entirely cute with no unsettling edge — that's just kawaii, not lowbrow/pop-surrealism.
- ❌ Use trippy warped 3D chrome type — that's acid-graphics' rave-flyer language, not this gallery-painting one.

## Don't confuse this with…

*Commonly confused neighbors:* pop-art, psychedelic, dreamcore.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
