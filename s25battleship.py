import random


class Dot:
    def __init__(self, ycoord, xcoord):
        self.ycoord = ycoord
        self.xcoord = xcoord
        
    def __eq__(self, other):
        return self.ycoord == other.ycoord, self.xcoord == other.xcoord

    def init_from_input(self, ycoord, xcoord):
        self.ycoord, self.xcoord = list(map(int, input("Ход игрока: ").split()))
       

class Ship:
    def __init__(self, length, nosey, nosex, direction, side):
        self.length = length
        self.nosey = nosey
        self.nosex = nosex
        self.direction = direction
        self.side = side
        shippoints = []
        self.result = 0
        board[self.nosey-1][self.nosex-1] = "| ■ |"
        shippoints.append([self.nosey-1, self.nosex-1])
        if self.length > 1:
            if self.direction == 0:
                try:
                    board[self.nosey-1][self.nosex] = "| ■ |"
                    shippoints.append([self.nosey-1, self.nosex])
                    self.result = 1
                except IndexError:
                    self.result = 0
                    shippoints.clear()
                    board[self.nosey-1][self.nosex-1] = "| O |"
                if self.length > 2:
                    try:
                        board[self.nosey-1][self.nosex+1] = "| ■ |"
                        shippoints.append([self.nosey-1, self.nosex+1])
                        self.result = 1
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                        try:
                            board[self.nosey-1][self.nosex] = "| O |"
                        except IndexError:
                            pass
                        finally:
                            board[self.nosey-1][self.nosex-1] = "| O |"
            if self.direction == 1:
                try:
                    board[self.nosey-1][self.nosex-2] = "| ■ |"
                    shippoints.append([self.nosey-1, self.nosex-2])
                    self.result = 1
                except IndexError:
                    self.result = 0
                    shippoints.clear()
                    board[self.nosey-1][self.nosex-1] = "| O |"
                if self.length > 2:
                    try:
                        board[self.nosey-1][self.nosex-3] = "| ■ |"
                        shippoints.append([self.nosey-1, self.nosex-3])
                        self.result = 1
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                        try:
                            board[self.nosey-1][self.nosex-2] = "| O |"
                        except IndexError:
                            pass
                        finally:
                            board[self.nosey-1][self.nosex-1] = "| O |"
            if self.direction == 2:
                try:
                    board[self.nosey][self.nosex-1] = "| ■ |"
                    shippoints.append([self.nosey, self.nosex-1])
                    self.result = 1
                except IndexError:
                    self.result = 0
                    shippoints.clear()
                    board[self.nosey-1][self.nosex-1] = "| O |"
                if self.length > 2:
                    try:
                        board[self.nosey+1][self.nosex-1] = "| ■ |"
                        shippoints.append([self.nosey+1, self.nosex-1])
                        self.result = 1
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                        try:
                            board[self.nosey][self.nosex-1] = "| O |"
                        except IndexError:
                            pass
                        finally:
                            board[self.nosey-1][self.nosex-1] = "| O |"
            if self.direction == 3:
                try:
                    board[self.nosey-2][self.nosex-1] = "| ■ |"
                    shippoints.append([self.nosey-2, self.nosex-1])
                    self.result = 1
                except IndexError:
                    self.result = 0
                    shippoints.clear()
                    board[self.nosey-1][self.nosex-1] = "| O |"
                if self.length > 2:
                    try:
                        board[self.nosey-3][self.nosex-1] = "| ■ |"
                        shippoints.append([self.nosey-3, self.nosex-1])
                        self.result = 1
                    except IndexError:
                        self.result = 0
                        shippoints.clear()
                        try:
                            board[self.nosey-2][self.nosex-1] = "| O |"
                        except IndexError:
                            pass
                        finally:
                            board[self.nosey-1][self.nosex-1] = "| O |"
        else:
            self.result = 1
        if (self.side == 0) and (self.result == 1):
            aishiplist.append(shippoints)
        if (self.side == 1) and (self.result == 1):
            playershiplist.append(shippoints)
            
        
            
    
class Board:
    def __init__(self, board):
        self.board = board

    def showboard(board):
        linenum = 1
        print("    | 1 |  | 2 |  | 3 |  | 4 |  | 5 |  | 6 |")
        for line in board:
            print(" ", str(linenum), end =" ")
            print('  '.join(map(str, line)))
            linenum += 1
        linenum = 1
        
    def add_ship(length, side):
        ship = Ship(length, random.randint(1,6), random.randint(1,6), random.randint(0,3), side)
            if ship.result == 1:
                return True
            else:
                return False
        
board = [["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
	 ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
	 ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
     ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
     ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"],
     ["| О |", "| О |", "| О |", "| О |", "| О |", "| О |"]]

aishiplist = []
playershiplist = []

class Game:
    def greet():
        print("                 МОРСКОЙ БОЙ")
        Board.showboard(board)
        print(" Пример хода: 1 2")
        board[0][1] = "| X |"
        Board.showboard(board)
        board[0][1] = "| О |"
        print("     ■ - корабли игрока")
        print("     X - подбитые корабли")
        print("     T - промахи")
        print("     О - пустая клетка")
    
    
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
       
        
    
    def start():
        Game.greet()
        
Game.start()
Game.random_board()
Board.showboard(board)
print(aishiplist)
print(playershiplist)
