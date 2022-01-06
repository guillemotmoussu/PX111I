"""
Here's my chess code
Let's do this
Good luck myself
"""

LsJuicerW = ["R1w", "N1w", "B1w", "Q1w", "KGw", "B2w", "N2w", "R2w"]
LsPawnsW = ["P1w", "P2w", "P3w", "P4w", "   ", "P6w", "P7w", "P8w"]
LsJuicerB = ["R1b", "N1b", "B1b", "Q1b", "KGb", "B2b", "N2b", "R2b"]
LsPawnsB = ["P1b", "P2b", "P3b", "P4b", "   ", "P6b", "P7b", "P8b"]
EmptyFile = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
columns = ["A", "B", "C", "D", "E", "F", "G", "H"]


def InitChessBoard():
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


def PrintChessBoard(matrix):
    print("[====================================================================]")
    for index in range(len(matrix)-1):
        print(matrix[9-index])
        print("[                                                                    ]")
    print(matrix[0])
    print("[====================================================================]")


def LetterTrad(letter):
    number = 0
    for index in range(8):
        if letter == columns[index]:
            number = index+1
    return number


def InputPiece(Bturn, ChessBoard):
    approved = False
    rank = 0
    file = 0
    piece = input("Which piece to move ? : ")
    if Bturn is True:
        turn = "b"
    if Bturn is False:
        turn = "w"
    if len(piece) == 2:
        if piece[0] == "K" or piece[0] == "Q" or piece[0] == "B" or piece[0] == "N" or piece[0] == "R" or piece[0] == "P":
            piece = piece + turn
            locate = LocatePiece(piece, ChessBoard)
            approved = locate[2]
            rank = locate[0]
            file = locate[1]
    while approved is False:
        if len(piece) < 2:
            piece = piece + "   "
        print("\n " + piece[0] + piece[1] + " is not a valid piece on the board...\n (expecting something you have here)")
        piece = input("Which piece to move ? : ")
        if len(piece) == 2:
            if piece[0] == "K" or piece[0] == "Q" or piece[0] == "B" or piece[0] == "N" or piece[0] == "R" or piece[0] == "P":
                piece = piece + turn
                locate = LocatePiece(piece, ChessBoard)
                approved = locate[2]
                rank = locate[0]
                file = locate[1]
    return [piece, rank, file]


def LocatePiece(piece, ChessBoard):
    fileP = 0
    rankP = 0
    found = False
    for rank in range(8):
        for file in range(8):
            if ChessBoard[rank+1][file+1] == piece:
                found = True
                rankP = rank + 1
                fileP = file + 1
    return[rankP, fileP, found]


def InputCoords(piece):
    approved = False
    coords = input("Where will you place your " + piece[0] + piece[1] + " ? : ")
    if len(coords) == 2:
        Verif1 = coords[0] == "A" or coords[0] == "B" or coords[0] == "C" or coords[0] == "D"
        Verif2 = coords[0] == "E" or coords[0] == "F" or coords[0] == "G" or coords[0] == "H"
        Verif3 = coords[1] == "1" or coords[1] == "2" or coords[1] == "3" or coords[1] == "4"
        Verif4 = coords[1] == "5" or coords[1] == "6" or coords[1] == "7" or coords[1] == "8"
        if Verif1 or Verif2:
            if Verif3 or Verif4:
                approved = True
    while approved is False:
        print("\n " + coords + " is not a valid position...\n (expected: File from A to H, Rank from 1 to 8, ex: E5)")
        coords = input("Where will you place your " + piece[0] + piece[1] + " ? : ")
        if len(coords) == 2:
            Verif1 = coords[0] == "A" or coords[0] == "B" or coords[0] == "C" or coords[0] == "D"
            Verif2 = coords[0] == "E" or coords[0] == "F" or coords[0] == "G" or coords[0] == "H"
            Verif3 = coords[1] == "1" or coords[1] == "2" or coords[1] == "3" or coords[1] == "4"
            Verif4 = coords[1] == "5" or coords[1] == "6" or coords[1] == "7" or coords[1] == "8"
            if Verif1 or Verif2:
                if Verif3 or Verif4:
                    approved = True
    return coords


def MovePiece(piece, actualcoords, coords, ChessBoard, RoqueOK1, RoqueOK2):
    Movedone = False
    if piece[0] == "K":
        MoveK = MoveKing(piece, actualcoords, coords, ChessBoard, Movedone, RoqueOK1, RoqueOK2)
        ChessBoard = MoveK[0]
        Movedone = MoveK[1]
        if Movedone is True:
            RoqueOK1 = False
            RoqueOK2 = False
    if piece[0] == "Q":
        MoveQ = MoveQueen(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveQ[0]
        Movedone = MoveQ[1]
    if piece[0] == "B":
        MoveB = MoveBishop(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveB[0]
        Movedone = MoveB[1]
    if piece[0] == "N":
        MoveN = MoveKnight(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveN[0]
        Movedone = MoveN[1]
    if piece[0] == "R":
        MoveR = MoveRook(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveR[0]
        Movedone = MoveR[1]
        if Movedone is True:
            if piece[1] == "1":
                RoqueOK1 = False
            if piece[1] == "2":
                RoqueOK2 = False
    if piece[0] == "P":
        MoveP = MovePawn(piece, actualcoords, coords, ChessBoard, Movedone)
        ChessBoard = MoveP[0]
        Movedone = MoveP[1]
    return(ChessBoard, Movedone, RoqueOK1, RoqueOK2)


def MoveKing(piece, actualcoords, coords, ChessBoard, Movedone, RoqueOK1, RoqueOK2):
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
        if coords[0] - actualcoords[0] in [-1, 0, 1] and coords[1] - actualcoords[1] in [-1, 0, 1]:
            ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
            ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
            Movedone = True
    return (ChessBoard, Movedone)


def MoveQueen(piece, actualcoords, coords, ChessBoard, Movedone):
    return (ChessBoard, Movedone)


def MoveBishop(piece, actualcoords, coords, ChessBoard, Movedone):
    EmptyTiles = False
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            print(ChessBoard[index][coords[1]-coords[0]+index])
            if ChessBoard[index][coords[1]-coords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == coords[1] - actualcoords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            print(ChessBoard[index][actualcoords[1]-actualcoords[0]+index])
            if ChessBoard[index][actualcoords[1]-actualcoords[0]+index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] < actualcoords[0]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            print(ChessBoard[index][coords[1]+coords[0]-index])
            if ChessBoard[index][coords[1]+coords[0]-index] != "   ":
                EmptyTiles = False
    if coords[0] - actualcoords[0] == actualcoords[1] - coords[1] and coords[0] > actualcoords[0]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            print(index)
            print(actualcoords[1]-actualcoords[0]-index)
            print(ChessBoard[index][actualcoords[1]+actualcoords[0]-index])
            if ChessBoard[index][actualcoords[1]+actualcoords[0]-index] != "   ":
                EmptyTiles = False
    if EmptyTiles is True:
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MoveKnight(piece, actualcoords, coords, ChessBoard, Movedone):
    return (ChessBoard, Movedone)


def MoveRook(piece, actualcoords, coords, ChessBoard, Movedone):
    EmptyTiles = False
    if coords[0] < actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[0]+1, actualcoords[0]):
            print(ChessBoard[index][actualcoords[1]])
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] > actualcoords[0] and coords[1] == actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[0]+1, coords[0]):
            print(ChessBoard[index][actualcoords[1]])
            if ChessBoard[index][actualcoords[1]] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] < actualcoords[1]:
        EmptyTiles = True
        for index in range(coords[1]+1, actualcoords[1]):
            print(ChessBoard[index][actualcoords[1]])
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if coords[0] == actualcoords[0] and coords[1] > actualcoords[1]:
        EmptyTiles = True
        for index in range(actualcoords[1]+1, coords[1]):
            print(ChessBoard[index][actualcoords[1]])
            if ChessBoard[actualcoords[0]][index] != "   ":
                EmptyTiles = False
    if EmptyTiles is True:
        ChessBoard[coords[0]][coords[1]] = ChessBoard[actualcoords[0]][actualcoords[1]]
        ChessBoard[actualcoords[0]][actualcoords[1]] = "   "
        Movedone = True
    return (ChessBoard, Movedone)


def MovePawn(piece, actualcoords, coords, ChessBoard, Movedone):
    return (ChessBoard, Movedone)


def PlayTurn(Bturn, ChessBoard, RoqueOK1, RoqueOK2):
    if Bturn is False:
        print("\n\n\n\n It's White's turn !\n")
    if Bturn is True:
        print("\n\n\n\n It's Black's turn !\n")
    Turndone = False
    PrintChessBoard(ChessBoard)
    GetPiece = InputPiece(Bturn, ChessBoard)
    piece = GetPiece[0]
    actualcoords = [GetPiece[1], GetPiece[2]]
    coords = InputCoords(piece)
    print(piece)
    print(actualcoords)
    print(coords)
    displaycoords = coords
    coords = [int(coords[1]), LetterTrad(coords[0])]
    print(coords)
    if ChessBoard[coords[0]][coords[1]][2] != piece[2]:
        move = MovePiece(piece, actualcoords, coords, ChessBoard, RoqueOK1, RoqueOK2)
        RoqueOK1 = move[2]
        RoqueOK2 = move[3]
        if move[1] is True:
            ChessBoard = move[0]
            Turndone = True
        else:
            print("\n [!] Invalid Move. Will be explanied in the future...\n")
    else:
        print("\n [!] You already have a piece on " + displaycoords + "...\n")
    return (ChessBoard, Turndone, RoqueOK1, RoqueOK2)


"More functions comming before this"


def StartGame():
    Bturn = False
    RoqueOKw1 = True
    RoqueOKw2 = True
    RoqueOKb1 = True
    RoqueOKb2 = True
    ChessBoard = InitChessBoard()
    CheckMate = False
    while CheckMate is False:
        if Bturn is False:
            play = PlayTurn(Bturn, ChessBoard, RoqueOKw1, RoqueOKw2)
            RoqueOKw1 = play[2]
            RoqueOKw2 = play[3]
        if Bturn is True:
            play = PlayTurn(Bturn, ChessBoard, RoqueOKb1, RoqueOKb2)
            RoqueOKb1 = play[2]
            RoqueOKb2 = play[3]
        if play[1] is True:
            ChessBoard = play[0]
            Bturn = not(Bturn)
    return(ChessBoard, CheckMate)


print("\n\n\n")
StartGame()
"Need CodeStyle"