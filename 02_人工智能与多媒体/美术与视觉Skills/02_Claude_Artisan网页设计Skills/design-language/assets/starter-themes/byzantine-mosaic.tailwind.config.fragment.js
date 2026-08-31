// Byzantine Mosaic — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#0d1b3d",
        "surface": "#142a5c",
        "surface-2": "#1c3a7a",
        "text": "#f5e6b8",
        "text-muted": "#c9b57a",
        "primary": "#d4af37",
        "accent": "#7a1f3d",
        "emerald-tile": "#1f6b4a",
        "gold-ground": "#caa036",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "8px",
        "pill": "999px",
      },
      boxShadow: {
        "gold-glow": "0 0 20px rgba(212,175,55,0.40), 0 8px 20px rgba(0,0,0,0.45)",
        "tile": "0 2px 0 rgba(0,0,0,0.35)",
      },
      fontFamily: {
        "sans": ["'Cormorant Garamond'", "'EB Garamond'", "serif"],
        "display": ["'Cinzel'", "'Cormorant Garamond'", "serif"],
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
        "standard": "cubic-bezier(0.3, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --tesserae-gradient: linear-gradient(135deg, #caa036 0%, #d4af37 20%, #b8860b 40%, #d4af37 60%, #caa036 80%, #b8860b 100%);
//   --tile-grid: repeating-linear-gradient(45deg, rgba(0,0,0,0.12) 0 2px, transparent 2px 8px);
