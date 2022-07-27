import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('APROVACAO')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    answer = f'{topic} - ERRO ERRO!'
    mean = (lst[0] + lst[1]) / 2
    if mean >= 7.0:
        answer = 'aprovado!'
    elif mean < 7 and mean > 3:
        if (mean + lst[2]) / 2 >= 5.0:
            answer = 'aprovado!'
        else:
            answer = 'reprovado!'
    else:
        answer = 'reprovado!'
    
    print(f'{topic} - O(A) aluno(a) tirou as notas {lst[0]}, {lst[1]}, {lst[2]} e foi {answer}')