import pandas as pd

def main():
    print('GaussParse is a python package to parse Gaussian output files.')


def collect_output_files(excel_file, sheet_name="Sheet1"):
    '''
    read all output files from csv file and return a list  

    input:
        excel_file: excel file 
        sheet_name: default "Sheet1"

    output:
        list of output files
    '''
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    output_files = df['output_file'].tolist()
    return output_files


if __name__ == "__main__":
    main()
