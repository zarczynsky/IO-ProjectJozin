"""
Moduł służący do operacji na funkcjach.
"""

import functions


class Functions:
    """Klasa zawierająca metody do operacji na funckajach"""

    def __init__(self):
        Functions.functionsConnectionList = []
        Functions.functionsConnectionWeight = []

    FunctionsConnectionList = []
    FunctionsConnectionWeight = []

    @classmethod
    def checking_connections_between_functions1(cls, file_list):
        """ funkcja sprawdzająca jak funkcje są połączone z sobą"""
        try:
            functions_list = []
            for actually_file in file_list:
                with open(functions.PATH + '\\' + actually_file, 'r') as open_file:
                    for line in open_file:
                        split_text = line.split()
                        if split_text and split_text[0] == "def":
                            tmp = split_text[1].split('(')
                            if tmp[0] != "__init__":
                                functions_list.append(tmp[0])

            return functions_list

        except IndexError as error:
            print(error)
            print("Lack of file")

    @classmethod
    def checking_connections_between_functions(cls, file_list,
                                               weight_list):
        """ funkcja sprawdzająca jak funkcje są połączone z sobą"""
        try:
            i = 0
            for actually_file in file_list:
                element = actually_file.split(".")
                with open(functions.PATH + '\\' + actually_file, 'r') as open_file:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    for line in open_file:
                        split_text = line.split()
                        if split_text and split_text[0] == "def":
                            tmp = split_text[1].split('(')
                            if tmp[0] != "__init__":
                                Functions.functionsConnectionList.append(tmp[0] + "[{}]".format(str(weight_list[i])))
                                Functions.functionsConnectionList.append(
                                    element[0] + "[{}]".format(numbers_of_code_lines_of_actually_file))
                                i += 1
            for element in range(int(len(Functions.functionsConnectionList) / 2)):
                Functions.functionsConnectionWeight.append(str(1))

        except IndexError as error:
            print(error)
            print("Lack of file")

    def checking_weight_of_connections_between_functions(self, file_list,
                                                         function_list):
        """ funkcja sprawdzająca wagi połączeń między funkcjami"""
        try:
            how_many_function = []
            for actually_fun in function_list:
                for actually_file in file_list:
                    with open(functions.PATH + '\\' + actually_file, 'r') as open_file:
                        for line in open_file:
                            split_text = line.split()
                            if split_text and split_text[0] != 'import':
                                for element in split_text:
                                    split_text_next_lvl = element.split('.')
                                    for el_next in split_text_next_lvl:
                                        split_text_final_lvl = el_next.split('(')
                                        if actually_fun == split_text_final_lvl[0]:
                                            how_many_function.append(split_text_final_lvl[0])
            return how_many_function

        except IndexError as error:
            print(error)
            print("Lack of file")
