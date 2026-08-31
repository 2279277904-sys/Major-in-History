# Amiga Workbench — Implementation Spec

*Aliases:* Workbench UI, AmigaOS desktop, Topaz UI  
*Slug:* `amiga-workbench` · *Category:* niche · *Era:* 1985–1990s

**Origin.** Commodore's AmigaOS desktop environment, "Workbench," shipped with the Amiga 1000 in 1985 and defined the platform's look through the A500/A1200 era into the mid-1990s.

**Reference example.** Workbench 1.3/2.0/3.1 desktop; the Topaz bitmap system font; Deluxe Paint's chrome; classic Amiga demoscene installer screens.

## Signature move(s)

Every surface is built from thick, hard-edged 3D bevels — a 2px light edge on top-left, a 2px dark edge on bottom-right, no gradient, no blur — carved directly out of a tight 4–8 color palette anchored by orange, blue, white, and black. Icons are chunky low-res pixel art, and all system text renders in the blocky bitmap Topaz font. The overall effect is a cheerful, toy-like chunkiness that never apologizes for its resolution.

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Chunky low-res pixel icons and blocky bitmap system font (Topaz)
- Tight, saturated 4–8 color core palette: orange, blue, white, black
- Thick flat 3D-beveled window/button chrome (hard light/dark edges, no gradients)
- Cheerful, toy-like chunky-pixel charm; zero anti-aliasing anywhere

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/amiga-workbench.css`.)

```css
/* Amiga Workbench — design tokens (generated from style_catalog.json) */
/* 1985–1990s | Commodore Amiga desktop: chunky bevels, 4-8 color palette. */
:root {
  /* color */
  --color-bg: #a8a8a8;
  --color-surface: #ffffff;
  --color-surface-2: #d4d4d4;
  --color-text: #000000;
  --color-text-muted: #4a4a4a;
  --color-primary: #0055aa;
  --color-accent: #ff8800;
  --color-bevel-light: #ffffff;
  --color-bevel-dark: #555555;
  --color-titlebar: #0055aa;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;
  --radius-pill: 0px;
  /* shadow */
  --shadow-bevel-out: inset 2px 2px 0 #ffffff, inset -2px -2px 0 #555555;
  --shadow-bevel-in: inset -2px -2px 0 #ffffff, inset 2px 2px 0 #555555;
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Topaz New', 'Press Start 2P', 'Courier New', monospace;
  --font-display: 'Topaz New', 'Press Start 2P', monospace;
  --font-mono: 'Topaz New', 'Courier New', monospace;
  /* text */
  --text-xs: 0.625rem;
  --text-sm: 0.75rem;
  --text-base: 0.875rem;
  --text-lg: 1rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;
  --text-4xl: 2.5rem;
  --text-5xl: 3rem;
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
  --ease-standard: steps(1, end);
  /* extra (signature gradients, composite borders, filters) */
  --titlebar-stripes: repeating-linear-gradient(90deg, #ff8800 0 4px, #0055aa 4px 8px);
  --bg-image: none;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Amiga Workbench — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#a8a8a8",
        "surface": "#ffffff",
        "surface-2": "#d4d4d4",
        "text": "#000000",
        "text-muted": "#4a4a4a",
        "primary": "#0055aa",
        "accent": "#ff8800",
        "bevel-light": "#ffffff",
        "bevel-dark": "#555555",
        "titlebar": "#0055aa",
      },
      borderRadius: {
        "sm": "0px",
        "md": "0px",
        "lg": "0px",
        "pill": "0px",
      },
      boxShadow: {
        "bevel-out": "inset 2px 2px 0 #ffffff, inset -2px -2px 0 #555555",
        "bevel-in": "inset -2px -2px 0 #ffffff, inset 2px 2px 0 #555555",
      },
      fontFamily: {
        "sans": ["'Topaz New'", "'Press Start 2P'", "'Courier New'", "monospace"],
        "display": ["'Topaz New'", "'Press Start 2P'", "monospace"],
        "mono": ["'Topaz New'", "'Courier New'", "monospace"],
      },
      fontSize: {
        "xs": "0.625rem",
        "sm": "0.75rem",
        "base": "0.875rem",
        "lg": "1rem",
        "xl": "1.25rem",
        "2xl": "1.5rem",
        "3xl": "2rem",
        "4xl": "2.5rem",
        "5xl": "3rem",
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
        "standard": "steps(1, end)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --titlebar-stripes: repeating-linear-gradient(90deg, #ff8800 0 4px, #0055aa 4px 8px);
//   --bg-image: none;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Flat grey fill, 2px black outline, hard outward bevel (light top-left/dark bottom-right); pressed state flips the bevel inward. |
| **Input** | White well with an inward bevel (looks "pressed into" the desktop), 2px black border, Topaz text. |
| **Card** | White panel, 2px black border, outward bevel — reads as a mini Workbench window. |
| **Nav** | Blue titlebar with an orange/blue diagonal stripe pattern at the drag corner, outward bevel along the bottom. |
| **Modal** | Same window chrome as Card, but centered with a drop-shadow-free hard black outline — Workbench windows never cast soft shadows. |
| **Table** | Flat white rows, 1px black rules, header row in the blue titlebar color with white text. |
| **Tooltip** | Small white box, 1px black border, no shadow, no radius — like a Workbench menu item. |
| **Badge** | Orange fill, 2px black border, black text — no radius, no gradient. |
| **Toggle** | A physical-looking two-state bevel: outward bevel when off, inward (pressed) bevel when on, orange fill on. |
| **Loading** | A blocky "busy" pointer bitmap swap or a chunky striped progress bar — animation is stepped, not eased. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `#000000` on the mid-grey desktop background `#a8a8a8` measures 8.83:1 — passes AA/AAA comfortably; verify with `contrast_check.py` if you lighten the desktop grey.
- Bitmap fonts (Topaz) can be illegible below their native pixel size when scaled — always provide a real, scalable fallback (`'Courier New', monospace`) for body copy rather than shipping only the bitmap face.
- The bevel-only affordance for pressed/unpressed states relies on directional light/dark edges; add a focus-visible outline (dotted, per the classic Amiga selection marquee) so keyboard users get a state cue that doesn't depend on perceiving bevel direction.
- Because the palette is intentionally tight (4–8 colors), don't introduce additional low-contrast greys for "disabled" — use opacity reduction on the existing high-contrast palette instead.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep bevels hard-edged and 2px — no blur, no gradient softening.
- ✅ Restrict the palette to the orange/blue/white/black core, plus at most a couple of muted greys.
- ✅ Use blocky, low-res-feeling type and icons throughout, not just in one hero spot.

## Don't

- ❌ Add soft drop shadows or rounded corners — Workbench chrome is always hard-edged and square.
- ❌ Use anti-aliased icons or smooth gradients — everything reads as stepped/blocky, deliberately.
- ❌ Expand the palette into a modern 20+ color system — the tight core palette is the point.

## Don't confuse this with…

*Commonly confused neighbors:* ascii-terminal, teletext, y2k-futurism.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
