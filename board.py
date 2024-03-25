import os

class Board:
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
    
    def display(self):
        print(self.cells[1]+" | "+self.cells[2]+" | "+self.cells[3])
        print("----------")
        print(self.cells[4]+" | "+self.cells[5]+" | "+self.cells[6])
        print("----------")
        print(self.cells[7]+" | "+self.cells[8]+" | "+self.cells[9])
    def update_board(self,cell_number,player):
        if self.cells[cell_number]==" ":
            self.cells[cell_number]=player
    def winner(self,player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            print(player + " is winner!")
            return True
        if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            print(player + " is winner!")
            return True
        if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            print(player + " is winner!")
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            print(player + " is winner!")
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            print(player + " is winner!")
            return True
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            print(player + " is winner!")
            return True
        if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            print(player + " is winner!")
            return True
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            print(player + " is winner!")
            return True
    def reset(self):
              self.cells = [" "," "," "," "," "," "," "," "," "," "]  