#  NHO Directionality and "Bond Bending" (deviations from line of nuclear centers)

# import libs
import re


def parser(content: str):
    """
    Parse the directionality from the given file.
    
    Parameters
    ----------
    content : str
        The content of the log file.
    """
    try:
        # check
        if not content:
            raise ValueError("No content found for directionality.")
        
        # dash-line pattern
        dash_line_pattern = re.compile(r'\s*[==]+\s*')
        # row pattern
        # row_pattern = r"\s*(\d+)\.\s+([\w*]+)\s*\(\s*(\d+)\)\s*([\w*]+)\s*(\d+)\s*-\s*([\w*]+)\s*(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)?\s*([\d.-]+)?\s*([\d.-]+)?\s*"
        row_pattern = r"\s*(\d+)\.\s+([\w*]+)\s*\(\s*(\d+)\)\s*([\w*]+)\s*(\d+)(?:\s*-\s*([\w*]+)\s*(\d+))?\s+((?:[\d.-]+|--))\s+((?:[\d.-]+|--))\s+((?:[\d.-]+|--))\s+((?:[\d.-]+|--))\s+((?:[\d.-]+|--))\s*(?:((?:[\d.-]+|--))\s+((?:[\d.-]+|--))\s+((?:[\d.-]+|--)))?\s*"
    
        # NOTE: search for the dash line
        match_found = dash_line_pattern.search(content) 
        
        # check
        if match_found:
            start_index = match_found.end()
            content_ = content[start_index:].strip().split('\n')

            table_data = []
            for line in content_:
                # NOTE: The regex pattern is used to extract the relevant data from each line.
                table_match = re.search(row_pattern, line)
                if table_match:
                    # extract the relevant data from the match
                    res_ = {
                        'No.': table_match.group(1),
                        'NBO': table_match.group(2),
                        'ID': table_match.group(3),
                        'Atom1': table_match.group(4),
                        'ID1': table_match.group(5),
                        'Atom2': table_match.group(6) if table_match.group(6) else '',
                        'ID2': table_match.group(7) if table_match.group(7) else '',
                        'Line of Centers Theta': '--' if table_match.group(8) == '--' else table_match.group(8),
                        'Line of Centers Phi': '--' if table_match.group(9) == '--' else table_match.group(9),
                        'Hybrid 1 Theta': '--' if table_match.group(10) == '--' else table_match.group(10),
                        'Hybrid 1 Phi': '--' if table_match.group(11) == '--' else table_match.group(11),
                        'Hybrid 1 Dev': '--' if table_match.group(12) == '--' else table_match.group(12),
                        'Hybrid 2 Theta': '--' if table_match.group(13) == '--' else table_match.group(13),
                        'Hybrid 2 Phi': '--' if table_match.group(14) == '--' else table_match.group(14),
                        'Hybrid 2 Dev': '--' if table_match.group(15) == '--' else table_match.group(15),
                    }
                    table_data.append(res_)

            return table_data
        else:
            return []
    except Exception as e:
        raise Exception(f"Error parsing directionality: {e}")


