from matplotlib.pyplot import legend
from sympy import symbols
from sympy import integrate
from sympy import *
from tkinter import messagebox

def ecuacionI(fx): #Lee la funcion

    if(fx == ""):
        messagebox.showerror("Error", "Ingrese una integral por favor.")

    dx = symbols('x') #Diferencial
    fx = sympify(fx)

    integral = integrate(fx, dx) #Integra la funcion y lo toma
    integral = str(integral)
    c = " + C"
    sol = str(integral + c)

    return sol
    
def graficaIS(fx, sol, resp): #Menu Despegable
    if(fx == ""):
        messagebox.showerror("Error", "Ingrese una integral por favor.")
    dx = symbols('x') #Diferencial
    fx = sympify(fx)

    del sol
    antIntegral = integrate(fx, dx)
    sol = antIntegral

    if(resp == "Si."):
        s = plot(sol, legend = True, show = False)
        s.title = ("GRÁFICA DE INTEGRAL INDEFINIDA")
        s.xlabel = ('$Eje X$')
        s[0].line_color = 'orange'
        s.show()
    
    elif(resp == "Si, mostrando la gráfica de la función."):
        s = plot(fx, sol, legend = True, show = False)
        s.title = ("GRÁFICA DE INTEGRAL INDEFINIDA & SU FUNCIÓN")
        s[0].line_color = '#007b99'
        s[1].line_color = 'orange'
        s.show()
        
    else:
        messagebox.showerror("Error", "Seleccione una opción por favor.")