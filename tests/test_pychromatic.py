"""Tests for the pychromatic package."""
from __future__ import annotations

import pytest

from pychromatic.colorclass import Color
from pychromatic.cutils import (
    brighten,
    create_colormap,
    find_intermediate_colors,
    hex_to_rgb,
    hls_to_rgb,
    mix_colors,
    rgb_to_hex,
    rgb_to_hls,
)
from pychromatic.palette import Palette
import pychromatic.colors as colors


# ---------------------------------------------------------------------------
# cutils — color conversion tests
# ---------------------------------------------------------------------------

class TestHexToRgb:
    def test_basic(self):
        assert hex_to_rgb("#ff0000") == [255, 0, 0]

    def test_black(self):
        assert hex_to_rgb("#000000") == [0, 0, 0]

    def test_white(self):
        assert hex_to_rgb("#ffffff") == [255, 255, 255]

    def test_arbitrary(self):
        assert hex_to_rgb("#1976d2") == [25, 118, 210]

    def test_without_hash(self):
        assert hex_to_rgb("ff5722") == [255, 87, 34]


class TestRgbToHex:
    def test_basic(self):
        assert rgb_to_hex([255, 0, 0]) == "#ff0000"

    def test_float_input(self):
        assert rgb_to_hex([1.0, 0.0, 0.0]) == "#ff0000"

    def test_black(self):
        assert rgb_to_hex([0, 0, 0]) == "#000000"

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            rgb_to_hex([300, 0, 0])


class TestRoundTripConversions:
    @pytest.mark.parametrize("hexval", ["#ff5722", "#1976d2", "#388e3c", "#000000", "#ffffff"])
    def test_hex_rgb_roundtrip(self, hexval):
        rgb = hex_to_rgb(hexval)
        assert rgb_to_hex(rgb) == hexval

    @pytest.mark.parametrize("hexval", ["#ff5722", "#1976d2", "#388e3c"])
    def test_rgb_hls_roundtrip(self, hexval):
        rgb = hex_to_rgb(hexval)
        hls = rgb_to_hls(rgb)
        rgb_back = hls_to_rgb(hls)
        # Allow small rounding error
        for a, b in zip(rgb, rgb_back):
            assert abs(a - b) <= 1


class TestBrighten:
    def test_brighten_returns_hex(self):
        result = brighten("#1976d2", fraction=0.1)
        assert result.startswith("#")
        assert len(result) == 7

    def test_darken_returns_hex(self):
        result = brighten("#1976d2", fraction=-0.1)
        assert result.startswith("#")

    def test_brighten_increases_luminance(self):
        original_hls = rgb_to_hls(hex_to_rgb("#1976d2"))
        brightened_hls = rgb_to_hls(hex_to_rgb(brighten("#1976d2", fraction=0.2)))
        assert brightened_hls[1] >= original_hls[1]


class TestMixColors:
    def test_equal_mix(self):
        result = mix_colors("#ff0000", "#0000ff", ratio=0.5)
        assert isinstance(result, str)
        assert result.startswith("#")

    def test_full_ratio_returns_first(self):
        result = mix_colors("#ff0000", "#0000ff", ratio=1.0)
        assert result == "#ff0000"

    def test_zero_ratio_returns_second(self):
        result = mix_colors("#ff0000", "#0000ff", ratio=0.0)
        assert result == "#0000ff"


class TestFindIntermediateColors:
    def test_returns_correct_count(self):
        result = find_intermediate_colors("#ff0000", "#0000ff", colors=3, ignore_edges=True)
        assert len(result) == 3

    def test_includes_edges(self):
        result = find_intermediate_colors("#ff0000", "#0000ff", colors=3, ignore_edges=False)
        assert len(result) == 5  # 3 intermediates + 2 edges

    def test_all_valid_hex(self):
        result = find_intermediate_colors("#ff0000", "#0000ff", colors=5)
        for c in result:
            assert c.startswith("#")
            assert len(c) == 7


class TestCreateColormap:
    def test_basic(self):
        cmap = create_colormap(["#ff0000", "#0000ff"])
        assert cmap is not None

    def test_too_few_colors_raises(self):
        with pytest.raises(ValueError):
            create_colormap(["#ff0000"])


# ---------------------------------------------------------------------------
# Color class tests
# ---------------------------------------------------------------------------

class TestColor:
    def test_construction(self):
        c = Color("#ff5722", name="orange")
        assert c.colorstr == "#ff5722"
        assert c.name == "orange"
        assert c.hex == "#ff5722"

    def test_rgb_conversion(self):
        c = Color("#ff0000")
        assert c.rgb == [255, 0, 0]

    def test_repr_is_pure(self):
        c = Color("#ff5722", name="orange")
        r = repr(c)
        assert "Color(" in r
        assert "#ff5722" in r
        assert "orange" in r

    def test_repr_no_name(self):
        c = Color("#ff5722")
        r = repr(c)
        assert "name=" not in r

    def test_brighten(self):
        c = Color("#1976d2", name="blue")
        original_hex = c.hex
        c.brighten(0.1)
        assert c.hex != original_hex
        assert c.name.startswith("light-")

    def test_darken(self):
        c = Color("#1976d2", name="blue")
        original_hex = c.hex
        c.darken(0.1)
        assert c.hex != original_hex
        assert c.name.startswith("dark-")

    def test_reset(self):
        c = Color("#1976d2", name="blue")
        c.brighten(0.5)
        c.reset()
        assert c.hex == "#1976d2"
        assert c.name == "blue"

    def test_mul_returns_new_object(self):
        c = Color("#1976d2", name="blue")
        result = c * 0.5
        assert result is not c
        assert c.hex == "#1976d2"  # original unchanged

    def test_rmul(self):
        c = Color("#1976d2", name="blue")
        result = 0.5 * c
        assert result is not c
        assert c.hex == "#1976d2"

    def test_mix(self):
        c1 = Color("#ff0000", name="red")
        c2 = Color("#0000ff", name="blue")
        c1.mix(c2, ratio=0.5)
        assert c1.hex != "#ff0000"


# ---------------------------------------------------------------------------
# Palette tests
# ---------------------------------------------------------------------------

class TestPalette:
    def test_default_construction(self):
        p = Palette()
        assert p.colors is not None
        assert len(p.colors) > 0

    def test_named_construction(self):
        p = Palette(palette="pastels")
        assert p.colors is not None
        assert len(p.colors) == 12

    def test_invalid_palette_raises(self):
        with pytest.raises(KeyError):
            Palette(palette="nonexistent_palette_xyz")

    def test_repr(self):
        p = Palette()
        r = repr(p)
        assert "Palette(" in r
        assert "default" in r

    def test_palette_setter(self):
        p = Palette()
        p.palette = "set2"
        assert p._palette == "set2"
        assert len(p.colors) == 5

    def test_add_color_str(self):
        p = Palette()
        initial_count = len(p.colors)
        p.add_color("#abcdef", name="custom")
        assert len(p.colors) == initial_count + 1
        assert hasattr(p, "custom")

    def test_add_color_object(self):
        p = Palette()
        initial_count = len(p.colors)
        c = Color("#abcdef", name="custom2")
        p.add_color(c)
        assert len(p.colors) == initial_count + 1

    def test_remove_color(self):
        p = Palette()
        p.add_color("#abcdef", name="custom")
        p.remove_color("custom")
        assert not hasattr(p, "custom")

    def test_reset(self):
        p = Palette()
        original_hex = p.colors[0].hex
        p.colors[0].brighten(0.5)
        p.reset()
        assert p.colors[0].hex == original_hex

    def test_get_cmap(self):
        p = Palette()
        cmap = p.get_cmap()
        assert cmap is not None


# ---------------------------------------------------------------------------
# colors.py data validation
# ---------------------------------------------------------------------------

class TestColorData:
    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_palette_colors_names_match(self, palette_name):
        palette = colors.color_palettes[palette_name]
        assert len(palette["colors"]) == len(palette["names"]), (
            f"Palette '{palette_name}': {len(palette['colors'])} colors but "
            f"{len(palette['names'])} names"
        )

    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_palette_has_type(self, palette_name):
        palette = colors.color_palettes[palette_name]
        assert "type" in palette

    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_all_colors_are_valid_hex(self, palette_name):
        palette = colors.color_palettes[palette_name]
        for c in palette["colors"]:
            assert c.startswith("#"), f"Color '{c}' in palette '{palette_name}' is not hex"
            assert len(c) == 7, f"Color '{c}' in palette '{palette_name}' is not 7-char hex"


# ---------------------------------------------------------------------------
# Colorblind-friendly palette tests
# ---------------------------------------------------------------------------

class TestColorblindPalettes:
    """Validate the four colorblind-friendly palettes."""

    @pytest.mark.parametrize("palette_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"])
    def test_present_in_color_palettes(self, palette_name):
        assert palette_name in colors.color_palettes

    @pytest.mark.parametrize("palette_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"])
    def test_qualitative_type(self, palette_name):
        assert colors.color_palettes[palette_name]["type"] == "qualitative"

    def test_okabe_ito_importable(self):
        from pychromatic import okabe_ito
        assert len(okabe_ito) == 8
        assert "orange" in okabe_ito
        assert okabe_ito["orange"] == "#E69F00"

    def test_tableau10_importable(self):
        from pychromatic import tableau10
        assert len(tableau10) == 10
        assert "teal" in tableau10
        assert tableau10["blue"] == "#4E79A7"

    def test_tol_bright_importable(self):
        from pychromatic import tol_bright
        assert len(tol_bright) == 7
        assert "cyan" in tol_bright
        assert tol_bright["blue"] == "#4477AA"

    def test_tol_muted_importable(self):
        from pychromatic import tol_muted
        assert len(tol_muted) == 9
        assert "teal" in tol_muted
        assert tol_muted["indigo"] == "#332288"

    @pytest.mark.parametrize("dict_name,expected_len", [
        ("okabe_ito", 8), ("tableau10", 10), ("tol_bright", 7), ("tol_muted", 9),
    ])
    def test_standalone_dict_matches_palette(self, dict_name, expected_len):
        standalone = getattr(colors, dict_name)
        palette_entry = colors.color_palettes[dict_name]
        assert len(standalone) == expected_len
        # All hex values in standalone should appear in the palette colors list
        for hexval in standalone.values():
            assert hexval in palette_entry["colors"]

    @pytest.mark.parametrize("dict_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"])
    def test_all_valid_hex(self, dict_name):
        standalone = getattr(colors, dict_name)
        for name, hexval in standalone.items():
            assert hexval.startswith("#"), f"{name}: {hexval}"
            assert len(hexval) == 7, f"{name}: {hexval}"

    def test_palette_object_construction(self):
        """Ensure each colorblind palette works with the Palette class."""
        for name in ["okabe_ito", "tableau10", "tol_bright", "tol_muted"]:
            p = Palette(palette=name)
            assert len(p.colors) > 0


# ---------------------------------------------------------------------------
# decors.py tests
# ---------------------------------------------------------------------------

class TestChromatifyDecorator:
    def test_decorator_wraps_function(self):
        from pychromatic.decors import chromatify

        @chromatify
        def dummy_subplot():
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            plt.close(fig)
            return ax

        # Should run without error
        ax = dummy_subplot()
        assert ax is not None
        import matplotlib.pyplot as plt
        plt.close("all")


# ---------------------------------------------------------------------------
# Multiplot tests
# ---------------------------------------------------------------------------

class TestMultiplot:
    def test_basic_construction(self):
        import matplotlib.pyplot as plt
        from pychromatic import Multiplot
        m = Multiplot(columns=2, rows=2)
        assert m.axes.shape == (2, 2)
        plt.close("all")

    def test_gridspec_kwargs(self):
        """Issue #4: arbitrary gridspec kwargs are forwarded."""
        import matplotlib.pyplot as plt
        from pychromatic import Multiplot
        m = Multiplot(
            columns=2, rows=1,
            gridspec_kwargs={"left": 0.1, "right": 0.9, "bottom": 0.15},
        )
        assert m.axes.shape == (1, 2)
        plt.close("all")

    def test_style_axes(self):
        """Issue #1: convenience axis/tick styling."""
        import matplotlib.pyplot as plt
        from pychromatic import Multiplot
        m = Multiplot(columns=1, rows=1)
        m.style_axes(
            (0, 0),
            xlabel="X", ylabel="Y", title="Test",
            xlim=(0, 10), ylim=(-1, 1),
            hide_spines=["top", "right"],
        )
        ax = m.axes[0, 0]
        assert ax.get_xlabel() == "X"
        assert ax.get_ylabel() == "Y"
        assert ax.get_title() == "Test"
        assert ax.get_xlim() == (0, 10)
        assert not ax.spines["top"].get_visible()
        assert not ax.spines["right"].get_visible()
        plt.close("all")

    def test_add_inset(self):
        """Issue #2: inset axes creation."""
        import matplotlib.pyplot as plt
        from pychromatic import Multiplot
        m = Multiplot(columns=1, rows=1)
        m.add_inset((0, 0), width="30%", height="30%")
        assert len(m.subaxes[0][0]) == 1
        plt.close("all")
