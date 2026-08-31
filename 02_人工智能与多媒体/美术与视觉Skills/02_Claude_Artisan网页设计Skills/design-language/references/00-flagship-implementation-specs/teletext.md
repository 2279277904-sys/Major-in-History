# Teletext — Implementation Spec

*Aliases:* Ceefax UI, videotex, viewdata graphics  
*Slug:* `teletext` · *Category:* niche · *Era:* 1970s–90s

**Origin.** Broadcast teletext services — BBC Ceefax and ITV Oracle in the UK (1974 onward), France's Antiope/Minitel-adjacent videotex — delivered text and crude graphics over unused broadcast TV lines, decoded by dedicated receiver chips through the 1990s.

**Reference example.** BBC Ceefax; ITV Oracle; French Minitel terminal screens; teletext subtitle/caption overlays.

## Signature move(s)

The screen is a fixed 40×24 grid of character cells; every "graphic" is built from a strict set of mosaic block characters filling those cells, rendered in one of exactly seven saturated colors (red, green, yellow, blue, magenta, cyan, white) on a pure black ground — no gradients, no anti-aliasing, no intermediate shades. Navigation happens by typing a three-digit page number, and that page-number motif (a red or yellow numeral badge) should appear anywhere the UI implies "go to a specific screen."

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Extremely low-res blocky mosaic character graphics (fixed grid cells)
- Strict 7-color palette (black bg + red/green/yellow/blue/magenta/cyan/white), zero gradients
- Monospaced blocky type only, no anti-aliasing
- Page-number navigation motif (P.1xx style badges/labels)

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/teletext.css`.)

```css
/* Teletext — design tokens (generated from style_catalog.json) */
/* 1970s–90s | Broadcast teletext/videotex: blocky mosaic graphics, strict 7-color palette. */
:root {
  /* color */
  --color-bg: #000000;
  --color-surface: #000000;
  --color-surface-2: #1a1a1a;
  --color-text: #ffffff;
  --color-text-muted: #00ff00;
  --color-primary: #00ff00;
  --color-red: #ff0000;
  --color-yellow: #ffff00;
  --color-blue: #0000ff;
  --color-magenta: #ff00ff;
  --color-cyan: #00ffff;
  --color-white: #ffffff;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;
  --radius-pill: 0px;
  /* shadow */
  --shadow-block: none;
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Bedstead', 'Courier New', monospace;
  --font-display: 'Bedstead', 'Courier New', monospace;
  --font-mono: 'Bedstead', 'Courier New', monospace;
  /* text */
  --text-xs: 0.875rem;
  --text-sm: 1rem;
  --text-base: 1.125rem;
  --text-lg: 1.25rem;
  --text-xl: 1.5rem;
  --text-2xl: 1.875rem;
  --text-3xl: 2.25rem;
  --text-4xl: 3rem;
  --text-5xl: 3.75rem;
  /* space */
  --space-1: 8px;
  --space-2: 16px;
  --space-3: 20px;
  --space-4: 24px;
  --space-6: 32px;
  --space-8: 40px;
  --space-12: 56px;
  --space-16: 72px;
  --space-24: 96px;
  /* ease */
  --ease-standard: steps(1, end);
  /* extra (signature gradients, composite borders, filters) */
  --mosaic-block: repeating-linear-gradient(0deg, currentColor 0 2px, transparent 2px 4px);
  --bg-image: none;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Teletext — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#000000",
        "surface": "#000000",
        "surface-2": "#1a1a1a",
        "text": "#ffffff",
        "text-muted": "#00ff00",
        "primary": "#00ff00",
        "red": "#ff0000",
        "yellow": "#ffff00",
        "blue": "#0000ff",
        "magenta": "#ff00ff",
        "cyan": "#00ffff",
        "white": "#ffffff",
      },
      borderRadius: {
        "sm": "0px",
        "md": "0px",
        "lg": "0px",
        "pill": "0px",
      },
      boxShadow: {
        "block": "none",
      },
      fontFamily: {
        "sans": ["'Bedstead'", "'Courier New'", "monospace"],
        "display": ["'Bedstead'", "'Courier New'", "monospace"],
        "mono": ["'Bedstead'", "'Courier New'", "monospace"],
      },
      fontSize: {
        "xs": "0.875rem",
        "sm": "1rem",
        "base": "1.125rem",
        "lg": "1.25rem",
        "xl": "1.5rem",
        "2xl": "1.875rem",
        "3xl": "2.25rem",
        "4xl": "3rem",
        "5xl": "3.75rem",
      },
      spacing: {
        "1": "8px",
        "2": "16px",
        "3": "20px",
        "4": "24px",
        "6": "32px",
        "8": "40px",
        "12": "56px",
        "16": "72px",
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
//   --mosaic-block: repeating-linear-gradient(0deg, currentColor 0 2px, transparent 2px 4px);
//   --bg-image: none;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Solid block fill (yellow default, red for primary), square corners, black uppercase or white text — reads like a filled character cell, not a rendered button. |
| **Input** | White cell block with black text, no border radius, no placeholder styling beyond dim grey — mimics a teletext "reveal" input line. |
| **Card** | Black panel framed by a solid 4px cyan rule (no shadow, no gradient) — the border itself is the only elevation cue. |
| **Nav** | Solid blue bar (a classic Ceefax header color) with a cyan bottom rule, page-number label pinned top-left. |
| **Modal** | Same block-bordered panel as Card, appears instantly with no transition — teletext pages "flip," they don't animate. |
| **Table** | Flat rows in alternating background blocks (e.g., black/blue), header row in solid yellow-on-black. |
| **Tooltip** | A solid-color block callout (magenta or cyan fill, black text), no blur or shadow. |
| **Badge** | Solid magenta or red block, square, bold uppercase black or white text — modeled on the page-number badge motif. |
| **Toggle** | Two solid-color blocks side by side (e.g., red = off block, green = on block) rather than a sliding knob — teletext has no continuous motion primitive. |
| **Loading** | A cycling color-block sequence (red→yellow→green blocks appearing in turn) instead of a spinner — evokes the page-building "reveal" scan. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- White text `#ffffff` on black `#000000` measures 21:1; yellow `#ffff00` on black measures 19.56:1; green `#00ff00` on black measures 15.3:1 — all verified AAA with `contrast_check.py`. Avoid the historically-accurate-but-risky combination of cyan-on-white or blue-on-black for body copy without rechecking (blue `#0000ff` on black is only ~2.4:1 and fails AA — reserve pure blue for large headers/bars, never body text).
- Because the palette is fixed to seven saturated hues, never rely on hue alone to distinguish state (e.g., "red = error, green = success") without also changing the label text — colorblind users may not distinguish red/green/magenta reliably at this saturation.
- Blocky mosaic graphics can visually vibrate at small sizes; keep block-pattern decoration large and low-frequency, and never place body text directly over an active mosaic pattern.
- Bold/uppercase monospace at teletext's native low resolution is legible; when adapting to real screens, don't shrink below the `--text-sm` token or the "chunky" character shapes stop reading as intentional and just look broken.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every fill a flat, saturated block from the seven-color set — no tints, no gradients.
- ✅ Use the page-number motif (P.1xx style badges) for any navigation or "jump to" affordance.
- ✅ Keep type monospaced, blocky, and mostly uppercase for headers/labels.

## Don't

- ❌ Add gradients, blur, or anti-aliasing anywhere — teletext graphics are hard-edged by transmission constraint, not choice, and that constraint is the whole aesthetic.
- ❌ Introduce colors outside the seven-hue set — no pastels, no off-black, no tinted greys.
- ❌ Animate with eased transitions — teletext pages cut/flip instantly, they never tween.

## Don't confuse this with…

*Commonly confused neighbors:* ascii-terminal, ansi-bbs-art, amiga-workbench.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
