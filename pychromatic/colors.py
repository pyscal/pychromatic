"""
Module containing color palettes
"""

# default colors
red = "#d32f2f"
pink = "#c2185b"
purple = "#7b1fa2"
blue = "#1976d2"
lightblue = "#0288d1"
cyan = "#0097a7"
teal = "#00796b"
green = "#388e3c"
lightgreen = "#689f38"
lime = "#afb42b"
yellow = "#fbc02d"
orange = "#f57c00"
brown = "#5d4037"
grey = "#616161"
bluegrey = "#455a64"
darkgrey = "#263238"
# color paletts -as dicts
color_palettes = {
    "default": {
        "colors": [
            blue,
            red,
            green,
            orange,
            purple,
            bluegrey,
            lightblue,
            pink,
            lightgreen,
            yellow,
            teal,
            grey,
            brown,
            lime,
            cyan,
        ],
        "names": [
            "blue",
            "red",
            "green",
            "orange",
            "purple",
            "bluegrey",
            "lightblue",
            "pink",
            "lightgreen",
            "yellow",
            "teal",
            "grey",
            "brown",
            "lime",
            "cyan",
        ],
        "type": "qualitative",
    },
    "pastels": {
        "colors": [
            "#8dd3c7",
            "#ffffb3",
            "#bebada",
            "#fb8072",
            "#80b1d3",
            "#fdb462",
            "#b3de69",
            "#fccde5",
            "#d9d9d9",
            "#bc80bd",
            "#ccebc5",
            "#ffed6f",
        ],
        "names": [
            "color1",
            "color2",
            "color3",
            "color4",
            "color5",
            "color6",
            "color7",
            "color8",
            "color9",
            "color10",
            "color11",
            "color12",
        ],
        "type": "qualitative",
    },
    "basics": {
        "colors": [
            "#e41a1c",
            "#377eb8",
            "#4daf4a",
            "#984ea3",
            "#ff7f00",
            "#ffff33",
            "#a65628",
            "#f781bf",
            "#999999",
        ],
        "names": [
            "color1",
            "color2",
            "color3",
            "color4",
            "color5",
            "color6",
            "color7",
            "color8",
            "color9",
        ],
        "type": "qualitative",
    },
    "set1_dark": {
        "colors": [
            "#1b9e77",
            "#d95f02",
            "#7570b3",
            "#e7298a",
            "#66a61e",
            "#e6ab02",
            "#a6761d",
            "#666666",
        ],
        "names": [
            "color1",
            "color2",
            "color3",
            "color4",
            "color5",
            "color6",
            "color7",
            "color8",
        ],
        "type": "qualitative",
    },
    "set1_pastel": {
        "colors": [
            "#66c2a5",
            "#fc8d62",
            "#8da0cb",
            "#e78ac3",
            "#a6d854",
            "#ffd92f",
            "#e5c494",
            "#b3b3b3",
        ],
        "names": [
            "color1",
            "color2",
            "color3",
            "color4",
            "color5",
            "color6",
            "color7",
            "color8",
        ],
        "type": "qualitative",
    },
    "excel": {
        "colors": [
            "#5F7CBB",
            "#B1534F",
            "#9DBD5B",
            "#7D60A0",
            "#E8994B",
            "#999999",
            "#67A8C4",
        ],
        "names": ["color1", "color2", "color3", "color4", "color5", "color6", "color7"],
        "type": "qualitative",
    },
    "set2": {
        "colors": ["#d11141", "#00b159", "#00aedb", "#f37735", "#ffc425"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "google": {
        "colors": ["#008744", "#0057e7", "#d62d20", "#ffa700", "#B9B9B9"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "set3": {
        "colors": ["#5fad56", "#f2c14e", "#f78154", "#4d9078", "#b4436c"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "set4": {
        "colors": ["#363537", "#0cce6b", "#dced31", "#ef2d56", "#ed7d3a"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "dark": {
        "colors": ["#007283", "#72013f", "#c76b0d", "#322569", "#124d25"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "earth": {
        "colors": ["#FDBF00", "#514939", "#BD5340", "#90A74F", "#D0B388"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "set5": {
        "colors": ["#F4AB33", "#EC7176", "#C068A8", "#5C63A2", "#1B4E6B"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "sequential",
    },
    "rainbow": {
        "colors": ["#015486", "#00B5D0", "#6EC626", "#FFBE00", "#FD5D47"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "sequential",
    },
    "set6": {
        "colors": ["#435772", "#2DA4A8", "#FD9C3C", "#FD6041", "#CF2257"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "set7": {
        "colors": ["#4597A3", "#D6765D", "#99CFAB", "#F0CB73", "#7B7E7E"],
        "names": ["color1", "color2", "color3", "color4", "color5"],
        "type": "qualitative",
    },
    "accent": {
        "colors": [
            "#d7191c",
            "#fdae61",
            "#abdda4",
            "#2b83ba",
            "#455A64",
            "#C62828",
            "#FFA000",
            "#008F68",
            "#006899",
            "#424242",
            "#e58080",
            "#ffc766",
            "#85e085",
            "#66cfff",
            "#b3b3b3",
        ],
        "names": [
            "lred",
            "lyellow",
            "lgreen",
            "lblue",
            "lgrey",
            "dred",
            "dyellow",
            "dgreen",
            "dblue",
            "dgrey",
            "pred",
            "pyellow",
            "pgreen",
            "pblue",
            "pgrey",
        ],
        "type": "qualitative",
    },
    # ── Colorblind-friendly palettes ──────────────────────────────────
    "okabe_ito": {
        "colors": [
            "#E69F00",
            "#56B4E9",
            "#009E73",
            "#F0E442",
            "#0072B2",
            "#D55E00",
            "#CC79A7",
            "#000000",
        ],
        "names": [
            "orange",
            "sky",
            "green",
            "yellow",
            "blue",
            "vermilion",
            "purple",
            "black",
        ],
        "type": "qualitative",
    },
    "tableau10": {
        "colors": [
            "#4E79A7",
            "#F28E2B",
            "#E15759",
            "#76B7B2",
            "#59A14F",
            "#EDC948",
            "#B07AA1",
            "#FF9DA7",
            "#9C755F",
            "#BAB0AC",
        ],
        "names": [
            "blue",
            "orange",
            "red",
            "teal",
            "green",
            "yellow",
            "purple",
            "pink",
            "brown",
            "grey",
        ],
        "type": "qualitative",
    },
    "tol_bright": {
        "colors": [
            "#4477AA",
            "#EE6677",
            "#228833",
            "#CCBB44",
            "#66CCEE",
            "#AA3377",
            "#BBBBBB",
        ],
        "names": ["blue", "pink", "green", "yellow", "cyan", "purple", "grey"],
        "type": "qualitative",
    },
    "tol_muted": {
        "colors": [
            "#332288",
            "#88CCEE",
            "#44AA99",
            "#117733",
            "#999933",
            "#DDCC77",
            "#CC6677",
            "#882255",
            "#AA4499",
        ],
        "names": [
            "indigo",
            "sky",
            "teal",
            "green",
            "olive",
            "sand",
            "rose",
            "wine",
            "violet",
        ],
        "type": "qualitative",
    },
}

accent = {
    "lred": "#d7191c",
    "lyellow": "#fdae61",
    "lgreen": "#abdda4",
    "lblue": "#2b83ba",
    "lgrey": "#455A64",
    "dred": "#C62828",
    "dyellow": "#FFA000",
    "dgreen": "#008F68",
    "dblue": "#006899",
    "dgrey": "#424242",
    "pred": "#e58080",
    "pyellow": "#ffc766",
    "pgreen": "#85e085",
    "pblue": "#66cfff",
    "pgrey": "#b3b3b3",
}

chromate = {
    "dark": {
        "red": "#C62828",
        "yellow": "#FFA000",
        "green": "#008F68",
        "blue": "#006899",
        "grey": "#424242",
    },
    "light": {
        "red": "#d7191c",
        "yellow": "#fdae61",
        "green": "#abdda4",
        "blue": "#2b83ba",
        "grey": "#455A64",
    },
    "pastel": {
        "red": "#e58080",
        "yellow": "#ffc766",
        "green": "#85e085",
        "blue": "#66cfff",
        "grey": "#b3b3b3",
    },
}

# ── Colorblind-friendly standalone dicts (importable) ──────────────

okabe_ito = {
    "orange": "#E69F00",
    "sky": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermilion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
}

tableau10 = {
    "blue": "#4E79A7",
    "orange": "#F28E2B",
    "red": "#E15759",
    "teal": "#76B7B2",
    "green": "#59A14F",
    "yellow": "#EDC948",
    "purple": "#B07AA1",
    "pink": "#FF9DA7",
    "brown": "#9C755F",
    "grey": "#BAB0AC",
}

tol_bright = {
    "blue": "#4477AA",
    "pink": "#EE6677",
    "green": "#228833",
    "yellow": "#CCBB44",
    "cyan": "#66CCEE",
    "purple": "#AA3377",
    "grey": "#BBBBBB",
}

tol_muted = {
    "indigo": "#332288",
    "sky": "#88CCEE",
    "teal": "#44AA99",
    "green": "#117733",
    "olive": "#999933",
    "sand": "#DDCC77",
    "rose": "#CC6677",
    "wine": "#882255",
    "violet": "#AA4499",
}
