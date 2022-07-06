import socket

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    #SOCK_STREAM is the protocol we are using to communicate here, using TCP protocoll
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)

    while True:
        client, address = server.accept()
        print(f'Connection Established - {address[0]}: {address[1]}')

        string = client.recv(128)
        string = string.decode('utf-8')

        lst = string.split(' ')

        lst[0] = float(lst[0])

        if lst[1] == 'feminino':
            answer = (62.1 * lst[0]) - 44.7
        else:
            answer = (72.7 * lst[0]) - 58

        client.send(bytes(str(answer), 'utf-8'))

        print('Closing connection!')
        client.close()
        break