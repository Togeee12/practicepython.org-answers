# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

import random


def search_list(the_list, target_num):
    for num in the_list:
        if num == target_num:
            return True
    return False


def generate_list(size):
    cnt = 0
    list1 = []
    while cnt < size:
        cnt += 1
        list1.append(random.randint(0, 50))

    return list1


def main():
    rand_list = generate_list(10)
    rand_list.sort()
    # print(rand_list)
    user_response = ''
    while user_response != 'exit':
        user_response = input(
            "Type 'exit' to quit or enter a number to search for in the list (1-1000): ")
        if user_response.isnumeric():
            user_response = int(user_response)
            while user_response >= 1 and user_response <= 50:
                result = search_list(rand_list, user_response)
                print(result)
                if result == True:
                    print(
                        f"Element found at location {rand_list.index(user_response)+ 1}!! Exiting program")
                    print()
                    print(rand_list)
                    user_response = 'exit'
                    break
                else:
                    user_response = -1
                    print("Element not found, try again")
        elif user_response == 'exit':
            break


main()
