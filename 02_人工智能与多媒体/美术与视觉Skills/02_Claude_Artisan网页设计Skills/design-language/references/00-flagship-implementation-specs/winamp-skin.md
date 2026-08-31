# Winamp Skin — Implementation Spec

*Aliases:* skinnable media player UI, brushed-metal player chrome  
*Slug:* `winamp-skin` · *Category:* niche · *Era:* late-1990s/early-2000s

**Origin.** Winamp's classic skin engine (1997 onward) turned the media-player chrome itself into a customizable canvas; a vast fan skinning economy (Winamp Skin Museum, WinampHeaven-era communities) produced thousands of brushed-metal, chrome, and hardware-panel skins through the early 2000s.

**Reference example.** Classic Winamp 2.x default skin; Winamp Skin Museum archive; Sonique and early WMP "hardware panel" skins.

## Signature move(s)

The whole interface reads as a physical hardware faceplate shrunk into a tiny window: brushed-metal or chrome-gradient panels, bevelled buttons the size of postage stamps, and a neon-green LED-style spectrum/level meter that's always animating. Controls are packed edge-to-edge — the UI deliberately fits more knobs, sliders, and readouts than the available space comfortably allows, because that density is what reads as "professional audio gear" rather than "software."

> Apply the signature move to *every relevant surface*, not once decoratively. Repeating it is what makes the style read as intentional.

## Defining traits

- Brushed-metal or chrome-gradient panel chrome throughout
- Tiny, pixel-precise controls (buttons, sliders, knobs at native small sizes)
- Neon-green LED-style level meters/visualizer accents
- Dense, "more controls than space" skeuomorphic hardware-panel layout

## Design tokens (CSS custom properties)

Paste into a `:root` block. (Also saved as a ready-to-import file at `assets/starter-themes/winamp-skin.css`.)

```css
/* Winamp Skin — design tokens (generated from style_catalog.json) */
/* late-90s/early-2000s | Brushed metal / chrome player-skin chrome, neon LED meters. */
:root {
  /* color */
  --color-bg: #0c0d10;
  --color-surface: #26292e;
  --color-surface-2: #34383f;
  --color-text: #d8dde3;
  --color-text-muted: #8b929c;
  --color-primary: #39ff6a;
  --color-primary-dim: #1c8f3b;
  --color-accent: #ffb347;
  --color-led-red: #ff4d4d;
  --color-chrome-hi: #eef1f4;
  --color-chrome-lo: #14161a;
  /* radius */
  --radius-sm: 2px;
  --radius-md: 3px;
  --radius-lg: 6px;
  --radius-pill: 999px;
  /* shadow */
  --shadow-panel: inset 0 1px 0 rgba(255,255,255,0.15), inset 0 -1px 0 rgba(0,0,0,0.6), 0 2px 4px rgba(0,0,0,0.5);
  --shadow-inset: inset 0 2px 3px rgba(0,0,0,0.7), inset 0 -1px 0 rgba(255,255,255,0.06);
  --shadow-led: 0 0 6px rgba(57,255,106,0.8);
  /* blur */
  --blur-none: 0px;
  /* font */
  --font-sans: 'Arial', 'Tahoma', sans-serif;
  --font-display: 'Arial Narrow', 'Tahoma', sans-serif;
  --font-mono: 'Fixedsys', 'Courier New', monospace;
  /* text */
  --text-xs: 0.625rem;
  --text-sm: 0.6875rem;
  --text-base: 0.75rem;
  --text-lg: 0.875rem;
  --text-xl: 1rem;
  --text-2xl: 1.25rem;
  --text-3xl: 1.75rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  /* space */
  --space-1: 2px;
  --space-2: 4px;
  --space-3: 6px;
  --space-4: 10px;
  --space-6: 16px;
  --space-8: 22px;
  --space-12: 32px;
  --space-16: 48px;
  --space-24: 72px;
  /* ease */
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  /* extra (signature gradients, composite borders, filters) */
  --brushed-metal: repeating-linear-gradient(180deg, #2d3037 0 1px, #24272c 1px 2px);
  --chrome-gradient: linear-gradient(180deg, #eef1f4 0%, #9aa1ab 45%, #14161a 51%, #3a3e46 100%);
  --led-meter: linear-gradient(90deg, #1c8f3b 0%, #39ff6a 70%, #ffb347 88%, #ff4d4d 100%);
  --bg-image: none;
}
```

## Tailwind config fragment

Merge into `tailwind.config.js` under `theme.extend`.

```js
// Winamp Skin — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#0c0d10",
        "surface": "#26292e",
        "surface-2": "#34383f",
        "text": "#d8dde3",
        "text-muted": "#8b929c",
        "primary": "#39ff6a",
        "primary-dim": "#1c8f3b",
        "accent": "#ffb347",
        "led-red": "#ff4d4d",
        "chrome-hi": "#eef1f4",
        "chrome-lo": "#14161a",
      },
      borderRadius: {
        "sm": "2px",
        "md": "3px",
        "lg": "6px",
        "pill": "999px",
      },
      boxShadow: {
        "panel": "inset 0 1px 0 rgba(255,255,255,0.15), inset 0 -1px 0 rgba(0,0,0,0.6), 0 2px 4px rgba(0,0,0,0.5)",
        "inset": "inset 0 2px 3px rgba(0,0,0,0.7), inset 0 -1px 0 rgba(255,255,255,0.06)",
        "led": "0 0 6px rgba(57,255,106,0.8)",
      },
      fontFamily: {
        "sans": ["'Arial'", "'Tahoma'", "sans-serif"],
        "display": ["'Arial Narrow'", "'Tahoma'", "sans-serif"],
        "mono": ["'Fixedsys'", "'Courier New'", "monospace"],
      },
      fontSize: {
        "xs": "0.625rem",
        "sm": "0.6875rem",
        "base": "0.75rem",
        "lg": "0.875rem",
        "xl": "1rem",
        "2xl": "1.25rem",
        "3xl": "1.75rem",
        "4xl": "2.25rem",
        "5xl": "3rem",
      },
      spacing: {
        "1": "2px",
        "2": "4px",
        "3": "6px",
        "4": "10px",
        "6": "16px",
        "8": "22px",
        "12": "32px",
        "16": "48px",
        "24": "72px",
      },
      transitionTimingFunction: {
        "standard": "cubic-bezier(0.4, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --brushed-metal: repeating-linear-gradient(180deg, #2d3037 0 1px, #24272c 1px 2px);
//   --chrome-gradient: linear-gradient(180deg, #eef1f4 0%, #9aa1ab 45%, #14161a 51%, #3a3e46 100%);
//   --led-meter: linear-gradient(90deg, #1c8f3b 0%, #39ff6a 70%, #ffb347 88%, #ff4d4d 100%);
//   --bg-image: none;
```

## Component rules (the 10 primitives)

Each shows how that primitive expresses the signature move.

| Primitive | How it expresses the style |
| --- | --- |
| **Button** | Tiny brushed-metal chip with an outward panel bevel; pressed state flips to an inset shadow, mimicking a real hardware button being pushed. |
| **Input** | A recessed black LCD-style readout well with green monospace text and an inset shadow, like a track-name display. |
| **Card** | Brushed-metal panel with a 1px dark border and outward panel bevel — a self-contained "module" like the EQ or playlist window. |
| **Nav** | Slim brushed-metal titlebar strip, dense with tiny icon-only controls crowded to the edges. |
| **Modal** | Same brushed panel treatment as Card, snaps open instantly (no easing spring — skins pop, they don't glide). |
| **Table** | Dense playlist rows, alternating dark shades, green monospace track text, tiny row height. |
| **Tooltip** | Small dark LCD-style bubble with a thin green border, monospace text, no blur. |
| **Badge** | Recessed LED-style pill with a glowing green border and glow shadow — reads as a physical indicator light. |
| **Toggle** | A tiny physical-looking rocker: inset/pressed look when on with a green LED glow, outward bevel when off. |
| **Loading** | An animating LED-meter bar (`--led-meter` gradient sweeping) rather than a spinner — mimics a VU meter. |

Cover all interactive states for the button at minimum: default / hover / active / disabled (and focus-visible for accessibility).

## Accessibility corrections (required)

Trendy styles often fight legibility by default. For this style specifically:

- Body text `#d8dde3` on the brushed-metal surface `#26292e` measures 10.68:1, and the LED green `#39ff6a` on the near-black readout well `#0c0d10` measures 14.51:1 — both verified AA/AAA with `contrast_check.py`.
- The style's native type sizes are very small (native skins often used 6–8px bitmap fonts); the tokens here are scaled up to a minimum `--text-xs` of 10px — never go below that for real body copy or labels, regardless of how "authentic" tinier text looks.
- Tiny pixel-precise controls fail touch-target guidance (44×44px minimum) at their native size — keep the *visual* footprint small but pad the actual hit area on interactive elements so the aesthetic doesn't create a mobile/motor-accessibility failure.
- LED-meter and glow-shadow color must never be the only signal for an error/success state — pair it with an icon or text change, since the green/red LED pairing is a common colorblind confusion.

Always finish with `scripts/contrast_check.py` on real text/background pairs and `scripts/consistency_audit.py` on the codebase.

## Do

- ✅ Keep every panel textured with the brushed-metal repeating gradient, not a flat fill.
- ✅ Use the neon-green LED accent sparingly but consistently for meters, indicators, and "live" states.
- ✅ Pack controls densely — negative space reads as "wrong" for this style; let panels feel crowded.

## Don't

- ❌ Round corners generously or add soft ambient shadows — chrome/metal panels use hard bevels, not soft elevation.
- ❌ Use a broad Y2K rainbow palette — Winamp skins are dominated by metal greys plus one neon accent, not multicolor holography (that's y2k-futurism's territory).
- ❌ Space controls out for modern touch-friendly breathing room — the density is the signature, not a flaw to fix.

## Don't confuse this with…

*Commonly confused neighbors:* y2k-futurism, acid-graphics, amiga-workbench.

---
*Generated from `scripts/style_catalog.json` + authored spec. Regenerate rather than hand-editing so tokens stay in sync.*
