from tkinter import *
from Volumen import *
from integralesIndefinidas import *
from integralesDefinidas import *
from areas import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import tkinter.font as tkFont
import tkinter as tk
import os


def main():
    ventana = Tk()
    ventana.iconbitmap('data/logo.ico')
    ventana.config(bg="white", bd=0)
    ventana.title('PlyMath')
    label = tkinter.Label(ventana, text="PlyMath", bg="white", fg="#007b99", )
    label.configure(font=("Bahnschrift Light bold", 19, tkFont.BOLD))
    label.pack()
    style = ttk.Style()
    settings = {"TNotebook.Tab": {"configure": {"padding": [111.2, 5],
                                                "background": "#f39200",
                                                "font": "Helvetica, 12"
                                                }}}
    style.theme_create("mi_estilo", parent="alt", settings=settings)
    style.theme_use("mi_estilo")

    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand=2, padx=3, pady=10)
    notebook.pressed_index = None
    pesInicio = tkinter.Frame(notebook, background="white")
    notebook.add(pesInicio, text="Inicio")

    img1 = PhotoImage(file="data/Area.png")
    img1 = img1.subsample(4, 4)
    lblarea = tk.Label(pesInicio, image=img1, borderwidth=0, highlightthickness=0)
    lblarea.place(x=7, y=10)

    img2 = PhotoImage(file="data/volumen.png")
    img2 = img2.subsample(4, 4)
    lblvol = tk.Label(pesInicio, image=img2, borderwidth=0, highlightthickness=0)
    lblvol.place(x=900, y=10)

    separ = tk.Label(pesInicio, text="Generalidades PlyMath", font="Helvetica 14 bold", bg='white',
                     foreground='#007b99')
    separ.place(x=580, y=270)
    sepa = tk.Label(pesInicio,
                    text="◥█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
                         "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█◤",
                    font="Helvetica 14", bg='white', foreground='#f39200')
    sepa.place(x=0, y=300)

    img3 = PhotoImage(file="data/g1.png")
    img3 = img3.subsample(4, 4)
    lblg1 = tk.Label(pesInicio, image=img3, borderwidth=0, highlightthickness=0)
    lblg1.place(x=7, y=330)

    img4 = PhotoImage(file="data/g2.png")
    img4 = img4.subsample(4, 4)
    lblg2 = tk.Label(pesInicio, image=img4, borderwidth=0, highlightthickness=0)
    lblg2.place(x=455, y=330)

    img5 = PhotoImage(file="data/g3.png")
    img5 = img5.subsample(4, 4)
    lblg3 = tk.Label(pesInicio, image=img5, borderwidth=0, highlightthickness=0)
    lblg3.place(x=900, y=330)

    img6 = PhotoImage(file="data/syslac.png")
    img6 = img6.subsample(12, 12)
    lblg4 = tk.Label(pesInicio, image=img6, borderwidth=0, highlightthickness=0)
    lblg4.place(x=550, y=80)

    def botmore():
        notebook.select(pes3)

    botmas = tk.Button(pesInicio, text="Más funciones", width="20", height="1", command=botmore,
                       font="Helvetica 14", foreground="black", bg='#f39200', activebackground='white',
                       activeforeground='#f39200')
    botmas.place(x=115, y=520)

    pes0 = tkinter.Frame(notebook, background="white")
    img7 = PhotoImage(file="data/syslac.png")
    img7 = img6.subsample(2, 2)

    fuente = tk.Label(pesInicio, text="Fuente: ", font="Helvetica 14 italic", bg='white')
    fuente.place(x=790, y=590)
    referencia = tk.Label(pesInicio, text="Larson, Ron y Edwards, Bruce (2011). Cálculo.  McGraw-Hill",
                          font="Helvetica 12 italic", bg='white')
    referencia.place(x=860, y=592)

    # --------Desarrollo de la pestaña integrales-----
    # -----------Parte Indefinidas-----------------
    # Ecuacion
    def ejem():
        ventana_about = Toplevel()
        ventana_about.iconbitmap('data/logo.ico')
        ventana_about.config(bg="white")
        ventana_about.title("About Us")
        ventana_about.geometry("1300x650+30+50")
        ventana_about.resizable(True, True)

        Label(ventana_about, text="About Us", width="15", height="1", font="Helvetica 14 bold",
              bg="white", fg="orange").place(x=600, y=10)
        contexto = """Plymath es un programa de escritorio creado por estudiantes del semillero SYSLAC que ayuda al fortalecimiento de conocimiento de ciencias basicas. 
Este programa se centra en temas especificos del calculo integral, como definiciones, y aplicaciones de integrales, además de generar graficas para un 
mejor entendimiento de los diferentes conceptos. """
        Label(ventana_about, text=contexto, width="115", height="3", font="Helvetica 12 bold",
              bg="white", fg="#007b99", justify=tk.LEFT).place(x=80, y=40)

        Label(ventana_about, text="Conoce nuestro equipo", width=20, height=1, font="Helvetica 14 bold",
              bg="white", fg="orange").place(x=10, y=115)
        equipo = ["Camilo Garcia Saldarriaga",
                  "Juan Jose Mazo Acevedo",
                  "Bryan Arias Quinchia",
                  "Sneyder Martinez Caicedo",
                  "Ingrid Durley Torres Pardo",
                  "Mauricio López Bonilla"]

        Label(ventana_about, text=equipo[0], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=20, y=160)
        e1photo = PhotoImage(file="data\Camilo.png", master=ventana_about).subsample(8, 7)
        e1_muestra = Label(ventana_about, image=e1photo)
        e1_muestra.image = e1photo
        e1_muestra.place(x=30, y=190)
        c = """Desarrollador
camilo.garciasa@amigo.edu.co"""
        e1_descripcion = Label(ventana_about, text=c, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e1_descripcion.place(x=155, y=190)

        Label(ventana_about, text=equipo[2], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=20, y=370)
        e2photo = PhotoImage(file="data\Brayan.png", master=ventana_about).subsample(8, 7)
        e2_muestra = Label(ventana_about, image=e2photo)
        e2_muestra.image = e2photo
        e2_muestra.place(x=30, y=400)
        b = """Desarrollador
bryan.ariasqu@amigo.edu.co"""
        e2_descripcion = Label(ventana_about, text=b, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e2_descripcion.place(x=150, y=400)

        Label(ventana_about, text=equipo[1], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=475, y=160)
        e3photo = PhotoImage(file="data\Juan.png", master=ventana_about).subsample(8, 7)
        e3_muestra = Label(ventana_about, image=e3photo)
        e3_muestra.image = e3photo
        e3_muestra.place(x=485, y=190)
        j = """Desarrollador
juan.mazoac@amigo.edu.co"""
        e3_descripcion = Label(ventana_about, text=j, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e3_descripcion.place(x=615, y=190)

        Label(ventana_about, text=equipo[3], width=30, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=475, y=370)
        e4photo = PhotoImage(file="data\Sneyder.png", master=ventana_about).subsample(7, 6)
        e4_muestra = Label(ventana_about, image=e4photo)
        e4_muestra.image = e4photo
        e4_muestra.place(x=485, y=400)
        s = """Desarrollador
sneyder.martinezca@amigo.edu.co"""
        e4_descripcion = Label(ventana_about, text=s, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e4_descripcion.place(x=615, y=400)

        Label(ventana_about, text=equipo[4], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=920, y=160)
        e5photo = PhotoImage(file="data\ingrid.png", master=ventana_about).subsample(8, 7)
        e5_muestra = Label(ventana_about, image=e5photo)
        e5_muestra.image = e5photo
        e5_muestra.place(x=930, y=190)
        i = """Docente Investigadora &
Directora del proyecto.
ingrid.torrespa@amigo.edu.co"""
        e5_descripcion = Label(ventana_about, text=i, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e5_descripcion.place(x=1055, y=190)

        Label(ventana_about, text=equipo[5], width=25, height=1, font="Helvetica 14", bg="white", justify=tk.LEFT,
              fg="orange").place(x=920, y=370)
        e6photo = PhotoImage(file="data\Brayan.png", master=ventana_about).subsample(8, 7)
        e6_muestra = Label(ventana_about, image=e6photo)
        e6_muestra.image = e6photo
        e6_muestra.place(x=930, y=400)
        m = """Jefe del departamento 
de Ciencias Basicas
mauricio.lopezbo@amigo.edu.co"""
        e6_descripcion = Label(ventana_about, text=m, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e6_descripcion.place(x=1055, y=400)

        Label(ventana_about, text="Agredecimientos a:", width=20, height=1, font="Helvetica 13 bold",
              bg="white", justify=tk.LEFT, fg="orange").place(x=5, y=550)

        d = """ David Estrada Jimenez
         por participación en el desarrollo del proyecto."""
        Label(ventana_about, text=d, width=40, height=2, font="Helvetica 12",
              bg="white", justify=tk.LEFT, fg="#007b99").place(x=40, y=575)

        jjd = """Juan Jose Hoyos Eusse
         por ser el docente promotor del proyecto."""
        Label(ventana_about, text=jjd, width=35, height=2, font="Helvetica 12",
              bg="white", justify=tk.LEFT, fg="#007b99").place(x=430, y=575)

    notebook.add(pes0, text='Integrales')
    btnab = Button(pes0, image=img7, command=ejem)
    btnab.place(x=1190, y=540)

    ecuaI = tk.Label(pes0, text="Digite el problema:", width="35", height="1", font="Helvetica 14", bg='white')
    caja1 = Entry(pes0, width=40, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                  highlightthickness=3)
    # Resultado
    resulI = tk.Label(pes0, text="El resultado de la integral es:", width="35", height="1", font="Helvetica 14",
                      bg='white')
    muestraI = tk.Label(pes0, text="", width="35", height="1", font="Helvetica 14 bold", background="white")
    # Grafica
    graficaI = tk.Label(pes0, text="¿Desea conocer la gráfica de la integral?", width="35", height="1",
                        font="Helvetica 14", bg='white')
    # Menu Despegable
    menuI = ttk.Combobox(pes0, width=35, font="Helvetica 18", state="readonly", foreground="#007b99",
                         values=["Sí.",
                                 "Sí, mostrando la gráfica de la función."])
    menuI.current()  # Valor por defectos

    # Botones de verificacion
    def obtenerI():
        funcion = caja1.get()
        respuesta = menuI.get()
        menuI.select_clear()
        solucion = muestraI.cget("text")
        graficaIS(funcion, solucion, respuesta)

    def limpiarI():
        caja1.delete(0, END)
        muestraI.config(text="")
        menuI.set("")
        messagebox.showinfo("Información", "La ecuación ha sido borrada")
        caja1.focus_set()

    def save():
        prueba = caja1.get()
        solucion = ecuacionI(prueba)
        muestraI.config(text=solucion)

    boton3 = Button(pes0, text="Borrar", width="20", height="1", font="Helvetica 14 bold",
                    command=limpiarI, foreground="white", bg='#007b99', activebackground='white',
                    activeforeground='#007b99')
    boton4 = Button(pes0, text="Calcular", width="20", height="1", font="Helvetica 14 bold",
                    command=save, foreground="white", bg='#007b99', activebackground='white',
                    activeforeground='#007b99')
    botonGraf = Button(pes0, text="Gráfica", width="20", font="Helvetica 14 bold",
                       command=obtenerI, foreground="white", bg='#007b99', activebackground='white',
                       activeforeground='#007b99')
    # -----------Parte Definidas-----------------
    # Limites
    limInfe = tk.Label(pes0, text="Ingrese límite inferior:", width="35", height="1", font="Helvetica 14", bg='white')
    cajaInfe = Entry(pes0, width=20, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                     highlightthickness=3)
    limSupe = tk.Label(pes0, text="Ingrese límite superior:", width="35", height="1", font="Helvetica 14", bg='white')
    cajaSupe = Entry(pes0, width=20, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                     highlightthickness=3)
    # Ecuacion
    ecuaD = tk.Label(pes0, text="Digite la ecuación:", width="35", height="1", font="Helvetica 14", bg='white')
    caja2 = Entry(pes0, width=40, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                  highlightthickness=3)
    # Pregunta
    question = '''      ¿Desea conocer el resultado
    en fraccionarios o en decimales ?'''
    pregu = tk.Label(pes0, text=question, width="35", height="2", font="Helvetica 14", justify=tk.LEFT, bg='white')
    # Menu Despegable
    menuD = ttk.Combobox(pes0, width=35, font="Helvetica 14", state="readonly", foreground="#007b99")
    menuD['values'] = ("Fraccionarios.",
                       "Decimales.")
    menuD.current()
    # Solucion
    resulD = tk.Label(pes0, text="El resultado de la integral es:", width="35", height="1", font="Helvetica 14",
                      bg="white")
    muestraD = tk.Label(pes0, text="", width="35", height="1", font="Helvetica 14  bold", bg="white")

    # Botones de verificacion
    def limpiarD():
        cajaInfe.delete(0, END)
        cajaSupe.delete(0, END)
        caja2.delete(0, END)
        menuD.set("")
        muestraD.config(text="")
        messagebox.showinfo("Información", "Los valores ingresados han sido borrados")
        cajaInfe.focus_set()

    def obtenerD():
        LimI = cajaInfe.get()
        LimS = cajaSupe.get()
        ec = caja2.get()
        res = menuD.get()
        menuD.select_clear()
        solucionI = ecuacionD(LimI, LimS, ec, res)
        muestraD.config(text=solucionI)

    boton5 = Button(pes0, text="Borrar", width="20", height="1", font="Helvetica 14 bold",
                    command=limpiarD, foreground="white", bg='#007b99', activebackground='white',
                    activeforeground='#007b99')
    boton6 = Button(pes0, text="Calcular", width="20", height="1", font="Helvetica 14 bold",
                    command=obtenerD, foreground="white", bg='#007b99', activebackground='white',
                    activeforeground='#007b99')
    boton7 = Button(pes0, text="Gráfica", width="20", height="1", font="Helvetica 14 bold",
                    command=lambda: graficaES(caja2.get(), cajaInfe.get(), cajaSupe.get()), foreground="white",
                    bg='#007b99',
                    activebackground='white', activeforeground='#007b99')

    # ShowWidgets
    def indefi():
        caja1.focus_set()
        ocultarD()
        ecuaI.grid(row=2, column=0, pady=5)
        caja1.place(x=630, y=120)
        resulI.grid(row=3, column=0, pady=25)
        muestraI.place(x=630, y=180)
        graficaI.grid(row=4, column=0, pady=10)
        menuI.place(x=630, y=245)
        boton3.grid(row=6, column=0, pady=50)
        boton4.grid(row=6, column=1)
        botonGraf.place(x=540, y=319)

    def defi():
        cajaInfe.focus_set()
        ocutarI()
        limInfe.grid(row=2, column=0)
        cajaInfe.place(x=630, y=115)
        limSupe.grid(row=3, column=0, pady=25)
        cajaSupe.place(x=630, y=170)
        ecuaD.grid(row=4, column=0, pady=4)
        caja2.place(x=630, y=225)
        pregu.grid(row=5, column=0, pady=25)
        menuD.place(x=630, y=310)
        resulD.grid(row=7, column=0)
        muestraD.place(x=630, y=360)
        boton5.grid(row=8, column=0, pady=35)
        boton6.grid(row=8, column=1)
        boton7.place(x=540, y=410)

    # OcultarWidgets
    def ocutarI():
        ecuaI.grid_forget()
        caja1.place_forget()
        graficaI.grid_forget()
        menuI.place_forget()
        resulI.grid_forget()
        muestraI.place_forget()
        boton3.grid_forget()
        boton4.grid_forget()
        botonGraf.place_forget()

    def ocultarD():
        limInfe.grid_forget()
        cajaInfe.place_forget()
        limSupe.grid_forget()
        cajaSupe.place_forget()
        ecuaD.grid_forget()
        caja2.place_forget()
        pregu.grid_forget()
        menuD.place_forget()
        resulD.grid_forget()
        muestraD.place_forget()
        boton5.grid_forget()
        boton6.grid_forget()
        boton7.place_forget()

    # Botones_I&D
    boton1 = Button(pes0, text="Indefinidas", width="78", height="2", font="Helvetica 10 bold",
                    command=indefi, foreground="white", bg='#f39200', activebackground='white',
                    activeforeground='#f39200')
    boton2 = Button(pes0, text="Definidas", width="80", height="2", font="Helvetica 10 bold",
                    command=defi, foreground="white", bg='#f39200', activebackground='white',
                    activeforeground='#f39200')
    # AGG botenes en pantalla
    boton1.grid(row=1, column=0, padx=16, pady=30)
    boton2.grid(row=1, column=1, padx=8, pady=30)
    # ----------FIN PARTE DE INTEGALES--------------------------------------#
    pes1 = tkinter.Frame(notebook, background="white")
    btnac = Button(pes1, image=img7, command=ejem)
    btnac.place(x=1190, y=540)
    imgejem = PhotoImage(file="data/ejemplo.png")
    imgejem = imgejem.subsample(1, 1)
    lblvol = tk.Label(pes1, image=imgejem, borderwidth=0, highlightthickness=0)
    lblvol.place(x=940, y=0)

    # --------Desarrollo de la pestaña Areas--------
    notebook.add(pes1, text='Área')
    fun1 = tk.Label(pes1, text="Ingrese la función en términos de x: ", width="35", height="1", font="Helvetica 14",
                    bg='white')
    fun1.place(x=10, y=25)
    caj1 = Entry(pes1, width=45, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                 highlightthickness=3)
    caj1.place(x=400, y=25)

    # accion boton
    def sefu():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una función")
        else:
            fun2.place(x=10, y=100)
            caj2.place(x=400, y=100)

    bot2fun = tk.Button(pes1, text="Añadir segunda función", width="20", height="1", command=sefu,
                        font="Helvetica 14", foreground="white", bg='#007b99', activebackground='white',
                        activeforeground='#007b99')
    bot2fun.place(x=50, y=60)
    fun2 = tk.Label(pes1, text="Ingrese la función en términos de x: ", width="35", height="1", font="Helvetica 14",
                    bg='white')
    caj2 = Entry(pes1, width=45, font="Helvetica 16", highlightbackground='#007b99',
                 highlightcolor='#f39200', highlightthickness=3)

    # accion boton
    def pun_cor():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una función")
        e2 = caj2.get()
        if not e2:
            e2 = 0
        aux1 = puntos_corte(e1, e2)
        resultPc = tk.Label(pes1, text="Los puntos de corte son: " + str(aux1), font="Helvetica 14", bg='white')
        resultPc.place(x=20, y=170)

    botpun = tk.Button(pes1, text="Calcular puntos de corte", width="20", height="1", command=pun_cor,
                       font="Helvetica 14", foreground="white", bg='#007b99', activebackground='white',
                       activeforeground='#007b99')
    botpun.place(x=50, y=130)
    liminfe = tk.Label(pes1, text="Ingrese límite inferior: ", width="35", height="1", font="Helvetica 14",
                       bg='white')
    liminfe.place(x=10, y=210)
    caj3 = Entry(pes1, width=45, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                 highlightthickness=3)
    caj3.place(x=400, y=210)
    limsupe = tk.Label(pes1, text="Ingrese límite superior: ", width="35", height="1", font="Helvetica 14",
                       bg='white')
    limsupe.place(x=10, y=260)
    caj4 = Entry(pes1, width=45, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                 highlightthickness=3)
    caj4.place(x=400, y=260)

    # accion boton
    def are():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una función")
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        try:
            float(l1)
            float(l2)
            aux2 = area(e1, e2, l1, l2)
            e1 = aux2[0]
            e2 = aux2[1]
            aux3 = aux2[2]
            funmay = tk.Label(pes1, text="La función mayor es: " + str(e1), width="45", height="1",
                              font="Helvetica 14", bg='white')
            funmay.place(x=20, y=380)
            funmen = tk.Label(pes1, text="La función menor es: " + str(e2), width="45", height="1",
                              font="Helvetica 14", bg='white')
            funmen.place(x=20, y=420)
            resulta = tk.Label(pes1, text="El área de la función es: " + str(aux3) + " U²", width="45", height="1",
                               font="Helvetica 14", bg='white')
            resulta.place(x=20, y=460)
        except ValueError:
            messagebox.showerror("Error", "Ingrese los límites en valores enteros o decimales")

    botresult = tk.Button(pes1, text="Calcular", width="20", height="1", command=are, font="Helvetica 14",
                          foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botresult.grid(row=14, column=0, pady=12)
    botresult.place(x=50, y=310)

    # accion boton
    def gra():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una función")
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        graficar(e1, e2, l1, l2)

    botgraf = tk.Button(pes1, text="Graficar", width="20", height="1", command=gra, font="Helvetica 14",
                        foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botgraf.place(x=50, y=520)

    # accion boton
    def eliminar():
        caj1.delete(0, END)
        caj2.delete(0, END)
        caj3.delete(0, END)
        caj4.delete(0, END)
        caj1.focus_set()
        resultPc = tk.Label(pes1, text=" ", width="86", height="1", font="Helvetica 14", bg='white')
        resultPc.place(x=20, y=170)
        funmay = tk.Label(pes1, text=" ", width="45", height="1", font="Helvetica 14", bg='white')
        funmay.place(x=20, y=380)
        funmen = tk.Label(pes1, text=" ", width="45", height="1", font="Helvetica 14", bg='white')
        funmen.place(x=20, y=420)
        resulta = tk.Label(pes1, text=" ", width="45", height="1", font="Helvetica 14", bg='white')
        resulta.place(x=20, y=460)
        lblvol = tk.Label(pes1, image=imgejem, borderwidth=0, highlightthickness=0)
        lblvol.place(x=949, y=0)
        messagebox.showinfo("Información", "Los campos fueron limpiados")

    botelim = tk.Button(pes1, text="Limpiar", width="20", height="1", command=eliminar, font="Helvetica 14",
                        foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botelim.place(x=400, y=520)
    # ----------------------FIN PARTE DE AREAS----------------------------------
    pes2 = tkinter.Frame(notebook, background="white")
    btnac = Button(pes2, image=img7, command=ejem)
    btnac.place(x=1190, y=540)
    # -------------------------------------INICIO PARTE DE VOLUMEN-----------------------------------------------------------------------#
    notebook.add(pes2, text='Volumen')
    imgejem2 = PhotoImage(file="data/ejemplo2.png")
    imgejem2 = imgejem2.subsample(2, 2)
    lblvol2 = tk.Label(pes2, image=imgejem2, borderwidth=0, highlightthickness=0)
    lblvol2.place(x=870, y=0)

    # HABILITAR TEXTBOX PARA SEGUNDA FUNCION
    def Habilitar():
        boxFuncion2.config(state=NORMAL)

    def LimpiarCampos():
        boxFuncion1.delete(0, END)
        boxFuncion2.delete(0, END)
        boxLimi1.delete(0, END)
        boxLimi2.delete(0, END)
        boxFuncion1.focus_set()
        boxFuncion2.config(state=DISABLED)
        FuncionMayor = Label(pes2, text="", width="500", height="35", bg='white')
        FuncionMayor.place(x=80, y=450, width=500, height=35)
        FuncionMenor = Label(pes2, text="", width="500", height="35", bg='white')
        FuncionMenor.place(x=80, y=500, width=500, height=35)
        ResultadoVolumen = Label(pes2, text="", width="500", height=35, bg='white')
        ResultadoVolumen.place(x=500, y=475, width="500", height="35")
        messagebox.showinfo("Información", "Los campos fueron limpiados")

    # FUNCION QUE GRAFICA CON LAS EXPRESIONES DADAS EN LOS TEXTBOX'S
    def Grafica():
        Expresion1 = boxFuncion1.get()
        if not Expresion1:
            messagebox.showerror("Error", "Ingrese una función")
        Expresion2 = boxFuncion2.get()
        if not Expresion2:
            Expresion2 = 0
        Limite1 = boxLimi1.get()
        if not Limite1:
            messagebox.showerror("Error", "Ingrese el límite inferior")
        Limite2 = boxLimi2.get()
        if not Limite2:
            messagebox.showerror("Error", "Ingrese el límite superior")
        Graficar(Expresion1, Expresion2, Limite1, Limite2)

    # FUNCION PARA HACER EL PROCESO DEL CALCULO DEL VOLUMEN
    def vol():
        Expresion1 = boxFuncion1.get()
        if not Expresion1:
            messagebox.showerror("Error", "Ingrese una función")
        Expresion2 = boxFuncion2.get()
        if not Expresion2:
            Expresion2 = 0  # EN LA CAJA 2 PARA SEGUNDA FUNCIÓN LLEVAR CERO SI NO DIGITÓ NADA
        Limite1 = boxLimi1.get()
        if not Limite1:
            messagebox.showerror("Error", "Ingrese el límite inferior")
        Limite2 = boxLimi2.get()
        if not Limite2:
            messagebox.showerror("Error", "Ingrese límite superior")
        auxResultado = volumenTotal(Expresion1, Expresion2, Limite1, Limite2)
        Expresion1 = auxResultado[0]
        Expresion2 = auxResultado[1]
        auxilio3 = auxResultado[2]
        FuncionMayor = Label(pes2, text="Función Mayor: " + str(Expresion1), width="500", height="35",
                             font="Helvetica 16", bg='white')  # SALIDAS DE EXPRESIONES MENORES Y MAYORES
        FuncionMayor.place(x=80, y=450, width=500, height=35)
        FuncionMenor = Label(pes2, text="Función Menor: " + str(Expresion2), width="500", height="35",
                             font="Helvetica 16", bg='white')
        FuncionMenor.place(x=80, y=500, width=500, height=35)
        ResultadoVolumen = Label(pes2, text="El volúmen es: (" + str(auxilio3) + ") π U³", width="500", height="35",
                                 font="Helvetica 16", bg='white')
        ResultadoVolumen.place(x=500, y=475, width=500, height=35)

    # ETIQUETAS DE TEXTO
    lblFuncion1 = Label(pes2, text="Ingrese la función en términos de x:", width="35", height="1",
                        font="Helvetica 14", bg='white')  # PRIMERA FUNCIÓN
    lblFuncion1.place(x=200, y=35, width=300, height=25)  # POSICIONAMIENTO

    lblFuncion2 = Label(pes2, text="Ingrese la función en términos de x:", width="35", height="1",
                        font="Helvetica 14", bg='white')
    lblFuncion2.place(x=200, y=140, width=300, height=25)  # POSICIONAMIENTO

    lblLimite1 = Label(pes2, text="Ingrese límite inferior:", width="35", height="1", font="Helvetica 14",
                       bg='white')  # PRIMER LIMITE (INFERIOR)
    lblLimite1.place(x=230, y=210, width=225, height=30)  # POSICIONAMIENTO

    lbllimite2 = Label(pes2, text="Ingrese límite superior:", width="35", height="1", font="Helvetica 14",
                       bg='white')  # SEGUNDO LIMITE (SUPERIOR)
    lbllimite2.place(x=230, y=290, width=225, height=30)  # POSICIONAMIENTO

    # CAJAS DE ENTRADA DE FUNCIONES
    boxFuncion1 = Entry(pes2, width=20, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                        highlightthickness=3)  # CAJA PARA PRIMERA FUNCION
    boxFuncion1.place(x=540, y=35, width=300, height=30)  # POSICIONAMIENTO

    boxFuncion2 = Entry(pes2, state=DISABLED, width=20, font="Helvetica 16", highlightbackground='#007b99',
                        highlightcolor='#f39200', highlightthickness=3)  # CAJA PARA SEGUNDA FUNCION
    boxFuncion2.place(x=540, y=140, width=300, height=30)  # POSICIONAMIENTO

    boxLimi1 = Entry(pes2, width=20, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                     highlightthickness=3)  # CAJA PARA LIMITE INFERIOR
    boxLimi1.place(x=540, y=210, width=145, height=25)  # POSICIONAMIENTO

    boxLimi2 = Entry(pes2, width=20, font="Helvetica 16", highlightbackground='#007b99', highlightcolor='#f39200',
                     highlightthickness=3)  # CAJA PARA LIMITE SUPERIOR
    boxLimi2.place(x=540, y=290, width=145, height=25)  # POSICIONAMIENTO
    # BOTONERA
    buttonCalcular = Button(pes2, text="Calcular", command=vol, width="20", height="1", font="Helvetica 16",
                            foreground="white",
                            bg='#007b99', activebackground='white',
                            activeforeground='#007b99')  # BOTÓN PARA CALCULAR EL VOLUMEN
    buttonCalcular.place(x=300, y=370, width=110, height=45)  # POSICIONAMIENTO

    buttonGrafica = Button(pes2, text="Gráfica", command=Grafica, width="20", height="1", font="Helvetica 16",
                           foreground="white",
                           bg='#007b99', activebackground='white',
                           activeforeground='#007b99')  # Llama a la funcion de la gráfica
    buttonGrafica.place(x=500, y=370, width=110, height=45)

    buttonLimpiar = Button(pes2, text="Limpiar", command=LimpiarCampos, width="20", height="1", font="Helvetica 16",
                           foreground="white",
                           bg='#007b99', activebackground='white', activeforeground='#007b99')
    buttonLimpiar.place(x=700, y=370, width=110, height=45)

    buttonHabilitar = Button(pes2, text="Agregar segunda función", command=Habilitar, font="Helvetica 16",
                             foreground="white",
                             bg='#007b99', activebackground='white', activeforeground='#007b99')
    buttonHabilitar.place(x=540, y=80, width=300, height=45)
    # ----------------------------------------------FIN PARTE VOLUMEN----------------------------------------------------------------------------#
    pes3 = tkinter.Frame(notebook, background="white")
    # -----------------------------INICIO PARTE HELP-------------------------------#
    notebook.add(pes3, text='Help')
    imagenLista = PhotoImage(file="data\entrada.png")
    logo_help = PhotoImage(file="data\logo.png")
    imagenLista = imagenLista.subsample(2, 2)
    labelImagen = Label(pes3, image=imagenLista)
    labelImagen.place(x=70, y=50, width=280, height=445)
    logo_help = logo_help.subsample(2, 2)
    label_logo = Label(pes3, image=logo_help)
    label_logo.place(x=820, y=50, width=228, height=195)

    syslac = PhotoImage(file="data\syslac.png")
    syslac = syslac.subsample(9, 9)
    labelsys = tk.Label(pes3, image=syslac)
    labelsys.place(x=420, y=70)
    cienciab = PhotoImage(file="data\cienciasb.png")
    cienciab = cienciab.subsample(1, 1)
    labelcienci = tk.Label(pes3, image=cienciab)
    labelcienci.place(x=1100, y=50)

    dialogo = """Version: 1.0.1
    Fecha: 5 de Abril del 2022 
    Python: 3.9.5
    OS: Windows 10 x 64 bits"""

    def manual():
        path = "docs\Manual_Usuario_PlyMath.pdf"
        os.system(path)

    def guia():
        path = "docs\Guia_PlyMath.pdf"
        os.system(path)

    # -----------------------------INICIO PARTE VENTANA DESARROLLADORES-------------------------------
    def about(dialogue):
        messagebox.showinfo("PlyMath", dialogue)
        ventana_about = Toplevel()
        ventana_about.iconbitmap('data/logo.ico')
        ventana_about.config(bg="white")
        ventana_about.title("About Us")
        ventana_about.geometry("1300x650+30+50")
        ventana_about.resizable(True, True)

        Label(ventana_about, text="About Us", width="15", height="1", font="Helvetica 14 bold",
              bg="white", fg="orange").place(x=600, y=10)
        contexto = """Plymath es un programa de escritorio creado por estudiantes del semillero SYSLAC que ayuda al fortalecimiento de conocimiento de ciencias basicas. 
Este programa se centra en temas especificos del calculo integral, como definiciones, y aplicaciones de integrales, además de generar graficas para un 
mejor entendimiento de los diferentes conceptos. """
        Label(ventana_about, text=contexto, width="115", height="3", font="Helvetica 12 bold",
              bg="white", fg="#007b99", justify=tk.LEFT).place(x=80, y=40)

        Label(ventana_about, text="Conoce nuestro equipo", width=20, height=1, font="Helvetica 14 bold",
              bg="white", fg="orange").place(x=10, y=115)

        equipo = ["Camilo Garcia Saldarriaga",
                  "Juan Jose Mazo Acevedo",
                  "Bryan Arias Quinchia",
                  "Sneyder Martinez Caicedo",
                  "Ingrid Durley Torres Pardo",
                  "Mauricio López Bonilla"]

        # Camilo
        Label(ventana_about, text=equipo[0], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=20, y=160)
        e1photo = PhotoImage(file="data\Camilo.png", master=ventana_about).subsample(8, 7)
        e1_muestra = Label(ventana_about, image=e1photo)
        e1_muestra.image = e1photo
        e1_muestra.place(x=30, y=190)
        c = """Desarrollador
camilo.garciasa@amigo.edu.co"""
        e1_descripcion = Label(ventana_about, text=c, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e1_descripcion.place(x=155, y=190)

        # Bryan
        Label(ventana_about, text=equipo[2], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=20, y=370)
        e2photo = PhotoImage(file="data\Brayan.png", master=ventana_about).subsample(8, 7)
        e2_muestra = Label(ventana_about, image=e2photo)
        e2_muestra.image = e2photo
        e2_muestra.place(x=30, y=400)
        b = """Desarrollador
bryan.ariasqu@amigo.edu.co"""
        e2_descripcion = Label(ventana_about, text=b, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e2_descripcion.place(x=150, y=400)

        # Juan Jose
        Label(ventana_about, text=equipo[1], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=475, y=160)
        e3photo = PhotoImage(file="data\Juan.png", master=ventana_about).subsample(8, 7)
        e3_muestra = Label(ventana_about, image=e3photo)
        e3_muestra.image = e3photo
        e3_muestra.place(x=485, y=190)
        j = """Desarrollador
juan.mazoac@amigo.edu.co"""
        e3_descripcion = Label(ventana_about, text=j, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e3_descripcion.place(x=615, y=190)

        # Sneyder
        Label(ventana_about, text=equipo[3], width=30, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=475, y=370)
        e4photo = PhotoImage(file="data\Sneyder.png", master=ventana_about).subsample(7, 6)
        e4_muestra = Label(ventana_about, image=e4photo)
        e4_muestra.image = e4photo
        e4_muestra.place(x=485, y=400)
        s = """Desarrollador
sneyder.martinezca@amigo.edu.co"""
        e4_descripcion = Label(ventana_about, text=s, width=30, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e4_descripcion.place(x=615, y=400)

        # Ingrid
        Label(ventana_about, text=equipo[4], width=25, height=1, font="Helvetica 14", bg="white",
              fg="orange").place(x=920, y=160)
        e5photo = PhotoImage(file="data\ingrid.png", master=ventana_about).subsample(8, 7)
        e5_muestra = Label(ventana_about, image=e5photo)
        e5_muestra.image = e5photo
        e5_muestra.place(x=930, y=190)
        i = """Docente Investigadora &
Directora del proyecto.
ingrid.torrespa@amigo.edu.co"""
        e5_descripcion = Label(ventana_about, text=i, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e5_descripcion.place(x=1055, y=190)

        # Mauricio
        Label(ventana_about, text=equipo[5], width=25, height=1, font="Helvetica 14", bg="white", justify=tk.LEFT,
              fg="orange").place(x=920, y=370)
        e6photo = PhotoImage(file="data\Brayan.png", master=ventana_about).subsample(8, 7)
        e6_muestra = Label(ventana_about, image=e6photo)
        e6_muestra.image = e6photo
        e6_muestra.place(x=930, y=400)
        m = """Jefe del departamento 
de Ciencias Basicas
mauricio.lopezbo@amigo.edu.co"""
        e6_descripcion = Label(ventana_about, text=m, width=25, font="Helvetica 12", bg="white", justify=tk.LEFT,
                               fg="#007b99")
        e6_descripcion.place(x=1055, y=400)

        # David & Juan Jose Docente
        Label(ventana_about, text="Agredecimientos a:", width=20, height=1, font="Helvetica 13 bold",
              bg="white", justify=tk.LEFT, fg="orange").place(x=5, y=550)

            # David
        d = """ David Estrada Jimenez
 por participación en el desarrollo del proyecto."""
        Label(ventana_about, text=d, width=40, height=2, font="Helvetica 12",
              bg="white", justify=tk.LEFT, fg="#007b99").place(x=40, y=575)
            # Juan Jose Docente
        jjd = """Juan Jose Hoyos Eusse
 por ser el docente promotor del proyecto."""
        Label(ventana_about, text=jjd, width=35, height=2, font="Helvetica 12",
              bg="white", justify=tk.LEFT, fg="#007b99").place(x=430, y=575)

    # -----------------------------FIN PARTE VENTANA DESARROLLADORES-------------------------------

    lblManual = Label(pes3, text="Manual de Usuario", width="20", height="1", font="Helvetica 20", bg='white')
    lblManual.place(x=400, y=300)
    lblGuia = Label(pes3, text="Guia Pedagógica", width="20", height="1", font="Helvetica 20", bg='white')
    lblGuia.place(x=400, y=400)
    btnAquiManual = Button(pes3, text="Aquí", width="18", height="0", font="Helvetica 16", foreground="white",
                           bg='#007b99', activebackground='white', activeforeground='#007b99', command=manual)
    btnAquiManual.place(x=800, y=300)
    btnAquiGuia = Button(pes3, text="Aquí", width="18", height="0", font="Helvetica 16", foreground="white",
                         bg='#007b99', activebackground='white', activeforeground='#007b99', command=guia)
    btnAquiGuia.place(x=800, y=400)

    btnAbout = Button(pes3, text="About", width="18", height="0", font="Helvetica 16", foreground="white",
                      bg='#f39200', activebackground='white', activeforeground='#007b99',
                      command=lambda: about(dialogo))
    btnAbout.place(x=800, y=500)
    # ---------------------FIN PARTE HELP------------------------------#
    w, h = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    ventana.geometry("%dx%d+0+0" % (w, h))
    ventana.mainloop()


if __name__ == '__main__':
    main()
