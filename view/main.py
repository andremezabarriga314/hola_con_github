import sys
import os
from tkinter import *

# Forzamos de forma segura la ruta para encontrar el archivo de la misma carpeta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importamos todo desde el archivo login.py (en minúsculas)
from login import *  

if __name__ == '__main__':
    ventana = Tk()
    ventana.title("Sistema Principal")
    ventana.geometry("400x300")  
    
    # Llamamos a la clase Login (Con 'L' mayúscula)
    app = Login(ventana)
    
    ventana.mainloop()
