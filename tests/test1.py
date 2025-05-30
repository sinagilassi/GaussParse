import GaussParse as gp
import os
# print("GaussParse: ")

# version
print(f"current version: {gp.__version__}")
# description
print(f"description: {gp.__description__}")

# *******************************
# collect all files
# *******************************
# excel file
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\frustose-TS2-data.xlsx'
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1-b3lyp.xlsx'
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-cis-3-Hexene-mechanism-1.xlsx'

# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-irc-B3LYP.xlsx'
# b3lyp-d3
xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1-B3LYP-6-311-g(3df-2p)-D3.xlsx'

# log files
# gp.collect_files_from(xls_file, sheet_name="Sheet1")
# txt files
# gp.collect_files_from(xls_file, sheet_name="Sheet2")

# *******************************
# Save result summary to Excel
# *******************************
# NOTE: file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test\1,2LO.txt"
gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test-1\\1,2LO.txt"
# save in excel
# res, dfs = gp.result_summary_to_excel(gaussian_log)
# print(res)
# print(dfs, type(dfs))

# NOTE: folder
# gaussian_log_folder = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test-1"
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-TS2-data'
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-cis-3-Hexene-mechanism-1'

# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-TS comparison-B3LYP'

# save in excel
# output_dir = r"D:\OneDrive\Desktop\res"

gaussian_log_folder = r'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1-B3LYP-6-311-g(3df-2p)-D3'

gp.result_summary_to_excel(gaussian_log_folder)

# *******************************
# Save result summary to dataframe
# *******************************
# dataframe
# df = gp.result_summary_to_dataframe(gaussian_log_folder)
# print(df, type(df))

# to dict
# res = gp.result_summary_to_dict(gaussian_log_folder)
# print(res, type(res))

# *******************************
# Save input orientation to txt
# *******************************
# file
# gaussian_log = r"D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1"
# gaussian_log = r"D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\fructose-dioxirane-limonene-mechanism-3"
# gaussian_log = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\frustose-TS2-data'
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo with fructose keton\mechansim 3\step 2\qst3-2\res 1\tight\res 1\g09_exp.log"

# folder
gaussian_log = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-2-B3LYP-6-311-g(3df-2p)'

# save in txt
# gp.input_orientation_to_txt(gaussian_log)

# *******************************
# Transform input orientation to xyz
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo\mechanism 1\step 1\qst3\solvent\res 2\lg bs\res 1\g09_exp.log"
# gaussian_log = r"D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1\\molecular-orientation_20240617_173242.txt"
# save in txt
# gp.txt_orientation_to_xyz(gaussian_log)

# *******************************
# Save energy profile
# *******************************
# file path
plt_data = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-2-B3LYP-6-311-g(3df-2p)\\energy.xlsx'

# plot energy profile and save it
# gp.plot_energy_profile(plt_data)

# *******************************
# Save IRC profile
# *******************************
# file path
# plt_data = "D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-irc-data\\trans-TS1.log"

# folder path
# plt_data = "D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\irc"
# plt_data = "D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\fructose-irc-data"
plt_data = "D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-irc-B3LYP"

# save IRC profile
# manual_options = {
#     "y_unit": "kcal/mol"
# }

# execute
# gp.plot_irc_profile(plt_data)

# *******************************
# Display NBO file in a browser
# *******************************
# file
nbo_file = r"E:\Python Projects\universal-projects\GaussParse\nbo_res_two_molecules.log"

# display
# gp.nbo_parser(nbo_file)
