import math
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Función del ejercicio
#    f(x) = cos^2(x) - 0.5 * x * e^(0.3x) + 5
# -------------------------------------------------------
def f(x: float) -> float:
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5


# -------------------------------------------------------
# 2. Método de la bisección
# -------------------------------------------------------
def biseccion(f, a_inicial, b_inicial, tol=5e-5, max_it=50):
    """
    f        : función
    a_inicial, b_inicial : intervalo inicial [a,b]
    tol      : tolerancia sobre |f(m)|
    max_it   : máximo de iteraciones
    """
    a = a_inicial
    b = b_inicial
    fa = f(a)
    fb = f(b)

    tabla = []

    for k in range(max_it):
        m = (a + b) / 2.0
        fm = f(m)

        # Guardamos fila: #, a, b, m, f(a), f(b), f(m)
        tabla.append((k, a, b, m, fa, fb, fm))

        # Criterio de paro, igual que en el Excel: |f(m)| <= tol
        if abs(fm) <= tol:
            break

        # Regla de bisección
        if fa * fm < 0:
            # La raíz está entre a y m
            b, fb = m, fm
        else:
            # La raíz está entre m y b
            a, fa = m, fm

    return tabla


# -------------------------------------------------------
# 3. Ejecutar bisección para el intervalo [3, 4]
# -------------------------------------------------------
tol = 5e-5
tabla = biseccion(f, 3.0, 4.0, tol=tol)

# La última fila contiene la aproximación final
_, a_fin, b_fin, m_fin, fa_fin, fb_fin, fm_fin = tabla[-1]

print("=== Método de la Bisección para cos^2(x) - 0.5 x e^(0.3x) + 5 = 0 ===\n")
print(" k        a              b              m              f(a)            f(b)            f(m)")
for k, a, b, m, fa, fb, fm in tabla:
    print(f"{k:2d}  {a:12.9f}  {b:12.9f}  {m:12.9f}  {fa: .9e}  {fb: .9e}  {fm: .9e}")

print("\nAproximación final de la raíz positiva (bisección):")
print(f"a_final = {a_fin:.12f}")
print(f"b_final = {b_fin:.12f}")
print(f"m_final = {m_fin:.12f}")
print(f"f(m_final) = {fm_fin:.9e}")


# -------------------------------------------------------
# 4. Gráfica como en el Excel
#    - x = 0,1,2,3,4,5,6
#    - curva de f(x)
#    - raíz marcada en m_final
# -------------------------------------------------------
x_vals = list(range(0, 7))      # 0,1,2,3,4,5,6
y_vals = [f(x) for x in x_vals]

plt.figure()

# Curva de la función
plt.plot(x_vals, y_vals, marker="o", label="f(x)")

# Eje x (y = 0)
plt.axhline(0, color="black")

# Punto de la raíz por bisección
plt.scatter([m_fin], [f(m_fin)], s=60, color="green", label="Raíz (bisección)")

plt.title("Gráfica de f(x) con raíz por bisección")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 6)
plt.grid(True)
plt.legend()

plt.show()
