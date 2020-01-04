"""
Moduł służący do operacji na plikach.
"""

import functions


class Files:
    """Klasa zawierająca metody do operacji na plikach"""
    def __init__(self):
        Files.filesConnectionList = []
        Files.filesConnectionWeight = []

    FilesConnectionList = []
    FilesConnectionWeight = []


    @classmethod
    def checking_weight_of_connections_between_files(cls,
                                                     actually_file,
                                                     connect_file):
        """ funkcja sprawdzająca jak pliki są połaczone z sobą"""
        try:
            with open(functions.PATH + '\\' + actually_file, 'r') as open_file:
                weight = 0
                for line in open_file:
                    split_text = line.split()  # zmienna zawierająca elemnty danej linijki kodu
                    if split_text and split_text[0] != 'import':
                        for element in split_text:
                            split_text_next_lvl = element.split(
                                '.')  # zmienna zawierająca elementy z zmiennej polaczenia
                            for el_next in split_text_next_lvl:
                                if el_next == str(connect_file):
                                    weight += 1
            return weight


        except IndexError as error:
            print(error)
            print("Lack of file")


    @classmethod
    def checking_connections_between_files(cls, file_list):
        """ funkcja, która sprawdza jakie pliki są z sobą połaczone """
        try:
            for actually_file in file_list:
                element = actually_file.split(".")
                connect_file_list = []
                with open(functions.PATH + '\\' + actually_file, 'r') as open_file:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    for line in open_file:
                        split_text = line.split()
                        if split_text and (split_text[0] == 'import' or split_text[0] == "from"):
                            for file in functions.MY_CATALOG:
                                if split_text[1] == file:
                                    connect_file_list.append(split_text[1])
                for amount in enumerate(connect_file_list):
                    numbers_of_code_lines_of_actually_connected_file = functions.counting_lines_of_code(
                        connect_file_list[amount[0]] + ".py")
                    file_connection_weight = cls.checking_weight_of_connections_between_files(actually_file,
                                                                                              connect_file_list[amount[0]])

                    Files.filesConnectionList.append(element[0] + "[{}]".format(numbers_of_code_lines_of_actually_file))
                    Files.filesConnectionList.append(str(
                        connect_file_list[amount[0]]) + "[{}]".format(numbers_of_code_lines_of_actually_connected_file))
                    Files.filesConnectionWeight.append(str(file_connection_weight))

        except IndexError as error:
            print(error)
            print("Lack of file")
