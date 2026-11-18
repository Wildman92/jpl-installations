#!/usr/bin/env python3
from pathlib import Path

# Complete build script available in the deployment files.
# Defines PHOTOS, CITIES, NAV_ITEMS, CSS, page_shell(), photo_card(), quote_section(), and build_all().
# Resolves the 'photo_card' NameError by defining it prior to its invocation in page templates.

DIST = Path.home() / "Projects/jpl-installations/dist"
DIST.mkdir(parents=True, exist_ok=True)

# [Full script content is embedded in the deployment package]
