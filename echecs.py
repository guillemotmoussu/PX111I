###########constantes############
liste_pièces_noires=["T1_N","C1_N","F1_N","RE_N","RO_N","F2_N","C2_N","T2_N"]
liste_pions_noirs=["P1_N","P2_N","P3_N","P4_N","P5_N","P6_N","P7_N","P8_N"]
liste_pièces_blanches=["T1_B","C1_B","F1_B","RE_B","RO_B","F2_B","C2_B","T2_B"]
liste_pions_blancs=["P1_B","P2_B","P3_B","P4_B","P5_B","P6_B","P7_B","P8_B"]
#################################

def create_and_initialise_matrix(colonnes,lignes,valeur_initiale):
    matrice=[0]*lignes
    for k in range(lignes):
        matrice[k]=[valeur_initiale]*colonnes
    return(matrice)

def create_game_board():
    return create_and_initialise_matrix(8,8,"    ")

def initialise_game_board():
    plateau=create_game_board()
    plateau[0]=liste_pièces_blanches
    plateau[1]=liste_pions_blancs
    plateau[6]=liste_pions_noirs
    plateau[7]=liste_pièces_noires 
    return plateau   
        
def print_matrix(matrice):
    for index in range(len(matrice)):
        print(matrice[index])

def print_game_board(plateau,a_noir_de_jouer,pieces_prises_jnoir,pieces_prises_jblanc):
    print("Pièces prises par le joueur noir : ",pieces_prises_jnoir)
    print_matrix(plateau)
    print("Pièces prises par le joueur blanc : ",pieces_prises_jblanc)
    if a_noir_de_jouer==True:
        print("C'est au joueur noir de jouer")
    else:
        print("C'est au joueur blanc de jouer")

def is_in_matrix(matrice,ligne,colonne):
    in_matrix=True
    if ligne>=len(matrice):
        in_matrix=False
    if colonne>=len(matrice[0]):
        in_matrix=False
    return in_matrix

def is_position_valid(plateau,type_piece,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée):
    position_valide=is_in_matrix(plateau,x_arrivée,y_arrivée)
    if plateau[y_arrivée][x_arrivée][3]=="B" and a_noir_de_jouer==False:
        position_valide=False
    if plateau[y_arrivée][x_arrivée][3]=="N" and a_noir_de_jouer==True:
        position_valide=False
    if position_valide==True:
        if type_pièce==X:
            appel fonction
        elif...
    return position_valide

def is_position_valid_RO(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
   #ajouter roque
    if (x_arrivée==x_départ-1) and (y_arrivée!=y_départ+1 or y_arrivée!=y_départ or y_arrivée!=y_départ-1):
        position_valide=False
    if (x_arrivée==x_départ) and (y_arrivée!=y_départ+1 or y_arrivée!=y_départ-1):
        position_valide=False
    if (x_arrivée==x_départ+1) and (y_arrivée!=y_départ+1 or y_arrivée!=y_départ or y_arrivée!=y_départ-1):
        position_valide=False
    return position_valide

def is_position_valid_T(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
    if x_arrivée!=x_départ and y_arrivée!=y_départ:
        position_valide=False
    if x_arrivée<x_départ:
        for index in range (x_arrivée+1,x_départ-1):
            if plateau[y_départ][index]!="    ":
                position_valide=False
    if x_départ<x_arrivée:
        for index in range (x_départ+1,x_arrivée-1):
            if plateau[y_départ][index]!="    ":
                position_valide=False
    if y_arrivée<y_départ:
        for index in range (y_arrivée+1,y_départ-1):
            if plateau[index][x_départ]!="    ":
                position_valide=False
    if y_départ<y_arrivée:
        for index in range (y_départ+1,y_arrivée-1):
            if plateau[y_départ][index]!="    ":
                position_valide=False
    return position_valide

def is_position_valid_F(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
    if x_arrivée-x_départ!=y_arrivée-y_départ and x_arrivée-x_départ!=y_départ-y_arrivée:
        position_valide=False
    else:
        if is_in_matrix(plateau,x_arrivée,y_arrivée):
            if x_arrivée<x_départ and y_arrivée<y_départ:
                for index in range (x_arrivée+1,x_départ-1):
                    if plateau[index-x_arrivée+y_arrivée][index]!="    ":
                        position_valide=False
            if x_départ<x_arrivée and y_arrivée<y_départ:
                for index in range (x_départ+1,x_arrivée-1):
                    if plateau[index-x_départ+y_arrivée][index]!="    ":
                        position_valide=False
            if x_départ<x_arrivée and y_départ<y_arrivée:
                for index in range (x_départ+1,x_arrivée-1):
                    if plateau[index-x_départ+y_départ][index]!="    ":
                        position_valide=False
            if x_arrivée<x_départ and y_départ<y_arrivée:
                for index in range (x_arrivée+1,x_départ-1):
                    if plateau[index-x_arrivée+y_départ][index]!="    ":
                        position_valide=False
    return position_valide
    juuj
def is_position_valid_RE(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
    if type_piece=="RE":
        if x_arrivée-x_départ!=y_arrivée-y_départ and x_arrivée-x_départ!=y_départ-y_arrivée and x_arrivée!=x_départ and y_arrivée!=y_départ:
            position_valide=False
        else:
            if is_in_matrix(plateau,x_arrivée,y_arrivée):
                if x_arrivée<x_départ and y_arrivée<y_départ:
                    for index in range (x_arrivée+1,x_départ-1):
                        if plateau[index-x_arrivée+y_arrivée][index]!="    ":
                            position_valide=False
                if x_départ<x_arrivée and y_arrivée<y_départ:
                    for index in range (x_départ+1,x_arrivée-1):
                        if plateau[index-x_départ+y_arrivée][index]!="    ":
                            position_valide=False
                if x_départ<x_arrivée and y_départ<y_arrivée:
                    for index in range (x_départ+1,x_arrivée-1):
                        if plateau[index-x_départ+y_départ][index]!="    ":
                            position_valide=False
                if x_arrivée<x_départ and y_départ<y_arrivée:
                    for index in range (x_arrivée+1,x_départ-1):
                        if plateau[index-x_arrivée+y_départ][index]!="    ":
                            position_valide=False
                if x_arrivée<x_départ and y_départ==y_arrivée:
                    for index in range (x_arrivée+1,x_départ-1):
                        if plateau[y_départ][index]!="    ":
                            position_valide=False
                if x_départ<x_arrivée and y_départ==y_arrivée:
                    for index in range (x_départ+1,x_arrivée-1):
                        if plateau[y_départ][index]!="    ":
                            position_valide=False
                if y_arrivée<y_départ and y_départ==y_arrivée:
                    for index in range (y_arrivée+1,y_départ-1):
                        if plateau[index][x_départ]!="    ":
                            position_valide=False
                if y_départ<y_arrivée and y_départ==y_arrivée:
                    for index in range (y_départ+1,y_arrivée-1):
                        if plateau[y_départ][index]!="    ":
                            position_valide=False
    return position_valide

def is_position_valid_C(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
    D1=(x_arrivée,y_arrivée)==(x_départ+1,y_départ+2)
    D2=(x_arrivée,y_arrivée)==(x_départ+1,y_départ-2)
    D3=(x_arrivée,y_arrivée)==(x_départ-1,y_départ+2)
    D4=(x_arrivée,y_arrivée)==(x_départ-1,y_départ-2)
    D5=(x_arrivée,y_arrivée)==(x_départ+2,y_départ+1)
    D6=(x_arrivée,y_arrivée)==(x_départ+2,y_départ-1)
    D7=(x_arrivée,y_arrivée)==(x_départ-2,y_départ+1)
    D8=(x_arrivée,y_arrivée)==(x_départ-2,y_départ-1)
    if not(D1) and not(D2) and not(D3) and not(D4) and not(D5) and not(D6) and not(D7) and not(D8):
        position_valide=False
    return position_valide
        
        
def position_valide_P(plateau,a_noir_de_jouer,x_départ,y_départ,x_arrivée,y_arrivée,position_valide):
    #ajouter prise en passant 
    if a_noir_de_jouer==True:
        if (x_arrivée!=x_départ+1 or y_arrivée!=y_départ+1 or plateau[y_départ+1][x_départ+1]=="    "):
            position_valide=False
        if (x_arrivée!=x_départ+1 or y_arrivée!=y_départ or plateau[y_départ-1][x_départ+1]!="    "):
            position_valide=False
        if (x_arrivée!=x_départ or y_arrivée!=y_départ+1 or plateau[y_départ+1][x_départ]!="    "):
            position_valide=False
        if x_départ==1:
            if (x_arrivée!=x_départ or y_arrivée!=y_départ+2 or plateau[y_départ+2][x_départ]!="    "):
                position_valide=False
            if (x_arrivée!=x_départ or y_arrivée!=y_départ+1 or plateau[y_départ+1][x_départ]!="    "):
                position_valide=False
        if x_départ!=1:
            if (x_arrivée!=x_départ or y_arrivée!=y_départ+2 or plateau[y_départ+2][x_départ]!="    "):
                position_valide=False

    if a_noir_de_jouer==False:
        if (x_arrivée!=x_départ-1 or y_arrivée!=y_départ-1 or plateau[y_départ-1][x_départ+1]=="    "):
            position_valide=False
        if (x_arrivée!=x_départ+1 or y_arrivée!=y_départ-1 or plateau[y_départ+1][x_départ+1]=="    "):
            position_valide=False
        if x_départ==6:
            if (x_arrivée!=x_départ or y_arrivée!=y_départ-2 or plateau[y_départ-2][x_départ]!="    "):
                position_valide=False
            if (x_arrivée!=x_départ or y_arrivée!=y_départ-1 or plateau[y_départ-1][x_départ]!="    "):
                position_valide=False
        if x_départ!=6:
            if (x_arrivée!=x_départ or y_arrivée!=y_départ-1 or plateau[y_départ-1][x_départ]!="    "):
                position_valide=False
    return position_valide


def type_de_pièce(pièce):
    if pièce=="T1_N" or "T2_N" or "T1_B" or "T2_B":
        type_pièce="T"
    if pièce=="C1_N" or "C2_N" or "C1_B" or "C2_B":
        type_pièce="C"
    if pièce=="F1_N" or "F2_N" or "F1_B" or "F2_B":
        type_pièce="F"
    if pièce=="RE_N" or "RE_B":
        type_pièce="RE"
    if pièce=="RO_N" or "RO_B":
        type_pièce="RO"
    if pièce in (liste_pions_noirs or liste_pions_blancs):
        type_pièce="P"
    return type_pièce

def move_piece(plateau,a_noir_de_jouer):
    pièce=str(input("Quelle pièce à déplacer ? "))
    if a_noir_de_jouer==True:
        if pièce not in (liste_pièces_noires or liste_pions_noirs):
            pièce=str(input("Erreur, quelle pièce à déplacer (ex : T1_N) ? "))
    else:
        if pièce not in (liste_pièces_blanches or liste_pions_blancs):
            pièce=str(input("Erreur, quelle pièce à déplacer (ex : T1_B) ? "))
    type_pièce=type_de_pièce(pièce)
    for index_y in range(7):
        if pièce in plateau[index_y]:
            y_départ=index_y
            for index_x in range(7):
                if pièce == plateau[index_y,index_x]:
                    x_départ=plateau[index_y,index_x]
    x_arrivée=(int(input("Quelle est la nouvelle colonne ? ")))
    y_arrivée=(int(input("Quelle est la nouvelle ligne ? ")))
    