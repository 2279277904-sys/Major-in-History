// Neoclassicism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2ede0",
        "surface": "#faf7ef",
        "surface-2": "#e3dbc7",
        "text": "#1f2733",
        "text-muted": "#5a5850",
        "primary": "#8a6d3b",
        "accent": "#2f3b52",
        "marble-vein": "#c9c0a8",
        "ink": "#14181f",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "plinth": "0 1px 0 #ffffff inset, 0 10px 22px rgba(31,39,51,0.14)",
        "relief": "0 1px 2px rgba(31,39,51,0.22)",
      },
      fontFamily: {
        "sans": ["'Trajan Pro'", "'Cinzel'", "'Georgia'", "serif"],
        "display": ["'Cinzel'", "'Trajan Pro'", "serif"],
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
        "standard": "cubic-bezier(0.4, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --pediment-cap: linear-gradient(180deg, #e3dbc7 0 3px, transparent 3px);
//   --fluted-divider: repeating-linear-gradient(90deg, #c9c0a8 0 1px, transparent 1px 10px);
