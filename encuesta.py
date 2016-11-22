# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
diction = {} #Diccionario donde guardare como clave el vegetal y valor el numero de votos

#FUNCION PARA CONTAR LOS VOTOS DE CADA VEGETAL
def count_votes(vegetal):
	print ("numero de votos para "+vegetal+ "...")
	global count
	count = 0
	for line in open('encuesta_espanol.txt'):
		line = line.strip()
		nombre, voto = line.split(" - ")
		#vegetal = vegetal.strip()
		if voto == vegetal:
			count = count + 1
	return count
m = 0
p = 0
while True:
    print "-----MENU-------"
    print "1 - Ver votos de todas las verduras"
    print "2 - Ver usuarios que votaron mas de una vez"
    print "3 - El ganador es: "
    print "4 - Graficar"
    print "5 - Salir"
    try:
        alternativa = int(raw_input("Seleccione alternativa: "))
        
        if alternativa == 1:
            lista = []
            nombres = [] #Lista donde guardo los nombres sin repetir
            nombres_deobles = [] #Lista donde guardo los nombres repetidos
            for line in open('encuesta_espanol.txt'):
                line = line.strip()
                nombre, vegetal = line.split(" - ")
                vegetal = vegetal.strip()
                if vegetal not in lista :
                   	lista.append(vegetal)
                elif nombre not in nombres:
                    nombres.append(nombre)
                elif nombre in nombres:
                    nombres_deobles.append(nombre)		
    
            n = 0
            #CREO UN CICLO PARA QUE SE EJECUTE LA FUNCION count_votes() PARA CADA VEGETAL
            while n <= (len(lista)-1):
                print (count_votes(lista[n]))
                diction.setdefault(lista[n],count)
                n += 1
            m = 1    
        elif alternativa == 2:
            if m == 1:
                print nombres_deobles    
            else:
                print "Seleccione la Opción 1 antes"
                
        elif alternativa == 3:
            if m == 1:
                votos = []
                votototal = 0
                #OTRO CICLO PARA GUARDAR LA CANTIDAD DE VOTOS POR VEGETAL, Y LUEGO SACAR EL MAXIMO DE ELLOS
                for k, v in diction.iteritems():
               	    votos.append(v)
               	    votototal += v
                maximo = max(votos)
                
                for k,v in diction.iteritems():
                    if maximo == v:
                        print "El ganador es" ,k,"por haber obtenido",maximo,"votos"
            else:
                print "Seleccione la opción 1 antes"
            p = 1
                    
        elif alternativa == 4:
            if m == 1 and p ==1:
                #Para sacar los porcentajes de cada vegetal
                porcentajes = []
                for x, y in diction.iteritems():
                    por = (float(y) / float(votototal)) * 100
                    redondeo = round(por,2)
                    diction[x] = redondeo
                for u, w in diction.iteritems():
                    print u,w,"%"
                plt.ion()  # Ponemos el modo interactivo
                votos_verduras = [diction["Kiwi"], diction["Brocoli"], diction["Sandia"], diction["Lechuga"], diction["Fresas"], diction["Papas"], diction["Pepinos"], diction["Tomates"], diction["Aguacate"], diction["Frijoles"]] 
                votos_verduras = np.append(votos_verduras, 100. - np.sum(votos_verduras))
                verduras = [u'Kiwi', u'Brocoli', 'Sandia', 'Lechuga', 'Fresas', 'Papas', u'Pepinos', 'Tomates', 'Aguacate', 'Frijoles', 'Rabano']  # Etiquetas para las porciones
                explode = [0, 0, 0, 0, 0, 0, 0.1, 0.0, 0, 0, 0]  # Division entre porciones
                plt.pie(votos_verduras, labels = verduras,autopct="%1.1f%%", explode = explode)  # Dibuja un gráfico de pastel
                plt.axis("equal")
                plt.title(u'Porcentaje de votos por verdura')
                plt.show()
                               
            else:
                print "Debe seleccionar las opciones 1 y 3 antes"
            
        elif alternativa == 5:
            break
    except:
        print "Seleccione una opcion valida"
       
