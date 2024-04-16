import os


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