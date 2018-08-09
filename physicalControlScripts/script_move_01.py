#!/usr/bin/env python
# Echo client program
import socket
import time

HOST1 = "10.74.48.221"    # The remote host for Manipulator A
HOST2 = "10.74.48.213"    # The remote host for Manipulator B
PORT = 30002              # The same port as used by the server

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((HOST1, PORT))

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST2, PORT))


print("Sending movej\n")
s1.send("movej([0.0, -1.571, 1.571, 0.0, 0.0, 0.0], a=1.2, v=0.25)" + "\n")
time.sleep(3)

'''
print("Getting TCP pose\n")
s1.send("get_actual_tcp_pose()" + "\n")
data = s1.recv(1024)
print ("Received", repr(data))
time.sleep(1)
'''

print("Sending movel\n")
s1.send("movel(p[-0.627, -0.270, 0.645, 1.51, 0.462, -0.433], a=1.2, v=0.25, t=0, r=0)" + "\n")
time.sleep(3)


s1.close()
s2.close()
