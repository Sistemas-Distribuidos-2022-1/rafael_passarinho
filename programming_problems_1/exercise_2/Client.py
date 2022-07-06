import socket

if __name__ == '__main__':
    ip = 'localhost'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    name = input('Nome: ')
    sex = input('Sexo: ')
    age = input('Idade: ')
    server.send(bytes(' '.join([name, sex, age]), 'utf-8'))

    answer = server.recv(128)
    answer = answer.decode('utf-8')

    print(f'Server:{answer}')