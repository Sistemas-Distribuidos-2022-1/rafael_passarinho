import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('CATEGORIA')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    age = socket.recv_json()

    categoria = ''
    if age >= 5 and age <= 7:
        categoria = 'infantil A.'
    elif age >=8 and age <= 10:
        categoria = 'infantil B.'
    elif age >= 11 and age <= 13:
        categoria = 'juvenil A.'
    elif age >= 14 and age <= 17:
        categoria = 'juvenil B.'
    elif age >= 18:
        categoria = 'adulto.'
    answer = f'{topic} - O(A) nadador(a) tem {age} e se enquadra na categoria {categoria}'
    print(answer)