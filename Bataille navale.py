def create_and_initialise_matrix(colonnes,lignes,valeur_initiale):
    matrice=[0]*lignes
    for k in range(lignes):
        matrice[k]=[valeur_initiale]*colonnes
    return(matrice)

def create_game_board(valeur_initiale):
    plateau_de_jeu=create_and_initialise_matrix(11,11,valeur_initiale)
    #plateau_de_jeu[0][0]=" "
    liste_titres_colonnes=[" ","A","B","C","D","E","F","G","H","I","J"]
    for index in range(11):
        plateau_de_jeu[0][index]=[index]
        plateau_de_jeu[index][0]=[liste_titres_colonnes[index]]
    return plateau_de_jeu

def print_matrix(matrice):
    for index in range(len(matrice)):
        print(matrice[index])

def print_game_board(valeur_initiale):
    print_matrix(create_game_board(valeur_initiale))

def is_in_matrix(matrice,ligne,colonne):
    possible=True
    if ligne>=len(matrice):
        possible=False
    if colonne>=len(matrice[0]):
        possible=False
    return possible

def enter_position(matrice):
    x=int(input("Ligne : "))
    y=int(input("Colonne : "))
    while is_in_matrix(matrice,x,y)==False:
        print("Coordonnées incorrectes")
        x=int(input("Nouvelle ligne : "))
        y=int(input("Nouvelle colonne : "))
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
        if is_in_matrix(plateau_de_jeu,x,(y+taille))==False:
            position_valide=False
    if orientation=="V":
        if is_in_matrix(plateau_de_jeu,(x+taille),y)==False:
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
    if is_boat_position_valid(plateau_de_jeu,taille,x,y,orientation) == True:
        for index in range(taille):
            if orientation=="H":
                plateau_de_jeu[x][y+index]=symbole
            if orientation=="V":
                plateau_de_jeu[x+index][y]=symbole
    else :
        print("Impossible d'insérer, position invalide")

def player_game_board_initialisation(plateau_de_jeu):
    for i in range (5):
        bateaux_disponibles=["T","S","R","C","P"]
        taille=demander_taille()
        x,y=enter_position(plateau_de_jeu)
        orientation=enter_orientation()
        symbole=str(input("Nom du bateau : "))
        insert_boat(plateau_de_jeu,taille,x,y,orientation,symbole)
        print_matrix(plateau_de_jeu)



plateau_de_jeu=create_game_board(" ")
print_matrix(plateau_de_jeu)
player_game_board_initialisation(plateau_de_jeu)