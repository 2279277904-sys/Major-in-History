// Street Art / Graffiti — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#2b2b2b",
        "surface": "#383838",
        "surface-2": "#454545",
        "text": "#f5f5f0",
        "text-muted": "#b8b8b0",
        "primary": "#ff3b3b",
        "accent": "#ffd400",
        "cyan": "#26c6da",
        "keyline": "#0a0a0a",
      },
      borderRadius: {
        "sm": "2px",
        "md": "8px",
        "lg": "18px",
        "pill": "999px",
      },
      boxShadow: {
        "spray": "0 0 0 4px #0a0a0a, 0 10px 24px rgba(0,0,0,0.45)",
        "drip": "0 8px 0 -2px rgba(255,59,59,0.35), 0 12px 4px -4px rgba(0,0,0,0.4)",
      },
      fontFamily: {
        "sans": ["'Archivo Black'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Titan One'", "'Archivo Black'", "'Impact'", "sans-serif"],
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
        "standard": "cubic-bezier(0.3, 0.9, 0.4, 1.2)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --spray-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.05) 0, transparent 3%), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.04) 0, transparent 4%), radial-gradient(circle at 40% 80%, rgba(255,255,255,0.04) 0, transparent 3%);
//   --wildstyle-outline: 0 0 0 3px #0a0a0a, 0 0 0 5px #ffd400;
//   --bg-image: linear-gradient(165deg, #383838 0%, #2b2b2b 55%, #1f1f1f 100%);
