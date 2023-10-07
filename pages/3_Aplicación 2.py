import streamlit as st
import datetime
import tkinter as tk
from tkinter import messagebox

# Diseño personalizado
st.header("Aplicacón 1")



def mostrar_fecha_hora():
    fecha_actual = datetime.datetime.now()
    mensaje = f"Fecha y hora actual:\n{fecha_actual}"
    messagebox.showinfo("Fecha y hora actual", mensaje)

def main():
    ventana = tk.Tk()
    ventana.title("Mostrar Fecha y Hora")
    
    etiqueta = tk.Label(ventana, text="¿Deseas ver la fecha y hora actual?")
    etiqueta.pack(padx=20, pady=20)
    
    boton_mostrar = tk.Button(ventana, text="Mostrar Fecha y Hora", command=mostrar_fecha_hora)
    boton_mostrar.pack()
    
    ventana.mainloop()

if __name__ == "__main__":
    main()