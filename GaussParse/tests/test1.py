import GaussParse as gp
print("GaussParse: ")

# app dir
# print(gp.app_dir())

# *******************************
# collect all files
# *******************************
# excel file
xls_file = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\fructose-irc-data.xlsx'
# gp.collect_files_from(xls_file, sheet_name="Sheet1")

# *******************************
# Save result summary to Excel
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test\1,2LO.txt"
# save in excel
# gp.result_summary_to_excel(gaussian_log)

# folder
# gaussian_log_folder = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test"
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\acetone-TS2-data'
# gaussian_log_folder = 'D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\frustose-TS2-data'
# save in excel
# gp.result_summary_to_excel(gaussian_log_folder)

# *******************************
# Save input orientation to txt
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo\mechanism 1\step 1\qst3\solvent\res 2\lg bs\res 1\g09_exp.log"
# save in txt
# gp.input_orientation_to_txt(gaussian_log)

# *******************************
# Transform input orientation to xyz
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo\mechanism 1\step 1\qst3\solvent\res 2\lg bs\res 1\g09_exp.log"
# save in txt
# gp.input_orientation_to_txt(gaussian_log)

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
plt_data = "D:\\OneDrive\\Project Analysis\\Computational Chemistry\\analysis\\terpens epoxidation\\extract data\\fructose-irc-data"
# save IRC profile
# manual_options = {
#     "y_unit": "kcal/mol"
# }
gp.plot_irc_profile(plt_data)
