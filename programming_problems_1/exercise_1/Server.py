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
        
        lst = string.split()
        lst[1] = float(lst[1])

        if lst[0] == 'operador':
            lst[1] *= 1.2
        else:
            lst[1] *= 1.18
        
        msg = str(lst[1])
        client.send(bytes(msg, 'utf-8'))

        print('Closing connection!')
        client.close()
        break
