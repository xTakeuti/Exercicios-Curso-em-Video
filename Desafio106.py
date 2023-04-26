import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print(Fore.BLUE + "="*40)
print("SISTEMA DE AJUDA PyHELP")
print(Fore.BLUE + "="*40)
print(Style.RESET_ALL)

while True:
    comando = input(Fore.YELLOW + "Digite o comando ou biblioteca (FIM para encerrar): ")
    if comando.upper() == "FIM":
        print(Fore.BLUE + "="*40)
        print("FINALIZANDO PyHELP")
        print(Fore.BLUE + "="*40)
        print(Style.RESET_ALL)
        break
    print(Fore.GREEN + "-"*40)
    print(Fore.YELLOW + f"Acessando o manual do comando {comando}...")
    help(comando)
    print(Style.RESET_ALL + "")
