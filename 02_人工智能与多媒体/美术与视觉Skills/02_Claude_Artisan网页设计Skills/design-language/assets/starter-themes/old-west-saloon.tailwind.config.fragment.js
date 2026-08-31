// Old West / Saloon — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#e8d9b8",
        "surface": "#f0e4c8",
        "surface-2": "#d8c397",
        "text": "#2c1608",
        "text-muted": "#6b4a28",
        "primary": "#7a2e17",
        "accent": "#c99a3b",
        "sienna": "#8a3d1f",
        "star": "#3a3226",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "8px",
        "pill": "999px",
      },
      boxShadow: {
        "weathered": "0 8px 20px rgba(44,22,8,0.28)",
        "weathered-sm": "0 3px 10px rgba(44,22,8,0.24)",
      },
      fontFamily: {
        "sans": ["'Roboto Slab'", "'Georgia'", "serif"],
        "display": ["'Rye'", "'Ultra'", "'Impact'", "'Arial Black'", "serif"],
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
//   --paper-grain: repeating-radial-gradient(circle at 25% 30%, rgba(44,22,8,0.06) 0px, transparent 3px, transparent 9px), repeating-linear-gradient(4deg, rgba(44,22,8,0.04) 0 1px, transparent 1px 6px);
//   --rope-frame: repeating-linear-gradient(135deg, #7a2e17 0 3px, #c99a3b 3px 6px);
