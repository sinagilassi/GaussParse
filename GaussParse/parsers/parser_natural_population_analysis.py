"""
Parser for Natural Population Analysis outputs from Gaussian calculation.
Extracts different sections from NBO analysis log files.
"""
# import libs
import re



def parser(content: str):
    """
    Parse Natural Population Analysis log file and extract different sections.
    
    Args:
        file_path (str): Path to the NPA log file
        
    Returns:
        dict: Dictionary containing different sections of the NPA output
    """
    # check
    if not isinstance(content, str):
        raise TypeError("Content must be a string.")

    # Initialize the dictionary to store results
    sections = {
        "header": "",
        "population_data": "",
        "totals": "",
        "population_summary": "",
        "electron_config_header": "",
        "electron_config_data": ""
    }
    
    # SECTION: Extract section 1: Header
    header_pattern = r"\s+Atom\s+No\s+Charge\s+Core\s+Valence\s+Rydberg\s+Total"
    header_match = re.search(header_pattern, content, re.DOTALL)
    if header_match:
        sections["header"] = header_match.group(0)
    
    # SECTION: Extract section 2: Population data
    data_pattern = r"-{70,}\n(.*?)={70,}"
    data_match = re.search(data_pattern, content, re.DOTALL)
    if data_match:
        sections["population_data"] = data_match.group(1).strip()
        # NOTE: The data is in the form of a table with multiple columns and rows.
        row_pattern = r"\s+([A-Za-z]+)\s+(\d+)\s+(-?\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)"
        rows = re.findall(row_pattern, sections["population_data"])
        sections["population_data"] = [list(row) for row in rows]
    else:
        sections["population_data"] = "Data not found"
        
    # SECTION: Extract section 3: Totals
    # totals start
    total_start = content.find("* Total *")
    if total_start != -1:
        # sections["totals"] = totals_match.group(0)
        # NOTE: The data is in the line following the match
        line_pattern = r"\*\s*Total\s*\*\s*([-+]?\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)"
        line_match = re.search(line_pattern, content[total_start:content.find('\n', total_start)], re.DOTALL)
        if line_match:
            line_ = line_match.groups()
            # dictionary with keys: charge, core, valence, rydberg, total
            sections["totals"] = dict(zip(["natural charge", "core", "valence", "rydberg", "total"], line_))
    else:
        sections["totals"] = "Totals not found"
    
    # SECTION: Extract section 4: Population summary
    summary_start = content.rfind("Natural Population")
    if summary_start != -1:
        # match
        section_match = r"-+[\s\S]*?-+"
        content_ = content[summary_start:].strip()
        population_summary_match = re.findall(section_match, content_)
        if population_summary_match:
            content_extracted = population_summary_match[0]
            
            # NOTE: The data is in the form of a table with multiple columns and rows.
            row_pattern = r"(\w+(?: \w+)*)(?:\s+)(\d+\.\d+)(?:\s+\((\s*(\d+\.\d+)%\s+of\s+(\d+))\))?"
            rows = re.findall(row_pattern, content_extracted)
            sections["population_summary"] = [list(row) for row in rows]
        else:
            sections["population_summary"] = "Summary not found"
    else:
        sections["population_summary"] = "Summary not found"
    
    # SECTION: Extract section 5: Electron config header
    ec_header_start = content.find("Atom  No          Natural Electron Configuration")
    if ec_header_start != -1:
        ec_header_end = content.find("-----", ec_header_start)
        if ec_header_end != -1:
            sections["electron_config_header"] = content[ec_header_start:ec_header_end + 5]
    
    # SECTION: Extract section 6: Electron configuration data
    if sections["electron_config_header"]:
        ec_data_start = content.find(sections["electron_config_header"]) + len(sections["electron_config_header"])
        ec_data_start = content.find("\n", ec_data_start) + 1  # Skip one line after the header
        electron_config_data_ = content[ec_data_start:].strip()
        # NOTE: The data is in the form of a table with multiple columns and rows.
        row_pattern = r"\s+([A-Za-z]+)\s+(\d+)\s+(?:\[core\]|\s+)(.+)"
        rows = re.findall(row_pattern, electron_config_data_)
        sections["electron_config_data"] = [list(row) for row in rows]
    
    return sections

