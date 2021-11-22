def create_and_initialise_matrix(colonnes,lignes,valeur_initiale):              #création d'une matrice contenant la valeur initiale dans toutes ses cases
    matrice=[0]*lignes
    for k in range(lignes):
        matrice[k]=[valeur_initiale]*colonnes
    return(matrice)

def create_game_board(valeur_initiale):                                         #création d'un plateau de jeu
    plateau_de_jeu=create_and_initialise_matrix(11,11,valeur_initiale)
    liste_titres_lignes=[" ","A","B","C","D","E","F","G","H","I","J"]
    for index in range(11):
        plateau_de_jeu[0][index]=[index]                                        #nommage des colonnes
        plateau_de_jeu[index][0]=[liste_titres_lignes[index]]                   #nommage des lignes
    return plateau_de_jeu

def print_matrix(matrice):                                                      #affichage d'une matrice donnée en paramètre sous forme de tableau
    for index in range(len(matrice)):
        print(matrice[index])

def print_game_board(valeur_initiale):                                          #affichage du plateau de jeu
    print_matrix(create_game_board(valeur_initiale))

def is_in_matrix(matrice,ligne,colonne):                                        #fonction retournant un booléen si un point de coordonnées données est dans la matrice
    in_matrix=True                                                              #on crée une variable à return, vraie s'il n'y a pas de problèmes
    if ligne>=len(matrice):                                                     #on assigne faux à notre variable si la ligne n'est pas dans la matrice
        in_matrix=False                  
    if colonne>=len(matrice[0]):                                                #on assigne faux à notre variable si la colonne n'est pas dans la matrice
        in_matrix=False
    return in_matrix

def convertir_lettres_en_chiffres(lettre):                                      #pour entrer une position sur une ligne on rentre une lettre mais le programme a besoin d'un chiffre, cette fonction s'occupe de la conversion
    lettres = ['A','B','C','D','E','F','G','H','I','J']                         #uniquement les lettres utiles pour notre programme
    chiffre=99                                                                  #chiffre hors de la matrice, sera rejeté par is_in_matrix si 'lettre' n'est pas dans 'lettres'
    for index in range(10):
        if lettre==lettres[index]:                                              #on vérifie si la lettre est dans notre liste de lettres utiles
            chiffre=(index+1)                                                   #on associe le chiffre correspondant à la lettre
    return chiffre

def enter_position(matrice):                                                    #fonction demandant où ajouter un bateau, et vérifiant via is_in_matrix si c'est correct
    x=str(input("Ligne (A à J): "))
    y=int(input("Colonne (1 à 10): "))
    x=convertir_lettres_en_chiffres(x)                                          #conversion de la lettre en chiffre
    while is_in_matrix(matrice,x,y)==False:                                     #tant que la position est invalide, on redemande des coordonnées
        print("Coordonnées incorrectes")
        x=str(input("Nouvelle ligne (A à J): "))
        y=int(input("Nouvelle colonne (1 à 10): "))
        x=convertir_lettres_en_chiffres(x)
    return (x,y)

def enter_orientation():                                                        #fonction demandant l'orientation, et vérifiant via is_in_matrix si elle est correcte
    orientation=str(input("Orientation : "))
    while (orientation != "H") and (orientation != "V"):                        #tant que l'orientation est invalide, on redemande
        orientation=str(input("Caractère incorrect, nouvelle orientation (H ou V) : "))
    return orientation

def demander_taille():                                                          #fonction demandant la taille du bateau et vérifiant qu'elle est correcte
    taille=int(input("Taille : "))
    while (taille < 2) or (taille > 5):                                         #tant que la taille est invalide, on redemande
        taille=int(input("Taille incorrecte, nouvelle taille (2 à 5) : "))
    return taille

def is_boat_position_valid(plateau_de_jeu,taille,x,y,orientation):              #fontion vérifiant que le positionnement d'un bateau est possible
    position_valide=True                                                        #on considère que c'est possible par défaut
    if x == 0 or y == 0:                                                        #sur la première ligne ou colonne c'est impossible
        position_valide=False
    if orientation=="H":                                                        #si il dépasse la taille du plateau c'est impossible
        if is_in_matrix(plateau_de_jeu,x,(y+taille-1))==False:
            position_valide=False
    if orientation=="V":                                                        #si il dépasse la taille du plateau c'est impossible
        if is_in_matrix(plateau_de_jeu,(x+taille-1),y)==False:
            position_valide=False
    if position_valide==True:                                                   #si toutefois la position est valide, on vérifie si les cases sont vides
        for index in range(taille):
            if orientation=="H":
                if plateau_de_jeu[x][y+index]!=" ":
                    position_valide=False
            if orientation=="V":
                if plateau_de_jeu[x+index][y]!=" ":
                    position_valide=False
    return position_valide    
            
def insert_boat(plateau_de_jeu,taille,x,y,orientation,symbole):                 #fonction permettant d'insérer le bateau dans le plateau, si sa position est valide
    insertion_réussie=False                                                     #on considère que ça n'est pas possible par défaut
    if is_boat_position_valid(plateau_de_jeu,taille,x,y,orientation) == True:   #si is_boat_position_valid est vraie alors on peut le placer
        for index in range(taille):                                             #on remplit les cases avec le symbole du bateau
            if orientation=="H":
                plateau_de_jeu[x][y+index]=symbole
            if orientation=="V":
                plateau_de_jeu[x+index][y]=symbole
        insertion_réussie=True
    else :                                                                      #sinon on informe que c'est impossible
        print("Impossible d'insérer, position invalide")
    return insertion_réussie

def player_game_board_initialisation(plateau_de_jeu):                           #fonction qui demande au joueur où souhaite-t-il placer ses bateaux
    print_matrix(plateau_de_jeu)                                                #on affiche le plateau de jeu vierge
    bateaux_disponibles=["P","C","R","S","T"]
    tailles=[5,4,3,3,2]
    pointeur=0                                                                  #le pointeur permet de parcourir les deux listes
    while pointeur<5:                                                           #la boucle tournera tant que tous les bateaux ne sont pas positionnés
        print("Insérer",bateaux_disponibles[pointeur])
        x,y=enter_position(plateau_de_jeu)
        orientation=enter_orientation()
        if insert_boat(plateau_de_jeu,tailles[pointeur],x,y,orientation,bateaux_disponibles[pointeur]):     #on execute la fonction qui insère un bateau en récupérant sa sortie
            pointeur+=1                                                         #si cette sortie est validée, le bateau est inséré, et on passe au suivant
        print_matrix(plateau_de_jeu)                                            #on affiche le plateau de jeu actualisé
        


#programme principal

plateau_de_jeu=create_game_board(" ")
player_game_board_initialisation(plateau_de_jeu)
