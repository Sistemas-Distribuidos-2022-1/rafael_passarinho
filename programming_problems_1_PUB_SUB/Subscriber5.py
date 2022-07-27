from unicodedata import category
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('CATEGORIA')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    categoria = ''
    if lst[0] >= 5 and lst[0] <= 7:
        categoria += 'infantil A.'
    elif lst[0] >=8 and lst[0] <= 10:
        categoria += 'infantil B.'
    elif lst[0] >= 11 and lst[0] <= 13:
        categoria += 'juvenil A.'
    elif lst[0] >= 14 and lst[0] <= 17:
        categoria += 'juvenil B.'
    elif lst[0] >= 18:
        categoria += 'adulto.'
    answer = f'{topic} - O(A) nadador(a) tem {lst[0]} e se enquadra na categoria {categoria}!'
    print(answer)