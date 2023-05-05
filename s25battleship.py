import random
import itertools


class Ship:
    def __init__(self, length, nosey, nosex, direction, side):
        self.length = length
        self.nosey = nosey
        self.nosex = nosex
        self.direction = direction
        self.side = side
        shippoints = []
        boardd = aiboard
        shiplist = aishiplist
        self.result = 1
        self.nosey = self.nosey - 1
        self.nosex = self.nosex - 1
        if self.side == 1:
            boardd = playerboard
            shiplist = playershiplist
        shippoints.append([self.nosey, self.nosex])
        adjac = lambda x, y: [[x2, y2] for x2 in range(x - 1, x + 2) for y2 in range(y - 1, y + 2) if
                              (-1 < x < 9 and -1 < y < 9 and (x != x2 or y != y2) and (0 <= x2 < 9) and (0 <= y2 < 9))]
        for i in adjac(self.nosey, self.nosex):
            if boardd[i[0]][i[1]] == "| ■ |":
                self.result = 0
                shippoints.clear()
                break
        if self.length == 1 and self.result == 1:
            try:
                for i in range(len(shippoints)):
                    if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                        raise IndexError
            except IndexError:
                self.result = 0
            else:
                self.result = 1
        if (self.length > 1 and self.result == 1):
            if self.direction == 0:
                shippoints.append([self.nosey, self.nosex + 1])
                if shippoints[-1][1] <= 8:
                    boardd[self.nosey][self.nosex + 1] = "| ■ |"
                    try:
                        for i in range(len(shippoints)):
                            if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                boardd[self.nosey][self.nosex + 1] = "| О |"
                                raise IndexError
                    except IndexError:
                        self.result = 0
                    else:
                        self.result = 1
                else:
                    self.result = 0
                if self.length > 2 and self.result == 1:
                    shippoints.append([self.nosey, self.nosex + 2])
                    if shippoints[-1][1] <= 8:
                        boardd[self.nosey][self.nosex + 2] = "| ■ |"
                        try:
                            for i in range(len(shippoints)):
                                if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                    boardd[self.nosey][self.nosex + 2] = "| О |"
                                    raise IndexError
                        except IndexError:
                            self.result = 0
                            shippoints.clear()
                        else:
                            self.result = 1
                    else:
                        self.result = 0
                        shippoints.clear()
                        boardd[self.nosey][self.nosex + 1] = "| О |"
            if self.direction == 1:
                shippoints.append([self.nosey, self.nosex - 1])
                if shippoints[-1][1] >= 0:
                    boardd[self.nosey][self.nosex - 1] = "| ■ |"
                    try:
                        for i in range(len(shippoints)):
                            if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                boardd[self.nosey][self.nosex - 1] = "| О |"
                                raise IndexError
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                    else:
                        self.result = 1
                else:
                    self.result = 0
                    shippoints.clear()
                if self.length > 2 and self.result == 1:
                    shippoints.append([self.nosey, self.nosex - 2])
                    if shippoints[-1][1] >= 0:
                        boardd[self.nosey][self.nosex - 2] = "| ■ |"
                        try:
                            for i in range(len(shippoints)):
                                if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                    boardd[self.nosey][self.nosex - 2] = "| О |"
                                    raise IndexError
                        except IndexError:
                            self.result = 0
                            shippoints.clear()
                        else:
                            self.result = 1
                    else:
                        self.result = 0
                        shippoints.clear()
                        boardd[self.nosey][self.nosex - 1] = "| О |"
            if self.direction == 2:
                shippoints.append([self.nosey + 1, self.nosex])
                if shippoints[-1][0] <= 8:
                    boardd[self.nosey + 1][self.nosex] = "| ■ |"
                    try:
                        for i in range(len(shippoints)):
                            if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                boardd[self.nosey + 1][self.nosex] = "| О |"
                                raise IndexError
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                    else:
                        self.result = 1
                else:
                    self.result = 0
                if self.length > 2 and self.result == 1:
                    shippoints.append([self.nosey + 2, self.nosex])
                    if shippoints[-1][0] <= 8:
                        boardd[self.nosey + 2][self.nosex] = "| ■ |"
                        try:
                            for i in range(len(shippoints)):
                                if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                    boardd[self.nosey + 2][self.nosex] = "| О |"
                                    raise IndexError
                        except IndexError:
                            self.result = 0
                            shippoints.clear()
                        else:
                            self.result = 1
                    else:
                        self.result = 0
                        shippoints.clear()
                        boardd[self.nosey + 1][self.nosex] = "| О |"
            if self.direction == 3:
                shippoints.append([self.nosey - 1, self.nosex])
                if shippoints[-1][0] >= 0:
                    boardd[self.nosey - 1][self.nosex] = "| ■ |"
                    try:
                        for i in range(len(shippoints)):
                            if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                boardd[self.nosey - 1][self.nosex] = "| О |"
                                raise IndexError
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                    else:
                        self.result = 1
                else:
                    self.result = 0
                if self.length > 2 and self.result == 1:
                    shippoints.append([self.nosey - 2, self.nosex])
                    if shippoints[-1][0] >= 0:
                        boardd[self.nosey - 2][self.nosex] = "| ■ |"
                        try:
                            for i in range(len(shippoints)):
                                if (shippoints[i] in shiplist or shippoints[i][0] < 0 or shippoints[i][1] < 0):
                                    boardd[self.nosey - 2][self.nosex] = "| О |"
                                    raise IndexError
                        except IndexError:
                            self.result = 0
                            shippoints.clear()
                        else:
                            self.result = 1
                    else:
                        self.result = 0
                        shippoints.clear()
                        boardd[self.nosey - 1][self.nosex] = "| О |"
        if self.result == 1:
            boardd[self.nosey][self.nosex] = "| ■ |"
        if (self.side == 0) and (self.result == 1):
            aishiplist.extend(shippoints)
        if (self.side == 1) and (self.result == 1):
            playershiplist.extend(shippoints)


class Board:
    def __init__(self, board):
        self.board = board

    def showboard(board):
        linenum = 1
        print("    | 1 |  | 2 |  | 3 |  | 4 |  | 5 |  | 6 |  | 7 |  | 8 |  | 9 |")
        for line in board:
            print(" ", str(linenum), end=" ")
            print('  '.join(map(str, line)))
            linenum += 1
        linenum = 1

    def shot(turny, turnx, board):
        mark = list((turny, turnx))
        if board == aiboard:
            if mark in aishiplist:
                print("ИГРОК: ПОПАДАНИЕ")
                mainboard[mark[0]][mark[1]] = "| X |"
                rem = aishiplist.index(mark)
                aishiplist[rem] = None
                return True
            else:
                print("ИГРОК: ПРОМАХ")
                mainboard[mark[0]][mark[1]] = "| T |"
                return False
        if board == playerboard:
            if mark in playershiplist:
                print("AI: ПОПАДАНИЕ")
                playerboard[mark[0]][mark[1]] = "| X |"
                mainboard[mark[0]][mark[1]] = "| ! |"
                rem = playershiplist.index(mark)
                playershiplist[rem] = None
                return True
            else:
                print("AI: ПРОМАХ")
                playerboard[mark[0]][mark[1]] = "| T |"
                return False

    @staticmethod
    def status():
        ai3xdown = all(i == None for i in aishiplist[0:3])
        if (ai3xdown):
            aishiplist[0] = "-"
            aishiplist[1] = "-"
            aishiplist[2] = "-"
            print("3Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai2xdown1 = all(i == None for i in aishiplist[3:5])
        if (ai2xdown1):
            aishiplist[3] = "-"
            aishiplist[4] = "-"
            print("2Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai2xdown2 = all(i == None for i in aishiplist[5:7])
        if (ai2xdown2):
            aishiplist[5] = "-"
            aishiplist[6] = "-"
            print("2Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai1xdown1 = all(i == None for i in aishiplist[7:8])
        if (ai1xdown1):
            aishiplist[7] = "-"
            print("1Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai1xdown2 = all(i == None for i in aishiplist[8:9])
        if (ai1xdown2):
            aishiplist[8] = "-"
            print("1Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai1xdown3 = all(i == None for i in aishiplist[9:10])
        if (ai1xdown3):
            aishiplist[9] = "-"
            print("1Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        ai1xdown4 = all(i == None for i in aishiplist[10:11])
        if (ai1xdown4):
            aishiplist[10] = "-"
            print("1Х КОРАБЛЬ ПРОТИВНИКА УНИЧТОЖЕН")
        aidown = all(i == "-" for i in aishiplist)
        if (aidown):
            return 1
        player3xdown = all(i == None for i in playershiplist[0:3])
        if (player3xdown):
            playershiplist[0] = "-"
            playershiplist[1] = "-"
            playershiplist[2] = "-"
            print("ВАШ 3Х КОРАБЛЬ УНИЧТОЖЕН")
        player2xdown1 = all(i == None for i in playershiplist[3:5])
        if (player2xdown1):
            playershiplist[3] = "-"
            playershiplist[4] = "-"
            print("ВАШ 2Х КОРАБЛЬ УНИЧТОЖЕН")
        player2xdown2 = all(i == None for i in playershiplist[5:7])
        if (player2xdown2):
            playershiplist[5] = "-"
            playershiplist[6] = "-"
            print("ВАШ 2Х КОРАБЛЬ УНИЧТОЖЕН")
        player1xdown1 = all(i == None for i in playershiplist[7:8])
        if (player1xdown1):
            playershiplist[7] = "-"
            print("ВАШ 1Х КОРАБЛЬ УНИЧТОЖЕН")
        player1xdown2 = all(i == None for i in playershiplist[8:9])
        if (player1xdown2):
            playershiplist[8] = "-"
            print("ВАШ 1Х КОРАБЛЬ УНИЧТОЖЕН")
        player1xdown3 = all(i == None for i in playershiplist[9:10])
        if (player1xdown3):
            playershiplist[9] = "-"
            print("ВАШ 1Х КОРАБЛЬ УНИЧТОЖЕН")
        player1xdown4 = all(i == None for i in playershiplist[10:11])
        if (player1xdown4):
            playershiplist[10] = "-"
            print("ВАШ 1Х КОРАБЛЬ УНИЧТОЖЕН")
        playerdown = all(i == "-" for i in playershiplist)
        if (playerdown):
            return 2

    def add_ship(length, side):
        nosey = random.randint(1, 9)
        nosex = random.randint(1, 9)
        direc = random.randint(0, 3)
        ship = Ship(length, nosey, nosex, direc, side)
        if ship.result == 1:
            return True
        else:
            return False


mainboard = [["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
             ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"]]

aiboard = [["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
           ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"]]

playerboard = [["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
               ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |", "| О |"]]

aishiplist = []
playershiplist = []


class Player:
    @staticmethod
    def ask():
        turny, turnx = list(map(int, input("Ход: ").split()))
        return turny, turnx


class User(Player):
    def ask():
        point = input("Ход игрока: ").strip()
        if " " not in point:
            point = point[0] + " " + point[1]
        turny, turnx = list(map(int, point.split()))
        turny -= 1
        turnx -= 1
        return turny, turnx


class AI(Player):
    def ask():
        turny = random.randint(1, 9)
        turnx = random.randint(1, 9)
        return turny, turnx


class Game:
    def greet():
        print("                 МОРСКОЙ БОЙ")
        Board.showboard(mainboard)
        print(" Пример хода: 1 2")
        mainboard[0][1] = "| X |"
        Board.showboard(mainboard)
        mainboard[0][1] = "| О |"
        print("     ■ - корабли игрока")
        print("     X - подбитые корабли")
        print("     T - промахи")
        print("     О - пустая клетка")

    def start():
        Game.greet()

    def random_board():

        while True:
            ship = Board.add_ship(3, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(2, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(2, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 0)
            if ship:
                break
        while True:
            ship = Board.add_ship(3, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(2, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(2, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 1)
            if ship:
                break
        while True:
            ship = Board.add_ship(1, 1)
            if ship:
                break

    def loop():
        game = 1
        turn = 1
        again = 0
        while game == 1:
            if turn == 1:
                again = 0
                a, b = User.ask()
                try:
                    if mainboard[a][b] == "| T |" or mainboard[a][b] == "| X |":
                        print("Уже было")
                        again = 1
                except IndexError:
                    print("Выберите между 1 и 9")
                    again = 1
                else:
                    sh = Board.shot(a, b, aiboard)
                    Board.showboard(mainboard)
                    print("")
                    Board.showboard(playerboard)
                    st = Board.status()
                    if not sh:
                        turn = 0
                    elif again == 1:
                        turn = 1
                    else:
                        turn = 1
                    if st == 1:
                        print("ВЫ ПОБЕДИЛИ")
                        game = 0
                        turn = 1
            if turn == 0:
                again = 0
                a, b = AI.ask()
                print("Ход AI:")
            try:
                if mainboard[a][b] == "| T |" or mainboard[a][b] == "| X |":
                    again = 1
            except IndexError:
                turn = 0
            else:
                sh = Board.shot(a, b, playerboard)
                Board.showboard(mainboard)
                print("")
                Board.showboard(playerboard)
                st = Board.status()
                if not sh:
                    turn = 1
                    if again == 1:
                        turn = 0
                else:
                    turn = 0
                if st == 2:
                    print("AI ПОБЕДИЛ")
                    game = 0


Game.start()
Game.random_board()
Board.showboard(mainboard)
print("")
Board.showboard(playerboard)
Game.loop()
