// Daguerreotype — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#d9d2c4",
        "surface": "#eae5da",
        "surface-2": "#c9c0ac",
        "text": "#2b2621",
        "text-muted": "#5c5347",
        "primary": "#4a4238",
        "accent": "#8a6d3a",
        "silver": "#b8b2a0",
        "sepia": "#6b5a3f",
      },
      borderRadius: {
        "sm": "4px",
        "md": "10px",
        "lg": "40px",
        "pill": "999px",
      },
      boxShadow: {
        "vignette": "inset 0 0 60px rgba(20,16,10,0.45)",
        "plate": "0 6px 20px rgba(20,16,10,0.30)",
      },
      fontFamily: {
        "sans": ["'Cormorant'", "'EB Garamond'", "serif"],
        "display": ["'Playfair Display'", "'Cormorant'", "serif"],
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
        "standard": "cubic-bezier(0.4, 0.0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --vignette-gradient: radial-gradient(ellipse at center, transparent 40%, rgba(20,16,10,0.55) 100%);
//   --gilt-edge: 0 0 0 3px #8a6d3a, 0 0 0 5px #d9d2c4;
