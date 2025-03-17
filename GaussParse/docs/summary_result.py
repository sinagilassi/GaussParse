# import packages/modules
# external
import pandas as pd
import os
import re
# internal
from ..utils import CheckFileFormat, checkFile, checkDir, ListFiles, generateFileName


class SummaryResult:
    '''
    Parse result class
    '''
    # excel file name
    excel_default_file_name = 'summary_result'

    def __init__(self, src):
        self.src = src

    def toExcel(self):
        '''
        Transform the summary result to excel file

        Parameters
        ----------
        None

        Returns
        -------
        res : bool
            True if the conversion was successful
        dfs : dict
            list of dataframe
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

            # analyze each file
            analyzed_files = self.AnalyzeFiles(file_dir, file_list)

            # transform to excel
            res, dfs = self.save_data_to_excel(
                analyzed_files, excel_file_dir=file_dir)

            return res, dfs
        except Exception as e:
            raise Exception("Excel conversion failed!, ", e)

    def ReadFile(self, filePath):
        '''
        Read the content of file and put the info in a matrix

        Parameters
        ----------
        filePath : str
            full name of file with directory and format

        Returns
        -------
        tuple
            fileName, item_rows, column_names
        '''
        try:
            # file info
            fileDir, fileName, fileExtension = CheckFileFormat(filePath)

            # dict
            item_rows = {}
            column_names = ['Parameter', 'Value', 'Unit']

            # index
            k = 1

            # file open
            with open(filePath, "r") as f:
                # find main section
                fContent = f.readlines()

                for item in fContent:
                    # to skip empty line
                    if len(item) > 1:
                        # set id
                        _id = "data "+str(k)
                        # find "=" otherwise is description line
                        if item.find("=") > -1:
                            # split: data 1 = data 2
                            data1, data2 = item.strip().split("=", 1)

                            # key
                            _key = str(data1).replace("\n", "").strip()

                            # check "space" between number and string
                            _str_search = data2.strip()
                            if _str_search.find(" ") > -1:
                                # check begins with [-][+][number]
                                if _str_search.startswith("-") or _str_search.startswith("+") or _str_search[0].isdigit():
                                    # sort data
                                    _ext = re.search(
                                        r"([-+]?\d*\.?\d+([eE][-+]?\d+)?)\s*(.*)", _str_search, re.M)
                                    # check
                                    if _ext:
                                        numeric_value = float(_ext.group(1))
                                        unit = str(_ext.group(3))
                                else:
                                    numeric_value = _str_search
                                    unit = ''
                            else:
                                # only one part value (without unit)
                                # check numeric
                                _data2 = str(data2).replace(
                                    "\n", "").replace(".", "").strip()
                                if _data2.isnumeric():
                                    # number
                                    numeric_value = float(data2)
                                else:
                                    # string
                                    numeric_value = data2
                                unit = ""

                        else:
                            # description line
                            _key = str(item).replace("\n", "")
                            numeric_value = ''
                            unit = ''

                        # store
                        item_rows[_id] = {"Parameter": str(
                            _key), "Value": numeric_value, "Unit": str(unit)}

                        # set
                        k += 1

            return fileName, item_rows, column_names
        except Exception as e:
            print(e)

    def AnalyzeFiles(self, targetPath, fileList):
        '''
        Analyze each file

        Parameters
        ----------
        targetPath : str
            full name of file with directory and format
        fileList : list
            list of selected files

        Returns
        -------
        res : list
            list of file paths
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
                    _res = self.ReadFile(_file_full_path)
                    # save
                    res.append(_res)

                # return
                return res
            else:
                raise Exception("file list is empty!")

        except Exception as e:
            print(e)

    def save_data_to_excel(self, d, excel_file_dir='', excel_file_name='', excel_engine='xlsxwriter') -> tuple[bool, dict[str, pd.DataFrame]]:
        '''
        Save gaussian output.log to excel

        Parameters
        ----------
        d : list
            list of data
        excel_file_dir : str
            path of excel file
        excel_file_name : str
            name of excel file
        excel_engine : str
            engine of excel file

        Returns
        -------
        bool
            True if the operation was successful.
        df_list : dict[str, pd.DataFrame]
            list of dataframe
        '''
        # file name
        if excel_file_name == '':
            excel_file_name = generateFileName(self.excel_default_file_name)

        # update name
        excel_file_name = excel_file_name+'.xlsx'
        #  excel file path
        if len(excel_file_dir) > 0:
            # chosen path
            excel_file_path = os.path.join(
                excel_file_dir, excel_file_name)
        else:
            # current directory
            excel_file_path = os.getcwd()+'/'+excel_file_name

        # check file exist
        # if not os.path.isfile(excel_file_path):
        #     if not os.path.exists(excel_file_path):
        #         # create excel file
        #         writer = pd.ExcelWriter(excel_file_path,engine='xlsxwriter')
        #         # writer.close()

        writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

        # df list
        df_dict = {}

        # add each df to the excel sheet
        for item in d:
            # sheet name
            sheet_name = item[0]
            sheet_data = list(item[1].values())
            sheet_column_name = item[2]

            # df
            df = pd.DataFrame.from_dict(sheet_data)
            # size
            row, col = df.shape

            # save df
            df_dict[sheet_name] = df

            # check excel engine
            if excel_engine == 'xlsxwriter':
                # store
                df.to_excel(writer, sheet_name=str(sheet_name),
                            index=False, header=True, columns=sheet_column_name)

                # workbook and worksheet objects
                workbook = writer.book
                worksheet = writer.sheets[str(sheet_name)]

                # set column
                worksheet.set_column(0, 0, 110)
                worksheet.set_column(1, 2, 30)

                # set boarder
                border_format = workbook.add_format({'border': 1})
                worksheet.conditional_format(
                    0, 0, row, col, {'type': 'no_blanks', 'format': border_format})
                worksheet.conditional_format(
                    0, 0, row, col, {'type': 'blanks', 'format': border_format})

            else:
                # store
                with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists="new") as writer2:
                    try:
                        df.to_excel(writer2, sheet_name=str(
                            sheet_name), index=False, header=True, columns=sheet_column_name)
                    except Exception as e:
                        df.to_excel(writer2, sheet_name=str(
                            sheet_name), index=False)
                        print(e)

        # close
        writer.close()

        # res
        return True, df_dict
