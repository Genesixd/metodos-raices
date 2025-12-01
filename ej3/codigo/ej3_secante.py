import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    Ecuación: x^3 - x^2 e^{-0.5x} - 3x = -1
#    → f(x) = x^3 - x^2 e^{-0.5x} - 3x + 1
# -------------------------------------------------------
def f(x: float) -> float:
    return x**3 - x**2 * math.exp(-0.5 * x) - 3 * x + 1


# -------------------------------------------------------
# 2. Método de la secante
# -------------------------------------------------------
def secante(f, x0, x1, tol=5e-5, max_it=50):
    """
    f      : función
    x0,x1  : dos aproximaciones iniciales
    tol    : tolerancia sobre |f(x_i)|
    max_it : máximo de iteraciones
    """
    tabla = []

    x_prev = x0
    x      = x1
    f_prev = f(x_prev)
    f_cur  = f(x)

    # Iteraciones 0 y 1 (como en tu Excel)
    tabla.append((0, x_prev, f_prev))
    tabla.append((1, x,      f_cur))

    for k in range(2, max_it + 1):
        # fórmula de la secante
        x_new = x - f_cur * (x_prev - x) / (f_prev - f_cur)
        f_new = f(x_new)

        tabla.append((k, x_new, f_new))

        if abs(f_new) <= tol:
            break

        x_prev, f_prev = x, f_cur
        x,      f_cur  = x_new, f_new

    return tabla


# -------------------------------------------------------
# 3. Obtener las tres raíces (mismos intervalos que en Excel)
#    Raíz 1:  [-1.5, -1]
#    Raíz 2:  [0, 0.5]
#    Raíz 3:  [1.5, 2]
# -------------------------------------------------------
tol = 5e-5

tab1 = secante(f, -1.5, -1.0, tol=tol)
tab2 = secante(f,  0.0,  0.5, tol=tol)
tab3 = secante(f,  1.5,  2.0, tol=tol)

root1 = tab1[-1][1]
root2 = tab2[-1][1]
root3 = tab3[-1][1]

print("=== Método de la secante para x^3 - x^2 e^{-0.5x} - 3x = -1 ===\n")

print("Raíz 1 (intervalo -1.5 a -1)")
print(" k        x_i               f(x_i)")
for k, xi, fxi in tab1:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}")
print(f"Raíz 1 ≈ {root1:.9f}, f(x) = {f(root1):.9e}\n")

print("Raíz 2 (intervalo 0 a 0.5)")
print(" k        x_i               f(x_i)")
for k, xi, fxi in tab2:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}")
print(f"Raíz 2 ≈ {root2:.9f}, f(x) = {f(root2):.9e}\n")

print("Raíz 3 (intervalo 1.5 a 2)")
print(" k        x_i               f(x_i)")
for k, xi, fxi in tab3:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}")
print(f"Raíz 3 ≈ {root3:.9f}, f(x) = {f(root3):.9e}\n")


# -------------------------------------------------------
# 4. Gráfica como en el Excel
#    - x de -2 a 3 cada 0.5
#    - curva de f(x)
#    - 3 raíces marcadas
# -------------------------------------------------------
x_vals = [-2 + 0.5 * i for i in range(11)]  # -2, -1.5, ..., 3
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíces encontradas
plt.scatter([root1], [f(root1)], s=60, color="purple", label="Raíz 1")
plt.scatter([root2], [f(root2)], s=60, color="orange", label="Raíz 2")
plt.scatter([root3], [f(root3)], s=60, color="green",  label="Raíz 3")

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
