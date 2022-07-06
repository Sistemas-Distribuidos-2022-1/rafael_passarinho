import socket 

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    N1 = input('N1: ')
    N2 = input('N2: ')
    N3 = input('N3: ')

    server.send(bytes(' '.join([N1, N2, N3]), 'utf-8'))

    answer = server.recv(128)
    answer = answer.decode('utf-8')

    print(answer)