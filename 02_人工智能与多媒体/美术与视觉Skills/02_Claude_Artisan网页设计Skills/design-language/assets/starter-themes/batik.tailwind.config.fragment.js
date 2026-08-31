// Batik — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f3e6cd",
        "surface": "#faf1de",
        "surface-2": "#e7d3ab",
        "text": "#2b1c12",
        "text-muted": "#6b5335",
        "primary": "#2c4a6e",
        "accent": "#b5501f",
        "ochre": "#c68a2e",
        "indigo-deep": "#1c3350",
      },
      borderRadius: {
        "sm": "6px",
        "md": "14px",
        "lg": "26px",
        "pill": "999px",
      },
      boxShadow: {
        "cloth": "0 10px 26px rgba(43,28,18,0.18)",
        "cloth-sm": "0 4px 12px rgba(43,28,18,0.14)",
      },
      fontFamily: {
        "sans": ["'Cormorant Garamond'", "'Marcellus'", "system-ui", "serif"],
        "display": ["'Marcellus'", "'Cormorant Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.33, 0.0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --crackle-veins: repeating-conic-gradient(from 20deg at 30% 40%, rgba(43,28,18,0.05) 0deg 4deg, transparent 4deg 26deg);
//   --motif-border: repeating-linear-gradient(90deg, #2c4a6e 0 6px, #c68a2e 6px 8px, transparent 8px 22px);
