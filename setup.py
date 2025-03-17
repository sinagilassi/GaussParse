from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

APP_NAME = 'GaussParse'
AUTHOR = 'Sina Gilassi'
VERSION = '1.3.1'
EMAIL = "<sina.gilassi@gmail.com>"
DESCRIPTION = 'GaussParse is a python package to parse Gaussian output files.'
LONG_DESCRIPTION = 'GaussParse is a python package to parse Gaussian output files. for instance, it can read log, txt files and convert them to excel/word files.'

# Setting up
setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    include_package_data=True,
    package_data={'': ['*.txt', '*.xlsx', '*.docx', '*.png', '*.html']},
    license='MIT',
    install_requires=['pandas', 'numpy', 'openpyxl',
                      'xlsxwriter', 'docx', 'matplotlib', 'jinja2', 'rich'],
    keywords=['Python', 'Gaussian Software', 'Computational Chemistry',
              'Gaussian Parser', 'Reaction Energy Profile'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.10',
)
