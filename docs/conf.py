# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Fieldmark"
copyright = "2023, Electronic Field Notebooks PTY LTD"
author = "Electronic Field Notebooks PTY LTD"
release = "0.7.940"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "announcement": "Draft Documentation! This documentation is for a beta version of FAIMS3! Contact info@faims.edu.au with questions.",
}

myst_heading_anchors = 1

extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "attrs_block",
    "amsmath",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
