from gi.repository import Gtk

p = 0

class MainGui:
	"GTK/Glade User intergace. This is a pyGTK window"
	def __init__(self):
		self.gladefile="entrega02.glade"
		self.glade = Gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.get_object("window1").show_all()
		signals = {"on_precio_change" : self.on_precio_change,
                           "on_combobox_changed" : self.on_combobox_changed
                           }
		
		self.glade.connect_signals(signals)
		
		self.entradaPrecio = self.glade.get_object("entradaPrecio")
                self.entradaCombobox = self.glade.get_object("entradaCombobox")
                self.precioFinal = self.glade.get_object("precioFinal")
                self.descuentoFinal = self.glade.get_object("descuentoFinal")
                
	def on_precio_change(self, widget):
		global num
		self.entradaPrecio.get_text()
		num = self.entradaPrecio.get_text()
		self.precioFinal.set_text(str(num))
	
	def on_combobox_changed(self, widget):
		precio = float(self.entradaPrecio.get_text())
		descuento = float(self.entradaCombobox.get_active_text())
		self.descuentoFinal.set_text(str(descuento))

		if self.entradaCombobox.get_active_text() == "0":
    			precioFinal = self.ceroDiscount(precio)
    			self.precioFinal.set_text(str(precioFinal))
		
    		if self.entradaCombobox.get_active_text() == "5":
    			precioFinal = self.descuentocinco(precio)
    			self.precioFinal.set_text(str(precioFinal))
    			
    		if self.entradaCombobox.get_active_text() == "10":
    			precioFinal = self.descuentodiez(precio)
    			self.precioFinal.set_text(str(precioFinal))

    		if self.entradaCombobox.get_active_text() == "20":
    			precioFinal = self.descuentoveinte(precio)
    			self.precioFinal.set_text(str(precioFinal))

    	def ceroDiscount(self,precio):
		desccinco = (precio) - ((precio*0)/100)
		return desccinco

    	def descuentocinco(self,precio):
		desccinco = (precio) - ((precio*5)/100)
		return desccinco
    	def descuentodiez(self, precio):
		descdiez = (precio) - ((precio*10)/100)
		return descdiez
    	def descuentoveinte(self, precio):
		descveinte = (precio) - ((precio*20)/100)
		return descveinte
 	
##        def on_combobox_changed(self, datosCombobox):
##                resultado = str(datosCombobox.get_active_text())
##		self.descuentoFinal.set_text(str(resultado))

    	def porcentaje(self,datosComboboxprecio):
		descuento = (datosCombobox) - ((datosCombobox*5)/100)
		return desccinco


if __name__=="__main__":
	MainGui()
	Gtk.main()
