from ex1 import full_name, is_mail

def test_is_mail() -> bool:
    """Fonction de test de la fonction is_mail()

    Returns:
        bool: True si tous les tests sont valides, False sinon
    """
    EMAIL_TO_TEST = {
        "bisgambiglia_paul@univ-corse.fr":(1,0),
        "bisgambiglia_paul@univ-corse.fr  ":(1,0),
        "bisgambiglia_paul@academie.univ-corse.fr":(1,0),
        "bisgambiglia_paul@academie.univ.corse.fr":(1,0),
        "@univ-corse.fr":(0,1),
        "ab@univ-corse.fr":(0,1),
        "bisgambiglia_paulOuniv-corse.fr":(0,2),
        "bisgambiglia_paul@.fr":(0,3),
        "bisgambiglia_paul@univ corse.fr":(0,3),
        "bisgambiglia_paul@univ-corsePOINTfr":(0,4)
    }
    nbr_test_valide = 0
    for value_to_test in EMAIL_TO_TEST.items():
        str_affichage = "Test : \"{}\", resultat attendu : {}, resultat obtenu : {}, reussit : ".format(value_to_test[0],value_to_test[1],str(is_mail(value_to_test[0])))
        if value_to_test[1] == is_mail(value_to_test[0]):
            str_affichage += "Oui"
            nbr_test_valide += 1
        else:
            str_affichage += "Non"
        print(str_affichage)

    if nbr_test_valide == len(EMAIL_TO_TEST):
        res = True
    else:
        res = False
    return res

# print (
#     test_is_mail()
# )

def test_full_name()-> bool:
    """Fonction de test de la fonction full_name()

    Returns:
        bool: True si tous les tests sont valides, False sinon
    """
    NAME_TO_TEST = {
        "Girard Malo":"GIRARD Malo",
        "girard malo":"GIRARD Malo",
        "GIRARD Malo":"GIRARD Malo",
        "Girard Malo Michel":"GIRARD Malo",
        " girard  malo   ":"GIRARD Malo"
    }
    nbr_test_valide = 0
    for value_to_test in NAME_TO_TEST.items():
        str_affichage = "Test : \"{}\", resultat attendu : {}, resultat obtenu : {}, reussit : ".format(value_to_test[0],value_to_test[1],str(full_name(value_to_test[0])))
        if value_to_test[1] == full_name(value_to_test[0]):
            str_affichage += "Oui"
            nbr_test_valide += 1
        else:
            str_affichage += "Non"
        print(str_affichage)

    if nbr_test_valide == len(NAME_TO_TEST):
        res = True
    else:
        res = False
    return res

print (
    test_full_name()
)