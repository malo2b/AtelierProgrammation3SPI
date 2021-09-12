def histo(liste:list) -> list:
    """
    Fonction qui a partir d'une liste de valeur en paramètre,
    retourne les valeurs d'un histogramme avec en abscice l'index
    de l'élément et la quantité en ordonnée

    Args:
        liste (list): liste contenant série de nombre a analyser

    Returns:
        list: retourne une liste "histogramme" avec l'index en abscice et la quantité en ordonnée
    """
    
    liste_histo = []
    i = 0
    
    while i < max(liste):
        cptQuantite = 0
        for el in liste:
            if (el == i):
                cptQuantite+=1
        liste_histo.append(cptQuantite)
        i+=1
    return liste_histo
        
def est_injective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est injective et retourne un boolen 

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si injective, False sinon
    """
    
    res = True
    i = 0
    
    while i < len(liste) and res:
        if liste[i] > 1:
            res = False
        i += 1
    return res   
        
# print(
#     est_injective (
#         histo([3,0,6,7,4,2,1,5])
#     )
# )

def est_surjective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est surjective et retourne un boolen 

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si surjective, False sinon
    """

    res = True
    i = 0
    
    while i < len(liste) and res:
        if liste[i] < 1:
            res = False
        i += 1
    return res

# print(
#     est_surjective (
#         histo([3,0,6,7,4,2,1,5])
#     )
# )

def est_bijective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est bijective et retourne un boolen 

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si bijective, False sinon
    """

    return est_surjective(liste) and est_injective(liste) 

print(
    est_bijective(
        histo(
            [3,0,6,7,4,2,1,5]
        )
    )
)