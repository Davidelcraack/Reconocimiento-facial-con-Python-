import tkinter as tk
from tkinter import Menu,messagebox,simpledialog,filedialog, Canvas

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.configurar_ventana()

    def configurar_ventana(self):
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")
        self.ventana.title("Inicio de sesion por reconocimiento facial")
        self.ventana.configure(bg="#8ed1fc")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.resizable(False, False)

        menubar = Menu(self.ventana)
        menu_archivo = Menu(menubar)
        menubar.add_cascade(menu=menu_archivo, label='Archivo')
        menu_archivo.add_command(label="Crear usuario", command=self.crear_usuario)
        menu_archivo.add_command(label="Modificar", command=self.modificar)

        menubar.add_command(label='Cerrar Sesion', command=self.cerrar_sesion)

        #Aqui se muestra todo lo que sale cuando vamos a iniciar sesion 
        frame = tk.Frame(self.ventana, bg="#EFEAE9")
        frame.pack(pady=20)
        frame_izquierda = tk.Frame(frame, bg="#EFEAE9")
        frame_izquierda.pack(side="left", padx=10)
        titulo = tk.Label(frame_izquierda, text="Introduce el nombre del usuario", font=("Arial", 14, "bold"), bg="#EFEAE9", fg="#000")
        titulo.pack(pady=10, anchor="center")
        entry_nombre = tk.Entry(frame_izquierda, width=27)
        entry_nombre.pack(pady=10, anchor="center")
        frame_columnas = tk.Frame(frame_izquierda, bg="#EFEAE9")
        frame_columnas.pack()
        columna1 = tk.Frame(frame_columnas, bg="#EFEAE9")
        columna1.pack(side="left", padx=10)
        boton_iniciar = tk.Button(columna1, text="Verificar", bg="#0693e3", fg="#fff", width=15, command="")
        boton_iniciar.pack(pady=10)

        frame_derecha = tk.Frame(frame, bg="#EFEAE9")
        frame_derecha.pack(side="left")
        canvas = Canvas(frame_derecha, width=750, height=750, bg="#EFEAE9")
        canvas.pack()
        canvas.create_rectangle(5, 5, 750, 750, outline="#202123", width=5)

        # Configurar otros elementos de la interfaz aquí
        # nota esto es solo para mostrar los datos del menu
        self.ventana.config(menu=menubar)

    def crear_usuario(self):
        print("Nuevo")

    def modificar(self):
        print("modificar")

    def cerrar_sesion(self):
        print("Cerrar Sesión")

    def ejecutar(self):
        self.ventana.mainloop()

# Crear una instancia de la clase y ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.ejecutar()