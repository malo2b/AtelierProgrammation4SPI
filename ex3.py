import random
import re

def places_lettre(caractere: str,mot: str) -> list:
    """recherche si un caractere est present dans le mot

    Args:
        caractere (str): caractere a rechercher
        mot (str):mot dont l'ont cherches le ou les caracteres

    Returns:
        list: []si caractere pas present sinon l'index d'ou il se situe
        """

    liste_de_caractere = []
    for index in range(len(mot)):
        if(mot[index] == caractere):
            liste_de_caractere.append(index)
    return liste_de_caractere

def outputStr(mot:str, lpos:list)-> str:
    """Retourne une chaine de caractère avec les lettres masquées selon la liste lpos passée en paramètres

    Args:
        mot (str): chaine de caractère a modifier
        lpos (list): liste contenant les indices des caractères a modifier

    Returns:
        str: chaine de caractère modifiée
    """
    liste_retour = []
    for _ in mot:
        liste_retour.append("-")
    for position_lettre in lpos:
        liste_retour[position_lettre] = mot[position_lettre]
    return "".join(liste_retour)

def run_game():
    liste_de_mots = build_list("capitales.txt")
    nombre_de_coup = 0
    nombre_de_coup_maximum = 5
    longueur_mot = 0
    print("Difficulté 1 : mot -7 lettres")
    print("Difficulté 2 : mot entre 6 et 9 lettres")
    print("Difficulté 3 : mot plsu de 9 lettres")
    while True:
        try:
            difficulte = int(input("Veuillez saisie votre niveau de difficulté : "))
            if difficulte == 1 or difficulte == 2 or difficulte == 3:
                break
            else:
                print("Veuillez faire une saisie valide")
        except ValueError:
            print("Veuillez faire une saisie valide")

    if(difficulte == 1):
       longueur_mot = 6
    elif(difficulte == 2):
        longueur_mot = random.randint(6,9)
    else:
        longueur_mot = 9

    mot_choisis = select_word(build_dict(liste_de_mots),longueur_mot)
    caractere_present = ["-"] * len(mot_choisis)
    caractere_present[0]= mot_choisis[0]
    retour_outputStr = outputStr(mot_choisis,[])
    jeu_en_cours = True
    print(outputStr(mot_choisis,[0]))
    dessin = ["|______","|/ \ ","| T ","| O ","|---] "]
    index_deja_tomber = [0]
    while(nombre_de_coup<nombre_de_coup_maximum and jeu_en_cours):
        # Saisie utilisateur
        caractere_saisie = ""
        while re.match("[a-z]{1}",caractere_saisie.lower()) == None:
            try:
                caractere_saisie = input("Entrez une lettre : ")
            except ValueError:
                print("Veuillez faire une saisie valide")
        # Recherche et affichage lettres manquantes
        retour_places_lettre = places_lettre(caractere_saisie,mot_choisis)
        if retour_places_lettre!= []:
            for index in retour_places_lettre:
                caractere_present[index] = mot_choisis[index]
                index_deja_tomber.append(index)
        retour_outputStr = outputStr(mot_choisis,index_deja_tomber)
        print(retour_outputStr)

        # Affichage du dessin et nombre de coups restants
        if(nombre_de_coup>=1 and retour_places_lettre == []):
            for index in range(nombre_de_coup,-1,-1):
                print(dessin[index])
            nombre_de_coup+=1
        elif nombre_de_coup==0 and retour_places_lettre == [] :
            print(dessin[nombre_de_coup])
            nombre_de_coup+=1
        if(mot_choisis == "".join(caractere_present)):
            jeu_en_cours = False
            print("FIN DU JEU BRAVO VOUS AVEZ GAGNER")
        elif nombre_de_coup_maximum-nombre_de_coup == 0:
            print("FIN DU JEU Vous avez perdu !")
            print("Le mot a trouver était {}".format(mot_choisis))
        else:
            print("il vous reste {} coups".format(nombre_de_coup_maximum-nombre_de_coup))


def build_list(file_name:str):
    with open(file_name, "r",encoding="UTF-8") as fichier:
        liste_retour = fichier.read().split("\n")
    fichier.close()
    return liste_retour

def build_dict(lst:list)->dict:
    dictionnaire_de_mot = {}
    for value in lst:
        if not len(value) in dictionnaire_de_mot:
            dictionnaire_de_mot[len(value)] = [value]
        else:
            dictionnaire_de_mot[len(value)].append(value)
    return dictionnaire_de_mot

def select_word(sorted_words:dict, word_len:int)->str:
    a= 0
    nombre_alea = random.randint(0,len(sorted_words[word_len]))
    return sorted_words[word_len][nombre_alea]
run_game()