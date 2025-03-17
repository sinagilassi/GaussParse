# NATURAL BOND ORBITAL ANALYSIS

# import libs
import re


def parser(content):
    """
    Extracts the data between the last two dash lines in the content.
    
    Parameters
    ----------
    content : str
        The content of the log file.
        
    Returns
    -------
    dict
        A dictionary containing the extracted data.
    """
    try:
        # pattern to find all dash lines
        pattern = r'-{3,}'
        # find all the dash lines
        dash_lines = [m.start() for m in re.finditer(pattern, content)]
        # check if there are at least two dash lines
        if len(dash_lines) >= 2:
            # extract the data between the last two dash lines
            start_index = dash_lines[-3]
            end_index = dash_lines[-1]
            # the data between the last two dash lines
            data = content[start_index:end_index].strip()
            
            # NOTE: The data is not well formatted, so we need to extract the data line by line
            # split the data by new line
            data_lines = data.split('\n')
            # initialize the dictionary to store the data
            sections = {}
            # initialize the key
            keys = ['Core', 'Valence Lewis', 'Total Lewis', 'Valence non-Lewis', 'Rydberg non-Lewis', 'Total non-Lewis']
            # iterate through the data lines
            for line in data_lines:
                
                # capture the line data
                line_data = capture_line_data(line)
                # check if the line data is not empty
                if line_data:
                    # append the line data to the key
                    val1, val2, val3, val4, val5 = line_data[0]
                    key = val1.strip()
                    # check
                    if key in keys:
                        # add the key to the dictionary
                        sections[key] = (val1, val2, val3, val4, val5)
                        
            return sections
        else:
            raise ValueError("Not enough dash lines found in the content.")
    except Exception as e:
        raise Exception(f"Error extracting data from : {e}")

def capture_line_data(data):
    '''Captures the data from the line'''
    pattern = r"(\S.*?\S)\s+([\d.]+)\s+\((\s*([\d.]+)%\s+of\s+(\d+))\)"
    return re.findall(pattern, data)


