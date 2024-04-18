import os
import datetime


def CheckFileFormat(file_path):
    '''
    check file format

    args:
        filePath: file name dir

    return:
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
    list files in a target file

    args:
        targetPath: target path
        fileExtension: file extension, default is txt, can be changed log

    return:
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
    generate a file name
    
    args:
        name: name of the file

    return:
        a file name
    '''
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Concatenate the parts to form the filename
    filename = f"{name}_{current_time}"
    return filename