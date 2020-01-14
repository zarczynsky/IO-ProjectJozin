"""Moduł uruchamiający kod rysujący graf w c++"""
import subprocess
import time


def open_draw_grapf_exe():
    """funkcja w terminalu cmd odpala exe modułu napisanego w cpp rysującego graf """
    cmd_command = 'start "" ".\\Graph_Drawing.exe"'
    proc = subprocess.call(cmd_command, shell=True)
    time.sleep(2)
