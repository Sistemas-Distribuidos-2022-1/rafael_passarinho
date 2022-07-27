import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('APOSENTADORIA')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    answr = f'{topic} - A pessoa tem {lst[0]} anos e {lst[1]} anos de serviço e não pode se aposentar.'

    if lst[0] >= 60 and lst[1] >= 25:
        answr = f'{topic} - A pessoa tem {lst[0]} anos e {lst[1]} anos de serviço e pode se aposentar!'
    elif lst[1] >= 30:
        answr = f'{topic} - A pessoa tem {lst[0]} anos e {lst[1]} anos de serviço e pode se aposentar!'
    elif lst[0] >= 65:
        answr = f'{topic} - A pessoa tem {lst[0]} anos e {lst[1]} anos de serviço e pode se aposentar!'
    
    print(answr)