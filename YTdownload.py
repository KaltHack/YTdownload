from pytube import YouTube
from colorama import Fore, Back, Style
print(" ")
print(Back.WHITE, Fore.RED, " ▄▄▄▄▄▄▄▄▄▄▄  ", Back.RESET)
print(Back.WHITE, Fore.RED, "█████ ▀██████ ", Back.RESET)
print(Back.WHITE, Fore.RED, "█████   ▀████ ", Back.RESET)
print(Back.WHITE, Fore.RED, "█████   ▄████ ", Back.RESET)
print(Back.WHITE, Fore.RED, "█████ ▄██████ ", Back.RESET)
print(Back.WHITE, Fore.RED, " ▀▀▀▀▀▀▀▀▀▀▀  ", Back.RESET)

print(Style.RESET_ALL)


link = input(Fore.WHITE + "Coloca el link de YouTube que deseas descargar" + Fore.RED + "\n> ")

Style.RESET_ALL

YouTube(link).streams.first().download()

print(Fore.RED + f'"{YouTube(link).title}" Ha sido descargado correctamente!')