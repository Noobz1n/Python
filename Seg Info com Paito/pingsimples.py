import os

ip_ou_host = input('Digite o IP ou Host a ser verificado: ')

os.system(f'ping -n 6 {ip_ou_host}')