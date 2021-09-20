import re

def mot_correspondant(mot:str,motif:str)->bool:
    """[summary] verifie si un motif et present dans mot

    Args:
        mot (str):mot fournit
        motif (str): motif peux contenir des jokers (.)

    Returns:
        bool: True si motif present False sinon
    """
    correspond = False
    if re.match(motif,mot):
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
    index_return = -1
    for index in range(len(mot)):
        if lettre == mot[index]:
            index_return = index
    return index_return


def mot_possible(mot:str,lettres:str) -> bool:
    """Retourne un booleen en fonction de si un mot est réalisable a partir d'une liste delettre passée en paramètre

    Args:
        mot (str): Mot a composer
        lettres (str): Lettres pour composer le mot

    Returns:
        bool: True si le mot est composable, False sinon
    """
    occurence_lettre_alphabet = [0]*26 # Initialisation d'un tableau de 26 0 ou l'index des éléments correspond au numero de la lettre de l'alphabet
    res = True
    # Pour chacune des lettres, on incrémente le compteur associé dans le tableau
    for lettre in lettres:
        occurence_lettre_alphabet[ord(lettre)-ord("a")] += 1
    # Verification si mot est composable
    for lettre in mot:
        if occurence_lettre_alphabet[ord(lettre)-ord("a")] == 0:    # Lettre pas disponible resultat non composable
            res = False
        else:
            occurence_lettre_alphabet[ord(lettre)-ord("a")] -= 1    # Lettre dispo, décrémente le compteur associé
    return res

def mot_possible2(mot:str,lettres:str):
    """Retourne un booleen en fonction de si un mot est réalisable a partir d'une liste de lettre passée en paramètre

    Args:
        mot (str): Mot a composer
        lettres (str): Lettres pour composer le mot

    Returns:
        bool: True si le mot est composable, False sinon
    """
    res = True
    for lettre in mot:
        indice_lettre = presente(lettre,lettres)
        if indice_lettre != -1:
            lettres = lettres.replace(lettres[indice_lettre],'',1)
        else:
            res = False
    return res

def mots_Nlettres(liste_mots:list,nbr_lettres:int) -> list: # Malo
    """Retourne les mots parmis la liste en paramètre contenant le nombre de lettre passé en paramètre

    Args:
        liste_mots (list): Liste de mots dans laquelle effectuer la recherche
        nbr_lettres (int): Nombre de lettre

    Returns:
        list: Liste comprenant le nombre de lettres spécifiées
    """
    liste_de_retour = []
    for mot in liste_mots:
        if len(mot) == nbr_lettres:
            liste_de_retour.append(mot)
    return liste_de_retour

def dictionnaire(nom_fichier:str) -> list[str]:
    """
    Retourne une liste des mots contenus dans un fichier texte

    Args:
        nom_fichier (str): Nom du fichier a lire

    Returns:
        list[str]: Liste des mots contenus dans le fichier
    """
    with open(nom_fichier, "r",encoding="UTF-8") as fichier:
        liste_mots = fichier.read().lower()
    fichier.close()
    return liste_mots.split("\n")

def correspondance_caracteres_speciaux(caractere:str) -> str:
    TABLE_DE_CORRESPONDANCE = {
        "e":"éèêë",
        "i":"ìíîï",
        "a":"àáâãäå",
        "u":"ùúüû",
        "c":"ç",
        "o":"òõöôó",
        "y":"ýÿ",
        "":"-\xA0",
    }
    res = ""
    for lettre_a_correspondre in TABLE_DE_CORRESPONDANCE.items():
        if caractere in lettre_a_correspondre[1]:
            res = lettre_a_correspondre[0]
        elif ord(caractere) == 160: # Si caractere 160 (espace)
            caractere = ""
    if res == "":
        res = caractere
    return res

def mot_optimaux(dico:list,lettres:str)->list:
    """
    Args:
        dico (list):mots disponible en fonction de lettre
        lettres (str): permet de restreidre le nombre de mot

    Returns:
        list: mot disponible
    """
    mots_optimaux = []
    liste_mots = []
    i = 0
    while mots_optimaux == [] and len(lettres)-i >= 2:
        # Creation de la liste comprenant les mots
        for mot in dico:    # Pour chacun des mots du dictionnaire
            if len(mot) == len(lettres)-i:
                if re.search("([éèêëìíîïàáâãäåùúüûçòõöôóýÿ\xA0])+",mot) is not None: # Si caractère spéciaux
                    flag = ""
                    for lettre in mot: # Pour chacune des lettres du mot
                        if re.search("([éèêëìíîïàáâãäåùúüûçòõöôóýÿ\xA0])+",mot) is not None: # Si caractere spécial
                            flag += correspondance_caracteres_speciaux(lettre)   # Caractère transformé par la fonction
                        else:
                            flag += lettre
                    mot = flag
                liste_mots.append(mot)

        # Construction de la liste mots_optimaux
        for mot in liste_mots:
            if mot_possible(mot,lettres): # Si mot est possible
                if not mot in mots_optimaux:    # Verifie qu'il n'y ait pas 2 mots identiques
                    mots_optimaux.append(mot)

        i += 1

    return mots_optimaux

print(
    mot_optimaux(
        dictionnaire("dico.txt"),
        "tesfzfecbjzxbfjhezcjfhzehftats"
    )
)
