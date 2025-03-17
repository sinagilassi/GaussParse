# (Occupancy)   Bond orbital/ Coefficients/ Hybrids
# https://nbo6.chem.wisc.edu/tutorial.html

# import libs
import re


def parser(content):
    """   
    Parse orbital occupacy 
    
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
        # check
        if not content:
            raise ValueError("No content found for natural atomic orbital occupancies.")
        # Initialize an empty dictionary to store the records
        records = {}
        
        # Find the start indices of all records
        record_starts = [m.start() for m in re.finditer(r'\d+\. \(', content)]
        
        # Extract each record's content
        for i, start in enumerate(record_starts):
            end = record_starts[i + 1] if i + 1 < len(record_starts) else len(content)
            record_content = content[start:end].strip()
            record_number = re.match(r'(\d+)\. \(', record_content).group(1)
            
            # NOTE: Check the patterns in the record
            extracted = check_patterns(record_content)
            
            records[record_number] = extracted

        return records
    except Exception as e:
        raise Exception(f"Error parsing occupancy log: {e}")

def check_patterns(record):
    """
    Check the patterns in the record

    Parameters
    ----------
    record : str
        The record content

    Returns
    -------
    dict
        A dictionary containing the extracted data.
    """
    try:
        pattern1 = r"\s*\((\d+\.\d+)\)\s*([A-Z]+?\*?)\s*\(\s*(\d+)\)\s*([A-Z]+)\s*(\d+)\s*-*\s*([A-Z]+)*\s*(\d+)*\s*"
        # pattern2 = r"\(\s*\d+\.\d+%\).*?\(\s*\d+\.\d+%\)(?:\n|.)*"

        # Extract the patterns
        match1 = re.search(pattern1, record)

        # Extract the relevant information from the matches
        # occupacy
        occupancy = match1.group(1) if match1 else None
        # nbo type
        nbo_type = match1.group(2) if match1 else None
        # nbo type id
        nbo_type_id = match1.group(3) if match1 else None
        # atom/id
        atom1 = match1.group(4) if match1 else None
        atom1_id = match1.group(5) if match1 else None
        atom2 = match1.group(6) if match1 else None
        atom2_id = match1.group(7) if match1 else None

        # Get the rest of the record after the last index of match1
        last_index = match1.end() if match1 else None
        
        # check
        if last_index:
            rest_of_record = record[last_index:] if last_index else None
        else:
            rest_of_record = None
        # set
        hybrids = rest_of_record
        
        # Return the extracted patterns
        res = {
            'occupancy': occupancy,
            'nbo_type': nbo_type,
            'nbo_type_id': nbo_type_id,
            'atom1': atom1,
            'atom1_id': atom1_id,
            'atom2': atom2,
            'atom2_id': atom2_id,
            'hybrids': hybrids
        }
        
        return res
    except Exception as e:
        raise Exception(f"Error checking patterns: {e}")