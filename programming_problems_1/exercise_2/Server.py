import socket

if __name__ == '__main__':
    ip = 'localhost'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)

    while True:
        client, address = server.accept()
        print(f'Connection Established - {address[0]}: {address[1]}')

        string = client.recv(128)
        string = string.decode('utf-8')

        lst = string.split()

        answer = ''
        lst[2] = int(lst[2])
        if lst[1] == 'masculino':
            if lst[2] >= 18:
                answer = f'{lst[0]} já atingiu a maior idade!'
            else:
                answer = f'{lst[0]} não atingiu a maior idade!'
        else:
            if lst[2] >= 21:
                answer = f'{lst[0]} já atingiu a maior idade!'
            else:
                answer = f'{lst[0]} não atingiu a maior idade!'
        
        client.send(bytes(answer, 'utf-8'))

        print('Closing Connection!')
        client.close()
        break