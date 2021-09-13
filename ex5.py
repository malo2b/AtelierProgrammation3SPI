def present(liste:list[int],element:int) -> bool:
    """
    Fonction qui verifie si un élément est présent dans une liste

    Args:
        Liste (list[int]): liste ou chercher l'element
        element (int): entier a chercher dans la liste

    Returns:
        bool: True si présent, False sinon
    """

    res = False
    i = 0
    taille_liste = len(liste)
    while i < taille_liste and not res:
        if liste[i] == element:
            res = True
        i += 1
    return res
