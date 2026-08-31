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
