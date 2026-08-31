// Nautical / Maritime — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f4f6f8",
        "surface": "#ffffff",
        "surface-2": "#e4e9ee",
        "text": "#0b1f38",
        "text-muted": "#51667e",
        "primary": "#0b1f38",
        "accent": "#b3391f",
        "brass": "#b8873a",
        "rope-tan": "#d9c49a",
      },
      borderRadius: {
        "sm": "2px",
        "md": "6px",
        "lg": "12px",
        "pill": "999px",
      },
      boxShadow: {
        "deck": "0 8px 20px rgba(11,31,56,0.14)",
        "deck-sm": "0 3px 10px rgba(11,31,56,0.12)",
      },
      fontFamily: {
        "sans": ["'Inter'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Oswald'", "'Helvetica Neue'", "sans-serif"],
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
        "standard": "cubic-bezier(0.2, 0, 0.1, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --stripe-field: repeating-linear-gradient(90deg, #0b1f38 0 14px, #ffffff 14px 28px);
//   --rope-border: repeating-linear-gradient(135deg, #b8873a 0 3px, #d9c49a 3px 6px);
