import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    f(x) = 3 sin(0.5x) - 0.5x + 2
# -------------------------------------------------------
def f(x: float) -> float:
    return 3 * math.sin(0.5 * x) - 0.5 * x + 2


# -------------------------------------------------------
# 2. Método de la secante
# -------------------------------------------------------
def secante(f, x0, x1, tol=5e-5, max_it=20):
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

    # Iteración 0 y 1 (como en tu tabla)
    tabla.append((0, x_prev, f_prev))
    tabla.append((1, x,      f_cur))

    for k in range(2, max_it + 1):
        # Fórmula de la secante
        x_new = x - f_cur * (x_prev - x) / (f_prev - f_cur)
        f_new = f(x_new)

        tabla.append((k, x_new, f_new))

        if abs(f_new) <= tol:
            break

        x_prev, f_prev = x, f_cur
        x,      f_cur  = x_new, f_new

    return tabla


# -------------------------------------------------------
# 3. Ejecutar la secante con x0=5, x1=6
# -------------------------------------------------------
tabla = secante(f, x0=5.0, x1=6.0, tol=5e-5)

print("=== Método de la secante para 3 sin(0.5x) - 0.5x + 2 = 0 ===")
print(" k        x_i               f(x_i)")
for k, xi, fxi in tabla:
    print(f"{k:2d}  {xi:14.9f}   {fxi: .9e}")

# Última fila = raíz aproximada
root = tabla[-1][1]
print("\nRaíz aproximada:")
print(f"x ≈ {root:.9f},   f(x) = {f(root):.9e}")


# -------------------------------------------------------
# 4. Gráfica como tu Excel
#    - puntos x = 0,1,2,3,4,5
#    - curva de f(x)
#    - raíz en rojo
# -------------------------------------------------------
x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función con los mismos puntos que la tabla
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz encontrada (x ≈ 5.7064)
plt.scatter([root], [f(root)], s=60, color="red", label="Raíz (secante)")

plt.xlim(0, 6.5)      # que se vea todo hasta un poco más de la raíz
# Deja que matplotlib ajuste el eje Y (sale parecido al Excel)

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
