# import packages/modules
# external
import os
from rich import print
import pandas as pd
from typing import List, Dict, Tuple, Union, Optional, Literal
# internal
from .docs import (
    SummaryResult, Structure, Manager, PlotResult, IRCResult, NBOParser
)
from .config import (
    __version__, __author__, __description__)
# local
# from GaussParse.utils import converter


def collect_files_from(file_path: str, file_type: Literal['Excel'] = "Excel",
                       sheet_name: Literal['Sheet1', 'Sheet2'] = 'Sheet1') -> bool:
    '''
    The function takes a folder path containing Gaussian files (log and txt files)
    and converts them into an Excel file.

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
        True if the conversion was successful, copy all files listed in the
        source file to a folder

    Examples
    --------
    >>> collect_files_from('tests', 'Excel', 'Sheet2')

    Notes
    -----
    1. Excel file format as:
        Excel file (gaussian log file list.xlsx) located in the `tests` folder.

    2. The log files MUST be listed in `Sheet1` and txt files in `Sheet2`.
    '''
    try:
        ManagerClass = Manager(file_path, file_type, sheet_name)
        # res
        res = ManagerClass.collect_files()
        return res
    except Exception as e:
        raise Exception("Conversion failed!, ", e)


def result_summary_to_excel(src: str, output_dir: Optional[str] = None, excel_file_name: Optional[str] = None) -> Tuple[bool, Dict[str, pd.DataFrame]]:
    """
    Convert Gaussian results summary text file to an Excel file,
    This function takes a file or folder path containing Gaussian results
    summary text files and converts them into an Excel file.

    Parameters
    ----------
    src : str
        Path to the file or folder containing the summary text files.
        If a folder is provided, all files in the folder will be converted.
        If a file is provided, only that file will be converted.
    output_dir : str, optional
        Path to the output directory where the Excel file will be saved.
        If not provided, the Excel file will be saved in the same directory as the source file.
    excel_file_name : str, optional
        Name of the output Excel file. If not provided, a default name will be used.
        
    Returns
    -------
    res : bool
        True if the conversion was successful.
    dfs : dict
        the list of dataframe

    Raises
    ------
    Exception
        If there is an error during the conversion process.
    """
    try:
        # init
        SummaryResultClass = SummaryResult(src, output_dir=output_dir, excel_file_name=excel_file_name)
        res, dfs = SummaryResultClass.toExcel()
        return res, dfs
    except Exception as e:
        raise Exception("Conversion failed!, ", e)
    
    
def result_summary_to_dataframe(src: str) -> Dict[str, pd.DataFrame]:
    """
    Convert Gaussian results summary text file to an Dataframe file,

    Parameters
    ----------
    src : str
        Path to the file or folder containing the summary text files.
        If a folder is provided, all files in the folder will be converted.
        If a file is provided, only that file will be converted.
        
    Returns
    -------
    res : Dict[str, pd.DataFrame]
        A dictionary containing the DataFrame data.

    Raises
    ------
    Exception
        If there is an error during the conversion process.
    """
    try:
        # init
        SummaryResultClass = SummaryResult(src)
        res = SummaryResultClass.toDataframe()
        return res
    except Exception as e:
        raise Exception("Conversion failed!, ", e)

def input_orientation_to_txt(src: str, file_name: str = ""):
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
        raise Exception("Operation failed!, ", e)


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
    res : list
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
        raise Exception("Operation failed!, ", e)


def plot_energy_profile(file_path: str, options: dict[str, str | int | list[int | float]] = {}, sheet_name: Literal['Sheet1'] = 'Sheet1', save_img: bool = True):
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
        raise Exception("Operation failed!, ", e)


def plot_irc_profile(file_path: str, options: dict[str, str | int | list[int | float]] = {}):
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
        raise Exception("Operation failed!, ", e)


def nbo_parser(file_path: str):
    '''
    Parse Gaussian NBO output file (NBO file) and open extracted data in the browser.

    Parameters
    ----------
    file_path : str
        path to the NBO output file

    Returns
    -------
    None

    Raises
    ------
    Exception
        If there is an error during the conversion process.

    '''
    try:
        # check
        if not file_path.endswith('.log'):
            raise Exception("Invalid file format, NBO file required!")

        # check file exist
        if not os.path.exists(file_path):
            raise Exception("File not found!, ", file_path)

        # init NBOParser
        nbo_parser = NBOParser(file_path)
        # NOTE: display in a browser
        nbo_parser.display_in_browser()

    except Exception as e:
        raise Exception("Operation failed!, ", e)
