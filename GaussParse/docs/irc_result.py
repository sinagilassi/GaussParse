# import packages/modules
# external
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
# internal
from GaussParse.utils import CheckFileFormat, checkFile, checkDir, ListFiles, generateFileName, EnergyUnit


class IRCResult:
    '''
    Parse IRC results
    '''
    # plot options
    options = {
        "fig_size": [12, 6],
        "img_name": 'img',
        "target_dir": "",
        "y_label": "Total Energy",
        "x_label": "Intrinsic Reaction Coordinate",
        "xlim": [10, 10],
        "ylim": [5, 5],
        "label_margin": 4,
        "y_major_locator": 5,
        "plt_style": 'bmh',
        "line_color": "blue",
        "y_unit": "Hartree"
    }

    def __init__(self, src):
        self.src = src

    def toImage(self, manual_options={}):
        '''
        Transform the IRC result to image
        '''
        try:
            # check file/folder
            if checkFile(self.src):
                # read file
                fileDir, fileName, fileExtension = CheckFileFormat(self.src)
                # check extension
                if fileExtension == '.log':
                    file_dir = fileDir
                    file = fileName+fileExtension
                    file_list = [file]

            if checkDir(self.src):
                # read folder
                file_dir = self.src
                file_list = ListFiles(file_dir, fileExtension="log")

            # update options
            if len(manual_options) > 0:
                self.update_plot_options(manual_options)

            # analyze each file
            analyzed_files = self.AnalyzeIRC(file_dir, file_list)

            # plot data and then save
            self.save_data_to_image(analyzed_files, image_file_dir=file_dir)

            return True
        except Exception:
            pass

    def update_plot_options(self, data):
        '''
        update plot options

        args:
            data {dict}: plot options
        '''
        try:
            for key, value in data.items():
                if key in self.options.keys():
                    self.options[str(key)] = str(value)
                else:
                    raise Exception(f"key {key} not found!")
        except Exception as e:
            raise Exception(e)

    def ReadIRC(self, filePath):
        '''
        read the content of IRC log file

        args:
            filePath {str}: full name of file with directory and format

        return:
            res {tuple}
                fileName {str}: file name
                item_loc {dict}: irc data
                column_names {List}: list of column names
        '''
        try:
            # file info
            fileDir, fileName, fileExtension = CheckFileFormat(filePath)

            # dict
            item_loc = []
            column_names = ['X', 'Energy', 'RxCoord']

            # index
            k = 1

            # file open
            with open(filePath, "r") as f:
                # content
                fContent = f.read()
                # find
                str_sub_1 = "Energies reported relative to the TS energy of "
                i_sub_1 = fContent.rfind(str_sub_1)
                str_1 = fContent[i_sub_1:]

                # split str by lines
                str_sub_lines = str_1.splitlines()

                # energy
                E_pattern = r"([-+]?\d*\.\d+|\d+)"
                E_match = re.search(E_pattern, str_sub_lines[0])
                if E_match:
                    E = float(E_match.group())
                    # print(E)
                else:
                    raise Exception(
                        "not found: Energies reported relative to the TS energy")

                # separator
                sep_1 = str_sub_lines[1]
                # table header
                table_header = str_sub_lines[2]

                # find the second separator
                k = 0
                k_set = 4
                for item in str_sub_lines:
                    # set regex
                    _line = item

                    # find
                    _res = re.search(
                        r"(\d+)\s+([-+]?\d*\.\d+|\d+)\s+([-+]?\d*\.\d+|\d+)", _line)
                    # check
                    if _res:
                        _X = _res.group(1)
                        _Energy = _res.group(2)
                        _RxCoord = _res.group(3)
                        # store
                        _ele = {
                            'X': int(_X),
                            'Energy': float(_Energy),
                            'RxCoord': float(_RxCoord),
                            'EnergyTotal': float(_Energy) + E,
                        }

                        item_loc.append(_ele)

                    # check the end of data zone
                    if k > k_set and item == sep_1:
                        sep_2 = item
                        break

                    # update
                    k += 1

            return fileName, item_loc, column_names
        except Exception as e:
            raise Exception(e)

    def AnalyzeIRC(self, targetPath, fileList):
        '''
        Analyze every file in the file list

        args:
            targetPath {str}: target folder
            fileList {List[str]}: list of selected files

        return:
            res: dict
        '''
        try:
            # check
            if len(fileList) > 0:
                # res
                res = []
                for item in fileList:
                    # file path
                    _file_full_path = os.path.join(str(targetPath), str(item))
                    # read file
                    _res = self.ReadIRC(_file_full_path)
                    # save
                    res.append(_res)

                # return
                return res
            else:
                raise Exception("file list is empty!")

        except Exception as e:
            raise Exception(e)

    def save_data_to_image(self, d, image_file_dir=''):
        '''
        Save IRC result output.log to image file format

        args:
            d {List[dict]}: input data
            image_file_dir {str}: file directory used for saving all images

        return:
            status {bool}: True for successful action 
        '''
        # index
        data_len = len(d)

        # unit class
        EnergyUnitClass = EnergyUnit(self.options['y_unit'])

        # add each df to the excel sheet
        for item in d:
            # extract data
            file_name = item[0]
            file_data = item[1]
            file_column_name = item[2]

            # img file name
            img_file_name = file_name.strip()

            #  img file path
            if len(image_file_dir) == 0:
                image_file_dir = os.getcwd()

            # dataframe
            _df = pd.DataFrame(file_data)

            # x values
            _X = _df['RxCoord']
            X = _X.to_numpy()

            # y values
            _Y = _df['EnergyTotal']
            Y = _Y.to_numpy()

            # check unit
            if self.options['y_unit'] == "kcal/mol":
                Y = EnergyUnitClass.hartree_to_kcal_per_mol(Y)
            elif self.options['y_unit'] == "kJ/mol":
                Y = EnergyUnitClass.hartree_to_kJ_per_mol(Y)
            elif self.options['y_unit'] == "eV":
                Y = EnergyUnitClass.hartree_to_eV(Y)
            else:
                # hartree
                Y = Y

                # save image
            self.save_plot(X, Y, file_name, image_file_dir, img_file_name)

            # empty dataframe
            _df = pd.DataFrame()

        # return
        return True

    def save_plot(self, X, Y, title, target_dir, img_file_name, display=False, format="png"):
        '''
        plot irc profile

        args:
            X {list}: x values
            Y {list}: y values
            title {str}: plot title
            target_dir {str}: target directory
            img_file_name {str}: image file name
            display {bool}: display plot (default: False)
            format {str}: image format (default: png, others: svg)
        '''
        # Add a title to the plot
        plt.title(title, fontweight='bold', color='black', fontsize=16)

        # styles
        plt_style = self.options['plt_style']
        plt.style.use(plt_style)

        # axe labels
        plt.xlabel(self.options['x_label'],
                   fontweight='bold', color='black')
        # set y label
        _y_label = self.options['y_label'] + \
            " (" + self.options['y_unit'] + ")"
        plt.ylabel(_y_label, fontweight='bold', color='black')

        # grid
        # plt.grid(which='both', color='gray', linestyle='--', linewidth=0.5)
        # Enable minor ticks
        plt.minorticks_on()
        # Customize major grid lines
        # plt.grid(which='major', color='grey', linestyle='-', linewidth=0.75)
        # Customize minor grid lines
        # plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

        # Customize major grid lines
        plt.grid(which='major', color='grey',
                 linestyle='-', linewidth=0.5, alpha=0.25)
        # Customize minor grid lines
        plt.grid(which='minor', color='gray',
                 linestyle=':', linewidth=0.4, alpha=0.25)

        # line color
        line_color = self.options['line_color']

        # plot data
        plt.plot(X, Y, color=line_color)

        # img file
        img_file = (img_file_name + "." + format).strip()
        # img file path
        img_path = os.path.join(target_dir, img_file)

        # save a figure
        # check
        if format == 'svg':
            # svg
            plt.savefig(img_path, dpi=300, facecolor='white',
                        bbox_inches='tight')
        elif format == 'png':
            # png
            plt.savefig(img_path, facecolor='white',
                        dpi=300, bbox_inches='tight')

        # Customize major tick marks for the current axes
        # plt.gca().tick_params(axis='both', which='major', length=5, width=1, colors='black', direction='in', labelsize=10)
        # Customize minor tick marks for the current axes
        # plt.gca().tick_params(axis='both', which='minor', length=5, width=1, colors='gray', direction='in', labelsize=10)
        # Set the y-axis limits to display the actual values
        plt.gca().yaxis.set_major_formatter(
            ticker.StrMethodFormatter('{x:,.3f}'))
        # Customize the appearance of the spines
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        plt.gca().spines['left'].set_color('black')

        # Set the minimum and maximum values for the x-axis
        plt.xlim(min(X)-1, max(X)+1)  # Adjust the values as needed

        # check
        if display:
            # show
            plt.show()

        # close
        plt.close()

    def change_unit(self, data):
        '''
        change unit from Hartree to kcal/mol or kJ/mol
        '''
        pass
