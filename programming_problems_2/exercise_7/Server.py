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
        lst = conn.recv(SIZE).decode(FORMAT)

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
        
        conn.send(str(answr).encode(FORMAT))
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