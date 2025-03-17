# import libs
import re


def parser(lines: list[str]) -> dict:
    """
    Extract the Second Order Perturbation Theory content from an NBO log file.

    This function parses NBO log files to extract Second Order Perturbation Theory
    analysis data, which shows donor-acceptor interactions between filled and empty orbitals.
    The function identifies different sections (within unit 1, from unit 1 to unit 2, etc.)
    and extracts detailed information about each interaction, including orbital types,
    atoms involved, and energetic data.

    Parameters
    ----------
    lines (list[str]): List of lines from the NBO log file.

    Returns
    -------
    dict: A dictionary with sections as keys and lists of interactions as values.
        Each interaction is a dictionary with donor, acceptor, and energy values.
    """
    # check
    if not lines:
        raise ValueError("No lines provided for parsing.")

    # Initialize variables
    section_started = False
    current_section = None
    sections = {}

    # Pattern to identify section headers (within unit X or from unit X to unit Y)
    section_pattern = re.compile(
        r"^\s*((?:within|from)\s+unit\s+\d+(?:\s+to\s+unit\s+\d+)?)"
    )

    # Donor pattern:
    donor_pattern = re.compile(
        r"(\d+)\.?\s*([A-Z]{2}\*?)\*?\s*\(\s*(\d+)\s*\)\s+([A-Z][a-z]*)\s+(\d+)(?:\s+-\s+([A-Z][a-z]*)\s+(\d+))?"
    )

    # Acceptor pattern:
    acceptor_pattern = re.compile(
        r"(?:/)(\d+)\.?\s*([A-Z]{2}\*?)\*?\s*\(\s*(\d+)\s*\)\s+([A-Z][a-z]*)\s+(\d+)(?:\s+-\s+([A-Z][a-z]*)\s+(\d+))?"
    )

    # Energy pattern: three floating point numbers for E(2), E(j)-E(i), and F(i,j)
    # 0.92    1.53    0.034
    energy_pattern = re.compile(r"\s*(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*$")

    # Extract the Second Order Perturbation Theory content
    try:
        # Iterate through lines to find the relevant section
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1

            # Check if we've reached the start of the section
            if (
                not section_started
                and "Second Order Perturbation Theory Analysis of Fock Matrix in NBO Basis"
                in line
            ):
                section_started = True
                # Set default section if no specific section is found
                if not current_section:
                    current_section = "default"
                    sections[current_section] = []
                continue

            # Skip lines until we reach the actual content
            if (
                section_started
                and "===================================================================================================="
                in line
            ):
                continue

            # Check if we've reached the end of the section (two consecutive empty lines)
            if section_started and line == "":
                if i < len(lines):
                    next_line = lines[i].strip()
                    if next_line == "":
                        break
                    else:
                        line = next_line
                        i += 1

            # Skip header lines
            if section_started and (
                "Threshold for printing" in line
                or "Intermolecular threshold" in line
                or "Donor NBO" in line
                or "E(2)" in line
                or not line
            ):
                continue
            
            # Check for section headers (within unit X or from unit X to unit Y)
            if section_started:
                section_match = section_pattern.match(line)
                if section_match:
                    current_section = section_match.group(1)
                    sections[current_section] = []
                    continue
            
            # If we've started but haven't found a section yet, use a default section
            if section_started and not current_section:
                current_section = "default"
                sections[current_section] = []
            
            # Try to parse interaction lines
            # Ensure line has content and we have a valid section
            if section_started and current_section and len(line.strip()) > 10:
                try:
                    # Apply the three patterns to extract donor, acceptor, and energy data
                    donor_match = donor_pattern.match(line)

                    if donor_match:
                        # NOTE: Extract donor information
                        # SECTION: 18. BD (   1) C   7 - C   9
                        (
                            donor_num,
                            donor_type,
                            donor_index,
                            donor_atom_1_symbol,
                            donor_atom_1_index,
                            donor_atom_2_symbol,
                            donor_atom_2_index,
                        ) = donor_match.groups()

                        # Extract remaining portion of the line after donor match
                        remaining_text = line[donor_match.end() :].strip()

                        # NOTE: Try to match acceptor pattern
                        # SECTION: /810. BD*(   1) C   1 - C   3 (always begins with /)
                        acceptor_match = acceptor_pattern.match(remaining_text)

                        if acceptor_match:
                            # Extract acceptor information
                            (
                                acceptor_num,
                                acceptor_type,
                                acceptor_index,
                                acceptor_atom_1_symbol,
                                acceptor_atom_1_index,
                                acceptor_atom_2_symbol,
                                acceptor_atom_2_index,
                            ) = acceptor_match.groups()

                            # NOTE: Extract energy data
                            # SECTION: Extract remaining portion for energy data
                            energy_text = remaining_text[
                                acceptor_match.end() :
                            ].strip()

                            # Match energy pattern
                            energy_match = energy_pattern.match(energy_text)

                            if energy_match:
                                # Extract energy values
                                e2, energy_diff, f_ij = energy_match.groups()
                            else:
                                # Skip lines that don't match the energy pattern
                                continue
                    else:
                        # Skip lines that don't match the donor pattern
                        continue

                    try:
                        # Validate and convert numeric values
                        donor_num = int(donor_num)
                        donor_index = int(donor_index)
                        acceptor_num = int(acceptor_num)
                        acceptor_index = int(acceptor_index)
                        e2 = float(e2)
                        energy_diff = float(energy_diff)
                        f_ij = float(f_ij)

                    except (ValueError, TypeError) as e:
                        # Skip entries with invalid numeric values
                        print(
                            f"Warning: Invalid numeric value in line: {line.strip()}"
                        )
                        print(f"Error details: {str(e)}")
                        continue

                    interaction = {
                        "donor_num": donor_num,
                        "donor_type": donor_type,
                        "donor_index": donor_index,
                        "donor_atom_1_symbol": donor_atom_1_symbol,
                        "donor_atom_1_index": donor_atom_1_index,
                        "donor_atom_2_symbol": donor_atom_2_symbol,
                        "donor_atom_2_index": donor_atom_2_index,
                        "acceptor_num": acceptor_num,
                        "acceptor_type": acceptor_type,
                        "acceptor_index": acceptor_index,
                        "acceptor_atom_1_symbol": acceptor_atom_1_symbol,
                        "acceptor_atom_1_index": acceptor_atom_1_index,
                        "acceptor_atom_2_symbol": acceptor_atom_2_symbol,
                        "acceptor_atom_2_index": acceptor_atom_2_index,
                        "e2": e2,  # Stabilization energy in kcal/mol
                        # E(j)-E(i) in a.u.
                        "energy_diff": energy_diff,
                        "f_ij": f_ij,  # Fock matrix element in a.u.
                    }

                    # NOTE: Append the interaction to the current section
                    sections[current_section].append(interaction)
                except Exception as e:
                    # Log the error but continue processing
                    print(f"Warning: Error processing line: {line.strip()}")
                    print(f"Error details: {str(e)}")
                    continue
    except Exception as e:
        raise ValueError(f"Error processing file: {str(e)}")

    # If no data was found, the section might not be in the file
    if not section_started:
        raise ValueError(
            "Second Order Perturbation Theory section not found in the file"
        )

    # If no sections were found but the section header was found, the format might be unexpected
    if section_started and not sections:
        raise ValueError(
            "Failed to parse Second Order Perturbation Theory section: unexpected format"
        )

    return sections
