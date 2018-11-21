
import time
import random


from multiprocessing import Process, Pipe

def myprocess(conn):

    while True:
        time.sleep(0.1)
        if conn.poll():
            data_from_parent = conn.recv()
            print('received from parent', data_from_parent)

        if random.random() <= 0.1:
            value = time.time()
            print('child sending      ', value)
            conn.send(value)


if __name__ == '__main__':
    parent_conn, child_conn = Pipe(duplex=True)
    p = Process(target=myprocess, args=(child_conn,))
    p.start()
    while True:
        time.sleep(0.1)

        if random.random() <= 0.1:
            value = time.time()
            print('parent sending      ', value)
            parent_conn.send(value)

        if parent_conn.poll():
            data_from_child = parent_conn.recv()
            print('received from child', data_from_child)
    p.join()
