// ANSI / BBS Art — Tailwind theme fragment (generated).
// Merge into tailwind.config.js under theme.extend.
module.exports = {
  theme: {
    extend: {
      colors: {
        "bg": "#000000",
        "surface": "#0a0a0a",
        "surface-2": "#1c1c1c",
        "text": "#c0c0c0",
        "text-muted": "#808080",
        "primary": "#ff5555",
        "accent": "#55ffff",
        "yellow": "#ffff55",
        "green": "#55ff55",
        "magenta": "#ff55ff",
        "blue": "#5555ff",
        "white": "#ffffff",
        "red-dark": "#aa0000",
      },
      borderRadius: {
        "sm": "0px",
        "md": "0px",
        "lg": "0px",
        "pill": "0px",
      },
      boxShadow: {
        "none": "none",
      },
      fontFamily: {
        "sans": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
        "display": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
        "mono": ["'Perfect DOS VGA 437'", "'Courier New'", "monospace"],
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
        "5xl": "3.75rem",
      },
      spacing: {
        "1": "1ch",
        "2": "2ch",
        "3": "3ch",
        "4": "4ch",
        "6": "6ch",
        "8": "8ch",
        "12": "12ch",
        "16": "16ch",
        "24": "24ch",
      },
      transitionTimingFunction: {
        "standard": "steps(1, end)",
      },
    },
  },
};

// Signature `extra` tokens are CSS-only (gradients/filters/composite
// borders). Add them as CSS custom properties or arbitrary values:
//   --box-double: 3px double #55ffff;
//   --shade-block: repeating-linear-gradient(45deg, currentColor 0 1px, transparent 1px 3px);
//   --bg-image: none;
