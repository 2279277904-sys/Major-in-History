// Kintsugi — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1c1a18",
        "surface": "#262320",
        "surface-2": "#322d28",
        "text": "#f0e6d2",
        "text-muted": "#b8ab94",
        "primary": "#d4a53d",
        "accent": "#8a6a3a",
        "seam": "#f0c04d",
        "lacquer": "#100e0c",
      },
      borderRadius: {
        "sm": "3px",
        "md": "10px",
        "lg": "18px",
        "pill": "999px",
      },
      boxShadow: {
        "seam-glow": "0 0 10px rgba(240,192,77,0.45)",
        "vessel": "0 10px 26px rgba(0,0,0,0.5)",
      },
      fontFamily: {
        "sans": ["'Noto Serif JP'", "'Shippori Mincho'", "'Georgia'", "serif"],
        "display": ["'Shippori Mincho'", "'Noto Serif JP'", "serif"],
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
        "standard": "cubic-bezier(0.4, 0, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --seam-gradient: linear-gradient(90deg, transparent, #f0c04d 15%, #d4a53d 50%, #f0c04d 85%, transparent);
//   --glaze-sheen: radial-gradient(circle at 25% 0%, rgba(240,230,210,0.06), transparent 55%);
