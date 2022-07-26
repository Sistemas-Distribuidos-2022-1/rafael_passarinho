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