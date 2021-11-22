def create_and_initialise_matrix(colonnes,lignes,valeur_initiale):
    #création d'une matrice contenant la valeur initiale dans toutes ses cases
    matrice=[0]*lignes
    for k in range(lignes):
        matrice[k]=[valeur_initiale]*colonnes
    return(matrice)

def create_game_board(valeur_initiale):
    #création d'un plateau de jeu
    plateau_de_jeu=create_and_initialise_matrix(11,11,valeur_initiale)
    liste_titres_lignes=[" ","A","B","C","D","E","F","G","H","I","J"]
    for index in range(11):
        plateau_de_jeu[0][index]=[index]                        #nommage des colonnes
        plateau_de_jeu[index][0]=[liste_titres_lignes[index]]   #nommage des lignes
    return plateau_de_jeu

def print_matrix(matrice):
    #affichage d'une matrice donnée en paramètre sous forme de tableau
    for index in range(len(matrice)):
        print(matrice[index])

def print_game_board(valeur_initiale):
    #affichage du plateau de jeu
    print_matrix(create_game_board(valeur_initiale))

def is_in_matrix(matrice,ligne,colonne):
    #fonction retournant un booléen si un point de coordonnées données est dans la matrice
    possible=True                       #on considère que c'est possible par défaut
    if ligne>=len(matrice):             #on dit que c'est faux si la ligne n'est pas dans la matrice
        possible=False                  
    if colonne>=len(matrice[0]):        #on dit que c'est faux si la colonne n'est pas dans la matrice
        possible=False
    return possible

def convertir_lettres_en_chiffres(lettre):
    #pour entrer une position sur une ligne on rentre une lettre mais le programme a besoin d'un chiffre,
    #cette fonction s'occupe de la conversion
    lettres = ['A','B','C','D','E','F','G','H','I','J']     #uniquement les lettres utiles pour notre programme
    chiffre=99                                              #chiffre hors de la matrice, sera rejeté par is_in_matrix si 'lettre' n'est pas dans 'lettres'
    for index in range(10):
        if lettre==lettres[index]:
            chiffre=(index+1)                               #on associe le chiffre correspondant à la lettre
    return chiffre

def enter_position(matrice):
    x=str(input("Ligne (A à J): "))
    y=int(input("Colonne (1 à 10): "))
    x=convertir_lettres_en_chiffres(x)
    while is_in_matrix(matrice,x,y)==False:
        print("Coordonnées incorrectes")
        x=str(input("Nouvelle ligne (A à J): "))
        y=int(input("Nouvelle colonne (1 à 10): "))
        x=convertir_lettres_en_chiffres(x)
    return (x,y)

def enter_orientation():
    orientation=str(input("Orientation : "))
    while (orientation != "H") and (orientation != "V"):
        orientation=str(input("Caractère incorrect, nouvelle orientation (H ou V) : "))
    return orientation

def demander_taille():
    taille=int(input("Taille : "))
    while (taille < 2) or (taille > 5):
        taille=int(input("Taille incorrecte, nouvelle taille (2 à 5) : "))
    return taille

def is_boat_position_valid(plateau_de_jeu,taille,x,y,orientation):
    position_valide=True
    if x == 0 or y == 0:
        position_valide=False
    if orientation=="H":
        if is_in_matrix(plateau_de_jeu,x,(y+taille-1))==False:
            position_valide=False
    if orientation=="V":
        if is_in_matrix(plateau_de_jeu,(x+taille-1),y)==False:
            position_valide=False
    if position_valide==True:
        for index in range(taille):
            if orientation=="H":
                if plateau_de_jeu[x][y+index]!=" ":
                    position_valide=False
            if orientation=="V":
                if plateau_de_jeu[x+index][y]!=" ":
                    position_valide=False
    return position_valide    
            
def insert_boat(plateau_de_jeu,taille,x,y,orientation,symbole):
    insertion_réussie=False
    if is_boat_position_valid(plateau_de_jeu,taille,x,y,orientation) == True:
        for index in range(taille):
            if orientation=="H":
                plateau_de_jeu[x][y+index]=symbole
            if orientation=="V":
                plateau_de_jeu[x+index][y]=symbole
        insertion_réussie=True
    else :
        print("Impossible d'insérer, position invalide")
    return insertion_réussie

def player_game_board_initialisation(plateau_de_jeu):
    bateaux_disponibles=["P","C","R","S","T"]
    tailles=[5,4,3,3,2]
    index_=0
    while index_<5:
        print("Insérer",bateaux_disponibles[index_])
        taille=tailles[index_]
        x,y=enter_position(plateau_de_jeu)
        orientation=enter_orientation()
        if insert_boat(plateau_de_jeu,taille,x,y,orientation,bateaux_disponibles[index_]):
            index_+=1
        print_matrix(plateau_de_jeu)
        





plateau_de_jeu=create_game_board(" ")
print_matrix(plateau_de_jeu)
player_game_board_initialisation(plateau_de_jeu)