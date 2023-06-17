from sympy.utilities.lambdify import lambdify
from sympy import *
import sympy as smp
from scipy.integrate import *
from scipy import integrate
import numpy as np
from numpy import cos, tan, sin, arccos, arcsin, arctan, sqrt, log, exp
import math
import warnings
warnings.filterwarnings("ignore")

def integrate_f_trigon():
    def g(x):
        func = eval(abc)
        return func
    print()
    print("Instrucciones, en caso de usar raices o funciones trigonometricas")
    print("usar un parentesis para introducir el argumento de la función")
    print()
    print("inserte su función: ")
    aba = input()
    abc = aba.replace("^","**")
    abc = aba.replace("√","sqrt")
    print("Inserte el limite inferior: ")
    low = float(input())
    print("Inserte el limite superior: ")
    upp = float(input())
    try:
        ab,bc = quad(g,low,upp)
        int_statement = "La integral de "+aba+" de "+str(low)+" a "+str(upp)+" es: "+str(ab)
        return(int_statement)
    except:
        print("Esta integral no puede resolverse")
print(integrate_f_trigon())
