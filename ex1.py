import re

def full_name(chaine:str) -> str:
    """Retourne le nom de famille tout en majuscule et le prenom avec la premiere lettre en majuscule

    Args:
        chaine (str): haine de caractère composée d'un nom et d'un prénom séparé d'un espace

    Returns:
        str: haine de caractère composée d'un nom et d'un prénom séparé d'un espace modifiée
    """
    flag = chaine.strip()
    flag = flag.split(" ")
    while '' in flag:
        flag.remove('')
    return flag[0].upper() + " " + flag[1].capitalize()

def saisie_full_name() -> str:
    """Fonction de saisie du nom et prenom respectant un bon format

    Returns:
        str: Chaine de caractère composée d'un nom et d'un prénom séparé d'un espace
    """
    while True:
        try:
            pattern = "^[a-zA-Z]{2,}[ ]{1}[a-zA-Z]{2,} *$"
            str_saisie = str(input("Veuillez saisir votre nom et prenom séparé d'un espace : "))
            if re.match(pattern,str_saisie):
                break
            else:
                print("Veuillez faire une saisie valide !")
        except ValueError:
            print("Veuillez faire une saisie valide !")
    return str_saisie

# print(
#     full_name(
#         saisie_full_name()
#     )
# )

def is_mail(chaine:str) -> tuple:
    """Fonction qui dis si un mail est valide et retourne un code d'erreur sinon

    Args:
        chaine (str): Chaine a verifier

    Returns:
        tuple: retourne un tuple composé d'une premiere valeur (1 si valide, 0 sinon)
                   et code d'erreur sinon
    """
    resultat = ()
    pattern_email = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    chaine = chaine.lower()
    if re.match(pattern_email,chaine): # Si email valide
        resultat = (1,0)
    else:
        if not re.match("^.*@{1}.*",chaine): # Si @ manquant
            resultat = (0,2)
        else:
            mail_split = chaine.split("@") # Sépare le corp du nom de domaine
            if not re.match("^[a-zA-Z0-9]{3,}([^ ][a-zA-Z0-9]{3,10})?$",mail_split[0]): # Verification du corp
               resultat = (0,1)
            elif re.match("[^.]",mail_split[1]):
                resultat = (0,4)
            elif not re.match("^[a-z0-9.-_]{3,15}[.][a-z0-9.-_]{2,10}",mail_split[1]):
                resultat = (0,3)
    return resultat
