# -*- coding: utf-8 -*-
import csv
import sys
from time import time
#import matplotlib.pyplot as plt
#import numpy as np
sys.setrecursionlimit(20000)
f = open("borrowers_test.csv")
lns = csv.reader(f,delimiter = ",")
diction = {}
n = 0
nombres_completos = []
lista_nombres = []
lista_apellidos = []
apellidos_completos = []
codigos_categoria = []
fechas_registro = []
codigo_carrera = []
nombres_carreras = []

for line in lns:
    apellido = line[0]
    apellidos = line[0].split()
    nombre = line[1]
    nombres = line[1].split()
    codigo_categoria = line[2]
    fecha_registro = line[3]
    sexo = line[4]
    cod_carrera = line[5]
    nombre_carrera = line[6]
    listas = [apellido, nombre, codigo_categoria, fecha_registro, sexo, cod_carrera, nombre_carrera]
    diction.setdefault(n,listas)
    n += 1
    codigos_categoria.append(codigo_categoria)
    fechas_registro.append(fecha_registro)
    codigo_carrera.append(cod_carrera)
    nombres_carreras.append(nombres_carreras)
    if len(nombres) == 2:
        lista_nombres.append(nombres[0].upper())
        lista_nombres.append(nombres[1].upper())
        
    elif len(nombres) == 1:
		if nombres[0] != "NULL":
			lista_nombres.append(nombres[0].upper())
        
    elif len(nombres) == 3:
        lista_nombres.append(nombres[0].upper())
        if nombres[1].upper() == "DE" or nombres[1].upper() == "DEL":
            nuevo = nombres[1] +" "+ nombres[2]
            lista_nombres.append(nuevo.upper())
        else:
            lista_nombres.append(nombres[1].upper())
       	    lista_nombres.append(nombres[2].upper())
			
    elif len(nombres) == 4:
        lista_nombres.append(nombres[0].upper())
        if nombres[1].upper() == "DE" and nombres[2].upper() == "LOS" or nombres[2].upper() == "LA":
            nuevo = nombres[1] + " " + nombres[2] + " " + nombres[3]
            lista_nombres.append(nuevo.upper())
    nombres_completos.append(nombre.upper())
            
    if len(apellidos) == 2:
        lista_apellidos.append(apellidos[0].upper())
        lista_apellidos.append(apellidos[1].upper())
             
    elif len(apellidos) ==1:
        lista_apellidos.append(apellidos[0].upper())
        
    elif len(apellidos) == 3:
        if apellidos[0].upper() == "DEL":
            otros = apellidos[0].upper() + " " + apellidos[1].upper()
            lista_apellidos.append(otros)
    apellidos_completos.append(apellido.upper())     
       

def registros_por_sexo():
	global m
	global f
	global o
	global t
	m = 0 #Variable donde se guardaran la cantidad de hombres
	f = 0 #Variable donde se guardaran la cantidad de mujeres
	o = 0 #Variable que guardara inconsistencias
	t = 0
	for k,v in diction.iteritems():
		if v[1] != "NULL":
		  if v[4] == "m" or v[4] == "M":
			m += 1
		  elif v[4] == "f" or v[4] == "F":
			f += 1
		  else:
				o += 1
		else:
			t +=1

registros_por_sexo()

def linearSearch(busqueda,buscar):
	n = 0
	for e in busqueda:
		if e == buscar:
			n += 1
	print "se encontraron" ,n, "coincidencias de: " 
	return buscar
	 
lista = lista_nombres
def busquedaLineal():
	if buscar in lista_nombres:
		print linearSearch(lista_nombres,buscar)
	elif buscar in lista_apellidos:
		print linearSearch(lista_apellidos,buscar)
	else:
		print "No se encontraron coincidencias de:" ,buscar


def lineal(lista):
	opsm = 0
	posicion = 0
	encontrado = False
	posicion_valor_buscar = 0

	for posicion in range(len(lista)):
		if lista[posicion] == buscar.lower() or lista[posicion] == buscar.upper():
			posicion_valor_buscar = posicion
			encontrado = True
		posicion = posicion +1
		if encontrado == True:
			#print "valor " + buscar+ " encontrado en posicion" , posicion_valor_buscar
			opsm += 1
		encontrado = False
	
	print "El numero de coincidencias de: " ,buscar, "es:" ,opsm

carreras = []
for clave, valor in diction.iteritems():
	if valor[6] not in carreras:
		carreras.append(valor[6])
dictions = {}		
def count_carreras(carrier):
	count = 0
	ma = 0
	print carrier.upper()
	for w, q in diction.iteritems():
		if carrier == q[6]:
			count +=1
	print count
	dictions.setdefault(carrier.upper(),count)

mn = {'g': 109, 'PROFESORADO EN BIOLOG\xc3\xadA PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 20, 'LICENCIATURA EN  CONTADUR\xc3\xadA P\xc3\xbaBLICA': 875, 'PROFESORADO EN F\xc3\xadSICA PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 6, 'LICENCIATURA EN MATEM\xc3\xa1TICA': 424, 'PROFESORADO EN QU\xc3\xadMICA PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 5, 'LICENCIATURA EN LETRAS': 185, 'LICENCIATURA EN SOCIOLOG\xc3\xadA': 194, 'LICENCIATURA EN ANESTESIOLOG\xc3\xadA E INHALOTERAPIA': 576, 'NOMBRE_CARRERA': 1, 'ESPECIALIDAD M\xc3\xa9DICA EN GINECOLOG\xc3\xadA Y OBSTETRICIA': 13, 'LICENCIATURA EN FISIOTERAPIA Y TERAPIA OCUPACIONAL': 593, 'ARQUITECTURA': 1034, 'LICENCIATURA EN PSICOLOGIA': 840, 'LICENCIATURA EN ECONOM\xc3\xadA': 29, 'PROFESORADO EN EDUCACI\xc3\xb3N INICIAL Y PARVULARIA': 44, 'LICENCIATURA EN MERCADEO INTERNACIONAL': 570, 'MAESTR\xc3\xadA EN SALUD P\xc3\xbaBLICA': 33, 'PROFESORADO EN CIENCIAS SOCIALES PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 28, 'LICENCIATURA EN CIENCIAS JUR\xc3\xadDICAS': 1317, 'PROFESORADO EN EDUCACI\xc3\xb3N B\xc3\xa1SICA PARA PRIMERO Y SEGUNDO CICLOS': 133, 'LICENCIATURA EN CIENCIAS DE LA EDUCACI\xc3\xb3N EN LA ESPECIALIDAD DE PRIMERO Y SEGUNDO CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA': 767, 'LICENCIATURA EN F\xc3\xadSICA': 65, 'INGENIER\xc3\xadA INDUSTRIAL': 325, 'INGENIER\xc3\xadA EL\xc3\xa9CTRICA': 85, 'LICENCIATURA EN CIENCIAS QU\xc3\xadMICAS': 71, 'LICENCIATURA EN LENGUAS MODERNAS ESPECIALIDAD EN FRANC\xc3\xa9S E INGL\xc3\xa9S': 503, 'D50101': 2, 'LICENCIATURA EN EDUCACI\xc3\xb3N INICIAL Y PARVULARIA': 7, 'INGENIERIA CIVIL': 995, 'ESPECIALIDAD M\xc3\xa9DICA EN MEDICINA PEDI\xc3\xa1TRICA': 7, 'MAESTR\xc3\xadA EN PROFESIONALIZACI\xc3\xb3N DE LA DOCENCIA SUPERIOR': 36, 'LICENCIATURA EN ADMINISTRACION DE EMPRESAS': 1236, 'INGENIER\xc3\xadA MEC\xc3\xa1NICA': 71, 'PROFESORADO EN IDIOMA INGL\xc3\xa9S PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 211, 'DOCTORADO EN MEDICINA': 3249, 'MAESTR\xc3\xadA EN ADMINISTRACI\xc3\xb3N FINANCIERA': 35, 'PROFESORADO EN MATEM\xc3\xa1TICA PARA TERCER CICLO DE EDUCACI\xc3\xb3N B\xc3\xa1SICA Y EDUCACI\xc3\xb3N MEDIA': 247, 'LICENCIATURA EN LABORATORIO CL\xc3\xadNICO': 1025, 'INGENIER\xc3\xadA AGRON\xc3\xb3MICA': 441, 'L50201': 3, 'MAESTR\xc3\xadA EN GESTI\xc3\xb3N AMBIENTAL': 27, 'INGENIER\xc3\xadA DE SISTEMAS INFORM\xc3\xa1TICOS': 623, 'LICENCIATURA EN QU\xc3\xadMICA Y FARMACIA': 203, 'LICENCIATURA EN BIOLOG\xc3\xadA': 169, 'MAESTR\xc3\xadA EN M\xc3\xa9TODOS Y T\xc3\xa9CNICAS DE INVESTIGACI\xc3\xb3N SOCIAL': 9}	        	        
n_lic = 0
n_prof = 0
n_ing = 0
n_maes = 0
n_arq = 0
n_doc = 0
n_esp = 0
otros = 0
for ke, va in mn.iteritems():
    l = ke.split()
    if l[0].upper() == "LICENCIATURA":
        n_lic += va
    elif l[0].upper() == "PROFESORADO":
        n_prof += va
    elif l[0].upper() == "INGENIERIA":
        n_ing += va
    elif l[0].upper() == "INGENIERíA":
        n_ing += va
    elif l[0].upper() == "MAESTRíA":
        n_maes += va
    elif l[0].upper() == "ARQUITECTURA":
        n_arq += va
    elif l[0].upper() == "DOCTORADO":
        n_doc += va
    elif l[0].upper() == "ESPECIALIDAD":
        n_esp += va    
    else:
        otros += va 

        
def vacios_null():	
    null_apellidos = 0
    null_nombres = 0
    null_codcat = 0
    null_fecha = 0
    null_sexo = 0
    null_codcar = 0
    null_nomcar = 0
    vacios_apellidos = 0
    vacios_nombres = 0
    vacios_codcat = 0
    vacios_fecha = 0
    vacios_sexo = 0
    vacios_codcar = 0
    vacios_nomcar = 0
    for k, v in diction.iteritems():
        if v[0] == "NULL":
            null_apellidos += 1
        elif v[1] == "NULL":
            null_nombres += 1
        elif v[2] == "NULL":
            null_codcat += 1
        elif v[3] == "NULL":
            null_fecha += 1
        elif v[4] == "NULL":
            null_sexo += 1
        elif v[5] == "NULL":
            null_codcat += 1
        elif v[6] == "NULL":
            null_nomcar += 1
        elif v[0] == "":
            vacios_apellidos += 1
        elif v[1] == "":
            vacios_nombres += 1
        elif v[2] == "":
            vacios_codcat += 1
        elif v[3] == "":
            vacios_fecha += 1
        elif v[4] == "":
            vacios_sexo += 1
        elif v[5] == "":
            vacios_codcat += 1
        elif v[6] == " ":
            vacios_nomcar += 1
    print "Valores NULL de apellidos: ",null_apellidos
    print "Valores NULL de nombres: ",null_nombres
    print "Valores NULL de Codigo Categoria: ",null_codcat 
    print "Valores NULL de Fecha de Ingreso: ",null_fecha 
    print "Valores NULL de Sexo: ",null_sexo 
    print "Valores NULL de Codigo carrera: ",null_codcar 
    print "Valores NULL de Nombre Carrera: ",null_nomcar 
    print "Valores VACIOS de apellidos: ",vacios_apellidos 
    print "Valores VACIOS de nombres: ",vacios_nombres 
    print "Valores VACIOS de Codigo Categoria: ",vacios_codcat 
    print "Valores VACIOS de Fecha de Ingreso: ",vacios_fecha 
    print "Valores VACIOS de sexo: ",vacios_sexo
    print "Valores VACIOS de Codigo Categoria: ",vacios_codcar 
    print "Valores VACIOS de Nombre Carrera: ",vacios_nomcar 

def agregar_registros():
	sex = ["m", "M", "f", "F"]
	f = open("borrowers_test.csv","a")
	obj = csv.writer(f,delimiter=",")#, quotechar="|", quoting = csv.QUOTE_NONNUMERIC)
	try:
		apellidos = raw_input("Apellidos: ")
		nombres = raw_input("Nombres: ")
		codigo_categoria = raw_input("Codigo: ")
		fecha_registro = raw_input("Fecha de Registro: ")
		while True:
			sexo = raw_input("Sexo: ")
			if sexo not in sex:
				print "Digite M o m para masculino y f o F para femenino"
			else:
				break
		cod_carrera = raw_input("Codigo de Carrera: ")
		nombre_carrera = raw_input("Nombre de Carrera: ")
		obj.writerow([apellidos, nombres, codigo_categoria, fecha_registro, sexo, cod_carrera, nombre_carrera])
		f.close()
	except:
		print "Registro no ingresado"

def quicksort(lista,izquierda,derecha):
    i=izquierda
    j=derecha
    x=lista[(izquierda + derecha)/2]
 
    while( i <= j ):
        while lista[i]<x and j<=derecha:
            i=i+1
        while x<lista[j] and j>izquierda:
            j=j-1
        if i<=j:
            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
            i=i+1;  j=j-1;
        if izquierda < j:
            quicksort( lista, izquierda, j );
    if i < derecha:
        quicksort( lista, i, derecha );
 
def imprimirLista(lista,tam):
    for i in range(0,tam):
        print lista[i]
        
def burbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;
 
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print lista[i]

def merge(left, right):
    result=[]
    
    while(len(left) > 0 and len(right) > 0):
        if (left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    if(len(left) > 0):
        result = result + left
    if(len(right) > 0):
        result = result + right

    return result
    
#array = [9,8,7,6,5,4,3,2,1,2,23,4,6,7,8,5,4]
def sort(arra):
    left=[]
    right=[]
    
    if(len(arra) <= 1):
        return arra
        
    else:
        middle=len(arra)/2
        middle-=1
        
        for x in range(middle+1):
            left.append(arra[x])
            
             
        for x in range(middle+1, len(arra)):
            right.append(arra[x])
            
        left = sort(left)
        right = sort(right)
        result = merge(left, right)
        
        return result

def impriLista(lista,tam):
    for i in range(0,tam):
        print lista[i]
        
nombres_sin_repetir = []
for l in lista_nombres:
	if l not in nombres_sin_repetir:
		nombres_sin_repetir.append(l)

fechas_sin_repetir = []
for l in fechas_registro:
    if l not in fechas_sin_repetir:
        fechas_sin_repetir.append(l)    

anho_2016 = 0
anho_2015 = 0
anho_2014 = 0
anho_2013 = 0   
otros_anhos = 0
for date in fechas_registro:
    datel = date.split("/")
    anho = datel[-1]
    if anho == "2016":
        anho_2016 +=1
    elif anho == "2015":
        anho_2015 +=1
    elif anho == "2014":
        anho_2014 +=1
    elif anho == "2013":
        anho_2013 +=1




while True:
	print "------------------------------MENU-----------------------------------"
	print "1 - Cantidad de Registros de Hombres y Mujeres"
	print "2 - Busqueda por nombres o apellidos"
	print "3 - Cantidad de estudiantes agrupados por carrera"
	print "4 - Cantidad de datos erroneos"
	print "5 - Agregar registros"
	print "6 - Ordenar registros por orden alfabetico"
	print "7 - Ordenar resgistros en orden alfabetico por columna seleccionada"
	print "8 - Graficar"
	print "9 - Salir"
	
	seleccion = int(raw_input("Seleccione opcion: "))
	if seleccion == 1:
		
		print "El total de hombres es: " ,m
		print "El total de mujeres es: " ,f
		print "Campos vacios: " ,o
		print "Personas sin nombre: " ,t
		
	elif seleccion == 2:
		buscar = raw_input("Buscar: ")
		buscar = buscar.upper()
		print "1 - Busqueda Lineal"
		print "2 - Busqueda por Posicion"
		print "3 - Busqueda Binaria" 
		opt = int(raw_input("OP: "))
		if opt == 1:
			tiempo_inicial = time()
			busquedaLineal()
			tiempo = time() - tiempo_inicial
			print "El tiempo de ejecucion fue: " , round(tiempo,4), "segundos"
			
		elif opt == 2:
			tiempo_inicial = time()
			if buscar in lista_nombres:
				lineal(lista_nombres)
			elif buscar in lista_apellidos:
				lineal(lista_apellidos)
			tiempo = time() - tiempo_inicial
			print "El tiempo de ejecucion fue: " , round(tiempo,4), "segundos"
			
		elif opt == 3:
			binarySearch()
		
	elif seleccion == 3:
		nx = 0
		while nx <= (len(carreras)-1):
			carrier = carreras[nx]
			count_carreras(carrier)
			nx +=1
		print n_lic
	elif seleccion == 4:
		vacios_null()                 
		
	elif seleccion == 5:
		agregar_registros()
		
	elif seleccion == 6:
		print "1 - QUICKSORT"
		print "2 - BUBBLE"
		print "3 - MERGE"
		lista = nombres_sin_repetir
		sel = int(raw_input("Opcion :"))
		if sel == 1:
			tiempo_inicial = time()
			quicksort(lista,0,len(lista)-1)
			imprimirLista(lista,len(lista))
			tiempo = time() - tiempo_inicial
			print "El tiempo de ejecucion fue: " , round(tiempo,2), "segundos"
		elif sel == 2:
			tiempo_inicial = time()
			burbuja(lista,len(lista))
			imprimeLista(lista,len(lista))
			tiempo = time() - tiempo_inicial
			print "El tiempo de ejecucion fue: " , round(tiempo,2), "segundos"
		elif sel == 3:
		    tiempo_inicial = time()
		    print sort(lista)
		    impriLista(lista,len(lista))
		    tiempo = time() - tiempo_inicial
		    print "El tiempo de ejecucion fue: " , round(tiempo,2), "segundos"
		  			
	elif seleccion == 7:
		print "1- Apellidos"
		print "2 - Nombres"
		print "3 - Codigo Categoria"
		print "4 - Fecha Ingreso"
		print "5 - Codigo Carrera"
		print "6 - Nombre Carrera"
		option = int(raw_input("Seleccione columna a ordenar:"))
		if option == 1:
			apellidos_sin_repetir = []
			for l in lista_apellidos:
				if l not in apellidos_sin_repetir:
					apellidos_sin_repetir.append(l)
			lista = apellidos_sin_repetir
						
		elif option == 2:
			lista = nombres_sin_repetir
			
		elif option == 3:
			codcat_sin_repetir = []
			for l in codigos_categoria:
				if l not in codcat_sin_repetir:
					codcat_sin_repetir.append(l)
			lista = codcat_sin_repetir
			
		elif option == 4:
			lista = fechas_sin_repetir
			
		elif option == 5:
			codcar_sin_repetir = []
			for l in codigo_carrera:
				if l not in codcar_sin_repetir:
					codcar_sin_repetir.append(l)
			lista = codcar_sin_repetir
			
		elif option == 6:
			lista = carreras
		quicksort(lista,0,len(lista)-1)
		imprimirLista(lista,len(lista))
		
	elif seleccion == 8:
	    print "1 - Hombres y mujeres"
	    print "2 - Inscritos por año"
	    print "3 - Alumnos por area"
	    
	    fp = int(raw_input("Seleccione: "))
	    if fp == 1:
   	        labels = 'Hombres', 'Mujeres'
                sizes = [m,f]
                colors = ['blue', 'red']
                explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
                plt.title('Cantidad de hombres y mujeres')
                plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.show()
                
            elif fp == 2:
                
              labels = '2016', '2015','2014', '2013'
              sizes = [anho_2016, anho_2015,anho_2014,anho_2013]
              colors = ['blue', 'red', "green", "orange"]
              explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
              plt.pie(sizes, explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90)
              plt.axis('equal')
              plt.show()  
              
            elif fp == 3:
                N = 7
                diction2 = {"Licenciatura":n_lic ,"Profesorado": n_prof , "Ingenieria":n_ing ,"Maestria": n_maes , "Arquitectura": n_arq , "Doctorado": n_doc, "Especialidad": n_esp}
                menMeans = diction2.values()
                menStd =  (7)
                ind = np.arange(N)  
                width = 0.35       
                fig, ax = plt.subplots()
                rects1 = ax.bar(ind, menMeans, width, color='b', yerr=menStd)
                ax.set_ylabel('Resultados')
                ax.set_title('Numero de Estudiantes por Area')
                ax.set_xticks(ind + width)
                ax.set_xticklabels(diction2.keys())
                def autolabel(rects):
                            
                   	for rect in rects:
                  		height = rect.get_height()
                                ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                                            '%d' % int(height),
                                            ha='center', va='bottom')
                                    
                                    
                        autolabel(rects1)
                        plt.show()
                plt.show()
              
        elif seleccion == 9:
            break
              
