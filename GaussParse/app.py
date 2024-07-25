# import packages/modules
# external
import os
# internal
from GaussParse.docs import SummaryResult, Structure, Manager, PlotResult, IRCResult
from GaussParse.config import __version__
# local
# from GaussParse.utils import converter


def main():
    '''
    Print app version and description
    '''
    # version
    print(
        f'GaussParse {__version__} is a python package to parse Gaussian output files.')


def app_dir():
    '''
    Return app directory
    '''
    return os.path.dirname(os.path.abspath(__file__))


def collect_files_from(file_path, file_type="Excel", sheet_name='Sheet1', ):
    '''
    Collect all gaussian files in a folder, excel file format as:
    Excel file (gaussian log file list.xlsx) located in tests folder

    Parameters
    ----------
    file_path : str
        path to the folder containing the files
    file_type : str
        file type (default: Excel)
    sheet_name : str
        sheet name (default: Sheet1)

    Returns
    -------
    res : bool
        True if the conversion was successful, copy all files listed in the source file to a folder

    Examples
    --------
    >>> collect_files_from('tests', 'Excel', 'Sheet2')

    '''
    try:
        ManagerClass = Manager(file_path, file_type, sheet_name)
        # res
        res = ManagerClass.collect_files()
        return res
    except Exception as e:
        print(e)


def result_summary_to_excel(src: str):
    """
    Convert Gaussian results summary text file to an Excel file,\
    This function takes a file or folder path containing Gaussian results summary text files \
    and converts them into an Excel file.

    Parameters
    ----------
    src : str
        Path to the file or folder containing the summary text files.\
        If a folder is provided, all files in the folder will be converted.\
        If a file is provided, only that file will be converted.

    Returns
    -------
    res : bool
        True if the conversion was successful.

    Raises
    ------
    Exception
        If there is an error during the conversion process.
    """
    try:
        SummaryResultClass = SummaryResult(src)
        res = SummaryResultClass.toExcel()
        return res
    except Exception as e:
        print(e)


def input_orientation_to_txt(src: str, file_name=""):
    """
    Save input orientations shown in Gaussian files to a text file,
    The Gaussian log file is parsed to extract data, such as the molecular orientation in the x, y, and z coordinates, 
    and saves this data to a text file.

    Parameters
    ----------
    src : str
        Path to the file or folder containing the Gaussian log files.
        If a folder is provided, all Gaussian log files in the folder will be parsed.
        If a Gaussian file is provided, only that file will be parsed.
    file_name : str, optional
        Name of the output text file. If not provided, a default name will be used.


    Returns
    -------
    res : bool
        True if the conversion was successful.

    Raises
    ------
    Exception
        If there is an error during the conversion process.

    """
    try:
        StructureClass = Structure(src)
        # res
        res = StructureClass.toTxt(file_name)
        return res
    except Exception as e:
        print(e)


def txt_orientation_to_xyz(src: str):
    '''
    Load an input orientation text file and then transform it to xyz format

    Parameters
    ----------
    src : str
        Path to the input orientation text file.
        If a folder is provided, all text files in the folder will be converted.
        If a text file is provided, only that file will be converted.

    Returns
    -------
    res : dict
        A dictionary containing the XYZ data.

    Raises
    ------
    Exception
        If there is an error during the conversion process.

    '''
    try:
        StructureClass = Structure(src)
        # res
        res = StructureClass.toXYZ()
        return res
    except Exception as e:
        print(e)


def plot_energy_profile(file_path, options={}, sheet_name='Sheet1', save_img=True):
    '''
    Plot energy profile from data stored in an excel file,

    Excel file (energy.xlsx) located in tests folder
    Excel file columns including (LABEL, X, Y, GROUP, LEGEND, COLOR, LABEL_POSITION, LABEL_DISPLAY, Y_POSITION, Y_DISPLAY):
    LABEL | X | Y | GROUP | LEGEND | COLOR | LABEL_POSITION | LABEL_DISPLAY | Y_POSITION | Y_DISPLAY

        LABEL: label text
        X: reaction coordinate
        Y: Gibbs free energy
        GROUP: indicate data series (id: 1, 2, 3)
        LEGEND: legend for each data series (short txt)
        COLOR: data series color (red, green, brown)
        LABEL_POSITION: label position (top, bottom)
        LABEL_DISPLAY: display data
        Y_POSITION: label position (top, bottom)
        Y_DISPLAY: display data

    Parameters
    ----------
    file_path : str
        path to the excel file
    options : dict
        plot options (default)
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
    sheet_name : str
        sheet name (default: 'Sheet1')
    save_img : bool
        save img (default: True)

    Returns
    -------
    res : bool
        display energy plot and save it in file directory

    Raises
    ------
    Exception
        If there is an error during the conversion process.
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
    Plot IRC profile from gaussian irc log file
    In Gaussian, Results -> IRC/Path... display IRC profile, this figure can be plotted.

    Parameters
    ----------
    file_path : str
        path to the log file
    options : dict
        plot options
            img_name {str}: plot name (file name), (default: plot)
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

    Returns
    -------
    res : bool
        display IRC plot and save it in file directory

    Raises
    ------
    Exception
        If there is an error during the conversion process.
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


# if __name__ == "__main__":
#     main()
