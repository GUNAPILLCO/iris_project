# IRIS PROJECT — KNOWLEDGE SYNTHESIS
## Síntesis crítica de Jansen + López de Prado + Murphy

**Naturaleza:** marco epistemológico único derivado de las tres Knowledge Bases. **No es un resumen, ni una concatenación, ni un diseño.**
**Fuentes autoritativas:** `KB01` (Jansen), `KB02` (López de Prado), `KB03` (Murphy). Los libros originales no se reprocesan.
**Posición:** última etapa bibliográfica. La siguiente es el análisis empírico del MNQ.

---

## CHECKPOINT

```
Fuentes:
KB01 Jansen            — utilizada
KB02 López de Prado    — utilizada
KB03 Murphy            — utilizada

Última sección completada: §23 — TODAS COMPLETADAS
Siguiente sección: — (ninguna)
Preguntas abiertas procesadas: 160 originales → 79 canónicas
Preguntas pendientes: ninguna sin clasificar
Estado: COMPLETE
```

---

## §0. CONVENCIONES

### 0.1 Categorías epistemológicas

| Etiqueta | Significado |
|---|---|
| `[CONSENSO FUERTE]` | Dos o tres fuentes sostienen principios compatibles y **no hay objeción material pendiente**. Usado con extrema parsimonia. |
| `[CONVERGENCIA]` | Las fuentes llegan por caminos distintos a una idea similar, **sin demostrar necesariamente lo mismo**. |
| `[COMPLEMENTARIEDAD]` | Una fuente aporta la pieza que resuelve un vacío de otra. |
| `[TENSIÓN]` | Posiciones incompatibles o parcialmente incompatibles entre fuentes. |
| `[CONTRADICCIÓN INTERNA]` | Una misma fuente sostiene posiciones incompatibles. |
| `[RESTRICCIÓN METODOLÓGICA]` | Condición que debe respetarse para que el resultado sea válido, **sea cual sea la arquitectura**. |
| `[HIPÓTESIS CANDIDATA]` | Idea razonable y falsable que merece contraste empírico. |
| `[PREGUNTA EMPÍRICA]` | Sólo resoluble analizando MNQ. |
| `[DECISIÓN DE DISEÑO ABIERTA]` | Varias alternativas defendibles; habrá que elegir más adelante. |
| `[VACÍO]` | Las tres fuentes son insuficientes. |
| `[FUERA DE ALCANCE ACTUAL]` | Requiere datos o arquitectura que contradicen el alcance vigente. |
| `[DESCARTABLE METODOLÓGICAMENTE]` | No debe avanzar en su formulación actual (look-ahead inevitable, no falsabilidad, subjetividad irreproducible, datos inexistentes, grados de libertad incontrolables). |

### 0.2 Atribución

`[JANSEN]` · `[LDP]` · `[MURPHY]` para afirmaciones de los autores según constan en las KB.
`[SÍNTESIS — INTERPRETACIÓN]` para inferencias nuevas producidas en esta etapa.
`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` para consecuencias potenciales.
`[CONOCIMIENTO EXTERNO]` sólo si es estrictamente necesario.

**Regla de trazabilidad:** toda conclusión material referencia la sección de la KB de origen (p. ej. `KB03 §4.4`).

### 0.3 Estatus del alcance actual

El alcance vigente —MNQ, `Timestamp+OHLCV`, orientación intradiaria, dependencia mínima de fuentes externas— se trata en todo el documento como **`[RESTRICCIÓN ACTUAL DEL PROYECTO]`**, no como configuración óptima demostrada. Cuando la literatura tensiona con él, se identifica la tensión, se nombra la defensa perdida, se estima el riesgo, se listan defensas sustitutivas y **la decisión queda abierta**.

### 0.4 Lo que esta síntesis no hace

No vota entre autores, no privilegia al más reciente ni al más matemático, no invalida a Murphy por cualitativo ni trata a Jansen como receta. No infiere capacidad predictiva de la existencia de una fórmula, ni robustez de la simplicidad, ni rigor de la complejidad. **No reutiliza ninguna decisión de versiones históricas de IRIS** (horarios, targets OPC, esquemas LONG_TP/SL, lookbacks, arquitecturas neuronales, walk-forward concreto): son antecedentes, no especificación.

---

# §1. INVENTARIO Y MAPA CANÓNICO DE PREGUNTAS ABIERTAS

## 1.1 Material de partida

| Fuente | Sección | Preguntas originales |
|---|---|---|
| KB01 Jansen | §24 (+ §23 matriz, §22 limitaciones, §25 qué llevar) | **60** |
| KB02 López de Prado | §30 (+ §25 A/B/C/D, §28 limitaciones, §29 matriz maestra) | **60** |
| KB03 Murphy | §31 (+ §26 tensiones, §27 limitaciones, §29 heredadas, §30 matriz) | **40** |
| | **Total bruto** | **160** |

Tras normalización y eliminación de duplicados conceptuales: **79 preguntas canónicas** agrupadas en **20 bloques**.

`[SÍNTESIS — INTERPRETACIÓN]` La reducción de 160 a 79 no es sólo compresión: **revela que las tres fuentes convergen sobre un conjunto sorprendentemente pequeño de decisiones fundamentales**, formuladas en vocabularios distintos. El ejemplo del encargo es exacto: "objetivo predictivo" (Jansen), "esquema de labeling" (LdP) y "dirección, magnitud, evento o decisión" (Murphy) son **la misma decisión** vista desde tres tradiciones.

## 1.2 Mapa canónico

Notación de trazabilidad: `J-n` = pregunta *n* de KB01 §24; `L-n` = pregunta *n* de KB02 §30; `M-n` = pregunta *n* de KB03 §31.

---

### BLOQUE A — Integridad y construcción de la serie

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **A1** | ¿Cómo se construye la serie continua de MNQ: qué criterio de rollover, qué método de ajuste de saltos, y qué se hace con los precios crudos frente a los ajustados? | J-10, L-9, M-16 | `[DECISIÓN DE DISEÑO ABIERTA]` + `[PREGUNTA EMPÍRICA]` |
| **A2** | ¿Qué ocurre con el volumen durante la transición de contratos, y cómo afecta a cualquier esquema de muestreo basado en volumen? | L-10, M-18 | `[VACÍO]` en las tres fuentes + `[PREGUNTA EMPÍRICA]` |
| **A3** | ¿Qué defectos de integridad tiene nuestro histórico (gaps, barras faltantes, días incompletos, timestamps, zona horaria, precios repetidos)? | J-13 (parcial), M implícito | `[PREGUNTA EMPÍRICA]` |
| **A4** | ¿Cuánto histórico tenemos realmente, y cuántos regímenes distintos contiene? | J-9, L-11, L-12, M-19 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE B — Propiedades estadísticas del instrumento

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **B1** | ¿Qué propiedades estadísticas tiene el MNQ intradiario: distribución de retornos, colas, autocorrelación de retornos y de retornos absolutos, clustering de volatilidad, estacionariedad? | J-13, L implícito, M implícito | `[PREGUNTA EMPÍRICA]` |
| **B2** | ¿Existe persistencia direccional medible por encima de la reversión, bajo alguna definición operativa de tendencia? | M-1 (premisa 2), J (momentum), L (implícito) | `[HIPÓTESIS CANDIDATA]` + `[PREGUNTA EMPÍRICA]` |
| **B3** | ¿Dónde está la señal, si existe: en el primer momento (dirección), en el segundo (volatilidad), o en la condicionalidad al régimen? | J-60 | `[PREGUNTA EMPÍRICA]` |
| **B4** | ¿Qué transformación de la serie es estacionaria, y cuánto cuesta en memoria conseguirlo (`d*` de diferenciación fraccionaria)? | L-28, J (estacionariedad) | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE C — Muestreo y unidad de observación

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **C1** | ¿Qué resolución base de barra se adopta, sabiendo que condiciona la calidad de toda aproximación posterior? | J-6, L-5, M-15 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **C2** | ¿Barras temporales, barras de volumen/dólar aproximadas, muestreo por movimiento de precio (P&F), o muestreo por eventos? | J-7, L-6, L-7, M-15, M-25 | `[DECISIÓN DE DISEÑO ABIERTA]` + `[PREGUNTA EMPÍRICA]` |
| **C3** | Si se usa muestreo por eventos: ¿qué variable subyacente y qué umbral, sabiendo que cada valor probado es un intento? | L-34, L-35, L-36 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **C4** | ¿El muestreo por eventos mejora el poder predictivo, o sólo reduce el tamaño muestral? | L-36 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE D — Estructura temporal intradía y definición de sesión

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **D1** | ¿Qué constituye "la sesión" en un instrumento de casi 24 horas? Condiciona pivotes intradía, perfil de sesión, estacionalidad y la propia noción de "día". | J-8, L-8, M-17 | `[VACÍO]` en las tres fuentes + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **D2** | ¿Cuál es la estructura intradiaria real de volatilidad y volumen, y es estable entre años? | J-18, M-24 | `[PREGUNTA EMPÍRICA]` |
| **D3** | ¿Cómo se trata el perfil determinista de la sesión: como feature, como componente a eliminar, o como condicionante del modelo? | J-18, M-24 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE E — Formulación del problema predictivo

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **E1** | ¿Qué debe predecir IRIS: dirección, retorno, magnitud, volatilidad, evento, probabilidad, o decisión directa? | J-1, L-13, M-10 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **E2** | ¿Es el problema predecir el mercado o **seleccionar momentos operables**? Son problemas distintos. | J-2, J-3, L-2 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **E3** | ¿Arquitectura de un componente, de dos (dirección + confianza/tamaño) o de tres (qué/cuándo/cuánto)? | J-4, L-21, L-22, L-23, M-11 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **E4** | ¿Qué significa "oportunidad operativa" en términos medibles? | J-5, L-47 | `[VACÍO]` + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **E5** | ¿Puede una regla técnica actuar como componente primario, o el análisis técnico sólo aporta features? | L-23, M-14 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE F — Etiquetado y horizonte

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **F1** | ¿Etiquetado de horizonte fijo o dependiente del camino? ¿Qué configuración de barreras? | J-24, J-28, L-14, L-15 | `[DECISIÓN DE DISEÑO ABIERTA]` + `[PREGUNTA EMPÍRICA]` |
| **F2** | ¿Qué horizonte, y debe ser fijo o dependiente del estado del mercado? | J-22, J-23, L-18 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **F3** | ¿Se escalan los umbrales por volatilidad, y con qué estimador (EWM de cierres, ATR, High-Low)? | J-25, L-17, L-31, M-implícito | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **F4** | ¿Barreras simétricas o asimétricas? (Acoplado a si se aprende el lado.) | L-16 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **F5** | ¿Se comprueban las barreras contra cierres o contra High/Low, y cómo se resuelve la **ambigüedad intrabar**? | L-19, M (limitación intrabar) | `[VACÍO]` en las tres fuentes + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **F6** | ¿Cómo se etiqueta el caso en que se agota el horizonte sin resolución? | L-20 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE G — Independencia efectiva de las observaciones

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **G1** | ¿Cuántas observaciones **efectivamente independientes** contiene nuestro histórico, dado el etiquetado y el muestreo elegidos? | J-9, J-32, L-11, L-45, M-19 | `[PREGUNTA EMPÍRICA]` (circular con F y C) |
| **G2** | ¿Cómo se maneja el solapamiento de etiquetas: purging, embargo, ponderación por unicidad, o combinación? | J-27, J-31, L-43, L-44 | `[RESTRICCIÓN METODOLÓGICA]` + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **G3** | ¿Cuánto conjunto de entrenamiento se pierde por purging y embargo en frecuencia intradiaria con nuestros horizontes? | L-43 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE H — Validación

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **H1** | ¿Qué esquema de validación: walk-forward purgado, CV purgada, CPCV? ¿Con qué parámetros? | J-29, J-30, L-41, L-42, M-31 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **H2** | ¿Cuánto histórico se reserva como hold-out final y cuándo se toca? | J-33 | `[RESTRICCIÓN METODOLÓGICA]` + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **H3** | ¿Cómo se integran los criterios de robustez de Murphy (estabilidad paramétrica y temporal) con los procedimientos de validación de las otras fuentes? | M-31, L-56 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **H4** | ¿Es CPCV computacionalmente viable a nuestra escala? | L-42 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE I — Presupuesto de investigación y multiple testing

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **I1** | ¿Cómo se registra y contabiliza cada experimento, incluidos los abandonados? | J-35, L (registro de intentos) | `[RESTRICCIÓN METODOLÓGICA]` |
| **I2** | ¿Cuántas hipótesis podemos permitirnos probar, dado el número efectivo de observaciones? | J-16, J-32, L-29, L-45, M-26 | `[PREGUNTA EMPÍRICA]` dependiente de G1 |
| **I3** | ¿Cómo se corrige el score de validación por el número de configuraciones probadas en el tuning? | L-46 | `[VACÍO]` en las tres fuentes |
| **I4** | ¿Qué criterio de parada se aplica a la búsqueda de estrategias? | J-34 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE J — Features e información

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **J1** | ¿Qué features contienen realmente información sobre MNQ? | J-14, L-26, M-20 | `[PREGUNTA EMPÍRICA]` |
| **J2** | ¿Contienen los indicadores técnicos señal incremental sobre retornos rezagados, o son transformaciones redundantes? | J-15, L-27, M-20 | `[PREGUNTA EMPÍRICA]` |
| **J3** | ¿Cómo se agrupan las features redundantes antes de interpretar importancias? | J-21, L-30, M-20 | `[RESTRICCIÓN METODOLÓGICA]` + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **J4** | ¿Cómo se normalizan features en una serie no estacionaria sin introducir look-ahead? | J-17 | `[RESTRICCIÓN METODOLÓGICA]` + `[VACÍO]` parcial |
| **J5** | ¿Qué ventanas temporales (lookback) son relevantes, y se usan varios horizontes simultáneos? | J-19, M-multi-horizonte | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **J6** | ¿Se usa la geometría continua elemental de OHLC o detectores de patrones nominales? | M-22 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **J7** | ¿Se incorpora la estructura de niveles (soportes/resistencias), única familia con problema de causalidad pero con el mejor mecanismo económico? ¿Con qué `k` de confirmación? | M-21, M-23 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **J8** | ¿Aportan valor las transformaciones costosas (fracdiff, entropía, rupturas estructurales, denoising) sobre alternativas simples? | J-20, L-28, L-32, L-33 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE K — Régimen y condicionalidad

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **K1** | ¿Existen regímenes identificables en MNQ, y cómo se asignan **causalmente**? | J-59, L-3, M-27, M-28 | `[PREGUNTA EMPÍRICA]` |
| **K2** | ¿Cambia el signo de la relación entre las features y el retorno futuro según el régimen? | M-27, L (hipótesis entropía), J (interacciones) | `[HIPÓTESIS CANDIDATA]` |
| **K3** | ¿Qué fracción del tiempo está MNQ en régimen tendencial, y es la identificación del régimen el problema principal? | M-13, M-28 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE L — Modelos

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **L1** | ¿Qué familia de modelos? (No respondible a priori: *no free lunch*.) | J-36, L-37, M-implícito | `[PREGUNTA EMPÍRICA]` |
| **L2** | ¿Qué baselines constituyen la referencia mínima obligatoria? | J-38 | `[RESTRICCIÓN METODOLÓGICA]` + `[DECISIÓN DE DISEÑO ABIERTA]` |
| **L3** | ¿Bajo qué evidencia exacta estaría justificado un modelo complejo (incluido Deep Learning)? | J-37 | `[RESTRICCIÓN METODOLÓGICA]` |
| **L4** | ¿Bagging o boosting? ¿Un modelo o un ensemble, y con qué configuración dada la unicidad media? | J-39, L-38, L-39 | `[PREGUNTA EMPÍRICA]` |

---

### BLOQUE M — Probabilidad, confianza y calibración

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **M1** | ¿Cómo se calibran las probabilidades del modelo? | J-44, L-40 | `[VACÍO]` en las tres fuentes |
| **M2** | ¿Cómo se cuantifica y comunica la confianza de una señal? | J-44, L-48 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **M3** | ¿Cómo se valida conjuntamente un sistema de dos modelos sin leakage entre capas? | L-24 | `[VACÍO]` en las tres fuentes |

---

### BLOQUE N — Abstención

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **N1** | ¿Qué mecanismo de abstención se adopta, entre los seis identificados (régimen, umbral de confianza, meta-etiqueta, discretización del tamaño, umbrales asimétricos de entrada/salida, umbral de decisión por costes)? | J-42, J-48, L-25, L-47, L-49, M-12 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **N2** | ¿Deben colapsarse en una única clase `NO_TRADE` los distintos motivos de no operar, o son estados conceptualmente distintos? | M-12, L-25 | `[HIPÓTESIS ESTRUCTURAL]` — ver §7.5 |
| **N3** | ¿Se mantiene una clase neutra explícita, pese a que LdP la desaconseja? | L-25 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE O — Dimensionamiento y gestión de riesgo

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **O1** | ¿Sizing fijo o proporcional a la confianza? (Acoplado a la métrica de entrenamiento.) | J-45, L-48, M-35 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **O2** | ¿Hay stop-loss y objetivo de beneficio? ¿Escalados por volatilidad o situados en niveles estructurales? | J-46, M-36, M-38 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **O3** | ¿Cómo se gestiona una posición abierta cuando llega una señal contraria o concurrente? | J-47, L (promediado de apuestas) | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **O4** | ¿Se adoptan salidas asimétricas, dado que Murphy sostiene que las salidas importan más que las entradas? | M-37 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **O5** | ¿Qué drawdown y tiempo bajo agua son aceptables? | J-55, L-54 | `[DECISIÓN DEL PROYECTO]` |

---

### BLOQUE P — Viabilidad económica y costes

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **P1** | ¿Cuáles son los costes reales de operar MNQ (comisión, spread, slippage) a la frecuencia candidata? | J-52, L-51, M-32 | `[PREGUNTA EMPÍRICA]` externa a los datos OHLCV |
| **P2** | ¿Cuál es el edge mínimo por operación que hace viable la estrategia, y qué precisión exigiría? | J-51, L-52, L-53, M-32 | `[PREGUNTA EMPÍRICA]` calculable *ex-ante* |
| **P3** | ¿Cuántas operaciones son sostenibles, y cuál es la relación entre frecuencia, edge por operación y coste total? | J-53, J-54, L-50 | `[PREGUNTA EMPÍRICA]` |
| **P4** | ¿Existe predictibilidad suficiente en MNQ intradiario para superar los costes? | J-50, L-1, M-implícito | `[PREGUNTA EMPÍRICA]` — **la pregunta terminal del proyecto** |

---

### BLOQUE Q — Métricas y evidencia

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **Q1** | ¿Qué métricas son primarias, entre los tres conjuntos disponibles (ML, económicas de riesgo-retorno, de sistema)? | J-56, M-33 | `[DECISIÓN DE DISEÑO ABIERTA]` |
| **Q2** | ¿Es el Information Coefficient una métrica válida para una serie temporal única, o requiere redefinición? | J-56 | `[VACÍO]` parcial |
| **Q3** | ¿Cómo se mide la amplitud (número de apuestas independientes) en un instrumento único? | J-57, L-implícito | `[VACÍO]` en las tres fuentes |
| **Q4** | ¿Tiene sentido hablar de alfa cuando el benchmark natural es el subyacente del propio contrato? | J-58, L-57 | `[VACÍO]` conceptual |
| **Q5** | ¿Cómo se agregan múltiples señales o múltiples horizontes en una decisión? | J-49, M-34 | `[VACÍO]` en las tres fuentes |

---

### BLOQUE R — Instrumento único y defensas sustitutivas

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **R1** | ¿Cómo se compensa la ausencia de la defensa que aporta un universo multiactivo, **recomendado explícitamente por LdP, exigido por Murphy como criterio de robustez, y presupuesto por el aparato métrico de Jansen**? | L-55, M-3, J-implícito | `[TENSIÓN]` estructural — ver §8 |
| **R2** | ¿Es el análogo temporal (consistencia entre períodos y regímenes) suficientemente fuerte como sustituto? | L-56, M-3 | `[VACÍO]` — es interpretación, no propuesta de ninguna fuente |

---

### BLOQUE S — Despliegue y monitorización

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **S1** | ¿Cómo se monitoriza que el sistema sigue siendo válido tras el despliegue? | J-41, L-58, M-39 | `[VACÍO]` en las tres fuentes |
| **S2** | ¿Con qué frecuencia se reentrena y bajo qué criterio se retira? | J-40, L-59, L-60, M-40 | `[DECISIÓN DE DISEÑO ABIERTA]` |

---

### BLOQUE T — Alcance del proyecto

| # | Pregunta canónica | Origen | Categoría |
|---|---|---|---|
| **T1** | ¿Se mantiene el instrumento único o se amplía el universo? | J-12, L-55, M-3 | `[DECISIÓN DEL PROYECTO]` |
| **T2** | ¿Se mantiene OHLCV como única fuente, o se incorporan datos de tick/quote? | J-11, L (renuncias), M (cuatro renuncias) | `[DECISIÓN DEL PROYECTO]` |
| **T3** | ¿Qué coste computacional es aceptable? Condiciona CPCV, sequential bootstrap, SADF y detectores paramétricos. | L-42, M-implícito | `[DECISIÓN DEL PROYECTO]` |

---

## 1.3 Observaciones sobre el mapa

`[SÍNTESIS — INTERPRETACIÓN]` Cuatro hallazgos del proceso de normalización:

**1. Diez preguntas son `[VACÍO]` en las tres fuentes simultáneamente.** A2 (volumen en rollover), D1 (definición de sesión), E4 (qué es una oportunidad), F5 (ambigüedad intrabar), I3 (corrección del score por tuning), M1 (calibración), M3 (validación de dos capas), Q3 (amplitud en instrumento único), Q5 (agregación de señales), S1 (monitorización). **Ninguna bibliografía adicional de este tipo las resolverá**: requieren o bien decisión propia, o bien desarrollo metodológico nuevo.

**2. Hay una dependencia circular estructural** entre C (muestreo), F (etiquetado) y G (independencia efectiva): no se puede calcular G1 sin fijar F, no se puede evaluar F sin conocer C, y la elección de C debería informarse por G. **Esto tiene consecuencias directas sobre el orden del análisis empírico** (ver §18).

**3. La pregunta P4 es terminal, no una más.** "¿Existe predictibilidad explotable en MNQ intradiario para superar los costes?" es la única cuya respuesta negativa invalidaría el proyecto entero. Las tres fuentes la dejan explícitamente abierta y **ninguna afirma que la respuesta sea sí** para ningún instrumento concreto.

**4. Tres preguntas no son científicas sino de proyecto** (T1, T2, T3) y una es de tolerancia al riesgo (O5). Mezclarlas con las demás sería un error de categoría: no se resuelven con datos ni con literatura.

---

# §2. MATRIZ DE COBERTURA CRUZADA

Cada fila contrasta qué aporta cada fuente sobre un tema y establece el **estado conjunto** con las categorías de §0.1.

| Tema | Jansen (KB01) | López de Prado (KB02) | Murphy (KB03) | Estado conjunto |
|---|---|---|---|---|
| **Naturaleza del problema** | El ML es un elemento dentro de un proceso, no el proceso (§1.1) | El problema no es predecir sino no engañarse; feature discovery ≠ strategy discovery (§1.5) | Análisis ≠ timing ≠ gestión monetaria: qué / cuándo / cuánto (§16.1) | **`[CONVERGENCIA]`** — las tres descomponen el problema, pero **en ejes distintos**. Ver §5.1 (posible falsa convergencia) |
| **Datos como ingrediente** | "Los datos son el ingrediente más importante"; la calidad se juzga por contenido de señal respecto al objetivo (§1.3) | Curación como estación propia; point-in-time obligatorio (§1.4) | "El mercado descuenta todo" → basta el precio (§1.2) | **`[TENSIÓN]` leve.** Murphy justifica filosóficamente la suficiencia del precio; las otras dos no la sostienen. Ver §7 |
| **OHLCV** | Trabaja con OHLCV+ y documenta lo que falta (quotes, order flow) (§3.6) | Filtro explícito: el núcleo metodológico es `OHLCV-OK`; se pierden barras de información y microestructura (§3.4) | Casi todo su aparato es `OHLCV-OK`; cuatro renuncias externas documentadas (§27) | **`[CONSENSO FUERTE]`** de que OHLCV **permite investigación seria pero restringe qué hipótesis son testables**. Ver §9 |
| **Instrumento único** | **No formula recomendación explícita contra él.** Su aparato es cross-sectional y sus métricas (IC, breadth, quantiles) presuponen universo; registra el instrumento único como caso no cubierto (§0.4, §22-D) | **Recomendación explícita**: modelar clases de activos o universos, no valores individuales; prefiere features stacking (§0.4, §28-E) | **Criterio explícito de robustez**: estabilidad entre mercados; descarta sistemas que no la cumplen (§20.C.5) | **`[TENSIÓN]` estructural conjunta, por tres vías distintas.** Sección propia: §8 |
| **Frecuencia / intradía** | Afirma que las estrategias algorítmicas rinden mejor a mayor frecuencia; su único ejemplo intradiario no fue backtesteado con costes (§20.2) | Marco agnóstico a la frecuencia; ejemplos mayoritariamente diarios o dollar bars (§28) | Tres advertencias de que el intradía es más difícil y subordinado; "la aleatoriedad es un fenómeno de muy corta duración" (§8.5, §16.8) | **`[TENSIÓN]`.** Ver §7.2. Queda `[PREGUNTA EMPÍRICA]` |
| **Muestreo** | Usa barras temporales en todo el libro; presenta las alternativas y no las compara (§5.3) | Crítica frontal al reloj cronológico; jerarquía tick→volumen→dólar→información (§3.1) | Indiferente a la construcción del gráfico; el P&F muestrea por movimiento de precio (§11.1) | **`[CONVERGENCIA]` parcial + `[DECISIÓN DE DISEÑO ABIERTA]`.** Ver §7.7 |
| **Futuros / rollover** | No trata futuros; sólo corporate actions de acciones (§22-D) | Método de gaps acumulados; precios rolados para PnL, crudos para sizing (§4.2) | Cuatro tipos de contrato continuo; renovación por erosión de volumen; advertencia de liquidez (§8.2) | **`[COMPLEMENTARIEDAD]`.** LdP aporta el método de ajuste, Murphy el criterio de renovación. **`[VACÍO]` compartido**: efecto sobre el volumen en transición |
| **Estacionariedad** | Precios no estacionarios; random walk; ADF; transformaciones (§3.3) | Dilema estacionariedad ↔ memoria; fracdiff con `d*` mínimo (§9) | No trata el concepto; su equivalente es la "tendencia" (§4) | **`[COMPLEMENTARIEDAD]`.** LdP resuelve un problema que Jansen plantea. Murphy es ajeno al marco |
| **Volatilidad** | Heterocedasticidad; GARCH; único momento tratado como predecible (§11.7) | Umbrales de etiquetado escalados por volatilidad; estimador High-Low superior al de cierres (§23.2) | ATR, ancho de banda, alternancia expansión/contracción como hipótesis (§9.6, §20.A.3) | **`[CONSENSO FUERTE]`** de que la volatilidad es **la variable de estado más tratable** y que los umbrales deben escalarse por ella |
| **Tendencia** | Momentum como familia de factores con racional conductual y microestructural (§6.2) | No la trata como concepto; su equivalente es la explosividad/SADF (§21) | Definición operativa (HH/HL), tres escalas, y tendencialidad medible (ADX, coef. de eficiencia) (§4, §9.10, §15.4) | **`[CONVERGENCIA]` sobre la existencia del fenómeno; `[COMPLEMENTARIEDAD]` sobre su medición.** Ver §4.A |
| **Momentum** | Factor canónico con dos racionales (infra/sobrerreacción; microestructura) (§6.2) | No lo trata explícitamente | Cuatro familias de osciladores reducibles a menos (§10.11) | **`[COMPLEMENTARIEDAD]`.** Jansen aporta el racional, Murphy el inventario y su redundancia |
| **Reversión** | Factor valor y reversión a la media (requiere fundamentales) (§6.2) | Proceso tipo Ornstein-Uhlenbeck en el backtesting sintético (§17) | Osciladores en rango; STARC; retrocesos (§6.6, §10.14) | **`[CONVERGENCIA]` débil.** Los tres mecanismos son distintos. Ver §5.2 |
| **Volumen** | Feature disponible; poco desarrollado como fuente propia | Lambda de Amihud aproximable; VPIN y flujo firmado no disponibles (§23) | Indicador secundario que confirma pero no señala; "el volumen precede al precio" (§7.2) | **`[CONSENSO FUERTE]`** de que el volumen agregado **no es order flow** y de que su papel es de confirmación. La afirmación de precedencia queda `[HIPÓTESIS CANDIDATA]` |
| **Soportes / resistencias** | No los trata | No los trata; su análogo son las rupturas estructurales (§21.1) | Mecanismo psicológico completo: cuatro grupos, cambio de polaridad, margin call (§4.4) | **`[COMPLEMENTARIEDAD]` fuerte.** Murphy aporta el mecanismo que LdP exige y no proporciona. Pero ver §5.3 (falsa convergencia con structural breaks) |
| **Patrones** | No los trata | No los trata | Catálogo completo con ≥9 grados de libertad; el autor admite que en futuros se completan menos (§5, §6) | **`[DESCARTABLE METODOLÓGICAMENTE]`** en su forma nominal; **`[HIPÓTESIS CANDIDATA]`** en su forma componencial (compresión → ruptura) |
| **Regímenes** | Cambios de distribución y no estacionariedad; sin método de detección (§3.3) | Structural breaks: CUSUM, SADF, tests sub/super-martingala (§21) | Cuatro formulaciones de la hipótesis de régimen; ADX como discriminador causal; estimación del 30% (§9.12, §15.3) | **`[CONVERGENCIA]` fuerte y probablemente el hallazgo más importante de la síntesis.** Ver §4.B |
| **Multitemporalidad** | Múltiples horizontes de forward return comparados por IC (§9.1) | No la trata explícitamente | Top-down explícito: escala larga = dirección, corta = timing; filtro semanal + disparo diario (§8.4, §10.15) | **`[COMPLEMENTARIEDAD]`.** Jansen la usa para elegir target; Murphy para estructurar la decisión. **Son usos distintos** |
| **Eventos** | No aborda la detección de eventos como formulación (§8.5) | Muestreo por eventos con CUSUM; reformula la pregunta predictiva (§5.1) | Rupturas, huecos, días de cambio, pivotes intradía como eventos discretos (§4.15, §16.9) | **`[COMPLEMENTARIEDAD]` fuerte.** LdP aporta el marco, Murphy los candidatos, Jansen el vacío que ambos llenan |
| **Feature engineering** | "A menudo el ingrediente más importante"; catálogo amplio (§6.3) | Fracdiff, entropía, microestructura; features como objeto de investigación (§9, §22) | Ocho familias informativas derivadas de decenas de indicadores (§22.2) | **`[CONSENSO FUERTE]`** de que las features son el objeto central de la investigación |
| **Redundancia** | PCA, mutual information, IC, SHAP; MI e IC correlacionan sólo ~0.16 (§7.2) | Efectos de sustitución; MDI/MDA/SFI; ortogonalización (§12.3) | Reducción explícita a familias; `%R = 100 − %K` (§10.11, §22) | **`[CONSENSO FUERTE]`.** Ver §4.D |
| **Causalidad / look-ahead** | Point-in-time; look-ahead como pitfall central (§15.4) | Purging, embargo, y advertencia sobre early stopping (§11) | Escala de cuatro niveles; el problema de pivotes como línea divisoria del libro (§0.3, §4.7) | **`[CONSENSO FUERTE]`** y **`[RESTRICCIÓN METODOLÓGICA]`** de primer orden. Ver §13 |
| **Targets** | Forward returns multi-horizonte; sin teoría del labeling (§9.3) | Triple barrera; ocho configuraciones; crítica al horizonte fijo (§6) | Stop implícito por margin call; risk/reward; salidas > entradas (§16.4, §20.C.3) | **`[COMPLEMENTARIEDAD]` + `[TENSIÓN]`.** Ver §7.6 |
| **Labeling** | **`[VACÍO]` declarado** (§9.3) | Teoría completa (§6, §7) | Aporta el racional del stop implícito | **`[COMPLEMENTARIEDAD]` fuerte** — LdP cierra el mayor vacío de Jansen |
| **Solapamiento** | Reconoce el problema, no lo resuelve (§15.3) | Concurrencia, unicidad media, sequential bootstrap (§8) | No lo trata | **`[COMPLEMENTARIEDAD]` fuerte** |
| **Sample weights** | No los trata | Atribución de retornos, time decay sobre unicidad acumulada, class weights (§8.7-8.9) | No los trata | **Aportación exclusiva de LdP** |
| **NO TRADE / abstención** | Umbral de decisión optimizable según costes y beneficios (§8.3) | Tres mecanismos; desaconseja la clase neutra explícita (§7.5) | Abstención por régimen lateral; umbrales asimétricos de salida (§4.1, §9.8) | **`[TENSIÓN]` productiva.** Seis mecanismos distintos. Ver §7.5 |
| **Probabilidad / confianza** | Los clasificadores no producen probabilidades calibradas (§8.7) | Estadístico z contra hipótesis nula; sizing continuo (§14.3) | No produce probabilidades en ningún momento (§27.1) | **`[VACÍO]` compartido sobre calibración.** LdP aporta el mecanismo, nadie la calibración |
| **Sizing** | No lo desarrolla (§22-D) | Cadena completa: probabilidad → z → tamaño → promediado → discretización (§14) | "Tan importante como el propio sistema"; reglas normativas sin derivar (§16.2, §16.3) | **`[CONVERGENCIA]` sobre la importancia; `[COMPLEMENTARIEDAD]` sobre el método** |
| **Modelos** | Catálogo amplio con supuestos y limitaciones (§10) | Deliberadamente agnóstico; sólo configuración de ensembles (§10) | No trata ML | **`[CONSENSO FUERTE]`** de que **no puede elegirse a priori** (*no free lunch*) |
| **Complejidad** | El ruido domina sobre las decisiones de arquitectura (R²≈0 en su experimento de redes) (§13.2) | Bagging preferible a boosting por asimetría del riesgo; parsimonia (§10.5) | "Optimizar lo menos posible; pocos parámetros"; "lo más complicado no siempre es mejor" (§20.C.3) | **`[CONSENSO FUERTE]`** sobre el principio de mínima complejidad |
| **Interpretabilidad** | SHAP, permutación, partial dependence (§19) | MDI/MDA/SFI; concordancia PCA↔importancia como evidencia confirmatoria (§12.5) | El gráfico como interpretación visual; irreproducible (§1.7) | **`[TENSIÓN]` leve** sobre qué constituye interpretación válida; `[CONSENSO]` sobre su necesidad |
| **Validación** | Tres particiones; hold-out de un solo uso; CV asume IID y finanzas no lo es (§15) | Purged K-Fold, embargo, CPCV, CSCV/PBO (§11, §16) | Estabilidad paramétrica y temporal; **el apéndice C rechaza el out-of-sample** (§20.C.5) | **`[TENSIÓN]` + `[CONTRADICCIÓN INTERNA]` en Murphy.** Ver §7.3 |
| **Purging** | Lo nombra y atribuye a LdP sin desarrollarlo (§15.3) | Criterio formal completo (§11.3) | No lo trata | **`[COMPLEMENTARIEDAD]` fuerte** |
| **Embargo** | Idem | Asimetría justificada; ~1% de la muestra (§11.4) | No lo trata | **`[COMPLEMENTARIEDAD]` fuerte** |
| **Multiple testing** | Longitud mínima de backtest; deflated Sharpe; regla de parada 1/e (§15.5) | ~20 iteraciones bastan para un falso descubrimiento; DSR; CSCV/PBO (§15) | **Concepto ausente en 547 páginas** (§27.1) | **`[CONSENSO FUERTE]` entre Jansen y LdP; `[VACÍO]` en Murphy.** Ver §15 |
| **Backtest** | Vectorizado vs event-driven; catálogo de pitfalls (§17) | "No es una herramienta de investigación"; "un backtest impecable probablemente esté equivocado" (§15) | Paso 4 de 5 del plan; excluye costes de las pruebas (§20.C.6) | **`[TENSIÓN]`.** Ver §7.3 |
| **Costes** | Los invoca constantemente; omite el cálculo en su ejemplo intradiario (§20.2) | Rendimiento por turnover; retorno sobre costes de ejecución (§18.4) | "El promedio por operación debe cubrir los costes"; pero los excluye de las pruebas (§20.C.6) | **`[CONSENSO FUERTE]` sobre su carácter decisivo; `[TENSIÓN]` sobre cuándo aplicarlos** |
| **Evidencia económica** | Alpha 054: IC significativo con retorno acumulado negativo (§7.6) | Precisión + frecuencia + estructura de pagos; probabilidad de fracaso (§19) | 40% de acierto compatible con rentabilidad si los pagos son asimétricos (§16.4) | **`[CONSENSO FUERTE]`: predicción estadística ≠ rentabilidad.** Ver §3.1 |
| **Despliegue / monitorización** | Factor decay; necesidad de monitorización sin método (§21-H4) | Ciclo de vida completo, sin protocolo de monitorización (§28-G) | Las relaciones cambian con el régimen; sin protocolo (§17.1) | **`[VACÍO]` compartido** |

---

# §3. PRINCIPIOS QUE SOBREVIVEN A LAS TRES FUENTES

El encargo pide **no declarar automáticamente** estos principios, sino verificar su respaldo real. Procedo caso por caso. Los principios se ordenan por solidez, no por importancia.

## 3.1 `[CONSENSO FUERTE]` — Predicción estadística ≠ rentabilidad

**Respaldo:** las tres fuentes, por vías independientes y con evidencia de tipos distintos.
- `[JANSEN]` Alpha 054 en el apéndice: IC significativo de 0.025, spread positivo entre quintiles, **retornos acumulados negativos** (`KB01 §7.6`). Es una demostración empírica, no un argumento.
- `[LDP]` El Sharpe depende de precisión, frecuencia **y estructura de pagos**: con 260 apuestas anuales, stop −1% y objetivo +0.5%, una precisión de 0.70 da Sharpe 1.17 y una de 0.67 lo anula (`KB02 §19.4`).
- `[MURPHY]` "Es posible estar en la dirección correcta del mercado y perder dinero igualmente"; y los mejores operadores de futuros ganan sólo en el 40% de sus operaciones (`KB03 §1.5, §16.4`).

**Objeción pendiente:** ninguna. Las tres coinciden en el contenido y ninguna lo matiza.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** Ninguna métrica de clasificación o de correlación puede usarse como evidencia de viabilidad sin traducción económica.

---

## 3.2 `[CONSENSO FUERTE]` — Causalidad temporal estricta y control de leakage

**Respaldo:**
- `[JANSEN]` Point-in-time obligatorio; look-ahead como pitfall central; advertencia explícita sobre early stopping que usa datos futuros (`KB01 §15.4, §13.1`).
- `[LDP]` Purging y embargo con criterio formal; **la fuga en presencia de features irrelevantes es lo que produce falsos descubrimientos** (`KB02 §11.2`).
- `[MURPHY]` "El chartista sólo puede estar razonablemente seguro de que se ha formado un mínimo de reacción después de que los precios hayan comenzado a subir desde él" (`KB03 §4.7`) — reconocimiento del problema desde una tradición que ni siquiera lo llama así.

**Objeción pendiente:** ninguna sobre el principio. Sí sobre su alcance: Murphy no extrae la consecuencia metodológica, sólo constata el hecho.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** Es la restricción de primer orden. Desarrollada en §13.

---

## 3.3 `[CONSENSO FUERTE]` — Las observaciones financieras no son independientes, y el número de filas no es el tamaño muestral

**Respaldo:**
- `[JANSEN]` La CV asume IID y los datos financieros no lo son, por correlación serial y heterocedasticidad (`KB01 §15.1`).
- `[LDP]` Formalización completa: concurrencia, unicidad media, y la cuantificación de que con etiquetas de 100 barras debería muestrearse ~1% de las observaciones por estimador (`KB02 §8.4`).
- `[MURPHY]` No lo trata. **No hay objeción, hay silencio.**

**Naturaleza del respaldo:** dos de tres, con la tercera muda. Pero la afirmación de LdP es formal y la de Jansen es explícita; no hay contradicción posible desde Murphy porque el marco le es ajeno.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** Con la matización de que el valor concreto de la unicidad media en MNQ es `[PREGUNTA EMPÍRICA]` (G1).

---

## 3.4 `[CONSENSO FUERTE]` — Necesidad de baselines y de valor incremental demostrado

**Respaldo:**
- `[JANSEN]` *No free lunch*; un modelo complejo aprende ruido si la relación es simple; en su propio experimento de redes, el R² de la arquitectura sobre el IC fue ≈0 (`KB01 §10.9, §13.2`).
- `[LDP]` Agnosticismo declarado sobre el algoritmo; el test del bagging como diagnóstico de sobreajuste (`KB02 §15.4`).
- `[MURPHY]` "Optimizar lo menos posible"; "lo más complicado no siempre es mejor"; y la ausencia de evidencia de que las EMA superen a las SMA (`KB03 §20.C.3, §9.3`).

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** Toda complejidad adicional debe demostrar valor incremental frente a una alternativa más simple, medido fuera de muestra.

---

## 3.5 `[CONSENSO FUERTE]` — Los costes y la ejecución forman parte de la viabilidad, no del cierre

**Respaldo:**
- `[JANSEN]` Los mercados no permiten ejecutar todo al precio objetivo; su ejemplo intradiario con edge de 0.5 pb/min **no fue backtesteado con costes** (`KB01 §20.2`).
- `[LDP]` Rendimiento en dólares por turnover y retorno sobre costes de ejecución como métricas primarias (`KB02 §18.4`).
- `[MURPHY]` "El promedio por operación debe ser suficiente para cubrir los costes, porque si no, perderemos dinero" (`KB03 §20.C.6`).

**Objeción pendiente:** `[CONTRADICCIÓN INTERNA]` en Murphy — el mismo apéndice que exige que el promedio cubra costes los excluye de las pruebas por "pureza". Ver §7.3.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ**, en la forma: *ninguna afirmación de viabilidad es válida sin costes modelados*. La cuestión de **cuándo** aplicarlos durante la investigación queda `[DECISIÓN DE DISEÑO ABIERTA]`.

---

## 3.6 `[CONSENSO FUERTE]` — Redundancia informativa y efectos de sustitución

**Respaldo:**
- `[JANSEN]` MI e IC discrepan (correlación de rangos ~0.16); las métricas de importancia no son intercambiables (`KB01 §7.2, §7.5`).
- `[LDP]` Efectos de sustitución: la importancia se reparte arbitrariamente entre features correlacionadas (`KB02 §12.3`).
- `[MURPHY]` "Casi todos los osciladores se parecen mucho"; `%R = 100 − %K` (`KB03 §10.2, §10.9`).

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** La importancia de features no puede interpretarse sin controlar previamente la redundancia. Desarrollado en §4.D y §11.

---

## 3.7 `[CONVERGENCIA]` — Registro de intentos y control del multiple testing

**Respaldo:**
- `[JANSEN]` 2 años de datos diarios no sostienen conclusiones sobre más de ~7 estrategias; 5 años, ~45. Deflated Sharpe. Regla de parada 1/e (`KB01 §15.5`).
- `[LDP]` ~20 iteraciones bastan para un falso descubrimiento al 5%; el DSR es **incalculable sin registro de intentos** (`KB02 §15.3, §18.5`).
- `[MURPHY]` **Concepto ausente.** No aparece en 547 páginas (`KB03 §27.1`).

**Por qué `[CONVERGENCIA]` y no `[CONSENSO FUERTE]`:** dos fuentes coinciden con fuerza, pero **la tercera no sólo calla: presenta decenas de indicadores parametrizables sin ninguna contabilidad**, y su apéndice metodológico rechaza el out-of-sample. No es silencio neutral, es una práctica opuesta.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ**, sobre la base de Jansen + LdP, y **registrando explícitamente que Murphy es una fuente que, seguida literalmente, la violaría**. Desarrollado en §15.

---

## 3.8 `[CONVERGENCIA]` — Necesidad de un mecanismo económico o conductual

**Respaldo:**
- `[JANSEN]` Priorizar estrategias con justificación económica antes de testear; elegir hipótesis por data-mining multiplica los falsos descubrimientos (`KB01 §1.2`).
- `[LDP]` La teoría debe identificar **el mecanismo por el que un agente nos pierde dinero**; pero las features pueden descubrirse en caja negra (`KB02 §1.7`).
- `[MURPHY]` "Si un sistema parece que funciona bien pero tiene poco sentido para usted, posiblemente se trate de una coincidencia" (`KB03 §20.C.3`).

**Por qué `[CONVERGENCIA]` y no `[CONSENSO FUERTE]`:** **las tres exigen mecanismo, pero en momentos distintos del proceso.** Ver §6.1, donde se examina si esto es contradicción o división de fases. La formulación consensuada es más débil que la de cualquiera de ellas por separado: *ninguna señal debe convertirse en estrategia sin un mecanismo propuesto*, sin pronunciarse sobre si el mecanismo debe preceder al descubrimiento.

---

## 3.9 `[CONVERGENCIA]` — Estabilidad temporal como criterio de validez

**Respaldo:**
- `[JANSEN]` Factor decay: los excesos de retorno caen ~25% desde el descubrimiento y >50% tras la publicación; la premisa de que la psicología no cambia debe comprobarse, no suponerse (`KB01 §6.1`).
- `[LDP]` Structural breaks; las relaciones aprendidas se degradan; el ciclo de vida contempla el desmantelamiento (`KB02 §21`).
- `[MURPHY]` Estabilidad temporal como uno de los tres criterios de robustez; las relaciones intermercado cambian con el régimen; las duraciones cíclicas "cambian continuamente" (`KB03 §20.C.5, §17.1`).

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ**, en la forma: *un resultado debe evaluarse por su estabilidad entre períodos y regímenes, no sólo por su valor agregado*.

---

## 3.10 `[CONVERGENCIA]` — Separación entre investigación y backtest

**Respaldo:**
- `[JANSEN]` El propósito del backtest es descartar modelos, no mejorarlos; no hacer backtest hasta que el modelo esté especificado (`KB01 §17.1` — recogido de su tratamiento de pitfalls).
- `[LDP]` "El backtesting no es una herramienta de investigación; la importancia de features sí lo es"; "investigar bajo la influencia de un backtest es como conducir bebido" (`KB02 §1.5`).
- `[MURPHY]` El backtest es el paso 4 de 5, posterior a la formulación completa de las reglas (`KB03 §20.C.2`).

**Por qué `[CONVERGENCIA]`:** las tres separan las fases, pero **sólo LdP la eleva a prohibición**. Murphy admite verificación visual previa (paso 3), que es una forma de mirar los datos antes de codificar.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ**, con la formulación mínima común: *el backtest se ejecuta sobre un sistema completamente especificado, y sus resultados no se usan para redefinir el sistema sin contabilizar el intento*.

---

## 3.11 `[CONSENSO FUERTE]` — El ratio señal/ruido es bajo y ése es el hecho definitorio del dominio

**Respaldo:**
- `[JANSEN]` Característica definitoria; obliga a emparejar complejidad de modelo y complejidad de datos (`KB01 §3.1`).
- `[LDP]` Consecuencia de las fuerzas de arbitraje; agravado por series cortas y ausencia de laboratorio (`KB02 §1.1`).
- `[MURPHY]` "Existe cierta cantidad de aleatoriedad o ruido en todos los mercados" — aunque lo minimiza (`KB03 §1.8`).

**Matización necesaria:** Murphy lo reconoce pero **sostiene que la aleatoriedad es un fenómeno de corto plazo**, lo cual es una afirmación distinta y adversa a nuestro horizonte. Ver §7.2.

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ** en la forma general (esperar edges pequeños e inestables); la afirmación sobre su distribución por horizonte queda `[PREGUNTA EMPÍRICA]`.

---

## 3.12 `[CONVERGENCIA]` — Tratamiento explícito del rollover

**Respaldo:**
- `[JANSEN]` No trata futuros; su análogo son las corporate actions, que exige ajustar antes de la ingesta (`KB01 §3.7`).
- `[LDP]` Método de gaps acumulados; los eventos que alteran la naturaleza de la serie **introducen rupturas estructurales que desvían la investigación** (`KB02 §4.1`).
- `[MURPHY]` Cuatro tipos de contrato continuo; el problema aparece "cuando un analista está probando un modelo con información de muchos años" (`KB03 §8.2`).

**Elevación a `[RESTRICCIÓN METODOLÓGICA]`: SÍ.** El tratamiento del rollover es preprocesado obligatorio, no una opción. **El método concreto queda `[DECISIÓN DE DISEÑO ABIERTA]` (A1).**

---

## 3.13 Principios que NO alcanzan el umbral

El encargo pide ser conservador. Estos candidatos **no** se elevan:

| Candidato | Por qué no |
|---|---|
| **"Los precios se mueven en tendencias"** | Sólo Murphy lo sostiene como premisa. Jansen lo trata como un factor entre varios con racional discutido; LdP no lo aborda. Y la versión débil es tautológica. **Queda `[HIPÓTESIS CANDIDATA]`** |
| **"El muestreo cronológico es inadecuado"** | Sólo LdP lo argumenta. Jansen usa barras temporales en todo su libro sin objeción; Murphy es indiferente. **Queda `[DECISIÓN DE DISEÑO ABIERTA]`** |
| **"El etiquetado debe depender del camino"** | Sólo LdP lo desarrolla. Murphy aporta el racional del stop implícito pero no un método; Jansen usa horizonte fijo universalmente. **`[TENSIÓN]`, ver §7.6** |
| **"La abstención debe existir"** | Las tres la contemplan pero **por mecanismos incompatibles**, y LdP desaconseja la clase explícita. **`[TENSIÓN]` productiva, ver §7.5** |
| **"El bagging es preferible al boosting"** | Sólo LdP, y lo presenta como argumento, no como evidencia. Contradice la práctica dominante. **`[PREGUNTA EMPÍRICA]`** |
| **"La volatilidad es predecible"** | Jansen lo sostiene (GARCH); LdP lo usa instrumentalmente; Murphy describe alternancia sin medirla. **`[HIPÓTESIS CANDIDATA]` fuerte, no principio** |
| **"Existe predictibilidad explotable"** | **Ninguna fuente lo afirma para ningún instrumento concreto.** `[PREGUNTA EMPÍRICA]` terminal |
| **"El instrumento único es inviable"** | **Sólo LdP lo desaconseja explícitamente**; Murphy exige estabilidad entre mercados como criterio de descarte; Jansen no formula recomendación, pero su aparato lo presupone. **Ninguna demuestra que sea inválido.** Es prudencia y dependencia metodológica, no un teorema. **`[TENSIÓN]`, ver §8** |

`[SÍNTESIS — INTERPRETACIÓN]` **Doce principios sobreviven; ocho candidatos plausibles no lo hacen.** La proporción es informativa: lo que las tres fuentes establecen conjuntamente es **casi enteramente metodológico y negativo** —cómo no engañarse— y casi nada sustantivo sobre cómo se comportan los mercados. **La bibliografía nos dice cómo investigar, no qué encontraremos.**

---

# §4. CONVERGENCIAS ENTRE FUENTES

Investigación de las cuatro convergencias que el encargo señala, **sin asumir previamente que sean válidas**.

## 4.A Mecanismos de tendencia y momentum

**Las tres posiciones:**

| Fuente | Formulación | Mecanismo propuesto | Observable |
|---|---|---|---|
| `[JANSEN]` | Momentum como familia de factores con correlación serial positiva (`KB01 §6.2`) | **Dos racionales distintos**: (a) conductual — infrarreacción y sobrerreacción a noticias, miedo y codicia; (b) **microestructural** — stops, CPPI, delta hedging y rebalanceo de risk parity **crean** momentum mecánicamente en horizontes intradiarios | Retornos pasados de distintas escalas |
| `[MURPHY]` | Premisa 2: una tendencia en movimiento es más probable que continúe (`KB03 §1.3`) | **Inercia por analogía newtoniana**, sin mecanismo de mercado en el capítulo. El mecanismo aparece disperso: participantes atrapados en niveles, margin call (`KB03 §4.4`) | Secuencia HH/HL; ADX; coeficiente de eficiencia |
| `[LDP]` | No trata "tendencia". Su análogo es la **explosividad**: crecimiento inconsistente con random walk (`KB02 §21`) | **Participantes atrapados en el lado perdedor que actúan irracionalmente antes de aceptar pérdidas**, y eventualmente son forzados a salir | SADF, tests sub/super-martingala, CUSUM |

**¿Son la misma hipótesis?**

`[SÍNTESIS — INTERPRETACIÓN]` **No. Son al menos tres hipótesis distintas que comparten un observable parcial.** El análisis:

1. **El racional conductual de Jansen (infra/sobrerreacción) y la inercia de Murphy son compatibles pero no idénticos.** El primero explica por qué el precio *tarda* en incorporar información; el segundo afirma que el movimiento se autoperpetúa. Son mecanismos distintos con la misma consecuencia observable.

2. **El racional microestructural de Jansen y el de participantes atrapados de LdP/Murphy son casi el mismo mecanismo.** Ambos describen **flujo forzado**: órdenes que se ejecutan no por convicción sino por compromiso previo (stops, delta hedging, rebalanceo) o por incapacidad de financiar (margin call). **Ésta es la convergencia real y es fuerte** — llega desde tres tradiciones independientes.

3. **Pero la escala difiere.** Jansen lo sitúa explícitamente en horizontes intradiarios (`KB01 §4`); Murphy en cualquier escala; LdP en transiciones de régimen sin especificar duración.

**Conclusión:**

`[CONVERGENCIA]` **fuerte y específica** sobre el **mecanismo de flujo forzado**: existen participantes cuyas órdenes están comprometidas de antemano o son involuntarias, y su ejecución produce movimiento no informacional. Trazabilidad: `KB01 §4` + `KB02 §21.1` + `KB03 §4.4`.

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Esta convergencia tiene tres propiedades valiosas: **(a) no requiere universo multiactivo**; **(b) es específicamente más fuerte en instrumentos apalancados** —que es MNQ—; **(c) predice condiciones observables**: el flujo forzado debería concentrarse cerca de niveles donde hubo acumulación previa de posiciones y tras movimientos que las pongan en pérdida. **Es la hipótesis con mejor respaldo cruzado de toda la síntesis.**

`[SÍNTESIS — INTERPRETACIÓN]` Y una advertencia: **"momentum" como familia de indicadores no es lo mismo que este mecanismo.** Un ROC de 14 barras mide variación de precio; el mecanismo predice algo más específico y condicional. Confundirlos sería tratar el indicador como si heredara el respaldo del mecanismo.

---

## 4.B Regímenes

**Las tres posiciones:**

| Fuente | Formulación | Cómo se detecta | Qué implica |
|---|---|---|---|
| `[MURPHY]` | Tendencia vs lateralidad; **cuatro formulaciones independientes** en capítulos distintos (`KB03 §9.12, §10.1, §14.6, §15.4`). Estimación de Wilder: ~30% del tiempo en tendencia | **ADX**, causal, un parámetro; coeficiente de eficiencia | **La herramienta apropiada depende del estado**: medias en tendencia, osciladores en rango |
| `[JANSEN]` | Cambios de distribución, no estacionariedad, cambios estructurales (`KB01 §3.3`) | **Sin método propio**; reconoce el problema y no lo resuelve | Las relaciones aprendidas se degradan |
| `[LDP]` | Structural breaks como oportunidad de riesgo/recompensa favorable (`KB02 §21`); muestreo por eventos que reformula la pregunta predictiva (`KB02 §5.1`) | CUSUM, SADF, tests SM, Brown-Durbin-Evans | **"¿Hay alguna condición bajo la cual el mercado sea predecible?"** |

**¿Existe una estructura común?**

`[SÍNTESIS — INTERPRETACIÓN]` **Sí, y es probablemente el hallazgo más importante de esta síntesis**, pero hay que enunciarlo con precisión porque los tres hablan de cosas parcialmente distintas:

- **Murphy habla de un estado persistente** (el mercado *está* en tendencia o en rango) que condiciona qué herramienta funciona.
- **LdP habla de una transición** (el momento en que el régimen cambia) como oportunidad.
- **Jansen habla del problema** (las relaciones no son estables) sin proponer solución.

**Son tres aspectos del mismo fenómeno**: estado, transición y consecuencia sobre la validez del modelo.

**La estructura común que emerge:**

```
El mercado ocupa estados distinguibles.
        ↓
La relación entre features y retorno futuro DEPENDE del estado.
        ↓
Por tanto: (a) un modelo no condicionado promedia relaciones contradictorias;
           (b) las transiciones entre estados son en sí mismas informativas;
           (c) la validez de cualquier hallazgo es condicional al estado.
```

**Estatus:** `[CONVERGENCIA]` fuerte. **No `[CONSENSO FUERTE]`** porque ninguna fuente demuestra que los regímenes sean identificables causalmente ni que la condicionalidad mejore la predicción — Murphy lo afirma sin medirlo, LdP ofrece detectores sin evidencia de utilidad, Jansen sólo constata el problema.

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Tres consecuencias:
1. **La identificación del régimen podría ser el problema principal, no un refinamiento.** Si la estimación del 30% es aproximadamente correcta, una herramienta direccional fallaría la mayor parte del tiempo (`KB03 §15.3`).
2. **Conecta directamente con la abstención** (§7.5): "no operar" puede ser una función del estado, no de la confianza del modelo.
3. **Es `OHLCV`-compatible en su totalidad**: ADX, coeficiente de eficiencia, ancho de banda de volatilidad y CUSUM son todos construibles y causales.

**Queda como `[HIPÓTESIS CANDIDATA]` de máxima prioridad y `[PREGUNTA EMPÍRICA]` (K1, K2, K3).**

---

## 4.C Soporte/resistencia y rupturas estructurales

**Las dos posiciones relevantes** (Jansen no trata ninguna de las dos):

| Fuente | Objeto | Mecanismo | Observable | Escala |
|---|---|---|---|---|
| `[MURPHY]` | Nivel de precio con memoria (`KB03 §4.4`) | **Cuatro grupos de participantes** con interés en el nivel: largos que quieren añadir, cortos que quieren salir en su punto de entrada, quienes liquidaron prematuramente, e indecisos. Al perforarse, las órdenes de compra se transforman en órdenes de venta. **Margin call como forzador** | Reaproximación del precio a un nivel donde hubo actividad previa | Cualquiera; sus ejemplos son diarios y semanales |
| `[LDP]` | Ruptura estructural (`KB02 §21.1`) | **Participantes atrapados en el lado perdedor** que actúan irracionalmente, mantienen la posición esperando recuperación, a veces la aumentan, y finalmente son forzados a cortar | Comportamiento explosivo del **proceso de precios**, no de un nivel | Transiciones de régimen |

**¿Dónde hay convergencia y dónde empieza la interpretación?**

`[SÍNTESIS — INTERPRETACIÓN]` **La convergencia es sobre el mecanismo psicológico-financiero, no sobre el objeto observado.** Con precisión:

**Convergen en:** la existencia de participantes con posiciones perdedoras cuya salida es forzada o inevitable, y en que esa salida produce movimiento. **Las descripciones son casi intercambiables** — ambas describen la misma secuencia: negación, esperanza, presión, liquidación.

**Divergen en el observable:**
- Murphy observa **un nivel de precio** definido por actividad histórica. Su predicción es *espacial*: el efecto ocurre cuando el precio vuelve a ese lugar.
- LdP observa **una propiedad del proceso** (explosividad medida por SADF). Su predicción es *dinámica*: el efecto se manifiesta como cambio en el comportamiento estadístico de la serie.

**Divergen en la condición de falsación:**
- Murphy: *el precio se comporta anómalamente al reaproximarse a niveles con actividad previa*. Falsable comparando el comportamiento cerca y lejos de tales niveles.
- LdP: *el proceso exhibe comportamiento inconsistente con random walk en ciertos períodos*. Falsable con un test estadístico sobre la serie completa.

**Estatus:** `[CONVERGENCIA]` sobre el **mecanismo**; **`[SÍNTESIS — INTERPRETACIÓN]`** cualquier afirmación de que sean el mismo fenómeno. Ver §5.3, donde se examina si tratarlos como equivalentes sería una falsa convergencia.

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Lo aprovechable es que **el mecanismo común genera predicciones distintas y ambas son testables por separado con OHLCV**. No hay que elegir: son dos hipótesis derivadas del mismo racional, y su confirmación conjunta sería mucho más informativa que la de cualquiera por separado. **Pero medir una no es evidencia sobre la otra.**

---

## 4.D Redundancia y principio de investigación de features

**Las tres posiciones:**

| Fuente | Aportación |
|---|---|
| `[MURPHY]` | **Reducción constructiva**: decenas de indicadores se reducen a ocho familias informativas; el propio autor declara que "casi todos los osciladores se parecen mucho" y que `%R` es el estocástico invertido (`KB03 §10.11, §22.2`) |
| `[LDP]` | **Diagnóstico del daño**: los efectos de sustitución hacen que la importancia estimada se reduzca por la presencia de features relacionadas; la ortogonalización sólo mitiga sustituciones **lineales** (`KB02 §12.3, §12.5`) |
| `[JANSEN]` | **Instrumental de medición**: IC, mutual information, feature importance, permutación, SHAP, PCA. Y el hallazgo de que **MI e IC correlacionan sólo ~0.16** al ordenar features (`KB01 §7.2, §7.5`) |

**¿Puede derivarse un principio de investigación de features?**

`[SÍNTESIS — INTERPRETACIÓN]` **Sí, y es una `[COMPLEMENTARIEDAD]` casi perfecta**: cada fuente aporta una pieza que las otras no tienen. El principio derivable:

> **PRINCIPIO DE INVESTIGACIÓN DE FEATURES**
> 1. **Antes de generar**: agrupar los candidatos por **familia informativa** (qué información económica o estadística representan), no por nombre ni por fórmula. `[MURPHY]`
> 2. **Antes de interpretar**: medir la redundancia efectiva dentro y entre familias, porque la importancia se reparte arbitrariamente entre sustitutos. `[LDP]`
> 3. **Al medir**: usar más de una métrica, sabiendo que **no son intercambiables** y que su discrepancia es en sí misma informativa. `[JANSEN]`
> 4. **Al concluir**: una feature con importancia baja no es necesariamente poco informativa; puede estar sustituida. Y una con importancia alta puede serlo por azar entre equivalentes.

**Estatus:** `[COMPLEMENTARIEDAD]` elevada a `[RESTRICCIÓN METODOLÓGICA]` en su punto 2, y a guía de proceso en el resto.

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` La consecuencia operativa es que **el espacio de features debe diseñarse por familias antes de instanciarse en indicadores** — lo contrario de generar cincuenta variables y después seleccionar. Esto reduce simultáneamente el problema de sustitución y el presupuesto de multiple testing. Desarrollado en §11.

---

# §5. FALSAS CONVERGENCIAS

El encargo pide actuar como crítico. Estos son casos donde **la coincidencia terminológica no implica coincidencia conceptual**.

## 5.1 "Descomposición del problema"

Las tres fuentes descomponen la decisión, y es tentador alinearlas:

| Fuente | Descomposición | Eje |
|---|---|---|
| `[JANSEN]` | Idea → datos → features → target → modelo → predicción → señal → regla → posición → resultado → validación | **Fases de un pipeline** |
| `[LDP]` | Side ≠ Size (`KB02 §7.1`) | **Contenido de la decisión** |
| `[MURPHY]` | Qué (análisis) / Cuándo (timing) / Cuánto (gestión monetaria) (`KB03 §16.1`) | **Preguntas de la decisión** |

`[SÍNTESIS — INTERPRETACIÓN]` **No son la misma descomposición y alinearlas mecánicamente sería un error.** El "cuándo" de Murphy **no tiene equivalente** en la dicotomía side/size de LdP: es una tercera dimensión. Y la cadena de Jansen es un flujo de trabajo, no una descomposición de la decisión.

Superponiéndolas:
- El **side** de LdP ≈ el **qué** de Murphy ≈ el eslabón *predicción→señal* de Jansen.
- El **size** de LdP ≈ el **cuánto** de Murphy ≈ el eslabón *señal→posición* de Jansen.
- El **cuándo** de Murphy **no aparece en LdP** y en Jansen está implícito en la elección de horizonte.

**Estatus:** `[COMPLEMENTARIEDAD]`, no convergencia. Murphy aporta un eje —el momento de ejecución dentro de una señal válida— que las otras dos no separan. `[DECISIÓN DE DISEÑO ABIERTA]` E3: si IRIS adopta una arquitectura de dos o de tres componentes, y con qué correspondencia.

---

## 5.2 "Reversión"

| Fuente | Objeto | Mecanismo | Escala |
|---|---|---|---|
| `[JANSEN]` | Factor **valor**: reversión hacia un valor fundamental justo (`KB01 §6.2`) | Corrección de una desviación respecto de un valor intrínseco **que requiere fundamentales** | Meses |
| `[LDP]` | Proceso con **reversión a la media** tipo Ornstein-Uhlenbeck para calibrar reglas de salida (`KB02 §17`) | Supuesto de modelado, no hipótesis de mercado | Duración de una posición |
| `[MURPHY]` | Osciladores en rango; sobrecompra/sobreventa; toque de banda STARC (`KB03 §10.14, §20.A.3`) | **Sobreextensión** respecto de un promedio reciente | Cualquiera |

`[SÍNTESIS — INTERPRETACIÓN]` **Tres conceptos distintos con la misma palabra.** El de Jansen **no es aplicable a IRIS** (requiere fundamentales y no existen para un futuro sobre índice). El de LdP es un **supuesto instrumental**, no una afirmación sobre el mercado. Sólo el de Murphy es una hipótesis testable con OHLCV — y el propio Murphy la contradice a sí mismo al presentar dos indicadores casi idénticos (STARC y Keltner) con reglas opuestas (`KB03 §20.A.3`).

**Estatus: FALSA CONVERGENCIA.** La única hipótesis de reversión utilizable es la de sobreextensión respecto de una referencia móvil, **y es exactamente la que carece de dirección estable en la propia fuente que la propone**. Esto refuerza `[HIPÓTESIS CANDIDATA]` K2: la relación cambia de signo según el régimen.

---

## 5.3 "Ruptura"

Ya analizado en §4.C. **Resumen del veredicto:**

`[SÍNTESIS — INTERPRETACIÓN]` **Convergencia real en el mecanismo, falsa convergencia en el observable.** "Ruptura de soporte" (`[MURPHY]`) es un evento **espacial** —el precio atraviesa un nivel identificado por actividad histórica— con condición de falsación local. "Structural break" (`[LDP]`) es un cambio en las **propiedades estadísticas del proceso**, detectado por tests sobre la serie, sin referencia a ningún nivel.

**Un precio puede romper un soporte sin que haya ruptura estructural, y puede haber ruptura estructural sin que se atraviese ningún nivel notable.** Tratarlos como el mismo fenómeno llevaría a usar evidencia sobre uno como respaldo del otro.

**Estatus: FALSA CONVERGENCIA en el observable.** Deben investigarse como **dos hipótesis separadas** que comparten racional.

---

## 5.4 "Tendencia"

| Fuente | Qué significa |
|---|---|
| `[MURPHY]` | **Estructura de precio**: secuencia de máximos y mínimos crecientes, sobre cierres, con retardo de pivote (`KB03 §4.1`) |
| `[JANSEN]` | **Correlación serial positiva de retornos**, medida como factor momentum sobre una ventana (`KB01 §6.2`) |
| `[LDP]` | No usa el término. Lo más próximo es la **explosividad**, que es una propiedad del proceso generador, no una dirección (`KB02 §21`) |

`[SÍNTESIS — INTERPRETACIÓN]` **La estructura HH/HL y la autocorrelación positiva no son la misma cosa.** Una serie puede tener autocorrelación positiva sin producir una secuencia limpia de pivotes crecientes, y puede tener estructura HH/HL con autocorrelación de retornos cercana a cero (si el avance ocurre en saltos discretos). **Son observables distintos con distinta sensibilidad al ruido.**

**Estatus: FALSA CONVERGENCIA parcial.** `[DECISIÓN DE DISEÑO ABIERTA]`: si "tendencia" se operacionaliza como estructura de pivotes (con `LOOK-AHEAD-LEVE`), como autocorrelación (causal), o como tendencialidad adimensional (ADX / coeficiente de eficiencia, causal). **Las tres son defendibles y no equivalentes.**

---

## 5.5 "Régimen"

| Fuente | Qué es un régimen |
|---|---|
| `[MURPHY]` | **Estado cualitativo binario o ternario**: tendencia alcista / bajista / lateral |
| `[JANSEN]` | **Distribución de los datos**: un régimen es un período con propiedades estadísticas distintas |
| `[LDP]` | **Implícito en la ruptura**: hay régimen antes y después de un break, sin caracterizarlos |

`[SÍNTESIS — INTERPRETACIÓN]` Coinciden en que existen estados distinguibles, pero **discrepan en su naturaleza**: cualitativo y observable (Murphy) frente a distribucional y latente (Jansen). Esa diferencia tiene consecuencia práctica directa: **un régimen observable se mide con un indicador; uno latente se infiere con un modelo**, y la asignación causal es un problema distinto en cada caso.

**Estatus: convergencia sobre la existencia, `[DECISIÓN DE DISEÑO ABIERTA]` sobre la naturaleza.** No es falsa convergencia, pero sí una convergencia **menos específica de lo que parece**.

---

## 5.6 "Volatilidad"

| Fuente | Uso |
|---|---|
| `[JANSEN]` | **Objeto de predicción**: la varianza condicional es predecible (GARCH); único momento tratado así |
| `[LDP]` | **Instrumento de normalización**: escala los umbrales de etiquetado; el estimador High-Low es más preciso que el de cierres |
| `[MURPHY]` | **Variable de estado**: ATR y ancho de banda; alternancia expansión-contracción como hipótesis |

`[SÍNTESIS — INTERPRETACIÓN]` **Tres usos distintos del mismo objeto, y son compatibles.** No es falsa convergencia: es un caso donde el mismo concepto cumple tres funciones no excluyentes (target, normalizador, contexto). **Merece registrarse porque la elección entre ellas es una decisión de diseño, no una cuestión de cuál es correcta.**

---

## 5.7 "Evento"

| Fuente | Qué es un evento |
|---|---|
| `[LDP]` | **Un momento seleccionado para muestrear**, definido por un filtro (CUSUM) sobre una variable acumulada. Su función es reducir el dataset a momentos potencialmente informativos (`KB02 §5.1`) |
| `[MURPHY]` | **Una configuración de precio discreta** (día de cambio, hueco, ruptura de pivote) con significado interpretativo propio |
| `[JANSEN]` | No formula la detección de eventos. Su análogo más próximo es el análisis del rendimiento de un factor durante períodos históricos concretos (`KB01 §8.5`) |

`[SÍNTESIS — INTERPRETACIÓN]` **Falsa convergencia parcial y consecuente.** El evento de LdP es un **criterio de muestreo** (cuándo mirar); el de Murphy es una **hipótesis de señal** (qué significa lo que veo). Son roles distintos y pueden combinarse —el evento de Murphy podría servir de disparador del muestreo de LdP— **pero no se sustituyen**.

**Estatus: `[COMPLEMENTARIEDAD]` si se mantienen separados; falsa convergencia si se confunden.**

---

## 5.8 "Confirmación" y "confianza"

| Término | Fuente | Significado |
|---|---|---|
| **Confirmación** | `[MURPHY]` | Que varios indicadores apunten en la misma dirección (`KB03 §6.9`) |
| **Confirmación** | `[LDP]` | La evidencia confirmatoria no supervisada: concordancia entre el ranking PCA y el de importancia (`KB02 §12.5`) |
| **Confianza** | `[LDP]` | Estadístico z de la probabilidad predicha contra la hipótesis nula (`KB02 §14.3`) |
| **Confianza** | `[MURPHY]` | Cualitativa; no produce probabilidades en ningún momento (`KB03 §27.1`) |

`[SÍNTESIS — INTERPRETACIÓN]` **Dos falsas convergencias en un mismo par de términos.**

Sobre **confirmación**: la de Murphy es acuerdo entre indicadores; la de LdP es acuerdo entre un método supervisado y uno no supervisado. **La segunda es evidencia contra el sobreajuste; la primera no**, porque si los indicadores son transformaciones de la misma información (que es lo que el propio Murphy establece en `KB03 §10.11`), su acuerdo es esperado por construcción y no aporta información independiente. **Ésta es una de las tensiones internas más consecuentes de Murphy** y ya está registrada en `KB03 §6.9`.

Sobre **confianza**: sólo LdP la define de forma medible. La de Murphy es un juicio.

**Estatus: FALSA CONVERGENCIA en ambos casos.**

---

# §6. FALSAS CONTRADICCIONES

Casos donde el conflicto aparente se disuelve al examinar el contexto.

## 6.1 Hipótesis económica primero vs descubrimiento de features primero

**El conflicto aparente:**
- `[JANSEN]` Priorizar hipótesis con justificación económica **antes de testear**; elegir por data-mining multiplica los falsos descubrimientos (`KB01 §1.2`).
- `[LDP]` **Las features pueden descubrirse en caja negra**; la teoría se construye después, entre el descubrimiento de features y la construcción de la estrategia (`KB02 §1.7`).

**¿Hablan de la misma etapa?**

`[SÍNTESIS — INTERPRETACIÓN]` **No, y ésta es una falsa contradicción.** LdP separa explícitamente **descubrimiento de features** de **descubrimiento de estrategia**, y sitúa la exigencia de teoría **entre ambos**: las features pueden hallarse sin hipótesis previa, pero **la estrategia requiere una teoría que identifique el mecanismo por el que un agente pierde dinero** (`KB02 §1.5`). Jansen no hace esa distinción y por eso su exigencia parece anterior.

**La formulación reconciliada, que respeta a ambos:**

```
Exploración de features        → puede ser agnóstica (LdP)
        ↓
Formulación de mecanismo       → OBLIGATORIA antes de estrategia (LdP + Jansen + Murphy)
        ↓
Test del mecanismo             → sobre datos que no participaron en el descubrimiento
        ↓
Estrategia
```

**Pero queda un residuo real de desacuerdo**, y conviene no borrarlo: Jansen sostiene que la exploración agnóstica **aumenta el multiple testing** y por eso desaconseja empezar por ahí. LdP acepta ese coste a cambio de no limitar el descubrimiento a lo que ya se sabía. **Es una diferencia de tolerancia al riesgo de falso descubrimiento, no de lógica.**

**Estatus:** `[COMPLEMENTARIEDAD]` con residuo. Murphy añade la tercera pieza: **"si funciona bien pero tiene poco sentido, posiblemente sea coincidencia"** (`KB03 §20.C.3`) — es exactamente el criterio de LdP formulado como test de plausibilidad.

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` La consecuencia práctica es que **el mecanismo no tiene por qué preceder a la exploración, pero sí a la conversión en estrategia**, y que la exploración agnóstica consume presupuesto de multiple testing que debe contabilizarse (§15).

---

## 6.2 Muestreo cronológico: uso vs crítica

**El conflicto aparente:**
- `[JANSEN]` Usa barras temporales en todo su libro, incluido su ejemplo intradiario (`KB01 §5.3`).
- `[LDP]` Las barras temporales **"deberían evitarse"**; sobremuestrean períodos de baja actividad y submuestrean los de alta (`KB02 §3.1`).

`[SÍNTESIS — INTERPRETACIÓN]` **Falsa contradicción parcial.** Jansen no defiende las barras temporales: **las presenta junto con las alternativas y simplemente no las compara** (`KB01 §5.3` lo registra como vacío). Su uso es una elección práctica no argumentada, no una posición contraria. **No hay dos tesis enfrentadas; hay una tesis (LdP) y una práctica sin justificar (Jansen).**

**Estatus:** el desacuerdo real es menor de lo que parece. Sigue siendo `[DECISIÓN DE DISEÑO ABIERTA]` (C2), pero **sin respaldo bibliográfico a favor de las barras temporales más allá de la conveniencia**.

---

## 6.3 Complejidad de modelo

**El conflicto aparente:**
- `[JANSEN]` Dedica seis capítulos a Deep Learning.
- `[LDP]` Es agnóstico al algoritmo y prefiere bagging sobre boosting.
- `[MURPHY]` No trata ML.

`[SÍNTESIS — INTERPRETACIÓN]` **Falsa contradicción.** Jansen expone el Deep Learning **y concluye que no aporta**: en su propio experimento, el R² de las decisiones de arquitectura sobre el IC fue prácticamente cero, y su CNN caía en óptimos locales prediciendo constantes (`KB01 §13.2`). **Exponer no es respaldar.** Las tres fuentes son compatibles en la conclusión: la complejidad debe demostrar valor incremental.

**Estatus:** `[CONSENSO FUERTE]` ya registrado en §3.4.

---

## 6.4 El papel del análisis técnico

**El conflicto aparente:** Murphy dedica un libro a técnicas que Jansen y LdP apenas mencionan.

`[SÍNTESIS — INTERPRETACIÓN]` **Falsa contradicción, y con un dato que la resuelve**: LdP propone explícitamente que **una regla técnica de trading puede funcionar como modelo primario** de un sistema de meta-labeling (`KB02 §7.6`), y sus propios ejercicios plantean cruces de medias y bandas de Bollinger como primarios. **No hay rechazo del análisis técnico; hay una asignación de rol**: fuente de reglas de dirección, no de validación.

Y Jansen incluye más de doscientos indicadores técnicos en su catálogo (`KB01 §6.3`), advirtiendo que **no debe asumirse que contengan señal**.

**Estatus:** `[COMPLEMENTARIEDAD]`. Las tres fuentes son compatibles en tratar el análisis técnico como **generador de hipótesis y de features candidatas, sin estatus probatorio propio**.

---

# §7. TENSIONES

Análisis exhaustivo de los conflictos reales. Para cada uno: posición de cada fuente, razonamiento, naturaleza de la diferencia, resolubilidad y consecuencias.

## 7.1 Instrumento único

**Tratada en profundidad en §8.** Resumen: **tensión conjunta por tres vías distintas** — recomendación explícita en LdP, criterio de robustez en Murphy, y dependencia estructural del aparato métrico en Jansen, que no formula recomendación. Es la tensión estructural del proyecto.

---

## 7.2 Intradiario vs horizontes mayores

**Posiciones:**

| Fuente | Posición | Razonamiento | Evidencia aportada |
|---|---|---|---|
| `[JANSEN]` | Favorable: "las estrategias algorítmicas tienden a rendir mejor a frecuencias más altas" (`KB01 §3.5`) | No lo argumenta | **Ninguna.** Su único ejemplo intradiario produjo un spread de 0.5 pb/min entre deciles y **no fue backtesteado con costes** (`KB01 §20.2`) |
| `[MURPHY]` | Desfavorable, tres veces: "la aleatoriedad es un fenómeno de muy corta duración"; el intradía como refinamiento subordinado; "dominar interdía antes que intradía" (`KB03 §8.5, §16.8, §16.10`) | La estructura es visible en gráficos de largo plazo | **Ninguna.** Argumento visual, que la propia KB03 identifica como circular |
| `[LDP]` | **Neutral.** Marco agnóstico a la frecuencia; ejemplos mayoritariamente diarios | — | **Ninguna** |

**Naturaleza de la diferencia:** `[SÍNTESIS — INTERPRETACIÓN]` **Es una tensión entre dos afirmaciones igualmente infundadas.** Ninguna de las dos posiciones está respaldada por evidencia en su respectiva fuente. Jansen afirma sin argumentar; Murphy argumenta visualmente, que es precisamente el mecanismo que las otras dos fuentes identifican como generador de falsos descubrimientos.

**Distinción obligatoria que el encargo exige:**

- **"Puede analizarse intradiario"** → `[CONSENSO]` implícito. Murphy afirma que el gráfico de barras se construye igual a cualquier escala (`KB03 §3.5`); LdP es agnóstico; Jansen lo hace. **Nadie sostiene que sea imposible.**
- **"Existe predictibilidad explotable intradiaria"** → **`[PREGUNTA EMPÍRICA]` (P4).** Ninguna fuente lo demuestra para ningún instrumento.

**¿Resoluble?** No conceptualmente. **Requiere datos** (P4, B1, B3).

**Consecuencia para IRIS:** `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` La orientación intradiaria del proyecto **no tiene respaldo bibliográfico ni refutación bibliográfica**. Es una `[RESTRICCIÓN ACTUAL DEL PROYECTO]` que debe validarse empíricamente y no puede darse por buena porque una de las tres fuentes la favorezca sin evidencia.

---

## 7.3 Qué constituye evidencia

**La tensión más consecuente para el diseño experimental.** Posiciones:

| Criterio | Jansen | López de Prado | Murphy |
|---|---|---|---|
| **Out-of-sample** | Obligatorio; hold-out de un solo uso (`KB01 §15.2`) | Obligatorio; base de purged CV y CPCV | **Cap. 9: obligatorio. Apéndice C: rechazado explícitamente** (`KB03 §26.1`) |
| **Purged CV / embargo** | Los nombra y atribuye a LdP sin desarrollar | Desarrollo completo | Ausente |
| **CPCV** | Ausente | Genera una distribución de Sharpes en lugar de un número | Ausente |
| **Multiple testing / DSR** | Longitud mínima de backtest; DSR | ~20 iteraciones; DSR; PBO | **Concepto ausente** |
| **Robustez paramétrica** | Implícita en curvas de validación | Test del bagging | **Criterio explícito y central** (`KB03 §20.C.5`) |
| **Robustez temporal** | Reporte separado in/out-of-sample | Múltiples caminos en CPCV | **Criterio explícito** |
| **Robustez entre mercados** | Implícita en su enfoque cross-sectional | Features stacking | **Criterio explícito** — inaccesible para IRIS |
| **Observación visual** | Rechazada implícitamente | Rechazada ("investigar bajo la influencia de un backtest…") | **Método principal**; "la observación empírica resulta más útil que las técnicas estadísticas sofisticadas" (`KB03 §1.8`) |
| **Backtest** | Herramienta de descarte | **"No es una herramienta de investigación"** | Paso 4 de 5, con costes excluidos |

**Naturaleza de la diferencia:** `[SÍNTESIS — INTERPRETACIÓN]` **Hay dos conflictos distintos aquí y conviene separarlos:**

**(a) Conflicto real Jansen+LdP vs Murphy sobre el estatus de la observación visual.** No es resoluble por acuerdo: son epistemologías incompatibles. **Pero sí es resoluble por criterio lógico** (§29 del encargo, criterio 1): la inspección visual de series para identificar patrones **no admite control de multiple testing ni es reproducible entre observadores** — y el propio Murphy reconoce ambas cosas (`KB03 §1.7`). **Se resuelve a favor de Jansen+LdP por razones metodológicas, no por votación.**

**(b) `[CONTRADICCIÓN INTERNA]` en Murphy sobre el out-of-sample.** El capítulo 9 afirma que "el procedimiento correcto es usar sólo parte de la información para elegir los parámetros y otra parte para examinar los resultados"; el apéndice C declara "uso la totalidad de las series de datos, sin guardar nada para hacer la prueba fuera de la muestra" (`KB03 §26.1`). **La justificación del apéndice es circular**: no reservar datos porque el método "descansa sobre conceptos firmes y prácticamente ninguna optimización" presupone precisamente lo que el out-of-sample serviría para verificar.

**Resolución propuesta:**

`[SÍNTESIS — INTERPRETACIÓN]` **Los criterios de robustez de Murphy son un complemento valioso y no un sustituto.** Robustez paramétrica y temporal detectan un modo de fallo (ajuste a ruido que se rompe al perturbar) que el out-of-sample **no detecta directamente**: un sistema puede pasar un hold-out por azar y aun así ser frágil. Y el out-of-sample detecta un modo de fallo (memorización de la muestra) que la robustez paramétrica no detecta. **Son ortogonales.**

**Jerarquía defendible resultante:**

```
NECESARIO (no negociable):
  causalidad estricta · control de leakage · out-of-sample real ·
  registro de intentos · corrección por multiple testing

ALTAMENTE RECOMENDABLE:
  purging y embargo cuando hay solapamiento · múltiples caminos (CPCV si es viable) ·
  robustez paramétrica · robustez temporal entre períodos y regímenes

COMPLEMENTARIO:
  concordancia entre métodos supervisados y no supervisados ·
  test del bagging · comparación contra baselines

NO ADMISIBLE COMO EVIDENCIA:
  inspección visual de gráficos · selección de ejemplos favorables ·
  backtest usado para redefinir el sistema sin contabilizar el intento
```

**Consecuencia para IRIS:** `[RESTRICCIÓN METODOLÓGICA]`. Desarrollada en §14.

---

## 7.4 Hipótesis primero vs features primero

**Ya resuelta como falsa contradicción en §6.1.** Residuo real: diferencia de tolerancia al riesgo de falso descubrimiento entre Jansen y LdP. `[DECISIÓN DE DISEÑO ABIERTA]` sobre cuánta exploración agnóstica se permite antes de exigir mecanismo.

---

## 7.5 NO TRADE y abstención — taxonomía de mecanismos

**El encargo pide una taxonomía y advierte que estos conceptos podrían no deber colapsarse en una única clase.**

**Los seis mecanismos identificados en las tres KB** (cinco numerados más una sexta vía implícita):

| # | Mecanismo | Fuente | Cómo emerge la abstención | Qué estado representa |
|---|---|---|---|---|
| **1** | **Régimen desfavorable** | `[MURPHY]` `KB03 §4.1` | El mercado está lateral; las herramientas direccionales no aplican; "mantenerse fuera es generalmente lo más sensato" | **No hay oportunidad** |
| **2** | **Baja confianza del modelo** | `[LDP]` `KB02 §14.3` | La probabilidad predicha es cercana al azar → estadístico z ≈ 0 → tamaño ≈ 0 | **Hay situación pero no sé lo suficiente** |
| **3** | **Meta-etiqueta 0** | `[LDP]` `KB02 §7.2` | Un modelo secundario predice que la señal primaria es un falso positivo | **Hay señal pero probablemente es errónea** |
| **4** | **Discretización del tamaño** | `[LDP]` `KB02 §14.5` | El tamaño calculado cae por debajo de medio paso y colapsa a cero | **La expectativa es positiva pero demasiado pequeña** |
| **5** | **Umbrales asimétricos de entrada/salida** | `[MURPHY]` `KB03 §9.8, §20.C.3` | Se sale con un criterio más laxo que el de entrada → estado de no-posición entre señales | **Ya no hay razón para estar dentro** |

**Y una sexta vía implícita:**

| **6** | **Umbral de decisión por costes y beneficios** | `[JANSEN]` `KB02… no — `KB01 §8.3` | El umbral de clasificación se optimiza según la función de coste; por debajo de él no se actúa | **El valor esperado no cubre el coste** |

**¿Son lo mismo?**

`[SÍNTESIS — INTERPRETACIÓN]` **No, y ésta es probablemente la aportación más importante de esta sección.** Los estados que representan son conceptualmente distintos y tienen **condiciones de falsación diferentes**:

| Estado | Pregunta que responde | Se falsaría observando |
|---|---|---|
| **No hay oportunidad** | ¿El mercado ofrece algo? | Que los retornos futuros en ese estado tengan la misma estructura que en otros |
| **No sé lo suficiente** | ¿Mi modelo discrimina aquí? | Que la precisión condicionada a baja confianza sea igual a la de alta confianza |
| **Sé pero probablemente me equivoco** | ¿Es este positivo verdadero? | Que la tasa de acierto del primario no dependa de las features del secundario |
| **Sé y acierto pero es demasiado pequeño** | ¿Cubre los costes? | Que la distribución de magnitudes esperadas sea independiente del edge realizado |
| **El riesgo es excesivo** | ¿La varianza condicional lo desaconseja? | Que el drawdown condicionado no difiera entre estados |

**`[HIPÓTESIS ESTRUCTURAL]`** `[SÍNTESIS — IMPLICACIÓN PARA IRIS]`
> **Colapsar estos estados en una única clase `NO_TRADE` destruye información que los distingue, y hace que el modelo tenga que aprender simultáneamente varias relaciones distintas bajo una misma etiqueta.**

Esto **no significa** que deban modelarse por separado —eso sería una decisión de arquitectura, prohibida en esta etapa—. Significa que:
1. **La decisión N1 (qué mecanismo adoptar) no es una elección entre alternativas equivalentes**, sino entre respuestas a preguntas distintas.
2. **Podrían coexistir**: un filtro de régimen (1) y un umbral de confianza (2) no se excluyen.
3. `[TENSIÓN]` con LdP, que **desaconseja la clase neutra explícita** (`KB02 §7.5`) argumentando que rompe la ponderación por atribución de retornos y que el neutro se implica de la baja confianza. **Su argumento cubre el mecanismo 2 pero no el 1**: un régimen desfavorable no es lo mismo que una predicción incierta.

**¿Resoluble?** Parcialmente. La distinción conceptual es resoluble ahora (queda establecida). **Cuál mecanismo usar es `[DECISIÓN DE DISEÑO ABIERTA]` que depende de E1, E3 y K1.**

---

## 7.6 Horizonte fijo vs labeling dependiente del camino

**Posiciones:**

| Fuente | Formulación | Qué problema resuelve | Qué ignora |
|---|---|---|---|
| `[JANSEN]` | Forward return a horizonte fijo, múltiples horizontes comparados por IC (`KB01 §9.1`) | Simplicidad; permite comparar horizontes sistemáticamente | **La trayectoria.** Dos observaciones con idéntico retorno final pueden tener caminos opuestos |
| `[LDP]` | Triple barrera con ocho configuraciones; el horizonte fijo es el caso degenerado `[0,0,1]` (`KB02 §6.4`) | **Realismo operativo**: "es irrealista construir una estrategia que obtenga beneficio de posiciones que habrían sido cerradas forzosamente" | Requiere fijar barreras, que son parámetros adicionales |
| `[MURPHY]` | No propone método de etiquetado, pero aporta el racional: **stop implícito por margin call**; risk/reward; "las salidas importan más que las entradas" (`KB03 §16.4, §20.C.3`) | Justifica por qué la trayectoria importa | No ofrece formalización |

**Naturaleza de la diferencia:** `[SÍNTESIS — INTERPRETACIÓN]` **No es un desacuerdo sobre hechos sino sobre qué se está modelando.** El horizonte fijo modela **el proceso de precios**; la triple barrera modela **el resultado de una regla operativa**. Son objetos distintos, y por eso "cuál es mejor" está mal planteado: depende de si IRIS quiere predecir el mercado o evaluar una regla (que es la pregunta canónica E2).

**El argumento de LdP es fuerte pero no concluyente:** su premisa es que toda estrategia tiene stop implícito. Murphy la corrobora independientemente (`KB03 §16.4`). **Ninguno de los dos demuestra que el etiquetado por barreras produzca mejores modelos**, sólo que produce etiquetas más realistas.

**La limitación que el encargo pide documentar:**

`[RESTRICCIÓN DE DATOS]` **Con OHLCV de una barra no conocemos el orden intrabar entre High y Low.** Consecuencias exactas:
- Si las barreras se comprueban **contra cierres** (como en la implementación de referencia de LdP, `KB02 §6.6`), no hay ambigüedad **pero se subestima cuántas veces habríamos sido detenidos**: el precio pudo tocar el stop intrabar y cerrar por encima.
- Si se comprueban **contra High/Low**, se refleja mejor la ejecución real de órdenes stop y limit, **pero cuando ambos extremos cruzan sus respectivas barreras en la misma barra es indecidible cuál se tocó primero**.
- **Ninguna de las tres fuentes menciona este problema.** `KB02 §6.6` y `KB03 §12.6` lo registran como vacío.
- `[SÍNTESIS — INTERPRETACIÓN]` La frecuencia del caso ambiguo **decrece con la resolución de barra** y es por tanto `[PREGUNTA EMPÍRICA]` medible sobre MNQ: qué proporción de barras candidatas presenta ambigüedad, a cada resolución.

**Consecuencia:** `[DECISIÓN DE DISEÑO ABIERTA]` F1 y F5. **No se declara ganador.**

---

## 7.7 Barras temporales vs muestreo por actividad o eventos

**Posiciones:** ya resumidas en §6.2 (Jansen usa sin defender; LdP critica; Murphy es indiferente pero aporta el P&F como muestreo por movimiento).

**Lo que el encargo pide clasificar — qué es realmente posible con OHLCV:**

| Esquema | Viabilidad | Condición |
|---|---|---|
| **Barras temporales** | **`OHLCV-OK`** | Es lo que tenemos |
| **Barras de volumen aproximadas** | **`OHLCV-COND`** | Agregando barras base hasta alcanzar un umbral. Pérdidas: frontera cuantizada a la resolución base; VWAP interno perdido; degeneración si una barra base excede el umbral (`KB02 §3.3`) |
| **Barras de dólar aproximadas** | **`OHLCV-COND`** | Igual, con un precio representativo por barra. Error de segundo orden, medible |
| **P&F de 3 registros** | **`OHLCV-COND`** | **Diseñado explícitamente para prescindir de datos intradía**: usa sólo High y Low con reglas de prioridad deterministas (`KB03 §11.3`). La regla de prioridad es una **convención arbitraria** ante la ambigüedad intrabar |
| **Muestreo por eventos (CUSUM)** | **`OHLCV-OK`** | Sólo requiere la serie de cierres o cualquier feature derivada (`KB02 §5.4`) |
| **Barras de tick** | **`GRANULAR`** | Requiere conteo de transacciones |
| **Barras de imbalance y de runs** | **`GRANULAR`** | Requieren firmar cada operación. **`KB02 §3.3` advierte explícitamente contra fabricar un sustituto desde el signo de barra**: un desbalance de flujo puede ser grande sin que el precio se haya movido |

`[SÍNTESIS — INTERPRETACIÓN]` **Hay un hallazgo cruzado que ninguna KB individual señala:** el método P&F de 3 registros y la aproximación de barras de volumen resuelven el mismo problema —muestrear por algo distinto del reloj— con datos que sí tenemos, y **ambos fueron diseñados en tradiciones que desconocían la otra**. El P&F, además, **es históricamente anterior y fue explícitamente rediseñado para funcionar sin datos intradía** (`KB03 §11.3`). Eso lo convierte en un precedente relevante: la disciplina ya resolvió una vez el problema de aproximar muestreo por actividad desde barras agregadas.

**Estatus:** `[DECISIÓN DE DISEÑO ABIERTA]` C2, informada por `[PREGUNTA EMPÍRICA]` sobre el error de aproximación (C1, C4).

---

## 7.8 Tensiones adicionales identificadas

Además de las siete obligatorias, la síntesis detecta:

| # | Tensión | Naturaleza | Resolubilidad |
|---|---|---|---|
| **7.8.a** | **Cuándo aplicar costes.** LdP y Jansen: desde el primer backtest. Murphy (apéndice C): excluidos de las pruebas por "pureza", incluidos al final | Metodológica | **Resoluble por lógica**: excluirlos es defendible para comparar variantes homogéneas, indefendible para decidir viabilidad. Y en alta frecuencia **puede invertir el orden entre sistemas de distinto turnover** (`KB03 §20.C.6`) |
| **7.8.b** | **Papel del juicio discrecional.** Murphy defiende que el operador intervenga cuando el sistema no reconoce estructuras visibles (`KB03 §15.5`); las otras dos exigen especificación completa | Epistemológica | **Resoluble**: el argumento de Murphy, si su premisa fuera cierta, implicaría incorporar esas estructuras como variables, no intervenir manualmente |
| **7.8.c** | **Selección de features.** Murphy: "elija uno o dos osciladores con los que se sienta cómodo". Jansen y LdP: por importancia medida fuera de muestra | Metodológica | **Resoluble a favor de Jansen+LdP**: el criterio de Murphy no es reproducible |
| **7.8.d** | **Optimización.** Tres posiciones **dentro de Murphy** (cauta en cap. 9, celebratoria en cap. 15, minimizada en apéndice C) frente a la posición única de LdP (contribuye al sobreajuste vía la propia CV) | `[CONTRADICCIÓN INTERNA]` + tensión | Resoluble a favor de LdP |
| **7.8.e** | **Clase neutra.** LdP la desaconseja; Murphy la deriva del régimen; Jansen la trata como umbral | Conceptual | **No resoluble ahora.** Ver §7.5 |
| **7.8.f** | **Qué es "alfa".** Jansen y LdP lo definen contra un benchmark; en MNQ el benchmark natural es el subyacente del propio contrato | Conceptual | **`[VACÍO]`** (Q4) |

---

# §8. INSTRUMENTO ÚNICO: ANÁLISIS ESPECÍFICO

La tensión estructural del proyecto. Análisis sobrio, sin concluir automáticamente "hay que añadir activos" ni minimizar el problema.

## 8.1 Las tres vías de la tensión, y por qué no son la misma

| Fuente | Advertencia | Mecanismo del argumento |
|---|---|---|
| `[LDP]` | **Primera de sus seis recomendaciones anti-overfitting**: desarrollar modelos para clases de activos o universos, no para valores específicos. "Si encuentras el error X sólo en el valor Y, por rentable que parezca, probablemente sea un falso descubrimiento" (`KB02 §15.4`) | **Replicación**: un patrón real debería aparecer en instrumentos relacionados porque los inversores diversifican |
| `[LDP]` | Prefiere **features stacking** —apilar datasets de muchos instrumentos— **incluso para predicción**, con la razón explícita de reducir la probabilidad de sobreajustar a un instrumento particular (`KB02 §12.6`) | **Tamaño muestral y regularización implícita** |
| `[MURPHY]` | **Estabilidad entre mercados** como uno de los tres criterios de robustez; "si no es así, buscaré una explicación y generalmente descartaré el sistema" (`KB03 §20.C.5`) | **Replicación**, formulada como test de descarte |
| `[JANSEN]` | **No formula ninguna recomendación contra el instrumento único.** Lo que hay es (a) dependencia estructural: IC como correlación de rangos entre activos, quantiles cross-sectional, breadth de la ley fundamental, carteras long-short (`KB01 §0.4`); y (b) el registro de que su libro **no contiene un solo ejemplo completo con un único activo** (`KB01 §22-D`), que es un vacío de cobertura, no una advertencia | **Estructural**: sus métricas no están definidas sin sección transversal. **No es un argumento contra el diseño, sino una limitación de trasladabilidad de su instrumental** |

`[SÍNTESIS — INTERPRETACIÓN]` **Son argumentos de distinta naturaleza, y sólo dos son advertencias.** LdP-recomendación y Murphy invocan **replicación**; LdP-stacking invoca **tamaño muestral**; **Jansen no advierte nada**: presenta un problema **de definición de métricas** y un vacío de cobertura. Confundirlos llevaría a creer que hay más consenso del que hay. La formulación precisa es: **una fuente lo desaconseja explícitamente (LdP), otra lo usa como criterio de descarte (Murphy), y la tercera simplemente no lo cubre y le presupone lo contrario (Jansen). Ninguna demuestra que un sistema de instrumento único sea inválido.**

## 8.2 Qué perdemos exactamente

| Pérdida | Qué defensa aportaba | Gravedad |
|---|---|---|
| **Replicación entre instrumentos** | Un patrón que aparece en N activos relacionados es mucho más difícil de atribuir al azar que uno que aparece en uno. **Es un test de significación implícito con N observaciones independientes** | **Alta.** Es la pérdida principal |
| **Validación cross-sectional** | Todo el aparato de Jansen: IC entre activos, quantiles, spreads long-short (`KB01 §22-C`) | **Alta en método, media en fondo**: las preguntas subyacentes son traducibles a serie temporal, sus propiedades estadísticas no |
| **Breadth (apuestas independientes)** | La ley fundamental: IR ≈ IC × amplitud. En instrumento único la amplitud es sólo temporal y **las apuestas consecutivas están correlacionadas** (`KB01 §18.3`) | **Alta.** Un IC dado produce menos IR que en cross-sectional, y aumentar la frecuencia **no aumenta la amplitud proporcionalmente pero sí los costes** |
| **Features stacking** | Dataset mucho mayor; conclusiones menos sesgadas por outliers de una serie | **Media.** Compensable parcialmente por la longitud del histórico intradiario |
| **Confirmación intermercado** | Cuarta fuente de corroboración de Murphy (`KB03 §17.2`) | **Media.** Deliberadamente fuera de alcance |
| **Amplitud del Nasdaq** | El MNQ *es* un índice de 100 valores; la información de amplitud existe y es directamente relevante (`KB03 §18.2`) | **Media-alta, y es la pérdida más punzante**: no requeriría otro mercado, sino la descomposición del propio índice |
| **Confirmación entre índices (Dow)** | Exigir que dos series relacionadas coincidan como reductor de falsos positivos (`KB03 §2.4`) | Baja-media |

## 8.3 Qué conservamos

`[SÍNTESIS — INTERPRETACIÓN]` Conviene ser igual de preciso con esto, porque el inventario de pérdidas puede dar una impresión desproporcionada:

| Conservamos | Valor |
|---|---|
| **Variación temporal extensa** | En frecuencia intradiaria, el histórico contiene un número de barras muy superior al de cualquier estudio diario. **Pero el número de observaciones *independientes* es la cuestión abierta G1**, no el de filas |
| **Múltiples períodos y regímenes** | Base de la defensa sustitutiva principal (§8.4) |
| **Toda la validación temporal** | Purging, embargo, walk-forward, CPCV: **ninguno requiere universo** (`KB02 §11, §16`) |
| **Todo el aparato de etiquetado y ponderación** | Triple barrera, unicidad, sample weights: `OHLCV-OK` y de instrumento único (`KB02 §6, §8`) |
| **Todo el control de multiple testing** | DSR, PBO, longitud mínima de backtest: operan sobre resultados, no sobre activos |
| **Los mecanismos económicos** | **Los tres mecanismos con mejor respaldo cruzado son de instrumento único**: flujo forzado (§4.A), memoria de niveles (§4.C) y régimen (§4.B) |
| **La especificidad del futuro apalancado** | El mecanismo de margin call es **más fuerte** en MNQ que en acciones al contado (`KB03 §4.4`) |
| **La estructura de sesión** | Perfil intradiario, pivotes, extensión del rango: sólo tienen sentido en un instrumento concreto |

## 8.4 Defensas sustitutivas — análisis honesto

Para cada una, el encargo exige indicar **qué compensa y qué NO puede compensar**.

| Defensa | Respaldo | Qué problema compensa | Qué problema **NO** compensa |
|---|---|---|---|
| **Estabilidad entre años** | `[MURPHY]` criterio explícito (`KB03 §20.C.5`); `[LDP]` implícito | Ajuste a un período concreto. **Detecta si el hallazgo depende de un régimen histórico** | **No es replicación.** Los períodos del mismo instrumento comparten estructura de mercado, participantes y microestructura. Su independencia es mucho menor que la de instrumentos distintos |
| **Estabilidad entre regímenes** | `[MURPHY]` (`KB03 §9.12`); `[JANSEN]` factor decay | Que el efecto sea un artefacto de un tipo de mercado | Igual limitación: los regímenes del mismo instrumento no son muestras independientes del "espacio de mercados" |
| **Robustez paramétrica** | `[MURPHY]` criterio central (`KB03 §20.C.5`); `[LDP]` test del bagging | **Ajuste a ruido**: si el resultado se rompe al perturbar los parámetros, era sobreajuste. **Detecta un modo de fallo que el out-of-sample no detecta** | No dice nada sobre si el efecto es real; un artefacto estable ante perturbaciones sigue siendo un artefacto |
| **Múltiples caminos OOS (CPCV)** | `[LDP]` (`KB02 §16.4`) | **Sobreajuste a un único camino histórico.** Produce una distribución de Sharpes en lugar de un número | **No genera observaciones nuevas.** Los caminos combinan los mismos datos; la información subyacente es la misma |
| **Purging y embargo** | `[LDP]` (`KB02 §11`) | **Leakage.** Necesario, no sustitutivo | No compensa nada de la pérdida cross-sectional |
| **Hold-out final intocado** | `[JANSEN]` (`KB01 §15.2`) | Contaminación por selección iterativa | Un solo test; consume histórico escaso |
| **DSR y registro de intentos** | `[JANSEN]` + `[LDP]` | **Multiple testing.** Es la defensa más directamente sustitutiva: donde el universo aportaba replicación, la corrección estadística aporta severidad | **No aumenta la potencia**: hace más difícil declarar un hallazgo, no más fiable el que se declare |
| **Simplicidad / pocos parámetros** | Las tres (§3.4) | **Reduce la superficie de sobreajuste ex-ante.** Es preventiva, no diagnóstica | No detecta nada; sólo evita crear el problema |
| **Hipótesis ex-ante con mecanismo** | Las tres (§3.8) | **Reduce el espacio de búsqueda**, que es la causa raíz del multiple testing | No garantiza que el mecanismo opere realmente |
| **Consistencia direccional del efecto** | `[SÍNTESIS — INTERPRETACIÓN]`, no propuesta por ninguna fuente | Que el signo del efecto sea el mismo en submuestras independientes | Es una forma débil de replicación **dentro** de la misma serie |
| **Pruebas placebo** | `[CONOCIMIENTO EXTERNO]` — no aparece en las tres KB | Aplicar el mismo procedimiento a datos donde no debería haber efecto (series permutadas, períodos aleatorizados) para calibrar la tasa de falsos positivos del propio procedimiento | No sustituye a la replicación real, pero **sí acota cuánto resultado espurio produce nuestro pipeline** |
| **Comparación contra baselines** | Las tres (§3.4) | Que el modelo aporte sobre lo trivial | No compensa la pérdida de replicación |
| **Sensibilidad temporal (evaluar por subperíodos)** | `[JANSEN]` reporte in/out; `[MURPHY]` estabilidad | Concentración del resultado en pocos episodios | Igual limitación de independencia |

## 8.5 Balance

`[SÍNTESIS — INTERPRETACIÓN]` **La conclusión honesta tiene tres partes:**

**1. Ninguna defensa temporal es matemáticamente equivalente a la validación entre activos, y no debe presentarse como si lo fuera.** La replicación entre instrumentos aporta muestras que son independientes en un sentido en que los subperíodos del mismo instrumento no lo son. **Perdemos potencia estadística real.**

**2. Pero el conjunto de defensas disponibles no es vacío ni marginal.** Cubre modos de fallo distintos y parcialmente complementarios: robustez paramétrica cubre ajuste a ruido, CPCV cubre dependencia del camino, DSR cubre multiple testing, simplicidad e hipótesis ex-ante reducen la superficie de búsqueda, y las pruebas placebo calibrarían la tasa de error del propio procedimiento. **La combinación es sustancialmente más estricta que lo que la mayoría de estudios aplican.**

**3. El coste real es de severidad, no de imposibilidad.** `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Trabajar con un instrumento único implica que **el umbral de evidencia debe ser más alto, no que la investigación sea inválida**. En términos operativos: menos hipótesis probadas, mecanismos exigidos antes, márgenes de efecto mayores para declarar un hallazgo, y aceptación explícita de que un resultado marginal **no es concluyente aunque pase todos los tests**.

**Estatus: `[TENSIÓN]` no resuelta. `[DECISIÓN DEL PROYECTO]` T1.** La decisión de mantener o ampliar el alcance **no es científica**: depende de qué coste de complejidad operativa se acepta a cambio de cuánta potencia estadística. **Queda explícitamente abierta y corresponde al usuario.**

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Y una observación que puede informarla: **la ampliación mínima que recuperaría la mayor parte de la defensa perdida no es "más activos" en general**, sino instrumentos donde la misma hipótesis debería operar por el mismo mecanismo — por ejemplo, otros futuros de índices líquidos y apalancados, donde el mecanismo de margin call y flujo forzado sería el mismo. **Eso es una observación sobre el diseño de un eventual test de replicación, no una recomendación de ampliar el alcance.**

---

# §9. OHLCV-ONLY: QUÉ PODEMOS Y QUÉ NO PODEMOS SABER

Integración de los filtros de disponibilidad de las tres KB.

## 9.1 Grupo A — `OHLCV-OK`: disponible de forma limpia

`[SÍNTESIS — INTERPRETACIÓN]` **El inventario es más amplio de lo que la restricción sugiere.** Está disponible sin condiciones:

**Metodología completa:**
- Purged K-Fold, embargo, walk-forward, CV backtesting, **CPCV** (`KB02 §11, §16`).
- Concurrencia, unicidad media, sequential bootstrap, atribución de retornos, time decay, class weights (`KB02 §8`).
- Triple barrera sobre cierres, umbrales dinámicos por volatilidad, meta-labeling, eliminación de etiquetas raras (`KB02 §6, §7`).
- Bet sizing desde probabilidades, promediado de apuestas activas, discretización (`KB02 §14`).
- PSR, DSR, CSCV/PBO, todas las métricas de backtest (`KB02 §18`).
- Marco de riesgo de estrategia y probabilidad de fracaso (`KB02 §19`).
- MDI, MDA, SFI, ortogonalización PCA, Kendall tau ponderada (`KB02 §12`).
- IC, mutual information, análisis por quantiles, SHAP, permutación (`KB01 §7, §19`).
- Curvas de aprendizaje y validación, bias-variance (`KB01 §15.6`).
- Diagnóstico de series temporales: ACF/PACF, ADF, descomposición, GARCH (`KB01 §11`).
- Fractional differentiation (`KB02 §9`).
- CUSUM y muestreo por eventos (`KB02 §5`).
- Chu-Stinchcombe-White, SADF, tests sub/super-martingala, entropía (`KB02 §21, §22`).
- Estabilidad paramétrica y temporal como criterios (`KB03 §20.C.5`).

**Features y estructura:**
- Las ocho familias informativas de `KB03 §22.2` completas.
- ATR, ADX, coeficiente de eficiencia, ancho de banda, posición en rango, RSI, geometría elemental de vela, volumen relativo, OBV, día de cambio, huecos como evento, números redondos, estacionalidad intradiaria, puntos pivote intradía, SAR (`KB03 §25.1`).
- Estimador de volatilidad High-Low, superior al de cierres según `KB02 §23.2`.

## 9.2 Grupo B — `OHLCV-COND`: disponible con aproximaciones declaradas

| Elemento | Condición y pérdida |
|---|---|
| **Barras de volumen / dólar** | Frontera cuantizada a la resolución base; VWAP interno perdido; degeneración si una barra base excede el umbral (`KB02 §3.3`) |
| **P&F de 3 registros** | Regla de prioridad arbitraria ante ambigüedad intrabar (`KB03 §11.3`) |
| **Triple barrera contra High/Low** | Ambigüedad intrabar indecidible (§7.6) |
| **Market Profile (TPO, área de valor)** | Supone que todos los precios entre L y H se negociaron; requiere definir sesión (`KB03 §20.B.3`) |
| **Lambda de Amihud** | Volumen en dólares aproximado como precio × volumen (`KB02 §23.2`) |
| **Modelo de Roll** | Condición no verificable: que la barra sea fina para que el bid-ask bounce domine la covarianza serial |
| **Serie continua de futuros** | Requiere identificador de contrato o fechas de roll (`KB02 §4.4`) |

## 9.3 Grupo C — `GRANULAR`: no reconstruible desde OHLCV

`[SÍNTESIS — INTERPRETACIÓN]` **Todo lo que depende de firmar operaciones o de la secuencia intrabar:**

- **Regla del tick** y todas sus transformaciones.
- **Barras de imbalance y de runs** (TIB, VIB, DIB, TRB, VRB, DRB). `KB02 §3.3` advierte explícitamente contra fabricar un sustituto desde el signo de barra.
- **Lambdas de Kyle y Hasbrouck, PIN, VPIN** (`KB02 §23.3`).
- **Distribución de tamaños de orden, tasas de cancelación, huella de algoritmos TWAP.**
- **Volumen al alza vs a la baja, delta, flujo firmado.** `[MURPHY]` lo confirma independientemente: "se dispone de los niveles al alza y a la baja para los valores, pero no para los futuros" (`KB03 §7.4`).
- **Flujo Monetario de Birinyi** (`KB03 §7.4`).
- **Market Profile auténtico con TPO por tiempo real de permanencia.**
- **Orden intrabar entre High y Low** — la limitación transversal.
- **Interpretación psicológica de la forma de la vela** (`KB03 §12.6`).
- **P&F de 1 registro** (`KB03 §11.3`).

## 9.4 Grupo D — `OTRAS FUENTES`

- **Interés abierto**, IRH, informe COT (`KB03 §7.6`).
- **Amplitud de mercado**: línea A/D, McClellan, TRIN, TICK, nuevos máximos/mínimos (`KB03 §18`).
- **Sentimiento / opinión contraria** (`KB03 §10.16`).
- **Análisis intermercado y fuerza relativa** (`KB03 §17`).
- **Confirmación entre índices** (Dow) (`KB03 §2.4`).
- **Fundamentales**: todos los factores de valor y calidad de Jansen (`KB01 §6.2`).
- **Universo multiactivo**: features stacking, HRP, ETF trick para cestas, importancia paralelizada, atribución por clases de riesgo.
- **Opciones y volatilidad implícita.**

## 9.5 Las renuncias, ordenadas por gravedad

`[SÍNTESIS — INTERPRETACIÓN]` Consolidando las tres KB:

| # | Renuncia | Qué perdemos | Gravedad |
|---|---|---|---|
| **1** | **Desbalance de flujo firmado** | El fenómeno que LdP identifica como el más asociado a traders informados. Perdemos simultáneamente **el esquema de muestreo más sofisticado** (barras de información) **y toda la tercera generación microestructural** | **Alta** |
| **2** | **Secuencia intrabar** | Ambigüedad en la triple barrera con High/Low; imposibilidad de interpretar la dinámica de la vela; regla de prioridad arbitraria en P&F | **Alta**, con la mitigación de que decrece con la resolución |
| **3** | **Amplitud del Nasdaq** | Divergencias entre el índice y sus componentes, que Murphy considera "de las mejores señales anticipadas". **Y es información sobre el propio instrumento** | **Media-alta** |
| **4** | **Interés abierto** | Distinguir si un movimiento viene de dinero nuevo o de liquidación. **Atenuada**: el propio Murphy lo desaconseja en muy corto plazo y se publica con retardo | **Media** |
| **5** | **Segunda generación de iliquidez** (Kyle, Hasbrouck) | Retenemos sólo Amihud, la más simple | **Media** |
| **6** | **Sentimiento e intermercado** | Corroboración desde canales independientes del precio | **Media** |
| **7** | **Anticipación al reajuste** | Sin flujo firmado, estructuralmente **llegamos después** de que la información se incorpore | **Alta conceptualmente**, si el mecanismo de flujo forzado es la hipótesis central |

## 9.6 La pregunta del encargo: ¿impide una investigación seria?

`[SÍNTESIS — INTERPRETACIÓN]` **No. Restringe qué hipótesis podemos investigar, no el rigor con que podemos investigarlas.** La distinción es material y merece enunciarse con precisión:

**Lo que la restricción NO afecta:** el núcleo metodológico completo de las tres fuentes está disponible. Etiquetado, ponderación, validación, control de multiple testing, evaluación económica, interpretabilidad e importancia de features son **todos `OHLCV-OK` sin condiciones**. `KB02 §3.4` lo formula así: la pérdida está concentrada en un capítulo de diecinueve más una sección del capítulo 2.

**Lo que la restricción SÍ afecta:** un subconjunto identificable de hipótesis. Concretamente, **todas las que requieren distinguir quién inició una operación**. Eso incluye la familia de hipótesis microestructurales que LdP considera más prometedora.

**La consecuencia precisa:**
> `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` **Con OHLCV podemos ejecutar una investigación metodológicamente completa sobre un espacio de hipótesis reducido.** El riesgo no es hacer mala ciencia; es que **el espacio de hipótesis accesible no contenga ninguna hipótesis verdadera**. Eso es exactamente `[PREGUNTA EMPÍRICA]` P4 y no puede resolverse desde la bibliografía.

**Y una asimetría que conviene registrar:** `[SÍNTESIS — INTERPRETACIÓN]` **la mitigación de la renuncia 2 (secuencia intrabar) crece al aumentar la resolución, mientras que la renuncia 1 (flujo firmado) es independiente de la resolución.** Una barra de un minuto acota mucho el espacio de trayectorias internas; no acota en absoluto la imposibilidad de firmar operaciones. **Esto tiene consecuencias sobre la decisión C1 (resolución base)**: aumentar la resolución compra reducción de ambigüedad intrabar, pero no compra información de flujo.

**Estatus: `[DECISIÓN DEL PROYECTO]` T2**, con la información anterior. **La prioridad de una eventual ampliación de datos**, si alguna vez se plantea, sería: **datos de tick con precio** (habilitan la regla del tick, y con ella barras de información, Kyle y autocorrelación de flujo) **antes que datos de quote o de libro completo** — `KB02 §28-D`. **Esto documenta dónde estaría el retorno, no recomienda hacerlo.**

---

# §10. HIPÓTESIS DE MERCADO CANDIDATAS

Familias de hipótesis **económicas o informativas**, no indicadores. Se prioriza el mecanismo sobre el nombre: `RSI`, `ROC` y `MACD` **no** son tres hipótesis distintas.

## 10.1 Matriz de familias

| # | Familia de hipótesis | Mecanismo propuesto | Fuente(s) | Observación necesaria | Falsable | OHLCV | GL | Riesgo principal |
|---|---|---|---|---|---|---|---|---|
| **H1** | **Flujo forzado / persistencia** — tras un movimiento, existe presión de órdenes comprometidas de antemano que lo prolonga | Stops, delta hedging, rebalanceo de risk parity, margin call. **Convergencia triple** (§4.A) | `[JANSEN]` `KB01 §4` + `[LDP]` `KB02 §21.1` + `[MURPHY]` `KB03 §4.4` | Retorno futuro condicionado a magnitud y contexto del movimiento previo | **Sí** | **OK** | 1–2 | Confundir el mecanismo con "momentum" genérico |
| **H2** | **Memoria de niveles** — el precio se comporta anómalamente al reaproximarse a zonas de actividad previa, y el efecto decae con el tiempo | Cuatro grupos de participantes con interés en el nivel; cambio de polaridad (§4.C) | `[MURPHY]` `KB03 §4.4` | Comportamiento del precio cerca vs lejos de niveles de alta actividad histórica | **Sí** | **OK**, con retardo de pivote | 3–5 | `LOOK-AHEAD-LEVE`; requiere declarar `k` |
| **H3** | **Régimen condiciona la relación** — el signo o la magnitud de la relación entre features y retorno futuro depende del estado del mercado | Distintas poblaciones de participantes dominan en distintos estados (§4.B) | `[MURPHY]` ×4 + `[LDP]` `KB02 §21` + `[JANSEN]` `KB01 §3.3` | Relación feature→retorno estimada por separado en subconjuntos definidos por una variable de estado causal | **Sí** | **OK** | 2–3 | Definición circular del régimen; look-ahead en la asignación |
| **H4** | **Ciclo de volatilidad** — la compresión de volatilidad precede a la expansión y viceversa, con caducidad temporal | Equilibrio que se rompe; agotamiento tras extensión | `[MURPHY]` `KB03 §9.6, §6.1` + `[JANSEN]` clustering `KB01 §3.4` | Volatilidad futura condicionada a volatilidad y duración actuales | **Sí** | **OK** | 1–2 | Confundir predecir volatilidad con predecir dirección |
| **H5** | **Ruptura estructural** — el proceso exhibe períodos con propiedades estadísticas inconsistentes con random walk, y son informativos | Participantes atrapados; transición de régimen | `[LDP]` `KB02 §21.1` | Estadísticos de explosividad (SADF, CUSUM) frente a retorno futuro | **Sí** | **OK**, coste cuadrático | 2–3 | **Coste computacional prohibitivo en intradiario** |
| **H6** | **Volumen como confirmación** — el volumen modula la fiabilidad de un movimiento de precio, y "precede al precio" | Intensidad de la participación detrás del movimiento | `[MURPHY]` `KB03 §7.2` | Retorno futuro condicionado conjuntamente a movimiento y volumen relativo | **Sí** | **OK** | 1–2 | El volumen agregado **no es order flow** |
| **H7** | **Posición en el rango** — el cierre tiende a situarse cerca del extremo del rango reciente durante movimientos direccionales | Premisa estructural del estocástico | `[MURPHY]` `KB03 §10.8` | Distribución de la posición del cierre en el rango, condicionada a régimen | **Sí** | **OK** (usa H y L) | 1–3 | Redundante con H1 si no se controla |
| **H8** | **Geometría elemental OHLC** — las relaciones entre apertura, extremos y cierre de una o pocas barras contienen información sobre el retorno siguiente | Psicología del período; agotamiento | `[MURPHY]` `KB03 §12.2` | Ratios adimensionales de cuerpo y sombras frente a retorno futuro | **Sí** | **OK** | **0–1** | Interpretación psicológica **no determinada** por la geometría (requiere intrabar) |
| **H9** | **Agotamiento / clímax** — expansión extrema simultánea de rango y volumen tras movimiento extendido señala reversión | Liquidación forzada que agota la presión y crea vacío | `[MURPHY]` `KB03 §4.15, §7.7` | Retorno futuro tras eventos de expansión extrema | **Sí** | **OK** | 1–2 | El **evento** es causal; la etiqueta "fue el techo" es retrospectiva |
| **H10** | **Estacionalidad intradiaria** — la posición dentro de la sesión condiciona sistemáticamente volatilidad, volumen y posiblemente retorno | Apertura, solapamiento de sesiones, cierre, publicaciones programadas | **Ninguna fuente la desarrolla.** `[MURPHY]` la usa implícitamente en pivotes intradía (`KB03 §16.9`) | Momentos estadísticos condicionados a hora de sesión | **Sí** | **OK** | **0–1** | **Que el modelo aprenda el reloj en lugar del mercado** |
| **H11** | **Multi-horizonte** — información calculada sobre horizontes distintos cumple funciones distintas (contexto vs disparo) | Top-down; escalas con roles asimétricos | `[MURPHY]` `KB03 §8.4, §10.15` + `[JANSEN]` multi-horizonte de targets `KB01 §9.1` | Interacción entre features de distinta ventana | **Sí** | **OK** | k | Multiplica el espacio de búsqueda |
| **H12** | **Simetría de impulsos** — la magnitud del movimiento posterior guarda relación con la del movimiento previo | Postulada sin mecanismo. **Cinco reglas de Murphy son la misma hipótesis** (`KB03 §6.7`) | `[MURPHY]` | Amplitud del impulso siguiente frente a la del previo | **Sí** | **OK** | 2 | **Sin mecanismo propuesto** — debilita su prioridad |
| **H13** | **Compresión temporal con caducidad** — la contracción de rango tiene una duración característica y pierde fuerza si se prolonga | Vértice del triángulo; agotamiento del equilibrio | `[MURPHY]` `KB03 §6.1` | Probabilidad de expansión condicionada a duración de la compresión | **Sí** | **OK** | 2 | Requiere delimitar la compresión (retardo) |
| **H14** | **Asimetría temporal** — en tendencia se pasa más tiempo moviéndose en la dirección dominante que en contra | Reformulada por el propio Murphy desde la traslación cíclica | `[MURPHY]` `KB03 §14.4` | Proporción de barras con retorno de cada signo en una ventana | **Sí** | **OK** | **1** | Redundante con H1 y H3 si no se controla |
| **H15** | **Memoria de precio (fracdiff)** — el nivel relativo del precio contiene información que la diferenciación entera destruye | Modelos de equilibrio necesitan memoria para medir desviación | `[LDP]` `KB02 §9.1` | Aporte incremental de la serie fraccionalmente diferenciada sobre retornos | **Sí** | **OK** | 1–2 | **Feature con correlación ~0.995 con el precio es un vehículo de memorización** |
| **H16** | **Entropía como estado** — el contenido informativo de la serie condiciona qué tipo de estrategia funciona (momentum en baja entropía, reversión en alta) | Eficiencia informacional variable | `[LDP]` `KB02 §22.1` | Entropía móvil frente a rendimiento condicionado de estrategias opuestas | **Sí** | **OK** | 3+ | Muy sensible a codificación, alfabeto y longitud → **muchos intentos** |
| **H17** | **Números redondos** — niveles de precio redondos detienen o aceleran movimientos | Objetivos psicológicos; concentración de órdenes | `[MURPHY]` `KB03 §4.6` | Comportamiento del precio cerca de múltiplos frente a lejos | **Sí** | **OK** | **1** | Ejemplos de Murphy son de escala anual, no intradiaria |
| **H18** | **Estructura de sesión** — el rango inicial de la sesión y su extensión posterior son informativos | Urgencia asimétrica entre participantes de corto y largo plazo | `[MURPHY]` Market Profile `KB03 §20.B.2` | Extensión del rango frente al equilibrio inicial | **Sí** | **COND** | 2 | **Requiere definir sesión** (D1, `[VACÍO]`) |

## 10.2 Observaciones sobre la matriz

`[SÍNTESIS — INTERPRETACIÓN]`

**1. Sólo H1 tiene respaldo triple.** El resto proviene mayoritariamente de Murphy —lo cual es coherente con que sea la única fuente que formula hipótesis de mercado— con LdP aportando H5, H15 y H16, y Jansen contribuyendo a H1, H3 y H4.

**2. Hay redundancia entre familias que debe controlarse.** H1, H7 y H14 comparten observable parcial (movimiento direccional reciente); H4, H9 y H13 comparten el eje de volatilidad; H2 y H5 comparten mecanismo pero no observable (§5.3). **Investigarlas como independientes inflaría el número de pruebas sin aumentar la información.**

**3. H10 es la única que ninguna fuente desarrolla y que es específica de nuestro problema.** `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Y tiene doble filo: es una hipótesis genuina **y** es el principal mecanismo de falso descubrimiento en intradiario, porque un modelo puede obtener buenas métricas aprendiendo el perfil determinista de la sesión sin capacidad direccional alguna (`KB01 §16`, escenario 7).

**4. H12 y H17 carecen de mecanismo o de respaldo de escala.** Se conservan por completitud, con prioridad baja.

**5. Ninguna hipótesis está verificada.** El encargo lo exige y conviene repetirlo: **las tres fuentes juntas no aportan una sola medición de tasa de acierto, edge o Sharpe sobre MNQ intradiario.**

---

# §11. TAXONOMÍA UNIFICADA DE INFORMACIÓN EN `Timestamp + OHLCV`

Integra las ocho familias de `KB03 §22.2` con los aportes de las otras dos KB. Sirve para **evitar crear cincuenta indicadores que contienen cinco informaciones**.

| # | Familia | Qué representa | Datos | Transformaciones que son esta familia | Redundancia previsible | Qué aporta de distinto |
|---|---|---|---|---|---|---|
| **F1** | **Dirección / desplazamiento neto** | Cuánto y hacia dónde se movió el precio en una ventana | C (a veces H,L) | Momento, ROC, pendiente de media, distancia precio-media, cruces de medias, histograma de medias, MACD y su histograma, +DI/−DI, retornos rezagados de Jansen | **Máxima.** Todos son la variación del precio con distinta ponderación | Es la base; su ventana es el parámetro |
| **F2** | **Tendencialidad / eficiencia** | Qué fracción del camino recorrido se convirtió en desplazamiento neto. **Magnitud sin dirección** | C, H, L | ADX, coeficiente de eficiencia de Kaufman, asimetría temporal, persistencia sobre/bajo una media | Baja: **familia poco poblada** | **Distingue tendencia de lateralidad de forma continua.** Soporta H3 |
| **F3** | **Volatilidad / dispersión** | Amplitud de la fluctuación | H, L, C | **ATR**, ancho de Bollinger, ancho de STARC/Keltner, rango de barra, desviación EWM de retornos, estimador High-Low | Media | **Normalizador universal**: hace adimensionales umbrales, stops y distancias |
| **F4** | **Posición dentro de un rango** | Dónde está el precio respecto a los extremos recientes | H, L, C | Estocástico %K, Williams %R (= 100 − %K), canal de Donchian, posición del cierre en la barra, retrocesos porcentuales | **Alta e interna**: %R es transformación afín de %K | **Adimensional por construcción**; usa H y L de forma esencial |
| **F5** | **Desviación normalizada de una referencia** | A cuántas unidades de dispersión está el precio de su media | C, H, L | CCI, posición en Bandas de Bollinger, STARC, Keltner, sobres porcentuales | Alta con F1 y F3 (es su cociente) | **Combina dirección y volatilidad en una variable** |
| **F6** | **Asimetría alza/baja** | Cómo se reparte la magnitud entre subidas y bajadas | C (o H,L) | **RSI**, volumen direccional, asimetría del perfil de sesión | **Baja: familia poco poblada** | Única que descompone el movimiento por signo |
| **F7** | **Actividad / participación** | Intensidad de la negociación y su relación con el movimiento | V, C | Volumen relativo, OBV, Índice de Demanda, lambda de Amihud aproximada, volumen en rupturas | Media | **Única fuente no derivada del precio que poseemos** |
| **F8** | **Estructura de niveles y memoria** | Dónde hubo concentración previa y cómo reacciona el precio al volver | H, L, C, V | Soportes y resistencias, cambio de polaridad, números redondos, área de valor, huecos como nivel, retrocesos respecto a impulsos | Media | **Único con mecanismo económico fuerte; único con `LOOK-AHEAD-LEVE`** |
| **F9** | **Memoria del nivel de precio** | Información contenida en el nivel absoluto o relativo, no en su variación | C | Fractional differentiation | Alta con el propio precio | `[LDP]` **Recupera lo que la diferenciación entera destruye** |
| **F10** | **Complejidad / contenido informativo** | Grado de estructura frente a aleatoriedad de la secuencia | C | Entropía (Shannon, Lempel-Ziv), estadísticos de explosividad | Baja | Mide una propiedad **de la secuencia**, no de su nivel ni de su variación |

**Dos ejes transversales que no son familias:**

| Eje | Contenido | Datos |
|---|---|---|
| **E1 — Escala temporal** | Cualquier familia puede calcularse sobre múltiples ventanas. **Es un multiplicador del espacio, no una fuente de información nueva** | Todos |
| **E2 — Posición temporal** | Hora de sesión, tiempo desde apertura, proximidad al cierre, día de la semana, cercanía al rollover | Timestamp |

## 11.2 Principio de investigación derivado

`[SÍNTESIS — INTERPRETACIÓN]` De §4.D y de esta taxonomía se deriva:

> **El espacio de features debe diseñarse por familias antes de instanciarse en indicadores concretos.**
>
> Consecuencias:
> 1. **Cada familia debería estar representada antes de que ninguna esté representada dos veces.** Diez variantes de F1 aportan menos que una de F1 más una de F6.
> 2. **Las familias F2, F6 y F10 están poco pobladas** en la literatura revisada, lo que sugiere —sin demostrarlo— que podrían contener información menos explotada.
> 3. **El eje E1 multiplica el espacio sin añadir dimensiones**: cada ventana adicional es un intento experimental (§15).
> 4. **F8 es la única familia con problema de causalidad**, y también la única con el mecanismo económico mejor respaldado. **Esa tensión es real y no se resuelve aquí** (decisión J7).

**Estatus: `[RESTRICCIÓN METODOLÓGICA]` en su punto 1, guía de proceso en el resto. No selecciona features.**

---

# §12. FILTRO DE MÍNIMA COMPLEJIDAD

Ordena el espacio de investigación. **No selecciona nada.**

## 12.1 `PRIORIDAD A` — investigación elemental

*Simple, causal, pocos parámetros, falsable, `OHLCV-OK`.*

| Elemento | GL | Familia | Por qué aquí |
|---|---|---|---|
| **ATR / medida de volatilidad** | 1 | F3 | **Normalizador universal.** Sin él, todos los umbrales son absolutos y no transferibles entre regímenes |
| **Retornos rezagados a varias escalas** | 1 | F1 | Baseline informativo obligatorio; en el ejemplo intradiario de Jansen fueron **las variables más informativas** (`KB01 §20.2`) |
| **Tendencialidad (ADX / coef. de eficiencia)** | 1 | F2 | Variable de régimen causal y adimensional; soporta H3 |
| **Ancho de banda de volatilidad** | 1 | F3 | Régimen de compresión/expansión; soporta H4 y H13 |
| **Posición en el rango de N barras** | 1 | F4 | Adimensional; unifica estocástico, %R y ruptura de canal; soporta H7 |
| **Geometría elemental de vela** | **0** | F4/F3 | Cinco ratios sin parámetros que agotan la información de una barra; soporta H8 |
| **Volumen relativo** | 1 | F7 | Única fuente no-precio; soporta H6 |
| **OBV** | **0** | F7 | Cero parámetros |
| **RSI** | 1 | F6 | Única familia de asimetría |
| **Día de cambio** | 0–2 | F4/F3 | Evento causal sin pivotes, con mecanismo; soporta H9 |
| **Hueco como evento** | 1 | F8 | Detección trivial y causal |
| **Estacionalidad intradiaria** | 0–1 | E2 | Soporta H10; **y es control obligatorio contra el falso descubrimiento por reloj** |
| **Distancia a números redondos** | 1 | F8 | Sin ambigüedad de detección; soporta H17 |
| **Asimetría temporal** | 1 | F2 | Soporta H14 |
| **Ajuste de rollover** | 2 | — | **Preprocesado obligatorio, no opcional** (§3.12) |
| **Baselines triviales** | 0 | — | Predicción nula, posición constante, AR sobre lags |

## 12.2 `PRIORIDAD B` — investigación posterior

*Razonable, más grados de libertad.*

| Elemento | GL | Reserva |
|---|---|---|
| Medias y derivados (distancia, pendiente, cruces, MACD) | 1–3 | **F1: máxima redundancia interna.** Elegir representantes |
| CCI / posición en bandas / STARC / Keltner | 1–3 | F5 es cociente de F1 y F3; **STARC y Keltner tienen interpretaciones opuestas** |
| Muestreo por eventos (CUSUM) | 2 | Barato; ataca la unicidad en la raíz; **cada umbral es un intento** |
| Triple barrera sobre cierres | 3–4 | Requiere fijar barreras y horizonte |
| Estructura de niveles (F8) como densidad ponderada por recencia | 3–5 | **`LOOK-AHEAD-LEVE`**; requiere declarar `k`; mejor mecanismo económico |
| Barras de volumen / dólar aproximadas | 2 | Medir el error de aproximación antes de creerlas |
| Multi-horizonte | k | Multiplica el espacio de búsqueda |
| Meta-labeling | — | Segunda superficie de sobreajuste |
| Sizing por probabilidad | 1–2 | **Depende de calibración, que es `[VACÍO]`** |
| Sample weights (unicidad, atribución, decay) | 1–3 | Baratos; cada configuración es un intento |
| Divergencia como discrepancia continua | 2–4 | Reformulación causal; **no es la divergencia de Murphy** |
| Extensión del rango de sesión | 2 | Requiere resolver D1 |
| Puntos pivote intradía | 1–3 | Objetivos y causales; requieren resolver D1 |

## 12.3 `PRIORIDAD C` — sólo con evidencia previa

| Elemento | Motivo |
|---|---|
| **Fractional differentiation** | Debe demostrar aporte incremental sobre retornos; **feature con correlación ~0.995 con el precio es vehículo de memorización** |
| **Entropía** | Sin evidencia en las fuentes; muy sensible a tres parámetros → **coste en presupuesto de intentos** |
| **SADF / QADF / tests SM** | **Coste cuadrático**: ~242 PFLOPs para 356k barras según `KB02 §21.3`. Inviable en intradiario sin paralelización seria |
| **Sequential bootstrap** | Coste cuadrático para mejora modesta (unicidad 0.6→0.7); `max_samples` captura gran parte a coste nulo |
| **CPCV** | Cambia cualitativamente la evidencia, pero coste multiplicativo. `[PREGUNTA EMPÍRICA]` H4 sobre viabilidad |
| **P&F como esquema de muestreo** | Transforma el dataset entero; complica la alineación con targets temporales |
| **Market Profile aproximado** | Supuesto de continuidad intrabar; requiere D1 |
| **Detectores de patrones nominales** | ≥9 GL; Murphy advierte que en futuros **se completan menos** |
| **Backtesting sobre datos sintéticos** | Capa entera de supuestos para un problema que las barreras por volatilidad ya mitigan |

## 12.4 `NO PRIORIZAR`

| Elemento | Motivo | Categoría |
|---|---|---|
| **Ondas de Elliott** | Recuento no único, excepciones no especificadas, grado no acotado. **El conjunto de trayectorias incompatibles con la teoría es prácticamente vacío** | `[DESCARTABLE METODOLÓGICAMENTE]` — no falsable |
| **Identificación de ciclos por inspección/ajuste** | "Ajustar hasta encontrar el ajuste adecuado"; sin criterio de significación; períodos que "cambian continuamente" | `[DESCARTABLE METODOLÓGICAMENTE]` — look-ahead grave |
| **Líneas de tendencia geométricas, Gann, abanico** | ≥7 GL; **no invariantes de escala**; el propio Murphy critica las de Gann | `[DESCARTABLE METODOLÓGICAMENTE]` en su forma original |
| **Líneas internas** | Maximizan explícitamente el ajuste a datos pasados | `[DESCARTABLE METODOLÓGICAMENTE]` |
| **Media centrada** | Requiere barras futuras por construcción | `[DESCARTABLE METODOLÓGICAMENTE]` — look-ahead grave |
| **Umbrales fijados por inspección visual del histórico completo** | Look-ahead; sustituibles por cuantiles móviles | `[DESCARTABLE METODOLÓGICAMENTE]` en su forma original |
| **Taxonomía de huecos** (separación/escape/agotamiento) | La clasificación se define por la posición dentro de un movimiento cuya extensión sólo se conoce a posteriori | `[DESCARTABLE METODOLÓGICAMENTE]` — el evento sí, el tipo no |
| **Platillo y púa** | El propio autor admite que no se puede establecer cuándo están completos ni medir su objetivo | `[DESCARTABLE METODOLÓGICAMENTE]` |
| **Estacionalidad anual** | Escala inadecuada para intradiario; 14–15 observaciones por mes; sin control de multiple testing | `[FUERA DE ALCANCE ACTUAL]` |
| **Interpretación psicológica de la forma de la vela** | Requiere secuencia intrabar | `[FUERA DE ALCANCE ACTUAL]` — `GRANULAR` |
| **Barras de imbalance y de runs** | Requieren firmar operaciones; **`KB02 §3.3` advierte contra fabricar sustitutos desde el signo de barra** | `[FUERA DE ALCANCE ACTUAL]` |
| **Interés abierto, amplitud, sentimiento, intermercado** | `OTRAS FUENTES` | `[FUERA DE ALCANCE ACTUAL]` |
| **HRP y optimización de cartera** | Requiere múltiples activos | `[FUERA DE ALCANCE ACTUAL]` |
| **Deep Learning como punto de partida** | `KB01 §13.3` establece condiciones previas que aún no se cumplen (baselines, validación resuelta, datos suficientes, razón estructural) | `[DECISIÓN DE DISEÑO ABIERTA]` diferida, no descartada |

`[SÍNTESIS — INTERPRETACIÓN]` **Observación de conjunto:** el filtro produce un resultado asimétrico respecto a la reputación de las técnicas. En `PRIORIDAD A` quedan mayoritariamente **medidas escalares de cero a dos parámetros**; en `NO PRIORIZAR` cae precisamente **aquello por lo que el análisis técnico es públicamente conocido**. La regularidad, ya identificada en `KB03 §25.4`: **las técnicas que sobreviven se definen por una fórmula; las que caen se definen por un dibujo.**

Y una advertencia simétrica: **esto no significa que las técnicas simples funcionen.** Significa que son las únicas cuya falsedad o veracidad podemos establecer con los recursos disponibles. `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` **Priorizar por falsabilidad no es priorizar por probabilidad de éxito.**

---

# §13. CAUSALIDAD Y LOOK-AHEAD COMO RESTRICCIÓN TRANSVERSAL

`[RESTRICCIÓN METODOLÓGICA]` de primer orden (§3.2). Integra las advertencias de las tres KB.

## 13.1 Escala de causalidad unificada

Adoptada de `KB03 §0.3` y aplicable a las tres fuentes:

| Nivel | Significado |
|---|---|
| **`CAUSAL`** | Calculable en `t` con información disponible hasta `t`, sin ambigüedad |
| **`CAUSAL-CONF`** | Calculable sólo tras un evento de confirmación posterior; la señal existe pero **llega con retardo estructural** |
| **`LOOK-AHEAD-LEVE`** | Requiere confirmación de barras futuras para fijar un punto; formalizable **declarando el retardo explícitamente** |
| **`LOOK-AHEAD-GRAVE`** | Sólo identificable conocido el desenlace. **No formalizable causalmente sin reformular el concepto** |

## 13.2 Tabla de riesgos

| Riesgo | Cómo aparece | Qué componentes afecta | Prevención conceptual |
|---|---|---|---|
| **Pivotes** | Un máximo o mínimo local sólo se conoce como tal tras `k` barras posteriores. `[MURPHY]`: "el chartista sólo puede estar razonablemente seguro… después de que los precios hayan comenzado a subir" (`KB03 §4.7`) | Estructura HH/HL, soportes, resistencias, líneas, canales, retrocesos, divergencias, patrones, ondas, familia F8 completa | **Declarar `k` explícitamente y aceptar el retardo.** La versión sin `k` es look-ahead. `[DECISIÓN DE DISEÑO ABIERTA]` J7 |
| **Soportes y resistencias** | Seleccionar niveles mirando el gráfico completo | F8 | Densidad de actividad calculada sólo con historia previa a `t`, con ventana declarada |
| **Divergencias** | Emparejar extremos de precio con extremos de indicador. **`[VACÍO]`: ninguna fuente especifica la ventana de emparejamiento** (`KB03 §10.12`) | Osciladores, volumen | Reformular como discrepancia continua entre variaciones normalizadas sobre ventana móvil |
| **Patrones chartistas y de velas nominales** | Requieren pivotes más umbrales de forma | F8 | Reformular como componentes continuos (compresión, expansión, amplitud relativa) |
| **Medias centradas** | Por construcción usan barras posteriores | Cualquier suavizado | **Prohibidas.** Sólo medias rezagadas |
| **Suavizado no causal** | Kalman en modo *smoothing*, reconstrucción wavelet sobre la serie completa (`KB01 §6.4`) | Denoising, fracdiff con ventana expansiva mal implementada | Sólo filtros estrictamente causales. **Test:** si el valor en `t` cambia al añadir datos posteriores a `t`, hay leakage |
| **Ciclos** | "Ajustar período y fase hasta encontrar el ajuste adecuado" (`KB03 §14.5`) | Cualquier feature cíclica | `[DESCARTABLE METODOLÓGICAMENTE]` en su forma original |
| **Elliott** | El recuento se revisa continuamente según el desenlace | — | `[DESCARTABLE METODOLÓGICAMENTE]` |
| **Labeling con umbrales globales** | Definir clases o barreras sobre la distribución de toda la muestra | Targets | Umbrales derivados de volatilidad estimada causalmente, o cuantiles expansivos |
| **Normalización y escalado** | Z-scores globales; escaladores ajustados sobre el dataset completo (`KB01 §16` escenario 1) | Todas las features | **Ajustar transformaciones sólo con datos de entrenamiento.** `[RESTRICCIÓN METODOLÓGICA]` |
| **Imputación** | Rellenar huecos con información posterior | Preprocesado | Imputación causal o exclusión |
| **Early stopping** | Parar el entrenamiento usando el conjunto que después se reporta. `[LDP]` y `[JANSEN]` lo advierten independientemente | Entrenamiento | **El conjunto de parada nunca puede ser el de reporte** |
| **Tuning de hiperparámetros** | El mismo test usado N veces. **Purged CV no protege de esto** (`KB02 §13.4`) | Selección de modelo | Presupuesto explícito de búsqueda + conjunto que no participó en la selección |
| **Solapamiento de etiquetas** | Etiquetas derivadas de períodos que se intersectan | Train/test | **Purging** por concurrencia + **embargo** hacia adelante (`KB02 §11`) |
| **Correlación serial de features** | Las features de barras contiguas comparten historia aunque las etiquetas no se solapen | Train/test | **Embargo** posterior al test (`KB02 §11.4`) |
| **Rollover no ajustado** | Salto artificial en fechas conocidas y de signo posiblemente sistemático | Toda la serie | Ajuste explícito; **precios ajustados para PnL, crudos para dimensionar** (`KB02 §4.3`) |
| **Ambigüedad intrabar** | Con `(O,H,L,C)` no se conoce el orden entre H y L | Triple barrera con extremos, P&F, Market Profile | **`[VACÍO]` en las tres fuentes.** Opciones: usar cierres; usar extremos con regla de desempate declarada; aumentar resolución. `[DECISIÓN DE DISEÑO ABIERTA]` F5 |
| **Hold-out contaminado** | Mirarlo, ajustar, volver a mirar | Evaluación final | Protocolo escrito; registro de accesos (`KB01 §15.2`) |
| **Estacionalidad como atajo** | El modelo aprende el perfil de sesión en lugar del mercado | Features de calendario | Evaluar rendimiento **condicionado a franja horaria**; baseline que use sólo variables de tiempo |

## 13.3 Regla general

`[RESTRICCIÓN METODOLÓGICA]`
> **Toda técnica que requiera información futura debe quedar: (a) reformulada causalmente con retardo explícito y declarado, o (b) descartada en su forma original.**
>
> **Test operativo universal:** si el valor de una variable en `t` cambia al añadir observaciones posteriores a `t`, hay leakage. Es aplicable a features, etiquetas, normalizaciones y filtros por igual.

---

# §14. MARCO UNIFICADO DE EVIDENCIA

**¿Qué evidencia necesitaremos para creer que un hallazgo sobre MNQ es real?** El encargo pide derivarla de las fuentes, no inventar requisitos.

## 14.1 El escalón de evidencia y su respaldo

| # | Escalón | Qué establece | Respaldo | Qué NO puede afirmarse aún |
|---|---|---|---|---|
| **1** | **Racional / hipótesis con mecanismo** | Que existe una razón por la que un agente perdería dinero frente a nosotros | `[LDP]` teoría antes de estrategia (`KB02 §1.7`); `[JANSEN]` intuición económica previa (`KB01 §1.2`); `[MURPHY]` "si no tiene sentido, es coincidencia" (`KB03 §20.C.3`) | Nada sobre el mercado |
| **2** | **Definición causal** | Que la hipótesis es computable en `t` sin información futura, con grados de libertad declarados | `[LDP]` §11; `[MURPHY]` criterio de las 100 personas (`KB03 §20.C.1`) | Nada sobre su valor |
| **3** | **Evidencia univariada** | Que la variable se asocia con el retorno futuro en la muestra | `[JANSEN]` IC, MI, análisis por quantiles **con dispersión** (`KB01 §7`); `[LDP]` SFI (`KB02 §12.4`) | **Nada sobre rentabilidad**: caso Alpha 054 (`KB01 §7.6`) |
| **4** | **Estabilidad temporal** | Que la asociación no depende de un período o régimen | `[MURPHY]` criterio explícito (`KB03 §20.C.5`); `[JANSEN]` factor decay; `[LDP]` structural breaks | Que generalice fuera de muestra |
| **5** | **Información incremental** | Que aporta sobre baselines y sobre features ya presentes | `[LDP]` MDA con purged CV, **que puede concluir que ninguna feature es informativa** (`KB02 §12.4`); `[JANSEN]` baselines | Que sea monetizable |
| **6** | **Modelo fuera de muestra** | Que un modelo entrenado sin ver el test predice mejor que el baseline | `[JANSEN]` hold-out de un solo uso; `[LDP]` purged CV / CPCV | Que el edge sobreviva a costes |
| **7** | **Robustez** | Que el resultado no se rompe al perturbar parámetros, período o semilla | `[MURPHY]` estabilidad paramétrica y temporal; `[LDP]` test del bagging; `[JANSEN]` fragilidad de las CNN | Que sea rentable |
| **8** | **Viabilidad económica** | Que el edge por operación supera los costes, con la frecuencia y estructura de pagos previstas | `[LDP]` marco de riesgo de estrategia (`KB02 §19`); `[MURPHY]` promedio por operación > costes; `[JANSEN]` rendimiento por turnover | Que la estrategia completa funcione |
| **9** | **Backtest** | Comprobación de sanidad sobre sizing, turnover, resistencia a costes y comportamiento bajo escenario | `[LDP]` **"no es una herramienta de investigación"**; `[JANSEN]` sirve para descartar | Que funcione en vivo. **Y ni siquiera que hubiera funcionado**: es una hipótesis, no un experimento (`KB02 §15.1`) |
| **10** | **Corrección por intentos** | Que el resultado sobrevive a la deflación por el número de pruebas | `[LDP]` DSR, PBO; `[JANSEN]` deflated Sharpe, longitud mínima | — |
| **11** | **Paper trading** | Que las latencias, retardos y ejecución reales no destruyen el edge | `[LDP]` ciclo de vida (`KB02 §1.4`); `[MURPHY]` implícito | Que persista |
| **12** | **Monitorización en vivo** | Que sigue funcionando | **`[VACÍO]` en las tres fuentes** sobre el protocolo | — |

## 14.2 Las cuatro fronteras que el encargo pide aclarar

`[SÍNTESIS — INTERPRETACIÓN]`

**Qué puede afirmarse ANTES de cualquier ML (escalones 1–4):**
- Que una variable es causalmente computable y con cuántos grados de libertad.
- Que se asocia univariadamente con el retorno futuro, y con qué dispersión.
- Que la asociación es o no estable entre períodos y regímenes.
- **Que un diseño es económicamente inviable**, mediante el marco de riesgo de estrategia: dada una estructura de pagos y una frecuencia, qué precisión haría falta. **Esto es notable: se puede refutar un diseño antes de entrenar nada** (`KB02 §19.6`).

**Qué puede afirmarse ANTES del backtest (escalones 5–7):**
- Que existe información incremental sobre baselines, fuera de muestra.
- Que el resultado es robusto a perturbaciones.
- **Que ninguna feature es informativa** — MDA puede establecerlo, y ningún backtest lo hará nunca.

**Qué sólo puede afirmarse DESPUÉS del backtest (escalones 8–10):**
- Que el edge sobrevive a costes y turnover con una regla operativa concreta.
- Que el perfil de riesgo (drawdown, concentración temporal, tiempo bajo agua) es aceptable.
- **Con la advertencia de LdP**: un backtest impecable probablemente esté equivocado, porque producirlo requiere experiencia y la experiencia implica intentos previos (`KB02 §15.2`).

**Qué sólo puede afirmarse DESPUÉS de paper trading o live (escalones 11–12):**
- Que la ejecución real preserva el edge.
- Que el sistema sigue siendo válido. **Y aquí las tres fuentes coinciden en que la validez caduca**: factor decay, structural breaks, relaciones que cambian con el régimen.

## 14.3 Regla de progresión

`[RESTRICCIÓN METODOLÓGICA]`
> **Un escalón no puede saltarse invocando el resultado de uno posterior.** Concretamente: **un buen backtest no sustituye a la evidencia de los escalones 1–7**, y `[LDP]` es explícito en que usar el backtest para redefinir el sistema invalida el proceso (`KB02 §15.3`).

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` La consecuencia práctica es que **la mayor parte del trabajo de IRIS debería ocurrir en los escalones 1–7**, donde las tres fuentes coinciden en que reside la investigación real, y el backtest debería aparecer una sola vez y tarde.

---

# §15. MULTIPLE TESTING Y PRESUPUESTO DE INVESTIGACIÓN

**El riesgo inmediato que el encargo identifica:** las tres KB han generado ~18 familias de hipótesis, 10 familias informativas, decenas de técnicas y centenares de parametrizaciones posibles. **Usar la bibliografía como excusa para probar cientos de combinaciones sería el modo de fallo más probable del proyecto.**

## 15.1 Las magnitudes que las fuentes aportan

| Dato | Fuente |
|---|---|
| **~20 iteraciones** del ciclo datos→ML→backtest bastan para "descubrir" una estrategia falsa al 5% | `[LDP]` `KB02 §1.5` |
| **2 años de datos diarios no sostienen conclusiones sobre más de ~7 estrategias; 5 años, ~45** | `[JANSEN]` `KB01 §15.5` |
| El máximo esperado de N estimaciones de Sharpe es **mayor que cero aunque el Sharpe real sea cero**, y crece con N y con la varianza entre intentos | `[LDP]` `KB02 §18.5` |
| **Menos del 5% de las ideas se transforman en beneficios** | `[MURPHY]` `KB03 §20.C.3` |
| El DSR es **incalculable sin el registro de intentos** | `[LDP]` `KB02 §18.5` |

`[SÍNTESIS — INTERPRETACIÓN]` La cifra de Jansen es la más operativa y la más incómoda: está expresada en **años de datos diarios**, y su traducción a intradiario **no es trivial** porque depende del número de observaciones *independientes*, no de barras (G1). **Un millón de barras de un minuto no autoriza un millón de pruebas.**

## 15.2 Qué cuenta como experimento nuevo

`[RESTRICCIÓN METODOLÓGICA]` El encargo lo exige explícitamente: **cambiar RSI 14 → RSI 13, horizonte 30 → 45 o barrera 1σ → 1.2σ aumenta los grados de libertad.**

| Situación | ¿Experimento nuevo? | Razón |
|---|---|---|
| Cambiar el valor de un parámetro (ventana, umbral, barrera, horizonte) | **SÍ** | Es una configuración distinta evaluada sobre los mismos datos |
| Cambiar de indicador dentro de la misma familia informativa | **SÍ** | Aunque la información sea redundante, la evaluación es un intento |
| Cambiar de familia de modelo | **SÍ** | — |
| Cambiar hiperparámetros del modelo | **SÍ.** `[LDP]`: la CV contribuye al sobreajuste a través del tuning (`KB02 §13.4`) | Purged CV no protege de esto |
| Cambiar el esquema de muestreo, el target o el etiquetado | **SÍ, y de forma especialmente costosa** | Modifican el dataset entero |
| Reejecutar el mismo experimento con otra semilla | **NO es experimento nuevo; es estimación de varianza del mismo** | Pero **reportar la mejor semilla sí lo es** |
| Ejecutar el mismo experimento en otro fold de la misma CV | **NO** | Es parte de la estimación |
| Evaluar la misma configuración con otra métrica y elegir la favorable | **SÍ** | Selección sobre el resultado |
| Explorar los datos sin ajustar nada (estadística descriptiva) | **NO, si no se usa para seleccionar hipótesis** | **Ambiguo si sí.** Ver 15.4 |

## 15.3 Diseño conceptual del registro

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` Sin implementar, lo que el registro debe capturar para que el DSR sea calculable y el resultado interpretable:

- **Identificador y fecha** de cada intento, incluidos los abandonados.
- **Especificación completa**: esquema de muestreo, target, horizonte, barreras, conjunto de features, modelo, hiperparámetros, esquema de validación.
- **Métrica resultante**, y **todas** las métricas calculadas (no sólo la reportada).
- **Motivo del intento**: hipótesis derivada de mecanismo, o exploración.
- **Resultado**: continuado, abandonado, o archivado.
- **Enlace al intento anterior** del que deriva, para reconstruir el árbol de búsqueda.

**Los dos insumos que el DSR necesita** y que sólo existen si se registran desde el principio: **el número de intentos independientes** y **la varianza entre sus Sharpes** (`KB02 §18.5`).

## 15.4 Tres problemas no resueltos

`[VACÍO]` **(a) Corrección del score de validación por el tuning.** `KB02 §13.4` lo declara vacío: el DSR corrige Sharpes de estrategias, no scores de validación de hiperparámetros. **Ninguna fuente lo resuelve.**

`[VACÍO]` **(b) Contabilidad de la exploración de datos.** Si el análisis empírico de MNQ (§17) sugiere qué hipótesis probar, **esa exploración ha consumido presupuesto**. Ninguna fuente aborda cómo contabilizar el análisis exploratorio previo a la formulación. `[SÍNTESIS — INTERPRETACIÓN]` Una vía conservadora sería **separar el histórico desde el principio**, reservando un tramo que no participe ni en la exploración ni en el desarrollo. Es interpretación nuestra, no propuesta de ninguna fuente.

`[VACÍO]` **(c) Herencia de intentos ajenos.** `[LDP]` señala que el riesgo incluye backtests hechos por otros sobre los mismos datos, y que por eso es "muy difícil de evitar" (`KB02 §15.4`). **Al partir de tres libros que catalogan técnicas ya exploradas por la industria durante décadas, IRIS hereda un sesgo de selección incuantificable.** Ninguna fuente ofrece corrección.

## 15.5 Consecuencias operativas

`[RESTRICCIÓN METODOLÓGICA]`
1. **El registro de intentos es requisito técnico, no buena práctica.** Sin él, el resultado final es literalmente ininterpretable.
2. **El presupuesto de pruebas debe fijarse antes de empezar**, en función de G1 (observaciones independientes), no del número de barras.
3. **La prioridad de las hipótesis debe decidirse por mecanismo, no por facilidad de cómputo**, porque cada prueba consume presupuesto escaso.
4. **Preferir búsqueda con presupuesto explícito** (aleatoria acotada) sobre búsqueda exhaustiva, no sólo por coste sino por control del multiple testing (`KB02 §13.2`).
5. **La agrupación por familias informativas (§11) reduce el presupuesto consumido**, porque evita evaluar diez transformaciones de la misma información como si fueran diez hipótesis.

---

# §16. QUÉ PUEDE RESOLVERSE AHORA Y QUÉ NO

## A. Puede establecerse desde la bibliografía

Sólo los principios genuinamente respaldados (§3), reformulados como restricciones operativas:

| # | Principio establecido | Nivel |
|---|---|---|
| A1 | Predicción estadística ≠ rentabilidad. Ninguna métrica de clasificación o correlación es evidencia de viabilidad sin traducción económica | `[CONSENSO FUERTE]` |
| A2 | Causalidad temporal estricta; toda técnica con look-ahead se reformula con retardo explícito o se descarta | `[CONSENSO FUERTE]` |
| A3 | Las observaciones no son independientes; el número de filas no es el tamaño muestral | `[CONSENSO FUERTE]` |
| A4 | Toda complejidad adicional debe demostrar valor incremental sobre un baseline, fuera de muestra | `[CONSENSO FUERTE]` |
| A5 | Los costes y la ejecución son parte de la viabilidad, no del cierre | `[CONSENSO FUERTE]` |
| A6 | La importancia de features no puede interpretarse sin controlar la redundancia previamente | `[CONSENSO FUERTE]` |
| A7 | El ratio señal/ruido es bajo: esperar edges pequeños e inestables | `[CONSENSO FUERTE]` |
| A8 | Toda modelización requiere elegir un modelo, y ninguno puede elegirse a priori (*no free lunch*) | `[CONSENSO FUERTE]` |
| A9 | Registro de intentos y corrección por multiple testing | `[CONVERGENCIA]` J+L, ausente en M |
| A10 | Ninguna señal se convierte en estrategia sin un mecanismo propuesto | `[CONVERGENCIA]` |
| A11 | Un resultado se juzga por su estabilidad entre períodos y regímenes, no sólo por su valor agregado | `[CONVERGENCIA]` |
| A12 | El backtest se ejecuta sobre un sistema especificado y no se usa para redefinirlo sin contabilizar el intento | `[CONVERGENCIA]` |
| A13 | El tratamiento del rollover es preprocesado obligatorio | `[CONVERGENCIA]` |
| A14 | Las transformaciones (escalado, normalización, imputación, denoising) se ajustan sólo con datos de entrenamiento y son estrictamente causales | `[CONSENSO FUERTE]` derivado de A2 |
| A15 | Purging por solapamiento y embargo por correlación serial cuando las etiquetas abarcan varias barras | `[COMPLEMENTARIEDAD]` L, aceptada por J |
| A16 | El escalón de evidencia de §14 y su regla de no salto | `[CONVERGENCIA]` |
| A17 | El espacio de features se diseña por familias informativas antes de instanciarse en indicadores | `[COMPLEMENTARIEDAD]` §4.D |
| A18 | Los distintos motivos de no operar son estados conceptualmente distintos y no deben colapsarse sin justificación | `[HIPÓTESIS ESTRUCTURAL]` §7.5 |

## B. Puede descartarse metodológicamente

**No porque no funcione, sino porque su formulación actual viola una condición necesaria.**

| Elemento | Condición violada |
|---|---|
| **Ondas de Elliott** | No falsabilidad: excepciones no especificadas, grado no acotado, recuento no único |
| **Identificación de ciclos por ajuste visual** | Look-ahead grave; sin criterio de significación; períodos declaradamente inestables |
| **Medias centradas** | Look-ahead por construcción |
| **Suavizado no causal** (Kalman *smoothing*, wavelets sobre serie completa) | Look-ahead |
| **Umbrales fijados por inspección del histórico completo** | Look-ahead; sustituibles por cuantiles móviles |
| **Taxonomía de huecos** (el tipo, no el evento) | Clasificación definida por el desenlace |
| **Platillo y púa** | Sin criterio de finalización según el propio autor |
| **Líneas de tendencia geométricas, Gann, ángulos de 45°** | No invariantes de escala; ≥7 GL no especificados |
| **Líneas internas** | Maximizan explícitamente el ajuste a datos pasados |
| **Selección de indicadores "por comodidad"** | No reproducible |
| **Uso del backtest para redefinir el sistema sin contabilizar** | Multiple testing incontrolado |
| **Inspección visual como evidencia** | No reproducible ni corregible por intentos |
| **Rechazo del out-of-sample** (apéndice C de Murphy) | Justificación circular; contradice al propio cap. 9 |
| **Barras de imbalance fabricadas desde el signo de barra** | El sustituto no mide la magnitud que pretende (`KB02 §3.3`) |

`[SÍNTESIS — INTERPRETACIÓN]` **Todos son descartes de forma, no de fondo.** Varios admiten reformulación causal: la estructura de niveles con `k` declarado, la divergencia como discrepancia continua, los patrones como componentes (compresión → expansión). **Descartar la forma no descarta la hipótesis subyacente.**

## C. Requiere análisis empírico del MNQ

**El grupo más importante.** Desarrollado como agenda en §17. Cubre: A1–A4, B1–B4, C1–C4, D1–D3, F5, G1, G3, H4, I2, J1–J2, J8, K1–K3, L1, L4, P1–P4.

## D. Requiere una decisión del usuario o del proyecto

**No son conclusiones científicas.** Mezclarlas con C sería un error de categoría.

| # | Decisión | Naturaleza del compromiso |
|---|---|---|
| **T1** | ¿Instrumento único o universo? | **Potencia estadística frente a complejidad operativa.** §8 documenta exactamente qué se pierde y qué defensas sustitutivas existen. Ninguna es equivalente |
| **T2** | ¿OHLCV o datos más granulares? | **Espacio de hipótesis accesible frente a dependencia de proveedores.** §9 documenta que el núcleo metodológico no se ve afectado, pero sí una familia entera de hipótesis |
| **T3** | ¿Qué coste computacional es aceptable? | Condiciona CPCV, sequential bootstrap, SADF, detectores paramétricos y el tamaño del espacio de búsqueda |
| **O5** | ¿Qué drawdown y tiempo bajo agua son tolerables? | Preferencia de riesgo. **Determina el escalón 8 del marco de evidencia** |
| **I4** | ¿Qué presupuesto de intentos se acepta? | Compromiso entre exhaustividad y credibilidad del resultado |
| **—** | ¿Qué se hace si la respuesta a P4 es negativa? | **Decisión de proyecto que conviene tomar antes de empezar**, para que el resultado negativo sea un resultado y no una crisis |

---

# §17. AGENDA DEL ANÁLISIS EMPÍRICO DEL MNQ

**Qué estudiar en los datos ANTES de formular el problema de ML.** Ordenada por dependencia. **No se ejecuta aquí.**

## FASE 0 — Integridad y construcción de la serie
*Bloquea todo lo demás. Ningún resultado posterior es interpretable si esta fase falla.*

| # | Qué establecer | Resuelve |
|---|---|---|
| 0.1 | Inventario del histórico: rango, contratos presentes, identificador de contrato disponible o no | A1, A4 |
| 0.2 | Timestamps: zona horaria, consistencia, alineación, presencia de DST | A3 |
| 0.3 | Barras faltantes, días incompletos, gaps de cotización, precios repetidos, volúmenes cero | A3 |
| 0.4 | Fechas de rollover: identificación por cambio de contrato o por erosión de volumen | A1 |
| 0.5 | Magnitud y signo de los saltos de roll; ¿son sistemáticos? | A1 |
| 0.6 | Comportamiento del volumen en la transición de contratos | A2 |
| 0.7 | Construcción de al menos dos series continuas por métodos distintos, y **comparación de sus retornos** | A1 |

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` El punto 0.7 es importante: **si dos métodos de empalme razonables producen retornos materialmente distintos, esa diferencia es una fuente de incertidumbre que se propaga a todo lo demás** y debe cuantificarse, no elegirse arbitrariamente.

## FASE 1 — Estructura temporal y definición de sesión
*Depende de FASE 0. Bloquea el muestreo y el etiquetado.*

| # | Qué establecer | Resuelve |
|---|---|---|
| 1.1 | Perfil de volatilidad por hora y por minuto de la sesión, a lo largo de varios años | D2 |
| 1.2 | Perfil de volumen por hora y por minuto | D2 |
| 1.3 | Estabilidad interanual de ambos perfiles | D2 |
| 1.4 | Caracterización de los tramos: RTH, overnight, solapamiento europeo, apertura, cierre | D1 |
| 1.5 | Proporción del movimiento diario que ocurre en cada tramo | D1 |
| 1.6 | ¿Qué delimitación de "sesión" es defendible y qué consecuencias tiene cada alternativa? | **D1 (`[VACÍO]` bibliográfico)** |

## FASE 2 — Propiedades estadísticas
*Depende de FASE 0 y 1 (para condicionar por tramo).*

| # | Qué establecer | Resuelve |
|---|---|---|
| 2.1 | Distribución de retornos a varias resoluciones: colas, asimetría, curtosis | B1 |
| 2.2 | Autocorrelación de retornos a distintos lags, **globalmente y condicionada a tramo de sesión** | B1, B2 |
| 2.3 | Autocorrelación de retornos absolutos o cuadrados: clustering de volatilidad y su persistencia | B1, H4 |
| 2.4 | Estacionariedad: ADF sobre precio, log-precio y retornos; y `d*` de diferenciación fraccionaria | B4, H15 |
| 2.5 | Estabilidad de todo lo anterior entre subperíodos | B1, A11 |
| 2.6 | Presencia de rupturas estructurales detectables a bajo coste (CUSUM sobre niveles) | K1 |

`[SÍNTESIS — INTERPRETACIÓN]` **El resultado de 2.2 y 2.3 es de los más informativos de toda la agenda.** Si —como es habitual en mercados líquidos— la autocorrelación de retornos es cercana a cero y la de retornos absolutos es fuerte y persistente, eso indica que **la señal explotable, si existe, no es una relación lineal simple sobre el primer momento**, sino no lineal, condicional al régimen, o localizada en el segundo momento (B3).

## FASE 3 — Muestreo y unidad de observación
*Depende de FASE 1 y 2.*

| # | Qué establecer | Resuelve |
|---|---|---|
| 3.1 | Propiedades de los retornos a distintas resoluciones base: ¿a cuál mejoran la normalidad y disminuye la autocorrelación espuria? | C1 |
| 3.2 | Error de aproximación de barras de volumen y de dólar construidas desde barras temporales | C2 |
| 3.3 | Comparación de propiedades estadísticas entre esquemas de muestreo | C2 |
| 3.4 | Comportamiento de un filtro de eventos (CUSUM) sobre distintas variables y umbrales: número de eventos, distribución temporal, concentración por tramo de sesión | C3 |
| 3.5 | ¿Los eventos seleccionados se concentran en franjas horarias concretas? | C3, D3 |

## FASE 4 — Independencia efectiva
*Depende de FASE 3, y es circular con FASE 5. Ver §18.*

| # | Qué establecer | Resuelve |
|---|---|---|
| 4.1 | Para varios horizontes candidatos y esquemas de muestreo: concurrencia y **unicidad media** | G1 |
| 4.2 | **Número efectivo de observaciones independientes** bajo cada combinación | **G1 — insumo del presupuesto de intentos** |
| 4.3 | Pérdida de conjunto de entrenamiento por purging y embargo bajo cada combinación | G3 |
| 4.4 | Persistencia de las señales candidatas: cuántas barras se mantiene un estado antes de cambiar | Q3 (proxy de amplitud) |

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` **4.2 es el resultado más consecuente de toda la agenda**, porque fija el presupuesto de multiple testing (§15) y por tanto **cuántas de las 18 familias de hipótesis podemos permitirnos evaluar**.

## FASE 5 — Viabilidad económica previa
*Puede ejecutarse en paralelo a FASE 4. **No requiere modelo.***

| # | Qué establecer | Resuelve |
|---|---|---|
| 5.1 | Costes reales de operar MNQ: comisión, spread típico y su variación por tramo horario, slippage estimado | P1 |
| 5.2 | Distribución de magnitudes de movimiento a distintos horizontes: ¿qué proporción supera el coste de ida y vuelta? | P2 |
| 5.3 | **Análisis de viabilidad *ex-ante***: para combinaciones plausibles de estructura de pagos y frecuencia, qué precisión sería necesaria | **P2 — puede refutar diseños antes de construirlos** |
| 5.4 | Relación entre frecuencia de operación, edge por operación y coste total | P3 |

`[SÍNTESIS — IMPLICACIÓN PARA IRIS]` **Esta fase puede ahorrar meses.** `KB02 §19` permite calcular, a coste computacional nulo, qué precisión exigiría un esquema dado. Si la respuesta es implausible, el diseño se descarta antes de entrenar nada.

## FASE 6 — Contraste univariado de hipótesis
*Depende de FASES 0–4. **Consume presupuesto de intentos: requiere haber fijado 4.2 primero.***

| # | Qué establecer | Resuelve |
|---|---|---|
| 6.1 | Priorización de las familias H1–H18 por mecanismo y coste, dentro del presupuesto | I2 |
| 6.2 | Para cada familia priorizada: **definición causal explícita con grados de libertad declarados** | A2 |
| 6.3 | Evidencia univariada: asociación con retorno futuro, **con dispersión, no sólo medias** | J1 |
| 6.4 | **Estabilidad de esa asociación entre subperíodos y regímenes** | A11 |
| 6.5 | Redundancia entre familias: correlación y número de condición de la matriz | J3, A6 |
| 6.6 | Contraste específico de H10 (estacionalidad intradiaria) **como baseline a superar, no sólo como hipótesis** | H10, D3 |
| 6.7 | Medición de la frecuencia de ambigüedad intrabar a cada resolución candidata | F5 |
| 6.8 | Contraste de K1–K3: ¿existen regímenes causalmente asignables y cambia la relación entre ellos? | K1, K2, K3 |

## FASE 7 — Preparación de la formulación
*Cierra la etapa de análisis y abre la de diseño.*

| # | Qué establecer |
|---|---|
| 7.1 | Síntesis: qué hipótesis sobrevivieron, con qué magnitud y qué estabilidad |
| 7.2 | Qué formulaciones del problema (E1, E2, E3) son compatibles con lo hallado |
| 7.3 | Qué presupuesto de intentos queda disponible |
| 7.4 | Reserva formal del hold-out final, no tocado en ninguna fase anterior |

`[RESTRICCIÓN METODOLÓGICA]` **El hold-out debería reservarse en la FASE 0, no en la 7.** Se registra aquí por completitud, pero la separación debe ocurrir antes de mirar nada. Ver §15.4(b).

---

# §18. GRAFO DE DEPENDENCIAS ENTRE DECISIONES

**Derivado de la síntesis, no asumido.**

```
                      [ INTEGRIDAD DE DATOS + ROLLOVER ]
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
        [ ESTRUCTURA DE SESIÓN ]         [ PROPIEDADES ESTADÍSTICAS ]
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                         [ RESOLUCIÓN BASE ]
                                    │
                                    ▼
                    ┌──── [ ESQUEMA DE MUESTREO ] ────┐
                    │                                  │
                    ▼                                  ▼
        [ EVENTOS / ANCLAJES ]              [ HORIZONTE + TARGET ]
                    │                                  │
                    └───────────────┬──────────────────┘
                                    ▼
                    [ SOLAPAMIENTO Y UNICIDAD EFECTIVA ]  ◄─── circular
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
        [ ESQUEMA DE VALIDACIÓN ]      [ PRESUPUESTO DE INTENTOS ]
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                            [ FEATURES ]
                                    │
                                    ▼
                       [ FAMILIA DE MODELO ]
                                    │
                                    ▼
                    [ PROBABILIDADES Y CALIBRACIÓN ]
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
            [ ABSTENCIÓN ]                   [ SIZING ]
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                        [ REGLA OPERATIVA COMPLETA ]
                                    │
                                    ▼
                             [ BACKTEST ]
                                    │
                                    ▼
                          [ PAPER TRADING ]
```

**Ramas transversales que no dependen del flujo principal:**

```
[ VIABILIDAD ECONÓMICA EX-ANTE ]  ──►  puede ejecutarse tras HORIZONTE+TARGET
                                       y puede refutar el diseño antes de FEATURES

[ RÉGIMEN ]  ──►  alimenta simultáneamente FEATURES, ABSTENCIÓN y
                  la evaluación condicionada en todas las etapas

[ HOLD-OUT ]  ──►  se reserva en INTEGRIDAD DE DATOS y no se toca hasta el final
```

## 18.1 Dependencias críticas que el grafo revela

`[SÍNTESIS — INTERPRETACIÓN]`

**1. La circularidad muestreo ↔ target ↔ unicidad es real y no eliminable.** No se puede calcular la unicidad sin fijar el horizonte; no se puede evaluar el horizonte sin conocer el esquema de muestreo; y la elección de muestreo debería informarse por la unicidad resultante. **Resolución práctica: iterar sobre un conjunto reducido de combinaciones candidatas fijado de antemano, contabilizando cada una como intento.**

**2. El presupuesto de intentos depende de la unicidad, y la unicidad depende de decisiones que consumen presupuesto.** Segunda circularidad. **Resolución: estimar la unicidad para un rango de combinaciones plausibles antes de comprometerse, en la FASE 4.**

**3. La validación debe fijarse ANTES que las features.** Es contraintuitivo respecto a la práctica habitual, pero se sigue de A15: el purging depende del horizonte de las etiquetas, no de las features. **Elegir features antes de tener el esquema de validación invita a evaluarlas con un procedimiento contaminado.**

**4. La calibración precede a la abstención y al sizing.** Si el mecanismo de abstención elegido depende de la confianza (§7.5, mecanismos 2 y 4), **y la calibración es `[VACÍO]` en las tres fuentes**, hay un eslabón sin respaldo bibliográfico en mitad de la cadena.

**5. El modelo es de las últimas decisiones, no de las primeras.** El grafo lo sitúa después de features, validación, presupuesto, target y muestreo. `[SÍNTESIS — IMPLICACIÓN PARA IRIS]` **Esto es exactamente lo que el encargo pedía impedir**: seleccionar un modelo antes de saber qué se intenta predecir.

**6. La viabilidad económica puede cortocircuitar el grafo.** Es la única rama que puede **refutar el diseño completo en una fase temprana**, y por eso conviene ejecutarla pronto pese a estar conceptualmente cerca del final.

---

# §19. MAPA DE DECISIONES ABIERTAS

**No selecciona alternativas.** Etapa adecuada según el grafo de §18.

| Decisión | Alternativas conocidas | Qué fuentes informan | Qué falta para decidir | Etapa adecuada |
|---|---|---|---|---|
| **Resolución base** | 1 min / varios min / otra | `[LDP]` argumenta contra el reloj; `[MURPHY]` indiferente; `[JANSEN]` usa 1 min sin justificar | Propiedades comparadas (FASE 3.1); frecuencia de ambigüedad intrabar (6.7); coste computacional | FASE 3 |
| **Definición de sesión** | RTH / Globex completo / segmentada por tramos | **`[VACÍO]` en las tres** | Perfiles de volatilidad y volumen; proporción de movimiento por tramo | FASE 1 |
| **Esquema de muestreo** | Temporal / volumen aprox. / dólar aprox. / P&F / por eventos | `[LDP]` jerarquía teórica; `[MURPHY]` P&F; `[JANSEN]` práctica | Error de aproximación; propiedades comparadas; efecto sobre unicidad | FASE 3 |
| **Event sampling** | Sin eventos / CUSUM sobre retornos / sobre retornos absolutos / sobre feature derivada | `[LDP]` `KB02 §5`; **sin criterio para el umbral** | Número y distribución de eventos; efecto sobre unicidad y sobre poder predictivo | FASE 3–4 |
| **Formulación del problema** | Predecir mercado / seleccionar momentos operables / decisión directa | Las tres, en ejes distintos (§5.1) | Resultados de FASE 6; qué hipótesis sobrevivieron | FASE 7 |
| **Target** | Retorno forward / dirección / magnitud / volatilidad / evento / resultado de regla | `[JANSEN]` forward returns; `[LDP]` triple barrera; `[MURPHY]` racional del stop | Formulación (E1); viabilidad económica (FASE 5) | FASE 7 |
| **Horizonte** | Fijo / dependiente del estado; varios candidatos | `[JANSEN]` compararlos por IC; `[LDP]` sin criterio para la barrera vertical | Unicidad resultante (4.1); distribución de magnitudes (5.2) | FASE 4–7 |
| **Labeling** | Horizonte fijo / triple barrera (8 configuraciones) / otro | `[LDP]` desarrollo completo; `[JANSEN]` `[VACÍO]`; `[MURPHY]` racional | Comparación empírica; F5 resuelto | FASE 7 |
| **Barreras contra cierres o extremos** | Cierres / High-Low con desempate / resolución más fina | **`[VACÍO]` en las tres** | Frecuencia de ambigüedad (6.7) | FASE 6 |
| **Estimador de volatilidad para umbrales** | EWM de retornos / ATR / High-Low (Parkinson) | `[LDP]` EWM en su implementación, **pero declara High-Low más preciso**; `[MURPHY]` ATR | Comparación empírica | FASE 6 |
| **Features** | Familias F1–F10 con múltiples instanciaciones | Las tres; taxonomía en §11 | Presupuesto de intentos (4.2); resultados univariados (6.3) | FASE 6 |
| **Multi-horizonte** | Una ventana / varias / roles asimétricos (contexto vs disparo) | `[MURPHY]` top-down; `[JANSEN]` multi-horizonte de targets | Redundancia entre ventanas (6.5); presupuesto | FASE 6 |
| **Regímenes** | Sin condicionar / variable continua de tendencialidad / estados discretos / latentes | `[MURPHY]` ADX y coef. eficiencia; `[LDP]` structural breaks; `[JANSEN]` clustering | K1–K3 (6.8) | FASE 6 |
| **Modelo primario** | Ninguno / regla técnica / modelo de ML | `[LDP]` propone regla técnica; `[MURPHY]` 13 candidatas causales | Formulación (E3); resultados de FASE 6 | Posterior a FASE 7 |
| **Modelo secundario / meta-labeling** | No / sí | `[LDP]` `KB02 §7`; requiere primario con recall alto | Si existe primario viable; **M3 (`[VACÍO]`)** | Posterior |
| **Abstención** | Seis mecanismos (§7.5), posiblemente combinables | Las tres, incompatibles entre sí | Formulación; K1; calibración | Posterior |
| **Calibración** | Sin calibrar / método a determinar | **`[VACÍO]` en las tres** | **Requiere conocimiento externo a las tres fuentes** | Posterior |
| **Sizing** | Fijo / proporcional a confianza / discretizado | `[LDP]` cadena completa; `[MURPHY]` normativo | Calibración; O5 | Posterior |
| **Familia de ML** | Lineal / árboles / bagging / boosting / redes | `[JANSEN]` catálogo; `[LDP]` agnóstico con preferencia por bagging; **ninguno decide** | Baselines; unicidad (configuración de ensembles); L3 | Posterior |
| **Validación** | WF purgado / CV purgada / CPCV; parámetros | `[LDP]` desarrollo completo; `[MURPHY]` robustez complementaria | Unicidad; coste computacional (H4); T3 | FASE 4, **antes que features** |
| **Métricas** | ML / económicas / de sistema | Las tres, conjuntos distintos | Formulación; O5 | FASE 7 |
| **Costes** | Modelo de costes a determinar | `[LDP]` métricas de shortfall; `[MURPHY]` promedio por operación | Datos externos (5.1) | FASE 5 |
| **Backtest** | Vectorizado / event-driven | `[JANSEN]` distingue ambos; `[LDP]` "no es herramienta de investigación" | Sistema completamente especificado | Última |
| **Monitorización** | Sin protocolo definido | **`[VACÍO]` en las tres** | Requiere desarrollo propio | Posterior a despliegue |

---

# §20. RESTRICCIONES FRENTE A PREFERENCIAS

El encargo exige no mezclar categorías.

## 20.1 Restricciones metodológicas
*Si no se cumplen, el experimento puede ser inválido.*

1. **No look-ahead.** Test operativo: si el valor en `t` cambia al añadir datos posteriores a `t`, hay leakage (§13.3).
2. **Purging y embargo** cuando las etiquetas abarcan varias barras (A15).
3. **Transformaciones ajustadas sólo con datos de entrenamiento** (A14).
4. **El conjunto usado para parar el entrenamiento nunca es el de reporte** (early stopping).
5. **Hold-out reservado antes de mirar los datos y usado una sola vez.**
6. **Registro de todos los intentos**, incluidos los abandonados (A9).
7. **Corrección por multiple testing** en el resultado final (A9).
8. **Comparación obligatoria contra baselines**, incluido un baseline de calendario (A4, 6.6).
9. **Ajuste explícito del rollover** antes de cualquier cálculo (A13).
10. **Costes modelados antes de afirmar viabilidad** (A5).
11. **Evaluación de estabilidad entre períodos y regímenes** (A11).
12. **El backtest sobre sistema especificado, una sola vez, sin redefinir a partir de él** (A12).
13. **Control de redundancia antes de interpretar importancias** (A6).
14. **Declaración explícita de grados de libertad** de cada técnica antes de evaluarla.

## 20.2 Restricciones de datos
*Impuestas por OHLCV. No negociables sin cambiar T2.*

1. **Sin secuencia intrabar**: orden entre High y Low desconocido.
2. **Sin aggressor side**: imposible firmar operaciones; barras de información inalcanzables.
3. **Sin bid/ask ni libro de órdenes.**
4. **Sin número de transacciones** (barras de tick auténticas inalcanzables).
5. **Sin VWAP real** (aproximable con error).
6. **Sin interés abierto.**
7. **Sin amplitud de mercado** — pese a que el MNQ *es* un índice de 100 valores.
8. **Sin sentimiento ni datos intermercado.**
9. **Sin fundamentales.**

## 20.3 Restricciones del proyecto
*Decisiones deliberadas por simplicidad. **Reconsiderables.***

1. **MNQ como instrumento único** (T1). Coste documentado en §8.
2. **OHLCV como fuente única** (T2). Coste documentado en §9.
3. **Orientación intradiaria** — **sin respaldo ni refutación bibliográfica** (§7.2).
4. **Dependencia mínima de proveedores externos.**
5. **Prioridad a simplicidad y reproducibilidad.**

## 20.4 Preferencias
*Deseos que podrían reconsiderarse si bloquean el objetivo.*

1. **Sistema operacionalmente simple** (`OHLCV → features → modelo → señal`). **No es una restricción metodológica**: nada en las tres fuentes exige ni prohíbe esa arquitectura.
2. **Preferencia por interpretabilidad.**
3. **Preferencia por coste computacional moderado** (T3).
4. **Preferencia por una señal discreta y accionable** frente a una salida continua.

## 20.5 Decisiones abiertas
*Sin información suficiente todavía.* Las 79 preguntas canónicas de §1.2 menos las ya cerradas en §16-A y §16-B. **Ninguna se cierra en esta síntesis.**

`[SÍNTESIS — INTERPRETACIÓN]` La distinción más importante de esta sección: **la orientación intradiaria está en 20.3, no en 20.1 ni en 20.4.** No es una restricción metodológica —nada la exige— ni una mera preferencia —condiciona todo el diseño—. Es una **restricción del proyecto sin respaldo bibliográfico**, y por tanto **la primera candidata a revisión si la evidencia empírica la desaconseja**.

---

# §21. IRIS — MARCO DE INVESTIGACIÓN DESPUÉS DE LA BIBLIOGRAFÍA

*Sección diseñada para leerse sola. Es el puente entre bibliografía y datos.*

## 21.1 Lo que sabemos

Doce principios sobreviven a las tres fuentes (§3). Los cinco de mayor consecuencia práctica:

1. **Predicción estadística ≠ rentabilidad.** Ninguna métrica de acierto o correlación autoriza una conclusión económica. Un factor con correlación significativa y spread positivo puede perder dinero.
2. **La causalidad temporal es la restricción de primer orden**, y su violación más frecuente no es evidente: normalizaciones globales, umbrales fijados mirando el histórico, pivotes sin retardo declarado, early stopping sobre el conjunto de reporte.
3. **El número de filas no es el tamaño muestral.** Con etiquetas solapadas, el número de observaciones independientes puede ser órdenes de magnitud menor, y de él depende cuántas hipótesis podemos permitirnos.
4. **La bibliografía nos dice cómo investigar, no qué encontraremos.** Lo establecido conjuntamente es casi enteramente metodológico y negativo. **Ninguna de las tres fuentes afirma que exista predictibilidad explotable en ningún instrumento concreto.**
5. **El backtest no es investigación.** La investigación ocurre en los escalones 1–7 del marco de evidencia; el backtest aparece una vez y tarde.

## 21.2 Lo que creemos que vale la pena investigar

**Hipótesis, no decisiones.** Las de mayor prioridad tras el filtro de mínima complejidad:

- **H1 — Flujo forzado.** La única con respaldo triple: stops, delta hedging, rebalanceo y margin call producen órdenes comprometidas de antemano. **No requiere universo multiactivo y es más fuerte en instrumentos apalancados.**
- **H3 — El régimen condiciona la relación.** La convergencia más importante de la síntesis: cuatro formulaciones independientes en Murphy, más structural breaks en LdP y no estacionariedad en Jansen. Medible causalmente con una o dos variables adimensionales.
- **H4 — Ciclo de volatilidad.** La volatilidad es el único momento que las tres fuentes tratan como predecible, y su medición es la más barata del inventario.
- **H2 — Memoria de niveles.** El mejor mecanismo económico del corpus, con el peor problema de causalidad. Requiere declarar el retardo de pivote.
- **H10 — Estacionalidad intradiaria.** **Ninguna fuente la desarrolla**, es específica de nuestro problema, y es simultáneamente hipótesis genuina y principal mecanismo de falso descubrimiento.
- **H6, H7, H8, H9** — volumen como confirmación, posición en rango, geometría OHLC y agotamiento: baratas, causales, con pocos grados de libertad.

Y el **principio de investigación de features** (§11.2): diseñar por familias informativas antes de instanciar indicadores, porque diez transformaciones de la misma información aportan menos que dos familias distintas y consumen diez veces más presupuesto.

## 21.3 Lo que sabemos que no debemos hacer

- **Investigar con el backtest.** ~20 iteraciones bastan para fabricar un falso descubrimiento al 5%.
- **Probar cientos de combinaciones** amparándose en que la bibliografía las sugiere. Cada parametrización es un intento; cambiar RSI 14 por RSI 13 aumenta los grados de libertad.
- **Confundir convergencia con consenso.** Que dos autores usen la palabra "ruptura" no significa que hablen del mismo observable (§5.3).
- **Adoptar técnicas por reputación.** El filtro de mínima complejidad descarta precisamente aquello por lo que el análisis técnico es conocido, y conserva medidas escalares de cero a dos parámetros.
- **Confiar en métricas out-of-bag** con muestras solapadas.
- **Elegir el modelo antes de saber qué se predice.** El grafo de dependencias lo sitúa en el penúltimo lugar.
- **Colapsar los motivos de no operar** en una única clase sin justificar por qué.
- **Tratar la inspección visual como evidencia.**
- **Avanzar con Elliott, ciclos ajustados, medias centradas, líneas geométricas o taxonomías retrospectivas** en su forma original.

## 21.4 Lo que no sabemos

**Las preguntas empíricas.** Por orden de dependencia: integridad y rollover (A1–A4) · estructura de sesión (D1–D3) · propiedades estadísticas (B1–B4) · muestreo y su error (C1–C4) · **número efectivo de observaciones independientes (G1)** · costes reales y edge mínimo (P1–P3) · qué features informan (J1–J2) · si existen regímenes causalmente asignables (K1–K3) · y, terminal, **si existe predictibilidad explotable en MNQ intradiario neta de costes (P4)**.

## 21.5 Lo que nuestros datos no pueden responder

Todo lo que requiera **firmar operaciones o conocer la secuencia intrabar**: barras de información, lambdas de Kyle y Hasbrouck, VPIN, delta, order flow. También interés abierto, amplitud del propio Nasdaq, sentimiento e intermercado.

**Pero el núcleo metodológico permanece intacto**: etiquetado, ponderación, validación, control de multiple testing, evaluación económica e interpretabilidad son todos `OHLCV-OK` sin condiciones. **El riesgo no es hacer mala ciencia; es que el espacio de hipótesis accesible no contenga ninguna hipótesis verdadera.**

## 21.6 Lo que deliberadamente aceptamos

- **Menor potencia estadística** por el instrumento único, configuración desaconsejada explícitamente por LdP y usada por Murphy como criterio de descarte. Las defensas sustitutivas cubren modos de fallo distintos, **pero ninguna es equivalente a la replicación entre activos.** El coste es de severidad: umbral de evidencia más alto, menos hipótesis, márgenes mayores para declarar un hallazgo.
- **Un espacio de hipótesis reducido** por OHLCV-only, con la familia microestructural excluida.
- **Una orientación intradiaria sin respaldo bibliográfico**, favorecida por una fuente sin evidencia y desaconsejada por otra sin evidencia.
- **Herencia incuantificable de sesgo de selección**: partimos de tres libros que catalogan técnicas ya exploradas por la industria durante décadas.

## 21.7 Qué debe hacer la siguiente etapa

**Ejecutar la agenda empírica de §17, en orden de dependencia**, sin adelantar decisiones de diseño:

```
FASE 0  Integridad, contratos y rollover        ── bloquea todo
FASE 1  Estructura de sesión                    ── resuelve un [VACÍO] bibliográfico
FASE 2  Propiedades estadísticas                ── informa dónde puede estar la señal
FASE 3  Muestreo y error de aproximación
FASE 4  Independencia efectiva                  ── FIJA EL PRESUPUESTO DE INTENTOS
FASE 5  Viabilidad económica ex-ante            ── puede refutar el diseño sin modelo
FASE 6  Contraste univariado de hipótesis       ── consume presupuesto
FASE 7  Preparación de la formulación
```

**Con dos condiciones previas a la FASE 0:** reservar el hold-out final antes de mirar nada, y abrir el registro de intentos.

**Y un criterio de éxito para la etapa que conviene fijar ahora:** el objetivo no es encontrar una estrategia, sino **saber si el espacio de hipótesis accesible contiene algo, y con qué presupuesto contamos para buscarlo**. Un resultado negativo bien establecido es un resultado.

---

# §22. CONTROL DE CALIDAD

| Verificación | Estado |
|---|---|
| Las tres KB fueron realmente utilizadas | ✔ Con trazabilidad de sección en todas las conclusiones materiales |
| Preguntas abiertas de las tres normalizadas | ✔ 160 originales → 79 canónicas en 20 bloques (§1) |
| Trazabilidad conservada | ✔ Notación `J-n` / `L-n` / `M-n` + referencias `KB0X §Y` |
| Convergencia ≠ consenso | ✔ §3 distingue; §5 examina ocho términos compartidos y declara falsa convergencia en cinco (5.2, 5.3, 5.4, 5.7, 5.8), complementariedad en 5.1, y convergencia real aunque menos específica en 5.5 y 5.6 |
| Hipótesis ≠ evidencia | ✔ §10 marca las 18 familias como no verificadas |
| Restricción ≠ decisión | ✔ §20 separa cuatro categorías |
| Preferencia del proyecto ≠ conclusión científica | ✔ §20.3 y §20.4 |
| No se diseñó IRIS | ✔ §23 |
| No se seleccionó modelo, target ni features | ✔ |
| No se reutilizaron decisiones históricas | ✔ Declarado en §0.4 |
| Instrumento único tratado explícitamente | ✔ §8 completa |
| OHLCV-only tratado explícitamente | ✔ §9 completa |
| Intradiario tratado explícitamente | ✔ §7.2 |
| NO TRADE tratado explícitamente | ✔ §7.5, taxonomía de seis mecanismos |
| Causalidad / look-ahead tratado explícitamente | ✔ §13 |
| Multiple testing tratado explícitamente | ✔ §15 |
| Dependencia intrabar tratada explícitamente | ✔ §7.6, §9.5, §13.2 |
| Rollover tratado explícitamente | ✔ §3.12, FASE 0 |
| Costes tratados conceptualmente | ✔ §3.5, §14, FASE 5 |
| Agenda del análisis empírico generada | ✔ §17, ocho fases |
| Mapa de decisiones abiertas generado | ✔ §19 |
| Grafo de dependencias generado | ✔ §18 |
| Tensiones no resolubles quedaron abiertas | ✔ §7, §8.5, y diez `[VACÍO]` comunes a las tres fuentes |

---

# §23. DECISIONES QUE SIGUEN PROHIBIDAS Y NO SE HAN TOMADO

Esta síntesis **no ha cerrado**: timeframe · horario operativo · regímenes horarios · tipo de barra · sampling · thresholds · target · horizonte · labeling · configuración de triple barrera · PT · SL · barrera vertical · definición de pivote · features · número de features · indicadores · ventanas · LONG/SHORT/NO_TRADE · modelo primario · meta-labeling · número de modelos · ninguna arquitectura neuronal ni de árboles · hiperparámetros · esquema definitivo de CV · sizing · stops · take-profit · estrategia · backtest final.

**Se ha concluido que ciertas alternativas no merecen prioridad** por razones metodológicas explícitas (§16-B, §12.4). **Eso no equivale a seleccionar la alternativa ganadora.**

---

## CHECKPOINT FINAL

```
Fuentes:
KB01 Jansen            — utilizada
KB02 López de Prado    — utilizada
KB03 Murphy            — utilizada

Última sección completada: §23 — TODAS COMPLETADAS
Siguiente sección: — (ninguna)
Preguntas abiertas procesadas: 160 originales → 79 canónicas
Preguntas pendientes: ninguna sin clasificar
Estado: COMPLETE
```

**Fin del documento — IRIS PROJECT KNOWLEDGE SYNTHESIS.**

**La fase bibliográfica queda cerrada. La siguiente etapa es estudiar empíricamente los datos reales del MNQ bajo las restricciones y preguntas definidas por esta síntesis.**
