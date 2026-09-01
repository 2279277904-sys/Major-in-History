#!/usr/bin/env python
"""Executable Python entry point used by process-image.ps1."""

from image_processing.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
