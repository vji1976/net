#!/usr/bin/env python3
import os
import socket
import sys
import threading as th
import tkinter as tk

SIP = '0.0.0.0'
PORT = 5000
ADDR = (SIP, PORT)
global console

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

def drawgui():
	root = tk.Tk()
	global console = tk.Text(root, height=20, width=100)
	console.grid(row=0, column=0, sticky='nsew', padx=4, pady=10)
	console.insert('1.0', f"SERVER LISTENING ON {SIP}")
	root.mainloop()
	
gui_thread = th.Thread(target=drawgui)
gui_thread.daemon = True
gui_thread.start()

while True:
	c, a = s.accept()
	console.insert(tk.END, f"{c} CONNECTED\n")
