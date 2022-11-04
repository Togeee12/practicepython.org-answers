# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

user_list = list()

# Taking the user input and modifying the list


def makelist():
    while True:
        user_elements = input("Enter the numeric elements: ")
        if user_elements == "done":
            break
        else:
            try:
                int_elements = int(user_elements)
            except:
                print("Please Type an integer!")
                continue
            user_list.append(int_elements)
    return first_last(user_list)

# Returning required list


def first_last(testlist):
    new_list = list()
    new_list.append(testlist[0])
    new_list.append(testlist[len(testlist) - 1])
    return new_list


print(makelist())
