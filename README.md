# GaussParse

GaussParse is a versatile Python package designed for parsing output files generated by Gaussian software, a widely used computational chemistry tool. This package enables users to efficiently extract essential information and perform various analytical tasks directly from Gaussian output files. Whether you need to visualize energy profiles, analyze IRC (Intrinsic Reaction Coordinate) curves, retrieve summary results, or extract molecular orientations, GaussParse provides a streamlined interface to accomplish these tasks with ease.

Key Features:

* Energy Profile Plotting: Visualize and analyze energy profiles directly from Gaussian  output files.

* IRC Curve Plotting: Generate plots of IRC curves to study reaction pathways.
    
* Summary Results Extraction: Extract and summarize key computational results from Gaussian calculations.
    
* Molecular Orientation Analysis: Retrieve detailed information about molecular orientations and configurations.
    
* Publication-Ready Data: Extract molecular orientation data into a Word file formatted for publication as supplementary information.
    
* GaussParse simplifies the process of post-processing Gaussian output, making it an invaluable tool for computational chemists and researchers working in molecular dynamics, quantum chemistry, and related fields.

## Installation

Install this project

```bash
  pip install GaussParse
```
    
## Documentation

Import GaussParse

```python
import GaussParse as gp
```

Available methods

```python
# *******************************
# collect all files
# *******************************
# excel file
xls_file = r'...\\frustose-TS2-data.xlsx'
gp.collect_files_from(xls_file, sheet_name="Sheet1")

# *******************************
# Save result summary to Excel
# *******************************
# file
gaussian_log = r"...\1,2LO.txt"
# save in excel
gp.result_summary_to_excel(gaussian_log)

# *******************************
# Save input orientation to txt
# *******************************
# file
gaussian_log = r"...\\acetone-limonene-mechanism-1"
# save in txt
gp.input_orientation_to_txt(gaussian_log)

# *******************************
# Transform input orientation to xyz
# *******************************
# file
gaussian_log = r"...\g09_exp.log"
# save in txt
gp.txt_orientation_to_xyz(gaussian_log)

# *******************************
# Save energy profile
# *******************************
# file path
plt_data = '...\\energy.xlsx'
# plot energy profile and save it
gp.plot_energy_profile(plt_data)

# *******************************
# Save IRC profile
# *******************************
# file path
plt_data = "...\\fructose-irc-data"
# save IRC profile
gp.plot_irc_profile(plt_data)

```

![Alt text](https://drive.google.com/uc?export=view&id=19fc5TJiB8fjIXTyh9hukdA2mNR-lgAXa)



## License

[MIT](https://choosealicense.com/licenses/mit/)


## FAQ

For any question, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/) 


## Authors

- [@sinagilassi](https://www.github.com/sinagilassi)

