import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función y derivada
#    Ecuación: x^3 - x^2 e^{-0.5x} - 3x = -1
#    → f(x) = x^3 - x^2 e^{-0.5x} - 3x + 1
#    → f'(x) = 3x^2 + (0.5x^2 - 2x) e^{-0.5x} - 3
# -------------------------------------------------------
def f(x: float) -> float:
    return x**3 - x**2 * math.exp(-0.5 * x) - 3 * x + 1


def fp(x: float) -> float:
    return 3 * x**2 + (0.5 * x**2 - 2 * x) * math.exp(-0.5 * x) - 3


# -------------------------------------------------------
# 2. Método de Newton–Raphson
# -------------------------------------------------------
def newton_raphson(f, fp, x0, tol=5e-5, max_it=20):
    """
    f     : función
    fp    : derivada de f
    x0    : aproximación inicial
    tol   : tolerancia sobre |f(x_i)|
    max_it: máximo de iteraciones
    """
    tabla = []
    x = x0

    for k in range(max_it + 1):
        fx = f(x)
        fpx = fp(x)

        tabla.append((k, x, fx, fpx))

        # criterio de paro como en tu Excel: |f(x_i)| <= tol
        if abs(fx) <= tol:
            break

        x = x - fx / fpx

    return tabla


# -------------------------------------------------------
# 3. Ejecutar Newton para las 3 raíces
#    (mismas x0 que en tu Excel: -1.2, 0.3, 1.8)
# -------------------------------------------------------
tol = 5e-5

tab1 = newton_raphson(f, fp, x0=-1.2, tol=tol)
tab2 = newton_raphson(f, fp, x0= 0.3, tol=tol)
tab3 = newton_raphson(f, fp, x0= 1.8, tol=tol)

root1 = tab1[-1][1]
root2 = tab2[-1][1]
root3 = tab3[-1][1]

print("=== Método de Newton–Raphson para x^3 - x^2 e^{-0.5x} - 3x = -1 ===\n")

print("Raíz 1  (x0 ≈ -1.2)")
print(" k        x_i               f(x_i)             f'(x_i)")
for k, xi, fxi, fpxi in tab1:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}   {fpxi: .9f}")
print(f"→ Raíz 1 ≈ {root1:.9f},   f(x) = {f(root1):.9e}\n")

print("Raíz 2  (x0 ≈ 0.3)")
print(" k        x_i               f(x_i)             f'(x_i)")
for k, xi, fxi, fpxi in tab2:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}   {fpxi: .9f}")
print(f"→ Raíz 2 ≈ {root2:.9f},   f(x) = {f(root2):.9e}\n")

print("Raíz 3  (x0 ≈ 1.8)")
print(" k        x_i               f(x_i)             f'(x_i)")
for k, xi, fxi, fpxi in tab3:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}   {fpxi: .9f}")
print(f"→ Raíz 3 ≈ {root3:.9f},   f(x) = {f(root3):.9e}\n")


# -------------------------------------------------------
# 4. Gráfica como en el Excel
#    - x de -2 a 3 con paso 0.5
#    - curva de f(x)
#    - tres raíces marcadas
# -------------------------------------------------------
x_vals = [-2 + 0.5 * i for i in range(11)]  # -2, -1.5, ..., 3
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x (y = 0)
plt.axhline(0, color="black")

# Marcar las 3 raíces
plt.scatter([root1], [f(root1)], s=60, color="purple", label="Raíz 1 (Newton)")
plt.scatter([root2], [f(root2)], s=60, color="orange", label="Raíz 2 (Newton)")
plt.scatter([root3], [f(root3)], s=60, color="green",  label="Raíz 3 (Newton)")

plt.title("Gráfica de f(x) con raíces (Newton–Raphson)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
