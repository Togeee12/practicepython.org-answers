# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

a = True
while a == True:
    input1 = input("Rock | Paper | Scissors : ")
    input2 = input("Rock | Paper | Scissors : ")
    while input1 == input2:
        input1 = input("Rock | Paper | Scissors : ")
        input2 = input("Rock | Paper | Scissors : ")
    if input1 == "Rock" and input2 == "Scissors":
        print("Player 1 wins")
    elif input1 == "Scissors" and input2 == "Paper":
        print("Player 1 wins")
    elif input1 == "Paper" and input2 == "Rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
    question = input("Do you want to play again? Y/N: ")
    if question == "Y":
        a = True
    elif question == "N":
        a = False
    else:
        print("Something went wrong, try again")
