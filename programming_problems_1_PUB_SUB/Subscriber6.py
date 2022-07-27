import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('SALARIOLIQ')

for _ in range(10): # 10 iterations
    topic = socket.recv_string()
    lst = socket.recv_json()

    salary = lst[2]
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
    print(f'{topic} - {lst[0]} terá o salário líquido de {round(salary,3)} reais')
