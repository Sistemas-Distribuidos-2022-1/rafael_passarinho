import socket 

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    height = input('Altura: ')
    sex = input('Sexo: ')

    server.send(bytes(' '.join([height, sex]), 'utf-8'))

    answer = server.recv(128)
    answer = answer.decode('utf-8')

    print(answer)