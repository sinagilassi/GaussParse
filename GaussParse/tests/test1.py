import GaussParse as gp
print("GaussParse: ")

# app dir
print(gp.app_dir())

# *******************************
# Save result summary to Excel
# *******************************
# file
# gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test\1,2LO.txt"
# save in excel
# gp.result_summary_to_excel(gaussian_log)

# folder
# gaussian_log_folder = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test"
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
gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\models\terpens epoxidation\limonene-dmdo\mechanism 1\step 1\qst3\solvent\res 2\lg bs\res 1\g09_exp.log"
# save in txt
gp.input_orientation_to_txt(gaussian_log)
