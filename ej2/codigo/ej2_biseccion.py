import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    f(x) = 3 sin(0.5x) - 0.5x + 2
# -------------------------------------------------------
def f(x: float) -> float:
    return 3 * math.sin(0.5 * x) - 0.5 * x + 2


# -------------------------------------------------------
# 2. Método de Bisección
# -------------------------------------------------------
def biseccion(f, a, b, tol=0.005, max_it=50):
    """
    f     : función
    a, b  : extremos iniciales del intervalo
    tol   : tolerancia sobre |f(m)|
    max_it: máximo de iteraciones
    """
    tabla = []

    fa = f(a)
    fb = f(b)

    for k in range(max_it):
        m = (a + b) / 2
        fm = f(m)

        tabla.append((k, a, b, m, fa, fb, fm))

        # criterio de paro como en el Excel: |f(m)| <= tol
        if abs(fm) <= tol:
            break

        # actualización del intervalo
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return tabla


# -------------------------------------------------------
# 3. Ejecutar bisección en el intervalo [5, 6]
# -------------------------------------------------------
tabla = biseccion(f, a=5.0, b=6.0, tol=0.005)

print("=== Método de Bisección para 3 sin(0.5x) - 0.5x + 2 = 0 ===")
print(" k        a           b           m           f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tabla:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")

# último m de la tabla = raíz aproximada
root = tabla[-1][3]

print("\nRaíz aproximada (tol = 0.005):")
print(f"x ≈ {root:.9f},   f(x) = {f(root):.6f}")


# -------------------------------------------------------
# 4. Gráfica como en el Excel
#    - puntos x = 0..8 de la tabla de exploración
#    - curva de f(x)
#    - raíz marcada
# -------------------------------------------------------
x_vals = list(range(0, 9))          # 0,1,2,3,4,5,6,7,8
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz encontrada
plt.scatter([root], [f(root)], s=60, color="red", label="Raíz (bisección)")

# Límites parecidos al Excel
plt.xlim(0, 8)
plt.ylim(-5, 4)

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
