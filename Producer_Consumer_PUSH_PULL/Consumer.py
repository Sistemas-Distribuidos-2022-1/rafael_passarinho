import time
import zmq
import random

def consumer():
    consumer_id = random.randrange(1, 10005)
    print("I'm consumer ", consumer_id)
    context = zmq.Context()

    #receive work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect('tcp://127.0.0.1:5557')

    #send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect('tcp://127.0.0.1:5558')

    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = {'consumer': consumer_id, 'num': data}
        if data % 2 == 0:
            consumer_sender.send_json(result)

consumer()