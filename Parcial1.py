productos = {
0: {"Dulces": [0.05, "bolsa",30]},
1: {"Pan": [0.15, "unidad",50]},
2: {"Leche": [2.50, "galon",10]},
3: {"Queso": [3.0, "libra",10]},
4: {"Frijol": [0.78, "libra",100]},
5: {"Arroz": [0.40, "libra",100]},
6: {"Cereal": [3.40, "caja",100]},
7: {"Jabon": [0.80, "unidad",30]},
8: {"Embutidos": [1.20, "libra",55]},
9: {"Leche": [2.40, "galon",55]},
10: {"Pan": [0.10, "unidad",50]},
11: {"Cafe": [1.5, "libra",100]},
12: {"Arroz": [1.00, "libra",100]},
13: {"Frijol": [0.80, "libra",50]},
}

lista_productos = []
producto_precio_existencia = {}
def actualizar():
    for k1 in productos.keys(): 
        for k, v in productos[k1].iteritems():          
            if k not in lista_productos:
                lista_productos.append(k)    
            else:
                producto_precio_existencia[k] = (v[0],v[2]) #Paso valores v[0] y v[1] a la clave k
                del productos[k1] #Borramos el diccionario k1. 
            
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():              
            for c, e in producto_precio_existencia.iteritems():
                if c == k: #Comparamos si la clave de producto_precio_existencia es igual a la clave de productos[k1]
                    v[0] = e[0] #Al valor precio de productos[k1] se le asigna el valor de precio de producto_precio_existencia 
                    v[2] += e[1]#Al valor existencia se le suma la existencia de producto_precio_existencia
    
actualizar()    

                
def modificar():
    try:
        pro = str(raw_input("Producto a modificar "))
    except:
        print "Debe digitar texto"
        
    try:
        for k1 in productos.keys():
            for k, v in productos[k1].iteritems():
                
                if k == pro:
                    print "\nQue desea modificar"
                    print "1 - Precio"
                    print "2 - Existencia"
                    print "3 - Salir"
                    x = int(raw_input("Seleccione opcion "))
                    if x == 1:
                        print "\nPrecio anterior:" ,v[0]
                        nuevo_precio = float(raw_input("Nuevo precio: "))
                        v[0] = nuevo_precio
                        print "Precio: " ,v[0]
                        
                    elif x == 2:
                        print "\nExistencia anterior:" ,v[2]
                        nueva_existencia = int(raw_input("Cuanto desea agregar:" ))
                        v[2] += nueva_existencia
                        print v[2] 
                    elif x == 3:
                        break
                    else:
                        print "\nOpcion incorrecta"
    except:
        print "Debe digitar numeros"
        
#lista_productos = []
dicp = {}                   
def vender():
    total1 = 0
    print "-------------------------------------PRODUCTOS-------------------------------------------------"
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            print "|" ,k,  "Precio:" ,v[0],  "Existencia: " ,v[2],
            #if k not in lista_productos:
                #lista_productos.append(k)
    while True: 
        try: 
            opcion = int(raw_input("Vender producto: 1 | Terminar venta: 2 | Pagar: 3 | Salir: 4 "))
            if opcion == 1: 
                try:
                    vender_producto = str(raw_input("Producto a vender: "))
                except:
                    print "Debe digitar texto"
                if vender_producto in lista_productos:
                    cantidad_venta = int(raw_input("Cantidad de producto a vender: "))
                    for k1 in productos.keys():
                        for k, v in productos[k1].iteritems():
                            if k == vender_producto:
                                if v[2] >= cantidad_venta:
                                    dicp[k] = (v[0],cantidad_venta)#nuevo diccionario donde pongo de clave el producto a vender y de elementos el precio y la cantidad de productos
                                    v[2] -= cantidad_venta
                                    print "Existencia restante: " ,v[2]
                                
                        
                                else:
                                    print "Solamente hay" ,v[2], "en existencia"
                else:
                    print "Producto no disponible"
                            
            elif opcion == 2:
                print "Cantidad -- Producto -------------Precio Unitario----Total"
                for m,c in dicp.iteritems():#Itero sobre el diccionario dicp que contiene los productos a vender
                    total = c[0] * c[1]   
                    total1 += total    
                    print "---",c[1], "______" ,m, "------------------",c[0], "---------",total                                             
                                    
            elif opcion == 3:
                print "EL TOTAL A PAGAR ES:" ,total1
    
            elif opcion == 4:
                break         
        except:
   
            print "Debe digitar numeros"                                                    

def mostrar_producto():
    print "-----------------------------------------------------------------------------------"
    print "PRODUCTO -------------------PRECIO----------EXISTENCIA-----------------PRESENTACION"
    print "------------------------------------------------------------------------------------"
    for k1 in productos.keys():
        for k ,v in productos[k1].iteritems():
            print "\n" ,k, "------------------",v[0],"---------------",v[2],"---------------------",v[1]
            
                
while True:
    #actualizar()
    print "SISTEMA DE INVENTARIO"
    print "------OPCIONES-------"
    print "1 - Registrar Producto"
    print "2 - Modificar Producto"
    print "3 - Vender Producto"
    print "4 - Mostrar Productos"
    print "5 - Salir"
    
    seleccion = int(raw_input("Seleccione una opcion: "))
    try:
        if seleccion == 1:
            print "\nOPCION NO DISPONIBLE\n"            
    
        elif seleccion == 2:
            modificar()
            
        elif seleccion == 3:
            vender()            
            
        elif seleccion == 4:
            mostrar_producto()
            
        elif seleccion == 5:
            break
            
        else:
            "\nOpcion no valida\n"
    except:
        print "Debe digitar numeros"