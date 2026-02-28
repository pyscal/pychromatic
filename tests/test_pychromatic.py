"""Tests for the pychromatic package."""

from __future__ import annotations

import matplotlib
import pytest

import pychromatic.colors as colors
from pychromatic.colorclass import Color
from pychromatic.cutils import (
    brighten,
    create_colormap,
    find_intermediate_colors,
    get_color,
    hex_to_rgb,
    hls_to_rgb,
    mix_colors,
    palette_cmap,
    rgb_to_hex,
    rgb_to_hls,
)
from pychromatic.palette import Palette

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
    @pytest.mark.parametrize(
        "hexval", ["#ff5722", "#1976d2", "#388e3c", "#000000", "#ffffff"]
    )
    def test_hex_rgb_roundtrip(self, hexval):
        rgb = hex_to_rgb(hexval)
        assert rgb_to_hex(rgb) == hexval

    @pytest.mark.parametrize("hexval", ["#ff5722", "#1976d2", "#388e3c"])
    def test_rgb_hls_roundtrip(self, hexval):
        rgb = hex_to_rgb(hexval)
        hls = rgb_to_hls(rgb)
        rgb_back = hls_to_rgb(hls)
        # Allow small rounding error
        for a, b in zip(rgb, rgb_back, strict=True):
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
        result = find_intermediate_colors(
            "#ff0000", "#0000ff", colors=3, ignore_edges=True
        )
        assert len(result) == 3

    def test_includes_edges(self):
        result = find_intermediate_colors(
            "#ff0000", "#0000ff", colors=3, ignore_edges=False
        )
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
            assert c.startswith(
                "#"
            ), f"Color '{c}' in palette '{palette_name}' is not hex"
            assert (
                len(c) == 7
            ), f"Color '{c}' in palette '{palette_name}' is not 7-char hex"


# ---------------------------------------------------------------------------
# Colorblind-friendly palette tests
# ---------------------------------------------------------------------------


class TestColorblindPalettes:
    """Validate the four colorblind-friendly palettes."""

    @pytest.mark.parametrize(
        "palette_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"]
    )
    def test_present_in_color_palettes(self, palette_name):
        assert palette_name in colors.color_palettes

    @pytest.mark.parametrize(
        "palette_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"]
    )
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

    @pytest.mark.parametrize(
        "dict_name,expected_len",
        [
            ("okabe_ito", 8),
            ("tableau10", 10),
            ("tol_bright", 7),
            ("tol_muted", 9),
        ],
    )
    def test_standalone_dict_matches_palette(self, dict_name, expected_len):
        standalone = getattr(colors, dict_name)
        palette_entry = colors.color_palettes[dict_name]
        assert len(standalone) == expected_len
        # All hex values in standalone should appear in the palette colors list
        for hexval in standalone.values():
            assert hexval in palette_entry["colors"]

    @pytest.mark.parametrize(
        "dict_name", ["okabe_ito", "tableau10", "tol_bright", "tol_muted"]
    )
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
            columns=2,
            rows=1,
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
            xlabel="X",
            ylabel="Y",
            title="Test",
            xlim=(0, 10),
            ylim=(-1, 1),
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


# ---------------------------------------------------------------------------
# Color __eq__ / __hash__ / __iter__ tests
# ---------------------------------------------------------------------------


class TestColorEquality:
    def test_equal_colors(self):
        c1 = Color("#ff5722", name="orange")
        c2 = Color("#ff5722", name="different_name")
        assert c1 == c2

    def test_case_insensitive(self):
        c1 = Color("#FF5722")
        c2 = Color("#ff5722")
        assert c1 == c2

    def test_not_equal_different_hex(self):
        c1 = Color("#ff5722")
        c2 = Color("#1976d2")
        assert c1 != c2

    def test_not_equal_to_non_color(self):
        c = Color("#ff5722")
        assert c != "#ff5722"
        assert c != 42

    def test_hash_equal_colors(self):
        c1 = Color("#ff5722")
        c2 = Color("#ff5722")
        assert hash(c1) == hash(c2)

    def test_hashable_in_set(self):
        c1 = Color("#ff5722")
        c2 = Color("#ff5722")
        c3 = Color("#1976d2")
        s = {c1, c2, c3}
        assert len(s) == 2

    def test_hashable_as_dict_key(self):
        c = Color("#ff5722")
        d = {c: "test"}
        assert d[Color("#ff5722")] == "test"


class TestColorIter:
    def test_unpack_rgb(self):
        c = Color("#ff0000")
        r, g, b = c
        assert r == 255
        assert g == 0
        assert b == 0

    def test_list_conversion(self):
        c = Color("#1976d2")
        assert list(c) == [25, 118, 210]

    def test_tuple_conversion(self):
        c = Color("#000000")
        assert tuple(c) == (0, 0, 0)


# ---------------------------------------------------------------------------
# Color input validation tests
# ---------------------------------------------------------------------------


class TestColorValidation:
    def test_invalid_no_hash(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            Color("ff5722")

    def test_invalid_short(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            Color("#fff")

    def test_invalid_chars(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            Color("#gggggg")

    def test_invalid_empty(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            Color("")

    def test_valid_lowercase(self):
        c = Color("#abcdef")
        assert c.hex == "#abcdef"

    def test_valid_uppercase(self):
        c = Color("#ABCDEF")
        assert c.hex == "#ABCDEF"


# ---------------------------------------------------------------------------
# Palette __len__ / __iter__ / __getitem__ tests
# ---------------------------------------------------------------------------


class TestPaletteContainer:
    def test_len(self):
        p = Palette("set2")
        assert len(p) == 5

    def test_len_default(self):
        p = Palette()
        assert len(p) == 15

    def test_iter(self):
        p = Palette("set2")
        items = list(p)
        assert len(items) == 5
        for item in items:
            assert isinstance(item, Color)

    def test_iter_in_for_loop(self):
        p = Palette("set2")
        hexes = [c.hex for c in p]
        assert len(hexes) == 5
        assert all(h.startswith("#") for h in hexes)

    def test_getitem_int(self):
        p = Palette("set2")
        c = p[0]
        assert isinstance(c, Color)
        assert c.hex == "#d11141"

    def test_getitem_negative_index(self):
        p = Palette("set2")
        c = p[-1]
        assert isinstance(c, Color)

    def test_getitem_str(self):
        p = Palette("default")
        c = p["blue"]
        assert isinstance(c, Color)
        assert c.hex == "#1976d2"

    def test_getitem_str_not_found(self):
        p = Palette("default")
        with pytest.raises(KeyError, match="No color named"):
            p["nonexistent"]

    def test_getitem_invalid_type(self):
        p = Palette()
        with pytest.raises(TypeError):
            p[3.14]

    def test_getitem_out_of_range(self):
        p = Palette("set2")
        with pytest.raises(IndexError):
            p[100]


# ---------------------------------------------------------------------------
# Palette remove_color index-shift fix
# ---------------------------------------------------------------------------


class TestPaletteRemoveColor:
    def test_remove_single(self):
        p = Palette("default")
        initial = len(p)
        p.add_color("#abcdef", name="custom1")
        p.add_color("#fedcba", name="custom2")
        p.remove_color("custom1")
        assert len(p) == initial + 1
        assert not hasattr(p, "custom1")
        assert hasattr(p, "custom2")

    def test_remove_preserves_order(self):
        p = Palette("set2")
        original_hexes = [c.hex for c in p]
        p.add_color("#abcdef", name="extra")
        p.remove_color("extra")
        assert [c.hex for c in p] == original_hexes


# ---------------------------------------------------------------------------
# Brighten can reach black
# ---------------------------------------------------------------------------


class TestBrightenBlack:
    def test_brighten_pure_black(self):
        result = brighten("#000000", fraction=0.5)
        assert result != "#000000", "Brightening black should produce a non-black color"
        assert result.startswith("#")
        assert len(result) == 7

    def test_brighten_black_fraction_1(self):
        result = brighten("#000000", fraction=1.0)
        assert result == "#ffffff"

    def test_darken_black_stays_black(self):
        result = brighten("#000000", fraction=-0.5)
        assert result == "#000000"


# ---------------------------------------------------------------------------
# Palette show() side effects removed
# ---------------------------------------------------------------------------


class TestPaletteNoSideEffects:
    def test_brighten_no_show(self):
        """Palette.brighten() should not call show() automatically."""
        import matplotlib.pyplot as plt

        p = Palette("set2")
        initial_figs = len(plt.get_fignums())
        p.brighten("color1", name="light1")
        # Should not have created any new figure
        assert len(plt.get_fignums()) == initial_figs
        plt.close("all")

    def test_darken_no_show(self):
        import matplotlib.pyplot as plt

        p = Palette("set2")
        initial_figs = len(plt.get_fignums())
        p.darken("color1", name="dark1")
        assert len(plt.get_fignums()) == initial_figs
        plt.close("all")


# ---------------------------------------------------------------------------
# get_color tests
# ---------------------------------------------------------------------------


class TestGetColor:
    def test_basic_viridis(self):
        result = get_color(0.5, "viridis")
        assert isinstance(result, str)
        assert result.startswith("#")
        assert len(result) == 7

    def test_value_zero(self):
        result = get_color(0.0, "viridis")
        assert result.startswith("#")

    def test_value_one(self):
        result = get_color(1.0, "viridis")
        assert result.startswith("#")

    def test_default_cmap(self):
        result = get_color(0.5)
        assert result.startswith("#")

    def test_different_cmaps(self):
        for cmap_name in ["plasma", "inferno", "magma", "coolwarm"]:
            result = get_color(0.5, cmap_name)
            assert result.startswith("#")

    def test_invalid_value_low(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            get_color(-0.1)

    def test_invalid_value_high(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            get_color(1.5)

    def test_endpoints_differ(self):
        low = get_color(0.0, "viridis")
        high = get_color(1.0, "viridis")
        assert low != high


# ---------------------------------------------------------------------------
# palette_cmap tests
# ---------------------------------------------------------------------------


class TestPaletteCmap:
    def test_returns_colormap(self):
        cmap = palette_cmap("rainbow")
        assert isinstance(cmap, matplotlib.colors.LinearSegmentedColormap)

    def test_cmap_callable(self):
        cmap = palette_cmap("set2")
        rgba = cmap(0.5)
        assert len(rgba) == 4
        assert all(0 <= v <= 1 for v in rgba)

    def test_cmap_name(self):
        cmap = palette_cmap("rainbow")
        assert cmap.name == "rainbow"

    def test_invalid_palette(self):
        with pytest.raises(KeyError, match="not found"):
            palette_cmap("nonexistent_xyz")

    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_all_palettes(self, palette_name):
        cmap = palette_cmap(palette_name)
        assert cmap is not None
        # Should be callable and return RGBA
        rgba = cmap(0.5)
        assert len(rgba) == 4


# ---------------------------------------------------------------------------
# chromatify decorator functools.wraps test
# ---------------------------------------------------------------------------


class TestChromatifyWraps:
    def test_preserves_function_name(self):
        from pychromatic.decors import chromatify

        @chromatify
        def my_custom_plot():
            """My docstring."""
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            plt.close(fig)
            return ax

        assert my_custom_plot.__name__ == "my_custom_plot"
        assert my_custom_plot.__doc__ == "My docstring."


# ---------------------------------------------------------------------------
# Palette type field validation
# ---------------------------------------------------------------------------


class TestPaletteTypes:
    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_type_not_empty(self, palette_name):
        palette = colors.color_palettes[palette_name]
        assert palette["type"] != "", f"Palette '{palette_name}' has empty type"

    @pytest.mark.parametrize("palette_name", list(colors.color_palettes.keys()))
    def test_type_is_valid(self, palette_name):
        valid_types = {"qualitative", "sequential", "diverging"}
        palette = colors.color_palettes[palette_name]
        assert (
            palette["type"] in valid_types
        ), f"Palette '{palette_name}' has invalid type '{palette['type']}'"


# ---------------------------------------------------------------------------
# Deprecated dict removal validation
# ---------------------------------------------------------------------------


class TestDeadCodeRemoved:
    def test_no_deprecated_dict(self):
        assert not hasattr(colors, "deprecated")

    def test_accent_dict_still_exists(self):
        assert hasattr(colors, "accent")

    def test_no_other_stuff_in_default(self):
        assert "other_stuff" not in colors.color_palettes["default"]


# ---------------------------------------------------------------------------
# Import tests
# ---------------------------------------------------------------------------


class TestImports:
    def test_get_color_importable(self):
        from pychromatic import get_color

        assert callable(get_color)

    def test_palette_cmap_importable(self):
        from pychromatic import palette_cmap

        assert callable(palette_cmap)


# ---------------------------------------------------------------------------
# Palette lighter / darker tests
# ---------------------------------------------------------------------------


class TestPaletteLighterDarker:
    """Tests for Palette.lighter() and Palette.darker() derivative palettes."""

    def test_lighter_returns_new_palette(self):
        p = Palette("default")
        p_light = p.lighter()
        assert isinstance(p_light, Palette)
        assert p_light is not p

    def test_lighter_preserves_length(self):
        p = Palette("default")
        p_light = p.lighter(0.5)
        assert len(p_light) == len(p)

    def test_lighter_preserves_names(self):
        p = Palette("default")
        p_light = p.lighter(0.4)
        original_names = [c.name for c in p]
        lighter_names = [c.name for c in p_light]
        assert original_names == lighter_names

    def test_lighter_colors_are_brighter(self):
        """Lighter palette should have higher luminance for each color."""
        p = Palette("default")
        p_light = p.lighter(0.5)
        for orig, light in zip(p, p_light):
            orig_hls = rgb_to_hls(hex_to_rgb(orig.hex))
            light_hls = rgb_to_hls(hex_to_rgb(light.hex))
            assert light_hls[1] >= orig_hls[1]

    def test_lighter_does_not_mutate_original(self):
        p = Palette("default")
        original_hexes = [c.hex for c in p]
        _ = p.lighter(0.6)
        assert [c.hex for c in p] == original_hexes

    def test_lighter_palette_name(self):
        p = Palette("default")
        p_light = p.lighter()
        assert p_light._palette == "default_lighter"

    def test_lighter_colors_accessible_by_name(self):
        p = Palette("default")
        p_light = p.lighter(0.3)
        for c in p:
            assert hasattr(p_light, c.name)
            assert getattr(p_light, c.name).hex != c.hex or c.hex == "#ffffff"

    def test_darker_returns_new_palette(self):
        p = Palette("default")
        p_dark = p.darker()
        assert isinstance(p_dark, Palette)
        assert p_dark is not p

    def test_darker_preserves_length(self):
        p = Palette("default")
        p_dark = p.darker(0.3)
        assert len(p_dark) == len(p)

    def test_darker_colors_are_darker(self):
        """Darker palette should have lower luminance for each color."""
        p = Palette("default")
        p_dark = p.darker(0.3)
        for orig, dark in zip(p, p_dark):
            orig_hls = rgb_to_hls(hex_to_rgb(orig.hex))
            dark_hls = rgb_to_hls(hex_to_rgb(dark.hex))
            assert dark_hls[1] <= orig_hls[1]

    def test_darker_does_not_mutate_original(self):
        p = Palette("default")
        original_hexes = [c.hex for c in p]
        _ = p.darker(0.3)
        assert [c.hex for c in p] == original_hexes

    def test_lighter_different_fractions(self):
        p = Palette("default")
        p1 = p.lighter(0.2)
        p2 = p.lighter(0.8)
        # Higher fraction should give brighter colors
        for c1, c2 in zip(p1, p2):
            hls1 = rgb_to_hls(hex_to_rgb(c1.hex))
            hls2 = rgb_to_hls(hex_to_rgb(c2.hex))
            assert hls2[1] >= hls1[1]

    def test_lighter_iterable(self):
        """Lighter palette should be iterable and zip-able with original."""
        p = Palette("default")
        p_light = p.lighter(0.5)
        pairs = list(zip(p, p_light))
        assert len(pairs) == len(p)

    def test_lighter_with_different_palettes(self):
        for name in ("pastels", "dark", "earth"):
            p = Palette(name)
            p_light = p.lighter(0.4)
            assert len(p_light) == len(p)
            assert p_light._palette == f"{name}_lighter"

    def test_darker_palette_name(self):
        p = Palette("earth")
        p_dark = p.darker(0.3)
        assert p_dark._palette == "earth_lighter"  # internally uses lighter(-frac)

    def test_chained_lighter(self):
        """Should be able to chain: p.lighter().lighter()."""
        p = Palette("default")
        p_ll = p.lighter(0.3).lighter(0.3)
        assert len(p_ll) == len(p)
        # Double-lightened should be brighter than single
        p_l = p.lighter(0.3)
        for single, double in zip(p_l, p_ll):
            hls_s = rgb_to_hls(hex_to_rgb(single.hex))
            hls_d = rgb_to_hls(hex_to_rgb(double.hex))
            assert hls_d[1] >= hls_s[1]
