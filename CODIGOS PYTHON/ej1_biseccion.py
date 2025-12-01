import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    f(x) = x^3 - e^{0.8x} - 20
# -------------------------------------------------------
def f(x: float) -> float:
    return x**3 - math.exp(0.8 * x) - 20


# -------------------------------------------------------
# 2. Método de Bisección
# -------------------------------------------------------
def biseccion(f, a, b, tol=0.005, max_it=50):
    """
    f     : función
    a, b  : intervalo inicial con cambio de signo
    tol   : tolerancia en |f(m)|
    max_it: máx. iteraciones
    """
    tabla = []
    fa = f(a)
    fb = f(b)

    for k in range(max_it):
        m = (a + b) / 2
        fm = f(m)
        tabla.append((k, a, b, m, fa, fb, fm))

        # criterio de paro igual que en Excel: |f(m)| <= tol
        if abs(fm) <= tol:
            break

        # actualización del intervalo
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return tabla


# -------------------------------------------------------
# 3. Aplicar bisección a las dos raíces
#    Raíz 1 en [3,4], Raíz 2 en [7,8]
# -------------------------------------------------------
tabla1 = biseccion(f, 3.0, 4.0, tol=0.005)
tabla2 = biseccion(f, 7.0, 8.0, tol=0.005)

# Mostrar las tablas (como en Excel)
print("=== Raíz 1 (intervalo 3–4) - Método de Bisección ===")
print(" k        a         b         m          f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tabla1:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")

print("\n=== Raíz 2 (intervalo 7–8) - Método de Bisección ===")
print(" k        a         b         m          f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tabla2:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")

# Último m de cada tabla = aproximación de la raíz
root1 = tabla1[-1][3]   # m de la última fila raíz 1
root2 = tabla2[-1][3]   # m de la última fila raíz 2

print("\nAproximaciones finales (bisección, tol = 0.005):")
print(f"Raíz 1 ≈ {root1:.9f}   f(x) = {f(root1):.6f}")
print(f"Raíz 2 ≈ {root2:.9f}   f(x) = {f(root2):.6f}")


# -------------------------------------------------------
# 4. Gráfica igual que en Excel
#    - puntos x = 0,1,2,3,4,5,6
#    - curva de f(x)
#    - raíz 1 en rojo, raíz 2 en verde
# -------------------------------------------------------
x_vals = [0, 1, 2, 3, 4, 5, 6]      # mismos puntos que tu tabla
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función con puntos
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x
plt.axhline(0, color="black")

# Raíz 1 (intervalo 3–4) en rojo
plt.scatter([root1], [f(root1)], s=60, color="red", label="Raíz 1")

# Raíz 2 (intervalo 7–8) en verde
plt.scatter([root2], [f(root2)], s=60, color="green", label="Raíz 2")

# Límites de ejes para que se parezca al Excel
plt.xlim(0, 8)
plt.ylim(-40, 80)

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
