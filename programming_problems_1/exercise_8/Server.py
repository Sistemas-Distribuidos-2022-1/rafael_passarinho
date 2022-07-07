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

        balance = client.recv(64)
        balance = balance.decode('utf-8')

        balance = int(balance)
        credit = balance
        if balance >= 201 and balance <= 400:
            credit *= 0.2
        elif balance >= 401 and balance <= 600:
            credit *= 0.3
        elif balance >= 601:
            credit *= 0.4
        
        answer = f'Saldo médio: {balance} - Valor de crédito: {credit}'

        client.send(bytes(answer, 'utf-8'))

        print('Closing connection!')
        client.close()
        break