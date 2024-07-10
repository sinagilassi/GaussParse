from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

APP_NAME = 'GaussParse'
VERSION = '1.0.0'
DESCRIPTION = 'GaussParse is a python package to parse Gaussian output files.'
LONG_DESCRIPTION = 'GaussParse is a python package to parse Gaussian output files. for instance, it can read log, txt files and convert them to excel/word files.'

# Setting up
setup(
    name=APP_NAME,
    version=VERSION,
    author="Sina Gilassi",
    author_email="<sina.gilassi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    license='MIT',
    install_requires=['pandas', 'numpy', 'openpyxl', 'xlsxwriter', 'docx'],
    keywords=['python', 'Gaussian Software', 'Computational Chemistry'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
