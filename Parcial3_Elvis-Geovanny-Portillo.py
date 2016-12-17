#coding=utf-8
import wx
import os
from subprocess import call, Popen, PIPE

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        self.dirname=''

        wx.Frame.__init__(self, parent, title=title, size=(800,500)) #Creamos el Frame
        sBar = self.CreateStatusBar(1) #Creamos una Barra de Estado 			
        self.texto = wx.StaticText(self, 0, "Ingrese URL: ",pos=(10,50)) #Label
        self.cajadetexto = wx.TextCtrl(self,value="", pos=(175, 50), size=(400,-1)) #Texbox
        self.texto = wx.StaticText(self, 0, "Seleccione Calidad: ",pos=(10,100))
        self.lista = ['MP4 - 720X1280', 'WEBM - 720X1280', 'MP4 - 360X640', "MP3"] #Lista de elementos que tendrá el Combobox
        self.combo_lista = wx.ComboBox(self, value = ' ', pos=(175, 100), size=(160, -1), choices=self.lista, style=wx.CB_DROPDOWN)
        
        boton_descarga =wx.Button(self, label="Descargar", pos=(250,150))
        boton_cancelar =wx.Button(self, label="Cancelar", pos=(400,150))

        # Creando el submenu
        menuArchivo = wx.Menu() 
        menuActualizar = menuArchivo.Append(0, "&Actualizar"," Actualizar Programa")
        menuArchivo.AppendSeparator()
        menuAcercaDe = menuArchivo.Append(wx.ID_ABOUT, "A&cerca de"," Información del programa")
        menuAyuda = menuArchivo.Append(wx.ID_HELP,"&Ayuda"," Como utilizar la aplicación")

        # Creando la Barra de Menú
        menuBar = wx.MenuBar()
        menuBar.Append(menuArchivo,"&Archivo")       
        self.SetMenuBar(menuBar) 

        # Creando los eventos.
        self.Bind(wx.EVT_MENU, self.OnUpdate, menuActualizar)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAcercaDe)
        self.Bind(wx.EVT_MENU, self.Onhelp, menuAyuda)
        self.Bind(wx.EVT_BUTTON, self.OnClick, boton_descarga)
        self.Bind(wx.EVT_COMBOBOX, self.Seleccion)
        self.Bind(wx.EVT_BUTTON, self.Oncancel, boton_cancelar)
       
        self.Centre() 
        self.Show(True) #Mostramos el frame

    def Seleccion(self,e): #Función donde guardaremos el valor seleccionado en el combobox
		value = self.combo_lista.GetValue()
		global value
    
    def OnUpdate(self,e):#Función para actualizar aplicación, desde el submenú actualizar
		actualizar = Popen(["youtube-dl","-U"], stdout = PIPE)
		mostrar = actualizar.stdout.read()
		dlg = wx.MessageDialog(self, mostrar, "Actualizar software") #Creamos un cuadro de diálogo
		dlg.ShowModal() #Mostramos el cuadro
		dlg.Destroy() #Destruimos el cuadro
		
    def Onhelp(self,e):
        dlg = wx.MessageDialog( self, "Para descargar archivos:\n 1 - Digite URL \n 2 - Seleccione formato \n 3 - Click en descargar \n 4 - Seleccione directorio donde desea guardar \n 5 - Click en Save", "ayuda", wx.OK)
        dlg.ShowModal()
        dlg.Destroy() 
		
    def OnAbout(self,e):
        dlg = wx.MessageDialog( self, "Pequeña aplicacion desde la cual se pueden descargar videos o audio desde youtube", "Acerca de ElgeDownloader", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def Oncancel(self,e):
		cancelar = ["youtube-dl","--skip-download"]
		call(cancelar)

    def OnClick(self,e):
		texto_box = self.cajadetexto.GetValue()
		valor = self.combo_lista.GetValue()
		if texto_box.isspace() == True or valor.isspace() == True:
			dlg = wx.MessageDialog(self,"Debe ingresar una URL y seleccionar un formato","ERROR")
			dlg.ShowModal()
			dlg.Destroy()       
		else:
			dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)# Cuadro estilo guardar
			if dlg.ShowModal() == wx.ID_OK:
				self.filename=dlg.GetFilename() 
				nombre_archivo = self.filename
				self.dirname=dlg.GetDirectory()
				directorio = self.dirname
			dlg.Destroy()
			
			pwd = Popen(["pwd"], stdout=PIPE)
			read = pwd.stdout.read()
			lista = read.split("\n")
			directorio_actual = lista[0]
			
			try:
				if value == "MP3":
					proceso = Popen(['youtube-dl', texto_box,'-x', "--audio-format", "mp3", "-o", nombre_archivo+".mp3"],stdout=PIPE)
					#proceso = ['youtube-dl', texto_box,'-x', "--audio-format", "mp3", "-o", nombre_archivo+".mp3"]
					cortar = ["mv",directorio_actual+"/"+nombre_archivo+".mp3",directorio]
				elif value == 'MP4 - 720X1280':
					proceso = Popen(['youtube-dl', "-f","22",texto_box, "-o", nombre_archivo+".mp4"], stdout=PIPE)
					#proceso = ['youtube-dl', "-f","22",texto_box, "-o", nombre_archivo+".mp4"]
					cortar = ["mv",directorio_actual+"/"+nombre_archivo+".mp4",directorio]
				elif value == 'WEBM - 720X1280':
					proceso = Popen(['youtube-dl', "-f","18",texto_box, "-o", nombre_archivo+".webm"], stdout=PIPE)
					#proceso = ['youtube-dl', "-f","18",texto_box, "-o", nombre_archivo+".webm"]
					cortar = ["mv",directorio_actual+"/"+nombre_archivo+".webm",directorio]
					#pro = ["youtube-dl","-f","18",texto_box]
				elif value == 'MP4 - 360X640':
					proceso = Popen(['youtube-dl', "-f","43",texto_box, "-o", nombre_archivo+".mp4"], stdout=PIPE)
					#proceso = ['youtube-dl', "-f","43",texto_box, "-o", nombre_archivo+".mp4"]
					cortar = ["mv",directorio_actual+"/"+nombre_archivo+".mp4",directorio]
				
				escucha = proceso.stdout.read()
				self.control = wx.TextCtrl(self, value= escucha, style=wx.TE_MULTILINE,size=(500,100),pos=(100,250))	
				#call(proceso)
				call(cortar)
				
				
			except:
				print "No se puede descargar el archivo"
			dlg = wx.MessageDialog( self, "Archivo descargado satisfactoriamente", "Información", wx.OK)
			dlg.ShowModal() 
			dlg.Destroy()
				
app = wx.App(False)
frame = MainWindow(None, "ElgeDownloader")
app.MainLoop()
