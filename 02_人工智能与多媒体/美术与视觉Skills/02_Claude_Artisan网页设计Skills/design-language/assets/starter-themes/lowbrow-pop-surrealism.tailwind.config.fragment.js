// Lowbrow / Pop Surrealism — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#17151f",
        "surface": "#201c2c",
        "surface-2": "#2c2740",
        "text": "#f4eefc",
        "text-muted": "#b8aed0",
        "primary": "#ff5fa2",
        "accent": "#4fd8e0",
        "gold": "#ffcc33",
        "lineweight": "#0e0c14",
      },
      borderRadius: {
        "sm": "6px",
        "md": "16px",
        "lg": "32px",
        "pill": "999px",
      },
      boxShadow: {
        "glossy": "0 10px 30px rgba(255,95,162,0.25), 0 2px 0 #0e0c14",
        "glossy-sm": "0 4px 14px rgba(79,216,224,0.25), 0 1px 0 #0e0c14",
      },
      fontFamily: {
        "sans": ["'Baloo 2'", "'Nunito'", "system-ui", "sans-serif"],
        "display": ["'Bungee'", "'Baloo 2'", "'Arial Rounded MT Bold'", "sans-serif"],
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
        "standard": "cubic-bezier(0.34, 1.4, 0.3, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --candy-sheen: radial-gradient(60% 45% at 30% 20%, rgba(255,255,255,0.35), transparent 60%);
//   --keyline-outline: 0 0 0 3px #0e0c14;
//   --bg-image: radial-gradient(120% 90% at 80% -10%, #2c2740 0%, #17151f 55%, #0e0c14 100%);
