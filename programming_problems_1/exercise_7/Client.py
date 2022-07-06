import socket 

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    age = input('Idade: ')
    service_time = input('Tempo de serviço: ')

    server.send(bytes(' '.join([age, service_time]), 'utf-8'))

    response = server.recv(128)
    response = response.decode('utf-8')

    print(response)
