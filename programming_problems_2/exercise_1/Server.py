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
        lst[1] = float(lst[1])

        if lst[0] == 'operador':
            lst[1] *= 1.2
        else:
            lst[1] *= 1.18
        
        msg = str(lst[1])
        conn.send(msg.encode(FORMAT))
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