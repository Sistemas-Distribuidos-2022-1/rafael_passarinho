import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('MAIORIDADE')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    answer = f'{topic} - ERRO ERRO!'
    if lst[1] == 'masculino':
        if lst[2] >= 18:
            answer = f'{topic} - {lst[0]} tem {lst[2]} anos e já atingiu a maior idade penal'
        else:
            answer == f'{topic} - {lst[0]} tem {lst[2]} anos e não atingiu a maior idade penal'
    else:
        if lst[2] >= 21:
            answer = f'{topic} - {lst[0]} tem {lst[2]} anos e já atingiu a maior idade penal'
        else:
            answer = f'{topic} - {lst[0]} tem {lst[2]} anos e não atingiu a maior idade penal'
    
    print(answer)