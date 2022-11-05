# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

length = int(input("Please enter a size of the game board: "))

for length in range(length):
    print(" --- " * length)
    print("|   |" * length)
    if length == length - 1:
        print(" --- " * (length))
