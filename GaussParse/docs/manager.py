# import packages/modules
# external
import os
import pandas as pd
import shutil
from rich import print
# internal
from ..utils import CheckFileFormat, checkFile, checkDir, ListFiles


class Manager():
    '''
    Manage gaussian log files
    '''

    def __init__(self, src, file_type, sheet_name):
        self.src = src
        self.file_type = file_type
        self.sheet_name = sheet_name
        self.destination_folder_dir = ''
        self.file_extension = ''
        self.file_name = ''

    def collect_files(self) -> bool:
        '''
        Collect based on file type
        '''
        try:
            # check file format
            # check file/folder
            if checkFile(self.src):
                # read file
                fileDir, fileName, fileExtension = CheckFileFormat(self.src)
                # check extension
                if fileExtension == '.xlsx':
                    self.file_name = fileName
                    self.file_extension = fileExtension
                    self.destination_folder_dir = os.path.join(
                        fileDir, fileName)
                    # collect
                    self.collect_files_from_excel()
                    # res
                    return True
                else:
                    raise Exception('file extension is not valid.')
            else:
                raise Exception('file path is not valid.')
        except Exception as e:
            print(e)

    def collect_files_from_excel(self) -> bool:
        '''
        Collect gaussian files (txt/log) saved in an excel file as:

        Parameters
        ----------
        sheet_name : str
            excel sheet name

        Returns
        -------
        res : bool
            True if the conversion was successful, copy all files listed in the source file to a folder

        Examples
        --------
        >>>
        ...excel file contents:
        ...No | Name | Src
        ...----------------------------
        ...1  | file1 | ../file1.txt
        ...2  | file2 | ../file2.txt
        '''
        try:
            # load excel file
            df = pd.read_excel(self.src, sheet_name=self.sheet_name)
            # df list
            df_list = df.values.tolist()

            # check file
            self.check_file_exists(df_list)

            # copy all gaussian files to destination folder (the folder excel file exists)
            self.copy_files(df_list, self.destination_folder_dir)

            return True

        except Exception as e:
            print(e)

    def check_file_exists(self, df_list):
        '''
        Check the file exists in that directory

        Parameters
        ----------
        df_list : list
            df list

        Returns
        -------
        file_extension : List
            file extensions

        '''
        try:
            # file extension
            file_extensions = []

            for r in df_list:
                # file no
                file_no = r[0]
                # file name
                file_name = r[1]
                # file src
                file_src = (r[2]).strip()

                # check file exists
                if os.path.isfile(file_src):
                    # check file
                    fileDir, fileName, fileExtension = CheckFileFormat(
                        file_src)
                    # add
                    file_extensions.append(fileExtension)
                    # print(f"exists *** {file_no} {file_name} {file_src} *** ")
                else:
                    raise Exception(
                        f"does not exist *** {file_no} {file_name} {file_src} *** ")

                # res
                return file_extensions
        except Exception as e:
            print(e)

    def copy_files(self, df_list, destination_folder_dir):
        '''
        Copy all files from the source folder to the destination folder

        Parameters
        ----------
        df_list : list
            df list
        destination_folder_dir : str
            destination folder

        Returns
        -------
        total_files_copied : int
            total number of files copied

        '''
        # check destination folder
        if os.path.exists(destination_folder_dir) is False:
            os.makedirs(destination_folder_dir, exist_ok=True)

        total_files_copied = 0
        # copy files
        for r in df_list:
            # file no
            file_no = r[0]
            # file name
            file_name = r[1]
            # file src
            file_src = (r[2]).strip()

            # extract file info
            fileDir, fileName, fileExtension = CheckFileFormat(
                file_src)

            # file name with extension
            destination_file_name = file_name + fileExtension

            # file dir
            source_folder = os.path.dirname(file_src)
            # file name (in dir)
            source_file_name = os.path.basename(file_src)

            # Check if the source folder exists
            if os.path.exists(source_folder):
                # Copy all files from the source folder to the destination folder
                for filename in os.listdir(source_folder):
                    shutil.copy(os.path.join(source_folder, source_file_name),
                                os.path.join(destination_folder_dir, destination_file_name))
                # update total number of files copied
                total_files_copied += 1
            else:
                print('Source folder does not exist.')

        # total number of files copied
        print(
            f"total number of files copied: {total_files_copied} of {len(df_list)}")

        # res
        return total_files_copied
