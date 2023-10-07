import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "x-450" # >=
f2 = "800-x" # <=
f3 = "1200-2*x" # <=
f4 = "(2400-3*x)/4" # <=

z = "(4900-8*x)/5" # max (del enunciado), Z = 4900

x = symbols('x')

plot(f1, f2, f3, f4, z, (x, 0, 1200))