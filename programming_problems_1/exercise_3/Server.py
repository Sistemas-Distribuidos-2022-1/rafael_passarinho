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

        for i in range(len(lst)):
            lst[i] = float(lst[i])
        
        answer = ''
        mean = (lst[0] + lst[1]) / 2
        if mean >= 7.0:
            answer = 'Aprovado!'
        elif mean < 7 and mean > 3:
            if (mean + lst[2]) / 2 >= 5.0:
                answer = 'Aprovado!'
            else:
                answer = 'Reprovado!'
        else:
            answer = 'Reprovado!'
        client.send(bytes(answer, 'utf-8'))
        
        print('Closing connection!')
        client.close()
        break