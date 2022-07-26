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
        msg = conn.recv(SIZE).decode(FORMAT)

        lst = msg.split()
        for i in range(len(lst)):
            lst[i] = float(lst[i])
        
        answer = ''
        mean = (lst[0] + lst[1]) / 2
        if mean >= 7.0:
            answer = 'Aprovado!'
        elif mean < 7 and mean > 3:
            if (mean + lst[2]) / 2 >= 5.0:
                answer = 'Aprovado!'
            else:
                answer = 'Reprovado!'
        else:
            answer = 'Reprovado!'
        
        conn.send(answer.encode(FORMAT))
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