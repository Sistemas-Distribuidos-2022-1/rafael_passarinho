import socket
import threading

IP = 'localhost'
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        balance = conn.recv(SIZE).decode(FORMAT)

        balance = int(balance)
        credit = balance
        if balance >= 201 and balance <= 400:
            credit *= 0.2
        elif balance >= 401 and balance <= 600:
            credit *= 0.3
        elif balance >= 601:
            credit *= 0.4
        
        answer = f'Saldo médio: {balance} - Valor de crédito: {credit}'
        
        conn.send(str(answer).encode(FORMAT))
        connected = False
        print(f'[{addr}] !DISCONNECT')
    
    conn.close()

def main():
    print('[STARTING] Server is starting...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f'[LISTENING] Server is listening on {IP}: {PORT}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTION] {threading.activeCount() - 1}')

if __name__ == '__main__':
    main()