import socket

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    name = input('Nome: ')
    position = input('Position: ')
    salary = input('Salário: ')
    server.send(bytes(' '.join([position, salary]), 'utf-8'))
    
    buffer = server.recv(128)
    buffer = buffer.decode('utf-8')

    print(f'{name} - salário reajustado: {buffer}')