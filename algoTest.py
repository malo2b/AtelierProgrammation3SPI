import random

def plusoumoins(min, max):
    """
    Jeu du plus ou moins
    """
    
    nbrAleatoire = random.randint(min,max)
    finDuJeu = False
    nbrCoups = 0
    saisie = None
            
    while not finDuJeu and nbrCoups < 10:
        while True:
            try:
                saisie = int(input("Veuillez saisir un nombre entre {} et {} : ".format(min,max)))
                break
            except ValueError:
                print("Veuillez faire une saisie valide")
                
        if saisie > nbrAleatoire:
            print("Trop grand !")
        elif saisie < nbrAleatoire:
            print("Trop petit !")            
        else:
            print("Tu as gagné en {} coups !".format(nbrCoups + 1))
            finDuJeu = True
        
        nbrCoups = nbrCoups + 1

    if (nbrCoups > 10):
        print("Perdu !")

plusoumoins(0, 10)