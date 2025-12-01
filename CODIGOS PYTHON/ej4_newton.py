import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función y derivada
#    f(x) = cos^2(x) - 0.5 * x * e^(0.3x) + 5
#    f'(x) = -sin(2x) - e^(0.3x) * (0.5 + 0.15x)
# -------------------------------------------------------
def f(x: float) -> float:
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5

def fp(x: float) -> float:
    return -math.sin(2 * x) - math.exp(0.3 * x) * (0.5 + 0.15 * x)


# -------------------------------------------------------
# 2. Método de Newton–Raphson
# -------------------------------------------------------
def newton_raphson(f, fp, x0, tol=5e-5, max_it=20):
    """
    f     : función
    fp    : derivada
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

        # mismo criterio que en Excel: |f(x_i)| <= tol
        if abs(fx) <= tol:
            break

        x = x - fx / fpx

    return tabla


# -------------------------------------------------------
# 3. Ejecutar Newton para x0 = 3.5
# -------------------------------------------------------
tol = 5e-5
tabla = newton_raphson(f, fp, x0=3.5, tol=tol)

root = tabla[-1][1]

print("=== Método de Newton–Raphson para cos^2(x) - 0.5 x e^(0.3x) + 5 = 0 ===\n")
print(" k        x_i               f(x_i)             f'(x_i)")
for k, xi, fxi, fpxi in tabla:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}   {fpxi: .9f}")

print("\nRaíz positiva aproximada (Newton):")
print(f"x ≈ {root:.9f}")
print(f"f(x) ≈ {f(root):.9e}")


# -------------------------------------------------------
# 4. Gráfica como en el Excel (x = 0..6)
# -------------------------------------------------------
x_vals = list(range(0, 7))    # 0,1,2,3,4,5,6
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x (y = 0)
plt.axhline(0, color="black")

# Punto de la raíz
plt.scatter([root], [f(root)], s=60, color="purple", label="Raíz (Newton)")

plt.title("Gráfica de f(x) con raíz (Newton–Raphson)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 6)
plt.grid(True)
plt.legend()

plt.show()
