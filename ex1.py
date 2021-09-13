import random
import statistics

def somme_in_range(L:list) -> float:
    """
    Retourne la somme des valeurs de la liste passée en paramètre
    """
    somme = 0
    for i in range(len(L)):
        somme = L[i] + somme
    return somme

def somme_in_list(L:list) -> float:
    """
    Retourne la somme des valeurs de la liste passée en paramètre
    """
    somme = 0
    for element in L:
        somme = element + somme
    return somme

def somme_while(L:list) -> float:
    """
    Retourne la somme des valeurs de la liste passée en paramètre
    """
    somme = 0
    i = 0
    while i < len(L):
        somme = somme + L[i]
        i +=1

def moyenne(L:list) -> float:
    """
    Retourne la moyenne des valeurs de la liste passée en paramètre
    """
    if L != []:
        return somme_in_range(L) / len(L)

def nb_sup(L:list,e:int) -> list:
    """
    Retourne une liste comprenant toutes les valeurs de la liste passée
    en paramètres superieur a l'entier passé en paramètres
    """
    res = []
    for element in L:
        if element > e:
            res.append(element)
    return res

def moy_sup(L:list,e:int) -> float:
    """
    Retourne la moyenne des valeurs de la liste passée
    en paramètres superieur a l'entier passé en paramètres
    """
    list_sup =  nb_sup(L,e)
    res = None
    if len(list_sup) > 0:
        somme = 0
        for element in list_sup:
            somme = somme + element
        res = somme / len(list_sup)
    return res

def val_max(L:list) -> object:
    """
    Retourne la valeur maximale d'une liste passée en paramètres
    """
    flag = 0
    for element in L:
        if flag < element:
            flag = element
    return flag

def ind_max(L):
    return L.index(val_max(L))

# def test():
#     """
#     fonction de test
#     """

#     # Moyenne

#     liste = []
#     for i in random.randint(3,8):
#         liste.append(random.randint(1,800))
#     if (moyenne(liste) == statistics.mean(liste)):
#         print("Test Reussit !")


#     # nb_sup

#     liste = []
#     superieur = random.randint(3,100)
#     for i in random.randint(3,8):
#         randomnbr = random.randint(1,800)
#         if
#         liste.append()
#     if (nb_sup(liste) == max(liste)):
#         print("Test Reussit !")


#     # moy_sup

#     # val_max

#     # ind_max




# test()