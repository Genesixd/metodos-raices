import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Definimos la función del problema
#    f(x) = x^3 - e^{0.8x} - 20
# -------------------------------------------------------
def f(x):
    return x**3 - math.exp(0.8 * x) - 20


# -------------------------------------------------------
# 2. Método de la secante
#    x_{i+1} = x_i - f(x_i) (x_{i-1} - x_i) / (f(x_{i-1}) - f(x_i))
# -------------------------------------------------------
def secante(f, x0, x1, tol=5e-5, max_it=20):
    """
    f   : función
    x0  : primer valor inicial
    x1  : segundo valor inicial
    tol : tolerancia en |f(x_i)|
    max_it : máximo de iteraciones
    """
    tabla = []

    # i = 0
    fx0 = f(x0)
    tabla.append((0, x0, fx0))

    # i = 1
    fx1 = f(x1)
    tabla.append((1, x1, fx1))

    x_prev, x = x0, x1
    f_prev, f_cur = fx0, fx1

    for i in range(2, max_it + 1):
        # fórmula de la secante
        if f_cur == f_prev:
            break  # evitar división entre cero

        x_new = x - f_cur * (x_prev - x) / (f_prev - f_cur)
        f_new = f(x_new)
        tabla.append((i, x_new, f_new))

        # criterio de paro: |f(x_i)| <= tol
        if abs(f_new) <= tol:
            break

        x_prev, x = x, x_new
        f_prev, f_cur = f_cur, f_new

    return tabla


# -------------------------------------------------------
# 3. Aplicamos la secante a las dos raíces
#    Raíz 1: intervalo [3, 4]
#    Raíz 2: intervalo [7, 8]
# -------------------------------------------------------
tabla1 = secante(f, 3.0, 4.0)  # raíz cercana a 3
tabla2 = secante(f, 7.0, 8.0)  # raíz cercana a 7.5

# Imprimimos las tablas de iteraciones (como en Excel)
print("=== Raíz 1 (intervalo 3–4) ===")
print(" i        x_i              f(x_i)")
for i, xi, fxi in tabla1:
    print(f"{i:2d}  {xi:14.12f}  {fxi: .6e}")

print("\n=== Raíz 2 (intervalo 7–8) ===")
print(" i        x_i              f(x_i)")
for i, xi, fxi in tabla2:
    print(f"{i:2d}  {xi:14.12f}  {fxi: .6e}")

# Último valor de cada tabla = aproximación de la raíz
root1 = tabla1[-1][1]
root2 = tabla2[-1][1]

print("\nAproximaciones finales:")
print(f"Raíz 1 ≈ {root1:.12f}    f(x) = {f(root1):.6e}")
print(f"Raíz 2 ≈ {root2:.12f}    f(x) = {f(root2):.6e}")

# -------------------------------------------------------
# 4. Gráfica como en Excel
#    - puntos x = 0,1,2,3,4,5,6,7
#    - curva f(x)
#    - puntos de las raíces
# -------------------------------------------------------
# -------------------------------------------------------
# 4. Gráfica como en Excel
# -------------------------------------------------------
x_vals = [0, 1, 2, 3, 4, 5, 6, 7]
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz 1 morada
plt.scatter([root1], [f(root1)], s=60, color="purple", label="Raíz 1")

# Raíz 2 naranja
plt.scatter([root2], [f(root2)], s=60, color="orange", label="Raíz 2")

# Límites de los ejes para que se parezca al Excel
plt.xlim(0, 8)
plt.ylim(-40, 80)

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
