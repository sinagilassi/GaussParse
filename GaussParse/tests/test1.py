import GaussParse as gp
print("GaussParse: ")

# app dir
print(gp.app_dir())
# file
gaussian_log = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test\1,2LO.txt"
# save in excel
gp.result_summary_to_excel(gaussian_log)

# folder
gaussian_log_folder = r"D:\OneDrive\Project Analysis\Computational Chemistry\analysis\terpens epoxidation\extract data\aceton-test"
# save in excel
gp.result_summary_to_excel(gaussian_log_folder)
