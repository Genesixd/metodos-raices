import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    f(x) = cos^2(x) - 0.5 * x * e^(0.3x) + 5
# -------------------------------------------------------
def f(x: float) -> float:
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5


# -------------------------------------------------------
# 2. Método de la secante
# -------------------------------------------------------
def secante(f, x0, x1, tol=5e-5, max_it=50):
    """
    f      : función
    x0,x1  : puntos iniciales
    tol    : tolerancia sobre |f(x_i)|
    max_it : máximo de iteraciones
    """
    tabla = []

    x_prev = x0
    x      = x1
    f_prev = f(x_prev)
    f_curr = f(x)

    # Iteraciones 0 y 1, igual que en tu Excel
    tabla.append((0, x_prev, f_prev))
    tabla.append((1, x,      f_curr))

    k = 1
    while k < max_it and abs(f_curr) > tol:
        # fórmula de la secante
        x_next = x - f_curr * (x_prev - x) / (f_prev - f_curr)

        x_prev, f_prev = x, f_curr
        x,      f_curr = x_next, f(x_next)

        k += 1
        tabla.append((k, x, f_curr))

    return tabla


# -------------------------------------------------------
# 3. Ejecutar la secante para el intervalo [3, 4]
# -------------------------------------------------------
tol = 5e-5
tabla = secante(f, 3.0, 4.0, tol=tol)

root = tabla[-1][1]

print("=== Método de la Secante para cos^2(x) - 0.5 x e^(0.3x) + 5 = 0 ===\n")
print(" k        x_i               f(x_i)")
for k, xi, fxi in tabla:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}")

print("\nRaíz positiva aproximada:")
print(f"x ≈ {root:.9f},   f(x) = {f(root):.9e}")


# -------------------------------------------------------
# 4. Gráfica como en tu Excel
#    - x = 0,1,2,3,4,5,6
#    - curva de f(x)
#    - raíz marcada
# -------------------------------------------------------
x_vals = list(range(0, 7))      # 0,1,2,3,4,5,6
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x (y = 0)
plt.axhline(0, color="black")

# Marcar la raíz encontrada
plt.scatter([root], [f(root)], s=60, color="green", label="Raíz (secante)")

plt.title("Gráfica de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 6)
plt.grid(True)
plt.legend()

plt.show()
