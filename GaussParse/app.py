# import packages/modules
# external
import os
# internal
from GaussParse.docs import SummaryResult, Structure, Manager, PlotResult, IRCResult
from GaussParse.config import __version__


def main():
    # version
    print(
        f'GaussParse {__version__} is a python package to parse Gaussian output files.')


def app_dir():
    return os.path.dirname(os.path.abspath(__file__))


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
                plot_type {str}: plot type, linear or gaussian (default: linear)
                img_name {str}: plot name (file name), (default: plot)
                target_dir {str}: plot img to target dir, (default: the same as source file)
                plot_sub {dict}: subplot details (not used)
                row {number}: plot row (not used)
                col {number}: plot column (not used)
                y_label {str}: y label text (default: "Gibbs free energy (kcal/mol)")
                x_label {str}: x label text (default: "Reaction coordinate")
                plot_title {str}: plot title (default: "")
                xlim {list[number]}: x-axis range (default: [10, 10])
                ylim {list[number]}: y-axis range (default: [5, 5])
                figsize {list[number]}: fig size (default: [12, 6])
                label_margin {number}: label margin (default: 4) 
                y_major_locator {number}: set y-axis major locator (default: 5)
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


def plot_irc_profile(file_path: str, options: dict = {}):
    '''
    plot IRC profile from gaussian irc log file

    args:
        file_path {str}: file path (log format)
        options {dict}: plot options 
            img_name {str}: plot name (file name), (default: plot)
            target_dir {str}: plot img to target dir, (default: the same as source file)
            y_label {str}: y label text (default: "Gibbs free energy (kcal/mol)")
            x_label {str}: x label text (default: "Reaction coordinate")
            xlim {list[number]}: x-axis range (default: [10, 10])
            ylim {list[number]}: y-axis range (default: [5, 5])
            figsize {list[number]}: fig size (default: [12, 6])
            label_margin {number}: label margin (default: 4) 
            y_major_locator {number}: set y-axis major locator (default: 5)
            plt_style {str}: plot theme (default: bmh),
            line_color {str}: plot line color (default: blue),
            y_unit {str}: y label unit (default: Hartree)

    return:
        save IRC plot
    '''
    try:
        IRCResultClass = IRCResult(file_path)
        # check
        if len(options) > 0:
            res = IRCResultClass.toImage(manual_options=options)
        else:
            res = IRCResultClass.toImage()
        # res
        return res
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
