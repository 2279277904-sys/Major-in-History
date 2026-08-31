// Circus / Carnival Poster — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2e6c9",
        "surface": "#fdf8ec",
        "surface-2": "#e8d6a8",
        "text": "#241812",
        "text-muted": "#5c4429",
        "primary": "#c81d25",
        "accent": "#d4a017",
        "navy": "#1c2a52",
        "cream": "#f2e6c9",
      },
      borderRadius: {
        "sm": "2px",
        "md": "6px",
        "lg": "14px",
        "pill": "999px",
      },
      boxShadow: {
        "poster": "0 6px 0 #1c2a52, 0 10px 18px rgba(28,19,10,0.35)",
        "poster-sm": "0 3px 0 #1c2a52, 0 4px 10px rgba(28,19,10,0.3)",
      },
      fontFamily: {
        "sans": ["'Josefin Sans'", "'Oswald'", "system-ui", "sans-serif"],
        "display": ["'Bebas Neue'", "'Oswald'", "'Arial Narrow'", "sans-serif"],
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
//   --stripe-pattern: repeating-linear-gradient(135deg, #c81d25 0 22px, #f2e6c9 22px 44px);
//   --starburst-gradient: radial-gradient(circle at 50% 0%, rgba(212,160,23,0.35), transparent 55%);
//   --scroll-border: 3px double #1c2a52;
