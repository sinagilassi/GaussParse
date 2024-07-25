# import packages/modules
# external
import os
import datetime
# local
from GaussParse.handlers import errGeneral


def CheckFileFormat(file_path):
    '''
    Check file format

    Parameters
    ----------
    file_path : str
        path to the file

    Returns
    -------
    tuple
        file directory, file name, file format
    '''
    # check file exist
    if os.path.isfile(file_path):
        # file analysis
        fileDir = os.path.dirname(file_path)
        fileNameWithExtension = os.path.basename(file_path)
        fileName, fileExtension = os.path.splitext(fileNameWithExtension)

        # res
        return fileDir, fileName, fileExtension
    else:
        raise Exception('file path is not valid.')


def ListFiles(targetPath, fileExtension='txt'):
    '''
    List files in a target file

    Parameters
    ----------
    targetPath : str
        target path
    fileExtension : str, optional
        file extension, by default 'txt' or 'log'

    Returns
    -------
    fileFound : list
        a list of files in the target path

    '''
    try:
        # check
        if os.path.exists(targetPath):
            filesFound = []
            for f in os.listdir(targetPath):
                if f.endswith('.'+str(fileExtension)):
                    filesFound.append(f)
            # res
            return filesFound
        else:
            raise Exception("target path is not valid.")

    except Exception as e:
        raise e


def checkFile(file):
    if os.path.isfile(file):
        return True
    else:
        return False


def checkDir(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False


def checkPath(path):
    if os.path.exists(path):
        return True
    else:
        return False


def generateFileName(name):
    '''
    Generate a file name

    Parameters
    ----------
    name : str
        name of the file (without extension)

    Returns
    -------
    str
        a file name
    '''
    try:
        # check name
        if " " in name:
            raise errGeneral(
                errCode=1, errMessage="Name cannot contain spaces.")

        # get current time
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # Concatenate the parts to form the filename
        filename = f"{name}_{current_time}"
        return filename
    except errGeneral as e:
        print(e)
