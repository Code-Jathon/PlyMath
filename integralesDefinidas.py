from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
from numpy import *
from sympy import *


def ecuacionD(i, s, fx, resp):
    if i == "":
        messagebox.showerror("Error", "Ingrese el límite inferior por favor.")
    elif s == "":
        messagebox.showerror("Error", "Ingrese el límite superior por favor.")
    elif fx == "":
        messagebox.showerror("Error", "Ingrese una ecuación por favor.")

    dx = symbols('x')  # Diferencial
    fx = sympify(fx)

    if resp == "Fraccionarios.":
        inte = integrate(fx, (dx, i, s))  # Fraccionario
    elif resp == "Decimales.":
        inte = integrate(fx, (dx, i, s)).evalf(3)  # Decimal
    else:
        messagebox.showerror("Error", "Seleccione una opción por favor.")

    return inte


def graficaES(fx, inf, sup):
    if inf == "":
        messagebox.showerror("Error", "Ingrese el límite inferior")
    if sup == "":
        messagebox.showerror("Error", "Ingrese el límite superior")
    if fx == "":
        messagebox.showerror("Error", "Ingrese una ecuación por favor.")

    def gES(x, gx, lI, lS):
        gx = np.array(gx, dtype=float)
        x = np.array(x, dtype=float)

        plt.figure('Plymath/Integrales')
        plt.title("Gráfica integral definida", color="#f39200", size=14)
        plt.ylabel('$Eje Y$')
        plt.xlabel('$Eje X$')
        plt.plot(x, gx, label="f(x)", linewidth=2, color='orange')
        legend()

        # Area sombreada
        plt.fill_between(x, gx, where=[(x >= lI) and (x <= lS) for x in x], color="#007b99", alpha=0.7)
        plt.grid(True)
        plt.axhline(0, color="#007b99", linestyle='solid', lw=2)
        plt.show()

    inf = float(inf)
    sup = float(sup)

    x = np.linspace(inf - 3, sup + 3, 256, endpoint=True)
    xi = []

    for i in x:
        xi.append(i)

    ffx = []

    for i in xi:
        x = symbols('x')
        fx = sympify(fx)
        ec = fx.evalf(subs={x: i})
        ffx.append(ec)

    gES(xi, ffx, inf, sup)
