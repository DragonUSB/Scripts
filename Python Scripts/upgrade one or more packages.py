import sys
import subprocess
from pip._internal.cli.main import main
from colorama import init, Fore

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

# process output with an API in the subprocess module:
# reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
reqs = subprocess.run([sys.executable, '-m', 'pip', 'freeze'], capture_output = True, check = True, text = True)
reqs = reqs.stdout
# installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
installed_packages = [r.split('==')[0] for r in reqs.split()]

# --upgrade to install or update existing packages
for installed in installed_packages:
    print(Fore.GREEN + '--------------------------------------------------')
    print(Fore.GREEN + 'Installed Packages ' + installed)
    print(Fore.GREEN + '--------------------------------------------------')
    main(['install'] + [installed] + ['--upgrade'])