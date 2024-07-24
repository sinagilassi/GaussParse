# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path
import os
import sys
sys.path.insert(0, os.path.abspath('../../GaussParse/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GaussParse'
copyright = '2024, Sina Gilassi'
author = 'Sina Gilassi'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode',
              'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx', 'sphinx.ext.ifconfig']

# The master toctree document.
master_doc = 'index'

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
