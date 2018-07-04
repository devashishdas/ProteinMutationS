aa1 = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',	 'S', 'T', 'V', 'W', 'Y']

aa2 = ['ILE', 'GLN', 'GLY', 'GLU', 'CYS', 'ASP', 'SER', 'LYS', 'PRO', 'ASN', 'VAL', 'THR', 'HIS', 'TRP', 'PHE', 'ALA', 'MET', 'LEU', 'ARG', 'TYR']

aa1aa3 = {'A': 'ALA', 'C': 'CYS', 'E': 'GLU', 'D': 'ASP', 'G': 'GLY', 'F': 'PHE', 'I': 'ILE', 'H': 'HIS', 'K': 'LYS', 'M': 'MET', 'L': 'LEU', 'N': 'ASN', 'Q': 'GLN', 'P': 'PRO', 'S': 'SER', 'R': 'ARG', 'T': 'THR', 'W': 'TRP', 'V': 'VAL', 'Y': 'TYR', 'Z': 'GLX'}

aa3aa1 = {'ILE': 'I', 'GLN': 'Q', 'GLX': 'Z', 'GLY': 'G', 'GLU': 'E', 'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'LYS': 'K', 'PRO': 'P', 'ASX': 'B', 'ASN': 'N', 'VAL': 'V', 'THR': 'T', 'HIS': 'H', 'TRP': 'W', 'PHE': 'F', 'ALA': 'A', 'MET': 'M', 'LEU': 'L', 'ARG': 'R', 'TYR': 'Y'}



def getAllMut(MUT):
    if len(MUT) == 3:
        defaultList1 = [i for i in aa1 if aa3aa1[i] != MUT]
        defaultList3 = [i for i in aa3 if i != MUT]
    elif len(MUT) == 1:
        defaultList1 = [i for i in aa1 if i != MUT]
        defaultList3 = [i for i in aa3 if aa1aa3[i] != MUT]
    return defaultList1, defaultList3


 
