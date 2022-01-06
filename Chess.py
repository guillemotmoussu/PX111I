'''
Jeu fonctionnel, pour une partie en JVJ

Règles implémentées :
    - fonctions élémentaires : création, affichage du plateau...
    - déplacement spécifique de chaque pièce
    - prise des pièces adverses
    - Roque
    - Prise en passant
    - Promotion

Cependant, pas de prise en compte de l'echec / echec et mat donc le jeu ne s'arrête jamais. C'est aux utilisateurs d'arbitrer la partie

'''

###########constantes############
LsJuicerW = ["R1w", "N1w", "B1w", "Q1w", "KGw", "B2w", "N2w", "R2w"]
LsPawnsW = ["P1w", "P2w", "P3w", "P4w", "P5w", "P6w", "P7w", "P8w"]
LsJuicerB = ["R1b", "N1b", "B1b", "Q1b", "KGb", "B2b", "N2b", "R2b"]
LsPawnsB = ["P1b", "P2b", "P3b", "P4b", "P5b", "P6b", "P7b", "P8b"]
EmptyFile = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
#################################

def InitChessBoard(): #initialise le plateau, avec les lettres et les chiffres pour identifier les positions
    ChessBoard = ["jaaj"]+[LsJuicerW]+[LsPawnsW]+4*[EmptyFile]+[LsPawnsB]+[LsJuicerB]+["jaaj"]
    ChessBoard[0] = ["(-)", "(A)", "(B)", "(C)", "(D)", "(E)", "(F)", "(G)", "(H)", "(-)"]
    ChessBoard[1] = ["(1)"]+ChessBoard[1]+["(-)"]
    ChessBoard[2] = ["(2)"]+ChessBoard[2]+["(-)"]
    ChessBoard[3] = ["(3)"]+ChessBoard[3]+["(-)"]
    ChessBoard[4] = ["(4)"]+ChessBoard[4]+["(-)"]
    ChessBoard[5] = ["(5)"]+ChessBoard[5]+["(-)"]
    ChessBoard[6] = ["(6)"]+ChessBoard[6]+["(-)"]
    ChessBoard[7] = ["(7)"]+ChessBoard[7]+["(-)"]
    ChessBoard[8] = ["(8)"]+ChessBoard[8]+["(-)"]
    ChessBoard[9] = ["(-)"]*10
    return ChessBoard


def PrintChessBoard(matrix):    #affichage du plateau de jeu
    print("[====================================================================]")
    for index in range(len(matrix)-1):
        print(matrix[9-index])
        print("[                                                                    ]")
    print(matrix[0])
    print("[====================================================================]")


def LetterTrad(letter):     #traduction des A,B,C sur le plateau en 1,2,3 pour le programme
    number = 0
    for index in range(8):
        if letter == columns[index]:
            number = index+1
    return number


def InputPiece(Bturn, ChessBoard):  #fonction permettant d'ajouter une pièce sur le plateau
    approved = False        #variable d'approbation
    rank = 0                #ligne de la pièce
    file = 0                #colonne de la pièce
    if Bturn is True:       #détermine b (black) ou w (white) selon le tour du joueur automatiquement
        turn = "b"
    if Bturn is False:
        turn = "w"
    while approved is False:
        piece = input("\nWhich piece to move ? : ")          
        if len(piece) == 2:     #longueur nominale
            if piece[0] == "K" or piece[0] == "Q" or piece[0] == "B" or piece[0] == "N" or piece[0] == "R" or piece[0] == "P":
                piece = piece + turn      #on ajoute à la variable le joueur qui possède cette pièce
                locate = LocatePiece(piece, ChessBoard)     #localisation de la pièce sur le plateau
                approved = locate[2]
                rank = locate[0]
                file = locate[1]
        if approved==False:
            print("\n This piece is not a valid piece...\n (expecting something like P4 or KG)")
    return [piece, rank, file]  #retourne la pièce (valide), et sa position


def LocatePiece(piece, ChessBoard):     #localise une pièce si elle existe
    fileP = 0                           #colonne de la pièce sur le plateau
    rankP = 0                           #ligne de la pièce sur le plateau
    found = False
    for rank in range(8):
        for file in range(8):
            if ChessBoard[rank+1][file+1] == piece:
                found = True
                rankP = rank + 1
                fileP = file + 1
    return[rankP, fileP, found]         #retourne found à false si la pièce n'existe pas sur le plateau


def InputCoords(piece):         #entrée des coordonnées
    approved = False
    while approved is False:    #vérification de la validité de la position, et reboucle si elle est fausse
        coords = input("Where will you place your " + piece[0] + piece[1] + " ? : ")
        if len(coords) == 2:    #longueur attendue de la réponse
            Verif1 = coords[0] == "A" or coords[0] == "B" or coords[0] == "C" or coords[0] == "D"
            Verif2 = coords[0] == "E" or coords[0] == "F" or coords[0] == "G" or coords[0] == "H"
            Verif3 = coords[1] == "1" or coords[1] == "2" or coords[1] == "3" or coords[1] == "4"
            Verif4 = coords[1] == "5" or coords[1] == "6" or coords[1] == "7" or coords[1] == "8"
            if Verif1 or Verif2:
                if Verif3 or Verif4:
                    approved = True
        if approved==False:
            print("\n " + coords + " is not a valid position...\n (expected: File from A to H, Rank from 1 to 8, ex: E5)")    
    return coords               #retourne les coordonnées (valides)


def MovePiece(piece, actualcoords, coords, ChessBoard, RoqueOK1, RoqueOK2, GhostPawn, NbJuicers):      #déplacement des pièces
    #on gère chaque type de pièce séparément, dans les sous-fonctions associées
    Movedone = False
    if piece[0] == "K":         #partie qui correspond au roi
        MoveK = MoveKing(piece, actualcoords, coords, ChessBoard, Movedone, RoqueOK1, RoqueOK2)
        ChessBoard = MoveK[0]
        Movedone = MoveK[1]
        if Movedone is True:
            RoqueOK1 = False
            RoqueOK2 = False
            GhostPawn = [0, 0]
    if piece[0] == "Q":         #partie qui correspond à la reine
        MoveQ = MoveQueen(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveQ[0]
        Movedone = MoveQ[1]
        if Movedone is True:
            GhostPawn = [0, 0]
    if piece[0] == "B":         #partie qui correspond au fou
        MoveB = MoveBishop(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveB[0]
        Movedone = MoveB[1]
        if Movedone is True:
            GhostPawn = [0, 0]
    if piece[0] == "N":         #partie qui correspond au cavalier
        MoveN = MoveKnight(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveN[0]
        Movedone = MoveN[1]
        if Movedone is True:
            GhostPawn = [0, 0]
    if piece[0] == "R":         #partie qui correspond à la tour
        MoveR = MoveRook(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveR[0]
        Movedone = MoveR[1]
        if Movedone is True:
            if piece[1] == "1":
                RoqueOK1 = False
            if piece[1] == "2":
                RoqueOK2 = False
            GhostPawn = [0, 0]
    if piece[0] == "P":         #partie qui correspond au pion
        MoveP = MovePawn(piece, actualcoords, coords, ChessBoard, Movedone, GhostPawn, NbJuicers)
        ChessBoard = MoveP[0]
        Movedone = MoveP[1]
        GhostPawn = MoveP[2]
        NbJuicers = MoveP[3]
    return(ChessBoard, Movedone, RoqueOK1, RoqueOK2, GhostPawn, NbJuicers)


def MoveKing(piece, actualcoords, coords, ChessBoard, Movedone, RoqueOK1, RoqueOK2):
    #partie correspondant au roque
    if piece[2] == "w" and coords == [1, 7]:
        if ChessBoard[1][6] == "   " and ChessBoard[1][7] == "   ":
            if RoqueOK2 is True:
                ChessBoard[1][7] = ChessBoard[1][5]
                ChessBoard[1][5] = "   "
                ChessBoard[1][6] = ChessBoard[1][8]
                ChessBoard[1][8] = "   "
                Movedone = True
    if piece[2] == "w" and coords == [1, 3]:
        if ChessBoard[1][4] == "   " and ChessBoard[1][3] == "   " and ChessBoard[1][2] == "   ":
            if RoqueOK1 is True:
                ChessBoard[1][3] = ChessBoard[1][5]
                ChessBoard[1][5] = "   "
                ChessBoard[1][4] = ChessBoard[1][1]
                ChessBoard[1][1] = "   "
                Movedone = True
    if piece[2] == "b" and coords == [8, 7]:
        if ChessBoard[8][6] == "   " and ChessBoard[8][7] == "   ":
            if RoqueOK2 is True:
                ChessBoard[8][7] = ChessBoard[8][5]
                ChessBoard[8][5] = "   "
                ChessBoard[8][6] = ChessBoard[8][8]
                ChessBoard[8][8] = "   "
                Movedone = True
    if piece[2] == "b" and coords == [8, 3]:
        if ChessBoard[8][4] == "   " and ChessBoard[8][3] == "   " and ChessBoard[8][2] == "   ":
            if RoqueOK1 is True:
                ChessBoard[8][3] = ChessBoard[8][5]
                ChessBoard[8][5] = "   "
                ChessBoard[8][4] = ChessBoard[8][1]
                ChessBoard[8][1] = "   "
                Movedone = True
    if Movedone is False:
    #partie correspondant au déplacement normal
        if coords[0] - actualcoords[0] in [-1, 0, 1] and coords[1] - actualcoords[1] in [-1, 0, 1]:
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            Movedone = True
    return (ChessBoard, Movedone)


def MoveQueen(actualcoords, coords, ChessBoard, Movedone):
    EmptyTiles = False      #vérifie que toutes les cases sur la ligne, diagonale ou colonne de déplacement sont libres
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][coords[1]-coords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]-actualcoords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][coords[1]+coords[0]-index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]+actualcoords[0]-index] != "   ":
                EmptyTiles = False
    if coords[0] < actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] > actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] < actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[1]+1, actualcoords[1]):
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] > actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[1]+1, coords[1]):
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if EmptyTiles is True:  #si le trajet est libre, déplacement normal
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MoveBishop(actualcoords, coords, ChessBoard, Movedone):
    EmptyTiles = False  #vérifie que toutes les cases sur la diagonale de déplacement sont libres
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][coords[1]-coords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]-actualcoords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][coords[1]+coords[0]-index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]+actualcoords[0]-index] != "   ":
                EmptyTiles = False
    if EmptyTiles is True:      #si le trajet est libre, déplacement normal
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MoveKnight(actualcoords, coords, ChessBoard, Movedone):
    #liste des mouvements possibles
    Move1 = [actualcoords[0]+1, actualcoords[1]+2]
    Move2 = [actualcoords[0]+1, actualcoords[1]-2]
    Move3 = [actualcoords[0]-1, actualcoords[1]+2]
    Move4 = [actualcoords[0]-1, actualcoords[1]-2]
    Move5 = [actualcoords[0]+2, actualcoords[1]+1]
    Move6 = [actualcoords[0]+2, actualcoords[1]-1]
    Move7 = [actualcoords[0]-2, actualcoords[1]+1]
    Move8 = [actualcoords[0]-2, actualcoords[1]-1]
    if coords in [Move1, Move2, Move3, Move4, Move5, Move6, Move7, Move8]:  #vérifie que le mouvement est possible
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MoveRook(actualcoords, coords, ChessBoard, Movedone):
    EmptyTiles = False      #vérifie que toutes les cases sur la ligne ou colonne de déplacement sont libres
    if coords[0] < actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] > actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] < actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[1]+1, actualcoords[1]):
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] > actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[1]+1, coords[1]):
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if EmptyTiles is True:      #si le trajet est libre, déplacement normal
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MovePawn(piece, actualcoords, coords, ChessBoard, Movedone, GhostPawn, NbJuicers):
    Pawnmove = 0
    #détermination de la direction que vont avoir les pions
    if piece[2] == "w":
        Pawnmove = 1
    if piece[2] == "b":
        Pawnmove = -1
    #vérification des mouvements possibles, sachant qu'ils diffèrent selon le joueur
    if coords[0] == actualcoords[0] + Pawnmove and coords[1] == actualcoords[1]:
        if ChessBoard[coords[0]][coords[1]] == "   ":
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            GhostPawn = [0, 0]
            Movedone = True
    if coords[0] == actualcoords[0] + 2*Pawnmove and coords[1] == actualcoords[1] and actualcoords[0] in [2, 7]:
        if ChessBoard[coords[0]][coords[1]] == "   " and ChessBoard[actualcoords[0] + Pawnmove][coords[1]] == "   ":
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            GhostPawn = [actualcoords[0] + Pawnmove, actualcoords[1]]
            Movedone = True
    if coords[0] == actualcoords[0] + Pawnmove and coords[1] in [actualcoords[1]-1, actualcoords[1]+1]:
        if ChessBoard[coords[0]][coords[1]] != "   ":
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            GhostPawn = [0, 0]
            Movedone = True
        if coords == GhostPawn:     #prise en passant
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            ChessBoard[actualcoords[0]][coords[1]] = "   "
            GhostPawn = [0, 0]
            Movedone = True
    if coords[0] in [1, 8]:         #promotion
        print("Congratulations, you promoted !")
        promotion = input("Choose which piece you want to use ? (Q, B, N or R) : ")
        if promotion == "Q":
            NbJuicers[0] += 1
            ChessBoard[coords[0]][coords[1]] = promotion + str(NbJuicers[0]) + piece[2]
        if promotion == "B":
            NbJuicers[1] += 1
            ChessBoard[coords[0]][coords[1]] = promotion + str(NbJuicers[1]) + piece[2]
        if promotion == "N":
            NbJuicers[2] += 1
            ChessBoard[coords[0]][coords[1]] = promotion + str(NbJuicers[2]) + piece[2]
        if promotion == "R":
            NbJuicers[3] += 1
            ChessBoard[coords[0]][coords[1]] = promotion + str(NbJuicers[3]) + piece[2]
    return (ChessBoard, Movedone, GhostPawn, NbJuicers)


def PlayTurn(Bturn, ChessBoard, RoqueOK1, RoqueOK2, GhostPawn, NbJuicers):     #tour de jeu
    if Bturn is False:
        print("\n It's White's turn !\n")
    if Bturn is True:
        print("\n It's Black's turn !\n")
    Turndone = False
    PrintChessBoard(ChessBoard)
    GetPiece = InputPiece(Bturn, ChessBoard)
    piece = GetPiece[0]
    actualcoords = [GetPiece[1], GetPiece[2]]
    coords = InputCoords(piece)                          #coordonnées futures entrées par l'utilisateur
    displaycoords = coords                               #utilisé dans les messages d'erreurs pour l'utilisateur
    coords = [int(coords[1]), LetterTrad(coords[0])]     #traduction des coordonnées en nombres
    if ChessBoard[coords[0]][coords[1]][2] != piece[2]:  #bloque les mouvements sur place et la prise d'une de ses pieces
        move = MovePiece(piece, actualcoords, coords, ChessBoard, RoqueOK1, RoqueOK2, GhostPawn, NbJuicers)
        RoqueOK1 = move[2]
        RoqueOK2 = move[3]
        GhostPawn = move[4]
        NbJuicers = move[5]
        if move[1] is True:
            ChessBoard = move[0]
            Turndone = True
        else:
            print("\n [!] Invalid Move...\n")
    else:
        print("\n [!] You already have a piece on " + displaycoords + "...\n")
    return (ChessBoard, Turndone, RoqueOK1, RoqueOK2, GhostPawn, NbJuicers)


def StartGame():
    print("\n\n\n\n\n")
    Bturn = False                       #on commence avec les blancs
    RoqueOKw1 = True                    #les roques sont possibles au début
    RoqueOKw2 = True                    #on a besoin de deux variables par joueur
    RoqueOKb1 = True                    #une pour le grand roque, et l'autre pour le petit roque
    RoqueOKb2 = True
    GhostPawn = [0, 0]                  #pion "fantôme" permettant la prise en passant
    NbJuicers = [1, 2, 2, 2]            #variable servant à la promotion des pions
    ChessBoard = InitChessBoard()
    CheckMate = False                   #pas implémenté pour le moment, donc ne s'arrête jamais. C'est à l'utilisateur d'arbitrer
    while CheckMate is False:
        if Bturn is False:
            play = PlayTurn(Bturn, ChessBoard, RoqueOKw1, RoqueOKw2, GhostPawn, NbJuicers)
            RoqueOKw1 = play[2]
            RoqueOKw2 = play[3]
            GhostPawn = play[4]
            NbJuicers = play[5]
        if Bturn is True:
            play = PlayTurn(Bturn, ChessBoard, RoqueOKb1, RoqueOKb2, GhostPawn, NbJuicers)
            RoqueOKb1 = play[2]
            RoqueOKb2 = play[3]
            GhostPawn = play[4]
            NbJuicers = play[5]
        if play[1] is True:
            ChessBoard = play[0]
            Bturn = not(Bturn)
    return(ChessBoard, CheckMate)


#main
StartGame()