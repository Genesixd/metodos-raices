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
        m = (a + b) / 2.0
        fm = f(m)

        # Guardamos la fila como en el Excel: k, a, b, m, f(a), f(b), f(m)
        tabla.append((k, a, b, m, fa, fb, fm))

        # Criterio de paro igual que el Excel: |f(m)| <= tol
        if abs(fm) <= tol:
            break

        # Reglas del método de bisección
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return tabla


# -------------------------------------------------------
# 3. Obtener las tres raíces en los mismos intervalos
# -------------------------------------------------------
tol = 0.005

tab1 = biseccion(f, -1.5, -1.0, tol=tol)   # Raíz 1
tab2 = biseccion(f,  0.0,  0.5, tol=tol)   # Raíz 2
tab3 = biseccion(f,  1.5,  2.0, tol=tol)   # Raíz 3

root1 = tab1[-1][3]  # último m
root2 = tab2[-1][3]
root3 = tab3[-1][3]

print("=== Método de Bisección para x^3 - x^2 e^{-0.5x} - 3x = -1 ===\n")

print("Raíz 1 (intervalo -1.5 a -1)")
print(" k        a           b           m           f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tab1:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")
print(f"→ Raíz 1 ≈ {root1:.9f},   f(x) = {f(root1):.6f}\n")

print("Raíz 2 (intervalo 0 a 0.5)")
print(" k        a           b           m           f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tab2:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")
print(f"→ Raíz 2 ≈ {root2:.9f},   f(x) = {f(root2):.6f}\n")

print("Raíz 3 (intervalo 1.5 a 2)")
print(" k        a           b           m           f(a)         f(b)         f(m)")
for k, a, b, m, fa, fb, fm in tab3:
    print(f"{k:2d}  {a:9.6f}  {b:9.6f}  {m:9.6f}  {fa:11.6f}  {fb:11.6f}  {fm:11.6f}")
print(f"→ Raíz 3 ≈ {root3:.9f},   f(x) = {f(root3):.6f}\n")


# -------------------------------------------------------
# 4. Gráfica igual a tu Excel
#    - x de -2 a 3 con paso 0.5
#    - curva de f(x)
#    - raíces marcadas
# -------------------------------------------------------
x_vals = [-2 + 0.5 * i for i in range(11)]  # -2, -1.5, ..., 3
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x (y = 0)
plt.axhline(0, color="black")

# Raíces encontradas (como en la gráfica de Excel)
plt.scatter([root1], [f(root1)], s=60, color="purple", label="Raíz 1")
plt.scatter([root2], [f(root2)], s=60, color="orange", label="Raíz 2")
plt.scatter([root3], [f(root3)], s=60, color="green",  label="Raíz 3")

plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()
