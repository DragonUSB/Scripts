import sys
import subprocess
from pip._internal.cli.main import main
from colorama import init, Fore

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

print('Escriba los paquetes a ser instalados separados por una coma:')
packages = input()

install_packages = [package for package in packages.split(',')]

# install one or more packages
for install in install_packages:
    reqs = main(['show'] + [install])    
    if reqs == 1:
        print(Fore.GREEN + '--------------------------------------------------')
        print(Fore.GREEN + 'Installed Packages ' + install)
        print(Fore.GREEN + '--------------------------------------------------')
        main(['install'] + [install])
    else:
        print(Fore.RED + 'Package ' + install + ' is already installed.')
