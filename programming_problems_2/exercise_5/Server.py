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
        age = conn.recv(SIZE).decode(FORMAT)

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