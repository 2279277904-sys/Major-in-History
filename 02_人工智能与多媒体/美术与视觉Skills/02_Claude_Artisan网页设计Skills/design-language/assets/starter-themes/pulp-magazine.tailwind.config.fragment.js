// Pulp Magazine Cover Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#1a1210",
        "surface": "#241a17",
        "surface-2": "#33231e",
        "text": "#f5e6d3",
        "text-muted": "#c9ad8f",
        "primary": "#d4361f",
        "accent": "#f2b705",
        "pulp-blue": "#1c4f8c",
        "shadow-ink": "#0c0806",
      },
      borderRadius: {
        "sm": "2px",
        "md": "4px",
        "lg": "10px",
        "pill": "999px",
      },
      boxShadow: {
        "lurid": "6px 6px 0 #0c0806",
        "lurid-sm": "3px 3px 0 #0c0806",
      },
      fontFamily: {
        "sans": ["'PT Sans'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Anton'", "'Oswald'", "'Arial Black'", "sans-serif"],
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
        "standard": "cubic-bezier(0.5, 0, 0.15, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --painted-vignette: radial-gradient(120% 90% at 50% 20%, rgba(212,54,31,0.22), transparent 60%), radial-gradient(140% 100% at 50% 100%, rgba(0,0,0,0.55), transparent 55%);
//   --masthead-shadow: 4px 4px 0 #0c0806, 8px 8px 0 rgba(0,0,0,0.25);
//   --bg-image: linear-gradient(180deg, #241a17 0%, #1a1210 60%, #0c0806 100%);
