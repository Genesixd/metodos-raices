// =============================
// Configuración global
// =============================
const TOL = 0.00005;
const MAX_ITER = 100;

// Datos de los ejercicios
const ejercicios = {
  ej1: {
    id: "ej1",
    nombre: "Ejercicio 1",
    descripcion: "x³ − e^{0.8x} − 20 = 0",
    f: (x) => x ** 3 - Math.exp(0.8 * x) - 20,
    df: (x) => 3 * x ** 2 - 0.8 * Math.exp(0.8 * x),
    exactRoots: [3.2082198, 7.4898387],
    plotRange: { min: 0, max: 9 }
  },
  ej2: {
    id: "ej2",
    nombre: "Ejercicio 2",
    descripcion: "3·sin(0.5x) − 0.5x + 2 = 0",
    f: (x) => 3 * Math.sin(0.5 * x) - 0.5 * x + 2,
    df: (x) => 1.5 * Math.cos(0.5 * x) - 0.5,
    exactRoots: [5.7064179972],
    plotRange: { min: 0, max: 8 }
  },
  ej3: {
    id: "ej3",
    nombre: "Ejercicio 3",
    descripcion: "x³ − x² e^{−0.5x} − 3x + 1 = 0",
    f: (x) => x ** 3 - x ** 2 * Math.exp(-0.5 * x) - 3 * x + 1,
    df: (x) =>
      3 * x ** 2 + (0.5 * x ** 2 - 2 * x) * Math.exp(-0.5 * x) - 3,
    exactRoots: [-1.234093, 0.315466, 1.780241],
    plotRange: { min: -2, max: 3 }
  },
  ej4: {
    id: "ej4",
    nombre: "Ejercicio 4",
    descripcion: "cos²(x) − 0.5x e^{0.3x} + 5 = 0",
    f: (x) =>
      Math.cos(x) ** 2 - 0.5 * x * Math.exp(0.3 * x) + 5,
    df: (x) =>
      -Math.sin(2 * x) - 0.5 * Math.exp(0.3 * x) - 0.15 * x * Math.exp(0.3 * x),
    exactRoots: [3.7256021765],
    plotRange: { min: 0, max: 6 }
  }
};

// =============================
// Sugerencias de valores iniciales
// =============================
const sugerencias = {
  ej1: {
    biseccion: [
      { titulo: "Raíz cercana a 3.208", a: 3, b: 4 },
      { titulo: "Raíz cercana a 7.489", a: 7, b: 8 }
    ],
    secante: [
      { titulo: "Raíz cercana a 3.208", x0: 3, x1: 4 },
      { titulo: "Raíz cercana a 7.489", x0: 7, x1: 8 }
    ],
    newton: [
      { titulo: "Raíz cercana a 3.208", x0: 3 },
      { titulo: "Raíz cercana a 7.489", x0: 8 }
    ]
  },
  ej2: {
    biseccion: [
      { titulo: "Única raíz (~5.7064)", a: 5, b: 6 }
    ],
    secante: [
      { titulo: "Única raíz (~5.7064)", x0: 5, x1: 6 }
    ],
    newton: [
      { titulo: "Única raíz (~5.7064)", x0: 5 }
    ]
  },
  ej3: {
    biseccion: [
      { titulo: "Raíz 1 (~−1.234)", a: -1.5, b: -1 },
      { titulo: "Raíz 2 (~0.315)", a: 0, b: 0.5 },
      { titulo: "Raíz 3 (~1.780)", a: 1.5, b: 2 }
    ],
    secante: [
      { titulo: "Raíz 1 (~−1.234)", x0: -1.5, x1: -1 },
      { titulo: "Raíz 2 (~0.315)", x0: 0, x1: 0.5 },
      { titulo: "Raíz 3 (~1.780)", x0: 1.5, x1: 2 }
    ],
    newton: [
      { titulo: "Raíz 1 (~−1.234)", x0: -1.2 },
      { titulo: "Raíz 2 (~0.315)", x0: 0.3 },
      { titulo: "Raíz 3 (~1.780)", x0: 1.8 }
    ]
  },
  ej4: {
    biseccion: [
      { titulo: "Única raíz (~3.7256)", a: 3, b: 4 }
    ],
    secante: [
      { titulo: "Única raíz (~3.7256)", x0: 3, x1: 4 }
    ],
    newton: [
      { titulo: "Única raíz (~3.7256)", x0: 3.5 }
    ]
  }
};

let chart = null;

// =====================================
// Métodos numéricos
// =====================================

function biseccion(f, a, b, tol = TOL, maxIter = MAX_ITER) {
  const iteraciones = [];

  let fa = f(a);
  let fb = f(b);

  if (fa * fb > 0) {
    return { error: "En [a,b] no hay cambio de signo (f(a)·f(b) > 0)." };
  }

  let prevM = null;
  let m = null;

  for (let i = 1; i <= maxIter; i++) {
    m = 0.5 * (a + b);
    const fm = f(m);

    let ea = null;
    let er = null;
    let ep = null;

    if (prevM !== null) {
      ea = Math.abs(m - prevM);
      if (m !== 0) {
        er = ea / Math.abs(m);
        ep = er * 100;
      }
    }

    iteraciones.push({
      iter: i,
      x: m,
      fx: fm,
      ea,
      er,
      ep
    });

    if (Math.abs(fm) <= tol) {
      return {
        root: m,
        iterations: i,
        iteraciones
      };
    }

    if (fa * fm < 0) {
      b = m;
      fb = fm;
    } else {
      a = m;
      fa = fm;
    }

    prevM = m;
  }

  return {
    root: m,
    iterations: maxIter,
    iteraciones,
    warning: "No se alcanzó la tolerancia dentro del número máximo de iteraciones."
  };
}

function secante(f, x0, x1, tol = TOL, maxIter = MAX_ITER) {
  const iteraciones = [];
  let fx0 = f(x0);
  let fx1 = f(x1);

  for (let i = 1; i <= maxIter; i++) {
    const denom = fx1 - fx0;
    if (denom === 0) {
      return { error: "División por cero en el método de la secante (f(x1) = f(x0))." };
    }

    const x2 = x1 - fx1 * (x1 - x0) / denom;
    const fx2 = f(x2);

    const ea = Math.abs(x2 - x1);
    let er = null;
    let ep = null;
    if (x2 !== 0) {
      er = ea / Math.abs(x2);
      ep = er * 100;
    }

    iteraciones.push({
      iter: i,
      x: x2,
      fx: fx2,
      ea,
      er,
      ep
    });

    if (Math.abs(fx2) <= tol) {
      return {
        root: x2,
        iterations: i,
        iteraciones
      };
    }

    x0 = x1;
    fx0 = fx1;
    x1 = x2;
    fx1 = fx2;
  }

  return {
    root: x1,
    iterations: maxIter,
    iteraciones,
    warning: "No se alcanzó la tolerancia dentro del número máximo de iteraciones."
  };
}

function newtonRaphson(f, df, x0, tol = TOL, maxIter = MAX_ITER) {
  const iteraciones = [];
  let x = x0;

  for (let i = 1; i <= maxIter; i++) {
    const fx = f(x);
    const dfx = df(x);

    if (dfx === 0) {
      return { error: "La derivada se anuló (f'(x) = 0). Newton no puede continuar." };
    }

    const xNext = x - fx / dfx;
    const ea = Math.abs(xNext - x);
    let er = null;
    let ep = null;

    if (xNext !== 0) {
      er = ea / Math.abs(xNext);
      ep = er * 100;
    }

    iteraciones.push({
      iter: i,
      x: xNext,
      fx: f(xNext),
      ea,
      er,
      ep
    });

    if (Math.abs(f(xNext)) <= tol) {
      return {
        root: xNext,
        iterations: i,
        iteraciones
      };
    }

    x = xNext;
  }

  return {
    root: x,
    iterations: maxIter,
    iteraciones,
    warning: "No se alcanzó la tolerancia dentro del número máximo de iteraciones."
  };
}

// =====================================
// Utilidades
// =====================================

function formatearNumero(v, dec = 8) {
  if (v === null || v === undefined || Number.isNaN(v)) return "-";
  return v.toFixed(dec);
}

function encontrarRaizExactaMasCercana(exactRoots, rootAprox) {
  if (!exactRoots || exactRoots.length === 0) return null;
  let mejor = exactRoots[0];
  let minDiff = Math.abs(rootAprox - mejor);
  for (let i = 1; i < exactRoots.length; i++) {
    const diff = Math.abs(rootAprox - exactRoots[i]);
    if (diff < minDiff) {
      minDiff = diff;
      mejor = exactRoots[i];
    }
  }
  return mejor;
}

// =====================================
// Gráfica con Chart.js
// =====================================

let chartInstance = null;

function graficarFuncion(ejercicioKey, rootAprox) {
  const ejercicio = ejercicios[ejercicioKey];
  const { min, max } = ejercicio.plotRange;
  const f = ejercicio.f;

  const puntos = [];
  const N = 200;
  const step = (max - min) / (N - 1);

  for (let i = 0; i < N; i++) {
    const x = min + i * step;
    const y = f(x);
    puntos.push({ x, y });
  }

  const ctx = document.getElementById("chart").getContext("2d");

  if (chartInstance) {
    chartInstance.destroy();
  }

  const rootsData = [];
  if (typeof rootAprox === "number") {
    rootsData.push({ x: rootAprox, y: 0 });
  }

  chartInstance = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          label: "f(x)",
          data: puntos,
          parsing: false,
          borderWidth: 1.5,
          pointRadius: 0,
          borderColor: "rgba(96, 165, 250, 1)"
        },
        {
          label: "Raíz aproximada",
          data: rootsData,
          parsing: false,
          type: "scatter",
          pointRadius: 5,
          borderWidth: 2,
          backgroundColor: "rgba(248, 250, 252, 1)",
          borderColor: "rgba(248, 250, 252, 1)"
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: {
            color: "#e5e7eb"
          }
        }
      },
      scales: {
        x: {
          type: "linear",
          position: "bottom",
          grid: {
            color: "rgba(31, 41, 55, 1)"
          },
          ticks: {
            color: "#9ca3af"
          }
        },
        y: {
          grid: {
            color: "rgba(31, 41, 55, 1)"
          },
          ticks: {
            color: "#9ca3af"
          }
        }
      }
    }
  });
}

// =====================================
// Sugerencias UI
// =====================================

function actualizarSugerencias() {
  const ejercicioKey = document.getElementById("ejercicio").value;
  const metodo = document.getElementById("metodo").value;
  const cont = document.getElementById("sugerencias");

  cont.innerHTML = "";

  const ej = ejercicios[ejercicioKey];
  const lista =
    sugerencias[ejercicioKey] && sugerencias[ejercicioKey][metodo]
      ? sugerencias[ejercicioKey][metodo]
      : null;

  const titulo = document.createElement("p");
  titulo.classList.add("sugerencias-titulo");
  titulo.textContent =
    "Sugerencias de valores iniciales para " +
    ej.nombre +
    " – " +
    metodo.toUpperCase();
  cont.appendChild(titulo);

  if (!lista || lista.length === 0) {
    const p = document.createElement("p");
    p.textContent =
      "No hay sugerencias predefinidas. Usa los valores que consideres adecuados.";
    cont.appendChild(p);
    return;
  }

  lista.forEach((sug) => {
    const card = document.createElement("div");
    card.classList.add("sugerencia-card");

    const pTitulo = document.createElement("p");
    pTitulo.innerHTML = "<strong>" + sug.titulo + "</strong>";
    card.appendChild(pTitulo);

    const pDatos = document.createElement("p");
    if (metodo === "biseccion") {
      pDatos.textContent = `a = ${sug.a}, b = ${sug.b}`;
    } else if (metodo === "secante") {
      pDatos.textContent = `x₀ = ${sug.x0}, x₁ = ${sug.x1}`;
    } else if (metodo === "newton") {
      pDatos.textContent = `x₀ = ${sug.x0}`;
    }
    card.appendChild(pDatos);

    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = "Usar estos valores";
    btn.addEventListener("click", () => {
      if (metodo === "biseccion") {
        document.getElementById("a").value = sug.a;
        document.getElementById("b").value = sug.b;
      } else if (metodo === "secante") {
        document.getElementById("x0-secante").value = sug.x0;
        document.getElementById("x1-secante").value = sug.x1;
      } else if (metodo === "newton") {
        document.getElementById("x0-newton").value = sug.x0;
      }
    });
    card.appendChild(btn);

    cont.appendChild(card);
  });
}

// =====================================
// Manejo de UI principal
// =====================================

function actualizarInputsMetodo() {
  const metodo = document.getElementById("metodo").value;

  const bloques = document.querySelectorAll(".method-inputs");
  bloques.forEach((b) => b.classList.add("hidden"));

  if (metodo === "biseccion") {
    document.getElementById("inputs-biseccion").classList.remove("hidden");
  } else if (metodo === "secante") {
    document.getElementById("inputs-secante").classList.remove("hidden");
  } else if (metodo === "newton") {
    document.getElementById("inputs-newton").classList.remove("hidden");
  }
}

function ejecutar() {
  const ejercicioKey = document.getElementById("ejercicio").value;
  const metodo = document.getElementById("metodo").value;
  const ejercicio = ejercicios[ejercicioKey];
  const mensajeError = document.getElementById("mensaje-error");
  const tbody = document.querySelector("#tabla-iteraciones tbody");
  const resumenDiv = document.getElementById("resumen");

  mensajeError.textContent = "";
  tbody.innerHTML = "";
  resumenDiv.innerHTML = "";

  let resultado = null;

  try {
    if (metodo === "biseccion") {
      const a = parseFloat(document.getElementById("a").value);
      const b = parseFloat(document.getElementById("b").value);
      if (Number.isNaN(a) || Number.isNaN(b)) {
        mensajeError.textContent = "Ingresa valores numéricos válidos para a y b.";
        return;
      }
      resultado = biseccion(ejercicio.f, a, b);
    } else if (metodo === "secante") {
      const x0 = parseFloat(document.getElementById("x0-secante").value);
      const x1 = parseFloat(document.getElementById("x1-secante").value);
      if (Number.isNaN(x0) || Number.isNaN(x1)) {
        mensajeError.textContent = "Ingresa valores numéricos válidos para x₀ y x₁.";
        return;
      }
      resultado = secante(ejercicio.f, x0, x1);
    } else if (metodo === "newton") {
      const x0 = parseFloat(document.getElementById("x0-newton").value);
      if (Number.isNaN(x0)) {
        mensajeError.textContent = "Ingresa un valor numérico válido para x₀.";
        return;
      }
      if (!ejercicio.df) {
        mensajeError.textContent = "Este ejercicio no tiene derivada definida.";
        return;
      }
      resultado = newtonRaphson(ejercicio.f, ejercicio.df, x0);
    }
  } catch (e) {
    mensajeError.textContent = "Ocurrió un error: " + e.message;
    return;
  }

  if (resultado.error) {
    mensajeError.textContent = resultado.error;
    return;
  }

  // ----- Resumen -----
  const rootAprox = resultado.root;
  const exactRoot = encontrarRaizExactaMasCercana(
    ejercicio.exactRoots,
    rootAprox
  );

  const errorAbsolutoFinal =
    exactRoot != null ? Math.abs(rootAprox - exactRoot) : null;
  const errorRelativoFinal =
    exactRoot != null && exactRoot !== 0
      ? errorAbsolutoFinal / Math.abs(exactRoot)
      : null;
  const errorPorcentualFinal =
    errorRelativoFinal != null ? errorRelativoFinal * 100 : null;

  const p1 = document.createElement("p");
  p1.innerHTML = `<strong>Ejercicio:</strong> ${ejercicio.nombre} – ${ejercicio.descripcion}`;
  const p2 = document.createElement("p");
  p2.innerHTML = `<strong>Método:</strong> ${metodo.toUpperCase()}`;
  const p3 = document.createElement("p");
  p3.innerHTML = `<strong>Tolerancia usada:</strong> ${TOL}`;
  const p4 = document.createElement("p");
  p4.innerHTML = `<strong>Raíz aproximada:</strong> ${formatearNumero(rootAprox, 10)}`;
  const p5 = document.createElement("p");
  p5.innerHTML = `<strong>Iteraciones:</strong> ${resultado.iterations}`;

  resumenDiv.appendChild(p1);
  resumenDiv.appendChild(p2);
  resumenDiv.appendChild(p3);
  resumenDiv.appendChild(p4);
  resumenDiv.appendChild(p5);

  if (exactRoot != null) {
    const p6 = document.createElement("p");
    p6.innerHTML = `<strong>Solución de referencia (raíz más cercana):</strong> ${formatearNumero(
      exactRoot,
      10
    )}`;
    const p7 = document.createElement("p");
    p7.innerHTML = `<strong>Error absoluto final:</strong> ${formatearNumero(
      errorAbsolutoFinal,
      10
    )}`;
    const p8 = document.createElement("p");
    p8.innerHTML = `<strong>Error relativo final:</strong> ${
      errorRelativoFinal != null ? formatearNumero(errorRelativoFinal, 10) : "-"
    }`;
    const p9 = document.createElement("p");
    p9.innerHTML = `<strong>Error porcentual final:</strong> ${
      errorPorcentualFinal != null
        ? formatearNumero(errorPorcentualFinal, 6)
        : "-"
    } %`;

    resumenDiv.appendChild(p6);
    resumenDiv.appendChild(p7);
    resumenDiv.appendChild(p8);
    resumenDiv.appendChild(p9);
  }

  if (resultado.warning) {
    const pw = document.createElement("p");
    pw.style.color = "#fbbf24";
    pw.textContent = "Aviso: " + resultado.warning;
    resumenDiv.appendChild(pw);
  }

  // ----- Tabla de iteraciones -----
  resultado.iteraciones.forEach((it) => {
    const tr = document.createElement("tr");

    const tdIter = document.createElement("td");
    tdIter.textContent = it.iter;

    const tdX = document.createElement("td");
    tdX.textContent = formatearNumero(it.x);

    const tdFx = document.createElement("td");
    tdFx.textContent = formatearNumero(it.fx);

    const tdEa = document.createElement("td");
    tdEa.textContent = it.ea != null ? formatearNumero(it.ea) : "-";

    const tdEr = document.createElement("td");
    tdEr.textContent = it.er != null ? formatearNumero(it.er) : "-";

    const tdEp = document.createElement("td");
    tdEp.textContent = it.ep != null ? formatearNumero(it.ep, 6) : "-";

    tr.appendChild(tdIter);
    tr.appendChild(tdX);
    tr.appendChild(tdFx);
    tr.appendChild(tdEa);
    tr.appendChild(tdEr);
    tr.appendChild(tdEp);

    tbody.appendChild(tr);
  });

  // ----- Gráfica -----
  graficarFuncion(ejercicioKey, rootAprox);
}

// =====================================
// Eventos
// =====================================

document.addEventListener("DOMContentLoaded", () => {
  actualizarInputsMetodo();
  actualizarSugerencias();

  document.getElementById("metodo").addEventListener("change", () => {
    actualizarInputsMetodo();
    actualizarSugerencias();
  });

  document.getElementById("ejercicio").addEventListener("change", () => {
    actualizarSugerencias();
  });

  document.getElementById("btn-ejecutar").addEventListener("click", ejecutar);
});
