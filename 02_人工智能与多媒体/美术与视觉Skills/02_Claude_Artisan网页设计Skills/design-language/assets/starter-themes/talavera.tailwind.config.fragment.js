// Talavera — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f5f2ea",
        "surface": "#ffffff",
        "surface-2": "#e7edf2",
        "text": "#0b2f52",
        "text-muted": "#3d5a75",
        "primary": "#0b2f52",
        "accent": "#d94f2b",
        "yellow": "#f2b705",
        "green": "#3f7d4c",
      },
      borderRadius: {
        "sm": "8px",
        "md": "16px",
        "lg": "28px",
        "pill": "999px",
      },
      boxShadow: {
        "glaze": "0 12px 28px rgba(11,47,82,0.16), inset 0 1px 0 rgba(255,255,255,0.6)",
        "glaze-sm": "0 4px 12px rgba(11,47,82,0.14)",
      },
      fontFamily: {
        "sans": ["'Fraunces'", "'Playfair Display'", "system-ui", "serif"],
        "display": ["'Playfair Display'", "'Fraunces'", "serif"],
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
        "standard": "cubic-bezier(0.34, 1.2, 0.4, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --glaze-sheen: linear-gradient(135deg, rgba(255,255,255,0.55) 0%, transparent 35%);
//   --tile-border: repeating-linear-gradient(90deg, #0b2f52 0 4px, #f2b705 4px 8px, #d94f2b 8px 12px, #3f7d4c 12px 16px);
