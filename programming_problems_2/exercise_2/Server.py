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
        sex = lst[1]
        age = int(lst[2])

        if sex == 'masculino':
            if age >= 18:
                answer = f'{lst[0]} já atingiu a maior idade!\n'
            else:
                answer = f'{lst[0]} não atingiu a maior idade!\n'
        else:
            if age >= 21:
                answer = f'{lst[0]} já atingiu a maior idade!\n'
            else:
                answer = f'{lst[0]} não atingiu a maior idade!\n'
        
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



