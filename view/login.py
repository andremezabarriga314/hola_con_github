from tkinter import *
from tkinter import ttk  

# La clase DEBE empezar con 'L' mayúscula
class Login(ttk.Frame):
    
    # Corrección: __init__ con dobles guiones bajos abajo y self
    def __init__(self, ventana):
        super().__init__(ventana)
        
        # Configuración básica del contenedor
        self.config(padding=(20, 20))
        self.grid(column=0, row=0, sticky=(N, S, E, W))
        
        # Un título de prueba para ver que funciona
        self.label_titulo = ttk.Label(self, text="Control de Acceso", font=("Arial", 16))
        self.label_titulo.grid(column=0, row=0, columnspan=2, pady=10)
