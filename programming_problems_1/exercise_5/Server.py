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

        age = client.recv(64)
        age = age.decode('utf-8')

        age = int(age)

        answer = 'O nadador se enquadra na categoria '
        if age >= 5 and age <= 7:
            answer += 'infantil A.'
        elif age >=8 and age <= 10:
            answer += 'infantil B.'
        elif age >= 11 and age <= 13:
            answer += 'juvenil A.'
        elif age >= 14 and age <= 17:
            answer += 'juvenil B.'
        elif age >= 18:
            answer += 'adulto.'
        
        client.send(bytes(answer, 'utf-8'))

        print('Closing connection!')
        client.close()
        break
