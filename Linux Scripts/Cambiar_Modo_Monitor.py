#!/bin/python3

import os
import subprocess

mode = 'Monitor'
interfaces = ''
iface = ''

output = subprocess.getoutput('iwconfig')
# out = subprocess.run("iwconfig", shell=True, stdout=subprocess.PIPE)
# output = out.stdout.decode()
for line in output.split('\n'):
    if len(line) == 0: continue
        
    if not line.startswith(' '):
        iface = line.split(' ')[0]
        if '\t' in iface:
            iface = iface.split('\t')[0].strip()

        iface = iface.strip()
        if len(iface) < 5:
            continue

        if mode is None:
            interfaces.append(iface)

    if mode is not None and 'Mode:{}'.format(mode) in line and len(iface) > 0:
        interfaces = iface

down = 'sudo ip link set ' + interfaces + ' down'
subprocess.run(down, shell=True)

managed = 'sudo iw ' + interfaces + ' set type managed' 
subprocess.run(managed, shell=True)

up = 'sudo ip link set ' + interfaces + ' up'
subprocess.run(up, shell=True)

subprocess.run("sudo service NetworkManager start", shell=True)