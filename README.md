# ej4_io

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/ej4_io)
https://github.com/lauralardies/ej4_io

## Enunciado

La industria de juguetes “Galaxia” produce dos tipos de juguetes:
- Space Ray
- Zapper

Los recursos están limitados a:
- 1200 kg de plástico por semana
- 40 horas de producción semanal

Los requerimientos de Marketing son:
- La producción total no puede exceder de 800 docenas.
- El número de docenas de Space Rays no puede exceder al número de docenas de Zappers por más de 450.
  
Los requerimientos Tecnológicos son:
- Space Rays requiere 2 kg de plástico y 3 minutos de producción por docena.
- Zappers requiere 1 kg de plástico y 4 minutos de producción por docena.

El plan de producción actual se establece mediante los siguientes criterios:
- Fabricar la mayor cantidad del producto que deje más beneficios, el cual corresponde a Space Ray (8 € de utilidad por docena).
- Usar la menor cantidad de recursos para producir Zappers, porque estos dejan una menor utilidad (5 € de utilidad por docena).
  
El plan de producción actual es, por tanto:
- Space Rays = 550 docenas
- Zappers = 100 docenas
Obteniéndose una utilidad Z de 4.900 € por semana.

Las variables de decisión son:
- x1 = Producción de Space Rays (en docenas por semana)
- x2 = Producción de Zappers (en docenas por semana)
- 
Se pide:

a) Emplear el método gráfico para visualizar las restricciones. Calcular Z, x1 y x2 para elplan de producción actual. (3 puntos)

b) ¿Se puede hacer mejor? ¿Cómo? (4 puntos)

c) Calcular Z, x1 y x2 para el mejor plan de producción sin Zapper (1 punto)

d) Calcular Z, x1 y x2 para el mejor plan de producción sin Space Ray (1 punto)

e) ¿x1 = 100; x2 = 150 es una solución factible? ¿Por qué? (0,5 puntos)

f) ¿x1 = 500; x2 = 150 es una solución factible? ¿Por qué? (0,5 puntos)

## Archivos
Todos los archivos de esta tarea se encuentran dentro de una carpeta llamada `Ejercicio 4`. Dentro de ella te encuentras lo siguiente:

- Otra carpeta llamada `Modelos` donde hay dos archivos de Python: `modelo.py`, `modelo_mejorado.py`. En estos archivos te vas a encontrar código que permite graficar las restricciones del problema y su solución.
- Un documento LaTeX llamado `Space_Ray_y_Zapper.pdf` en el cual encuentras la resolución del problema enunciado previamente.

## Código
### Código `modelo.py`
```
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
```
### Código `modelo_mejorado.py`
```
import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "x-450" # >=
f2 = "800-x" # <=
f3 = "1200-2*x" # <=
f4 = "(2400-3*x)/4" # <=

z = "(5040-8*x)/5" # max (modelo mejorado), Z = 5040

x = symbols('x')

plot(f1, f2, f3, f4, z, (x, 0, 1200))
```
