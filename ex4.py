import re

def mot_correspondant (mot:str,motif:str)->bool:
    """[summary] verifie si un motif et present dans mot

    Args:
        mot (str):mot fournit
        motif (str): motif peux contenir des jokers (.)

    Returns:
        bool: True si motif present False sinon
    """    
    correspond = False
    if(re.match(motif,mot)):
        correspond = True
    return correspond

def presente(lettre:str,mot:str)->int:
    """fonction verifiant si lettre et present dans mot

    Args:
        lettre (str): lettre rechercher
        mot (str): mot

    Returns:
        int: indice de la lettre
    """
    index_return = 0
    for index in range(len(mot)):
        if lettre == mot[index]:
            index_return = index
    return index_return


