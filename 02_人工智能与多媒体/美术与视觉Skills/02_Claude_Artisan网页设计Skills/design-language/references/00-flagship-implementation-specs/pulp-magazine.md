# Pulp Magazine Cover Art — Implementation Spec

*Aliases:* pulp fiction cover art, pulp illustration, lurid pulp painting, newsstand pulp
*Slug:* `pulp-magazine` · *Category:* niche · *Era:* 1930s–1950s (revival ongoing)

**Origin.** Cheap American pulp-fiction magazine cover illustration — mass-market newsstand paperbacks and digests printed on cheap wood-pulp paper, sold to move copies fast.

**Reference example.** *Weird Tales*, *Amazing Stories*, *Black Mask* cover paintings; Norman Saunders and Margaret Brundage newsstand cover art.

## Signature move(s)

A single dramatic painted illustration moment — never a sequence of panels — rendered in saturated primary color with a hard black offset shadow behind every major shape, like a cheap four-color press slightly out of registration. A radial vignette wash pushes the eye toward one lurid, melodramatic focal point, and the masthead/headline type sits in heavy black-shadowed slab caps across the top.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Dramatic, high-contrast painted single-image illustration (not sequential panels)
- Saturated primary colors against heavy black shadow
- Bold slab/condensed masthead display type
- Lurid, melodramatic newsstand energy

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/pulp-magazine.css`.)

```css
/* Pulp Magazine Cover Art — design tokens (generated from style_catalog.json) */
/* 1930s–1950s (revival ongoing) | Cheap American pulp-fiction magazine cover illustration. */
:root {
  /* color */
  --color-bg: #1a1210;
  --color-surface: #241a17;
  --color-surface-2: #33231e;
  --color-text: #f5e6d3;
  --color-text-muted: #c9ad8f;
  --color-primary: #d4361f;
  --color-accent: #f2b705;
  --color-pulp-blue: #1c4f8c;
  --color-shadow-ink: #0c0806;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 10px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-lurid: 6px 6px 0 var(--color-shadow-ink);
  --shadow-lurid-sm: 3px 3px 0 var(--color-shadow-ink);
  /* font */
  --font-sans: 'PT Sans', 'Helvetica Neue', system-ui, sans-serif;
  --font-display: 'Anton', 'Oswald', 'Arial Black', sans-serif;
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
  --ease-standard: cubic-bezier(0.5, 0, 0.15, 1);
  /* extra (signature gradients, composite borders, filters) */
  --painted-vignette: radial-gradient(120% 90% at 50% 20%, rgba(212,54,31,0.22), transparent 60%), radial-gradient(140% 100% at 50% 100%, rgba(0,0,0,0.55), transparent 55%);
  --masthead-shadow: 4px 4px 0 var(--color-shadow-ink), 8px 8px 0 rgba(0,0,0,0.25);
  --bg-image: linear-gradient(180deg, #241a17 0%, #1a1210 60%, #0c0806 100%);
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Pulp Magazine Cover Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1a1210",
        "surface": "#241a17",
        "surface-2": "#33231e",
        "text": "#f5e6d3",
        "text-muted": "#c9ad8f",
        "primary": "#d4361f",
        "accent": "#f2b705",
        "pulp-blue": "#1c4f8c",
        "shadow-ink": "#0c0806",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "10px",
        "pill": "999px",
      },
      boxShadow: {
        "lurid": "6px 6px 0 #0c0806",
        "lurid-sm": "3px 3px 0 #0c0806",
      },
      fontFamily: {
        "sans": ["'PT Sans'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Anton'", "'Oswald'", "'Arial Black'", "sans-serif"],
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
        "standard": "cubic-bezier(0.5, 0, 0.15, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --painted-vignette: radial-gradient(120% 90% at 50% 20%, rgba(212,54,31,0.22), transparent 60%), radial-gradient(140% 100% at 50% 100%, rgba(0,0,0,0.55), transparent 55%);
//   --masthead-shadow: 4px 4px 0 #0c0806, 8px 8px 0 rgba(0,0,0,0.25);
//   --bg-image: linear-gradient(180deg, #241a17 0%, #1a1210 60%, #0c0806 100%);
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Dark surface with a hard offset black shadow (`--shadow-lurid-sm`) that grows when pressed toward the viewer on hover. |
| **Input** | Dark well with a muted-tan border, no glow — plain and utilitarian like classified-ad copy. |
| **Card** | Surface washed with `--painted-vignette`, framed by a hard offset shadow, like a cover panel pasted onto the page. |
| **Nav** | Dark bar under a thick primary-red rule, masthead wordmark in shadowed slab caps. |
| **Modal** | Snaps in fast (no easing float) with the full lurid offset-shadow treatment — a "special edition" announcement. |
| **Table** | Alternating dark rows, header row in shadowed display caps, hard rules instead of soft dividers. |
| **Tooltip** | Small accent-yellow bubble with a hard black offset shadow, no blur. |
| **Badge** | Accent-yellow "price sticker" pill with dark ink text and a hard shadow, like a cover price stamp. |
| **Toggle** | Track as a thick painted bar; knob snaps between primary-red (off) and accent-yellow (on) with no easing drift. |
| **Loading** | A pulsing exclamation burst or hard-edged spinning starburst, evoking a cover "SHOCKING!" caption. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- `--color-text` (#f5e6d3) on `--color-bg` (#1a1210) is warm cream on near-black — passes AA with large margin; verify with `contrast_check.py`.
- `--color-text-muted` (#c9ad8f) on `--color-surface`/`--color-surface-2` stays well above 4.5:1 — re-check if you lighten either surface tone.
- Dark ink text on the accent-yellow badge/tooltip fill is intentional and passes AA; never swap in the primary red for small badge text — it drops below 4.5:1 at that size.
- The painted vignette wash is decorative; keep body copy on the flat surface color, not directly inside the darkest vignette corner.
- Hard offset "press" shadows on hover/active must still respect `prefers-reduced-motion` — keep the shadow but drop the translate animation.
- Keep focus rings a solid accent-yellow outline with real offset; the offset shadow is not a substitute for a focus indicator.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every raised surface's shadow hard-edged and offset — no blur, no gradient fade.
- ✅ Reserve full saturation (red, yellow, blue) for a few dominant shapes; let the ground stay dark and desaturated.
- ✅ Set masthead/headline type in heavy shadowed slab caps — that's the newsstand "grab the eye" voice.

## Don't

- ❌ Break the composition into sequential panels or speech bubbles — that's comic's territory, not a single painted pulp cover.
- ❌ Soften the offset shadow into a blurred drop-shadow — it must read as flat, hard-edged, slightly misregistered ink.
- ❌ Desaturate the whole palette into moody grays — pulp covers are lurid and saturated, even against a dark ground.

## Don't confuse this with…

*Commonly confused neighbors:* comic, film-noir, halftone.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
