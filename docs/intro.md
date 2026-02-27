# pychromatic

**A Python library for working with colors, palettes, and publication-quality plots.**

pychromatic provides a clean API for color manipulation, palette management, and
matplotlib integration — making it easy to create beautiful, accessible visualizations.

## Features

- **Color class** — create, brighten, darken, mix, and display colors
- **Palette class** — 22 built-in palettes with container protocol support
- **Colorblind palettes** — Okabe-Ito, Tableau 10, Tol Bright, Tol Muted
- **Colormaps** — generate matplotlib colormaps from any palette
- **Multiplot** — flexible subplot layouts with gridspec control
- **BrokenAxes** — broken axis plots for discontinuous data
- **chromatify** — decorator to auto-style matplotlib subplots

## Quick Start

```python
from pychromatic import Color, Palette

# Work with colors
c = Color("#1976d2")
c.display()

# Use a palette
p = Palette("default")
p.show()
```

## Installation

```bash
pip install pychromatic
```

## Contents

```{tableofcontents}
```
