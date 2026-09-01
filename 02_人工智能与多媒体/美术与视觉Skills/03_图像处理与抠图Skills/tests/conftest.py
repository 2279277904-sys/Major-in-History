from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).parents[1] / "image-processing" / "scripts"
sys.path.insert(0, str(SCRIPTS))
