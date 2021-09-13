def separer(liste:list) -> list:
    """
    Sépare les éléments de la liste passée en paramètre dans une deuxieme liste en regroupant
    les éléments entre négatifs, nuls et positifs

    Args:
        liste (list): liste en paramètre et a trier

    Returns:
        list: liste triée
    """

    liste_triee = []
    nbr_element_negatifs = 0

    for el in liste:
        if el < 0:
            liste_triee.insert(0,el)
            nbr_element_negatifs += 1
        elif el > 0:
            liste_triee.append(el)
        else:
            liste_triee.insert(nbr_element_negatifs,0)

    return liste_triee

print(
    separer(
        [1,2,6,-6,-4,0,0,42,0,0,9,-12,444,-72,-69,51]
    )
)