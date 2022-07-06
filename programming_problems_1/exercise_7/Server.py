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

        message = client.recv(128)

        lst = message.decode('utf-8')
        age, service_time = lst.split()
        age = int(age)
        service_time = int(service_time)
        answr = 'Não pode se aposentar.'

        if age >= 60 and service_time >= 25:
            answr = 'Pode se aposentar!'
        elif service_time >= 30:
            answr = 'Pode se aposentar!'
        elif age >= 65:
            answr = 'Pode se aposentar!'

        client.send(bytes(answr, 'utf-8'))

        print('Closing connection!')
        client.close()
        break
        