from random import *

# fct qui va afficher l'interface du jeu
def afficher(tab):
    print("--- Début --\n")
    for line in tab:
        for col in line:
            print(col, end=" | ")
        print("\n")
    print("--- Fin ---\n\n")

    
# fct qui verifie si les croix ont gagnés  
def verifC(tmp) :
    if tmp[0][0] == 1 and tmp[0][1] == 1 and tmp[0][2] == 1: # ligne 1
        return True
    elif tmp[0][0] == 1 and tmp[1][0] == 1 and tmp[2] [0] == 1: # colonne 1
        return True
    elif tmp[1][0] == 1 and tmp[1][1] == 1 and tmp[1] [2] == 1: # ligne 2
        return True
    elif tmp[0][1] == 1 and tmp[1][1] == 1 and tmp[2] [1] == 1: # colonne 2
        return True
    elif tmp[2][0] == 1 and tmp[2] [1] == 1 and tmp[2] [2]== 1: # ligne 3
        return True
    elif tmp[0][2] == 1 and tmp[1] [2] == 1 and tmp[2] [2]== 1: # colonne 3
        return True
    elif tmp[0][0] == 1 and tmp[1] [1] == 1 and tmp[2] [2] == 1: # diagonale droite
        return True
    elif tmp[0][2] == 0 and tmp[1][1] == 0 and tmp[2][0] == 0 : # diagonale gauche
        return True
    else:
        return False

    
# fct qui verifie si les ronds ont gagnés
def verifR(tmp) :
    if tmp[0][0] == 0 and tmp[0][1]== 0 and tmp[0][2] == 0 : # ligne 1
        return True
    elif tmp[0][0] == 0 and tmp[1][0] == 0 and tmp[2] [0] == 0 : # colonne 1
        return True
    elif tmp[1][0] == 0 and tmp[1][1] == 0 and tmp[1] [2] == 0: # ligne 2
        return True
    elif tmp[0][1] == 0 and tmp[1][1] == 0 and tmp[2] [1] == 0 : # colonne 2
        return True
    elif tmp[2][0] == 0 and tmp[2] [1] == 0 and tmp[2] [2] == 0 : # ligne 3
        return True
    elif tmp[0][2]== 0 and tmp[1] [2]== 0 and tmp[2] [2] == 0 : # colonne 3
        return True
    elif tmp[0][0] == 0 and tmp[1][1] == 0 and tmp[2][2] == 0 : # diagonale droite
        return True
    elif tmp[0][2] == 0 and tmp[1][1] == 0 and tmp[2][0] == 0 : # diagonale gauche
        return True
    else:
        return False

# fct qui va determiner si une partie est gagné ou pas 
def peutJouer(tmp, tab):
    if verifR(tmp):
        afficher(tab)
        print("Les Ronds ont gagnés ! Félicitations ^_^ ")
        return False
    if verifC(tmp):
        afficher(tab)
        print("Les Croix ont gagnés ! Félicitations ^_^ ")
        return False
    # on verifie si le tableau n'est pas déjà remplie
    else:
        for line in tmp :
            for col in line:
                if col == -1:
                    return True
        return False

# fct qui va gerer le tour de la machine pendant une partie
def ordiJouer(tmp, equipe):
    # index de ligne
    i = randint(0,2)
    #index de colonne
    j = randint(0,2)
    # tant que les index tirés aletoirement donne une non libre on tire aleatoirement d'autres index
    while tmp[i][j] != -1:
        i = randint(0,2)
        j = randint(0,2)
    # on modifie le tableau de jeu
    if equipe == 'O':
        tmp[i][j] = 1
    else:
        tmp[i][j] = 0
    return tmp, i, j


# fct principale qui va derouler le jeu
def jouer(tab):
    
    motif = ' ' # variable pour l'equipe du joueur
    ordi = ' ' # variable pour l'equipe de la machine
    tmp = [[-1 for j in range(3)] for j in range(3)] # initilisation du tableau qui va servir a determiner le denouement du jeu
    
    choix = randint(0,1) # choix aléatoire de l'equipe du joueur 0 pour les ronds et 1 pour les croix
    if choix == 0 :
        motif = 'O' 
        ordi = 'X' 
        print("Vous êtes dans l'équipe des RONDS." ) 
    else:
        motif = 'X' 
        ordi = 'O' 
        print("Vous êtes dans l'équipe des CROIX." ) 

    # tant qu'on peut jouer on demandera au joueur les index
    while peutJouer(tmp,tab) :
        
        afficher(tab) # affichage de l'interface
        
        i = int(input("Saisie le numéro de ligne (entre 1 et 3) : "))  # on demande au joueur l'index de ligne
        j = int(input("Saisie le numéro de colonne (entre 1 et 3) : ")) # on demande au joueur l'index de colonne
        
        if (1 <= i and i <= 3) and (1 <= j and j <= 3) : # verifie si les index de lignes et colonnes saisie sont juste
            if tmp[i-1][j-1] == - 1: # verifie si la case donnée est libre, si c'est le cas on met à jour l'interface du jeu
                tmp[i-1][j-1] = choix
                tab[i-1][j-1]= motif
                if peutJouer(tmp,tab): # si le joueur n'a pas gagné la machine peut jouer à son tour
                    tmp, i2, j2 = ordiJouer(tmp, motif) 
                    tab[i2][j2] = ordi
            else :
                print("Vous avez choisie une case non libre. Choissisez une case avec un point (libre) !")
        else :
         print("Votre numéro de ligne et colonne doit être compris entre 1 et 3 !")
         
    if peutJouer(tmp,tab):
        afficher(tab)
        print("Fin de partie ! ")
    
   

# main
run = 1
while run:
    
    tab = [['.' for j in range(3)]for i in range(3)] # interface de jeu
    jouer(tab) # lancement d'une partie
    run = int(input("Vous voulez rejouer une nouvelle partie ? ( 1 pour oui ou 0 pour non) : "))
    if run == 0:
        break
    while run != 1 and run != 0:
        run = int(input("Saisisez 1 pour oui ou 0 pour non : "))
    
