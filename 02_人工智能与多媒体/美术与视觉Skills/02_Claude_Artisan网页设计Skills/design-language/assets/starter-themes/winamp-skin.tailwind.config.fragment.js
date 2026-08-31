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
