

def createZeroMatrix(r,c):
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

def printTTT(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print( '-----')
piece = ['X','O']

def checkValidMove(game,inp):
    if (inp > 9) or (inp < 1):
        return False
    pos = inp - 1
    if type(game[pos//3][pos%3]) == int:
        return True
    return False

def checkWin(game):
    players = ['X','O']
    for player in players:
        if ((player == game[0][0] == game[0][1] == game[0][2]) or
            (player == game[1][0] == game[1][1] == game[1][2]) or
            (player == game[2][0] == game[2][1] == game[2][2]) or
            (player == game[0][0] == game[1][0] == game[2][0]) or
            (player == game[0][1] == game[1][1] == game[2][1]) or
            (player == game[0][2] == game[1][2] == game[2][2]) or
            (player == game[0][0] == game[1][1] == game[2][2]) or
            (player == game[0][2] == game[1][1] == game[2][0])) :
            return player
    return False

def tttGamePlay():
    game = createZeroMatrix(3,3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0

    printTTT(game)
    print()
    for i in range(9): # Anyhow play 9 times
        pos = int(input(f'Player {piece[player]} move:')) - 1
        if checkValidMove(game,pos+1):
            game[pos//3][pos%3] = piece[player]
            player = 1 - player
            printTTT(game)
            winner = checkWin(game)
            if winner:
                print('Player',winner,'won!')
                break
            else:
                print()
        else:
            print('Invalid move!')

# game1 = [[1,2,3],[4,5,6],[7,8,9]]
# game2 = [['X',2,3],['X',5,6],['X',8,9]]
# game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
# game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
# game5 = [['X','X','O'],['X','O','X'],['O','X','X']]

# print(checkWin(game1))
# print(checkWin(game2))
# print(checkWin(game3))
# print(checkWin(game4))
# print(checkWin(game5))
tttGamePlay()
