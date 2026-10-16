import os
import tkinter as tk
from tkinter import ttk

try:
    from PIL import Image, ImageTk  # pip install pillow
except ImportError:
    Image = ImageTk = None

# Los .ico se buscan en la carpeta del script y en la carpeta /imagenes.
# En este proyecto, los archivos reales están en c:\xampp\hola_con_github\imagenes.
CARPETA = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(CARPETA, "imagenes")


def _resolver_icono(nombre_archivo):
    rutas = [
        os.path.join(CARPETA, nombre_archivo),
        os.path.join(CARPETA_IMAGENES, nombre_archivo),
    ]
    for ruta in rutas:
        if os.path.exists(ruta):
            return ruta
    return rutas[0]  # devuelve la ruta esperada para mostrar el error si no existe


ICONO_VENTANA = _resolver_icono("logo.ico")
LOGO_TARJETA = _resolver_icono("logo2.ico")  # logo dentro del login

# --- Paleta de colores ---
BG = "#16161d"          # fondo de la ventana
CARD = "#1e1e28"        # fondo de la tarjeta
INPUT_BG = "#2a2a36"    # fondo de los campos
BORDER = "#383846"      # borde normal
ACCENT = "#4f8cff"      # color de acento
ACCENT_HOVER = "#3a74e6"
ACCENT_PRESS = "#2e5fc2"
TEXT = "#f2f2f7"
MUTED = "#8b8b9a"
ERROR = "#ff6b6b"
OK = "#4cd9a0"

FUENTE = "Segoe UI"


class Login(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana, style="Card.TFrame", padding=(32, 30))
        self.ventana = ventana

        self._configurar_estilos()
        self._construir_interfaz()

        # Atajos de teclado
        ventana.bind("<Return>", lambda e: self.ingresar())
        ventana.bind("<Escape>", lambda e: self.salir())
        self.entrada_usuario.focus_set()

    # ------------------------------------------------------------------
    def _configurar_estilos(self):
        s = ttk.Style()
        s.theme_use("clam")

        s.configure(".", background=CARD, foreground=TEXT, font=(FUENTE, 10))
        s.configure("Card.TFrame", background=CARD)

        s.configure("Titulo.TLabel", font=(FUENTE, 20, "bold"),
                    foreground=TEXT, background=CARD)
        s.configure("Subtitulo.TLabel", font=(FUENTE, 10),
                    foreground=MUTED, background=CARD)
        s.configure("Texto.TLabel", font=(FUENTE, 9, "bold"),
                    foreground=MUTED, background=CARD)
        s.configure("Error.TLabel", font=(FUENTE, 9),
                    foreground=ERROR, background=CARD)

        # Campos de entrada con borde que cambia al enfocar
        s.configure("Moderno.TEntry",
                    fieldbackground=INPUT_BG, foreground=TEXT,
                    insertcolor=TEXT, padding=(10, 8),
                    bordercolor=BORDER, lightcolor=BORDER, darkcolor=BORDER,
                    borderwidth=1, relief="flat")
        s.map("Moderno.TEntry",
              bordercolor=[("focus", ACCENT), ("invalid", ERROR)],
              lightcolor=[("focus", ACCENT), ("invalid", ERROR)],
              darkcolor=[("focus", ACCENT), ("invalid", ERROR)])

        # Botón principal
        s.configure("Primario.TButton",
                    font=(FUENTE, 11, "bold"), foreground="#ffffff",
                    background=ACCENT, padding=(10, 10),
                    borderwidth=0, relief="flat", focuscolor=ACCENT,
                    bordercolor=ACCENT, lightcolor=ACCENT, darkcolor=ACCENT)
        s.map("Primario.TButton",
              background=[("pressed", ACCENT_PRESS), ("active", ACCENT_HOVER)],
              bordercolor=[("pressed", ACCENT_PRESS), ("active", ACCENT_HOVER)],
              lightcolor=[("pressed", ACCENT_PRESS), ("active", ACCENT_HOVER)],
              darkcolor=[("pressed", ACCENT_PRESS), ("active", ACCENT_HOVER)])

        # Botón secundario (solo texto, estilo "ghost")
        s.configure("Secundario.TButton",
                    font=(FUENTE, 10), foreground=MUTED,
                    background=CARD, padding=(10, 8),
                    borderwidth=0, relief="flat", focuscolor=CARD,
                    bordercolor=CARD, lightcolor=CARD, darkcolor=CARD)
        s.map("Secundario.TButton",
              foreground=[("active", TEXT)],
              background=[("active", INPUT_BG)],
              bordercolor=[("active", INPUT_BG)],
              lightcolor=[("active", INPUT_BG)],
              darkcolor=[("active", INPUT_BG)])

        # Checkbutton "Mostrar contraseña"
        s.configure("Moderno.TCheckbutton",
                    background=CARD, foreground=MUTED, font=(FUENTE, 9),
                    focuscolor=CARD, indicatorbackground=INPUT_BG,
                    indicatorforeground=ACCENT)
        s.map("Moderno.TCheckbutton",
              foreground=[("active", TEXT)],
              background=[("active", CARD)],
              indicatorbackground=[("selected", ACCENT)])

    # ------------------------------------------------------------------
    def _construir_interfaz(self):
        self.columnconfigure(0, weight=1)

        # Logo de la tarjeta (logo2.ico); si no se puede cargar, usa el dibujo
        self.logo_img = self._cargar_logo(LOGO_TARJETA, 72)
        if self.logo_img:
            tk.Label(self, image=self.logo_img, bg=CARD, bd=0).grid(
                row=0, column=0, pady=(0, 14))
        else:
            icono = tk.Canvas(self, width=64, height=64, bg=CARD,
                              highlightthickness=0)
            icono.create_oval(2, 2, 62, 62, fill=ACCENT, outline="")
            icono.create_oval(24, 14, 40, 30, fill="#ffffff", outline="")
            icono.create_arc(16, 32, 48, 66, start=0, extent=180,
                             fill="#ffffff", outline="")
            icono.grid(row=0, column=0, pady=(0, 14))

        ttk.Label(self, text="Bienvenido", style="Titulo.TLabel").grid(
            row=1, column=0, pady=(0, 2))
        ttk.Label(self, text="Inicia sesión para continuar",
                  style="Subtitulo.TLabel").grid(row=2, column=0, pady=(0, 22))

        # Usuario
        ttk.Label(self, text="USUARIO O CORREO", style="Texto.TLabel").grid(
            row=3, column=0, sticky="w", pady=(0, 5))
        self.entrada_usuario = ttk.Entry(self, style="Moderno.TEntry",
                                         font=(FUENTE, 11))
        self.entrada_usuario.grid(row=4, column=0, sticky="ew", pady=(0, 14))

        # Contraseña
        ttk.Label(self, text="CONTRASEÑA", style="Texto.TLabel").grid(
            row=5, column=0, sticky="w", pady=(0, 5))
        self.entrada_contrasena = ttk.Entry(self, style="Moderno.TEntry",
                                            show="•", font=(FUENTE, 11))
        self.entrada_contrasena.grid(row=6, column=0, sticky="ew", pady=(0, 8))

        # Mostrar contraseña
        self.ver_pass = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, text="Mostrar contraseña",
                        style="Moderno.TCheckbutton",
                        variable=self.ver_pass,
                        command=self._alternar_contrasena,
                        cursor="hand2").grid(row=7, column=0, sticky="w")

        # Mensaje de estado / error
        self.mensaje = tk.StringVar()
        self.lbl_mensaje = ttk.Label(self, textvariable=self.mensaje,
                                     style="Error.TLabel", anchor="center")
        self.lbl_mensaje.grid(row=8, column=0, sticky="ew", pady=(10, 6))

        # Botones
        self.boton_ingresar = ttk.Button(self, text="Ingresar",
                                         style="Primario.TButton",
                                         cursor="hand2", command=self.ingresar)
        self.boton_ingresar.grid(row=9, column=0, sticky="ew", pady=(0, 8))

        self.boton_salir = ttk.Button(self, text="Cancelar",
                                      style="Secundario.TButton",
                                      cursor="hand2", command=self.salir)
        self.boton_salir.grid(row=10, column=0, sticky="ew")

        # Limpiar el error al escribir
        for e in (self.entrada_usuario, self.entrada_contrasena):
            e.bind("<Key>", lambda ev: self._limpiar_estado())

    # ------------------------------------------------------------------
    @staticmethod
    def _cargar_logo(ruta, tamano):
        """Carga un .ico y lo escala. Devuelve None si no es posible."""
        if Image is None or not os.path.exists(ruta):
            return None
        try:
            img = Image.open(ruta).convert("RGBA")
            img = img.resize((tamano, tamano), Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"No se pudo cargar {ruta}: {e}")
            return None

    def _alternar_contrasena(self):
        self.entrada_contrasena.configure(show="" if self.ver_pass.get() else "•")

    def _limpiar_estado(self):
        self.mensaje.set("")
        for e in (self.entrada_usuario, self.entrada_contrasena):
            e.state(["!invalid"])

    def _error(self, texto, *campos):
        self.lbl_mensaje.configure(style="Error.TLabel")
        self.mensaje.set(texto)
        for c in campos:
            c.state(["invalid"])

    # ------------------------------------------------------------------
    def ingresar(self):
        usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get()

        if not usuario and not contrasena:
            self._error("Completa usuario y contraseña",
                        self.entrada_usuario, self.entrada_contrasena)
            return
        if not usuario:
            self._error("Ingresa tu usuario o correo", self.entrada_usuario)
            self.entrada_usuario.focus_set()
            return
        if not contrasena:
            self._error("Ingresa tu contraseña", self.entrada_contrasena)
            self.entrada_contrasena.focus_set()
            return

        # Aquí iría tu validación real
        print(f"Intentando iniciar sesión como: {usuario}")
        ttk.Style().configure("Ok.TLabel", font=(FUENTE, 9),
                              foreground=OK, background=CARD)
        self.lbl_mensaje.configure(style="Ok.TLabel")
        self.mensaje.set("Verificando credenciales...")

    def salir(self):
        self.ventana.destroy()


# --- Arranque ---
if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Inicio de Sesión")
    raiz.configure(background=BG)
    raiz.resizable(False, False)

    # Icono de la ventana (logo.ico)
    try:
        raiz.iconbitmap(ICONO_VENTANA)
    except tk.TclError:
        print("No se encontró logo.ico, se usa el icono por defecto")

    app = Login(raiz)
    app.pack(padx=40, pady=40)  # la tarjeta flota sobre el fondo oscuro

    # Centrar la ventana según su tamaño real
    raiz.update_idletasks()
    ancho, alto = raiz.winfo_width(), raiz.winfo_height()
    x = (raiz.winfo_screenwidth() - ancho) // 2
    y = (raiz.winfo_screenheight() - alto) // 2
    raiz.geometry(f"+{x}+{y}")

    raiz.mainloop()