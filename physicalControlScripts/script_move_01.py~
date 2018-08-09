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

print("Setting O2 on Manipulator A\n")
s1.send ("set_digital_out(2,True)" + "\n")
data = s1.recv(1024)
print ("Received", repr(data))

time.sleep(2)
print("Setting O2 on Manipulator B\n")
s2.send ("set_digital_out(2,True)" + "\n")
data = s2.recv(1024)
print ("Received", repr(data))

time.sleep(2)
print("Clearing O2 on Manipulator A\n")
s1.send ("set_digital_out(2,False)" + "\n")
data = s1.recv(1024)
print ("Received", repr(data))

time.sleep(2)
print("Clearing O2 on Manipulator B\n")
s2.send ("set_digital_out(2,False)" + "\n")
data = s2.recv(1024)
print ("Received", repr(data))

s1.close()
s2.close()
