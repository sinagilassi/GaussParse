# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path
import os
import sys

# worked
# sys.path.insert(0, os.path.abspath('../../../GaussParse/'))
# sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../GaussParse/'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GaussParse'
copyright = '2024, Sina Gilassi'
author = 'Sina Gilassi'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode',
#               'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.ifconfig']

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode',
              'sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

# index
# master_doc = 'GaussParse'
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
