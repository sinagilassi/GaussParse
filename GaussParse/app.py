# import packages/modules
# external
import os
import pandas as pd
# internal
from GaussParse.docs import SummaryResult, Structure
from GaussParse.config import __version__


def main():
    # version
    print(
        f'GaussParse {__version__} is a python package to parse Gaussian output files.')


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


def test(name):
    print("my name is, ", name)


def result_summary_to_excel(src: str):
    '''
    Convert summary result to excel file

    args:
        src {str}: file | folder
            file format: *.txt
            folder: all *.txt files in the folder

    return:
        excel file - return value is True
    '''
    try:
        SummaryResultClass = SummaryResult(src)
        return SummaryResultClass.toImage()
    except Exception as e:
        print(e)


def input_orientation_to_txt(src: str):
    '''
    Convert input orientation in Gaussian files

    args:
        src {str}: file | folder
            Gaussian file: *.log
            folder: all Gaussian *.log files in the folder

    return:
        txt file {str} - return value is True
    '''
    try:
        StructureClass = Structure(src)
        return StructureClass.toTxt()
    except Exception as e:
        print(e)


def toXYZ(src: str):
    '''
    load an input orientation file and then transform it to xyz format

    args:
        src {str}: file | folder
            Gaussian file: *.log
            folder: all Gaussian *.log files in the folder

    return:
        xyz file {str} - return value is True
    '''
    try:
        StructureClass = Structure(src)
        return StructureClass.SaveToXYZ()
    except Exception as e:
        print(e)


def app_dir():
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    main()
