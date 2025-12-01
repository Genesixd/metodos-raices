import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función y derivada
#    f(x) = 3 sin(0.5x) - 0.5x + 2
#    f'(x) = 1.5 cos(0.5x) - 0.5
# -------------------------------------------------------
def f(x: float) -> float:
    return 3 * math.sin(0.5 * x) - 0.5 * x + 2


def fp(x: float) -> float:
    return 1.5 * math.cos(0.5 * x) - 0.5


# -------------------------------------------------------
# 2. Método de Newton–Raphson
# -------------------------------------------------------
def newton_raphson(f, fp, x0, tol=5e-5, max_it=20):
    tabla = []
    x = x0

    for k in range(max_it + 1):
        fx = f(x)
        fpx = fp(x)

        tabla.append((k, x, fx, fpx))

        # criterio: |f(x_i)| <= tol
        if abs(fx) <= tol:
            break

        x = x - fx / fpx

    return tabla


# -------------------------------------------------------
# 3. Ejecutar Newton con x0 = 5
# -------------------------------------------------------
tabla = newton_raphson(f, fp, x0=5.0, tol=5e-5)

print("=== Método de Newton–Raphson para 3 sin(0.5x) - 0.5x + 2 = 0 ===")
print(" k        x_i               f(x_i)           f'(x_i)")
for k, xi, fxi, fpxi in tabla:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}   {fpxi: .9f}")

# Último x_i = raíz aproximada
root = tabla[-1][1]
print("\nRaíz aproximada (tol = 0.00005):")
print(f"x ≈ {root:.9f},   f(x) = {f(root):.9e}")


# -------------------------------------------------------
# 4. Gráfica igual a la de Excel
#    - puntos x = 0..8
#    - curva de f(x)
#    - raíz marcada en rojo
# -------------------------------------------------------
x_vals = list(range(0, 9))           # 0,1,2,3,4,5,6,7,8
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz encontrada
plt.scatter([root], [f(root)], s=60, color="red", label="Raíz (Newton)")

# Límites parecidos a tu gráfico de Excel
plt.xlim(0, 8)
plt.ylim(-5, 4)

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
