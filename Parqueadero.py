import tkinter as Ventana
class Parqueadero:
    def __init__(self):
        self.entryPlaca = " "
        self.entryMarca = " "
        self.entryColor = " "
        self.entryTipo = " "
        self.entryHora = " "
        self.formulario = " "
        self.vehiculos = []
        
    def setPlaca(self, placa):
        self.placa = placa
    def getPlaca(self):
        return self.placa

    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color

    def setTipo(self, tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo

    def setHoraIngreso(self, hora):
        self.horaIngreso = hora
    def getHoraIngreso(self):
        return self.horaIngreso
        
    def iniciarVentana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro De Vehículos")
        self.formulario.geometry("800x800")
        self.formulario.resizable(False,True)
        self.formulario.configure(bg="lightblue")
        self.formulario.configure(cursor="hand2")
        return self.formulario
    
    def iniciarPreguntas(self):
        labelPlaca = Ventana.Label(self.formulario, text="Digite la placa del vehículo: ")
        labelPlaca.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), borderwidth=2, relief="raised", width=40, height=1, cursor="hand2", padx=10, pady=10, anchor="w")
        labelPlaca.pack()
        self.entryPlaca = Ventana.Entry(self.formulario)
        self.entryPlaca.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), width=40, insertbackground="black", cursor="xterm")
        self.entryPlaca.pack(padx=10, pady=10)

        labelMarca = Ventana.Label(self.formulario, text="Digite la marca del vehículo: ")
        labelMarca.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), borderwidth=2, relief="raised", width=40, height=1, cursor="hand2", padx=10, pady=10, anchor="w")
        labelMarca.pack()
        self.entryMarca = Ventana.Entry(self.formulario)
        self.entryMarca.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), width=40, insertbackground="black", cursor="xterm")
        self.entryMarca.pack(padx=10, pady=10)

        labelColor = Ventana.Label(self.formulario, text="Digite el color del vehículo: ")
        labelColor.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), borderwidth=2, relief="raised", width=40, height=1, cursor="hand2", padx=10, pady=10, anchor="w")
        labelColor.pack()
        self.entryColor = Ventana.Entry(self.formulario)
        self.entryColor.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), width=40, insertbackground="black", cursor="xterm")
        self.entryColor.pack(padx=10, pady=10)

        labelTipo = Ventana.Label(self.formulario, text="Digite el tipo (Residente / Visitante): ")
        labelTipo.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), borderwidth=2, relief="raised", width=40, height=1, cursor="hand2", padx=10, pady=10, anchor="w")
        labelTipo.pack()
        self.entryTipo = Ventana.Entry(self.formulario)
        self.entryTipo.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), width=40, insertbackground="black", cursor="xterm")
        self.entryTipo.pack(padx=10, pady=10)

        labelHora = Ventana.Label(self.formulario, text="Digite la hora de ingreso: ")
        labelHora.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), borderwidth=2, relief="raised", width=40, height=1, cursor="hand2", padx=10, pady=10, anchor="w")
        labelHora.pack()
        self.entryHora = Ventana.Entry(self.formulario)
        self.entryHora.configure(bg="yellow", fg="red", font=("Arial", 16, "bold"), width=40, insertbackground="black", cursor="xterm")
        self.entryHora.pack(padx=10, pady=10)

        self.botonGuardar = Ventana.Button(self.formulario, text="Guardar Cliente", font=("Arial", 16, "bold"), command=lambda: self.eventoClick())
        self.botonGuardar.configure(bg="blue", fg="yellow", width=30, cursor="hand2", highlightbackground="blue")
        self.botonGuardar.pack(padx=10, pady=10)

        self.botonLimpiar = Ventana.Button(self.formulario, text="Limpiar", font=("Arial", 16, "bold"), command=lambda: self.eventoBorrar())
        self.botonLimpiar.configure(bg="green", fg="white", width=30, cursor="hand2", highlightbackground="green")
        self.botonLimpiar.pack(padx=10, pady=10)
        
    def evento_click(self):
        valor = self.entry_nombre.get()
        print("Cliente guardado:", valor)

    def evento_borrar(self):
        self.entry_nombre.delete(0, Ventana.END)

        
    def validarCampos(self):
        if (self.entryPlaca.get().strip() == "" or
            self.entryMarca.get().strip() == "" or
            self.entryColor.get().strip() == "" or
            self.entryTipo.get().strip() == "" or
            self.entryHora.get().strip() == ""):
            return False
        return True
    
    def guardarVehiculo(self):
        if not self.validarCampos():
            Ventana.Label(self.formulario, text="Todos los campos son obligatorios", bg="yellow", fg="red", font=("Arial", 12, "bold")).pack(pady=10)
            return

        self.setPlaca(self.entryPlaca.get().upper())
        self.setMarca(self.entryMarca.get())
        self.setColor(self.entryColor.get())
        self.setTipo(self.entryTipo.get())
        self.setHoraIngreso(self.entryHora.get())

        vehiculo = {
            "placa": self.getPlaca(),
            "marca": self.getMarca(),
            "color": self.getColor(),
            "tipo": self.getTipo(),
            "horaIngreso": self.getHoraIngreso()
        }
        self.vehiculos.append(vehiculo)

        Ventana.Label(self.formulario, text=f"Vehículo registrado: {vehiculo}", bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
        print("Vehículo guardado:", vehiculo)  

    def limpiarCampos(self):
        self.entryPlaca.delete(0, Ventana.END)
        self.entryMarca.delete(0, Ventana.END)
        self.entryColor.delete(0, Ventana.END)
        self.entryTipo.delete(0, Ventana.END)
        self.entryHora.delete(0, Ventana.END)

    def mostrarRegistros(self):
        if not self.vehiculos:
            Ventana.Label(self.formulario, text="No hay vehículos registrados.", bg="yellow", fg="black", font=("Arial", 12, "bold")).pack(pady=10)
            return

        texto = "Registros:"
        for v in self.vehiculos:
            texto += f"{v['placa']} | {v['marca']} | {v['color']} | {v['tipo']} | {v['horaIngreso']}\n"

        Ventana.Label(self.formulario, text=texto, bg="lightblue", fg="black", font=("Arial", 12)).pack(pady=10)
        print("Lista de vehículos registrados:", self.vehiculos)


    def funcionGeneral(self, accion):
        if accion == "guardar":
            self.guardarVehiculo()
        elif accion == "limpiar":
            self.limpiarCampos()
        elif accion == "mostrar":
            self.mostrarRegistros()