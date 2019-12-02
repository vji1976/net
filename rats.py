#!/usr/bin/env python3
import os
import socket, sys
import threading as th

def conHandler(c, a):
	while True:
		print("You are blocking receiving data\n\n")
		data = conn.recv(1024)
		if not data:
			msg = "+ {} has disconnected server says: goodbye".format(client_addrs[0])   # terrible list handling
			print(msg)
			conn.send(msg.encode("utf-8"))
			conn.close()			
			break
		print("{} bytes of data received".format(len(data)))
		print(data.decode("utf-8"))
		txt = data.decode("utf-8").upper()
		msg = "+ {} says: {}\n".format(addr, txt)
		conn.send(msg.encode("utf-8"))	

SIP = '0.0.0.0'
SPORT = 4800
ADDR = (SIP, SPORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(ADDR)
server_sock.listen(2)		# 2 just to add one addtional connection
				# in non threaded host
client_socks = []
client_addrs = []

print("SERVER@{} LISTENING".format(ADDR))

while True:
	print("You are blocking waiting for connection")
	conn, addr = server_sock.accept()
	client_socks.append(conn)
	client_addrs.append(addr)
	print("+ " + "{} connected".format(addr))
	client_thread = th.Thread(target=conHandler, args=(conn, addr))
	client_thread.daemon = True
	client_thread.start()