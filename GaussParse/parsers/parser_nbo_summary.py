# import libs
import re

def extract_nbo_summary_contents(content: str):
    """
    Extracts only the content after the "Natural Bond Orbitals (Summary):" header
    by first finding the line number and then extracting all subsequent lines
    until the end of the section.
    
    Parameters:
    -----------
    content : str
        The content of the file as a string.
        
    Returns:
    --------
    str
        The extracted content after the "Natural Bond Orbitals (Summary):" header,
        not including the header line itself. Returns empty string if the section is not found.
    """
    try:
        # check
        if not content:
            raise ValueError("Content is empty.")
        
        # check if content is a string
        if not isinstance(content, str):
            raise ValueError("Content should be a string.")
        
        # check if content is empty
        if not content.strip():
            raise ValueError("Content is empty.")
        
        # split content into lines
        lines = content.split("\n")
        
        # Find the line number containing the header
        header_line = -1
        for i, line in enumerate(lines):
            if "Natural Bond Orbitals (Summary):" in line:
                header_line = i
                break
        
        # If header not found, return empty string
        if (header_line == -1):
            raise ValueError("Natural Bond Orbitals (Summary) section not found in the file.")
        
        # summary section ends with a blank line
        all_content = lines[header_line:]
        # convert to string
        all_content = "\n".join(all_content)
        
        return all_content
    except Exception as e:
        raise Exception(f"Error extracting NBO summary content: {e}")

def parse_nbo_entry(content):
    """
    Parse NBO entries with format like:
                                                        
    Parameters:
    -----------
    content : str
        A string containing the NBO entry
        
    Returns:
    --------
    dict
        Parsed NBO entry information
    """
    # Define regex pattern for the first line - making the contributions part optional
    # pattern = r'(\d+)\.\s+([\w*]+)\s*\(\s*(\d+)\)\s+([A-Za-z]+)\s+(\d+)\s*-\s*([A-Za-z]+)\s+(\d+)\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)(?:\s+(.*?))?(?:\n|$)'
    pattern = r'(\d+)\.\s+([\w*]+)\s*\(\s*(\d+)\)\s+([A-Za-z]+)\s+(\d+)\s-*\s*([A-Za-z]+)*\s+(\d+)*\s+([-+]?\d*\.\d+)\s+([-+]?\d*\.\d+)(?:\s+(.*?))?(?:\n|$)'
    
    # Find the main entry
    match = re.search(pattern, content)
    
    if not match:
        raise Exception("NBO entry could not be parsed.")
    
    # Extract values from the main match
    entry_number = match.group(1)
    orbital_type = match.group(2)
    orbital_number = match.group(3)
    atom1_type = match.group(4)
    atom1_number = match.group(5)
    atom2_type = match.group(6)
    atom2_number = match.group(7)
    value1 = match.group(8)
    value2 = match.group(9)
    
    # Get contributions from first line (if they exist)
    contributions_first_line = match.group(10).strip() if match.group(10) else ""
    
    # Pattern to find continued lines with contributions (indented lines)
    continued_pattern = r'^\s+(.*?)$'
    
    # Find all continuation lines
    continued_lines = re.findall(continued_pattern, content, re.MULTILINE)
    
    # Combine all contributions
    all_contributions = [contributions_first_line] + continued_lines if contributions_first_line else continued_lines
    contributions_text = " ".join(all_contributions).strip()
    
    # Extract individual contributions with their types
    contributions = []
    # contribution 
    contribution_types = {
        'g': [],
        'v': [],
        'r': [],
    }
    # check if contributions exist
    if contributions_text:
        contrib_pattern = r'(\d+)\(([vgr])\)'
        contributions = re.findall(contrib_pattern, contributions_text)
        # contribution type
        for contrib in contributions:
            contrib_type = contrib[1]
            contrib_number = contrib[0]
            contribution_types[contrib_type].append(contrib_number)

    # Create structured output
    result = {
        "entry_number": entry_number,
        "orbital_type": orbital_type,
        "orbital_number": orbital_number,
        "bond": f"{atom1_type} {atom1_number} - {atom2_type} {atom2_number}",
        "atom1": {"type": atom1_type, "number": atom1_number},
        'atom1_type': atom1_type,
        'atom1_number': atom1_number,
        "atom2": {"type": atom2_type, "number": atom2_number},
        "atom2_type": atom2_type,
        "atom2_number": atom2_number,
        "values": [float(value1), float(value2)],
        "occupancy": float(value1),
        "energy": float(value2),
        "principal_delocalizations": [{"number": number, "type": contrib_type} for number, contrib_type in contributions],
        'geminal_contributions': contribution_types['g'],
        'vicinal_contributions': contribution_types['v'],
        'remote_contributions': contribution_types['r'],
    }
    
    return result


def extract_nbo_summary_content(content: str):
    """
    Parse a Gaussian NBO output file and extract molecular unit information.
    """
    try:
        # find find all molecular unit declarations
        unit_declarations = re.findall(r'(Molecular unit\s+(\d+)\s+\((.*?)\))', content)
        
        # find charge unit declarations
        charge_declarations = re.findall(r'(Charge unit\s+\d+\s+[-+]?\d*\.\d+)', content)
        
        # unit info
        unit_info = {}
        
        # convert to list
        content_list = content.split("\n")
        
        # looping through each unit
        for m, unit in enumerate(unit_declarations):
            # check unit index
            for i, line in enumerate(content_list):
                line_ = line.strip()
                unit_ = unit[0].strip()
                # looping through each line
                if unit_ in line_:
                    # store the unit info
                    unit_info[unit[1]] = {
                        "unit_declaration": unit[0],
                        "unit_index": unit[1],
                        "unit_name": unit[2],
                        'start_line_index': i,
                        "unit_content": [],
                        "end_line_index": None,
                    }
                # end of unit
                end_line = charge_declarations[m]
                if end_line in line_:
                    unit_info[unit[1]]["end_line_index"] = i
        
        # extract unit content
        for unit in unit_info:
            start_line = unit_info[unit]["start_line_index"]
            end_line = unit_info[unit]["end_line_index"]
            # unit content
            content_ = content_list[start_line+1:end_line-6]
            # format content
            unit_info[unit]["unit_content"] = content_
            
            # Parse all NBO entries at once using the new bulk function
            unit_content_dict = {}
            n_parent = 0
            # looping through each line
            for n, line in enumerate(content_):
                # check if line contains NBO entry
                if re.match(r'^\s*\d+\.\s+', line):
                    # store the NBO entry
                    unit_content_dict[str(n)] = str(line).strip()
                    # increment parent
                    n_parent = str(n)
                else:
                    # append to the previous NBO entry
                    unit_content_dict[n_parent] += line
                    unit_content_dict[n_parent] = unit_content_dict[n_parent].strip()
            
            # format content (start from )
            unit_info[unit]["unit_content_dict"] = unit_content_dict
            
            # Parse NBO entries
            nbo_entries_dict = {}
            for key, value in unit_content_dict.items():
                nbo_entries_dict[key] = parse_nbo_entry(value)
            # save
            unit_info[unit]["nbo_entries_dict"] = nbo_entries_dict

            # summary
            summary_ = content_list[end_line-6:end_line+1]
            summary = summary_generator(summary_)
            unit_info[unit]["summary"] = summary
        
        # return
        return unit_info
        
    except Exception as e:
        print(f"An error occurred while extracting NBO summary content: {e}")
        return []
    

def summary_generator(summary_data):
    """  
    Generate summary for NBO entries.
    
    Parameters
    ----------
    summary_data : Dict
        NBO entries summary data
    """
    try:
        # clean summary data
        summary_data = [item.strip() for item in summary_data if item.strip()]
        
        # res
        summary_data_filtered = []
        
        # looping through each line
        for item in summary_data:
            # not started by letter
            if all(c =='-' for c in item.strip()):
                continue
            
            # save
            summary_data_filtered.append(item)
                
        return summary_data_filtered
    except Exception as e:
        raise Exception(f"An error occurred while generating summary: {e}")
    
    
def analyze_nbo_energy(molecule_unit):
    '''
    Analyze NBO energy to find the HOMO and LUMO
    
    Parameters
    ----------
    molecule_unit : Dict
        molecule unit info
    
    '''
    try:
        # nbo energies 
        nbo_energies = molecule_unit['1']['nbo_entries_dict']
        
        # Create a new dictionary sorted by the key 'energy' with keys starting from 0
        sorted_nbo_energies = {i: v for i, (k, v) in enumerate(sorted(nbo_energies.items(), key=lambda item: item[1]['energy']))}
        
        # Find all negative energy values
        negative_energies = [value for value in sorted_nbo_energies.values() if value['energy'] < 0]
        
        # Sort negative energies to find the one closest to zero
        if negative_energies:
            first_negative_energy = min(negative_energies, key=lambda x: abs(x['energy']))
        else:
            first_negative_energy = None
        
        # Get the top and bottom record of the first negative energy record
        if first_negative_energy:
            # find record in sorted ref
            key_ = [k for k, v in sorted_nbo_energies.items() if v['entry_number'] == first_negative_energy['entry_number']][0]
            # top record
            top_record = sorted_nbo_energies[key_ + 1]
            # bottom record
            bottom_record = sorted_nbo_energies[key_ - 1]
        else:
            top_record = None
            bottom_record = None
        

        # analyze the NBO energy
        # orbital types:
        # - core (CR)
        # - valence | lone pair (LP)
        # - valence | bonding (BD)
        # - valence | antibonding (BD*)
        # - Rydberg (RY)
        # - Rydberg | antibonding (RY*)
        # - unfilled nonbonding | lone vacancy (LV)
        
        # Return the results
        return {
            "first_negative_energy": first_negative_energy,
            "top_record": top_record,
            "bottom_record": bottom_record
        }
        
    except Exception as e:
        raise Exception(f"An error occurred while analyzing NBO energy: {e}")


def parser(content: str):
    """
    Parse the NBO summary from the lines of a Gaussian output file.
    
    Parameters
    ----------
    lines : list[str]
        A list of lines from the NBO output file.
        
    Returns
    -------
    dict
        A dictionary containing the parsed NBO summary information.
    """
    try:
        # nbo summary
        nbo_summary = extract_nbo_summary_contents(content)
        
        # check
        if not nbo_summary:
            raise ValueError("No NBO summary found in the file.")
        
        # Parse and get units
        units = extract_nbo_summary_content(nbo_summary)
        return units
    except Exception as e:
        raise Exception(f"Error parsing NBO summary: {e}")


