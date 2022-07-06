import socket 

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    name = input('Nome: ')
    level = input('Nível: ')
    salary = input('Salário bruto: ')
    dependents = input('Número de dependentes: ')

    server.send(bytes(' '.join([name, level, salary, dependents]), 'utf-8'))

    response = server.recv(128)
    response = response.decode('utf-8')

    print(response)