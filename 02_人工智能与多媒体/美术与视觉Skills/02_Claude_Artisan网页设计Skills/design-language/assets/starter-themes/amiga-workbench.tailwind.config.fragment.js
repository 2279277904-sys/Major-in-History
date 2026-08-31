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
