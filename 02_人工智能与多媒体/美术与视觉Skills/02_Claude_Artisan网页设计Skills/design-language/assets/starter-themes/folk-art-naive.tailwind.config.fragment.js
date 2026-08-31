// Folk Art / Naive Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#fbf1de",
        "surface": "#fff8ec",
        "surface-2": "#f3e2bf",
        "text": "#3a2317",
        "text-muted": "#6b4a35",
        "primary": "#d63b2f",
        "accent": "#2f7a63",
        "mustard": "#e0a629",
        "outline-ink": "#2b1a10",
      },
      borderRadius: {
        "sm": "6px",
        "md": "14px",
        "lg": "24px",
        "pill": "999px",
      },
      boxShadow: {
        "outline": "0 3px 0 #2b1a10",
        "outline-sm": "0 2px 0 #2b1a10",
      },
      fontFamily: {
        "sans": ["'Fredoka'", "'Baloo 2'", "system-ui", "sans-serif"],
        "display": ["'Baloo 2'", "'Fredoka'", "sans-serif"],
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
        "standard": "cubic-bezier(0.34, 1.56, 0.64, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --motif-border: repeating-linear-gradient(45deg, #d63b2f 0 6px, #e0a629 6px 12px, #2f7a63 12px 18px);
//   --outline-stroke: 3px solid #2b1a10;
