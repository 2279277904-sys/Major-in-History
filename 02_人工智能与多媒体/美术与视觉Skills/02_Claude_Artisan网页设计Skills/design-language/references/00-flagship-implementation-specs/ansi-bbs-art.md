# ANSI / BBS Art — Implementation Spec

*Aliases:* ANSI art, BBS splash art, TheDraw art, CP437 mosaic  
*Slug:* `ansi-bbs-art` · *Category:* niche · *Era:* 1980s–90s

**Origin.** Dial-up bulletin board systems (BBSes) used ANSI escape codes and the CP437 extended-ASCII character set to render colorful splash screens, menus, and "artscene" signature pieces — drawn in tools like TheDraw and traded through groups like ACiD and iCE through the 1980s–90s.

**Reference example.** Classic BBS login/menu splash screens; ACiD/iCE Productions ANSI art packs; TheDraw-authored door-game menus.

## Signature move(s)

Every surface is built from the 16-color ANSI palette (8 base + 8 "bright" variants) rendered through CP437 block and line-drawing glyphs — half-blocks (░▒▓), double-line box borders (═║╔╗╚╝), and shading characters — all on a black ground, all monospaced, never anti-aliased. Compositions favor saturated primary/neon combinations (red, cyan, yellow, magenta, green, blue, white) packed densely into a fixed character grid, with a strong sense of "hand-drawn in a text editor."

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- 16-color ANSI/CP437 block-character art (half-blocks, shading glyphs)
- Saturated primary/neon palette on pure black, no gradients
- Blocky extended-ASCII border and shading characters (double-line boxes, ░▒▓)
- Monospaced type only, everywhere — no proportional fonts

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/ansi-bbs-art.css`.)

```css
/* ANSI / BBS Art — design tokens (generated from style_catalog.json) */
/* 1980s-90s | Dial-up BBS splash art: 16-color ANSI/CP437 block-character mosaics. */
:root {
  /* color */
  --color-bg: #000000;
  --color-surface: #0a0a0a;
  --color-surface-2: #1c1c1c;
  --color-text: #c0c0c0;
  --color-text-muted: #808080;
  --color-primary: #ff5555;
  --color-accent: #55ffff;
  --color-yellow: #ffff55;
  --color-green: #55ff55;
  --color-magenta: #ff55ff;
  --color-blue: #5555ff;
  --color-white: #ffffff;
  --color-red-dark: #aa0000;
  /* radius */
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;
  --radius-pill: 0px;
  /* shadow */
  --shadow-none: none;
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Perfect DOS VGA 437', 'Courier New', monospace;
  --font-display: 'Perfect DOS VGA 437', 'Courier New', monospace;
  --font-mono: 'Perfect DOS VGA 437', 'Courier New', monospace;
  /* text */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.375rem;
  --text-2xl: 1.75rem;
  --text-3xl: 2.25rem;
  --text-4xl: 3rem;
  --text-5xl: 3.75rem;
  /* space */
  --space-1: 1ch;
  --space-2: 2ch;
  --space-3: 3ch;
  --space-4: 4ch;
  --space-6: 6ch;
  --space-8: 8ch;
  --space-12: 12ch;
  --space-16: 16ch;
  --space-24: 24ch;
  /* ease */
  --ease-standard: steps(1, end);
  /* extra (signature gradients, composite borders, filters) */
  --box-double: 3px double #55ffff;
  --shade-block: repeating-linear-gradient(45deg, currentColor 0 1px, transparent 1px 3px);
  --bg-image: none;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// ANSI / BBS Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#000000",
        "surface": "#0a0a0a",
        "surface-2": "#1c1c1c",
        "text": "#c0c0c0",
        "text-muted": "#808080",
        "primary": "#ff5555",
        "accent": "#55ffff",
        "yellow": "#ffff55",
        "green": "#55ff55",
        "magenta": "#ff55ff",
        "blue": "#5555ff",
        "white": "#ffffff",
        "red-dark": "#aa0000",
      },
      borderRadius: {
        "sm": "0px",
        "md": "0px",
        "lg": "0px",
        "pill": "0px",
      },
      boxShadow: {
        "none": "none",
      },
      fontFamily: {
        "sans": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
        "display": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
        "mono": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
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
        "5xl": "3.75rem",
      },
      spacing: {
        "1": "1ch",
        "2": "2ch",
        "3": "3ch",
        "4": "4ch",
        "6": "6ch",
        "8": "8ch",
        "12": "12ch",
        "16": "16ch",
        "24": "24ch",
      },
      transitionTimingFunction: {
        "standard": "steps(1, end)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --box-double: 3px double #55ffff;
//   --shade-block: repeating-linear-gradient(45deg, currentColor 0 1px, transparent 1px 3px);
//   --bg-image: none;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Solid flat color block (green default, red for primary), thin white 1px border, bracketed uppercase label (e.g. `[Y]es`) evoking a BBS hotkey menu. |
| **Input** | Black field with green monospace text, a blinking-cursor feel, and a plain 1px grey border that turns cyan on focus. |
| **Card** | Black panel wrapped in a `--box-double` cyan double-line border, no radius, no shadow. |
| **Nav** | Solid blue bar with a double-line bottom border and a centered ASCII-banner-style title. |
| **Modal** | Same double-line-bordered panel as Card, appears instantly — BBS screens redraw, they don't fade. |
| **Table** | Flat monospace rows, alternating dim/bright text color, single-line ASCII rule between header and body. |
| **Tooltip** | Small block-color callout (magenta fill, black text), single-line border, no blur. |
| **Badge** | Solid magenta or cyan block, square corners, bold uppercase black text — modeled on a BBS "new message" flag. |
| **Toggle** | Two adjacent character-cell blocks (e.g. `[ON]`/`[OFF]` bracketed text) that swap fill color rather than sliding — no continuous motion in this vocabulary. |
| **Loading** | A classic ANSI "spinner" character cycle (`|/-\`) or a sweeping block-character progress bar, stepped not eased. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `#c0c0c0` (ANSI "light grey") on black `#000000` measures 11.54:1, and the yellow accent `#ffff55` on black measures 19.69:1 — both verified AA/AAA with `contrast_check.py`. Avoid the historically-common dark-blue-on-black combination (`#5555ff` on `#000000` is only ~3.1:1) for body text; reserve it for large banner fills only.
- With 16 saturated hues in play, never encode meaning by color alone (e.g., "red = locked door, green = open door") — pair every color-coded state with a bracketed text label or icon glyph, matching the style's own convention of labeling hotkeys in brackets.
- CP437 block/shading glyphs used as decorative texture (░▒▓) must never sit directly behind body text at full opacity — keep dense shading patterns to borders/backgrounds away from the reading column, or contrast drops unpredictably per-glyph.
- Because everything is monospaced, don't shrink text below `--text-sm` to fit more into the character grid — legibility, not density, should win when the two conflict.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Use only the 16-color ANSI palette (8 standard + 8 bright) — no colors outside that set.
- ✅ Build borders and dividers from box-drawing/double-line characters, not CSS radius or shadow.
- ✅ Keep every hotkey/action labeled with a bracketed letter, matching authentic BBS menu conventions.

## Don't

- ❌ Anti-alias or blur any edge — CP437 glyphs are hard-pixel by definition.
- ❌ Use it as a synonym for monochrome green terminal text — that register belongs to ascii-terminal; this style is full 16-color mosaic art.
- ❌ Add rounded corners or soft shadows anywhere — box-drawing characters are the only "border" vocabulary this style has.

## Don't confuse this with…

*Commonly confused neighbors:* ascii-terminal, teletext, amiga-workbench.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
