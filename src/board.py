board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_board():
    for i in range(1, 20):
        print("-", end="")
    print()

    for i in range(1, 10):
        print("| ", board[i-1], " ", end="")
        if i % 3 == 0:
            print("| ")

    for i in range(1, 20):
        print("-", end="")
    print()

