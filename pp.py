 # -*- coding: utf-8 -*-
import socket
import sys
from thread import *
from subprocess import Popen, PIPE

diction = {
			"Arandano":"Arbusto de tallo reptante, ramas erectas, hojas alternas y ovaladas, con pecíolo corto, de color verde claro, flores blancas o rosadas y fruto en forma de baya esférica; puede alcanzar hasta 60 cm de altura",
			"Frambuesa":"Fruto del frambueso, comestible, de color rojo más oscuro que el de la fresa, olor suave y sabor agridulce",
			"Marañon":"Árbol de tronco irregular, hojas ovaladas, flores en racimo y fruto en forma de pera, sostenido por un pedúnculo grueso, cuya semilla es comestible",
			"Kiwi":"Fruto de este arbusto, comestible, de forma ovalada, piel delgada y vellosa, de color verde pardusco y pulpa jugosa, de color verde brillante y con diminutas semillas dispuestas en torno a un corazón blanco",
			"Melocoton":"Fruto del melocotonero, comestible, de forma esférica, piel amarillenta y aterciopelada, pulpa dulce y jugosa y hueso duro",
			"Manzana":"Fruto del manzano, comestible, de forma redondeada y algo hundida por los extremos, piel fina, de color verde, amarillo o rojo, carne blanca y jugosa, de sabor dulce o ácido, y semillas en forma de pepitas encerradas en una cápsula de cinco divisiones",
			"Guayaba":"Fruto del guayabo, comestible, de forma ovalada, parecido a una pera, y carne dulce y llena de semillas pequeñas",
			"Fresa":"Planta herbácea de tallos rastreros, hojas dentadas, divididas en tres segmentos, flores blancas o amarillentas y fruto comestible",
			"Pera":"Fruto del peral, comestible, de color verde, amarillo o encarnado, ancho por la parte de abajo y delgado por la de arriba, de piel fina y pulpa blanca, muy jugosa, sabor dulce y, en el centro, unas semillas pequeñas de color negro",
			"Mandarina":"Fruto del mandarino, parecido a la naranja, de forma achatada por la parte superior e inferior, cáscara de color anaranjado brillante, muy fácil de separar, y pulpa muy dulce",
			"Naranja":"Fruto del naranjo, comestible, de forma redonda, cáscara gruesa y rugosa y pulpa dividida en gajos, agridulce y muy jugosa.",
			"Limon":"Fruto del limonero, comestible, de forma ovalada, piel de color amarillo o verde y pulpa dividida en gajos, de sabor ácido y muy aromático",
			"Banana":"Planta tropical de tallo muy alto, sin ramificaciones, hojas dispuestas en forma de espiral que constituyen un haz apical, provistas de pecíolo corto y grandes láminas oblongas, con fuerte nerviación central, flores amarillas y fruto (banana o banano) comestible y sin semilla",
			"Aguacate":"Árbol tropical de tronco erecto, copa dilatada y globosa, hojas perennes y grandes, en forma elíptica o de lanza, flores verdosas en espiga y fruto comestible, en forma de drupa carnosa",
			"Uva":"Fruto de la vid, comestible, pequeño y de forma redonda u ovalada, piel muy fina y carne muy jugosa; nace junto a otros formando racimos",
			"Papaya":"Fruto del papayo, comestible, de forma alargada, pulpa semejante a la del melón, de color naranja y con muchas semillas en su interior",
			"Mango":" es una fruta pulposa y jugosa que es muy rica en magnesio y en provitaminas A y C. Asimismo, cuenta con altas concentraciones de hidratos de carbono lo que hace que tenga un valor calórico elevado",
			"Sandia":"Planta herbácea de tallo tendido, hojas de color verde oscuro, flores amarillas y fruto esférico, de pulpa roja",
			"Piña":"Fruto del pino y otros árboles, de forma ovalada o cónica, terminado en punta, y formado por muchas piezas duras y leñosas, colocadas en forma de escamas, debajo de las cuales están los piñones, en las variedades que los tienen",
			"Cereza":"Fruto del cerezo, pequeño y redondeado, de color rojo oscuro, pulpa dulce y jugosa y un hueso en su interior",
			"Guanabana":"Fruto del guanábano, de forma acorazonada, corteza verdosa, pulpa blanca y sabor dulce y refrescante",
			
			"hola":"Hola que tal", "como te llamas":"Debian", "Cuantos años tienes":"22", "Como estas":"Bien, gracias",
			"estado civil":"Compilado", "Tienes hijos": "si", "Como se llaman":"linuxmint, ubuntu, trisquel",
			"quien fue tu creador": "Linus Torvald", "A quien odias":"A Windows", "que te ha hecho":"Es una burla para los sistemas operativos" 
			}

funciones = {
			"ram":Popen(['free', '-m'], stdout=PIPE),
			"cpu":Popen(['lscpu'], stdout=PIPE),
			"sistema":Popen(['uname',"-a"], stdout=PIPE),
			"listar":Popen(["ls","-l"], stdout=PIPE),
			"descargas":Popen(["du","-h"], stdout=PIPE),
			"usuario":Popen(["whoami"], stdout=PIPE),
			"hora":Popen(["date"], stdout=PIPE),
			"host":Popen(["hostname"], stdout=PIPE),
			"terminal":Popen(["stty"], stdout=PIPE),
			"kernel":Popen(["uname","-v"], stdout=PIPE)
			}

HOST = "" #Escuchara por todas las interfaces
PORT = 8895

s = socket.socket(
		socket.AF_INET, socket.SOCK_STREAM)
print "Socket Creado"

n = 10
try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print "Error al crear Socket. Error code: " + str(msg[0]) + ",Mensaje de Error; " + msg[1]
	sys.exit()

print "Enlace Via Socket Activo"

s.listen(n) #Encolara un maximo de 10 conexiones
print "Socket escuchando en puerto " +str(PORT)
 
def hilo_cliente(conn):
	#Enviar un mensaje al cliente cuando se conecte
	conn.send("Bienvenido al server. Escriba algo y presione INTRO")
	#Ciclo infinito de es
	while True:
		claves = []
		for d in diction.iterkeys():
			claves.append(d.upper())
		data = conn.recv(1024)
		print data
		if not data:
			break
		elif data == "q":
			opcion = "Que informacion desea"
			conn.send(opcion)
			info = conn.recv(512)	
			lista_funciones = []
			for sd in funciones.iterkeys():
				lista_funciones.append(sd.upper())
			if info.upper() in	lista_funciones:	
				for l,m in funciones.iteritems():
					if l.upper() == info.upper():
						proceso = m
						listado = proceso.stdout.read()
						proceso.stdout.close()
						#for i in listado:
						respuesta = listado
			else:
				respuesta = "No esta esa funcion"

		elif data.upper() in claves:
			for k, v in diction.iteritems():
				if k.upper() == data.upper():
					respuesta = v
					
		else:
			respuesta = "NO ENCONTRADO"
		conn.sendall(respuesta)

	conn.close()

#Comunicandose con el cliente
while 1:
	#Espera para aCEPTAR CONEXIONES
	conn, addr = s.accept()
	print "Conectado con " + addr[0] + ":" + str(addr[1])
	
	#Inicia un nuevo hilo el cual recibe 2 parametros: el hilo y la conexion
	start_new_thread(hilo_cliente,(conn,))
s.close()
