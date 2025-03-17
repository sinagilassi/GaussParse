# import libs
import re
from typing import Optional, Union, List, Dict


def parser(content: str | List[str]) -> Dict[str, Union[List[Dict[str, Union[str, float]]], str]]:
    """
    Parse natural atomic orbital occupancies from the content of NBO output file.
    
    Parameters
    ----------
    content : str
        The content of the NBO output file.
        
    Returns
    -------
    dict
        A dictionary containing parsed data.
    """
    try:
        # Initialize an empty dictionary to hold the parsed data
        data = {}
        
        # check
        if isinstance(content, str):
            # REVIEW: Split the content into lines
            lines = content.split("\n")
        elif isinstance(content, list):
            # REVIEW: Use the content directly
            lines = content
        
        # Initialize a list to hold the data for the current item
        item_data = []
        item_id = None
        
        # Iterate through each line in the content
        for line in lines:
            if line == '' or line == '\n':
                # if item_data is not empty, set the data for the current item
                if item_data:
                    # set
                    data[item_id] = item_data
                    item_data = []
                continue
            
            # trim line
            line = line.strip()
            
            # pattern
            pattern = r'\s*(\d+)\s+(\w+)\s+(\d+)\s+(\w+)\s+' \
                r'(\w+\(\s*\d+\w+\))\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)'
            
            # match
            # REVIEW: Use re.match to match the pattern against the line
            match = re.match(
                pattern,
                line
            )
            if match:
                # set
                record = {
                    'NAO': match.group(1),
                    'Atom': match.group(2),
                    'No': match.group(3),
                    'lang': match.group(4),
                    'Type(AO)': match.group(5),
                    'Occupancy': float(match.group(6)),
                    'Energy': float(match.group(7))
                }
                
                
                # append
                item_data.append(record)
            
                # item id
                item_id = f'{match.group(2)}{match.group(3)}'
        # res
        return data
    except Exception as e:
        raise Exception(f"Error parsing natural atomic orbital occupancies: {e}")
