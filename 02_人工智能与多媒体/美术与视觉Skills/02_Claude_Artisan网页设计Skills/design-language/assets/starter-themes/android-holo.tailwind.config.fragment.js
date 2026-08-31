// Android Holo — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#000000",
        "surface": "#0c0f10",
        "surface-2": "#171b1c",
        "text": "#e8f7fa",
        "text-muted": "#8a9a9d",
        "primary": "#33b5e5",
        "primary-bright": "#8fdce8",
        "divider": "#2a2f30",
        "danger": "#ff4444",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "2px",
        "pill": "999px",
      },
      boxShadow: {
        "glow": "0 0 8px rgba(51,181,229,0.55), 0 0 1px rgba(51,181,229,0.9)",
        "glow-strong": "0 0 16px rgba(51,181,229,0.75), 0 0 2px rgba(143,220,232,0.9)",
      },
      fontFamily: {
        "sans": ["'Roboto Condensed'", "'Droid Sans'", "'Helvetica Neue'", "Arial", "sans-serif"],
        "display": ["'Roboto Condensed'", "'Droid Sans'", "sans-serif"],
        "mono": ["'Droid Sans Mono'", "ui-monospace", "monospace"],
      },
      fontSize: {
        "xs": "0.6875rem",
        "sm": "0.8125rem",
        "base": "0.9375rem",
        "lg": "1.0625rem",
        "xl": "1.25rem",
        "2xl": "1.5rem",
        "3xl": "2rem",
        "4xl": "2.75rem",
        "5xl": "3.5rem",
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
        "standard": "linear",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --holo-underline: linear-gradient(90deg, transparent, #33b5e5, transparent);
//   --bg-image: none;
