import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://localhost:1234"  # how and where to communicate
socket.connect(p) # connect to the server
socket.subscribe('REAJUSTESALARIO')

for _ in range(10): # 10 iterations
	topic = socket.recv_string()
	lst = socket.recv_json()
	
	if lst[1] == 'operador':
		lst[2] *= 1.2
	else:
		lst[2] *= 1.18
	
	print(f'{topic} - {lst[0]} - salário reajustado: {round(lst[2],3)}')