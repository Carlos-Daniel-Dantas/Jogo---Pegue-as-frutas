import os
import sys

def caminho_relativo(caminho):
    try:
        base = sys._MEIPASS
    except AttributeError:
        base = os.path.abspath(".")

    return os.path.join(base, caminho)

