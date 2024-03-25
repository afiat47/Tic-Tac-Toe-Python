from board import Board

b=Board()
b.display()

def screen():
    b.display()

while True:
    choice=input("Enter your cell choice (1-9) for X : ")
    choice=int(choice)
    b.update_board(choice,"X")
    screen()
    if b.winner("X"):
        x=input("Want to play again? (Y/N): ")
        if x=='Y':
            b.reset()
            screen()
            continue
        else:
            break
    choice=input("Enter your cell choice (1-9) for O : ")
    choice=int(choice)
    b.update_board(choice,"O")
    screen()
    if b.winner("O"):
        x=input("Want to play again? (Y/N): ")
        if x=='Y':
            b.reset()
            screen()
            continue
        else:
            break