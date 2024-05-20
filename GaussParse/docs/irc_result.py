# import packages/modules
# external
import pandas as pd
import os
import re
# internal
from GaussParse.utils import CheckFileFormat, checkFile, checkDir, ListFiles, generateFileName


class IRCResult:
    '''
    Parse IRC results
    '''
    def __init__(self, src):
        self.src = src
        
    def toImage(self):
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
                file_list = ListFiles(file_dir)

            # analyze each file
            analyzed_files = self.AnalyzeIRC(file_dir, file_list)
            
            # transform to excel
            # self.save_data_to_excel(analyzed_files, excel_file_dir=file_dir)
            
            return True
        except Exception:
            pass

    def ReadIRC(self, filePath):
        '''
        read the content of IRC log file

        args:
            filePath {str}: full name of file with directory and format

        return:
            res {tuple}: 
                fileName {str}: file name
                item_loc {dict}: 
                    
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
                    print(E)
                else:
                    print("not found: Energies reported relative to the TS energy")
                    raise

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
            raise
        
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
            raise
        
    def save_data_to_image(self, d, image_file_dir=''):
        '''
        Save IRC result output.log to image file format

        args:
            d {List[dict]}: input data
            image_file_dir {str}: file directory used for saving all images
            
        return:
            status {bool}: True for successful action 
        '''
 
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
                    except:
                        df.to_excel(writer2, sheet_name=str(
                            sheet_name), index=False)

        # close
        writer.close()