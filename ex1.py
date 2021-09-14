import re

def full_name(chaine:str) -> str:
    """Retourne le nom de famille tout en majuscule et le prenom avec la premiere lettre en majuscule

    Args:
        chaine (str): haine de caractère composée d'un nom et d'un prénom séparé d'un espace

    Returns:
        str: haine de caractère composée d'un nom et d'un prénom séparé d'un espace modifiée
    """
    flag = chaine.split(" ")
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

print(
    full_name(
        saisie_full_name()
    )
)
