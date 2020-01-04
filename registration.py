"""
Moduł służący do operacji zapisania danych do pliku.
"""

import files
import function
import modules


class Registration(files.Files, function.Functions, modules.Modules):
    """Klasa zawierająca metody zapisujące dane do plików"""

    def __init__(self):
        pass

    @classmethod
    def write_to_file(cls, sub, *args):
        """Funkcja zapisująca wszystkie dane do pliku graf_jozin.txt"""
        with open('graf_jozin.txt', 'a') as open_file:
            if sub != "":
                open_file.write(sub.upper() + "\n")
            for arg in args:
                for element in arg:
                    open_file.write(element)
                    open_file.write("\n")
            open_file.write("dane\n")
