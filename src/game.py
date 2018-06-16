from gameCore import *
from board import *


def main():
    print_board()
    print(" Choose your Symbol ")
    print("    User 1 - X      ")
    print("    User 2 - O      ")

    t = 1
    while t <= 9:

        turn(t)
        print_board()
        t += 1
        res = check_win()
        if res is not False:
            print(res)
            break
    else:
        print("Draw")


main()

