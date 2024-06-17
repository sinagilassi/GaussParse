

class EnergyUnit:
    '''
    energy unit converter
    '''

    def __init__(self, unit):
        self.unit = unit

    @staticmethod
    def hartree_to_kcal_per_mol(value):
        '''
        convert hartree to kcal/mol
        '''
        return value*627.5

    @staticmethod
    def kcal_per_mol_to_hartree(value):
        '''
        convert kcal/mol to hartree
        '''
        return value/627.5

    @staticmethod
    def hartree_to_kJ_per_mol(value):
        '''
        convert hartree to kJ/mol
        '''
        return value*2625.5

    @staticmethod
    def kJ_per_mol_to_hartree(value):
        '''
        convert kJ/mol to hartree
        '''
        return value/2625.5

    @staticmethod
    def hartree_to_eV(value):
        '''
        convert hartree to eV
        '''
        return value*27.211

    @staticmethod
    def eV_to_hartree(value):
        '''
        convert eV to hartree
        '''
        return value/27.211

    @staticmethod
    def hartree_to_inverse_cm(value):
        '''
        convert hartree to inverse cm
        '''
        return value*219474.6

    @staticmethod
    def inverse_cm_to_hartree(value):
        '''
        convert inverse cm to hartree
        '''
        return value/219474.6
