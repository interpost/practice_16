from random import randint


board = []

rules = str(input(
    "Хотите сыграть в морской бой ?" "(" + '\x1b[1;31;1m' + 'n' + '\x1b[0m' + "/" + '\x1b[1;32;1m' + 'y' + '\x1b[0m' + ")"))

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):

    print("Поиграем в морской бой !")
    if rules == "n":
        print()
        print(
            "За ограниченное количество ходов, нужно потопить корабль")
        print()
    print("Удачи!")
    print()
    print("МОРСКОЙ БОЙ")
    print("  0|1|2|3|4|5")
    for row in range(len(board)):
        print(str(row) + "|" + "|".join(board[row]))
    print()


print_board(board)


def random_row(board):
    return (randint(0, len(board) - 1))


def random_col(board):
    return (randint(0, len(board[0]) - 1))

ship_row = random_row(board)
ship_col = random_col(board)

p1 = str(input("Введите своё имя : "))


for turn in range(6):
    print("Turn", turn)

    guess_col = int(input("Guess Col:"))
    guess_row = int(input("Guess Row:"))

    if guess_row == ship_row and guess_col == ship_col:
        print()
        print('\x1b[1;32;1m' + 'Поздравляем' + '\x1b[0m' + " " + p1 + ", " + 'Вы потопили корабль!')
        break
    else:
        if ((guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6)):

            print()
            print("Это- вне игры")
        elif (board[guess_row][guess_col] == "•"):
            print()
            print("Догадались?")
        else:
            board[guess_row][guess_col] = "•"
            print()
            print("Пропустили корабль !")
            if turn == 6:
                print('\x2b[1;31;1m' + 'Game' + '\x1b[0m' + " " + '\x1b[1;31;1m' + 'Over.' + '\x1b[0m')
                print()
                break
        print_board(board)

