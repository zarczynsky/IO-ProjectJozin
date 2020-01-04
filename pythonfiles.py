"""
Moduł służący do operacji wyszukiwania plików o danym rozszerzeniu w danym katalogu.
"""

import glob
from os import *


class FileInDirectory:
    """Klasa obsłuhująca przeszukiwanie katalogów"""

    def __init__(self):
        self.python_file = []

    def list_directory(self, directory, extd):
        """funkcja, która wyszukuje wszystkie pliki o danym rozszerzeniu(extd) w danym katalogu(directory)"""
        for actuale_file in glob.glob('{}*.{}'.format(directory, extd)):
            self.python_file.append(path.split(actuale_file)[1])

        return self.python_file
