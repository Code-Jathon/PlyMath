from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
from integralesIndefinidas import *
from integralesDefinidas import *
from areas import *

def main():
    ventana= Tk()
    ventana.iconbitmap('data/logo.ico')
    ventana.config(bg="white",bd=0)
    ventana.title('PlyMath')
    label= tkinter.Label(ventana, text="PlyMath", bg="white", fg="#007b99", )
    label.configure(font=("Bahnschrift Light", 19,tkFont.BOLD))
    label.pack()
    style = ttk.Style()    
    settings = {"TNotebook.Tab": {"configure": {"padding": [120, 5],
                                            "background": "#f39200",
                                            "font":"Helvetica, 11 "
                                            }}}  
    style.theme_create("mi_estilo", parent="alt", settings=settings)
    style.theme_use("mi_estilo")
    
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand='yes',padx=7, pady=20)
    notebook.pressed_index = None
    pes0 = tkinter.Frame(notebook,background="white")
    
#--------Desarrollo de la pestaña integrales-----
    #-----------Parte Indefinidas-----------------
        #Ecuacion
    ecuaI = tk.Label(pes0, text ="Digite el problema:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    caja1 = Entry(pes0, width = 40, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Resultado    
    resulI = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Helvetica 14"),  bg = 'white')
    muestraI = tk.Label(pes0, text = "" , width = "35", height = "1", font = ("Helvetica 14 italic bold"), foreground = "#007b99", background = "#f39200")
        #Grafica
    graficaI = tk.Label(pes0, text ="¿Desea conocer la grafica de la integral?", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
        #Menu Despegable
    menuI = ttk.Combobox(pes0, width = "35", font = ("Helvetica 18"), state = "readonly", foreground = "#007b99",
                         values = ["Si.", 
                                   "Si, mostrando la grafica de la integral."])
    menuI.current()#Valor por defectos
        #Botones de verificacion
    def obtenerI():
        funcion  = caja1.get()
        respuesta = menuI.get()
        menuI.select_clear()
        solucion = muestraI.cget("text")
        prueba2 = graficaIS(funcion, solucion, respuesta)

    def limpiarI():
        caja1.delete(0, END)
        muestraI.config(text = "")
        menuI.set("")
        messagebox.showinfo("Informacion", "La ecuacion y ha sido borrada")
        caja1.focus_set()
        
    def save():
        prueba = caja1.get()
        solucion = ecuacionI(prueba)
        muestraI.config(text = solucion)
        
    botonGraf = Button(pes0, text = "Grafica", width = "20", font = ("Helvetica 14 bold"),
                    command = obtenerI, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton3 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Helvetica 14 bold"), 
                    command = limpiarI, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton4 = Button(pes0, text = "Ingresar", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = save, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    #-----------Parte Definidas-----------------
        #Limites
    limInfe = tk.Label(pes0, text="Ingrese limite inferior:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    cajaInfe = Entry(pes0, width = 20, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
    limSupe = tk.Label(pes0, text="Ingrese limite superior:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    cajaSupe = Entry(pes0, width = 20, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Ecuacion
    ecuaD = tk.Label(pes0, text ="Digite la ecuacion:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    caja2 = Entry(pes0, width = 40, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Pregunta
    question = '''      ¿Desea conocer el resultado
    en fraccionario o en decimales ?'''
    pregu = tk.Label(pes0, text = question, width = "35", height = "2", font = ("Helvetica 14"), justify = tk.LEFT, bg = 'white')
        #Menu Despegable
    menuD =  ttk.Combobox(pes0, width = "35", font = ("Helvetica 14"), state = "readonly", foreground = "#007b99")
    menuD['values'] = (  "Fraccionario.",
                         "Decimales.")
    menuD.current()
        #Solucion
    resulD = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Helvetica 14"),  bg="white")
    muestraD = tk.Label(pes0, text = "", width = "35", height = "1", font = ("Helvetica 14 italic bold"), bg = "white", foreground = "#007b99", 
                        background = "#f39200")

        #Botones de verificacion
    def limpiarD():
        cajaInfe.delete(0, END)
        cajaSupe.delete(0, END)
        caja2.delete(0, END)
        menuD.set("")
        muestraD.config(text = "")
        messagebox.showinfo("Informacion", "Los valores ingresados han sido borrados")
        cajaInfe.focus_set()

    def obtenerD():
        LimI = cajaInfe.get()
        LimS = cajaSupe.get()
        ec   = caja2.get()
        res  = menuD.get()
        menuD.select_clear()
        solucionI = ecuacionD(LimI, LimS, ec, res)
        muestraD.config(text = solucionI)

    boton5 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Helvetica 14 bold"), 
                    command = limpiarD, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton6 = Button(pes0, text = "Resultado", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = obtenerD, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton7 = Button(pes0, text = "Grafica", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = lambda: graficaES(caja2.get()), foreground = "white", bg = '#007b99', activebackground = 'white', 
                    activeforeground = '#007b99')

    #ShowWidgets
    def indefi():
        caja1.focus_set()
        ocultarD()
        ecuaI.grid(row = 2, column = 0, pady = 5)
        caja1.place(x = 630, y = 120)
        resulI.grid(row = 3, column = 0, pady = 25)
        muestraI.place(x = 630, y = 180)
        graficaI.grid(row = 4, column = 0, pady = 10)
        menuI.place(x = 630, y = 245)
        boton3.grid(row = 6, column= 0, pady = 30)
        boton4.grid(row = 6, column= 1)
        botonGraf.place(x = 460, y = 310)

    def defi():
        cajaInfe.focus_set()
        ocutarI()
        limInfe.grid(row = 2, column = 0)
        cajaInfe.place(x = 630 , y = 115)
        limSupe.grid(row = 3, column= 0, pady = 25)
        cajaSupe.place(x = 630 , y = 170)
        ecuaD.grid(row = 4, column = 0, pady = 4)
        caja2.place(x = 630 , y = 225)
        pregu.grid(row = 5, column = 0, pady = 25)
        menuD.place(x = 630 , y = 310)
        resulD.grid(row = 7, column = 0)
        muestraD.place( x = 630, y = 360)    
        boton5.grid(row = 8, column = 0, pady = 25)
        boton6.grid(row = 8, column = 1)
        boton7.place(x = 461, y = 411)

    #OcultarWidgets
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
        
    #Botones_I&D
    boton1 = Button(pes0, text = "INDEFINIDAS", width = "78", height = "3", font = ("Calibri 10 bold italic"),
                    command = indefi, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton2 = Button(pes0, text = "DEFINIDAS", width = "80", height = "3", font = ("Calibri 10 bold italic"),
                    command = defi, foreground = "white", bg = '#f39200', activebackground = 'white', activeforeground = '#f39200')
    #AGG botenes en pantalla
    boton1.grid(row = 1, column=0, padx = 16, pady = 30)
    boton2.grid(row = 1, column=1, padx = 8, pady = 30)


    pes1 = tkinter.Frame(notebook,background="white")
#--------Desarrollo de la pestaña Areas-----

    pes2 = tkinter.Frame(notebook,background="white")
#--------Desarrollo de la pestaña Volumenes-----

    pes3 = tkinter.Frame(notebook,background="white")
    notebook.add(pes0, text='Integrales')   
    #Parte Area
    notebook.add(pes1, text='Área')
    fun1=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width="35", height="1", font=("Helvetica 14"), bg='white')
    fun1.grid(row=2, column=0, pady=4)
    caj1 = Entry(pes1, width= 45, font = ("Helvetica 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj1.grid(row=2, column=1, pady=4)
    #accion boton
    def sefu():
        fun2.grid(row=4, column=0)
        caj2.grid(row=4,column=1)

    bot2fun = tk.Button(pes1, text="Añadir segunda funcion", width = "20", height = "1", command=sefu 
    , font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    bot2fun.grid(row=3,column=0, pady= 6)
    fun2=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    caj2 = Entry(pes1, width= 45, font= ("Calibri 16"), highlightbackground='#007b99'
    , highlightcolor='#f39200', highlightthickness=3)
    #accion boton
    def pun_cor():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        aux1 = puntos_corte(e1, e2)
        resultPc = tk.Label(pes1, text="Los puntos de corte son: " + str(aux1), width = "35", height = "1"
        , font = ("Helvetica 14"), bg='white')
        resultPc.grid(row=6,column=0)

    botpun = tk.Button(pes1, text="Calcular puntos de corte", width = "20", height = "1", command = pun_cor
    , font = ("Helvetica 14") ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botpun.grid(row=5, column=0, pady= 8)
    liminfe = tk.Label(pes1, text="Ingrese limite inferior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    liminfe.grid(row=7, column=0)
    caj3 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj3.grid(row=7, column=1, pady= 9)
    limsupe = tk.Label(pes1, text="Ingrese limite superior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    limsupe.grid(row=10, column=0)
    caj4 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj4.grid(row=10, column=1, pady= 11)
    #accion boton
    def are():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        aux2 = area(e1, e2, l1, l2)
        e1 = aux2[0]
        e2 = aux2[1]
        aux3 = aux2[2]
        funmay = tk.Label(pes1, text="La funcion mayor es: " + str(e1), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmay.grid(row=16,column=0)
        funmen = tk.Label(pes1, text="La funcion menor es: " + str(e2), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmen.grid(row=18,column=0)      
        resulta = tk.Label(pes1, text="El area de la funcion es: " + str(aux3) + " U²", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resulta.grid(row=20,column=0)

    botresult = tk.Button(pes1, text="Calcular", width = "20", height = "1",command = are, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botresult.grid(row=14,column=0, pady=12)  
    #accion boton
    def gra():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        graficar(e1, e2, l1, l2)

    botgraf = tk.Button(pes1, text="Graficar", width = "20", height = "1",command = gra, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botgraf.grid(row=24,column=0, pady=16)  
    #accion boton
    def eliminar():
        caj1.delete(0, END)
        caj2.delete(0 , END)
        caj3.delete(0 , END)
        caj4.delete(0 , END)
        caj1.focus_set()
        resultPc = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resultPc.grid(row=6,column=0)
        funmay = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmay.grid(row=16,column=0)
        funmen = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmen.grid(row=18,column=0)      
        resulta = tk.Label(pes1, text=" " , width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resulta.grid(row=20,column=0)

    botelim = tk.Button(pes1, text="Limpiar", width = "20", height = "1", command = eliminar, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botelim.grid(row=24,column=1, pady=20)  
    
    notebook.add(pes2, text='Volumen')
    notebook.add(pes3, text='About Us')

    ventana.geometry("1200x650")
    ventana.resizable(1,1)
    ventana.mainloop()

if __name__=='__main__':
    main()