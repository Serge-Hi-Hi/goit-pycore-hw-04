import sys
from pathlib import Path
from colorama import  Fore, Style, init

init()

if len(sys.argv) < 2 :
    print('Будь ласка, вкажіть шлях до директорії')
    sys.exit(1)

directory_path = Path(sys.argv[1])

if not directory_path.exists():
    print('Вказаний шлях не існує')
    sys.exit(1)

if not directory_path.is_dir():
    print('Вказаний шлях не є директорією')
    sys.exit(1)

def display_tree(directory:Path, indent: str= ''):
    print(Fore.YELLOW + indent + directory.name + Style.RESET_ALL)

    for item in directory.iterdir():
        if item.is_dir():
            display_tree(item, indent + '  ')
        else:
            print(Fore.GREEN + indent + item.name + Style.RESET_ALL )

display_tree(directory_path)