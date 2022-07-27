import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('CREDITO')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    balance = socket.recv_json()

    credit = balance
    if balance >= 201 and balance <= 400:
        credit *= 0.2
    elif balance >= 401 and balance <= 600:
        credit *= 0.3
    elif balance >= 601:
        credit *= 0.4
    
    answer = f'{topic} - Saldo médio: {balance} - Valor de crédito: {round(credit, 2)}'

    print(answer)