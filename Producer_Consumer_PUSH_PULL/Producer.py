import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind('tcp://127.0.0.1:5557')

    #start your result manager and workers beforer you start producers
    num = 0
    while num < 2000:
        time.sleep(.05)
        work_message = {'num': num}
        zmq_socket.send_json(work_message)
        num += 1

producer()