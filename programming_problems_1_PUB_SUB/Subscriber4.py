import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('PESO')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    answer = f'{topic} - ERRO ERRO!'
    if lst[1] == 'feminino':
        answer = (62.1 * lst[0]) - 44.7
    else:
        answer = (72.7 * lst[0]) - 58
    
    print(f'{topic} - A altura da pessoa é {lst[0]} cm e o seu peso ideial deve ser {answer}')