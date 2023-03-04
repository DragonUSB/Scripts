import sys
import subprocess
from pip._internal.cli.main import main
from colorama import init, Fore

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

print('Escriba los paquetes a ser instalados separados por una coma:')
packages = input()

install_packages = [package for package in packages.split(',')]

reqs = subprocess.run([sys.executable, '-m', 'pip', 'freeze'], capture_output = True, check = True, text = True)
reqs = reqs.stdout
installed_packages = [r.split('==')[0] for r in reqs.split()]

# install one or more packages
for install in install_packages:
    value = False
    for installed in installed_packages:
        if install == installed:
            print('Package ' + install + ' is already installed.')
            value = True
    if value == False:
        print(Fore.GREEN + '--------------------------------------------------')
        print(Fore.GREEN + 'Installed Packages ' + install)
        print(Fore.GREEN + '--------------------------------------------------')
        main(['install'] + [install])