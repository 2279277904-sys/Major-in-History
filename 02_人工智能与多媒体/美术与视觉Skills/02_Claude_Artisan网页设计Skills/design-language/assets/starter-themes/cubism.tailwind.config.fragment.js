// Cubism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#e8dcc3",
        "surface": "#f2e9d8",
        "surface-2": "#d9c9a3",
        "text": "#1c1610",
        "text-muted": "#5c4f3a",
        "primary": "#b5451f",
        "accent": "#2b4c6f",
        "ochre": "#c68a2e",
        "ink": "#16130f",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "facet": "3px 3px 0 #16130f",
        "collage": "0 6px 18px rgba(22,19,15,0.28)",
      },
      fontFamily: {
        "sans": ["'Arial'", "'Helvetica Neue'", "sans-serif"],
        "display": ["'Georgia'", "'Times New Roman'", "serif"],
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
        "standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --facet-gradient: linear-gradient(115deg, rgba(181,69,31,0.14) 0 32%, rgba(43,76,111,0.12) 32% 61%, rgba(198,138,46,0.16) 61% 100%);
//   --collage-paper: repeating-linear-gradient(4deg, rgba(22,19,15,0.04) 0 2px, transparent 2px 6px);
