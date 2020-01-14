"""
Moduł zawierający różne przydatne funckcje.
"""

import subprocess
import time

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
    cc_list = []
    for actually_file in RESLUT2:
        with open(PATH + '\\' + actually_file, 'r') as open_file:
            try:
                open_file = open_file.read()
                complexity = cc_visit('''{}'''.format(open_file))
                for element in complexity:
                    split_text = str(element).split()
                    split_text_final_lvl = split_text[2].split('.')
                    if len(split_text_final_lvl) > 1:
                        if split_text_final_lvl[1] != '__init__':
                            cc_list.append(str(split_text_final_lvl[1]) + '[{}]'.format(split_text[4]))
                    else:
                        cc_list.append(str(split_text_final_lvl[0]) + '[{}]'.format(split_text[4]))

            except IndentationError as error:
                print(error)
    return cc_list


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


def compare(list1, list2):
    """Funkcja porównująca dwie listy i tworząca nową liste przydatną do cc"""
    compared_list = []
    for element1 in list1:
        split_text = element1.split('[')
        for element2 in list2:
            split_text_next_lvl = element2.split('[')
            if split_text[0] == split_text_next_lvl[0]:
                compared_list.append(element1 + ' [' + split_text_next_lvl[1])
            else:
                pass
    return compared_list


def convert_list_to_list_for_cc(*args):
    """Funkcja konwerująca listy do postaci przydanej do cc"""
    list_for_cc = []
    for actual_list in args:
        for element in actual_list:
            new_element = element + " [0]"
            list_for_cc.append(new_element)
    return list_for_cc


def show_hash_commit():
    """funkcja w terminalu cmd wywoluje sh.exe a w nim wykonuje git loga aktualizujac commity na folder git_log.txt znajdujacy sie w folderze projektu """
    #cmd_command = 'start "" "C:\\Program_Files\\Git\\bin\\sh.exe" --login -i -c "cd C:\\Users\\WIKUS\\PycharmProjects\\IO-ProjectJozin\\ && git --no-pager log > git_log.txt"'
    cmd_command='cd C:\\Users\\WIKUS\\PycharmProjects\\IO-ProjectJozin\\ && git --no-pager log > git_log.txt"'
    proc = subprocess.call(cmd_command, shell=True)
    time.sleep(2)
    with open('./git_log.txt', 'r') as hash_file:
        first_line = hash_file.readline()
        first_line = first_line.split(' ')
        commit = first_line[1]
        commit = commit.replace('\n', '')

        print('actual commit hash  : {}'.format(commit))

        commit_as_list=[]
        commit_as_list.append(commit)
    return commit_as_list
