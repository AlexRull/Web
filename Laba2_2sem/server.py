import socket
import time
from json import dumps
from threading import Thread

connections_array = []
connect_time_array = []
start_time = 0
connections_amount = 0
sockets = []
connections_list = {}
sock = socket.socket()
sock.bind(('', 5050))
sock.listen(13)


def sending(connections_array):
    for i in range(13):
        convert_to = dumps(connections_array)
        sockets[i].send(convert_to.encode("utf-8"))
        i = i + 1
    print("23 seconds passed, data sent to clients, current time: ", time.ctime())


def timer(connections_array):
    while time.process_time() < 23:
        do_nothing = 0
    else:
        sending(connections_array)


while True:

    conn, addr = sock.accept()
    time.sleep(0.1)
    connections_amount = connections_amount + 1
    if connections_amount == 1:
        start_time = time.ctime()
        print("first connections, timer starts at", start_time)
        th_1 = Thread(target=timer, args=(connections_array,))
        th_1.start()
        connections_array.append(start_time)
    connection_time = time.ctime()
    data = conn.recv(4096)
    if not data:
        break
    print("№", connections_amount, ", client info: ", data.decode('utf-8'), addr)
    print("connection time: ", connection_time, "\n")
    connections_list = {"name: ": data.decode('utf-8'), "adress: ": addr, "connection time: ": connection_time}
    connections_array.append(connections_list)
    sockets.append(conn)
