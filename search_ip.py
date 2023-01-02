import socket
#import smtplib as smtp
from requests import get
#from getpass import getpass


hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text

print(f'Хост: {hostname}')
print(f'Локальный IP: {local_ip}')
print(f'Публичный IP: {public_ip}')

