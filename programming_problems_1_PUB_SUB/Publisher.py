import time
import random
import names
import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind('tcp://*:1234')

lst_sex = ['feminino', 'masculino']
lst_level = ['A', 'B', 'C', 'D']
lst_position = ['operador', 'programador']

while(True):
    n = []
    for i in range(3):
        grade = random.randint(0,10)
        n.append(grade)
    
    #topic:REAJUSTESALARIO
    time.sleep(1)
    topic1 = (names.get_first_name(), random.choice(lst_position), random.random() * 10000)
    
    socket.send_string("REAJUSTESALARIO", flags=zmq.SNDMORE)
    socket.send_json(topic1)

    #topic: MAIORIDADE
    time.sleep(1)
    topic2 = (names.get_first_name(),random.choice(lst_sex), random.randint(0,99))
    
    socket.send_string("MAIORIDADE", flags=zmq.SNDMORE)
    socket.send_json(topic2)

    #topic:APROVACAO
    time.sleep(1)
    topic3 = (n[0], n[1], n[2])

    socket.send_string('APROVACAO',flags=zmq.SNDMORE)
    socket.send_json(topic3)

    #topic:PESO
    time.sleep(1)
    topic4 = (random.randint(50,230), random.choice(lst_sex))

    socket.send_string('PESO', flags=zmq.SNDMORE)
    socket.send_json(topic4)

    #topic:CATEGORIA
    time.sleep(1)
    topic5 = (random.randint(4,99))

    socket.send_string('CATEGORIA', flags=zmq.SNDMORE)
    socket.send_json(topic5)

    #topic: SALARIOLIQ
    time.sleep(1)
    topic6 = (names.get_first_name(), random.choice(lst_level), random.random() * 10000, random.randint(0,1))

    socket.send_string('SALARIOLIQ', flags=zmq.SNDMORE)
    socket.send_json(topic6)

    #topic: APOSENTADORIA
    time.sleep(1)
    topic7 = (random.randint(18,90), random.randint(0, 70))

    socket.send_string('APOSENTADORIA', flags=zmq.SNDMORE)
    socket.send_json(topic7)

    #topic: CREDITO
    time.sleep(1)
    topic8 = (random.randint(0, 1000))

    socket.send_string('CREDITO', flags=zmq.SNDMORE)
    socket.send_json(topic8)
