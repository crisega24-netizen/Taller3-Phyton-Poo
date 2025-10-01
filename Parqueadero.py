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
        
    def getPlaca(self):
        return self.placa

    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color

    def getTipo(self):
        return self.tipo

    def getHoraIngreso(self):
        return self.hora
    
    def setPlaca(self, placa):
        self.placa = placa
        if self.entryPlaca != " ":   
            self.entryPlaca.delete(0, Ventana.END)
            self.entryPlaca.insert(0, placa)

    def setMarca(self, marca):
        self.marca = marca
        if self.entryMarca != " ":
            self.entryMarca.delete(0, Ventana.END)
            self.entryMarca.insert(0, marca)

    def setColor(self, color):
        self.color = color
        if self.entryColor != " ":
            self.entryColor.delete(0, Ventana.END)
            self.entryColor.insert(0, color)

    def setTipo(self, tipo):
        self.tipo = tipo
        if self.entryTipo != " ":
            self.entryTipo.delete(0, Ventana.END)
            self.entryTipo.insert(0, tipo)

    def setHora(self, hora):
        self.hora = hora
        if self.entryHora != " ":
            self.entryHora.delete(0, Ventana.END)
            self.entryHora.insert(0, hora)
        
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

        botonGuardar = Ventana.Button(self.formulario, text="Guardar Vehículo", font=("Arial", 16, "bold"), command=lambda: self.funcionGeneral())
        botonGuardar.configure(bg="blue", fg="yellow", width=30, cursor="hand2", highlightbackground="blue")
        botonGuardar.pack(padx=10, pady=10)

        botonLimpiar = Ventana.Button(self.formulario, text="Limpiar Campos", font=("Arial", 16, "bold"), command=lambda: self.limpiarCampos())
        botonLimpiar.configure(bg="green", fg="white", width=30, cursor="hand2")
        botonLimpiar.pack(padx=10, pady=10)

        botonMostrar = Ventana.Button(self.formulario, text="Mostrar Registros", font=("Arial", 16, "bold"), command=lambda: self.mostrarRegistros())
        botonMostrar.configure(bg="purple", fg="white", width=30, cursor="hand2")
        botonMostrar.pack(padx=10, pady=10)

    def validarCampos(self):
        mensajes = []
        if self.entryPlaca.get().strip() == "":
            mensajes.append("Placa vacía")
        else:
            mensajes.append("Placa válida")
        if self.entryMarca.get().strip() == "":
            mensajes.append("Marca vacía")
        else:
            mensajes.append("Marca válida")
        if self.entryColor.get().strip() == "":
            mensajes.append("Color vacío")
        else:
            mensajes.append("Color válido")
        if self.entryTipo.get().strip() == "":
            mensajes.append("Tipo vacío")
        else:
            mensajes.append("Tipo válido")
        if self.entryHora.get().strip() == "":
            mensajes.append("Hora vacía")
        else:
            mensajes.append("Hora válida")
        return mensajes


    def tomarDatos(self):
        self.setPlaca(self.entryPlaca.get())
        self.setMarca(self.entryMarca.get())
        self.setColor(self.entryColor.get())
        self.setTipo(self.entryTipo.get())
        self.setHora(self.entryHora.get())

        vehiculo = {
            "placa": self.getPlaca(),
            "marca": self.getMarca(),
            "color": self.getColor(),
            "tipo": self.getTipo(),
            "hora": self.getHoraIngreso()
        }
        self.vehiculos.append(vehiculo)
        return vehiculo


    def imprimirDatos(self, mensajes, vehiculo):
        Ventana.Label(self.formulario, text="Resultados de validación:", font=("Arial", 14, "bold"), bg="yellow").pack(pady=10)
        for m in mensajes:
            Ventana.Label(self.formulario, text=m, bg="yellow", fg="black").pack()
        Ventana.Label(self.formulario, text=f"Vehículo registrado: {vehiculo}", bg="green", font=("Arial", 12, "bold")).pack(pady=10)

    def funcionGeneral(self):
        mensajes = self.validarCampos()
        vehiculo = self.tomarDatos()
        self.imprimirDatos(mensajes, vehiculo)

    def limpiarCampos(self):
        self.setPlaca("")
        self.setMarca("")
        self.setColor("")
        self.setTipo("")
        self.setHora("")

    def mostrarRegistros(self):
        if not self.vehiculos:
            Ventana.Label(self.formulario, text="No hay vehículos registrados", bg="red", fg="white").pack(pady=10)
        else:
            Ventana.Label(self.formulario, text="Vehículos registrados:", font=("Arial", 14, "bold"), bg="yellow").pack(pady=10)
            for v in self.vehiculos:
                Ventana.Label(self.formulario, text=str(v), bg="lightblue", fg="black").pack()
            print("=== Lista de Vehículos Registrados ===")
            for v in self.vehiculos:
                print(v)
