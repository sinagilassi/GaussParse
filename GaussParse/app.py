# import packages/modules
# external
import os
import pandas as pd
# internal
from GaussParse.docs import SummaryResult, Structure, Manager, PlotResult
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


def collect_files_from(file_path, file_type="Excel", sheet_name='Sheet1', ):
    '''
    Collect all gaussian files in a folder

    args:
        file_path {str}: file path
        file_type {str}: file type (default: Excel)
        sheet_name {str}: sheet name (default: Sheet1)

    return:
        copy all files listed in the source file to a folder
    '''
    try:
        ManagerClass = Manager(file_path, file_type, sheet_name)
        return ManagerClass.collect_files()
    except Exception as e:
        print(e)


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
        return SummaryResultClass.toExcel()
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
        return StructureClass.toXYZ()
    except Exception as e:
        print(e)


def plot_energy_profile(file_path, options={}, sheet_name='Sheet1', save_img=True):
    '''
    plot energy profile from data stored in an excel file

    args:
        file_path {str}: file path (xls format)
        options {dict}: plot options (default)
        sheet_name {str} : sheet name (default: Sheet1)

    return:
        display energy plot and save it in file directory
    '''
    try:
        PlotResultClass = PlotResult(file_path, sheet_name)
        # check manual options
        if len(options) > 0:
            res = PlotResultClass.init_plot(
                manual_options=options, save_img=save_img)
        else:
            res = PlotResultClass.init_plot(save_img=save_img)
        # return
        return res
    except Exception as e:
        print(e)


def app_dir():
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    main()
