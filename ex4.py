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
        
print(
    histo (
        [1,1,3,4]
    )
)