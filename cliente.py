 # -*- coding: utf-8 -*-
import socket
TCP_IP = "127.0.0.1"
TCP_PORT = 8895
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
print "Si desea informacion del servidor, presione q"
while True:
	data = s.recv(BUFFER_SIZE)
	
	print "EL server dijo: \n", data
	msg = raw_input("Ingrese un texto: ")
	if msg != 0:
		s.send(msg)
	elif msg == "q":
		dat = s.recv(512)
		print dat
		#print "Su peticion: " ,peticion
	else:
		print "Hasta luego"
		s.close()
