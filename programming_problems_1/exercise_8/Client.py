import socket

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    balance = input('Saldo médio: ')

    server.send(bytes(balance, 'utf-8'))

    response = server.recv(64)
    response = response.decode('utf-8')

    print(response)