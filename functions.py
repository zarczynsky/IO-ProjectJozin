"""
Moduł zawierający różne przydatne funckcje.
"""

from radon.complexity import cc_visit

import pythonfiles

FILES_WITH_CODE = pythonfiles.FileInDirectory()
PATH = r'.\\'
EXTEND = 'py'
RESLUT2 = FILES_WITH_CODE.list_directory(PATH, EXTEND)  # przeszukanie katalogu ,aby znaleźć pliki z rozszerzeniem py

MY_CATALOG = []  # lista przechowująca liste plików
for actual_element in RESLUT2:
    MY_CATALOG.append(actual_element.split('.')[0])


def counting_lines_of_code(element):
    """  funkcja podająca rozmiar pliku w linijkach kodu"""
    try:
        with open(PATH + '\\' + element, 'r') as open_file:
            lines = 0
            for line in open_file:
                if line != '\n':
                    lines += 1
            return lines

    except IndexError as error:
        print(error)
        print("Lack of file")


def write_to_file_fun_data(list1, list2):
    """ funkcja zliczająca wagę połączeń"""
    lista3 = []
    for element in list1:
        counter = -1
        for next_element in list2:
            if element == next_element:
                counter += 1
        lista3.append(str(counter))
    return lista3


def cyclomatic_complexity():
    """ funkcja obliczająca złożoność cyklometryczną kodu"""
    for actually_file in RESLUT2:
        with open(PATH + '\\' + actually_file, 'r') as open_file:
            try:
                open_file = open_file.read()
                complexity = cc_visit('''{}'''.format(open_file))
                for element in complexity:
                    split_text = str(element).split()
                    split_text_final_lvl = split_text[2].split('.')
                    with open('cc.txt', 'a') as next_open_file:
                        if len(split_text_final_lvl) > 1:
                            if split_text_final_lvl[1] != '__init__':
                                next_open_file.write(str(split_text_final_lvl[1]) + '[{}]'.format(split_text[4]) + '\n')
                        else:
                            next_open_file.write(str(split_text_final_lvl[0]) + '[{}]'.format(split_text[4]) + '\n')

            except IndentationError as error:
                print(error)


def menu():
    """Funkcja drukiująca opcje menu"""
    print("Menu:")
    print("1.Pliki")
    print("2.Funkcje")
    print("3.Moduły")
    print("4.Pliki i funkcje")
    print("5.Pliki i moduły")
    print("6.Funkcje i moduły")
    print("7.Pliki, funkcje i moduły")
    choice = int(input("Wybierz co chciałbyś zobaczyć na grafie."))
    return choice
