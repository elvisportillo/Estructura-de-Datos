# -*- coding: utf-8 -*-
import random
Datos_usuario = {
0:[" ", " ", " ", " ", " ", 0]}

preguntas = ("1.CUALES DE LOS SIGUIENTES SON PROTOCOLOS DE ENRUTAMIENTO","2.CUALES DE LOS SIGUIENTES CAPAS DEL MODELO OSI CORRESPONDEN A LA CAPA DE APLICACION DEL MODELO TCP/IP","3.ENTRE LAS UNIDADES DE PROTOCOLO DE DATOS (PDU POR SUS SIGLAS EN INGLES) SE ENCUENTRAN DATOS; A QUE CAPAS DEL MODELO OSI CORRESPONDEN","4.LA CAPA DE TRANSPORTE DEL MODELO OSI TIENE DOS CLASES DE PDU, CUALES SON","5.CUALES SON LOS DOS ESTANDARES PARA LA CREACION DE CABLES DE RED","6.CUALES DE LOS SIGUIENTES SON MEDIOS DE TRANSMISION GUIADOS","7.CUALES DE LOS SIGUIENTES SON TOPOLOGIAS DE RED","8.CUALES DE LAS SIGUIENTES ESTAN DENTRO DE LA CLASIFICACION DE REDES SEGUN SU TAMAÑO","9.UNA BUENA ARQUITECTURA DE RED DEBE CUMPLIR 4 CARACTERISTICAS BASICAS, DOS DE LAS CUALES SON:","10.CUALES SON LOS PROTOCOLOS QUE HACEN FUNCIONAR EL CORREO ELECTRONICO","11.CUALES DE LOS SIGUIENTES COMANDOS SE UTILIZAN PARA RUTAS EN CMD","12.PROTOCOLOS DE ACCESO REMOTO","13.PROTOCOLOS DE ASIGNACION DE IP","14.PROTOCOLOS DE LA CAPA DE ENLACE","15.MODOS DE CONFIGURACION EN UN ROUTER POR MEDIO DE CISCO IOS CLI","16.CON QUE NOMBRES SE LE CONOCE A LA DIRECCION IP 127.0.0.1","17.IP INICIAL E IP FINAL DE UNA RED CLASE A","18.CON QUE NOMBRES SE LE CONOCE AL DISPOSITIVO QUE ACTUA COMO INTERFAZ DE CONEXION ENTRE DOS O MAS DISPOSITIVOS PARA COMPARTIR RECURSOS","19.QUE COMANDOS SE PUEDEN UTILIZAR EN EL MODO PRIVILEGIADO","20.QUE COMANDOS SE PUEDEN UTILIZAR EN EL MODO DE CONFIGURACION GLOBAL","21.CUALES DE LOS SIGUIENTES SON DISPOSITIVOS FINALES EN UNA RED INFORMATICA","22.CUALES DE LOS SIGUIENTES SON DISPOSITIVOS INTERMEDIOS EN UNA RED INFORMATICA","23.CUALES DE LAS SIGUIENTES SON FUNCIONES DE UN ROUTER","24.EN CUALES DE LOS NIVELES DEL MODELO OSI PUEDEN FUNCIONAR LOS FIREWALLS","25.QUE DISPOSITIVOS SE NECESITAN PARA INTERCONECTAR DOS REDES LAN","26.CUALES DE LAS SIGUIENTES ESTAN DENTRO DE LA CLASIFICACION DE REDES SEGUN SU TECNOLOGIA DE TRANSMISION","27.PROTOCOLOS QUE FUNCIONAN BAJO EL NIVEL DE TRANSPORTE DEL MODELO TCP/IP","28.SISTEMAS Y/O PROGRAMAS PARA COMPARTIR ARCHIVOS DE RED","29.PROGRAMAS PARA ANALISIS DE RED","30.DOS DE LAS CLASES DE REDES SON:")

Respuestas1 = ["OSPF","EIGRP","GRP","GSM","NFS"]
Respuestas2 = ["PRESENTACION","TRANSPORTE","SESION","RED","ENLACE DE DATOS"]
Respuestas3 = ["PRESENTACION","TRANSPORTE","RED","FISICA","APLICACION"]
Respuestas4 = ["TRAMAS","SEGMENTOS","BITS","DATAGRAMAS","PAQUETES"]
Respuestas5 = ["508-A","568-B","568-A","508-B", "508-C"]
Respuestas6 = ["CABLE UTP","BLUETOOTH","AIRE","FIBRA OPTICA","INFRARROJO"]
Respuestas7 = ["ESTRELLA","ANILLO","CENTELLA","CIRCULO","TRAMA"]
Respuestas8 = ["DAN","TAN","LAN","WAN","FAN"]
Respuestas9 = ["SOPORTE TECNICO","TOLERANCIA A FALLOS","CALIDAD DE SERVICIO","TRANSMISION IMPLECABLE","FACIL CONFIGURACION"]
Respuestas10 = ["NMTP","SMTP","POP/POP3","NFS","HTTP"]
Respuestas11 = ["TRACERT","PING","IPCONFIG","NETSTAT","ROUTE"]
Respuestas12 = ["SSH","SMTP","TELNET","DNS","DHCP"]
Respuestas13 = ["HTTP","FTP","DHCP","BOOTP","IMAP"]
Respuestas14 = ["OSPF","ETHERNET","IP","PPP","UDP"]
Respuestas15 = ["PRIVILEGIADO","ROOT","CONFIGURACION GLOBAL","STANDARD","MONITOR"]
Respuestas16 = ["OWN","LOCALHOST","LOOPBACK","CLASS","GUEST"]
Respuestas17 = ["1.0.0.1","127.255.255.254","128.0.0.1","223.255.255.254","192.0.0.1"]
Respuestas18 = ["GATEWAY","RACK","PUERTA DE ENLACE","ACCESS POINT","PC"]
Respuestas19 = ["SHOW","HOSTNAME","WRITE","BANNER","END"]
Respuestas20 = ["SETUP","TERMINAL","LOGIN","INTERFACE","SHOW"]
Respuestas21 = ["PC","SWITCH","ROUTER","FIREWALL","IMPRESOR"]
Respuestas22 = ["TELEFONO","ESCANER","SWITCH","ROUTER","CABLES"]
Respuestas23 = ["ENCENDER UN EQUIPO","REGENERAR SEÑALES","ENVIAR CORREOS","PERMITIR O DENEGAR FLUJO DE DATOS","APAGAR UN DISPOSITIVO"]
Respuestas24 = ["RED","FISICO","ENLACE","PRESENTACION","APLICACION"]   
Respuestas25 = ["ROUTER","REPETIDOR","PC","IMPRESORA","ACCESS POINT"]
Respuestas26 = ["BROADCAST","PEER TO PEER","POINT TO POINT","UNICAST","MULTICAST"]
Respuestas27 = ["UDP","HTTP","TCP","IP","ETHERNET"]
Respuestas28 = ["SAMBA","CUMBIA","GTA","NFS","SHARED"]
Respuestas29 = ["HYDRA","WIRESHARK","ETTHERCAP","JACK THE RIPPER","BRUTUS"]
Respuestas30 = ["A","H","J","C","P"]

oportunidad = 0
def mostrar_resultados():
    
    try:
        contador = 0
    
        if respuesta1_1 == Respuestas1.index("OSPF") and respuesta1_2 == Respuestas1.index("EIGRP") or respuesta1_1 == Respuestas1.index("EIGRP") and respuesta1_2 == Respuestas1.index("OSPF"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[0], "las respuestas correctas son OSPF Y EIGRP \n" 
    
        if respuesta2_1 == Respuestas2.index("SESION") and respuesta2_2 == Respuestas2.index("PRESENTACION") or respuesta2_1 == Respuestas2.index("PRESENTACION") and respuesta2_2 == Respuestas2.index("SESION"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[1], "las respuestas correctas son PRESENTACION Y SESION \n" 
        
        if respuesta3_1 == Respuestas3.index("PRESENTACION") and respuesta3_2 == Respuestas3.index("APLICACION") or respuesta3_1 == Respuestas3.index("APLICACION") and respuesta3_2 == Respuestas3.index("PRESENTACION"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[2], "las respuestas correctas son APLICACION Y PRESENTACION \n" 
            
        if respuesta4_1 == Respuestas4.index("SEGMENTOS") and respuesta4_2 == Respuestas4.index("DATAGRAMAS") or respuesta4_1 == Respuestas4.index("DATAGRAMAS") and respuesta4_2 == Respuestas4.index("SEGMENTOS"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[3], "las respuestas correctas son DATAGRAMAS Y SEGMENTOS \n" 
        
        if respuesta5_1 == Respuestas5.index("568-B") and respuesta5_2 == Respuestas5.index("568-A") or respuesta5_1 == Respuestas5.index("568-A") and respuesta5_2 == Respuestas5.index("568-B"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[4], "las respuestas correctas son 568 - A y 568 - B \n" 
            
        if respuesta6_1 == Respuestas6.index("CABLE UTP") and respuesta6_2 == Respuestas6.index("FIBRA OPTICA") or respuesta6_1 == Respuestas6.index("FIBRA OPTICA") and respuesta6_2 == Respuestas6.index("CABLE UTP"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[5], "las respuestas correctas son CABLE UTP y FIBRA OPTICA \n" 
        
        if respuesta7_1 == Respuestas7.index("ESTRELLA") and respuesta7_2 == Respuestas7.index("ANILLO") or respuesta7_1 == Respuestas7.index("ANILLO") and respuesta7_2 == Respuestas7.index("ESTRELLA"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[6], "las respuestas correctas son ESTRELLA y ANILLO \n" 
        
        if respuesta8_1 == Respuestas8.index("LAN") and respuesta8_2 == Respuestas8.index("WAN") or respuesta8_1 == Respuestas8.index("WAN") and respuesta8_2 == Respuestas8.index("LAN"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[7], "las respuestas correctas son LAN y WAN \n" 
        
        if respuesta9_1 == Respuestas9.index("TOLERANCIA A FALLOS") and respuesta9_2 == Respuestas9.index("CALIDAD DE SERVICIO") or respuesta9_1 == Respuestas9.index("CALIDAD DE SERVICIO") and respuesta9_2 == Respuestas9.index("TOLERANCIA A FALLOS"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[8], "las respuestas correctas son TOLERANCIA A FALLOS y CALIDAD DE SERVICIO \n" 
        
        if respuesta10_1 == Respuestas10.index("SMTP") and respuesta10_2 == Respuestas10.index("POP/POP3") or respuesta10_1 == Respuestas10.index("POP/POP3") and respuesta10_2 == Respuestas10.index("SMTP"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[9], "las respuestas correctas son SMTP y POP/POP3 \n" 
    
        if respuesta11_1 == Respuestas11.index("TRACERT") and respuesta11_2 == Respuestas11.index("ROUTE") or respuesta11_1 == Respuestas11.index("ROUTE") and respuesta11_2 == Respuestas11.index("TRACERT"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[10], "las respuestas correctas son TRACERT y ROUTE \n" 
        
        if respuesta12_1 == Respuestas12.index("SSH") and respuesta12_2 == Respuestas12.index("TELNET") or respuesta12_1 == Respuestas12.index("TELNET") and respuesta12_2 == Respuestas12.index("SSH"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[11], "las respuestas correctas son TRACERT y ROUTE \n"    
    
        if respuesta13_1 == Respuestas13.index("DHCP") and respuesta13_2 == Respuestas13.index("BOOTP") or respuesta13_1 == Respuestas13.index("BOOTP") and respuesta13_2 == Respuestas13.index("DHCP"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[12], "las respuestas correctas son TRACERT y ROUTE \n"         
        
        if respuesta14_1 == Respuestas14.index("ETHERNET") and respuesta14_2 == Respuestas14.index("PPP") or respuesta14_1 == Respuestas14.index("PPP") and respuesta14_2 == Respuestas14.index("ETHERNET"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[13], "las respuestas correctas son ETHERNET y PPP \n"
            
        if respuesta15_1 == Respuestas15.index("PRIVILEGIADO") and respuesta15_2 == Respuestas15.index("CONFIGURACION GLOBAL") or respuesta15_1 == Respuestas15.index("CONFIGURACION GLOBAL") and respuesta15_2 == Respuestas15.index("PRIVILEGIADO"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[14], "las respuestas correctas son CONFIGURACION GLOBAL y PRIVILEGIADO \n"        
    
        if respuesta16_1 == Respuestas16.index("LOCALHOST") and respuesta16_2 == Respuestas16.index("LOOPBACK") or respuesta16_1 == Respuestas16.index("LOOPBACK") and respuesta16_2 == Respuestas16.index("LOCALHOST"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[15], "las respuestas correctas son LOCALHOST y LOOPBACK \n"        
        
        if respuesta17_1 == Respuestas17.index("1.0.0.1") and respuesta17_2 == Respuestas17.index("127.255.255.254") or respuesta17_1 == Respuestas17.index("127.255.255.254") and respuesta17_2 == Respuestas17.index("1.0.0.1"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[16], "las respuestas correctas son 1.0.0.1 y 127.255.255.254 \n"        
    
        if respuesta18_1 == Respuestas18.index("GATEWAY") and respuesta18_2 == Respuestas18.index("PUERTA DE ENLACE") or respuesta18_1 == Respuestas18.index("PUERTA DE ENLACE") and respuesta18_2 == Respuestas18.index("GATEWAY"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[17], "las respuestas correctas son GATEWAY y PUERTA DE ENLACE \n" 
            
        if respuesta19_1 == Respuestas19.index("SHOW") and respuesta19_2 == Respuestas19.index("WRITE") or respuesta19_1 == Respuestas19.index("WRITE") and respuesta19_2 == Respuestas19.index("SHOW"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[18], "las respuestas correctas son SHOW y WRITE \n" 
            
        if respuesta20_1 == Respuestas20.index("INTERFACE") and respuesta20_2 == Respuestas20.index("LOGIN") or respuesta20_1 == Respuestas20.index("LOGIN") and respuesta20_2 == Respuestas20.index("INTERFACE"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[19], "las respuestas correctas son SHOW y INTERFACE \n"         
        
        if respuesta21_1 == Respuestas21.index("PC") and respuesta21_2 == Respuestas21.index("IMPRESOR") or respuesta21_1 == Respuestas21.index("IMPRESOR") and respuesta21_2 == Respuestas21.index("PC"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[20], "las respuestas correctas son IMPRESOR y PC \n"      
    
        if respuesta22_1 == Respuestas22.index("SWITCH") and respuesta22_2 == Respuestas22.index("ROUTER") or respuesta22_1 == Respuestas22.index("ROUTER") and respuesta22_2 == Respuestas22.index("SWITCH"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[21], "las respuestas correctas son SWITCH y ROUTER \n"     
        
        if respuesta23_1 == Respuestas23.index("REGENERAR SEÑALES") and respuesta23_2 == Respuestas23.index("PERMITIR O DENEGAR FLUJO DE DATOS") or respuesta23_1 == Respuestas23.index("PERMITIR O DENEGAR FLUJO DE DATOS") and respuesta23_2 == Respuestas23.index("REGENERAR SEÑALES"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[22], "las respuestas correctas son REGENERAR SEÑALES y PERMITIR O DENEGAR FLUJO DE DATOS \n"     
    
        if respuesta24_1 == Respuestas24.index("RED") and respuesta24_2 == Respuestas24.index("APLICACION") or respuesta24_1 == Respuestas24.index("APLICACION") and respuesta24_2 == Respuestas24.index("RED"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[23], "las respuestas correctas son RED y APLICACION \n"  
        
        if respuesta25_1 == Respuestas25.index("ROUTER") and respuesta25_2 == Respuestas25.index("REPETIDOR") or respuesta25_1 == Respuestas25.index("REPETIDOR") and respuesta25_2 == Respuestas25.index("ROUTER"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[24], "las respuestas correctas son ROUTER y REPETIDOR \n"   
    
        if respuesta26_1 == Respuestas26.index("BROADCAST") and respuesta26_2 == Respuestas26.index("POINT TO POINT") or respuesta26_1 == Respuestas26.index("POINT TO POINT") and respuesta26_2 == Respuestas26.index("BROADCAST"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[25], "las respuestas correctas son BROADCAST y POINT TO POINT \n"          
                
        if respuesta27_1 == Respuestas27.index("UDP") and respuesta27_2 == Respuestas27.index("TCP") or respuesta27_1 == Respuestas27.index("TCP") and respuesta27_2 == Respuestas27.index("UDP"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[26], "las respuestas correctas son UDP y TCP \n"  
    
        if respuesta28_1 == Respuestas28.index("SAMBA") and respuesta28_2 == Respuestas28.index("NFS") or respuesta28_1 == Respuestas28.index("NFS") and respuesta28_2 == Respuestas28.index("SAMBA"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[27], "las respuestas correctas son SAMBA y NFS \n"      
    
        if respuesta29_1 == Respuestas29.index("WIRESHARK") and respuesta29_2 == Respuestas29.index("ETTHERCAP") or respuesta29_1 == Respuestas29.index("ETTHERCAP") and respuesta29_2 == Respuestas29.index("WIRESHARK"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[28], "las respuestas correctas son WIRESHARK y ETTHERCAP \n"        
        
        if respuesta30_1 == Respuestas30.index("A") and respuesta30_2 == Respuestas30.index("C") or respuesta30_1 == Respuestas30.index("C") and respuesta30_2 == Respuestas30.index("A"):
            contador += 1
        else:
            print "Para la pregunta" ,preguntas[29], "las respuestas correctas son A y C \n" 
        
        calificacion = (contador * 100) / 30    
        if oportunidad == 1:
            if calificacion >= 60 and calificacion <= 70:
                print "Aprobo por obtener:" ,calificacion, "% de respuestas correctas \n"
            elif calificacion >= 70 and calificacion <= 80:
                print "Acreedor de un certificado como Experto en Informatica por obtener:" ,calificacion, "% de respuestas correctas \n"
            elif calificacion >= 80 and calificacion <= 100:
                print "Acreedor de un certificado como Experto en Informatica con HONORES por obtener:" ,calificacion, "% de respuestas correctas \n"
            else:
                print "Obtuvo menos del 60% de respuestas correctas, tiene la oportunidad de hacerlo de nuevo, pero con penalizacion del 20% sobre nota final \n"
                print "Desea hacer nuevamente el cuestionario"
                rehacer = int(raw_input("1 - SI | 2 - NO"))
                if rehacer == 1:
                    pass
        elif oportunidad != 1:
            calificacion -= 20
            print "SU nueva calificacion es: " ,calificacion
                
                
    
    except:
        print "NO HAY RESPUESTAS"
    



n = 0
def Datos_user():
   
    try:
        while True:
            #try:
               # o  = int(raw_input("Opcion"))
               # if o == 1:
            try:
                login = str(raw_input("Usuario: "))
                name = str(raw_input("Nombre: "))
                surname = str(raw_input("Apellidos: "))
                address = str(raw_input("Direccion: "))
                depto = str(raw_input("Departamento: "))
                
            except:
                print "DIgite texto"
            try:
                for k ,v in Datos_usuario.iteritems():
                    tel = int(raw_input("Telefono"))
                    if tel == v[5]:
                       print "NUMERO DE TELEFONO YA EXISTE"
                       
                    else:
                        Datos_usuario[n] = (login,name,surname,address,depto,tel)
                
                print Datos_usuario
                for k ,v in Datos_usuario.iteritems():
                    print v[0]
                break
            except:
                print"DIGITE NUMEROS"
                
                        
                #elif o == 2:
                #    break
           # except:
              #  print "mal"

            
    except:
        print "NO HAY USUARIOS INGRESADOS"
         
    
def barajar(num):
    if num == 0:
        interrogantes = list(preguntas) 
        for i in interrogantes:
            random.shuffle(interrogantes)
            print i    
    
def goto(cont):
    global line
    line = cont

                   
while True:
    print "SISTEMA DE CUESTIONARIO"
    print " -------OPCIONES------- "
    print "1 - Registrar nuevo usuario"
    print "2 - Iniciar cuestionario"
    print "3 - Reanudar cuestionario"
    print "4 - Mostrar resultados"
    print "5 - Salir"
    
    try:
        opcion = int(raw_input("Seleccione opcion: "))
        
        if opcion == 1:
            Datos_user()
            n +=1
    
        elif opcion == 2:
            #print Datos_usuario[login]
            login = raw_input("Digite su usuario_: ")
            for k ,v in Datos_usuario.iteritems():
                
                if v[0] == login:
                    print "BIENVENIDO" ,v[1] ,v[2]
                    num = int(raw_input("Digite 0 para Aleatorio y 1 para orden normal. "))
                    if num == 0:
                        barajar(num)
                        
                    elif num == 1:
                        
                        print "INDICACIONES"
                        print "Para seleccionar la primera opcion digite 0"
                        print "Para seleccionar la segunda opcion digite 1"
                        print "Para seleccionar la tercera opcion digite 2"
                        print "Para seleccionar la cuarta opcion digite 3"
                        print "Para seleccionar la quinta opcion digite 4"
                        print "Para interrumpir el cuestionario presione 9 en cualquiera de las respuestas"
                        
                        while True:
                            try:
                                print preguntas[0], ":" ,Respuestas1
                                respuesta1_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta1_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta1_1 == 9 or respuesta1_2 == 9: 
                                    break
                                else:
                                    cont = 2 
                                
                                print "\n" ,preguntas[1], ":" ,Respuestas2
                                respuesta2_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta2_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta2_1 == 9 or respuesta2_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[2], ":" ,Respuestas3
                                respuesta3_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta3_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta3_1 == 9 or respuesta3_2 == 9:
                                    break
                                else:
                                    cont += 1 
                                
                                print "\n" ,preguntas[3], ":" ,Respuestas4
                                respuesta4_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta4_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta4_1 == 9 or respuesta4_2 == 9:
                                    break
                                else:
                                    cont += 1 
                                
                                print "\n" ,preguntas[4], ":" ,Respuestas5
                                respuesta5_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta5_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta5_1 == 9 or respuesta5_2 == 9:
                                    break
                                else:
                                    cont += 1 
                                
                                print "\n" ,preguntas[5], ":" ,Respuestas6
                                respuesta6_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta6_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta6_1 == 9 or respuesta6_2 == 9:
                                    break
                                else:
                                    cont += 1 
                                
                                print "\n" ,preguntas[6], ":" ,Respuestas7
                                respuesta7_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta7_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta7_1 == 9 or respuesta7_2 == 9:
                                    break
                                else:
                                    cont += 1 
                                
                                print "\n" ,preguntas[7], ":" ,Respuestas8
                                respuesta8_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta8_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta8_1 == 9 or respuesta8_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[8], ":" ,Respuestas9
                                respuesta9_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta9_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta9_1 == 9 or respuesta9_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[9], ":" ,Respuestas10
                                respuesta10_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta10_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta10_1 == 9 or respuesta10_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[10], ":" ,Respuestas11
                                respuesta11_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta11_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta11_1 == 9 or respuesta11_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[11], ":" ,Respuestas12
                                respuesta12_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta12_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta12_1 == 9 or respuesta12_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[12], ":" ,Respuestas13
                                respuesta13_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta13_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta13_1 == 9 or respuesta13_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[13], ":" ,Respuestas14
                                respuesta14_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta14_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta14_1 == 9 or respuesta14_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[14], ":" ,Respuestas15
                                respuesta15_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta15_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta15_1 == 9 or respuesta15_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[15], ":" ,Respuestas16
                                respuesta16_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta16_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta16_1 == 9 or respuesta16_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[16], ":" ,Respuestas17
                                respuesta17_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta17_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta17_1 == 9 or respuesta17_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[17], ":" ,Respuestas18
                                respuesta18_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta18_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta18_1 == 9 or respuesta18_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[18], ":" ,Respuestas19
                                respuesta19_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta19_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta19_1 == 9 or respuesta19_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[19], ":" ,Respuestas20
                                respuesta20_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta20_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta20_1 == 9 or respuesta20_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[20], ":" ,Respuestas21
                                respuesta21_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta21_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta21_1 == 9 or respuesta21_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[21], ":" ,Respuestas22
                                respuesta22_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta22_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta22_1 == 9 or respuesta22_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[22], ":" ,Respuestas23
                                respuesta23_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta23_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta23_1 == 9 or respuesta23_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[23], ":" ,Respuestas24
                                respuesta24_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta24_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta24_1 == 9 or respuesta24_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[24], ":" ,Respuestas25
                                respuesta25_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta25_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta25_1 == 9 or respuesta25_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[25], ":" ,Respuestas26
                                respuesta26_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta26_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta26_1 == 9 or respuesta26_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[26], ":" ,Respuestas27
                                respuesta27_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta27_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta27_1 == 9 or respuesta27_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[27], ":" ,Respuestas28
                                respuesta28_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta28_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                                if respuesta28_1 == 9 or respuesta28_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[28], ":" ,Respuestas29
                                respuesta29_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta29_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta29_1 == 9 or respuesta29_2 == 9:
                                    break
                                else:
                                    cont += 1
                                
                                print "\n" ,preguntas[29], ":" ,Respuestas30
                                respuesta30_1 = int(raw_input("Seleccione la primera respuesta: "))
                                respuesta30_2 = int(raw_input("Seleccione la segunda respuesta: "))
                                if respuesta30_1 == 9 or respuesta30_2 == 9:
                                    break
                                else:
                                    cont += 1
                                    oportunidad += 1
                                    print "\n" 
                                    break
                            except: 
                                print "Debe digitar numeros"
        
                        
                        
                    else:
                        print "No valido"
            else:
                print "Usuario Equivocado"        
                                                                                                                                                                                                                                
        elif opcion == 3:
            
            try:
                line = cont
            
                while True:
                    try:            
                        if line == 1: 
                            print preguntas[0], ":" ,Respuestas1
                            respuesta1_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta1_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta1_1 == 9 or respuesta1_2 == 9:
                                break
                            else:
                                cont = 1 
                            
                        elif line == 2: 
                            print "\n" ,preguntas[1], ":" ,Respuestas2
                            respuesta2_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta2_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta2_1 == 9 or respuesta2_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(3)
                            
                        elif line == 3: 
                            print "\n" ,preguntas[2], ":" ,Respuestas3
                            respuesta3_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta3_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta3_1 == 9 or respuesta3_2 == 9:
                                break
                            else:
                                cont += 1 
                                goto(4)
                            
                        elif line == 4: 
                            print "\n" ,preguntas[3], ":" ,Respuestas4
                            respuesta4_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta4_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta4_1 == 9 or respuesta4_2 == 9:
                                break
                            else:
                                cont += 1 
                                goto(5)
                            
                        elif line == 5:
                            print "\n" ,preguntas[4], ":" ,Respuestas5
                            respuesta5_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta5_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta5_1 == 9 or respuesta5_2 == 9:
                                break
                            else:
                                cont += 1 
                                goto(6)
                            
                        elif line == 6: 
                            print "\n" ,preguntas[5], ":" ,Respuestas6
                            respuesta6_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta6_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta6_1 == 9 or respuesta6_2 == 9:
                                break
                            else:
                                cont += 1 
                                goto(7)
                            
                        elif line == 7: 
                            print "\n" ,preguntas[6], ":" ,Respuestas7
                            respuesta7_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta7_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta7_1 == 9 or respuesta7_2 == 9:
                                break
                            else:
                                cont += 1 
                                goto(8)
                            
                        elif line == 8: 
                            print "\n" ,preguntas[7], ":" ,Respuestas8
                            respuesta8_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta8_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta8_1 == 9 or respuesta8_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(9)
                            
                        elif line == 9: 
                            print "\n" ,preguntas[8], ":" ,Respuestas9
                            respuesta9_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta9_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta9_1 == 9 or respuesta9_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(10)
                            
                        elif line == 10: 
                            print "\n" ,preguntas[9], ":" ,Respuestas10
                            respuesta10_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta10_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta10_1 == 9 or respuesta10_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(11)
                            
                        elif line == 11: 
                            print "\n" ,preguntas[10], ":" ,Respuestas11
                            respuesta11_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta11_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta11_1 == 9 or respuesta11_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(12)
                            
                        elif line == 12: 
                            print "\n" ,preguntas[11], ":" ,Respuestas12
                            respuesta12_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta12_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta12_1 == 9 or respuesta12_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(13)
                            
                        elif line == 13: 
                            print "\n" ,preguntas[12], ":" ,Respuestas13
                            respuesta13_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta13_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta13_1 == 9 or respuesta13_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(14)
                            
                        elif line == 14: 
                            print "\n" ,preguntas[13], ":" ,Respuestas14
                            respuesta14_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta14_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta14_1 == 9 or respuesta14_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(15)
                            
                        elif line == 15: 
                            print "\n" ,preguntas[14], ":" ,Respuestas15
                            respuesta15_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta15_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta15_1 == 9 or respuesta15_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(16)
                            
                        elif line == 16: 
                            print "\n" ,preguntas[15], ":" ,Respuestas16
                            respuesta16_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta16_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta16_1 == 9 or respuesta16_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(17)
                            
                        elif line == 17: 
                            print "\n" ,preguntas[16], ":" ,Respuestas17
                            respuesta17_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta17_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta17_1 == 9 or respuesta17_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(18)
                            
                        elif line == 18: 
                            print "\n" ,preguntas[17], ":" ,Respuestas18
                            respuesta18_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta18_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta18_1 == 9 or respuesta18_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(19) 
                            
                        elif line == 19: 
                            print "\n" ,preguntas[18], ":" ,Respuestas19
                            respuesta19_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta19_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta19_1 == 9 or respuesta19_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(20)
                            
                        elif line == 20: 
                            print "\n" ,preguntas[19], ":" ,Respuestas20
                            respuesta20_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta20_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta20_1 == 9 or respuesta20_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(21)
                            
                            
                        elif line == 21: 
                            print "\n" ,preguntas[20], ":" ,Respuestas21
                            respuesta21_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta21_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta21_1 == 9 or respuesta21_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(22)
                            
                        elif line == 22: 
                            print "\n" ,preguntas[21], ":" ,Respuestas22
                            respuesta22_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta22_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta22_1 == 9 or respuesta22_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(23)
                            
                        elif line == 23: 
                            print "\n" ,preguntas[22], ":" ,Respuestas23
                            respuesta23_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta23_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta23_1 == 9 or respuesta23_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(24)
                            
                        elif line == 24: 
                            print "\n" ,preguntas[23], ":" ,Respuestas24
                            respuesta24_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta24_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta24_1 == 9 or respuesta24_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(25)
                            
                        elif line == 25: 
                            print "\n" ,preguntas[24], ":" ,Respuestas25
                            respuesta25_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta25_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta25_1 == 9 or respuesta25_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(26)
                            
                        elif line == 26: 
                            print "\n" ,preguntas[25], ":" ,Respuestas26
                            respuesta26_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta26_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta26_1 == 9 or respuesta26_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(27)
                            
                        elif line == 27: 
                            print "\n" ,preguntas[26], ":" ,Respuestas27
                            respuesta27_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta27_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta27_1 == 9 or respuesta27_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(28)
                            
                        elif line == 28: 
                            print "\n" ,preguntas[27], ":" ,Respuestas28
                            respuesta28_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta28_2 = int(raw_input("Seleccione la segunda respuesta: ")) 
                            if respuesta28_1 == 9 or respuesta28_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(29)
                            
                        elif line == 29: 
                            print "\n" ,preguntas[28], ":" ,Respuestas29
                            respuesta29_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta29_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta29_1 == 9 or respuesta29_2 == 9:
                                break
                            else:
                                cont += 1
                                goto(30) 
                            
                        elif line == 30: 
                            print "\n" ,preguntas[29], ":" ,Respuestas30
                            respuesta30_1 = int(raw_input("Seleccione la primera respuesta: "))
                            respuesta30_2 = int(raw_input("Seleccione la segunda respuesta: "))
                            if respuesta30_1 == 9 or respuesta30_2 == 9:
                                break
                            else:
                                cont += 1
                                oportunidad += 1
                                print "\n" 
                                break
                    except:
                        print "Digite solo numeros"  
            except:
                print "EL CUESTIONARIO NO HA SIDO INICIADO"                     
            
        elif opcion == 4:
            mostrar_resultados()
            
        elif opcion == 5:  
            break    

        
        else:
            print "Opcion Invalida"
    except:
        print "DEBE DIGITAR NUMEROS"
