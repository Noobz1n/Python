import os
from time import sleep


with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f'Verificando o ip: {ip}')
        print('-'*50)
        os.system(f'ping -n 2 {ip}')
        print('-'*50)
        sleep(3)