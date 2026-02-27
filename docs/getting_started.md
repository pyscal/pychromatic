# Getting Started

## Installation

Install pychromatic from PyPI:

```bash
pip install pychromatic
```

Or install the development version:

```bash
pip install git+https://github.com/pyscal/pychromatic.git
```

## Requirements

- Python >= 3.10
- matplotlib
- numpy
- rich
- cycler

## Basic Usage

```python
from pychromatic import Color, Palette

# Create a color
c = Color("#d32f2f")
c.display()

# Load a palette
p = Palette("rainbow")
p.show()

# Brighten a color
lighter = c.brighten(0.3)
lighter.display()

# Mix two colors
mixed = c.mix(Color("#1976d2"), ratio=0.5)
mixed.display()
```

See the [Examples](examples/colors.ipynb) section for comprehensive usage guides.
