import socket
import smtplib as smtp
from requests import get
from getpass import getpass


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text

#почта, с которой будет отпрвляться письмо
email = '***'
password = '***'

#почта, куда будет присылаться письмо
dest_email = '****'

subject = 'IP'
email_text = (f'Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}')

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)

server = smtp.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()





#print(f'Хост: {hostname}')
#print(f'Локальный IP: {local_ip}')
#print(f'Публичный IP: {public_ip}')

