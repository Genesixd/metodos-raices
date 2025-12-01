import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función y derivada
#    f(x) = x^3 - e^{0.8x} - 20
#    f'(x) = 3x^2 - 0.8 e^{0.8x}
# -------------------------------------------------------
def f(x: float) -> float:
    return x**3 - math.exp(0.8 * x) - 20


def fp(x: float) -> float:
    return 3 * x**2 - 0.8 * math.exp(0.8 * x)


# -------------------------------------------------------
# 2. Método de Newton–Raphson
# -------------------------------------------------------
def newton_raphson(f, fp, x0, tol=5e-5, max_it=20):
    """
    f    : función
    fp   : derivada de f
    x0   : valor inicial
    tol  : tolerancia en |f(x_i)|
    max_it : máximo de iteraciones
    """
    tabla = []
    x = x0

    for k in range(max_it + 1):
        fx = f(x)
        fpx = fp(x)
        tabla.append((k, x, fx, fpx))

        if abs(fx) <= tol:
            break

        x = x - fx / fpx

    return tabla


# -------------------------------------------------------
# 3. Aplicar Newton a las dos raíces
#    Raíz 1 con x0 = 3
#    Raíz 2 con x0 = 8
# -------------------------------------------------------
tabla1 = newton_raphson(f, fp, x0=3.0, tol=5e-5)
tabla2 = newton_raphson(f, fp, x0=8.0, tol=5e-5)

print("=== Raíz 1 (x0 = 3) - Método de Newton–Raphson ===")
print(" k        x_i              f(x_i)           f'(x_i)")
for k, xi, fxi, fpxi in tabla1:
    print(f"{k:2d}  {xi:14.10f}  {fxi:14.8e}  {fpxi:14.8f}")

print("\n=== Raíz 2 (x0 = 8) - Método de Newton–Raphson ===")
print(" k        x_i              f(x_i)           f'(x_i)")
for k, xi, fxi, fpxi in tabla2:
    print(f"{k:2d}  {xi:14.10f}  {fxi:14.8e}  {fpxi:14.8f}")

# Últimos x_i de cada tabla = raíces aproximadas
root1 = tabla1[-1][1]
root2 = tabla2[-1][1]

print("\nAproximaciones finales (tol = 0.00005):")
print(f"Raíz 1 ≈ {root1:.10f}   f(x) = {f(root1):.8e}")
print(f"Raíz 2 ≈ {root2:.10f}   f(x) = {f(root2):.8e}")


# -------------------------------------------------------
# 4. Gráfica igual a tu Excel
#    - puntos x = 0,1,2,3,4,5,6,7,8
#    - curva de f(x)
#    - raíz 1 en rojo, raíz 2 en verde
# -------------------------------------------------------
x_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva con puntos
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz 1 (cerca de 3.208...) en rojo
plt.scatter([root1], [f(root1)], s=60, color="red", label="Raíz 1")

# Raíz 2 (cerca de 7.4898...) en verde
plt.scatter([root2], [f(root2)], s=60, color="green", label="Raíz 2")

# Límites para que se parezca a tu gráfica del Excel
plt.xlim(0, 9)        # eje x de 0 a 9
plt.ylim(-150, 100)   # eje y de -150 a 100

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
