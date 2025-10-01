import tkinter as Ventana

class Vehiculo:
    def __init__(self, placa, marca, color, tipo, hora_ingreso):
        self.placa = placa
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.hora_ingreso = hora_ingreso

    def __str__(self):
        return f"{self.placa} - {self.marca} - {self.color} - {self.tipo} - {self.hora_ingreso}"

class Formulario:
    def __init__(self):
        self.vehiculos = [] 
        
        self.ventana_formulario = Ventana.Tk()
        self.ventana_formulario.title("Registro de Vehículos")
        
        self.label_placa = Ventana.Label(self.ventana_formulario, text="Placa: ")
        self.entry_placa = Ventana.Entry(self.ventana_formulario)

        self.label_marca = Ventana.Label(self.ventana_formulario, text="Marca: ")
        self.entry_marca = Ventana.Entry(self.ventana_formulario)

        self.label_color = Ventana.Label(self.ventana_formulario, text="Color: ")
        self.entry_color = Ventana.Entry(self.ventana_formulario)

        self.label_tipo = Ventana.Label(self.ventana_formulario, text="Tipo (Residente/Visitante): ")
        self.entry_tipo = Ventana.Entry(self.ventana_formulario)

        self.label_hora = Ventana.Label(self.ventana_formulario, text="Hora de ingreso: ")
        self.entry_hora = Ventana.Entry(self.ventana_formulario)
        
        self.boton_guardar = Ventana.Button(self.ventana_formulario, text="Guardar",command=lambda: self.evento_guardar())
        self.boton_limpiar = Ventana.Button(self.ventana_formulario, text="Limpiar",command=lambda: self.evento_borrar())
        self.boton_mostrar = Ventana.Button(self.ventana_formulario, text="Mostrar Registros",command=lambda: self.evento_mostrar())
        self.label_mensaje = Ventana.Label(self.ventana_formulario,  fg="red")

        self.label_placa.pack()
        self.entry_placa.pack()
        self.label_marca.pack()
        self.entry_marca.pack()
        self.label_color.pack()
        self.entry_color.pack()
        self.label_tipo.pack()
        self.entry_tipo.pack()
        self.label_hora.pack()
        self.entry_hora.pack()
        self.boton_guardar.pack()
        self.boton_limpiar.pack()
        self.boton_mostrar.pack()
        self.label_mensaje.pack()

        self.ventana_formulario.mainloop()

    def evento_guardar(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        color = self.entry_color.get()
        tipo = self.entry_tipo.get()
        hora = self.entry_hora.get()

        validar_campos = lambda x: x if x else None
        if not (validar_campos(placa) and validar_campos(marca) and validar_campos(color) and validar_campos(tipo) and validar_campos(hora)):
            self.label_mensaje.config(text="Todos los campos son obligatorios", fg="red")
            return
        
        vehiculo = Vehiculo(placa, marca, color, tipo, hora)

        self.vehiculos.append(vehiculo)
        
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')
        
        self.label_mensaje.config(text="Vehículo guardado exitosamente", fg="green")

    def evento_borrar(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')
        self.label_mensaje.config(text="Campos limpiados", fg="blue")

    def evento_mostrar(self):
        if not self.vehiculos:
            self.label_mensaje.config(text="No hay vehículos registrados", fg="red")
        else:
            registros = "\n".join([str(vehiculo) for vehiculo in self.vehiculos])
            self.label_mensaje.config(text=registros, fg="black")
            print(registros)

obj_formulario = Formulario()
