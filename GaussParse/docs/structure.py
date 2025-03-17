# import packages/modules
import numpy as np
import pandas as pd
import os
import re
# internal
from ..utils import CheckFileFormat, checkFile, checkDir, ListFiles, generateFileName
from ..config import pt_dict


class Structure():
    '''
    Analyze input orientation
    '''

    def __init__(self, src):
        self.src = src
        # file path
        self.target_dir = ''

    def toTxt(self, file_name: str):
        '''
        Transform to txt

        Parameters
        ----------
        file_name : str
            file name (if it is empty, generate a name)


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

            # set
            self.target_dir = str(file_dir)

            # file name
            if len(file_name) == 0:
                file_name = generateFileName("molecular-orientation")

            # analyze each file
            analyzed_files = self.AnalyzeFiles(file_dir, file_list)

            # transform to excel
            res, _ = self.save_data_to_txt(analyzed_files, file_name)

            return res
        except Exception as e:
            print(e)

    def toXYZ(self):
        '''
        Transform to xyz format
        '''
        try:
            # check file/folder
            if checkFile(self.src):
                # read file
                fileDir, fileName, fileExtension = CheckFileFormat(self.src)
                # check extension
                if fileExtension == '.txt':
                    file_dir = fileDir
                    file = fileName+fileExtension
                    file_list = [file]

            if checkDir(self.src):
                # read folder
                file_dir = self.src
                file_list = ListFiles(file_dir)

            # set
            self.target_dir = str(file_dir)

            # analyze each file
            res = self.AnalyzeTxtFiles(file_dir, file_list)

            # return
            return res
        except Exception as e:
            raise Exception("toXYZ Operation failed!, ", e)

    def ReadXYZLogFile(self, filePath, pt_dict):
        '''
        read the content of log file

        Parameters
        ----------
        filePath : str
            full name of file with directory and format
        pt_dict : dict
            parodic table dict

        Returns
        -------
        tuple
            fileName, item_conv, item_loc, column_names

        '''
        try:
            # file info
            fileDir, fileName, fileExtension = CheckFileFormat(filePath)

            # dict
            item_loc = []
            item_conv = []
            column_names = ['Center Number', 'Atomic Number',
                            'Atomic Symbol', 'X', 'Y', 'Z']

            # index
            k = 1

            # file open
            with open(filePath, "r") as f:
                # find
                fContent = f.read()

                # find
                # ---------------------------------------------------------------------
                # Center     Atomic      Atomic             Coordinates (Angstroms)
                # Number     Number       Type             X           Y           Z
                # ---------------------------------------------------------------------
                # str_sub_1 = 'Number     Number              X              Y              Z'
                str_sub_1 = 'Center     Atomic      Atomic             Coordinates (Angstroms)'
                i_sub_1 = fContent.rfind(str_sub_1)
                str_1 = fContent[i_sub_1:]

                # split str by lines
                str_sub_lines = str_1.splitlines()

                # coordinate
                coordinate_1 = str_sub_lines[1]

                # separator
                sep_1 = str_sub_lines[2]

                # find the second separator
                k = 0
                for item in str_sub_lines:
                    # set regex
                    _line = item

                    # find
                    # force - groups(5)
                    # _res = re.search(r"\s+(\d+)\s+(\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)", _line)
                    # coordinate - groups(6)
                    _res = re.search(
                        r"\s+(\d+)\s+(\d+)\s+(\w+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)", _line)
                    # regex 1
                    # \s+(\d+)\s+(\d+)\s+(\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)
                    # regex 2
                    # \s+(\d+)\s+(\d+)\s+(\w+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)
                    # check
                    if _res:
                        _center_number = _res.group(1)
                        _atomic_number = _res.group(2)
                        _atomic_type = _res.group(3)
                        _X = _res.group(4)
                        _Y = _res.group(5)
                        _Z = _res.group(6)

                        # atomic symbol
                        _atomic_symbol = pt_dict.get(
                            str(int(_atomic_number)-1))['Symbol']
                        # store
                        _ele = {
                            'Center Number': _center_number,
                            'Atomic Number': _atomic_number,
                            'Atomic Symbol': _atomic_symbol,
                            'X': _X,
                            'Y': _Y,
                            'Z': _Z
                        }

                        item_loc.append(_ele)

                    if k > 2 and item == sep_1:
                        sep_2 = item
                        break

                    # update
                    k += 1

            return fileName, item_conv, item_loc, column_names
        except Exception as e:
            raise Exception(e)

    def AnalyzeFiles(self, targetPath: str, fileList: list):
        '''
        analyze each file

        Parameters
        ----------
        targetPath : str
            full name of file with directory and format
        fileList : list
            list of selected files

        Returns
        -------
        res : dict
            dictionary of input orientation data

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
                    _res = self.ReadXYZLogFile(_file_full_path, pt_dict)
                    # save
                    res.append(_res)

                # return
                return res
            else:
                raise Exception("file list is empty!")
        except Exception as e:
            raise Exception(f"File analysis failed!, {e}")

    def save_data_to_txt(self, d, file_name, df_format='string'):
        '''
        save xyz coordination output.log to txt file such as Notepad

        Parameters
        ----------
        d : dict
            dictionary of input orientation data
        file_name : str
            file name, default: res

        Returns
        -------
        tuple
            (True, text_file_path)

        '''

        # text file path
        _file_name = file_name + '.txt'
        # text_file_path = os.getcwd() + '/' + file_name + '.txt'
        text_file_path = os.path.join(self.target_dir, _file_name)

        # open the text file in write mode
        with open(text_file_path, 'w') as f:
            # add each df to the text file
            for item in d:
                # sheet name
                file_name_full = item[0]
                item_conv = item[1]
                item_loc = item[2]
                column_names = item[3]

                # df
                df = pd.DataFrame.from_dict(item_loc)

                # check df format
                if df_format == 'string':
                    # df to string
                    df_string = df.to_string(
                        index=False, col_space=10, justify='left')
                    # Add 6 spaces indent to each line
                    indented_df_string = '\n'.join(
                        ['      ' + line for line in df_string.split('\n')])

                    # sep lin
                    sep_line = '---------------------------------------------------------------------------------'
                    # Split the string into lines
                    lines = indented_df_string.split('\n')

                    # find atomic symbol
                    # atomic_numbers = [item.split(" ")[0] for item in lines]

                    # Find the maximum length of the lines
                    max_length = max(len(line) for line in lines)

                    # write file name as heading
                    # f.write('-' * max_length + '\n')
                    f.write("Input orientation: "+file_name_full+'\n')
                    # f.write('-' * max_length + '\n')

                    # write df string to the text file
                    # header line
                    # f.write(lines[0] + '\n')

                    _header = """---------------------------------------------------------------------------------
Center      Atomic      Atomic                   Coordinates (Angstroms)
Number      Number      Symbol                  X           Y           Z
---------------------------------------------------------------------------------
"""
                    f.write(_header)

                    # content
                    f.write(indented_df_string[max_length+1:] + '\n')

                    # last line
                    f.write(sep_line + '\n\n')
                else:
                    # write file name as heading
                    f.write(file_name_full + '\n')
                    f.write('-' * len(file_name_full) + '\n')

                    # write the header
                    f.write('\t'.join(df.columns) + '\n')

                    # write the rest of the data frame
                    for i in range(df.shape[0]):
                        f.write('\t'.join(map(str, df.iloc[i])) + '\n')
                    f.write('\n')
        # res
        return (True, text_file_path)

    def AnalyzeTxtFiles(self, targetPath: str, fileList: list[str]):
        '''
        Analyze each file

        Parameters
        ----------
        targetPath : str
            full name of file with directory and format
        fileList: list
            list of selected files

        Returns
        -------
        res : dict
            dictionary of input orientation data

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
                    _res = self.SaveToXYZ(_file_full_path)
                    # save
                    res.append(_res)

                # return
                return res
            else:
                raise Exception("file list is empty!")
        except Exception as e:
            raise Exception(f"Text file analysis failed!, {e}")

    def generate_xyz_file(self, atom_list: list, file_name: str = "molecule"):
        """
        Generates an XYZ file from a list of atom positions with nicely formatted columns.

        Parameters
        ----------
        atom_list : list
            List of tuples containing the atom symbol and its coordinates (x,y,z).
        file_name : str
            The name of the output XYZ file.

        Returns
        -------
        str
            The name of the generated XYZ file.


        Example
        -------
        >>> atom_list = [
        ...     ("C", 0.000000, 0.000000, 0.000000),
        ...     ("H", 0.000000, 0.000000, 1.089000),
        ...     ("H", 1.026719, 0.000000, -0.363000),
        ...     ("H", -0.513360, -0.889165, -0.363000),
        ...     ("H", -0.513360, 0.889165, -0.363000)
        ... ]
        >>> file_name = "molecule"
        >>> generate_xyz_file(atom_list, file_name)

        """
        # number of atoms
        num_atoms = len(atom_list)
        # file
        _file = file_name+".xyz"
        # save
        with open(_file, 'w') as file:
            file.write(f"{num_atoms}\n")
            file.write(f"{file_name}\n")
            for atom in atom_list:
                element, x, y, z = atom
                # file.write(f"{element}\t{x:.6f}\t{y:.6f}\t{z:.6f}\n")
                file.write(
                    f"{element:<2} {x:> 10.6f} {y:> 10.6f} {z:> 10.6f}\n")
        # file name
        return _file

    def SaveToXYZ(self, file_path: str):
        '''
        read the content of txt file

        Parameters
        ----------
        file_path : str
            full name of file with directory and format

        Returns
        -------
        res : tuple
            _file_name, item_conv, item_loc, column_names
        '''
        try:
            # file info
            fileDir, fileName, fileExtension = CheckFileFormat(file_path)

            # dict
            item_loc = []
            item_conv = []
            column_names = ['Center Number', 'Atomic Number',
                            'Atomic Symbol', 'X', 'Y', 'Z']

            # index
            k = 1

            # file open
            with open(file_path, "r") as f:
                # find
                fContent = f.read()

                # lines
                lines = fContent.split('\n')

                # title
                title = lines[0].split(":")[1].strip()
                sep_1 = lines[1]

                # split str by lines
                str_sub_lines = lines[4:]

                # find the second separator
                k = 0
                for item in str_sub_lines:
                    # set regex
                    _line = item

                    # find
                    # force - groups(5)
                    # _res = re.search(r"\s+(\d+)\s+(\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)", _line)
                    # coordinate - groups(6)
                    _res = re.search(
                        r"\s+(\d+)\s+(\d+)\s+(\w+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)", _line)
                    # regex 1
                    # \s+(\d+)\s+(\d+)\s+(\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)
                    # regex 2
                    # \s+(\d+)\s+(\d+)\s+(\w+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)
                    # check
                    if _res:
                        _center_number = _res.group(1)
                        _atomic_number = _res.group(2)
                        _atomic_symbol = _res.group(3)
                        _X = _res.group(4)
                        _Y = _res.group(5)
                        _Z = _res.group(6)

                        # store
                        _ele = (_atomic_symbol, float(
                            _X), float(_Y), float(_Z))

                        item_loc.append(_ele)
                    # else:
                    #   print(f"{_res},{k}")

                    if k > 2 and item.strip() == sep_1:
                        sep_2 = item.strip()
                        break

                    # update
                    k += 1

            # save xyz file
            _file_name = self.generate_xyz_file(item_loc, title)

            return _file_name, item_conv, item_loc, column_names
        except Exception as e:
            raise Exception(f"Save to XYZ failed!, {e}")

    def FindStructures(self, txt_file: str, display_res: bool = False):
        '''
        Find structures saved in a text file (.txt)

        Parameters
        ----------
        txt_file : str
            full name of file with directory and format
        display_res : bool
            whether to display the result

        Returns
        -------
        res : list
            list of str matched
        '''
        pattern = re.compile(
            r'((\w+)?\n)?'
            r'---------------------------------------------------------------------------------\n'
            r' Center      Atomic      Atomic                   Coordinates \(Angstroms\)\n'
            r' Number      Number      Symbol                  X           Y           Z\n'
            r'---------------------------------------------------------------------------------\n'
            r'(.*?)\n---------------------------------------------------------------------------------', re.DOTALL)

        # Find all matches
        matches = pattern.findall(txt_file)

        # res
        res = []

        # Print each match with the name (if present)
        for match in matches:
            full_match, name, coordinates = match
            name = name if name else "No name"
            _record = [name, coordinates]
            res.append(_record)
            # check
            if display_res:
                print(f"Input orientation: {name}")
                print(coordinates)
                print('---')
        # res
        return res
