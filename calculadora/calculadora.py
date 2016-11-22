#Linea para importar GTK
from gi.repository import Gtk
#Clase que carga la interfaz

class MainGui:
	def __init__(self):
            
		self.gladefile = "calculadora.glade" 
        	self.glade = Gtk.Builder()
       		self.glade.add_from_file(self.gladefile)
        	self.glade.get_object("window1").show_all()
        	
		signals = {
		"cero_btn" : self.cero_btn,
                           
		"uno_btn" : self.uno_btn,
                           
		"dos_btn" : self.dos_btn,
                           
		"tres_btn" : self.tres_btn,
                           
		"cuatro_btn" : self.cuatro_btn,
                           
		"cinco_btn" : self.cinco_btn,
                           
		"seis_btn" : self.seis_btn,
                           
		"siete_btn" : self.siete_btn,
                           
		"ocho_btn" : self.ocho_btn,
                           
		"nueve_btn" : self.nueve_btn,
                           
		"suma_btn" : self.suma_btn,
                           
		"nueve_btn" : self.nueve_btn,
                           
		"resta_btn" : self.resta_btn,
                           
		"multiplica_btn" : self.multiplica_btn,
                           
		"divide_btn" : self.divide_btn,
                            
		"punto_btn" : self.punto_btn,

                "igual_btn" : self.igual_btn,

		"borrar_btn" : self.borrar_btn
                           }

		self.glade.connect_signals(signals)
		self.entry = self.glade.get_object("entry")

		self.operacion1 = ""
		self.operacion2 = ""
		self.operador = ""

	def cero_btn(self,widget):
                num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(0)
		self.entry.set_text(num)
		
	def uno_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(1)
		self.entry.set_text(num)

	def dos_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(2)
		self.entry.set_text(num)

        def tres_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(3)
		self.entry.set_text(num)

	def cuatro_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(4)
		self.entry.set_text(num)
		
	def cinco_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(5)
		self.entry.set_text(num)

	def seis_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(6)
		self.entry.set_text(num)

        def siete_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(7)
		self.entry.set_text(num)
	
	def ocho_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(8)
		self.entry.set_text(num)

        def nueve_btn(self,widget):
		num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
		num += str(9)
		self.entry.set_text(num)

	def suma_btn(self,widget):
		self.operacion1 = self.entry.get_text()
		self.operador = "+"
		self.entry.set_text("")

        def resta_btn(self,widget):
		self.operacion1 = self.entry.get_text()
		self.operador = "-"
		self.entry.set_text("")
	
	def multiplica_btn(self,widget):
		self.operacion1 = self.entry.get_text()
		self.operador = "*"
		self.entry.set_text("")

        def divide_btn(self,widget):
		self.operacion1 = self.entry.get_text()
		self.operador = "/"
		self.entry.set_text("")

	def punto_btn(self,widget):
                num = ""
		if self.entry.get_text() != '':
			num = self.entry.get_text()
			num += str(".")
			
	def borrar_btn(self, widget):
		self.entry.set_text("")
		

        def igual_btn(self,widget):
                calculo = 0
		self.operacion2 = self.entry.get_text()
		if self.operador == "-":
			calculo = float(self.operacion1) - float(self.operacion2)
		if self.operador == "+":
			calculo = float(self.operacion1) + float(self.operacion2)
		if self.operador == "/":
			try:
				calculo = float(self.operacion1) / float(self.operacion2)
			except:
				print("error, La division por cero no esta definida")
		if self.operador == "*":
			calculo = float(self.operacion1) * float(self.operacion2)
		self.entry.set_text(str(calculo))

#Para cargar la interfaz grafica llamando a MainGui y Gtk
if __name__== "__main__":
	MainGui()
	Gtk.main()
