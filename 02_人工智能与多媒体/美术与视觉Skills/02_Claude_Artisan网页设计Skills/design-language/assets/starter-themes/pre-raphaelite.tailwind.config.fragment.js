// Pre-Raphaelite — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1a0f14",
        "surface": "#2a151c",
        "surface-2": "#3d1f28",
        "text": "#f3e6d8",
        "text-muted": "#cbb8a8",
        "primary": "#8c1f3f",
        "accent": "#1f6b4a",
        "gold": "#c9a227",
        "ivory": "#fff6e8",
      },
      borderRadius: {
        "sm": "2px",
        "md": "8px",
        "lg": "20px",
        "pill": "999px",
      },
      boxShadow: {
        "glaze": "0 1px 0 rgba(255,246,232,0.08) inset, 0 14px 34px rgba(0,0,0,0.5)",
        "gilt": "0 0 0 1px #c9a227, 0 10px 26px rgba(140,31,63,0.3)",
      },
      fontFamily: {
        "sans": ["'EB Garamond'", "'Cormorant Garamond'", "serif"],
        "display": ["'Cormorant Garamond'", "'EB Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.3, 0.6, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --gold-glaze: radial-gradient(circle at 30% 0%, rgba(201,162,39,0.16), transparent 55%);
//   --vine-border: linear-gradient(180deg, #1f6b4a 0 8%, transparent 8% 92%, #1f6b4a 92% 100%);
