// Chalkboard Lettering — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1f2421",
        "surface": "#262b27",
        "surface-2": "#323830",
        "text": "#f5f5f0",
        "text-muted": "#b8bdb4",
        "primary": "#f5f5f0",
        "accent": "#f4a6c1",
        "chalk-teal": "#8fd9c4",
        "chalk-yellow": "#f5e08a",
      },
      borderRadius: {
        "sm": "3px",
        "md": "8px",
        "lg": "16px",
        "pill": "999px",
      },
      boxShadow: {
        "chalk-dust": "0 2px 6px rgba(0,0,0,0.40)",
        "chalk-glow": "0 0 8px rgba(245,245,240,0.18)",
      },
      fontFamily: {
        "sans": ["'Patrick Hand'", "'Comic Neue'", "cursive"],
        "display": ["'Caveat'", "'Kalam'", "cursive"],
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
        "standard": "cubic-bezier(0.34, 1.2, 0.64, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --chalk-texture: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.03) 0 1px, transparent 1px), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.025) 0 1px, transparent 1px);
//   --wobble: rotate(-0.4deg);
