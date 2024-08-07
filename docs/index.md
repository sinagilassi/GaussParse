# Welcome to GaussParse's documentation!

GaussParse is a versatile Python package designed for parsing output files generated by Gaussian software, a widely used computational chemistry tool. This package enables users to efficiently extract essential information and perform various analytical tasks directly from Gaussian output files. Whether you need to visualize energy profiles, analyze IRC (Intrinsic Reaction Coordinate) curves, retrieve summary results, or extract molecular orientations, GaussParse provides a streamlined interface to accomplish these tasks with ease.


Key Features:


- Energy Profile Plotting: Visualize and analyze energy profiles directly from Gaussian  output files.
- IRC Curve Plotting: Generate plots of IRC curves to study reaction pathways.
- Summary Results Extraction: Extract and summarize key computational results from Gaussian calculations.
- Molecular Orientation Analysis: Retrieve detailed information about molecular orientations and configurations.
- Publication-Ready Data: Extract molecular orientation data into a Word file formatted for publication as supplementary information.
- GaussParse simplifies the process of post-processing Gaussian output, making it an invaluable tool for computational chemists and researchers working in molecular dynamics, quantum chemistry, and related fields.

## Installation

To install GaussParse, run the following command in your terminal:

```bash
pip install GaussParse
```
## Usage
To use GaussParse, simply import the package into your Python script or Jupyter notebook and start using
it.

```python
import GaussParse as gp

# version
print(f"GaussParse version: {gp.__version__}")
```

## Contributing
If you would like to contribute to GaussParse, please feel free to submit a pull request or open
an issue.

<!-- ## Modules

::: GaussParse.app -->