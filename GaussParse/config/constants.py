# GaussParse version
__version__ = "1.3.5"
# author
__author__ = "Sina Gilassi"
# app name
APP_NAME = 'GaussParse'
# app description
APP_DESCRIPTION = f'{APP_NAME} {__version__} is a python package to parse Gaussian output files.'


# periodic table dict
pt_dict = {'0': {'AtomicNumber': 1, 'Symbol': 'H'},
           '1': {'AtomicNumber': 2, 'Symbol': 'He'},
           '2': {'AtomicNumber': 3, 'Symbol': 'Li'},
           '3': {'AtomicNumber': 4, 'Symbol': 'Be'},
           '4': {'AtomicNumber': 5, 'Symbol': 'B'},
           '5': {'AtomicNumber': 6, 'Symbol': 'C'},
           '6': {'AtomicNumber': 7, 'Symbol': 'N'},
           '7': {'AtomicNumber': 8, 'Symbol': 'O'},
           '8': {'AtomicNumber': 9, 'Symbol': 'F'},
           '9': {'AtomicNumber': 10, 'Symbol': 'Ne'},
           '10': {'AtomicNumber': 11, 'Symbol': 'Na'},
           '11': {'AtomicNumber': 12, 'Symbol': 'Mg'},
           '12': {'AtomicNumber': 13, 'Symbol': 'Al'},
           '13': {'AtomicNumber': 14, 'Symbol': 'Si'},
           '14': {'AtomicNumber': 15, 'Symbol': 'P'},
           '15': {'AtomicNumber': 16, 'Symbol': 'S'},
           '16': {'AtomicNumber': 17, 'Symbol': 'Cl'},
           '17': {'AtomicNumber': 18, 'Symbol': 'Ar'},
           '18': {'AtomicNumber': 19, 'Symbol': 'K'},
           '19': {'AtomicNumber': 20, 'Symbol': 'Ca'},
           '20': {'AtomicNumber': 21, 'Symbol': 'Sc'},
           '21': {'AtomicNumber': 22, 'Symbol': 'Ti'},
           '22': {'AtomicNumber': 23, 'Symbol': 'V'},
           '23': {'AtomicNumber': 24, 'Symbol': 'Cr'},
           '24': {'AtomicNumber': 25, 'Symbol': 'Mn'},
           '25': {'AtomicNumber': 26, 'Symbol': 'Fe'},
           '26': {'AtomicNumber': 27, 'Symbol': 'Co'},
           '27': {'AtomicNumber': 28, 'Symbol': 'Ni'},
           '28': {'AtomicNumber': 29, 'Symbol': 'Cu'},
           '29': {'AtomicNumber': 30, 'Symbol': 'Zn'},
           '30': {'AtomicNumber': 31, 'Symbol': 'Ga'},
           '31': {'AtomicNumber': 32, 'Symbol': 'Ge'},
           '32': {'AtomicNumber': 33, 'Symbol': 'As'},
           '33': {'AtomicNumber': 34, 'Symbol': 'Se'},
           '34': {'AtomicNumber': 35, 'Symbol': 'Br'},
           '35': {'AtomicNumber': 36, 'Symbol': 'Kr'},
           '36': {'AtomicNumber': 37, 'Symbol': 'Rb'},
           '37': {'AtomicNumber': 38, 'Symbol': 'Sr'},
           '38': {'AtomicNumber': 39, 'Symbol': 'Y'},
           '39': {'AtomicNumber': 40, 'Symbol': 'Zr'},
           '40': {'AtomicNumber': 41, 'Symbol': 'Nb'},
           '41': {'AtomicNumber': 42, 'Symbol': 'Mo'},
           '42': {'AtomicNumber': 43, 'Symbol': 'Tc'},
           '43': {'AtomicNumber': 44, 'Symbol': 'Ru'},
           '44': {'AtomicNumber': 45, 'Symbol': 'Rh'},
           '45': {'AtomicNumber': 46, 'Symbol': 'Pd'},
           '46': {'AtomicNumber': 47, 'Symbol': 'Ag'},
           '47': {'AtomicNumber': 48, 'Symbol': 'Cd'},
           '48': {'AtomicNumber': 49, 'Symbol': 'In'},
           '49': {'AtomicNumber': 50, 'Symbol': 'Sn'},
           '50': {'AtomicNumber': 51, 'Symbol': 'Sb'},
           '51': {'AtomicNumber': 52, 'Symbol': 'Te'},
           '52': {'AtomicNumber': 53, 'Symbol': 'I'},
           '53': {'AtomicNumber': 54, 'Symbol': 'Xe'},
           '54': {'AtomicNumber': 55, 'Symbol': 'Cs'},
           '55': {'AtomicNumber': 56, 'Symbol': 'Ba'},
           '56': {'AtomicNumber': 57, 'Symbol': 'La'},
           '57': {'AtomicNumber': 58, 'Symbol': 'Ce'},
           '58': {'AtomicNumber': 59, 'Symbol': 'Pr'},
           '59': {'AtomicNumber': 60, 'Symbol': 'Nd'},
           '60': {'AtomicNumber': 61, 'Symbol': 'Pm'},
           '61': {'AtomicNumber': 62, 'Symbol': 'Sm'},
           '62': {'AtomicNumber': 63, 'Symbol': 'Eu'},
           '63': {'AtomicNumber': 64, 'Symbol': 'Gd'},
           '64': {'AtomicNumber': 65, 'Symbol': 'Tb'},
           '65': {'AtomicNumber': 66, 'Symbol': 'Dy'},
           '66': {'AtomicNumber': 67, 'Symbol': 'Ho'},
           '67': {'AtomicNumber': 68, 'Symbol': 'Er'},
           '68': {'AtomicNumber': 69, 'Symbol': 'Tm'},
           '69': {'AtomicNumber': 70, 'Symbol': 'Yb'},
           '70': {'AtomicNumber': 71, 'Symbol': 'Lu'},
           '71': {'AtomicNumber': 72, 'Symbol': 'Hf'},
           '72': {'AtomicNumber': 73, 'Symbol': 'Ta'},
           '73': {'AtomicNumber': 74, 'Symbol': 'W'},
           '74': {'AtomicNumber': 75, 'Symbol': 'Re'},
           '75': {'AtomicNumber': 76, 'Symbol': 'Os'},
           '76': {'AtomicNumber': 77, 'Symbol': 'Ir'},
           '77': {'AtomicNumber': 78, 'Symbol': 'Pt'},
           '78': {'AtomicNumber': 79, 'Symbol': 'Au'},
           '79': {'AtomicNumber': 80, 'Symbol': 'Hg'},
           '80': {'AtomicNumber': 81, 'Symbol': 'Tl'},
           '81': {'AtomicNumber': 82, 'Symbol': 'Pb'},
           '82': {'AtomicNumber': 83, 'Symbol': 'Bi'},
           '83': {'AtomicNumber': 84, 'Symbol': 'Po'},
           '84': {'AtomicNumber': 85, 'Symbol': 'At'},
           '85': {'AtomicNumber': 86, 'Symbol': 'Rn'},
           '86': {'AtomicNumber': 87, 'Symbol': 'Fr'},
           '87': {'AtomicNumber': 88, 'Symbol': 'Ra'},
           '88': {'AtomicNumber': 89, 'Symbol': 'Ac'},
           '89': {'AtomicNumber': 90, 'Symbol': 'Th'},
           '90': {'AtomicNumber': 91, 'Symbol': 'Pa'},
           '91': {'AtomicNumber': 92, 'Symbol': 'U'},
           '92': {'AtomicNumber': 93, 'Symbol': 'Np'},
           '93': {'AtomicNumber': 94, 'Symbol': 'Pu'},
           '94': {'AtomicNumber': 95, 'Symbol': 'Am'},
           '95': {'AtomicNumber': 96, 'Symbol': 'Cm'},
           '96': {'AtomicNumber': 97, 'Symbol': 'Bk'},
           '97': {'AtomicNumber': 98, 'Symbol': 'Cf'},
           '98': {'AtomicNumber': 99, 'Symbol': 'Es'},
           '99': {'AtomicNumber': 100, 'Symbol': 'Fm'},
           '100': {'AtomicNumber': 101, 'Symbol': 'Md'},
           '101': {'AtomicNumber': 102, 'Symbol': 'No'},
           '102': {'AtomicNumber': 103, 'Symbol': 'Lr'},
           '103': {'AtomicNumber': 104, 'Symbol': 'Rf'},
           '104': {'AtomicNumber': 105, 'Symbol': 'Db'},
           '105': {'AtomicNumber': 106, 'Symbol': 'Sg'},
           '106': {'AtomicNumber': 107, 'Symbol': 'Bh'},
           '107': {'AtomicNumber': 108, 'Symbol': 'Hs'},
           '108': {'AtomicNumber': 109, 'Symbol': 'Mt'},
           '109': {'AtomicNumber': 110, 'Symbol': 'Ds'},
           '110': {'AtomicNumber': 111, 'Symbol': 'Rg'},
           '111': {'AtomicNumber': 112, 'Symbol': 'Cn'},
           '112': {'AtomicNumber': 113, 'Symbol': 'Nh'},
           '113': {'AtomicNumber': 114, 'Symbol': 'Fl'},
           '114': {'AtomicNumber': 115, 'Symbol': 'Mc'},
           '115': {'AtomicNumber': 116, 'Symbol': 'Lv'},
           '116': {'AtomicNumber': 117, 'Symbol': 'Ts'},
           '117': {'AtomicNumber': 118, 'Symbol': 'Og'}}
