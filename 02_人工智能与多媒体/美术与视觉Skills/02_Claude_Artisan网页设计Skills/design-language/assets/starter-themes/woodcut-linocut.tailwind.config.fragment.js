// Woodcut / Linocut — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#f2e8d3",
        "surface": "#f8f1e0",
        "surface-2": "#e9dcbc",
        "text": "#1c1712",
        "text-muted": "#5a4a35",
        "primary": "#1c1712",
        "accent": "#a4271f",
        "cream": "#f2e8d3",
        "carve-line": "#241d16",
      },
      borderRadius: {
        "sm": "0px",
        "md": "2px",
        "lg": "4px",
        "pill": "999px",
      },
      boxShadow: {
        "print": "6px 6px 0 rgba(28,23,18,0.9)",
        "print-sm": "3px 3px 0 rgba(28,23,18,0.9)",
      },
      fontFamily: {
        "sans": ["'Space Grotesk'", "'Helvetica Neue'", "system-ui", "sans-serif"],
        "display": ["'Bebas Neue'", "'Anton'", "'Arial Black'", "sans-serif"],
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
        "standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --gouge-texture: repeating-linear-gradient(35deg, rgba(28,23,18,0.10) 0px, rgba(28,23,18,0.10) 2px, transparent 2px, transparent 7px);
//   --ink-border: 3px solid #1c1712;
