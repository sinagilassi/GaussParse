import GaussParse as gp
# print("GaussParse: ")

# version
print(f"current version: {gp.__version__}")
# info
gp.app_info()

# *******************************
# collect all files
# *******************************
# excel file
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\frustose-TS2-data.xlsx'
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1-b3lyp.xlsx'
# xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-cis-3-Hexene-mechanism-1.xlsx'

xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-2-B3LYP-6-311-g(3df-2p).xlsx'
# log files
# gp.collect_files_from(xls_file, sheet_name="Sheet1")
# txt files
# gp.collect_files_from(xls_file, sheet_name="Sheet2")

# *******************************
# Save result summary to Excel
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test\1,2LO.txt"
# save in excel
# res, dfs = gp.result_summary_to_excel(gaussian_log)
# print(res)
# print(dfs, type(dfs))

# folder
# gaussian_log_folder = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test"
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-TS2-data'
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-cis-3-Hexene-mechanism-1'

gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-2-B3LYP-6-311-g(3df-2p)'

# save in excel
gp.result_summary_to_excel(gaussian_log_folder)

# *******************************
# Save input orientation to txt
# *******************************
# file
# gaussian_log = r"D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-1"
# gaussian_log = r"D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\fructose-dioxirane-limonene-mechanism-3"
# gaussian_log = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\frustose-TS2-data'
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo with fructose keton\mechansim 3\step 2\qst3-2\res 1\tight\res 1\g09_exp.log"
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
# plt_data = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-limonene-mechanism-2\\energy.xlsx'
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
# save IRC profile
# manual_options = {
#     "y_unit": "kcal/mol"
# }
# gp.plot_irc_profile(plt_data)
