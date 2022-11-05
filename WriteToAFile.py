# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

def get_names_from_file(gender="Male"):

    def choose_gender_of_name(file_bufor, gender):

        GENDER_DICTIONARY = {"Rank": 0, "Male": 1, "Female": 2}

        names_bufor = []
        for line in range(1, len(file_bufor)):
            names_bufor.append(file_bufor[line][GENDER_DICTIONARY[gender]])
        return names_bufor

    file = open('22_Read From File.txt', 'r', encoding="utf-8")
    file_bufor = []

    for line in file:
        file_bufor.append(line.split())

    file.close()

    return choose_gender_of_name(file_bufor, gender)


print("--------------------------------------------")
print("Program gets a list of names from file!")


print(get_names_from_file("Male"))
print(get_names_from_file("Female"))
