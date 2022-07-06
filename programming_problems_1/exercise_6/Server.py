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
        lst = lst.split()

        salary = float(lst[2])
        lst[3] = int(lst[3])

        if lst[1] == 'A':
            if lst[3] == 0:
                salary -= salary * 0.03
            else:
                salary -=  salary * 0.08
        elif lst[1] == 'B':
            if lst[3] == 0:
                salary -= salary * 0.05
            else:
                salary -= salary * 0.1
        elif lst[1] == 'C':
            if lst[3] == 0:
                salary -= salary * 0.08
            else:
                salary -= salary * 0.15
        elif lst[1] == 'D':
            if lst[3] == 0:
                salary -= salary * 0.10
            else:
                salary -= salary * 0.17
        
        answr = f'O salário líquido do(a) funcionário(a) {lst[0]} será {str(salary)} reais.'

        client.send(bytes(answr, 'utf-8'))

        print('Closing connection!')
        client.close()
        break