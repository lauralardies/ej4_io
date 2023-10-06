import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "x-450" # >=
f2 = "800-x" # <=
f3 = "1200-2*x" # <=
f4 = "(2400-3*x)/4" # <=

z_a = "(4900-8*x)/5" # max (del enunciado)
z_b = "(5040-8*x)/5" # max (modelo mejorado)

x = symbols('x')

plot(f1, f2, f3, f4, z_a, z_b, (x, 0, 1200))