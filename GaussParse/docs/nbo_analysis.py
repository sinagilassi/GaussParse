#  ******************************Gaussian NBO Version 3.1******************************
#              N A T U R A L   A T O M I C   O R B I T A L   A N D
#           N A T U R A L   B O N D   O R B I T A L   A N A L Y S I S
#  ******************************Gaussian NBO Version 3.1******************************

# import libs
import os
from typing import Literal, Optional, Union, Any, Dict, List, Tuple
# path
from pathlib import Path


class NBOAnalysis:
    """
    Parser for Natural Bond Orbital (NBO) analysis outputs from Gaussian calculation.
    Extracts different sections from NBO analysis log files.
    """
    # extracted content
    _content: Dict[str, Tuple[str, List[str], Tuple[int, int]]] = {}

    # NOTE: these are the keywords used to identify sections in the NBO output
    NORMAL_TERMINATION = 'Normal termination of Gaussian'
    NATURAL_ATOMIC_ORBITAL_ACCUPACIES = 'NATURAL POPULATIONS:  Natural atomic orbital occupancies'
    SUMMARY_OF_NATURAL_POPULATION_ANALYSIS = 'Summary of Natural Population Analysis:'
    NATURAL_BOND_ORBITAL_ANALYSIS = 'NATURAL BOND ORBITAL ANALYSIS:'
    BOND_ORBITAL_COEFFICIENTS_HYBRIDS = '(Occupancy)   Bond orbital/ Coefficients/ Hybrids'
    NHO_DIRECTIONALITY_BOND_BENDING = 'NHO Directionality and "Bond Bending" (deviations from line of nuclear centers)'
    SECOND_ORDER_PERTURBATION_THEORY_ANALYSIS = 'Second Order Perturbation Theory Analysis of Fock Matrix in NBO Basis'
    NATURAL_BOND_ORBITALS_SUMMARY = 'Natural Bond Orbitals (Summary):'

    def __init__(self, file_path: Path | str):
        """
        Initialize the NBOAnalysis class with the path to the Gaussian log file.

        Parameters
        ----------
        file_path : Path | str
            Path to the Gaussian log file.
        """
        # file path
        self.file_path = file_path
        # load log file
        self.log_lines = self.log_loader()
        # extractor
        self.extractor()

    def extractor(self) -> None:
        """Extract NBO analysis content from the file."""
        # reset
        self._content: Dict[str, Tuple[str, List[str], Tuple[int, int]]] = {}
        # extract content
        check_ = self.check_normal_termination()

        # check
        if not check_:
            raise ValueError(
                "The Gaussian log file does not indicate normal termination.")

        # extract sections
        # SECTION: NATURAL POPULATIONS:  Natural atomic orbital occupancies
        self._content[self.NATURAL_ATOMIC_ORBITAL_ACCUPACIES] = self.extract_natural_atomic_orbital_occupancies()
        # SECTION: Summary of Natural Population Analysis:
        self._content[self.SUMMARY_OF_NATURAL_POPULATION_ANALYSIS] = self.extract_summary_of_natural_population_analysis()
        # SECTION: NATURAL BOND ORBITAL ANALYSIS
        self._content[self.NATURAL_BOND_ORBITAL_ANALYSIS] = self.extract_natural_bond_orbital_analysis()
        # SECTION: (Occupancy)   Bond orbital/ Coefficients/ Hybrids
        self._content[self.BOND_ORBITAL_COEFFICIENTS_HYBRIDS] = self.extract_bond_orbital_coefficients_hybrids()
        # SECTION: NHO Directionality and "Bond Bending" (deviations from line of nuclear centers)
        self._content[self.NHO_DIRECTIONALITY_BOND_BENDING] = self.extract_nho_directionality_bond_bending()
        # SECTION: Second Order Perturbation Theory Analysis of Fock Matrix in NBO Basis
        self._content[self.SECOND_ORDER_PERTURBATION_THEORY_ANALYSIS] = self.extract_second_order_perturbation_theory_analysis()
        # SECTION: Natural Bond Orbitals (Summary):
        self._content[self.NATURAL_BOND_ORBITALS_SUMMARY] = self.extract_natural_bond_orbitals_summary()

    def log_loader(self) -> List[str]:
        """
        Load the log file

        Parameters
        ----------
        None

        Returns
        -------
        lines : list
            List of lines in the log file.
        """
        # check path | str
        if isinstance(self.file_path, str):
            self.file_path = Path(self.file_path)

        # check file existence
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"The file {self.file_path} does not exist.")

        # check file extension
        if not self.file_path.suffix == '.log':
            raise ValueError(
                f"The file {self.file_path} is not a Gaussian log file.")

        # load file
        # NOTE: read lines
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        return lines

    def content_retriever(self, section: str) -> Tuple[str, List[str]] | None:
        """
        Retrieve the content of a specific section.

        Parameters
        ----------
        section : str
            The section to retrieve.

        Returns
        -------
        content : str | None
            The content of the section or None if not found.
        """
        return self._content.get(section, None)

    def extract_summary_of_natural_population_analysis(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """Summary of Natural Population Analysis"""
        # get log lines
        lines = self.log_lines

        summary_lines = []
        in_summary = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.SUMMARY_OF_NATURAL_POPULATION_ANALYSIS in line:
                # set
                in_summary = True
                start_index = lines.index(line)
            elif in_summary and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_summary:
                summary_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(summary_lines), summary_lines, (start_index, end_index)

    def extract_natural_atomic_orbital_occupancies(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """NATURAL POPULATIONS:  Natural atomic orbital occupancies"""
        # get log lines
        lines = self.log_lines

        occupancies_lines = []
        in_occupancies = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for i, line in enumerate(lines):
            if self.NATURAL_ATOMIC_ORBITAL_ACCUPACIES in line:
                # set
                in_occupancies = True
                start_index = i
            elif in_occupancies and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
                # append
                # NOTE: already found the section
                occupancies_lines.append(line)
            elif in_occupancies:
                occupancies_lines.append(line.strip())
                empty_line_count = 0
                end_index = i

        return '\n'.join(occupancies_lines), occupancies_lines, (start_index, end_index)

    def extract_natural_bond_orbital_analysis(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """NATURAL BOND ORBITAL ANALYSIS"""
        # get log lines
        lines = self.log_lines

        nbo_lines = []
        in_nbo = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.NATURAL_BOND_ORBITAL_ANALYSIS in line:
                in_nbo = True
                start_index = lines.index(line)
            elif in_nbo and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_nbo:
                nbo_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(nbo_lines), nbo_lines, (start_index, end_index)

    def extract_bond_orbital_coefficients_hybrids(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """(Occupancy)   Bond orbital/ Coefficients/ Hybrids"""
        # get log lines
        lines = self.log_lines

        bond_orbital_lines = []
        in_bond_orbital = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.BOND_ORBITAL_COEFFICIENTS_HYBRIDS in line:
                in_bond_orbital = True
                start_index = lines.index(line)
            elif in_bond_orbital and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_bond_orbital:
                bond_orbital_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(bond_orbital_lines), bond_orbital_lines, (start_index, end_index)

    def extract_nho_directionality_bond_bending(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """NHO Directionality and "Bond Bending" (deviations from line of nuclear centers)"""
        # get log lines
        lines = self.log_lines

        nho_lines = []
        in_nho = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.NHO_DIRECTIONALITY_BOND_BENDING in line:
                in_nho = True
                start_index = lines.index(line)
            elif in_nho and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_nho:
                nho_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(nho_lines), nho_lines, (start_index, end_index)

    def extract_second_order_perturbation_theory_analysis(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """Second Order Perturbation Theory Analysis of Fock Matrix in NBO Basis"""
        # get log lines
        lines = self.log_lines

        perturbation_lines = []
        in_perturbation = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.SECOND_ORDER_PERTURBATION_THEORY_ANALYSIS in line:
                # set
                in_perturbation = True
                start_index = lines.index(line)
                # append
                perturbation_lines.append(line.strip())
            elif in_perturbation and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_perturbation:
                perturbation_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(perturbation_lines), perturbation_lines, (start_index, end_index)

    def extract_natural_bond_orbitals_summary(self) -> Tuple[str, List[str], Tuple[int, int]]:
        """Natural Bond Orbitals (Summary):"""
        # get log lines
        lines = self.log_lines

        nbo_summary_lines = []
        in_nbo_summary = False
        empty_line_count = 0
        # index
        start_index = 0
        end_index = 0

        for line in lines:
            if self.NATURAL_BOND_ORBITALS_SUMMARY in line:
                # set
                in_nbo_summary = True
                start_index = lines.index(line)
                # append
                nbo_summary_lines.append(line.strip())
            elif in_nbo_summary and line.strip() == '':
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            elif in_nbo_summary:
                nbo_summary_lines.append(line.strip())
                empty_line_count = 0
                end_index = lines.index(line)

        return '\n'.join(nbo_summary_lines), nbo_summary_lines, (start_index, end_index)

    def check_normal_termination(self) -> bool:
        ''"Check if the Gaussian log file indicates normal termination."
        # get log lines
        lines = self.log_lines

        return self.NORMAL_TERMINATION in lines[-1]
