// Populuxe — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f4ede0",
        "surface": "#fffaf3",
        "surface-2": "#ffe3ec",
        "text": "#2b2320",
        "text-muted": "#6b5f56",
        "primary": "#ff6f61",
        "accent": "#1fb5a3",
        "chrome": "#c8ccd0",
        "gold": "#d4af37",
      },
      borderRadius: {
        "sm": "4px",
        "md": "10px",
        "lg": "20px",
        "pill": "999px",
      },
      boxShadow: {
        "chrome": "0 0 0 1px #ffffff, 0 0 0 2px #c8ccd0, 0 8px 20px rgba(43,35,32,0.18)",
        "starburst": "0 10px 24px rgba(255,111,97,0.25)",
      },
      fontFamily: {
        "sans": ["'Futura'", "'Century Gothic'", "'Trebuchet MS'", "sans-serif"],
        "display": ["'Futura'", "'Century Gothic'", "sans-serif"],
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
//   --starburst: conic-gradient(from 0deg, #ff6f61 0 6deg, transparent 6deg 30deg, #1fb5a3 30deg 36deg, transparent 36deg 60deg, #d4af37 60deg 66deg, transparent 66deg 90deg);
//   --boomerang-sweep: linear-gradient(100deg, #ffe3ec 0 38%, transparent 38% 62%, rgba(31,181,163,0.16) 62% 100%);
