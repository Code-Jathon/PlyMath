from numpy.lib import math
from sympy import *
import sympy
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from    matplotlib.pyplot import legend
from sympy.core import expr
from sympy.simplify.fu import L
sympy.init_printing()


def puntos_corte(expre_1,expre_2,): 
    x, y, z = symbols('x, y, z')
    expre_1 = sympify(expre_1)
    expre_2 = sympify(expre_2)
    aux_puntos = (expre_1)-(expre_2)      
    solucion = solve(aux_puntos, dict=False)  
    return solucion

def evaluar(exp1, exp2, l1):
    x, y, z = symbols('x, y, z')
    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)     

def area(expre1, expre2, lim1, lim2):
    x, y, z = symbols('x, y, z')
    lim1=sympify(lim1)
    lim2=sympify(lim2)
    expre1=sympify(expre1)
    expre2=sympify(expre2) 

    #ordena las funciones en mayor y menor
    lista=evaluar(expre1, expre2, lim1)

    expre1 = lista[0]
    expre2 = lista[1]

    aux = (expre1) - (expre2)   
    areaf = integrate(aux ,(x, lim1, lim2))
    return expre1, expre2, areaf

#Esto
def graficar(f1, f2, lim1, lim2):

    def grafica(x, y1, y2, lim1, lim2):
        
        y1=np.array(y1, dtype=float)
        y2=np.array(y2, dtype=float)
        x=np.array(x, dtype=float)
    
        '''
        plt.figure('Plymath/Area')
        plt.plot(x,y1)
        plt.plot(x,y2)  
        '''  
        #area sombreada
        plt.figure('Plymath/Area')
        plt.title("Área bajo la curva", color = "#f39200", size = 14)
        plt.ylabel('$Eje Y$')
        plt.xlabel('$Eje X$')
        plt.plot(x, y1, label= "Función 1", linewidth = 2, color = 'orange')
        plt.plot(x, y2, label= "Función 2", linewidth = 2, color = '#007b99')
        plt.fill_between(x, y1,y2, where = [(x > lim1) and (x < lim2) for x in x], color = 'red', alpha = 0.5)      
        legend()
        plt.grid(True)
                        
        plt.show()

    lim1=float(lim1)
    lim2=float(lim2)
    x = np.linspace(lim1-3, lim2+3, 256, endpoint=True)

    xi=[]
    for i in x:
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

    grafica(xi, ff1, ff2,lim1, lim2)
