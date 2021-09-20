# coding: utf-8

import re

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

def commence_par(mot:str,prefixe:str)->bool: # Francois
    """ verifie si mot commence par le prefixe

    Args:
        mot (str): mot definit par utilisateur
        prefixe (str): prefixe definit par utilisateur

    Returns:
        bool: True si le prefixe est bon False sinon
    """
    regex = '^'+prefixe
    commence_bien_par = False
    if(re.match(regex,mot)!=None):
        commence_bien_par = True
    return commence_bien_par

def finit_par(mot:str,suffixe:str)->bool: # Francois
    """ verifie si mot commence par le prefixe

    Args:
        mot (str): mot definit par utilisateur
        suffixe (str): suffixe definit par utilisateur

    Returns:
        bool: True si le prefixe est bon False sinon
    """
    regex = suffixe+"$"
    finis_bien_par = False
    if(re.search(regex,mot)!=None):
        finis_bien_par = True
    return finis_bien_par


def finissent_par(liste_mots:list,suffixe:str) -> list: #Malo
    """Fonction qui retourne la liste des mots qui finissent par un suffixe passé en paramètre

    Args:
        liste_mots (list): Liste de mots dans laquelle effectuer la recherche
        suffixe (str): Chaine de fin a rechercher

    Returns:
        list: Liste des mots finissant par le suffixe
    """
    liste_de_retour = []
    for mot in liste_mots:
        if finit_par(mot,suffixe):
            liste_de_retour.append(mot)
    return liste_de_retour

def commencent_par(liste_mots:list,suffixe:str) -> list: # Malo
    """Fonction qui retourne la liste des mots qui commencent par un suffixe passé en paramètre

    Args:
        liste_mots (list): Liste de mots dans laquelle effectuer la recherche
        suffixe (str): Chaine de fin a rechercher

    Returns:
        list: Liste des mots finissant par le suffixe
    """
    liste_de_retour = []
    for mot in liste_mots:
        if commence_par(mot,suffixe):
            liste_de_retour.append(mot)
    return liste_de_retour


def liste_mots(lst_mot:list,prefixe:str,suffixe:str,nombre_caracteres:int)->list:
    """[summary]

    Args:
        lst_mot (list): [description]
        prefixe (str): [description]
        suffixe (str): [description]
        nombre_caracteres (int): [description]

    Returns:
        list: [description]
    """
    # liste_de_mots_present = mots_Nlettres(lst_mot,nombre_caracteres)
    # liste_de_mots_present = commencent_par(liste_de_mots_present,prefixe)
    # liste_de_mots_present = finissent_par(liste_de_mots_present,suffixe)

    return finissent_par(
        commencent_par(
            mots_Nlettres(lst_mot,nombre_caracteres),prefixe
            ),
    suffixe)

def dictionnaire(nom_fichier:str) -> list[str]:
    """Retourne la liste des mots contenu dans un fichier texte dont le nom est passé en paramètre

    Args:
        nom_fichier (str): Nom du fichier a lire

    Returns:
        list[str]: Liste des mots contenus dans le fichier
    """
    with open(nom_fichier, "r") as fichier:
        dictionnaire = fichier.read()
    fichier.close()
    return dictionnaire.split("\n")
