from tkinter import messagebox
import matplotlib.pyplot as plt 
import numpy as np
from sympy import *
from sympy import Integral, integrate
from sympy.core import symbol
from sympy.core.numbers import Exp1
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot
from sympy.testing.runtests import SymPyOutputChecker
from sympy.core import expr
from sympy.simplify.fu import L
import mpl_toolkits.mplot3d.axes3d as axes3d
from numpy.lib.function_base import meshgrid


def evaluar(exp1, exp2,l1):
    x, y, z =symbols('x, y, z')
    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)      

def volumenTotal(expresion1, expresion2, limite1, limite2):
    x, y, z =symbols('x, y, z')
    x=sympify('x')
    y=simplify('y')
    z=simplify('z')
    limite1=sympify(limite1)
    limite2=sympify(limite2)
    expresion1=sympify(expresion1)
    expresion2=sympify(expresion2)

#EVALUA LAS FUNCIONES PARA MAYOR Y MENOR.
    lista=evaluar(expresion1, expresion2, limite1)
    expresion1 = lista[0]
    expresion2 = lista[1]
    res = integrate(((expresion1)**2 - (expresion2)**2), (x, limite1, limite2))
    
    return expresion1, expresion2,res
#FUNCION PARA GRAFICAR
def Graficar(f1, f2, lim1, lim2):   

    lim1=float(lim1)
    lim2=float(lim2)

    def sus(x1, f1, f2):
        xi=[]
        for i in x1:
            xi.append(i)

        ff1=[]
        ff2=[]
            
        for i in xi:
            x, y, z = symbols('x, y, z')
            f1=sympify(f1)
            f2=sympify(f2)
            e1 = f1.evalf(subs={x: i})
            e2 = f2.evalf(subs={x: i})
            ff1.append(e1)
            ff2.append(e2)
        f1=np.array(ff1, dtype=float)
        f2=np.array(ff2, dtype=float)
        return(f1, f2)
            

    fig = plt.figure('Plymath/Volumen')
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    u = np.linspace(lim1, lim2, 60)             
    v = np.linspace(lim1-10, (lim2-10)*np.pi, 60)       
    U, V = np.meshgrid(u, v)

    x = u
    resul = sus(u, f1, f2)

    Y1 = (resul[0])*np.cos(V)        
    Z1 = (resul[0])*np.sin(V)        

    Y2 = (resul[1])*np.cos(V)        
    Z2 = (resul[1])*np.sin(V)        

    ax.plot_surface(x, Y1, Z1, alpha=0.3, color="red", rstride=5, cstride=5)
    ax.plot_surface(x, Y2, Z2, alpha=0.5, color="b", rstride=5, cstride=5)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_title("Sólido de revolución")
    ax.grid()
    plt.show()
