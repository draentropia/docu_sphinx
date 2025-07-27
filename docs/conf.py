# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from sphinxawesome_theme.postprocess import Icons  # pylint: disable=import-error

project = "Docs Sphinx"
author = 'E. Ortega'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinx_mdinclude",  # allows the mdinclude directive to add Markdown files
    "sphinx.ext.napoleon",  # converts Google docstrings into rst
    "sphinx_automodapi.automodapi",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = [".rst", ".pynb"]
pygments_style = "default"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_preprocess_types = True

automodapi_toctreedirnm = "code/api"  # location where the automodapi rst files are builti

autoclass_content = "class"  # only show class docstrings (hide init docstrings)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
#html_permalinks_icon = Icons.permalinks_icon
html_favicon = "_static/q_light.jpeg"
html_theme = "sphinxawesome_theme"
html_theme_options = {
    "logo_light": "_static/gamepad.png",
    "logo_dark": "_static/game.png",
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_copy_source = False
html_show_sourcelink = False

from inspect import getsourcefile
import os

# Get path to directory containing this file, conf.py.
DOCS_DIRECTORY = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

def ensure_pandoc_installed(_):
    import pypandoc

    # Download pandoc if necessary. If pandoc is already installed and on
    # the PATH, the installed version will be used. Otherwise, we will
    # download a copy of pandoc into docs/bin/ and add that to our PATH.
    pandoc_dir = os.path.join(DOCS_DIRECTORY, "bin")
    # Add dir containing pandoc binary to the PATH environment variable
    if pandoc_dir not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + pandoc_dir
    pypandoc.ensure_pandoc_installed(
        quiet=True,
        targetfolder=pandoc_dir,
        delete_installer=True,
    )


def setup(app):
    app.connect("builder-inited", ensure_pandoc_installed)
