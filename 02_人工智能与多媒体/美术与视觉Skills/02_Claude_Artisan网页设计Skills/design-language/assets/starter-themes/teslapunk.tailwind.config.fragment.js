// Teslapunk — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#060b1a",
        "surface": "#0d1830",
        "surface-2": "#142544",
        "text": "#eaf4ff",
        "text-muted": "#9fb8d9",
        "primary": "#4fd8ff",
        "accent": "#d98a3d",
        "brass": "#c9a24b",
        "copper": "#a8622f",
      },
      borderRadius: {
        "sm": "3px",
        "md": "10px",
        "lg": "22px",
        "pill": "999px",
      },
      boxShadow: {
        "arc": "0 0 22px rgba(79,216,255,0.45), 0 8px 22px rgba(0,0,0,0.5)",
        "brass": "0 4px 12px rgba(201,162,75,0.25), inset 0 1px 0 rgba(255,255,255,0.15)",
      },
      fontFamily: {
        "sans": ["'Cormorant'", "'EB Garamond'", "system-ui", "serif"],
        "display": ["'Cinzel'", "'Cormorant'", "serif"],
        "mono": ["'JetBrains Mono'", "ui-monospace", "monospace"],
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
        "standard": "cubic-bezier(0.2, 0.8, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --arc-gradient: radial-gradient(circle at 50% 0%, rgba(79,216,255,0.35), transparent 55%);
//   --brass-trim: linear-gradient(180deg, #e7c47a 0%, #c9a24b 45%, #8a6a2c 100%);
//   --bg-image: radial-gradient(140% 100% at 50% -10%, #142544 0%, #060b1a 60%, #030612 100%);
