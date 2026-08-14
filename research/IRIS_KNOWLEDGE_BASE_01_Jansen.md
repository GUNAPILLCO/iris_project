# IRIS PROJECT — KNOWLEDGE BASE 01
## Machine Learning for Algorithmic Trading — Stefan Jansen (2ª edición, 2020)

**Estado:** documento de memoria técnica permanente. Fuente única analizada: Jansen.
**Etapa:** 1 de 3 (Jansen → López de Prado → Murphy → Síntesis).
**Regla de esta etapa:** no se diseña IRIS. Se extrae conocimiento y se mantienen abiertas las decisiones.

---

## 0. CÓMO LEER ESTE DOCUMENTO

### 0.1 Convenciones de atribución

Todo el documento está etiquetado para poder distinguir fuente, interpretación e implicación:

| Etiqueta | Significado |
|---|---|
| `[JANSEN]` | Afirmación que el libro sostiene explícitamente. |
| `[INTERPRETACIÓN]` | Inferencia propia a partir de lo que dice el libro. No está escrita así en el texto. |
| `[IMPLICACIÓN PARA IRIS]` | Consecuencia potencial para nuestro proyecto. No es una decisión. |
| `[CONOCIMIENTO EXTERNO AL LIBRO]` | Observación que NO proviene de Jansen. Usado con moderación deliberada. |
| `[VACÍO]` | Problema que Jansen no cubre, o cubre de forma insuficiente para nuestro caso. |

Todo el contenido está reformulado con palabras propias. No se reproducen pasajes del libro.

### 0.2 Mapa Tarea → Sección

| Tarea del encargo | Sección de este documento |
|---|---|
| T1 — Filosofía general | §1 |
| T2 — Mapa de relevancia por capítulo | §2 |
| T3 — Formulación del problema predictivo | §8 |
| T4 — Datos financieros | §3, §4, §5 |
| T5 — Feature engineering y alpha factors | §6, §7 |
| T6 — Targets y objetivos de aprendizaje | §9 |
| T7 — Validación temporal | §15, §16 |
| T8 — Modelos de ML | §10, §12, §14 |
| T9 — Series temporales | §11 |
| T10 — Trading intradiario | §20 |
| T11 — Deep Learning | §13 |
| T12 — Predicción ≠ rentabilidad | §18 |
| T13 — Backtesting | §17 |
| T14 — Interpretabilidad | §19 |
| T15 — Errores que destruirían IRIS | §21 |
| T16 — Limitaciones de Jansen | §22 |
| T17 — Base de conocimiento | Todo el documento |
| T18 — Matriz de conocimiento | §23 |
| T19 — Preguntas abiertas | §24 |
| T20 — Qué llevar al siguiente libro | §25 |

### 0.3 Advertencia estructural sobre la fuente (leer antes que nada)

`[INTERPRETACIÓN]` El libro de Jansen está construido, casi en su totalidad, sobre un **paradigma cross-sectional**: muchos activos, un instante; el modelo ordena (rankea) activos y la estrategia va larga en el decil superior y corta en el inferior. Prácticamente todo su aparato de evaluación —Alphalens, quantile spreads, Information Coefficient calculado como correlación de Spearman entre activos, la "breadth" de la ley fundamental, las carteras long-short, pyfolio— **presupone una sección transversal de activos**.

IRIS es lo contrario: **un solo instrumento (MNQ), muchos instantes**. Es un problema *time-series*, no *cross-sectional*.

Esto no invalida el libro, pero cambia radicalmente qué se puede trasladar. Este documento marca sistemáticamente esa frontera. Es, con diferencia, la limitación más importante de esta fuente para nuestro proyecto y está desarrollada en §22.

---

## 1. FILOSOFÍA DE MACHINE LEARNING PARA TRADING (Tarea 1)

### 1.1 La tesis central del libro

`[JANSEN]` El ML no es un ejercicio aislado que produce un modelo: es **un elemento dentro de un proceso**. Jansen llama a ese proceso el *ML4T workflow* y lo presenta como la unidad de análisis relevante. Un modelo con buenas métricas estadísticas no constituye un resultado; el resultado es una estrategia simulada de forma realista y evaluada económicamente.

`[JANSEN]` La propuesta de valor concreta del ML en trading es la capacidad de extraer información accionable de volúmenes de datos mucho mayores, y de forma más sistemática, que un analista humano. No es "predecir mejor por ser más sofisticado".

`[JANSEN]` El libro es explícito en que **no ofrece algoritmos listos para operar**, y deliberadamente incluye ejemplos que no dan buenos resultados, para no exagerar los beneficios del ML ni minimizar el esfuerzo requerido.

`[INTERPRETACIÓN]` Esta última decisión editorial es en sí misma un dato metodológico: el autor considera que el fracaso parcial es el estado normal de la investigación en este dominio, no una anomalía.

### 1.2 La cadena completa: de la idea al resultado económico

Jansen no presenta esta cadena como una lista, sino distribuida a lo largo del libro. Aquí la reconstruyo en el orden que pidió el encargo, indicando qué dice el libro en cada eslabón.

```
IDEA
 ↓  ¿por qué debería existir señal aquí? (economía, comportamiento, microestructura)
DATOS
 ↓  ¿point-in-time? ¿qué mide exactamente? ¿qué frecuencia? ¿qué calidad?
FEATURES (alpha factors)
 ↓  transformaciones que hacen accesible al algoritmo la información latente
TARGET
 ↓  forward returns / dirección / clases, y en qué horizonte
MODELO
 ↓  familia elegida según supuestos, datos disponibles y ratio señal/ruido
PREDICCIÓN
 ↓  score continuo o probabilidad
SEÑAL
 ↓  agregación, ranking, umbral, ensemble
REGLA OPERATIVA
 ↓  cuándo entrar, cuánto, cuándo salir
POSICIÓN
 ↓  sizing, riesgo, restricciones
EJECUCIÓN
 ↓  timing, comisiones, spread, slippage, turnover
RESULTADO ECONÓMICO
 ↓  PnL, Sharpe, drawdown, cola
VALIDACIÓN
    out-of-sample honesto, corregido por número de intentos
```

**Cómo construye Jansen cada eslabón:**

**(1) De idea de trading a problema cuantitativo.** `[JANSEN]` El punto de partida no es el dato ni el modelo, sino el *caso de uso*. Jansen insiste en que las estrategias deben priorizarse por su justificación económica o teórica antes de testearse, y no al revés. La razón que da es directa: elegir hipótesis por data-mining multiplica el riesgo de falsos descubrimientos. La expresión que usa para criticar esta práctica es la conocida idea de que si torturas los datos suficiente tiempo, confesarán.

**(2) De problema cuantitativo a problema de ML.** `[JANSEN]` La misma tarea admite formulaciones distintas: combinar varios alpha factors puede plantearse como regresión de retornos, como clasificación binaria de dirección, o como clasificación multiclase por quintiles de rendimiento. El libro presenta esto como una **decisión de diseño abierta**, no como algo determinado por la tarea. `[IMPLICACIÓN PARA IRIS]` Jansen valida explícitamente nuestra decisión de no cerrar todavía la formulación.

**(3) Papel de los datos.** `[JANSEN]` Los datos son el ingrediente individual más importante. Su calidad no tiene un estándar objetivo: depende del **contenido de señal respecto de nuestro objetivo de inversión concreto**. Además, el valor suele emerger de la *combinación* de fuentes complementarias, porque los modelos no lineales (árboles, redes) explotan interacciones entre variables que capturan aspectos distintos del mismo fenómeno.

**(4) Qué significa extraer información predictiva.** `[JANSEN]` Significa encontrar una asociación estadística entre features conocidas en `t` y un resultado en `t+h`, que sea *estable* y no un artefacto muestral. Jansen subraya que en finanzas no sabemos hoy separar señal de ruido desde la perspectiva de los resultados de mañana; sólo disponemos de validación cuidadosa y diagnóstico de modelos para aproximarnos.

**(5) Qué son las señales y los alpha factors.** `[JANSEN]` Un alpha factor es una transformación de datos crudos que apunta a predecir movimientos de precio; devuelve **un único valor por activo cada vez que la estrategia lo evalúa**. Las decisiones pueden basarse en valores relativos entre activos o en patrones de un solo activo. `[INTERPRETACIÓN]` Esa segunda opción —patrones de un solo activo— es la puerta que Jansen deja abierta para un caso como IRIS, pero es una puerta que él prácticamente no atraviesa en los ejemplos.

**(6) Cómo se investiga si una variable contiene señal.** Desarrollado en §7. En resumen: Information Coefficient, mutual information, retornos por quantil, turnover, feature importance, permutation importance, SHAP, y finalmente rendimiento fuera de muestra.

**(7) Cómo se construyen features.** `[JANSEN]` El feature engineering es a menudo *el ingrediente más importante* de un modelo predictivo exitoso, y se beneficia de tres cosas: conocimiento del dominio, estadística/teoría de la información, y creatividad. Jansen es explícito en que se aprende con experiencia más que con reglas.

**(8) Cómo se definen objetivos predictivos.** `[JANSEN]` Distingue tareas por la naturaleza de la salida: variable continua → regresión; categórica → clasificación; categórica ordenada → ranking. Y añade un matiz importante: definir el objetivo del algoritmo es uno de los primeros pasos y a veces el más difícil (por ejemplo cuando importan simultáneamente precisión y recall, o cuando hay condiciones que deben *cumplirse* en lugar de optimizarse).

**(9) Cómo se seleccionan modelos.** `[JANSEN]` Vía el teorema *no free lunch*: ningún algoritmo es universalmente superior. Un modelo simple falla si la relación es compleja, pero un modelo complejo **también falla si la relación es simple y los datos son ruidosos**, porque aprenderá el ruido como si fuera parte de la relación compleja que asume existir. Las herramientas para elegir son exploración de datos y experimentación informada por los supuestos del modelo.

**(10) Cómo se validan modelos.** Desarrollado en §15. Núcleo: cross-validation que respete el orden temporal, split en tres partes (train / validation / hold-out), curvas de aprendizaje y validación, y conciencia de que el score del mejor modelo tras muchas iteraciones de CV **ya está sesgado por multiple testing** y no es un buen estimador del error de generalización.

**(11) Cómo se evita overfitting.** `[JANSEN]` Más datos es la mejor protección; después, regularización (penalizaciones, early stopping, dropout, restricciones de profundidad). Y a nivel de proceso: priorizar hipótesis justificadas, reportar el número de pruebas, y corregir las métricas por ese número (deflated Sharpe ratio).

**(12) Cómo se conectan predicciones con decisiones y posiciones.** `[JANSEN]` En sus ejemplos, típicamente: predicción continua → ranking → seleccionar los N mejores y N peores → posiciones equiponderadas long/short → rebalanceo diario. `[INTERPRETACIÓN]` Este paso es, con diferencia, **el menos desarrollado del libro**. La regla operativa es casi siempre "top N / bottom N", elegida por conveniencia expositiva, no derivada de un análisis.

**(13) Cómo se hace backtesting.** Desarrollado en §17. Distinción central: vectorizado vs event-driven.

**(14) Cómo se evalúa una estrategia.** Desarrollado en §18. Métricas de riesgo-retorno, no de error de predicción.

### 1.3 Las cinco lecciones que el propio Jansen destila al cerrar el libro

`[JANSEN]` En el capítulo de conclusiones enumera lo que considera esencial:

1. **Los datos son el ingrediente más importante**, y requieren sourcing y control de calidad cuidadosos.
2. **El conocimiento del dominio es clave** para dirigir la estrategia, seleccionar datos, diseñar features y evitar trampas.
3. **El ML es una caja de herramientas** adaptable y combinable, no una solución.
4. **La elección de objetivos y diagnósticos de rendimiento es crítica.**
5. **El backtest overfitting es un desafío enorme** que requiere atención sostenida.
6. **La transparencia de los modelos black-box** ayuda a construir confianza y a validar la lógica del modelo.

`[JANSEN]` Añade dos características del dominio que agravan todo lo anterior: el ratio señal/ruido de los datos financieros es bajo, y la naturaleza competitiva del trading implica que **los patrones se degradan rápido** (factor decay), lo que obliga a monitorización y mantenimiento continuos, no sólo a una validación inicial.

`[IMPLICACIÓN PARA IRIS]` El punto 6 conecta directamente con una de las preguntas del objetivo de IRIS ("¿qué condiciones del mercado explican la señal?"). Jansen sitúa la interpretabilidad no como un lujo sino como parte del control de riesgo del propio proceso de investigación.

---

## 2. MAPA COMPLETO DE RELEVANCIA DEL LIBRO (Tarea 2)

Clasificación: **A** = crítico · **B** = importante · **C** = complementario · **D** = poco relevante en la primera etapa.

El criterio aplicado, según pidió el encargo, es el **principio metodológico subyacente**, no el activo del ejemplo.

---

### Capítulo 1 — Machine Learning for Trading: From Idea to Execution — **B**

1. **Problema que aborda:** por qué el ML entró en la industria, cómo se estructura el proceso de inversión, dónde aporta valor el ML.
2. **Conceptos importantes:** el ML4T workflow; las tres olas de estrategias cuantitativas; *factor decay*; taxonomía de objetivos algorítmicos (ejecución, corto plazo, comportamiento, predicción de precios relativos); casos de uso del ML (minería de datos, creación de alfas, agregación de señales, asignación, testeo, RL).
3. **Qué conservar:** el marco completo idea→ejecución; la advertencia sobre decay de factores; la afirmación de que el libro se centra en estrategias que operan sobre expectativas de cambios de precio *relativos* en horizontes más allá del muy corto plazo dominado por latencia.
4. **Relación con IRIS:** define el mapa mental del proceso. También delimita honestamente dónde se sitúa el libro: **no** en HFT puro, **no** en un único instrumento.
5. **Específico del ejemplo:** la historia industrial (AQR, quant quake de 2007, Quantopian, RenTec).
6. **Generalizable:** el workflow; el decay de señal; que la mayoría de estrategias del libro son de expectativas relativas entre activos.
7. **No trasladar:** la idea de "breadth" como número de apuestas independientes entre activos (ver §18.3).
8. **Nivel: B.**
9. **Justificación:** aporta el marco y el vocabulario, pero poco contenido técnico directamente aplicable.

---

### Capítulo 2 — Market and Fundamental Data — **A (parcial) / D (parcial)**

1. **Problema:** de dónde vienen los datos de mercado y cómo su estructura institucional condiciona el análisis.
2. **Conceptos importantes:** **microestructura de mercado**; tipos de órdenes (market, limit, stop, all-or-none, fill-or-kill, IOC, not-held, market-on-open/close); libro de órdenes; datos ITCH; **de ticks a barras**: tick bars, time bars, volume bars, dollar bars; **bid-ask bounce**; OHLCV + VWAP; barras de minuto de AlgoSeek con información de quote (NBBO), volumen al bid/ask/midpoint, upticks/downticks, spread mínimo y máximo; almacenamiento eficiente (HDF5, parquet).
3. **Qué conservar:** *todo* lo relativo a microestructura, muestreo y construcción de barras. Es el capítulo más directamente relevante para IRIS de toda la primera parte.
4. **Relación con IRIS:** trabajamos con datos intradiarios OHLCV de un futuro. Este capítulo es el que discute exactamente esa capa.
5. **Específico del ejemplo:** ITCH de Nasdaq, SIP, Reg NMS, NBBO, dark pools, FINRA — todo específico de renta variable estadounidense fragmentada.
6. **Generalizable:** el argumento de por qué existen las barras alternativas (volumen/dólar) y qué problema resuelven; que los retornos de tick no son normales; que el bid-ask bounce introduce oscilación espuria; que agregar mejora las propiedades estadísticas.
7. **No trasladar directamente al MNQ:** la fragmentación de mercado y el NBBO no aplican a un futuro que cotiza centralizado en CME. Las "dollar bars" motivadas por splits y cambios de valor de la acción tienen otra justificación en futuros (rollover, cambio de contrato, cambio de nivel del índice).
8. **Nivel: A** para las secciones de microestructura y barras; **D** para las secciones de datos fundamentales (XBRL, filings, P/E).
9. **Justificación:** el principio de muestreo es el que más puede condicionar toda la arquitectura posterior de IRIS.

---

### Capítulo 3 — Alternative Data — **D**

1. **Problema:** categorías, criterios de evaluación y adquisición de datos alternativos.
2. **Conceptos:** fuentes (individuos, procesos de negocio, sensores); criterios de evaluación (calidad del contenido de señal, calidad del dato, aspectos técnicos); scraping.
3. **Qué conservar:** únicamente el **framework de criterios de evaluación de una fuente de datos** —en particular la idea de que la calidad se juzga por el contenido de señal respecto al objetivo, no en abstracto.
4. **Relación con IRIS:** marginal hoy. Relevante si en el futuro se plantea añadir datos externos (calendario macro, VIX, order flow, datos de otros índices).
5. **Específico:** OpenTable, transcripciones de earnings calls.
6. **Generalizable:** el checklist de evaluación de una fuente nueva.
7. **No trasladar:** nada del scraping.
8. **Nivel: D.**
9. **Justificación:** IRIS parte de OHLCV. El capítulo no habla de nuestro problema.

---

### Capítulo 4 — Financial Feature Engineering: How to Research Alpha Factors — **A**

1. **Problema:** cómo se diseñan y, sobre todo, **cómo se evalúan** variables predictivas.
2. **Conceptos:** definición de alpha factor; categorías clásicas (momentum/sentimiento, valor, volatilidad/tamaño, calidad) y sus racionales económicos (racional vs conductual); construcción con pandas/NumPy y TA-Lib (200+ indicadores); **denoising con filtro de Kalman**; **wavelets**; **Alphalens**: forward returns, quantiles de factor, retornos medios por quantil, dispersión (violin plots), **Information Coefficient** (Spearman), IC ajustado por riesgo, **factor turnover**.
3. **Qué conservar:** el método completo de evaluación de un factor. La exigencia de intuición económica previa. La advertencia sobre proliferación de factores (~250 publicados con evidencia empírica en revistas reputadas hacia 2015, creciendo unos 40/año según Jason Hsu, citado por Jansen). La observación de que un IC de 0.05 es bajo pero puede ser significativo y rentable si hay suficientes oportunidades de aplicarlo.
4. **Relación con IRIS:** es el capítulo que define **cómo se decide si una variable contiene información**. Núcleo absoluto.
5. **Específico del ejemplo:** todo lo cross-sectional — quantiles de activos, portfolios long-short por decil, sectorización, Alphalens como librería.
6. **Generalizable:** IC como concepto (correlación de rangos entre score y retorno futuro); análisis por quantiles como concepto (comparar retorno futuro condicionado al valor del factor); turnover como proxy de coste; la exigencia de dispersión y no sólo de media; denoising.
7. **No trasladar directamente:** los factores de valor y calidad (requieren fundamentales, inexistentes para un índice futuro); la construcción de quantiles *entre activos*.
8. **Nivel: A.**
9. **Justificación:** aunque el vehículo sea cross-sectional, las **preguntas** que plantea (¿separa el factor los retornos futuros? ¿es estable en el tiempo? ¿qué dispersión tiene? ¿cuánto rota?) son universales y traducibles a series temporales.

---

### Capítulo 5 — Portfolio Optimization and Performance Evaluation — **B**

1. **Problema:** cómo medir el rendimiento de una estrategia y cómo dimensionar posiciones.
2. **Conceptos:** Sharpe ratio y sus problemas de estimación cuando los retornos no son IID (ajustes de Lo por autocorrelación); Information Ratio; **ley fundamental de la gestión activa** (IR ≈ IC × amplitud, con extensión por transfer coefficient); MPT, CAPM, media-varianza y sus alternativas; risk parity; hierarchical risk parity; **pyfolio**: max drawdown, Calmar, Omega, Sortino, tail ratio, VaR diario, alpha, beta, leverage bruto, turnover diario; **walk-forward testing** con separación in-sample / out-of-sample.
3. **Qué conservar:** el **conjunto de métricas económicas** y la práctica de reportarlas separadamente in-sample y out-of-sample. La advertencia sobre anualizar Sharpe desde frecuencias altas cuando hay autocorrelación.
4. **Relación con IRIS:** define el vocabulario de "¿esto es una buena estrategia?".
5. **Específico:** optimización de carteras multiactivo, eigenportfolios, HRP.
6. **Generalizable:** todas las métricas de riesgo; el reporte in/out-of-sample; la advertencia sobre el escalado √t del Sharpe.
7. **No trasladar:** la ley fundamental tal cual — su "breadth" es el número de apuestas *independientes*, y en un único instrumento las apuestas consecutivas están correlacionadas. La optimización media-varianza no aplica a un instrumento único.
8. **Nivel: B.**
9. **Justificación:** crítico para evaluación, irrelevante para construcción de cartera en nuestro caso.

---

### Capítulo 6 — The Machine Learning Process — **A**

1. **Problema:** cómo formular, entrenar, tunear y evaluar modelos de forma sistemática.
2. **Conceptos:** supervisado / no supervisado / refuerzo; **framing del problema**: regresión vs clasificación vs ranking; predicción vs inferencia; **causalidad ≠ correlación**; métricas de regresión (RMSE, RMSLE, MAE, MedAE, varianza explicada, R²) y de clasificación (matriz de confusión, ROC-AUC, precision-recall, F1, y el **umbral como variable de decisión a optimizar según costes y beneficios**); **mutual information**; **bias-variance trade-off**; over/underfitting; CV (KFold, LOO, LPO, ShuffleSplit); **los desafíos de la CV en finanzas**; TimeSeriesSplit; **purging, embargoing y CV combinatoria** (atribuidos explícitamente a López de Prado); curvas de validación y de aprendizaje; GridSearchCV y Pipeline.
3. **Qué conservar:** prácticamente todo. Especialmente: la CV asume IID y **los datos financieros no lo son**; el split en tres partes con hold-out usado una sola vez; que el score del mejor modelo tras muchas iteraciones ya está sesgado; que los labels solapados (por retornos calculados sobre varios períodos) filtran información.
4. **Relación con IRIS:** es el capítulo que define nuestra **higiene experimental**.
5. **Específico:** el ejemplo con precios de vivienda y KNN.
6. **Generalizable:** todo el marco.
7. **No trasladar:** ninguna CV que baraje (`shuffle=True`).
8. **Nivel: A.**
9. **Justificación:** sin esto, cualquier resultado de IRIS será indistinguible del ruido.

---

### Capítulo 7 — Linear Models: From Risk Factors to Return Forecasts — **A**

1. **Problema:** regresión lineal y logística para inferencia y predicción; regularización.
2. **Conceptos:** OLS, Gauss-Markov, inferencia estadística, diagnóstico (heterocedasticidad, autocorrelación serial, multicolinealidad); SGD; modelos de factores (CAPM → Fama-French); regresión Fama-MacBeth; **ridge y lasso** como cobertura contra overfitting; **preparación de features y forward returns para múltiples horizontes**; regresión logística para predecir dirección del movimiento; **MultipleTimeSeriesCV** (CV custom que respeta el orden temporal con longitudes de train/test parametrizables).
3. **Qué conservar:** (a) la **construcción explícita de forward returns para varios horizontes con el fin de identificar cuál produce mejor precisión predictiva medida por IC** — esto es un principio metodológico directamente transferible; (b) la regularización como herramienta de control de varianza; (c) el `MultipleTimeSeriesCV` como patrón; (d) el uso de modelos lineales como **baseline con inferencia estadística disponible**.
4. **Relación con IRIS:** define el baseline obligatorio y la mecánica de construcción del dataset supervisado (lags como features, forward returns como target).
5. **Específico:** universo de 100 acciones más líquidas por dollar volume, dummies de sector, Fama-French.
6. **Generalizable:** lags de retornos a múltiples escalas como features; winsorización de retornos; forward returns a múltiples horizontes; búsqueda del horizonte óptimo por IC; regularización.
7. **No trasladar:** los factores de riesgo Fama-French y la lógica cross-sectional del modelo de factores.
8. **Nivel: A.**
9. **Justificación:** es el capítulo donde el libro *construye el dataset supervisado*, y esa mecánica es la nuestra.

---

### Capítulo 8 — The ML4T Workflow: From Model to Strategy Backtesting — **A**

1. **Problema:** cómo simular una estrategia con honestidad metodológica.
2. **Conceptos:** **pitfalls del backtest** organizados en tres bloques —*datos* (look-ahead bias, survivorship bias, control de outliers, elección del período muestral), *simulación* (mark-to-market, costes de transacción y slippage, timing de decisiones) y *estadística* (multiple testing, **deflated Sharpe ratio**, **longitud mínima de backtest**, **parada óptima**)—; **backtesting vectorizado vs event-driven**; arquitectura de un motor de backtest (ingesta, calendarios, factores, modelo, reglas de trading, evaluación); backtrader y Zipline.
3. **Qué conservar:** el capítulo completo. Especialmente los tres resultados cuantitativos sobre multiple testing:
   - Jansen reporta que 2 años de datos diarios de backtest no sostienen conclusiones sobre más de ~7 estrategias; 5 años, sobre ~45.
   - El *deflated Sharpe ratio* corrige la significación del SR por número de pruebas, no-normalidad y longitud muestral.
   - La regla de parada derivada del problema de la secretaria: probar un ~37% (1/e) de las estrategias razonables registrando su rendimiento, y luego continuar hasta que una supere a todas las anteriores.
4. **Relación con IRIS:** es nuestro protocolo de honestidad.
5. **Específico:** Zipline, backtrader, pipelines, bundles de Quandl.
6. **Generalizable:** absolutamente todos los pitfalls y sus remedios.
7. **No trasladar:** survivorship bias (irrelevante para un instrumento único), aunque su análogo sí existe (ver §21).
8. **Nivel: A.**
9. **Justificación:** es la sección del libro que más directamente protege a IRIS de autoengañarse.

---

### Capítulo 9 — Time-Series Models for Volatility Forecasts and Statistical Arbitrage — **A**

1. **Problema:** herramientas de diagnóstico y modelado de series temporales.
2. **Conceptos:** descomposición (tendencia, estacionalidad, residuo); **rolling windows y medias móviles**; **autocorrelación (ACF) y autocorrelación parcial (PACF)**; correlogramas; **estacionariedad** (estricta vs covarianza-estacionaria); transformaciones (log, deflación, detrending, diferenciación); **raíces unitarias y random walk**; test ADF; AR, MA, ARIMA y extensiones; **ARCH/GARCH para volatilidad**; VAR multivariante; **cointegración** (Engle-Granger, Johansen) y pairs trading.
3. **Qué conservar:** el **kit de diagnóstico** (ACF/PACF, ADF, descomposición, rolling stats) como forma de *estudiar nuestros datos* antes de modelarlos. La observación explícita de que al modelar volatilidad **se abandona el supuesto de estacionariedad en segundo momento** y se asume que la varianza cambia de forma predecible. La caracterización del random walk: la varianza crece con t, y las innovaciones persisten (long memory).
4. **Relación con IRIS:** define cómo caracterizar estadísticamente el MNQ intradiario.
5. **Específico:** forecast de variables macro de la Fed, pairs trading con ETFs.
6. **Generalizable:** todo el instrumental de diagnóstico y las transformaciones de estacionarización.
7. **No trasladar:** cointegración y pairs trading requieren ≥2 series; no aplican a un instrumento único (salvo que el futuro se amplíe a MNQ vs otros índices, lo cual sería otro proyecto).
8. **Nivel: A** para diagnóstico y volatilidad; **C** para cointegración.
9. **Justificación:** es el único capítulo que trata la serie temporal *como serie temporal* y no como corte transversal.

---

### Capítulo 10 — Bayesian ML: Dynamic Sharpe Ratios and Pairs Trading — **C**

1. **Problema:** inferencia probabilística y cuantificación de incertidumbre.
2. **Conceptos:** actualización bayesiana; MAP; inferencia aproximada determinista (variacional) y estocástica (MCMC); PyMC3; **Sharpe ratio bayesiano para comparar rendimiento**; regresión rolling bayesiana; **modelos de volatilidad estocástica**.
3. **Qué conservar:** la idea de que el rendimiento de una estrategia debe reportarse **con incertidumbre**, no como un número puntual. El Sharpe bayesiano es la instancia concreta.
4. **Relación con IRIS:** relevante para la pregunta "¿qué nivel de confianza existe en la señal?" y para comparar variantes de estrategia sin sobreinterpretar diferencias pequeñas.
5. **Específico:** PyMC3, predicción de recesiones, pairs trading.
6. **Generalizable:** cuantificación de incertidumbre en métricas de rendimiento; volatilidad estocástica.
7. **No trasladar:** el pipeline de pairs trading.
8. **Nivel: C**, con un elemento de nivel B (Sharpe bayesiano).
9. **Justificación:** valioso pero no bloqueante en la primera etapa.

---

### Capítulo 11 — Random Forests: A Long-Short Strategy for Japanese Stocks — **A**

1. **Problema:** modelos no lineales basados en árboles y su uso en un workflow completo.
2. **Conceptos:** cómo aprenden reglas los árboles; overfitting y regularización de árboles; tuning de hiperparámetros; **por qué funcionan los ensembles**; bootstrap aggregation; random forest; feature importance; **out-of-bag testing**; pros y contras. Y crucialmente: **el diseño experimental del workflow ML4T** — lookback period, lookahead period, test period, hiperparámetros, ensembling; `MultipleTimeSeriesCV`; muestreo de tickers para acelerar la CV.
3. **Qué conservar:** (a) el árbol/RF como familia con buen equilibrio potencia-interpretabilidad; (b) **la lista de decisiones de diseño experimental** (lookback, lookahead, test period, hiperparámetros, ensembling) como checklist; (c) la advertencia de que activar `early_stopping` dentro de la CV **sesga al alza** las estimaciones porque usa información del outcome no disponible en condiciones realistas.
4. **Relación con IRIS:** los árboles son candidatos naturales para features tabulares ruidosas; el diseño experimental es directamente adoptable.
5. **Específico:** acciones japonesas, universo de 250 tickers, dummies de sector.
6. **Generalizable:** todo el diseño experimental y la teoría de ensembles.
7. **No trasladar:** el ranking cross-sectional de activos.
8. **Nivel: A.**
9. **Justificación:** contiene el esqueleto experimental más limpio del libro.

---

### Capítulo 12 — Boosting Your Trading Strategy — **A**

1. **Problema:** gradient boosting y su interpretación; **y el único ejemplo intradiario del libro**.
2. **Conceptos:** AdaBoost; gradient boosting; XGBoost / LightGBM / CatBoost e innovaciones algorítmicas; tuning; **feature importance (gain, split count, permutation)**; partial dependence plots; **SHAP values** (individualizados, teóricamente consistentes, computables en tiempo razonable para ensembles de árboles); force plots; backtest de la estrategia diaria; **estrategia intradiaria con datos de minuto**.
3. **Qué conservar:** todo. En particular la sección intradiaria (ver §20) y SHAP (ver §19). También el resultado empírico del ejemplo diario: rendimiento anual del 27.3% in-sample frente a 8.0% out-of-sample; Sharpe 1.24 vs 0.61. `[INTERPRETACIÓN]` Esa caída de más del 50% en el Sharpe entre in y out-of-sample, en el ejemplo que el autor eligió para mostrar el método, es uno de los datos más informativos del libro.
4. **Relación con IRIS:** boosting sobre features tabulares es probablemente el punto de partida más razonable *si* se decide un enfoque supervisado tabular; y el ejemplo intradiario es el único puente directo del libro a nuestro problema.
5. **Específico:** universo de acciones US, NASDAQ 100 vía AlgoSeek.
6. **Generalizable:** el algoritmo, el tuning, SHAP, y el diseño del experimento intradiario.
7. **No trasladar:** las features derivadas de quote/NBBO específicas de equities fragmentadas si no tenemos su equivalente en MNQ; las dummies de sector.
8. **Nivel: A.**
9. **Justificación:** máxima densidad de contenido transferible por página.

---

### Capítulo 13 — Data-Driven Risk Factors and Asset Allocation with Unsupervised Learning — **C**

1. **Problema:** reducción de dimensionalidad y clustering.
2. **Conceptos:** maldición de la dimensionalidad; PCA e ICA; manifold learning (no lineal); factores de riesgo data-driven; eigenportfolios; k-means, clustering jerárquico, DBSCAN, mixturas gaussianas; hierarchical risk parity.
3. **Qué conservar:** (a) la **maldición de la dimensionalidad** como argumento contra generar cientos de features sin control; (b) PCA como herramienta de diagnóstico de redundancia entre features; (c) clustering como forma de **descubrir regímenes** en lugar de imponerlos.
4. **Relación con IRIS:** el clustering para identificar regímenes de mercado es una línea de investigación potencialmente muy relevante para la pregunta "¿en qué condiciones debería IRIS abstenerse?". Pero Jansen **no lo usa así**: lo usa para agrupar activos.
5. **Específico:** eigenportfolios, HRP, asignación multiactivo.
6. **Generalizable:** PCA sobre features; clustering sobre estados/ventanas temporales `[INTERPRETACIÓN — el libro no hace esto]`.
7. **No trasladar:** HRP y eigenportfolios.
8. **Nivel: C**, con potencial de B si la línea de regímenes se desarrolla.
9. **Justificación:** las técnicas son útiles pero su aplicación en el libro está lejos de nuestro problema.

---

### Capítulos 14, 15, 16 — NLP: Sentiment Analysis, Topic Modeling, Word Embeddings — **D**

1. **Problema:** convertir texto en features numéricas y extraer señal de él.
2. **Conceptos:** pipeline NLP, bag-of-words, matriz documento-término, naive Bayes, LSI/pLSA/LDA, word2vec/GloVe, embeddings.
3. **Qué conservar:** una sola idea transversal — la noción de **representación aprendida**: que un espacio vectorial denso puede capturar estructura que las features crudas no exponen. Es el mismo principio que sustenta autoencoders y embeddings de variables categóricas.
4. **Relación con IRIS:** ninguna en la etapa actual (no tenemos datos de texto).
5. **Específico:** todo.
6. **Generalizable:** el concepto de embedding.
7. **No trasladar:** todo lo demás.
8. **Nivel: D.**
9. **Justificación:** no hay texto en nuestro problema. Reevaluar sólo si se incorporan noticias o datos macro cualitativos.

---

### Capítulo 17 — Deep Learning for Trading — **B**

1. **Problema:** redes feedforward: diseño, entrenamiento, regularización, y un caso completo aplicado a trading.
2. **Conceptos:** arquitectura y propagación hacia adelante; **decisiones de diseño** (número de capas y nodos, conexiones, funciones de activación); ReLU vs tanh vs sigmoide y el problema de la saturación; unidades de salida y funciones de coste según el tipo de problema; **regularización**: penalizaciones de norma (L1/L2), **early stopping** y **dropout**; optimización (SGD, momentum, Nesterov, tasas adaptativas); TensorFlow/PyTorch; GPU; **caso práctico: optimizar una NN para una estrategia long-short**.
3. **Qué conservar (y es el material más valioso del capítulo):**
   - La observación de que el modelo con menor error de generalización suele **no** ser el del tamaño exacto correcto de parámetros, sino uno más grande bien regularizado.
   - La advertencia explícita de que **early stopping puede introducir look-ahead bias**: si el criterio de parada usa datos fuera de muestra que no estarían disponibles en la implementación real, los resultados del backtest saldrán excesivamente positivos.
   - El resultado empírico del experimento: al regresar el IC diario sobre dummies de las opciones arquitectónicas, el R² es **prácticamente cero**, y Jansen lo interpreta como que el ruido de los datos domina sobre la señal aportada por las decisiones de arquitectura. Los IC medianos de las cinco mejores configuraciones se movían en un rango muy estrecho (aprox. 0.0236–0.0246).
4. **Relación con IRIS:** define el estándar de evidencia que debería exigirse antes de usar DL (ver §13).
5. **Específico:** 995 acciones US, features del capítulo 12, ensembles de las 3 mejores configuraciones.
6. **Generalizable:** todas las decisiones de diseño, la regularización, y sobre todo el resultado sobre la irrelevancia relativa de la arquitectura frente al ruido.
7. **No trasladar:** los números de rendimiento (22.8% anualizado, Sharpe 2.15 out-of-sample) — son antes de costes, sobre 995 acciones, con rebalanceo diario y una ventana out-of-sample de 12 meses.
8. **Nivel: B.**
9. **Justificación:** el conocimiento es sólido, pero la conclusión operativa que sugiere es *prudencia*, no adopción.

---

### Capítulo 18 — CNNs for Financial Time Series and Satellite Images — **C**

1. **Problema:** convoluciones aplicadas a datos con estructura de rejilla, incluidas series temporales.
2. **Conceptos:** operación de convolución; arquitecturas clásicas; transfer learning; **CNN autorregresiva con convoluciones 1D** (12 retornos mensuales rezagados → retorno del mes siguiente); **CNN-TA** (15 indicadores × 15 intervalos organizados en una rejilla 15×15, con selección de features por mutual information y ordenación por clustering jerárquico).
3. **Qué conservar:** (a) la condición bajo la cual una CNN tiene sentido en series temporales — que existan **patrones locales** (autocorrelación o relaciones no lineales a intervalos relevantes) y que **la organización espacial de los datos importe**, a diferencia de una red feedforward donde permutar dimensiones es inocuo; (b) las **lecciones de fracaso**: el resultado no era robusto, modificaciones ligeras degradaban mucho el rendimiento, y con ratio señal/ruido bajo una red demasiado compleja o un optimizador inadecuado llevaban a un óptimo local donde la CNN **predecía siempre un valor constante**.
4. **Relación con IRIS:** la conversión de indicadores × ventanas en rejilla es conceptualmente aplicable a MNQ intradiario. Las lecciones de fracaso son más valiosas que la técnica.
5. **Específico:** imágenes satelitales, EUROSAT, transfer learning con AlexNet/LeNet.
6. **Generalizable:** convoluciones 1D sobre secuencias; el criterio de localidad; la fragilidad observada.
7. **No trasladar:** todo lo de visión por computador.
8. **Nivel: C.**
9. **Justificación:** línea de investigación futura, no de primera etapa.

---

### Capítulo 19 — RNNs for Multivariate Time Series and Sentiment Analysis — **B**

1. **Problema:** arquitecturas recurrentes para datos secuenciales.
2. **Conceptos:** por qué las feedforward no tienen memoria y las CNN sólo comparten parámetros de forma superficial; desdoblamiento del grafo computacional; backpropagation through time; **el problema de las dependencias de largo alcance**; LSTM y GRU; RNN profundas; regresión univariante (S&P 500); **stacked LSTM combinando secuencias con features no secuenciales** mediante la API funcional de Keras (secuencia de 52 retornos semanales + embedding del ticker + dummies de mes); regresión multivariante para macro.
3. **Qué conservar:** (a) la justificación conceptual de las RNN — cada salida es función de la salida previa *y* de información nueva, lo que permite compartir parámetros a lo largo de una cadena computacional mucho más profunda; (b) el patrón arquitectónico de **combinar entradas secuenciales y no secuenciales en una misma red**; (c) el resultado empírico modesto: AUC de test ≈ 0.68 y accuracy ≈ 0.62 prediciendo el signo del retorno semanal.
4. **Relación con IRIS:** si IRIS decide modelar la secuencia intradiaria directamente en lugar de features tabulares, este es el capítulo de referencia.
5. **Específico:** retornos semanales de ~2.400 acciones; embeddings de ticker.
6. **Generalizable:** la arquitectura mixta; el formato 3D de entrada; LSTM/GRU.
7. **No trasladar:** el embedding de ticker (no hay universo de activos en IRIS).
8. **Nivel: B.**
9. **Justificación:** conceptualmente muy pertinente a un problema de serie temporal única; empíricamente no demostrado como superior.

---

### Capítulo 20 — Autoencoders for Conditional Risk Factors and Asset Pricing — **C**

1. **Problema:** compresión no lineal y extracción de representaciones.
2. **Conceptos:** autoencoders como generalización no lineal de la reducción de dimensionalidad lineal; convolucionales; regularizados y dispersos; **denoising autoencoders**; seq2seq; variacionales; autoencoder condicional que aprende simultáneamente retornos de factores y cargas condicionadas a características del activo.
3. **Qué conservar:** el **denoising autoencoder** como concepto de reducción de ruido aprendida (complementa Kalman y wavelets del cap. 4), y la idea de aprender representaciones compactas de un espacio de features grande.
4. **Relación con IRIS:** posible línea futura para comprimir un espacio de features amplio o filtrar ruido.
5. **Específico:** el modelo condicional de asset pricing es intrínsecamente cross-sectional.
6. **Generalizable:** denoising, compresión.
7. **No trasladar:** la arquitectura condicional completa.
8. **Nivel: C.**

---

### Capítulo 21 — GANs for Synthetic Time-Series Data — **C**

1. **Problema:** generar datos sintéticos realistas.
2. **Conceptos:** entrenamiento adversarial; TimeGAN; evaluación de la calidad de series sintéticas.
3. **Qué conservar:** la **motivación**: el overfitting crónico y la escasez de historia hacen valiosa la capacidad de generar datos. Jansen lo conecta explícitamente con el pitfall del período muestral: una solución posible es generar datos sintéticos que reflejen características de mercado relevantes ausentes del histórico. Y también sus **límites**: el ejemplo generó precios diarios para un número pequeño de activos, y el autor advierte que la dinámica se vuelve más compleja con más activos y mayor frecuencia.
4. **Relación con IRIS:** relevante a medio plazo para stress-testing de la estrategia, no para la primera etapa.
5. **Nivel: C.**

---

### Capítulo 22 — Deep Reinforcement Learning: Building a Trading Agent — **C**

1. **Problema:** aprender políticas de decisión por interacción con un entorno.
2. **Conceptos:** política, recompensa, función de valor; MDP finitos; iteración de política y de valor; Q-learning; ε-greedy; Deep Q-Learning y extensiones (DDQN); OpenAI Gym; entorno de trading custom.
3. **Qué conservar — y aquí las advertencias valen más que la técnica:**
   - `[JANSEN]` El RL es a menudo considerado el enfoque más prometedor porque **modela con más fidelidad la tarea real del inversor** (decisiones secuenciales con consecuencias, no predicciones aisladas).
   - `[JANSEN]` Pero sus propios ejemplos simplificados ilustran que **crear un entorno realista es un desafío considerable**.
   - `[JANSEN]` Y que el DRL puede enfrentar **mayores obstáculos** en finanzas por el ruido de los datos, que dificulta aprender una función de valor basada en recompensas diferidas.
   - `[JANSEN]` Su agente operaba un solo activo, lo que **incrementa muchísimo el riesgo de overfitting**, y necesitó el equivalente a unos 2.000 años de datos de entrenamiento para alcanzar un rendimiento similar al del mercado.
4. **Relación con IRIS:** `[IMPLICACIÓN PARA IRIS]` Muy relevante como *tentación a resistir*. IRIS opera un único instrumento, exactamente la configuración que Jansen señala como la de mayor riesgo de sobreajuste en RL.
5. **Nivel: C.**
6. **Justificación:** conceptualmente atractivo, empíricamente no respaldado por el libro para nuestro caso.

---

### Capítulo 23 — Conclusions and Next Steps — **A**

1. **Problema:** destilar las lecciones.
2. **Conceptos:** los seis takeaways (§1.3); calidad de datos; integración de fuentes; expertise de dominio; el *no free lunch*; bias-variance y curvas de aprendizaje; **optimization verification test** de Andrew Ng (distinguir si el fallo viene del algoritmo de aprendizaje o del de optimización); backtest overfitting; transparencia de modelos y el contrapunto de Hinton (quizá deban juzgarse por resultados, como a los gestores).
3. **Qué conservar:** el capítulo entero. Es la sección con mayor densidad de principios por página.
4. **Nivel: A.**

---

### Apéndice — Alpha Factor Library — **A**

1. **Problema:** catálogo de features y, más importante, **comparación empírica de métodos para evaluarlas**.
2. **Conceptos:** ~200 indicadores de TA-Lib organizados en medias móviles, overlap studies, momentum, volumen/liquidez, volatilidad, factores de riesgo fundamentales; **101 alphas formulaicas de WorldQuant** (Kakushadze 2016, de las cuales ~80% estaban en producción según reporta Jansen), con funciones cross-sectional (rank, scale) y de serie temporal (ts_lag, ts_delta, ts_rank, ts_mean, ts_weighted_mean, ts_sum, ts_product, ts_stddev, ts_max/min, ts_argmax/argmin, ts_correlation); **evaluación comparada** con IC, mutual information, feature importance de LightGBM y SHAP.
3. **Qué conservar — el hallazgo más importante del apéndice:**
   - La correlación de rangos entre SHAP y la importancia convencional por ganancia es alta (~0.89).
   - Entre SHAP y las métricas univariantes, sustancial (~0.5).
   - **Entre mutual information e Information Coefficient, sólo ~0.16.**
   - Y el ejemplo de Alpha 054: IC significativo de 0.025, spread medio de ~1.5 puntos básicos diarios entre quintil superior e inferior, y sin embargo **los retornos acumulados de una cartera long-short fueron negativos**.
4. **Relación con IRIS:** `[IMPLICACIÓN PARA IRIS]` Estos dos hallazgos son fundacionales. El primero significa que **las métricas de evaluación de features no son intercambiables**: elegir una u otra cambia qué features parecen importantes. El segundo es la demostración empírica más limpia del libro de que **poder predictivo estadísticamente significativo ≠ rentabilidad**.
5. **Específico:** universo de 500 acciones US 2007-2016; las funciones cross-sectional (rank, scale, group normalization).
6. **Generalizable:** el catálogo de indicadores; **todas las funciones ts_\*** (son puramente de serie temporal y directamente aplicables a MNQ); el protocolo de evaluación multi-métrica.
7. **No trasladar:** las funciones cross-sectional y las alphas que dependen de ellas.
8. **Nivel: A.**

---

### 2.1 Resumen del mapa

| Nivel | Capítulos |
|---|---|
| **A — Crítico** | 2 (microestructura y barras), 4, 6, 7, 8, 9 (diagnóstico y volatilidad), 11, 12, 23, Apéndice |
| **B — Importante** | 1, 5, 17, 19 |
| **C — Complementario** | 9 (cointegración), 10, 13, 18, 20, 21, 22 |
| **D — Poco relevante ahora** | 2 (datos fundamentales), 3, 14, 15, 16 |

---

## 3. DATOS FINANCIEROS: PROPIEDADES ESPECIALES (Tarea 4, parte 1)

### 3.1 Ruido y ratio señal/ruido

`[JANSEN]` El ratio señal/ruido de los datos financieros es **bajo**, y esto es la característica que define el dominio. Sus consecuencias, según el libro:

- Los modelos de alta capacidad requieren cuidado especial para no sobreajustar.
- Complejidad de modelo y complejidad de datos deben emparejarse: gestionar el trade-off bias-varianza **se vuelve más difícil cuanto mayor es el ruido**.
- Los datasets financieros son además comparativamente **pequeños** frente a los datasets de imagen o texto a escala web, lo que agrava el problema.

`[JANSEN]` Los datos de ticks crudos son "muy ruidosos" y llegan a intervalos irregulares indexados en nanosegundos. El **bid-ask bounce** hace oscilar el precio entre bid y ask según se alternen órdenes de compra y venta agresivas, generando variación que no refleja información nueva.

`[INTERPRETACIÓN]` Jansen presenta la agregación en barras precisamente como el primer mecanismo de reducción de ruido del pipeline: no es una conveniencia de formato, es una decisión estadística.

### 3.2 Distribución de retornos y no-normalidad

`[JANSEN]` Los retornos de tick están lejos de ser normales; el libro lo verifica con un test de normalidad que arroja un p-valor muy bajo. Más en general, muchos modelos de mercado asumen normalidad cuando en realidad los valores extremos se observan con más frecuencia, como indican las distribuciones de colas pesadas.

`[JANSEN]` Los retornos financieros violan con frecuencia el supuesto IID. Andrew Lo derivó los ajustes necesarios a la distribución del estimador del Sharpe ratio y a su agregación temporal para retornos estacionarios pero autocorrelacionados. Esto importa porque **las propiedades de serie temporal de una estrategia (reversión a la media, momentum, otras formas de correlación serial) tienen impacto no trivial sobre el propio estimador del Sharpe**, especialmente al anualizarlo desde datos de alta frecuencia.

`[IMPLICACIÓN PARA IRIS]` Cualquier Sharpe que calculemos anualizando desde barras intradiarias mediante √t estará mal si hay autocorrelación en los retornos de la estrategia. Esto debe verificarse, no asumirse.

### 3.3 No estacionariedad y cambios estructurales

`[JANSEN]` Una serie estacionaria tiene propiedades estadísticas (media, varianza, autocorrelación) independientes del período. Estacionariedad estricta exige que la distribución conjunta de cualquier subconjunto de observaciones sea independiente del tiempo respecto a *todos* los momentos. En la práctica se restringe a estacionariedad en covarianza: media, varianza y autocorrelación constantes.

`[JANSEN]` Los precios de activos típicamente **no** son estacionarios porque no existe un nivel al que la serie revierta. El **random walk** es el ejemplo canónico: tiene raíz unitaria, su varianza crece con el tiempo, y presenta *long memory* — al ser el valor actual la suma de todas las perturbaciones pasadas, las innovaciones grandes persisten mucho más que en una serie estacionaria con reversión a la media.

`[JANSEN]` La estacionariedad **no** prohíbe la dependencia entre valores a distintos lags. Lo que exige es que esas relaciones sean **estables**.

`[INTERPRETACIÓN]` Esta distinción es sutil y crítica: no buscamos ausencia de estructura temporal, buscamos estructura temporal *estable*. Un modelo predictivo necesita exactamente eso.

`[JANSEN]` Los cambios estructurales aparecen en el libro de forma indirecta pero consistente:
- El *factor decay*: los retornos en exceso de nuevas anomalías caen aproximadamente un cuarto desde el descubrimiento hasta la publicación, y más del 50% tras publicarse, por competencia y crowding.
- La ventaja del filtro de Kalman se formula precisamente como su capacidad de adaptarse con flexibilidad a datos no estacionarios con características distribucionales cambiantes.
- El pitfall de "sample period": un backtest no generaliza si la muestra no refleja el entorno actual y probable futuro; puede carecer de aspectos de régimen de mercado como volatilidad o volúmenes.

`[VACÍO]` Jansen **no** desarrolla detección formal de cambios de régimen, ni tests de ruptura estructural, ni estrategias de reentrenamiento adaptativo más allá del walk-forward. Es un hueco importante para IRIS.

### 3.4 Dependencia temporal, autocorrelación, heterocedasticidad

`[JANSEN]` Los datos financieros no son ni independientes ni idénticamente distribuidos, por **correlación serial** y por **desviación estándar variable en el tiempo (heterocedasticidad)**. Esta es la razón que da para que la cross-validation estándar no aplique.

`[JANSEN]` La autocorrelación mide la relación lineal entre valores separados por un lag k; la autocorrelación **parcial** elimina la influencia indirecta de los puntos intermedios y mide sólo la dependencia lineal directa a esa distancia. Ambas (ACF y PACF) son herramientas de diagnóstico centrales para el diseño de modelos lineales de serie temporal.

`[JANSEN]` Para volatilidad, el libro **abandona explícitamente el supuesto de estacionariedad en segundo momento** y asume que la varianza cambia de forma predecible: ese es el terreno de ARCH/GARCH.

`[INTERPRETACIÓN]` Hay una asimetría reveladora en el libro: la media de los retornos se trata como casi impredecible, mientras que la varianza se trata como predecible y se le dedica una sección entera. Es un indicio de dónde el propio autor cree que hay señal.

### 3.5 Frecuencia de observación

`[JANSEN]` Las opciones habituales, en orden creciente de complejidad computacional y requisitos de memoria y almacenamiento, son: diaria, minuto, tick. Frecuencias intermedias también son posibles.

`[JANSEN]` Añade una afirmación empírica relevante: las **estrategias algorítmicas tienden a rendir mejor a frecuencias más altas**, y los inversores institucionales requerirán con certeza frecuencia de tick.

`[INTERPRETACIÓN]` Esto es un argumento *a favor* de trabajar intradiario, pero Jansen no lo respalda con evidencia sistemática en el libro; su único ejemplo intradiario usa barras de minuto y produce un IC bajo aunque estadísticamente significativo.

### 3.6 Microestructura de mercado

`[JANSEN]` La microestructura estudia cómo el entorno institucional afecta al proceso de trading y moldea resultados como el descubrimiento de precios, los spreads bid-ask, el comportamiento intradiario y los costes de transacción.

`[JANSEN]` Elementos que el libro identifica como relevantes para *simular* correctamente una estrategia:
- **Tipos de orden** disponibles: market (ejecución inmediata al precio vigente), limit (sólo si el precio cruza el límite), stop (se activa al superar/perforar un nivel, y puede combinarse con límite), y condicionales (all-or-none, fill-or-kill, immediate-or-cancel, not-held, market-on-open/close).
- **Dónde se opera**: bolsas, dark pools, feed consolidado.
- La granularidad máxima disponible es la microestructura del exchange (cada orden, ejecución y cancelación), que permite reconstruir el libro de órdenes completo.

`[JANSEN]` Sobre las barras de minuto de AlgoSeek, describe qué información adicional al OHLCV existe cuando se dispone de datos de quote: precio y tamaño del bid/ask vigente, volumen negociado en o por debajo del bid, entre bid y midpoint, en el midpoint, entre midpoint y ask, y en o por encima del ask; número de acciones negociadas con uptick, downtick o sin cambio (diferenciado por la dirección previa); VWAP; y spread bid-ask mínimo y máximo de la barra.

`[IMPLICACIÓN PARA IRIS]` Esta lista es un **catálogo de lo que nos falta**. Con OHLCV puro no tenemos ninguna de estas variables. Es una pregunta abierta cuánta de la señal del ejemplo intradiario de Jansen provenía precisamente de ellas (ver §20).

### 3.7 Problemas de calidad de datos

`[JANSEN]` Los problemas que menciona explícitamente:
- **Timestamps**: es vital asignar timestamps que reflejen con precisión la disponibilidad histórica real; de lo contrario se introduce look-ahead bias.
- **Datos point-in-time**: hay que garantizar que todo dato estaba verdaderamente disponible en el momento en que se usa como input.
- **Corporate actions**: splits, dividendos y reexpresiones requieren ajustes previos a la ingesta.
- **Errores de datos**: en un ejemplo, retornos mensuales superiores al 100% se marcan como faltantes por considerarse probables errores.
- **Outliers**: winsorización o clipping, con la advertencia de que hay que **distinguir outliers no representativos de valores extremos que son parte integral del entorno de mercado**.
- **Calendarios de trading**: ayudan a limitar los datos a fechas y horas legítimas.
- **Horario**: en el ejemplo intradiario, Jansen restringe deliberadamente a las 390 barras de 9:30 a 16:00, tanto para acotar el tamaño como **para evitar períodos de actividad irregular**.

### 3.8 Normalización, transformaciones y almacenamiento

`[JANSEN]` Transformaciones documentadas:
- **Log** para convertir crecimiento exponencial en tendencia lineal y estabilizar varianza.
- **Deflación** (dividir por otra serie que causa la tendencia).
- **Detrending** por regresión sobre índice temporal, usando residuos.
- **Diferenciación** (período a período o estacional). Aplicada a una serie log-transformada, el resultado representa tasas de crecimiento instantáneas, es decir, retornos.
- **Winsorización** de retornos (en un ejemplo, en los percentiles 0.01 y 99.99; en otro, en 1 y 99).
- **Estandarización** de indicadores para hacerlos comparables entre activos (ejemplo: normalizar el ATR).
- **Log de diferencias porcentuales** para comprimir distribuciones (ejemplo: distancia del precio a las bandas de Bollinger).
- **Escalas de ranking** (ejemplo: rankear en escala 1-20 respecto al retorno reciente).

`[JANSEN]` Almacenamiento: recomienda formatos **HDF5 y parquet** por velocidad de exploración e iteración; para datos que no caben en memoria, procesamiento distribuido (Spark).

`[INTERPRETACIÓN]` La normalización en Jansen tiene dos propósitos distintos que conviene no confundir: (a) hacer comparables activos distintos —irrelevante para IRIS—, y (b) estabilizar la distribución de una variable en el tiempo —muy relevante para IRIS.

### 3.9 Implicaciones potenciales para MNQ intradiario

Sin cerrar ninguna decisión, esto es lo que el capítulo obliga a investigar sobre nuestros propios datos:

| Pregunta a investigar sobre el MNQ | Por qué, según Jansen |
|---|---|
| ¿Cuál es la distribución empírica de los retornos a distintas frecuencias? ¿Colas, asimetría, curtosis? | Los retornos de alta frecuencia no son normales; muchos métodos lo asumen. |
| ¿Cuánta autocorrelación hay en retornos y en retornos absolutos/cuadrados, a distintos lags? | ACF/PACF son el diagnóstico previo obligatorio; los retornos al cuadrado revelan clustering de volatilidad. |
| ¿Es estacionaria alguna transformación de la serie? ¿ADF sobre qué? | Requisito de los modelos clásicos; e indicador de si el precio es cercano a random walk. |
| ¿Cómo varía la volatilidad **intradía** (apertura, mediodía, cierre, overnight)? | Jansen restringe el horario precisamente por actividad irregular; la estacionalidad intradiaria es un patrón determinista que puede confundirse con señal. |
| ¿Cómo varía el volumen intradía y entre días? | Motiva la elección entre barras temporales y barras de volumen. |
| ¿Qué proporción del movimiento diario ocurre fuera del horario RTH? ¿Incluimos globex? | Decisión de universo temporal, análoga a la del ejemplo intradiario. |
| ¿Cómo tratamos los **rollovers de contrato**? | Análogo funcional de las corporate actions: crea saltos artificiales de precio. Jansen exige ajustar antes de la ingesta. |
| ¿Qué gaps, barras faltantes, precios repetidos o volúmenes cero hay? | Control de calidad básico; además, "precio repetido" es una feature real en su ejemplo intradiario. |
| ¿Qué valores extremos son errores y cuáles son eventos de mercado reales? | Advertencia explícita sobre control de outliers. |
| ¿Cuánto histórico tenemos realmente y cuántos regímenes distintos contiene? | El pitfall del período muestral y la regla de longitud mínima de backtest. |
| ¿El bid-ask bounce es material a nuestra frecuencia candidata? | Es el argumento base para agregar. |
| ¿Tenemos o podemos obtener datos de quote/tick, o sólo OHLCV? | Determina si podemos replicar las features más informativas de su ejemplo intradiario. |

---

## 4. MARKET MICROSTRUCTURE — SÍNTESIS OPERATIVA

`[JANSEN]` La razón por la que la microestructura importa a un proyecto de ML no es teórica: los detalles institucionales condicionan **la interpretación correcta de los datos de mercado, el diseño de la estrategia, y la implementación de backtests realistas**.

Tres consecuencias concretas que el libro deriva:

1. **Interpretación**: el precio observado en una barra depende de cómo se agregó y de qué eventos la generaron. Una barra de tiempo con poco volumen y una con mucho volumen no son observaciones equivalentes.
2. **Diseño**: los tipos de orden disponibles determinan qué reglas operativas son siquiera expresables.
3. **Simulación**: los costes (comisiones, spread, slippage) y el timing de ejecución deben modelarse; los mercados no permiten ejecutar cualquier operación en cualquier momento al precio objetivo.

`[JANSEN]` Sobre momentum, hace una observación de microestructura directamente pertinente a horizontes cortos: en horizontes intradiarios, efectos de microestructura pueden **crear** momentum de precio porque los participantes implementan estrategias que comprometen anticipadamente a vender cuando un activo cae y comprar cuando sube (stop-loss, CPPI, delta hedging dinámico, protective puts). El rebalanceo automático de estrategias de risk parity refuerza el mismo efecto.

`[IMPLICACIÓN PARA IRIS]` Este es uno de los pocos pasajes donde Jansen ofrece un **racional económico para señal intradiaria en un instrumento único**, sin depender de sección transversal. Merece ser retenido como hipótesis candidata: el momentum de corto plazo puede tener origen mecánico en el comportamiento de otros participantes, no sólo estadístico.

---

## 5. MUESTREO Y CONSTRUCCIÓN DE BARRAS (Tarea 4, parte 2)

### 5.1 El problema

`[JANSEN]` Los datos de trade llegan a intervalos irregulares y son muy ruidosos. Para mejorar el ratio señal/ruido y las propiedades estadísticas de la serie de precios, hay que **remuestrear y regularizar** agregando la actividad de trading.

`[INTERPRETACIÓN]` Nótese la formulación: agregar es un acto de *mejora estadística deliberada*, no un requisito técnico. La elección del esquema de agregación es, por tanto, una decisión de modelado.

### 5.2 Los cuatro tipos de barra

| Tipo | Criterio de agregación | Qué problema resuelve | Qué limitación tiene |
|---|---|---|---|
| **Tick bars** | Materia prima cruda: cada operación | Ninguno; es el punto de partida | Ruido máximo, intervalos irregulares, bid-ask bounce, retornos fuertemente no normales |
| **Time bars** | Períodos de reloj fijos | Denoising básico; regulariza el índice temporal | `[JANSEN]` Pueden **fallar en dar cuenta de la fragmentación de órdenes**: una sola orden grande dividida en muchas ejecuciones (p.ej. por un algoritmo VWAP) se distribuye entre barras distintas aunque no haya llegado información nueva al mercado |
| **Volume bars** | Cantidad fija de volumen acumulado | Alinea el muestreo con la actividad real en lugar del reloj | `[JANSEN]` No reflejan correctamente cambios significativos de precio ni splits: el valor de una cantidad dada de acciones cambia |
| **Dollar bars** | Cantidad fija de valor negociado (precio × cantidad) | Corrige el problema anterior de las volume bars | El libro no discute sus limitaciones |

`[JANSEN]` La computación en todos los casos recoge OHLCV del período agregado, más VWAP y el timestamp asociado.

### 5.3 Lo que Jansen NO hace con esto

`[VACÍO]` El libro **presenta** las cuatro barras en unas pocas páginas del capítulo 2 y luego **no las usa**. Todo el resto del libro —incluido el ejemplo intradiario del capítulo 12— trabaja con **barras temporales** (diarias, semanales, mensuales o de minuto).

`[VACÍO]` No hay:
- Comparación empírica del contenido de señal según tipo de barra.
- Análisis de cómo cambian las propiedades estadísticas (normalidad, autocorrelación, estacionariedad) con el esquema de muestreo.
- Discusión de cómo interactúa el tipo de barra con la validación temporal o con el labeling.
- Ninguna barra basada en información o en desequilibrio de órdenes.

`[IMPLICACIÓN PARA IRIS]` Jansen nos da **el vocabulario y la motivación** de las barras alternativas, pero no evidencia sobre si mejoran resultados. Esta es explícitamente una pregunta que llevamos abierta a la siguiente etapa (López de Prado desarrolla este tema con mucha más profundidad, pero no anticipamos aquí sus conclusiones).

### 5.4 Preguntas abiertas sobre muestreo para el MNQ

- ¿Qué esquema de muestreo produce retornos con mejores propiedades estadísticas en MNQ?
- ¿La fragmentación de órdenes es un fenómeno material en MNQ, dado que es un futuro centralizado con alta participación algorítmica?
- ¿El equivalente del problema de "splits" en futuros es el rollover, y las dollar bars lo resuelven o lo agravan?
- ¿Un esquema de muestreo no temporal complica la relación entre nuestras señales y el horizonte de trading real (que se mide en tiempo de reloj)?
- Si usamos barras no temporales, ¿cómo se define un horizonte predictivo "de N barras" en términos económicos?

---

## 6. FEATURES Y ALPHA FACTORS (Tarea 5, parte 1)

### 6.1 Definición y encuadre

`[JANSEN]` Un alpha factor es una transformación de datos crudos que aspira a predecir movimientos de precio de activos, diseñada para capturar riesgos que impulsan los retornos. Puede combinar uno o varios inputs pero produce **un único valor por activo cada vez que se evalúa**. Las decisiones de trading pueden basarse en valores relativos entre activos **o en patrones de un activo individual**.

`[JANSEN]` Requisito previo esencial: para evitar falsos descubrimientos y garantizar consistencia, un factor **debería tener una intuición económica significativa** basada en categorías establecidas y sus racionales. Esto hace más plausible que el factor refleje un riesgo por el que el mercado compensa.

`[JANSEN]` Y una advertencia de escala: hacia 2015 se habían publicado unos 250 factores con evidencia empírica en revistas reputadas, con estimación de crecimiento de unos 40 al año.

`[INTERPRETACIÓN]` La combinación de esas dos afirmaciones es el mensaje real: no hay escasez de factores; hay escasez de factores que sobrevivan fuera de muestra. La intuición económica funciona como **prior** que reduce el espacio de búsqueda y por tanto el multiple testing.

### 6.2 Las categorías de factores y sus racionales

Jansen organiza décadas de investigación en cuatro familias, cada una con explicación racional y conductual.

**Momentum / sentimiento.** `[JANSEN]` Premisa: los precios exhiben tendencia, reflejada en correlación serial positiva. Racionales: infrarreacción y sobrerreacción a noticias (los inversores procesan información a velocidades distintas); psicología de miedo y codicia; retroalimentación positiva entre activos de riesgo y economía; desequilibrios persistentes de oferta y demanda por fricciones; y —clave para nosotros— **efectos de microestructura en horizontes intradiarios** (ver §4). Métricas típicas: RSI, momentum de precio, momentum de 12 meses ajustado por volumen, aceleración de precio, distancia porcentual al máximo de 52 semanas.

**Valor.** `[JANSEN]` Se basa en reversión a la media hacia un valor justo. Sus propiedades son a menudo **opuestas** a las de momentum. `[IMPLICACIÓN PARA IRIS]` Requiere fundamentales; no aplicable a un futuro sobre índice. La *idea* de reversión a la media sí es aplicable, pero entonces no es un factor de valor sino un factor técnico de reversión.

**Volatilidad y tamaño.** `[JANSEN]` El efecto tamaño (exceso de rendimiento de capitalizaciones bajas) y el factor de baja volatilidad (exceso de rendimiento de acciones con volatilidad, beta o riesgo idiosincrático por debajo de la media). `[IMPLICACIÓN PARA IRIS]` El tamaño no aplica. La volatilidad como *variable de estado* sí es central.

**Calidad.** Requiere fundamentales. No aplicable.

`[INTERPRETACIÓN]` De las cuatro familias canónicas de Jansen, **sólo momentum y volatilidad tienen traducción directa a un futuro sobre índice operado intradía**. Esto reduce drásticamente el catálogo utilizable y refuerza que no debemos asumir que los indicadores técnicos contienen señal sólo porque el libro los lista.

### 6.3 Construcción de features: el catálogo instrumental

`[JANSEN]` Operaciones aritméticas simples sobre datos crudos: cambios absolutos o relativos en el tiempo, ratios entre series, agregaciones sobre ventanas (media móvil simple o exponencial).

`[JANSEN]` **Retornos y lags**: cálculo de retornos a múltiples escalas (1 día, 1 y 2 semanas, 1, 2, 3 meses en su ejemplo), transformados a media geométrica diaria para hacerlos comparables, winsorizados, y desplazados para servir como features. Además de los retornos más recientes de cada período, usa también los **5 resultados previos** de cada escala.

`[JANSEN]` **Rolling statistics**: pandas con ventanas móviles o expansivas, pesos uniformes o decrecientes; media, suma, desviación estándar, correlación, covarianza, y funciones definidas por el usuario. Las medias móviles exponenciales calculan recursivamente pesos que decaen para observaciones más antiguas.

`[JANSEN]` **Indicadores técnicos vía TA-Lib**: más de 200 indicadores estandarizados que usan sólo precio y volumen. Ejemplos que utiliza en distintos capítulos: RSI, Bandas de Bollinger, ATR/NATR, MACD, PPO, medias móviles ponderadas y exponenciales, rate of change, Chande Momentum Oscillator, Chaikin A/D Oscillator, ADX, Balance of Power, Commodity Channel Index, Money Flow Index.

`[JANSEN]` Sobre Bollinger Bands hace una observación honesta: en su gráfico ilustrativo, tanto las bandas como el RSI señalaron condiciones de sobrecompra durante la recuperación post-crisis mientras el precio seguía subiendo. Es decir, **muestra explícitamente el indicador fallando**.

`[JANSEN]` **Indicadores temporales**: variables indicadoras de año, mes, día de la semana para capturar efectos estacionales (menciona el efecto enero). `[IMPLICACIÓN PARA IRIS]` En su modelo de boosting diario, **los indicadores de período temporal dominaron la importancia de features**. Esto es relevante y preocupante a la vez: en intradiario, la hora del día es probablemente una variable de estado muy potente (apertura, cierre, sesión europea/americana), pero también un candidato ideal para sobreajustar a patrones de calendario espurios.

`[JANSEN]` **Funciones de serie temporal de WorldQuant** (Apéndice): ts_lag, ts_delta, ts_rank, ts_mean, ts_weighted_mean, ts_sum, ts_product, ts_stddev, ts_max, ts_min, ts_argmax, ts_argmin, ts_correlation. `[IMPLICACIÓN PARA IRIS]` Este es **el subconjunto del apéndice directamente utilizable en IRIS**, porque no requiere sección transversal. Las funciones cross-sectional (rank, scale, normalización por grupo) no aplican.

`[JANSEN]` Advierte además que las alphas formulaicas, a diferencia de los factores comunes, **no vienen acompañadas de una interpretación económica** del riesgo que representan, y que su minería a gran escala es propensa a sesgo de pruebas múltiples y falsos descubrimientos.

### 6.4 Filtrado y reducción de ruido

**Filtro de Kalman.** `[JANSEN]`
- Es un modelo lineal dinámico de datos secuenciales que se adapta a nueva información conforme llega.
- A diferencia de una media móvil (ventana fija) o de una EMA (pesos dados), incorpora los datos nuevos a su estimación del valor actual **según un modelo probabilístico**.
- Modela una secuencia de observaciones y una secuencia de estados ocultos; toma un enfoque bayesiano que propaga la distribución posterior de los estados dadas las mediciones.
- **Supuestos**: sistema lineal; el proceso de estado oculto es una cadena de Markov; las mediciones están sujetas a ruido gaussiano no correlacionado de covarianza constante.
- **Ventaja**: se adapta con flexibilidad a datos no estacionarios con características distribucionales cambiantes; no requiere especificar la longitud de una ventana.
- **Desventaja explícita**: los supuestos de linealidad y ruido gaussiano **que los datos financieros violan con frecuencia**. Existen extensiones (Kalman extendido, unscented) y alternativas (filtro de partículas con Monte Carlo para distribuciones no normales).
- En su ejemplo sobre el S&P 500, el filtro se comporta de forma similar a una media móvil de un mes pero **es más sensible a los cambios de comportamiento de la serie**.

**Wavelets.** `[JANSEN]`
- Descomponen una señal en componentes de distintas escalas.
- Ventaja sobre Fourier: mejores para funciones con discontinuidades y picos abruptos, y para aproximar señales no periódicas o no estacionarias.
- Denoising por *shrinkage/thresholding*: se descompone, se omiten los coeficientes por debajo de un umbral (asumiendo que representan detalles menores que no forman parte de la señal verdadera), y se reconstruye con la transformada inversa.
- Umbrales más altos producen series significativamente más suaves.

`[INTERPRETACIÓN]` Ambas técnicas comparten un riesgo que Jansen no subraya lo suficiente: **suavizar puede introducir look-ahead si la implementación usa información futura**. Un filtro de Kalman en modo *filter* (sólo pasado) es causal; en modo *smooth* (usando toda la serie) no lo es. Lo mismo con la reconstrucción wavelet sobre una serie completa. `[IMPLICACIÓN PARA IRIS]` Cualquier denoising que apliquemos debe ser estrictamente causal, verificado explícitamente.

### 6.5 Relaciones lineales, no lineales e interacciones

`[JANSEN]` La razón de ser de los modelos no lineales (ensembles de árboles, redes) es en parte su capacidad de detectar relaciones no lineales, **en particular efectos de interacción entre variables**. La capacidad de modular el impacto de una variable en función de otras se nutre de inputs que capturan aspectos distintos del mismo resultado.

`[JANSEN]` Herramientas para visualizar estas relaciones: partial dependence plots (individuales y por pares, en 2D o 3D), que marginalizan el resto de features y permiten interpretar la dependencia parcial como la respuesta esperada del target.

`[IMPLICACIÓN PARA IRIS]` Esto sugiere un criterio de diseño de features: no basta añadir variantes de la misma información (cinco medias móviles de longitudes parecidas), sino **inputs que capturen dimensiones distintas** (tendencia, volatilidad, volumen, hora, estructura de la barra), donde las interacciones puedan aportar algo.

### 6.6 Normalización y escalado

`[JANSEN]` Usos documentados: estandarización de indicadores para comparabilidad entre activos; logs de diferencias porcentuales para comprimir distribuciones; winsorización; rankings; dummy encoding de categóricas (con la advertencia de que convertir *todas* las categorías en dummies y estimar con intercepto genera multicolinealidad); LightGBM no requiere one-hot encoding porque ordena categorías según el outcome.

`[VACÍO]` Jansen **no discute sistemáticamente** cómo normalizar features en un contexto de serie temporal única y no estacionaria — por ejemplo, si usar z-scores rolling, cuál debe ser la ventana, o cómo evitar que la normalización introduzca look-ahead. Es un hueco relevante para IRIS.

---

## 7. EVALUACIÓN DE FACTORES: ¿CÓMO SABEMOS SI UNA FEATURE CONTIENE INFORMACIÓN? (Tarea 5, parte 2)

Esta es, junto con §15-16, la sección más importante del documento.

### 7.1 Information Coefficient (IC)

`[JANSEN]`
- **Definición**: el objetivo de un alpha factor es la predicción direccional precisa de retornos futuros, por lo que una medida natural de rendimiento es la **correlación entre las predicciones del factor y los retornos futuros** de los activos objetivo.
- **Se recomienda la correlación de rangos de Spearman** en lugar de Pearson, porque mide si la relación puede describirse mediante una función monótona, no si es lineal.
- Se calcula período a período y suele visualizarse como serie temporal con media móvil.
- **IC ajustado por riesgo**: media del IC dividida por su desviación estándar, con test t de dos colas contra la hipótesis nula IC = 0.
- **Magnitudes**: un IC de 0.05 o incluso 0.1 permite superar significativamente al benchmark si hay suficientes oportunidades de aplicar esa habilidad predictiva. Un IC por debajo de 0.05 es bajo pero puede ser significativo. En la práctica, gestores con un conjunto amplio de decisiones de inversión pueden lograr excesos de rendimiento ajustados por riesgo relevantes con IC entre 0.05 y 0.15.
- El IC del factor de ejemplo era **históricamente irregular**: gráficamente muestra su variación año a año.

`[IMPLICACIÓN PARA IRIS]` Tres cosas que hay que retener:
1. El IC de una señal útil es **bajo en términos absolutos**. Si obtenemos IC de 0.3 en MNQ, la primera hipótesis debe ser leakage, no descubrimiento.
2. La condición "si hay suficientes oportunidades de aplicar esa habilidad" es exactamente donde el trading intradiario de un instrumento único **puede** compensar el bajo IC con frecuencia — pero sólo si las apuestas son razonablemente independientes (ver §18.3).
3. Hay que reportar **la estabilidad temporal del IC**, no sólo su media.

### 7.2 Mutual Information

`[JANSEN]`
- Mide la dependencia mutua entre dos variables y **extiende la noción de correlación a relaciones no lineales**; cuantifica la información obtenida sobre una variable a través de la otra. Está estrechamente relacionada con la entropía.
- Disponible en scikit-learn para regresión y clasificación.
- **Hallazgo empírico del apéndice**: la correlación de rangos entre las clasificaciones de features por MI y por IC es de apenas ~0.16. Jansen se muestra sorprendido de que MI discrepe tanto y de que pocas de las features que MI puntúa alto tengan un papel significativo en el modelo de gradient boosting. Su explicación tentativa es que el cálculo usa sólo una muestra del 10% y los scores parecen sensibles al tamaño muestral.

`[IMPLICACIÓN PARA IRIS]` Esto es una advertencia doble: (a) las métricas univariantes no coinciden entre sí, así que **elegir una sola es una decisión con consecuencias**; (b) la MI estimada por vecinos más próximos es cara y sensible al muestreo, lo que en datos intradiarios (millones de observaciones) exigirá cuidado.

### 7.3 Retornos por quantil del factor

`[JANSEN]`
- Se agrupan las observaciones por quantil del valor del factor y se comparan los **retornos futuros medios** por quantil, para varios horizontes de holding.
- **Criterio de un factor útil**: debería entregar retornos marcadamente distintos entre quantiles distintos — negativos en el quintil inferior, positivos en el superior. Y los retornos acumulados de cada quintil deberían desarrollarse por trayectorias claramente separadas.
- **Pero además hay que mirar la dispersión, no sólo las medias**: en su ejemplo, el gráfico de violín muestra que el rango de retornos diarios es bastante amplio y que, pese a medias distintas, **la separación de las distribuciones es muy limitada**, de modo que en un día cualquiera las diferencias de rendimiento entre quintiles pueden ser bastante escasas.

`[INTERPRETACIÓN]` Este es uno de los puntos más honestos del libro. Una diferencia de medias estadísticamente significativa entre grupos con distribuciones casi solapadas significa que **el factor discrimina poblaciones, no eventos individuales**. Para una estrategia que toma decisiones una a una, eso es una limitación severa.

`[IMPLICACIÓN PARA IRIS]` La traducción a serie temporal única es directa y conserva el sentido: agrupar los momentos históricos por decil del valor de la feature y comparar la distribución del retorno futuro. Es un análisis que **podemos y debemos hacer sobre MNQ** aunque no tengamos sección transversal.

### 7.4 Turnover del factor

`[JANSEN]`
- Mide con qué frecuencia cambian los activos asociados a un quantil dado; concretamente, la proporción de activos actualmente en un quantil que no estaban en él el período anterior.
- Vista alternativa: la correlación del rango del activo a lo largo de distintos horizontes de holding.
- **Criterio**: en general **más estabilidad es preferible** para mantener los costes de trading manejables. En su ejemplo, el turnover alto sugiere que los costes de trading suponen un desafío para capturar el beneficio del rendimiento predictivo.
- Conectado con el pitfall de costes: limitar el universo y usar supuestos realistas protege también contra conclusiones engañosas derivadas de **señales de factor inestables que decaen rápido y producen turnover alto**.

`[IMPLICACIÓN PARA IRIS]` En intradiario, el turnover es *el* problema. Una señal que cambia de signo cada pocas barras generará costes que dominarán cualquier edge. El análogo directo de "factor turnover" en IRIS sería la **persistencia/autocorrelación de la propia señal** y la frecuencia de cambio de signo.

### 7.5 Feature importance, permutation importance y SHAP

`[JANSEN]` Tres formas de importancia global en modelos de árboles:
- **Gain**: la contribución total de la feature a la reducción de la función de pérdida (enfoque clásico de Breiman, 1984).
- **Split count**: cuántas veces se usa la feature.
- **Permutation**: se permutan aleatoriamente los valores de la feature en un conjunto de test y se mide la degradación del rendimiento.

`[JANSEN]` **SHAP**:
- Parte de la constatación de que los métodos de atribución de features para ensembles de árboles son **inconsistentes**: un cambio en el modelo que aumente el impacto de una feature sobre la salida puede *reducir* su valor de importancia.
- Unifica teoría de juegos colaborativos con explicaciones locales; es teóricamente óptimo, consistente y localmente preciso.
- La innovación algorítmica clave redujo la complejidad de O(TLDM) a O(TLD²) (T = árboles, M = features, D = profundidad máxima, L = hojas), permitiendo explicar predicciones de modelos con miles de árboles y features en fracciones de segundo.
- Se calcula **para cada feature y cada muestra**: mide cómo contribuye una feature a la salida del modelo para una observación dada. Esto ofrece visión diferenciada de cómo varía el impacto de una feature entre muestras, algo importante dado el papel de los efectos de interacción en modelos no lineales.
- Visualizaciones: media de valores absolutos por feature (resumen global); scatterplot que muestra el impacto de cada feature en cada muestra coloreado por el valor de la feature; **force plots** para explicar una predicción individual; force plots apilados con clustering aglomerativo jerárquico para descubrir patrones de influencia recurrentes en el dataset.
- **Hallazgo**: comparando con la importancia convencional, SHAP dio más peso al MACD y a medidas de retorno relativo.

`[JANSEN]` **Comparación de métricas (Apéndice)**: correlación de rangos SHAP ↔ importancia por gain ≈ 0.89; SHAP ↔ métricas univariantes ≈ 0.5; MI ↔ IC ≈ 0.16.

### 7.6 El criterio final: rendimiento fuera de muestra

`[JANSEN]` Todas las métricas anteriores son intermedias. El criterio último es el **valor de las señales de trading**, evaluado con supuestos realistas fuera de muestra.

Y aquí el libro entrega su ejemplo más contundente: **Alpha 054 tenía un IC significativo de 0.025 y un spread medio diario de ~1.5 puntos básicos entre quintiles extremos, pero los retornos acumulados de la cartera long-short fueron negativos.**

`[INTERPRETACIÓN]` Un factor puede simultáneamente: (a) tener correlación estadísticamente significativa con retornos futuros, (b) producir spreads positivos entre quantiles en promedio, y (c) **perder dinero**. Las razones posibles son concentración temporal de los aciertos, asimetría de la distribución, o simplemente que un spread medio pequeño no sobrevive a la variabilidad.

### 7.7 Riesgos de la búsqueda de features

`[JANSEN]` Riesgos que el libro identifica explícitamente:

**Feature mining / data snooping.** La minería de señales en datasets grandes es propensa a sesgo de pruebas múltiples y falsos descubrimientos. Jansen recoge la crítica de que la mayoría de resultados empíricos en finanzas —afirmaciones de señal predictiva en cientos de variables— se basan en data mining generalizado y no son robustos a cambios en el diseño experimental: la significación estadística resulta a menudo de ensayo y error a gran escala más que de una relación sistemática real.

**Selección por rendimiento histórico.** El *factor decay* implica que un factor que funcionó bien históricamente tiende a funcionar peor después: los excesos de rendimiento caen ~25% desde el descubrimiento hasta la publicación y más del 50% después.

**Multicolinealidad.** Convertir todas las categorías en dummies con intercepto la genera inadvertidamente; en el diagnóstico de modelos lineales aparece como problema a detectar y remediar.

**Maldición de la dimensionalidad.** Tratada en el capítulo 13 como motivación de la reducción de dimensionalidad.

**Features redundantes y correlacionadas.** `[JANSEN]` Menciona que el análisis exploratorio incluye la correlación entre factores, aunque en el apéndice la omite del texto principal. `[VACÍO]` No hay un tratamiento sistemático de cómo la correlación entre features distorsiona las medidas de importancia (ver §19.4).

**Sobreoptimización.** El riesgo de backtest overfitting no surge sólo de correr muchas pruebas, sino también de diseñar estrategias basándose en conocimiento previo de qué funciona y qué no. Como esos riesgos incluyen el conocimiento de backtests hechos por *otros* sobre los *mismos* datos, es muy difícil de evitar en la práctica.

`[JANSEN]` **La solución que propone**: priorizar pruebas justificables por teoría económica o de inversión, en lugar de esfuerzos arbitrarios de minería de datos; testear en contextos y escenarios variados, incluyendo posiblemente datos sintéticos; y reportar el número de pruebas realizadas para permitir evaluar el riesgo de sesgo de selección.

---

## 8. FORMULACIÓN DEL PROBLEMA PREDICTIVO (Tarea 3)

`[JANSEN]` El principio rector: la misma tarea puede formularse de varias maneras, y la elección es de diseño. El ejemplo que da: combinar varios alpha factors puede plantearse como regresión de retornos, clasificación binaria de dirección, o clasificación multiclase por quintiles de rendimiento.

`[JANSEN]` La taxonomía base: salida continua → **regresión**; salida categórica → **clasificación**; categórica ordenada → **ranking**.

A continuación, cada enfoque analizado según el esquema pedido. Marco con `[JANSEN]` lo que el libro sostiene y con `[INTERPRETACIÓN]` lo que deduzco.

### 8.1 Predecir precios

- **Qué aprende el modelo**: el nivel futuro del precio.
- **Información requerida**: la serie de precios.
- **Ventajas**: interpretación directa.
- **Problemas**: `[JANSEN]` Los precios típicamente no son estacionarios y suelen comportarse como random walk con raíz unitaria. `[INTERPRETACIÓN]` Un modelo entrenado sobre niveles aprenderá esencialmente a repetir el último precio, obteniendo R² altísimo y valor predictivo nulo. Es la trampa clásica.
- **Riesgo de ruido**: el modelo confundirá la tendencia con señal.
- **Evaluación**: RMSE sobre precios es engañosa por la razón anterior.
- **Relación con señal de trading**: prácticamente nula sin transformación.
- **Veredicto según Jansen**: el libro **nunca** predice niveles de precio. Siempre predice retornos o direcciones. `[INTERPRETACIÓN]` Esa ausencia es una posición metodológica implícita.

### 8.2 Predecir retornos (regresión continua)

- **Qué aprende**: la magnitud y el signo del retorno a horizonte h.
- **Información requerida**: features en t, retornos forward en t+h.
- **Ventajas**: `[JANSEN]` conserva toda la información del outcome; permite ranking natural; es la formulación que Jansen usa con más frecuencia (regresión lineal, LightGBM, NN, CNN). Permite dimensionar posiciones según magnitud esperada.
- **Problemas**: `[JANSEN]` RMSE está dominada por errores grandes y por tanto por el ruido; en un entorno de bajo ratio señal/ruido la métrica de error puede ser casi insensible a la parte útil de la predicción. `[INTERPRETACIÓN]` De hecho, Jansen **casi nunca reporta RMSE** en sus ejemplos financieros: reporta IC. Es decir, entrena una regresión pero la evalúa como un problema de ranking.
- **Riesgo de ruido**: alto — la varianza del target es mayormente irreducible.
- **Evaluación**: IC (Spearman) por período, IC medio, IC ajustado por riesgo, spread por quantil.
- **Relación con señal**: directa vía ranking o umbral.

### 8.3 Predecir dirección (clasificación binaria)

- **Qué aprende**: probabilidad de que el retorno futuro sea positivo.
- **Información requerida**: igual, con target binarizado.
- **Ventajas**: `[JANSEN]` La regresión logística permite inferencia estadística sobre los coeficientes; la clasificación produce scores que pueden calibrarse; el **umbral es en sí mismo una variable de decisión que debe optimizarse teniendo en cuenta costes y beneficios de aciertos y errores**. `[INTERPRETACIÓN]` Esta última afirmación es muy relevante para IRIS: el umbral es donde se puede insertar la opción "no operar".
- **Problemas**: `[JANSEN]` El clasificador normalmente **no produce probabilidades calibradas**; el score debe convertirse en predicción mediante un umbral que es una decisión aparte. `[INTERPRETACIÓN]` Binarizar destruye la información de magnitud: un movimiento de +0.01% y uno de +2% se etiquetan igual, y como los pequeños son mucho más frecuentes, el modelo optimiza esencialmente contra ruido.
- **Riesgo de ruido**: muy alto cerca del umbral cero.
- **Evaluación**: matriz de confusión, accuracy, ROC-AUC (con la propiedad de representar la probabilidad de que el clasificador ordene una instancia positiva por encima de una negativa aleatoria, y de ser insensible al desequilibrio de clases), precision-recall, F1.
- **Relación con señal**: directa. `[JANSEN]` En su LSTM con target binario obtuvo AUC ≈ 0.68 y accuracy ≈ 0.62 sobre retornos semanales.

### 8.4 Predecir magnitud

- `[INTERPRETACIÓN]` Jansen no trata la magnitud como problema separado; está implícita en la regresión de retornos.
- `[VACÍO]` No hay tratamiento de predicción de magnitud independiente del signo (por ejemplo, "¿habrá un movimiento de al menos X?"), ni de targets basados en umbrales de movimiento.

### 8.5 Detección de eventos

- `[VACÍO]` **Jansen no aborda la detección de eventos como formulación predictiva.** No hay filtros de eventos, ni muestreo condicionado a eventos, ni labeling basado en la ocurrencia de un movimiento definido.
- `[JANSEN]` Lo más cercano: Alphalens permite analizar el rendimiento de un factor durante eventos específicos, y pyfolio permite comparar el rendimiento durante períodos de eventos históricos. Pero eso es análisis *post-hoc*, no formulación del problema.
- `[IMPLICACIÓN PARA IRIS]` Este es un hueco significativo, especialmente relevante para nuestra pregunta "¿existe actualmente una oportunidad operativa?", que es intrínsecamente una formulación de detección de eventos.

### 8.6 Estimar volatilidad

- **Qué aprende**: la varianza condicional futura.
- `[JANSEN]` Es el único caso donde el libro trata explícitamente la varianza como predecible: los modelos ARCH/GARCH abandonan el supuesto de estacionariedad en segundo momento y asumen que la varianza cambia de forma predecible.
- **Ventajas**: `[INTERPRETACIÓN]` La volatilidad es notablemente más predecible que la media de los retornos. Es un target con mucho mejor ratio señal/ruido.
- **Relación con señal de trading**: `[INTERPRETACIÓN]` Indirecta pero potencialmente valiosa: sizing de posición, definición de stops, y filtro de régimen ("no operar cuando la volatilidad esperada supere X").
- `[IMPLICACIÓN PARA IRIS]` Una formulación que IRIS no debería descartar: predecir *volatilidad* en lugar de *dirección*, y usar esa predicción como componente de la decisión.

### 8.7 Estimar probabilidades

- `[JANSEN]` La salida de un clasificador es un score que puede interpretarse como probabilidad, pero normalmente **no está calibrado**. El enfoque bayesiano del capítulo 10 sí produce distribuciones posteriores genuinas.
- **Ventajas**: `[INTERPRETACIÓN]` Una probabilidad calibrada es lo que permite responder "¿qué nivel de confianza existe en la señal?" y decidir el sizing.
- **Problemas**: la calibración requiere un procedimiento explícito que Jansen no desarrolla.
- `[VACÍO]` No hay tratamiento de calibración de probabilidades (Platt scaling, isotónica, etc.).

### 8.8 Clasificación multiclase

- `[JANSEN]` La menciona como alternativa (asignar activos a clases de rendimiento como quintiles de retorno). En el capítulo 18 señala que el trabajo original de CNN-TA que replica usaba un enfoque de clasificación con etiquetas buy/hold/sell generadas algorítmicamente, mientras que su propia réplica aplicó regresión a los retornos diarios.
- `[INTERPRETACIÓN]` La formulación tri-clase (comprar / no hacer nada / vender) es la que más se parece a lo que IRIS quiere responder. Jansen la menciona pero **no la implementa ni la evalúa**, y no describe el mecanismo de etiquetado que usa el trabajo original.
- `[VACÍO]` Importante: cómo definir la clase "no operar" es exactamente el problema que Jansen no resuelve.

### 8.9 Ranking

- `[JANSEN]` Lo identifica como el caso especial de variable categórica ordenada.
- `[INTERPRETACIÓN]` Es, de facto, la formulación **implícita** de casi todo el libro: aunque entrene regresión, evalúa con IC de Spearman (una métrica de ranking) y opera con top-N/bottom-N (una regla de ranking).
- `[IMPLICACIÓN PARA IRIS]` **El ranking es la formulación menos trasladable a IRIS**, porque ordenar requiere una sección transversal. La única traducción posible sería un ranking *temporal* (¿está el momento actual entre el X% de momentos más favorables históricamente?), que es una idea distinta y que Jansen no explora.

### 8.10 Generación directa de señales y predicción directa de decisiones

- `[JANSEN]` El único enfoque que aprende decisiones directamente es el **reinforcement learning**: no se detiene en predicciones, toma una perspectiva end-to-end de la toma de decisiones orientada a objetivos, incluyendo acciones y sus consecuencias. Y es "considerado a menudo el enfoque más prometedor porque modela con más precisión la tarea que enfrenta un inversor".
- **Problemas**: `[JANSEN]` construir un entorno realista es un desafío considerable; el ruido financiero dificulta aprender una función de valor basada en recompensas diferidas; un solo activo aumenta enormemente el riesgo de overfitting; su ejemplo necesitó el equivalente a ~2.000 años de datos.
- `[IMPLICACIÓN PARA IRIS]` Jansen presenta el RL como la formulación conceptualmente correcta y prácticamente más peligrosa para nuestro caso exacto.

### 8.11 Criterios que deberemos analizar para decidir la formulación

Sin elegir todavía, estos son los criterios que Jansen nos permite establecer:

1. **¿Qué información del outcome se pierde con cada formulación, y esa pérdida es un coste o una protección contra el ruido?** Binarizar pierde magnitud, pero también puede reducir la sensibilidad al ruido de cola.
2. **¿La métrica de evaluación de la formulación está alineada con lo que queremos?** Jansen entrena con RMSE y evalúa con IC: hay una desalineación explícita que él resuelve *a posteriori*.
3. **¿La formulación permite expresar "no operar"?** La regresión y la clasificación binaria no lo hacen naturalmente; requieren un umbral externo.
4. **¿La formulación permite expresar confianza?** Requiere probabilidades calibradas o un enfoque bayesiano.
5. **¿La formulación depende de sección transversal?** Ranking sí; el resto no.
6. **¿Cuánta señal hay realmente en el target elegido?** Volatilidad > dirección en predictibilidad, según la estructura del propio libro.
7. **¿La formulación se conecta con una regla operativa sin pasos arbitrarios intermedios?** Cuantos más pasos ad-hoc entre predicción y posición, más superficie para el overfitting.
8. **¿Cuál es el horizonte y por qué?** Jansen recomienda probar varios y comparar por IC.
9. **¿Es evaluable económicamente, no sólo estadísticamente?** Ver §18.

---

## 9. TARGETS Y OBJETIVOS DE APRENDIZAJE (Tarea 6)

### 9.1 Cómo construye Jansen sus targets

`[JANSEN]` El procedimiento estándar del libro:
- Se calcula el retorno del período `t` a `t+h` y se **desplaza hacia atrás h períodos**, de modo que el retorno futuro queda alineado con las features del momento en que la decisión se toma. El ejemplo textual: el retorno de 5 días de t0 a t5 se desplaza 5 días atrás para que ese valor sea el target de t0.
- Se generan **múltiples horizontes simultáneamente** (diario, semanal, bisemanal, mensual en el ejemplo de acciones; 1, 5, 21, 63 días en otros).
- **El objetivo declarado de generar múltiples horizontes es identificar el período de holding que produce la mejor precisión predictiva, medida por el IC.**
- Los retornos se winsorizan.
- Los leads y lags implicados por retornos históricos y futuros causan **pérdida de datos que aumenta con el horizonte de inversión**.

`[IMPLICACIÓN PARA IRIS]` Esto es un método directamente adoptable: no elegir el horizonte por intuición, sino **generar varios y dejar que el IC out-of-sample lo determine**. Es una de las pocas recetas concretas y defendibles que el libro ofrece para una decisión que teníamos abierta.

### 9.2 Análisis por alternativa

**Forward returns continuos**
- *Información que proporciona*: signo y magnitud.
- *Información que pierde*: la trayectoria intermedia — nada dice de si el precio primero cayó un 2% antes de subir un 1%.
- *Dificultad*: distribución con colas pesadas; el modelo dedica capacidad a predecir extremos irreducibles.
- *Problemas estadísticos*: `[JANSEN]` para horizontes > 1 período, las etiquetas se derivan de **datos solapados**, lo que crea correlación serial entre observaciones y filtración de información entre train y test.
- *Relación con decisión*: permite sizing proporcional a la magnitud esperada.

**Dirección binaria**
- *Proporciona*: signo.
- *Pierde*: magnitud completamente. Un movimiento marginal cuenta igual que uno grande.
- *Dificultad*: el desbalance cerca de cero; la mayoría de observaciones son casi-empates.
- *Problemas estadísticos*: mismo solapamiento; además, `[JANSEN]` el umbral de clasificación no está calibrado y debe optimizarse aparte.
- *Relación con decisión*: directa pero sin información de tamaño ni de riesgo.

**Clases múltiples (p.ej. quintiles de retorno)**
- *Proporciona*: orden y granularidad intermedia.
- *Pierde*: la escala continua; y las fronteras entre clases son arbitrarias.
- *Problemas*: `[INTERPRETACIÓN]` si los quintiles se definen sobre la distribución empírica *de toda la muestra*, se introduce look-ahead. Deben definirse con información disponible en el momento.
- *Relación con decisión*: natural para LONG / NO TRADE / SHORT.

**Probabilidades**
- *Proporciona*: confianza.
- *Pierde*: nada, si están calibradas.
- *Dificultad*: la calibración no es automática.
- `[VACÍO]` Jansen no desarrolla esto.

**Volatilidad futura**
- *Proporciona*: régimen de riesgo.
- *Relación con decisión*: sizing, stops, filtro de abstención.
- `[JANSEN]` Único target con tratamiento de modelado dedicado (ARCH/GARCH).

### 9.3 Lo que Jansen NO cubre sobre labeling — declaración explícita

Esto es importante dejarlo escrito con claridad, porque condiciona la siguiente etapa del proyecto.

`[VACÍO]` **Jansen no tiene una teoría del labeling.** Concretamente, no aborda:

1. **Etiquetado basado en barreras o niveles.** No hay ningún esquema donde la etiqueta dependa de si el precio alcanza primero un objetivo de beneficio o un stop. Todos sus targets son "retorno a h períodos vista", ignorando el camino.
2. **Horizontes variables o dependientes del evento.** El horizonte es siempre fijo y elegido por el investigador.
3. **Etiquetas ajustadas por volatilidad.** No escala los umbrales del target por la volatilidad del momento, pese a documentar que la volatilidad varía.
4. **Ponderación de muestras por unicidad.** Reconoce que las etiquetas solapadas son un problema (lo menciona al introducir purging y embargoing) pero no propone ponderar observaciones por su grado de solapamiento.
5. **Muestreo condicionado a eventos.** Todas las observaciones entran al dataset; no hay filtro que seleccione momentos "interesantes".
6. **La clase "no operar".** No la define, no la etiqueta, no la evalúa.
7. **Meta-etiquetado** o cualquier arquitectura de dos niveles que separe la decisión de dirección de la decisión de tamaño/confianza.

`[JANSEN]` El propio libro **remite explícitamente a López de Prado** para las técnicas de adaptación de la cross-validation al contexto financiero (purging, embargoing, CV combinatoria), reconociendo que ese trabajo cubre problemas que él no desarrolla.

`[IMPLICACIÓN PARA IRIS]` **No debemos elegir un target basándonos únicamente en Jansen.** El libro nos da: (a) la mecánica de construcción de forward returns, (b) el método de elegir horizonte por IC, (c) la advertencia sobre etiquetas solapadas. No nos da un sistema de etiquetado. Esta decisión queda formalmente abierta hasta la siguiente etapa.


---

## 10. MODELOS PREDICTIVOS SUPERVISADOS (Tarea 8, parte 1)

Para cada familia, los 12 puntos que pidió el encargo, condensados en una ficha. Recuerdo la instrucción: **no hay ranking definitivo y no se asume que el modelo más complejo sea mejor**.

### 10.1 Regresión lineal (OLS)

1. **Problema**: regresión; también inferencia.
2. **Supuestos**: `[JANSEN]` linealidad en parámetros; condiciones Gauss-Markov para que OLS sea el mejor estimador lineal insesgado; residuos sin autocorrelación ni heterocedasticidad; sin multicolinealidad.
3. **Relaciones que aprende**: lineales, o no lineales si se codifican explícitamente en las features.
4. **Ventajas**: interpretable; inferencia estadística disponible (p-valores, intervalos de confianza); rápido; pocos hiperparámetros.
5. **Limitaciones**: `[JANSEN]` los datos financieros violan típicamente los supuestos de no autocorrelación y homocedasticidad.
6. **Overfitting**: bajo, salvo con muchas features.
7. **Interpretabilidad**: máxima.
8. **Necesidad de datos**: baja.
9. **Coste computacional**: mínimo.
10. **Utilidad en series intradiarias**: `[INTERPRETACIÓN]` alta como diagnóstico y como baseline; baja como modelo final si las relaciones son no lineales.
11. **Cuándo probarlo en IRIS**: **siempre, primero.** Es el baseline obligatorio.
12. **Cuándo no**: como modelo de producción si se demuestra que hay estructura no lineal significativa.

### 10.2 Regularización: Ridge y Lasso

1. **Problema**: regresión con control de varianza.
2. **Supuestos**: los de OLS más una penalización sobre la norma de los coeficientes.
3. **Relaciones**: lineales, con encogimiento.
4. **Ventajas**: `[JANSEN]` cobertura contra overfitting; **Lasso (L1) puede producir estimaciones dispersas reduciendo pesos hasta cero** (selección de features implícita); **Ridge (L2) preserva las direcciones a lo largo de las cuales los parámetros reducen significativamente la función de coste**.
5. **Limitaciones**: requiere tuning del parámetro de penalización; sigue siendo lineal.
6. **Overfitting**: reducido por diseño.
7. **Interpretabilidad**: alta.
8-9. Datos y cómputo: bajos.
10. **Utilidad intradiaria**: alta como baseline robusto con muchas features correlacionadas.
11. **Cuándo probarlo**: inmediatamente después de OLS; especialmente si el número de features crece.
12. **Cuándo no**: si el objetivo es capturar interacciones.

### 10.3 Regresión logística

1. **Problema**: clasificación binaria (dirección).
2. **Supuestos**: relación lineal entre features y log-odds.
3. **Ventajas**: `[JANSEN]` permite inferencia estadística sobre los coeficientes con statsmodels; produce scores continuos.
4. **Limitaciones**: lineal en log-odds; scores no necesariamente calibrados.
5-9. Similares al caso lineal.
10-12. `[IMPLICACIÓN PARA IRIS]` Es el baseline natural si IRIS adopta una formulación direccional.

### 10.4 Árboles de decisión

1. **Problema**: regresión y clasificación.
2. **Supuestos**: `[JANSEN]` prácticamente ninguno sobre la forma funcional; aproxima la función con pocas restricciones tratando el proceso generador como caja negra.
3. **Relaciones**: no lineales, con interacciones capturadas por la estructura jerárquica de reglas.
4. **Ventajas**: interpretable a poca profundidad; no requiere escalado; maneja categóricas.
5. **Limitaciones**: `[JANSEN]` alta varianza; propenso a overfitting sin regularización.
6. **Overfitting**: **muy alto**. `[JANSEN]` Se controla con restricciones de profundidad y de número mínimo de muestras por hoja.
7. **Interpretabilidad**: alta si es superficial.
8. **Datos**: moderados.
9. **Cómputo**: bajo.
10-12. `[INTERPRETACIÓN]` Rara vez útil solo; su valor es ser el bloque constructivo de ensembles.

### 10.5 Random Forest

1. **Problema**: regresión y clasificación.
2. **Supuestos**: mínimos.
3. **Relaciones**: no lineales con interacciones; promediado de muchos árboles descorrelacionados.
4. **Ventajas**: `[JANSEN]` los ensembles rinden mejor que los modelos individuales; bootstrap aggregation reduce la varianza; **out-of-bag testing** proporciona una estimación de rendimiento sin conjunto de validación separado; feature importance nativa.
5. **Limitaciones**: menos interpretable; más lento que un árbol.
6. **Overfitting**: reducido frente a un árbol, pero no eliminado.
7. **Interpretabilidad**: media (importancias, partial dependence, SHAP).
8. **Datos**: moderados-altos.
9. **Cómputo**: `[JANSEN]` entrenar un RF lleva bastante más tiempo que una regresión lineal, con el número y la profundidad de árboles como principales determinantes.
10. **Utilidad intradiaria**: `[INTERPRETACIÓN]` buena si trabajamos con features tabulares; el promediado es útil en entornos ruidosos.
11. **Cuándo probarlo en IRIS**: como primer modelo no lineal, tras los baselines lineales.
12. **Cuándo no**: si los datos son secuenciales y la estructura temporal importa más que las features agregadas. **Nota importante**: el OOB testing de RF asume muestras intercambiables, lo que no se cumple en series temporales `[INTERPRETACIÓN]`.

### 10.6 AdaBoost

1. **Problema**: clasificación (y regresión).
2. **Supuestos**: mínimos.
3. **Relaciones**: no lineales por adición secuencial de aprendices débiles reponderando errores.
4. **Ventajas**: conceptualmente simple; base histórica del boosting.
5. **Limitaciones**: sensible a ruido y outliers `[INTERPRETACIÓN]`; superado por gradient boosting.
10-12. `[INTERPRETACIÓN]` Valor principalmente pedagógico; poco motivo para usarlo en IRIS sobre GBM.

### 10.7 Gradient Boosting (y XGBoost / LightGBM / CatBoost)

1. **Problema**: regresión, clasificación, ranking.
2. **Supuestos**: `[JANSEN]` muy pocos; se construye secuencialmente añadiendo árboles superficiales que usan un número muy pequeño de features para mejorar las predicciones existentes.
3. **Relaciones**: no lineales con interacciones profundas.
4. **Ventajas**: `[JANSEN]` aplicable con gran flexibilidad a un amplio rango de funciones de pérdida; muchas oportunidades de tunear el modelo al dataset y a la tarea; las implementaciones recientes aceleran mucho el entrenamiento y ofrecen información más consistente y detallada sobre importancia de features y drivers de predicciones individuales; LightGBM permite **evaluar un modelo entrenado usando un subconjunto de sus árboles**, lo que permite probar varios valores de número de iteraciones en una sola sesión de entrenamiento; LightGBM **no requiere one-hot encoding** porque ordena las categorías según el outcome.
5. **Limitaciones**: `[JANSEN]` numerosos hiperparámetros; entrenamiento costoso con datos grandes (en su ejemplo intradiario, el entrenamiento ya llevaba varias horas con sólo 250 árboles y la IC de validación seguía mejorando en la mayoría de folds, es decir, **sus resultados no eran óptimos por límite computacional**).
6. **Overfitting**: alto si no se regulariza. `[JANSEN]` Advertencia específica: activar early stopping dentro de la CV **sesga al alza** las estimaciones porque usa información del outcome que no estaría disponible realmente.
7. **Interpretabilidad**: media-alta gracias a SHAP.
8. **Datos**: moderados-altos.
9. **Cómputo**: alto pero manejable.
10. **Utilidad intradiaria**: `[JANSEN]` Es el modelo que él elige para su único ejemplo intradiario. `[INTERPRETACIÓN]` Es el estado del arte para features tabulares heterogéneas y ruidosas.
11. **Cuándo probarlo en IRIS**: como el modelo no lineal de referencia, después de haber establecido baselines lineales y con validación temporal ya resuelta.
12. **Cuándo no**: si el problema es genuinamente secuencial y la ingeniería de features no logra capturar la estructura temporal.
- **Hallazgo empírico relevante**: `[JANSEN]` en su tuning de LightGBM diario, los **árboles superficiales** produjeron el mejor IC global entre horizontes; entrenamientos más largos (4.5 años) dieron mejores resultados; y para horizontes cortos, un lookback más largo, learning rate más alto y árboles más profundos ayudaron, mientras que para horizontes largos el cuadro era menos claro. Advierte explícitamente que **estos resultados aplican sólo a ese ejemplo**.

### 10.8 Modelos bayesianos

1. **Problema**: inferencia con incertidumbre; regresión rolling; volatilidad estocástica.
2. **Supuestos**: se especifica un modelo generativo y priors.
3. **Ventajas**: `[JANSEN]` distribuciones posteriores completas sobre parámetros y modelos; permite comparar el rendimiento de estrategias con un **Sharpe ratio bayesiano** que expresa incertidumbre.
4. **Limitaciones**: coste computacional del muestreo; requiere especificación cuidadosa.
5-9. Interpretabilidad alta; cómputo alto.
10-12. `[IMPLICACIÓN PARA IRIS]` Muy pertinente para la pregunta de "nivel de confianza" y para no sobreinterpretar diferencias entre variantes de estrategia. No es un candidato como modelo predictivo principal en la primera etapa.

### 10.9 Baselines obligatorios que Jansen justifica

`[INTERPRETACIÓN a partir de JANSEN]` El libro no da una lista explícita de baselines, pero su propia estructura y sus advertencias la implican:

| Baseline | Por qué es necesario según Jansen |
|---|---|
| **Predicción trivial** (retorno futuro = 0, o = media histórica) | Sin esto no sabemos si el modelo hace algo. El *no free lunch* implica que un modelo complejo puede ser peor que nada. |
| **Buy & hold / posición constante** | Jansen compara todas sus estrategias contra un benchmark (S&P 500) y reporta alpha y beta respecto a él. |
| **AR(p) / regresión sobre lags de retorno** | Es el modelo canónico de serie temporal; los lags de retorno recientes resultaron ser las variables más informativas en su ejemplo intradiario. |
| **Regresión lineal / logística regularizada sobre features** | Permite inferencia; establece cuánta de la señal es lineal. |
| **Un modelo de volatilidad (GARCH)** | Establece cuánta estructura hay en el segundo momento frente al primero. |
| **Random / señal aleatoria con mismo turnover** | `[CONOCIMIENTO EXTERNO AL LIBRO]` — Jansen no lo propone explícitamente, pero es la consecuencia lógica de su insistencia en que los costes pueden dominar. |

`[JANSEN]` La justificación general que sí es explícita: la curva de aprendizaje debe compararse con **un benchmark humano o de otro tipo** para juzgar si el rendimiento del modelo cumple expectativas.

---

## 11. SERIES TEMPORALES (Tarea 9)

### 11.1 Conceptos fundamentales

`[JANSEN]`
- Una serie temporal es una secuencia de valores separados por intervalos discretos, típicamente equiespaciados, modelable como proceso estocástico.
- **Lag**: el número de períodos entre dos puntos. Hay T−1 lags distintos en una serie de longitud T. Así como en modelos cross-sectional importan las relaciones entre variables distintas en un instante, en series temporales **importan las relaciones entre puntos separados por un lag dado**.
- En contexto de serie temporal, algunos o todos los valores rezagados del propio outcome juegan el papel de las variables input.
- **Ruido blanco**: secuencia IID con media y varianza finitas; gaussiano si es normal con media cero y varianza constante.
- Una serie es **lineal** si puede escribirse como suma ponderada de perturbaciones pasadas (innovaciones) más la media. El objetivo del análisis es entender el comportamiento dinámico gobernado por esos coeficientes.

### 11.2 Descomposición

`[JANSEN]` Una serie combina componentes sistemáticos (tendencia, estacionalidad, ciclos) con ruido no sistemático. Pueden modelarse de forma aditiva (cuando las fluctuaciones no dependen del nivel) o multiplicativa. Statsmodels descompone en tendencia, estacionalidad y residuo usando medias móviles. **El componente residual sería el foco del modelado posterior**, asumiendo que tendencia y estacionalidad son más deterministas y extrapolables.

`[IMPLICACIÓN PARA IRIS]` Aplicado a MNQ intradiario, esto sugiere una línea de investigación concreta: separar el patrón intradiario determinista (la "sonrisa" de volatilidad y volumen a lo largo de la sesión) del residuo, y modelar sobre el residuo. Sin esta separación, un modelo puede parecer que "predice" cuando en realidad sólo ha memorizado la hora del día.

### 11.3 Estadísticos de ventana móvil

`[JANSEN]` Producen una nueva serie donde cada punto resume un período de la original. **El objetivo es detectar si la serie es estable o cambia con el tiempo, y obtener una representación suavizada que capture aspectos sistemáticos filtrando el ruido.** Los pesos pueden ser iguales o enfatizar datos recientes; las medias móviles exponenciales calculan recursivamente pesos que decaen. Pandas soporta ventanas rolling y expanding con distintas distribuciones de peso, y funciones tanto integradas como definidas por el usuario.

`[JANSEN]` Los modelos de forecast tempranos eran medias móviles con pesos exponenciales (exponential smoothing), populares para series sin patrones muy complicados o abruptos.

### 11.4 ACF y PACF

`[JANSEN]`
- **ACF**: coeficientes de correlación en función del lag.
- **PACF**: elimina la influencia indirecta de los puntos intermedios; se obtiene usando los residuos de una regresión lineal de la serie sobre sus valores rezagados.
- **Correlograma**: gráfico de ACF o PACF para lags sucesivos. Su uso principal es **detectar autocorrelación remanente tras eliminar tendencia determinista o estacionalidad**.
- Ambos son herramientas de diagnóstico clave para el diseño de modelos lineales de serie temporal.

### 11.5 Estacionariedad y raíces unitarias

Ya cubierto en §3.3. Añado aquí lo operativo:

`[JANSEN]` **Transformaciones para lograr estacionariedad**, a menudo en varios pasos: log; deflación; ajuste de tendencia por regresión con el índice temporal como variable independiente, usando los residuos; y diferenciación (período a período y/o estacional). Aplicada a una serie log-transformada, la diferenciación produce tasas de crecimiento instantáneas, es decir, retornos.

`[JANSEN]` Si una serie se vuelve estacionaria tras diferenciar d veces, es **integrada de orden d**. Las raíces unitarias son la causa.

`[JANSEN]` **Test ADF**: hipótesis nula de raíz unitaria contra alternativa de estacionariedad. Regresa la serie diferenciada sobre una tendencia temporal, el primer lag y todas las diferencias rezagadas, y computa el estadístico a partir del coeficiente del valor rezagado.

### 11.6 Modelos univariantes: AR, MA, ARIMA

`[JANSEN]`
- **AR**: el valor actual es una suma ponderada de valores pasados más una perturbación aleatoria.
- **MA**: construido sobre las innovaciones.
- **ARIMA**: combina ambos con diferenciación, y admite extensiones.
- Se usan en el libro para forecast de fundamentales macro.

`[INTERPRETACIÓN]` Jansen dedica poco espacio a los ARIMA para predecir retornos de activos, y cuando los aplica es a macro. La lectura implícita es que no espera que un ARIMA prediga retornos de mercado — coherente con el random walk.

### 11.7 Modelos de volatilidad: ARCH/GARCH

`[JANSEN]` Se usan para forecast de volatilidad, abandonando explícitamente el supuesto de varianza constante y asumiendo que la varianza cambia de forma predecible.

`[IMPLICACIÓN PARA IRIS]` De todo el capítulo 9, este es el bloque con mayor probabilidad de aportar valor directo a IRIS: un modelo de volatilidad condicional puede alimentar sizing, stops y filtros de abstención, independientemente de qué modelo prediga la dirección.

### 11.8 Modelos multivariantes: VAR y cointegración

`[JANSEN]`
- **VAR**: sistemas de ecuaciones donde cada variable se regresa sobre lags de todas.
- **Cointegración**: series con tendencia compartida; tests de Engle-Granger (dos pasos) y Johansen (ratio de verosimilitud); base del pairs trading.

`[IMPLICACIÓN PARA IRIS]` No aplicables a un instrumento único. Serían relevantes sólo si IRIS incorporase series adicionales (otros índices, VIX, tipos, divisas), lo cual **no está en el alcance actual pero tampoco descartado**.

### 11.9 Qué llevarse del capítulo 9 para MNQ intradiario

`[IMPLICACIÓN PARA IRIS]` El valor de este capítulo no es el conjunto de modelos, es el **kit de diagnóstico**. Antes de modelar, estas herramientas nos dicen qué tipo de objeto tenemos entre manos:

1. Descomposición → ¿cuánto del movimiento intradiario es patrón determinista de sesión?
2. ACF/PACF sobre retornos → ¿hay dependencia lineal directa a algún lag? ¿A qué escala?
3. ACF sobre retornos absolutos o al cuadrado → ¿hay clustering de volatilidad, y a qué escala persiste?
4. ADF sobre precio, log-precio, retornos → ¿qué transformación es estacionaria?
5. Rolling mean/std de retornos → ¿cambian las propiedades entre períodos? ¿hay regímenes visibles?
6. GARCH → ¿cuánta estructura hay en la varianza condicional?

`[INTERPRETACIÓN]` Si el resultado de (2) es que no hay autocorrelación lineal significativa en los retornos pero sí una fuerte en la volatilidad (que es el resultado típico en mercados líquidos), eso ya es una conclusión metodológica importante: sugiere que la señal explotable, si existe, es **no lineal**, **condicional al régimen**, o **está en el segundo momento**, no en una relación lineal simple sobre el primero.

---

## 12. MACHINE LEARNING NO SUPERVISADO (Tarea 8, parte 2)

`[JANSEN]` El aprendizaje no supervisado aporta valor descubriendo estructuras en los datos sin necesidad de una variable outcome que guíe la búsqueda. En lugar de predecir resultados futuros, **aprende una representación informativa de los datos** que ayuda a explorar, obtener insights o resolver otra tarea con más eficacia.

### 12.1 Reducción de dimensionalidad

`[JANSEN]`
- **Maldición de la dimensionalidad**: motivación central.
- **Lineal**: PCA (componentes principales), ICA (componentes independientes). En trading, se usan para extraer factores de riesgo data-driven y construir eigenportfolios.
- **No lineal (manifold learning)**: para estructuras que la proyección lineal no captura.

`[IMPLICACIÓN PARA IRIS]` Usos potenciales *no explorados por Jansen* pero conceptualmente coherentes:
- PCA sobre nuestra matriz de features para diagnosticar redundancia (¿cuántas dimensiones efectivas tienen 40 indicadores técnicos?).
- Reducción de un espacio de features grande antes de un modelo, para controlar varianza.
- `[INTERPRETACIÓN]` Ambos usos son defendibles; el uso de PCA como *extracción de factores de riesgo* no lo es en un instrumento único.

### 12.2 Clustering

`[JANSEN]` k-means; clustering jerárquico; clustering basado en densidad (DBSCAN); mixturas gaussianas. Aplicación en el libro: agrupar activos para asignación de cartera (hierarchical risk parity), y ordenar indicadores en la rejilla 2D de CNN-TA.

`[IMPLICACIÓN PARA IRIS]` La aplicación potencialmente valiosa para nosotros es una que **Jansen no realiza**: agrupar *momentos temporales* (no activos) por sus características de mercado para descubrir **regímenes**. Esto conecta directamente con dos preguntas del objetivo de IRIS: "¿qué condiciones del mercado explican la señal?" y "¿existen condiciones en las que el modelo debería abstenerse?".

`[INTERPRETACIÓN]` Es una línea de investigación legítima, pero hay que advertir un riesgo: clusterizar sobre toda la historia y luego usar la etiqueta de cluster como feature **introduce look-ahead**, porque la definición del cluster usó información futura. Cualquier régimen debe asignarse de forma causal.

### 12.3 Autoencoders

`[JANSEN]` Aprenden representaciones no lineales sofisticadas capaces de comprimir datos complejos con poca pérdida de información; útiles contra la maldición de la dimensionalidad. Variantes: dispersos, profundos, convolucionales, **denoising** (para corregir datos corrompidos), seq2seq (para features de series temporales), variacionales (generativos).

`[IMPLICACIÓN PARA IRIS]` El **denoising autoencoder** y el **seq2seq autoencoder** son los dos que tienen sentido conceptual para nosotros. Ambos son líneas de exploración avanzadas, no de primera etapa.

### 12.4 GANs

`[JANSEN]` Dos redes en competencia: generador y discriminador. Motivación en finanzas: crear datos sintéticos para entrenar modelos o hacer backtests, dada la escasez de historia y el problema perenne del overfitting. TimeGAN como ejemplo específico para series temporales.

`[JANSEN]` **Límites declarados**: el ejemplo generó precios diarios de un número pequeño de activos; en la práctica interesarían retornos de muchos más activos y posiblemente a mayor frecuencia; la dinámica cross-sectional y temporal se volverá más compleja y podría requerir ajustes de arquitectura y entrenamiento. Es un campo en fases muy tempranas.

`[IMPLICACIÓN PARA IRIS]` Relevante a medio plazo para stress-testing y para el pitfall del período muestral. No para la primera etapa.

---

## 13. DEEP LEARNING Y MODELOS SECUENCIALES (Tarea 11)

### 13.1 Qué presenta Jansen

**Redes feedforward.** `[JANSEN]`
- El DL es una forma de **representation learning** que extrae features jerárquicas de datos no estructurados de alta dimensión.
- Decisiones de diseño: número de capas y nodos, conexiones entre capas, funciones de activación. La forma funcional de las activaciones puede **facilitar o entorpecer el flujo de información del gradiente**; funciones con regiones planas para rangos amplios de input tienen gradiente muy bajo y pueden bloquear el progreso del entrenamiento.
- ReLU frente a sigmoide/tanh: ReLU tiene derivada constante mientras la unidad está activa y mejoró mucho el rendimiento de las redes feedforward; tanh suele rendir mejor que la sigmoide porque se parece más a la identidad para valores pequeños, haciendo que la red se comporte más como un modelo lineal, lo que facilita el entrenamiento. Ambas sufren saturación.
- Salidas y costes: lineal para regresión; sigmoide para binaria; softmax para multiclase; entropía cruzada mejora significativamente la eficacia del entrenamiento frente a MSE en clasificación.
- Skip connections facilitan el flujo del gradiente; la omisión deliberada de conexiones reduce parámetros, limita capacidad y puede reducir el error de generalización además del coste computacional.

**Regularización.** `[JANSEN]`
- El reverso de la capacidad de aproximar funciones arbitrarias es un **riesgo de overfitting muy incrementado**.
- La mejor protección es entrenar con un dataset mayor; el data augmentation es una alternativa potente (y en finanzas, la generación de datos sintéticos es un área de investigación activa).
- **Hallazgo práctico común**: el modelo con menor error de generalización no es el del tamaño de parámetros exactamente correcto, sino **un modelo más grande bien regularizado**.
- Penalizaciones L1 (dispersión) y L2 (preservación de direcciones que reducen el coste); normalmente sólo sobre pesos, no sobre sesgos; variar penalizaciones por capa hace el tuning prohibitivo.
- **Early stopping**: el método más común, efectivo y simple. **Con la advertencia explícita de look-ahead bias**: los resultados del backtest serán excesivamente positivos si el early stopping usa datos fuera de muestra que no estarían disponibles en la implementación real.
- **Dropout**: omisión aleatoria de unidades; computacionalmente barato; no restringe la elección de modelo ni de procedimiento de entrenamiento; requiere más iteraciones pero cada una es más rápida; reduce el overfitting **impidiendo que unas unidades compensen los errores de otras**.

**Optimización.** `[JANSEN]` Desafíos: mínimos locales; regiones planas de gradiente bajo que no son mínimos; regiones de gradiente muy alto; y arquitecturas profundas o dependencias de largo plazo en RNN que requieren multiplicar muchos términos. Soluciones: SGD, momentum, Nesterov, tasas de aprendizaje adaptativas. **No hay un algoritmo mejor**, aunque las tasas adaptativas han mostrado cierta promesa.

**CNN.** `[JANSEN]` Aplicables a series temporales porque tienen estructura de rejilla. **Condición clave**: la aplicación dará fruto sólo si los datos cumplen el supuesto del modelo de que **los patrones o relaciones locales ayudan a predecir el resultado**. En series temporales, esos patrones locales podrían ser autocorrelación o relaciones no lineales similares a intervalos relevantes. Como la localidad importa, **la organización de los datos es esencial**, en contraste con las feedforward donde permutar los elementos de cualquier dimensión no afecta al aprendizaje.

**RNN/LSTM/GRU.** `[JANSEN]` Las feedforward tratan cada vector de features como IID y **no tienen memoria**; las CNN sólo permiten compartición superficial de parámetros. La innovación de las RNN es que **cada salida es función tanto de la salida previa como de información nueva**, lo que permite compartir parámetros a lo largo de un grafo computacional mucho más profundo. Desafío central: aprender dependencias de largo alcance. LSTM y GRU son las respuestas.

### 13.2 Los resultados empíricos de Jansen con DL — leídos críticamente

Este es el material más importante para responder a la pregunta del encargo.

| Experimento | Resultado reportado | Lectura crítica `[INTERPRETACIÓN]` |
|---|---|---|
| **NN feedforward, retornos diarios, 995 acciones (cap. 17)** | IC mediano de las 5 mejores configuraciones: 0.0236–0.0246. Regresión OLS del IC sobre dummies de arquitectura: **R² prácticamente cero**. Batch 256 y dropout 0.2 con contribuciones significativas pero pequeñas. | El propio autor concluye que el ruido de los datos domina sobre la señal que aportan las decisiones de arquitectura. Es decir: **el tuning arquitectónico no fue el factor determinante**. Un resultado profundamente relevante. |
| **Estrategia basada en ensemble de las 3 mejores NN** | 22.8% anualizado en 36 meses; 16.5% in-sample, 35.7% out-of-sample; Sharpe 0.72 in-sample, 2.15 out-of-sample; **antes de costes**. | El Sharpe out-of-sample triplica al in-sample sobre una ventana de sólo 12 meses. Esto es estadísticamente inverosímil como estimación estable; lo más plausible es varianza muestral de una ventana corta. **No debe leerse como evidencia de que las NN funcionan.** |
| **CNN 1D autorregresiva (cap. 18)** | Sólo el lag 5 resultó no significativo entre los 12 retornos mensuales rezagados. | La señal detectada es esencialmente autorregresiva; no está claro que la CNN aporte sobre un AR. |
| **CNN-TA, rejilla 15×15 (cap. 18)** | ~4 pb/día de spread entre quintiles; 35.6% de retorno acumulado; Sharpe 0.53 antes de costes. **Y**: el resultado no era robusto, modificaciones ligeras degradaban significativamente el rendimiento, y con bajo ratio señal/ruido la red podía caer en un óptimo local **prediciendo siempre un valor constante**. | Esta es la confesión metodológica más útil del libro sobre DL. Un resultado que se rompe con cambios pequeños **no es un resultado**. |
| **Stacked LSTM, retornos semanales (cap. 19)** | AUC de test 0.6816, accuracy 0.6193, con ~2.400 acciones y 52 semanas de historia por muestra. | Sobre 1.16 millones de observaciones cross-sectional. La traducción a una serie única con muchísimos menos ejemplos independientes es incierta. |
| **Agente DQN, un solo activo (cap. 22)** | Rendimiento similar al del mercado tras entrenar con el equivalente a ~2.000 años de datos. | Jansen advierte él mismo que un solo activo **aumenta enormemente** el riesgo de overfitting. |

### 13.3 Respuesta a la pregunta: ¿qué debería ocurrir para que usar Deep Learning en IRIS esté científicamente justificado?

Derivo esto directamente de los principios de Jansen, marcando la fuente de cada criterio.

**Condiciones previas — sin ellas, el DL no está justificado bajo ningún resultado:**

1. `[JANSEN]` **Debe existir un baseline simple, correctamente validado, con un resultado conocido.** El *no free lunch* implica que la complejidad no es una virtud; un modelo complejo aprenderá ruido si la relación verdadera es simple.
2. `[JANSEN]` **La validación temporal debe estar resuelta antes**, sin leakage, sin early stopping que use datos futuros, con hold-out intacto.
3. `[JANSEN]` **Debe haber suficientes datos.** El rendimiento predictivo de las redes profundas mejora con más datos; esa es su ventaja característica. Sin volumen, se pierde la razón de usarlas.
4. `[JANSEN]` **Debe haber una razón estructural**: si es CNN, que existan patrones locales y que la organización de los datos importe; si es RNN, que existan dependencias temporales que las features agregadas no capturen. Usar una arquitectura secuencial sobre features tabulares donde el orden ya se codificó explícitamente no tiene justificación conceptual.

**Evidencia que debería demostrar que el modelo complejo supera realmente al baseline:**

5. `[INTERPRETACIÓN de JANSEN]` **Superioridad fuera de muestra en la métrica que nos importa (IC o rendimiento económico), no en la función de pérdida de entrenamiento**, y de magnitud materialmente superior al baseline — no una mejora en el tercer decimal.
6. `[JANSEN — derivado de su experimento del cap. 17]` **La mejora debe ser atribuible al modelo y no al ruido.** Su propio test es replicable: regresar la métrica de rendimiento sobre las opciones de diseño y comprobar si explican algo. Si el R² es ~0, las diferencias entre configuraciones son ruido y "el mejor modelo" es un artefacto de selección.
7. `[JANSEN — derivado del cap. 18]` **Robustez a perturbaciones del diseño.** Si modificaciones ligeras de arquitectura, semilla o hiperparámetros degradan significativamente el rendimiento, el resultado no es fiable.
8. `[JANSEN]` **Consistencia a lo largo de múltiples splits temporales**, no un buen resultado en una ventana.
9. `[JANSEN]` **Corrección por número de pruebas.** El DL multiplica el espacio de configuraciones; la longitud mínima de backtest y el deflated Sharpe ratio se vuelven más exigentes, no menos.
10. `[JANSEN]` **Superioridad que sobreviva a costes de transacción.** Ninguno de los resultados de DL del libro está reportado neto de costes.
11. `[JANSEN]` **Interpretabilidad suficiente** para verificar que la lógica del modelo es coherente con alguna teoría del comportamiento del mercado, no arbitraria.

`[INTERPRETACIÓN]` Mi lectura del conjunto: **Jansen presenta el Deep Learning con entusiasmo técnico y resultados empíricos débiles o frágiles.** No hay en el libro ni un solo caso donde una arquitectura profunda demuestre convincentemente superar a un gradient boosting bien tuneado sobre las mismas features. La conclusión defendible desde esta fuente no es "el DL no sirve", sino: **el libro no aporta evidencia que justifique empezar por ahí.**

---

## 14. REINFORCEMENT LEARNING (Tarea 8, parte 3)

`[JANSEN]`
- **Elementos**: política (traduce estados en acciones), recompensas (aprender de las acciones), función de valor (elección óptima a largo plazo), y la distinción entre métodos con y sin modelo del entorno.
- **Formulación**: proceso de decisión de Markov finito; solución por programación dinámica (iteración de política, iteración de valor, iteración generalizada de política).
- **Q-learning**: encuentra una política óptima sobre la marcha; política ε-greedy para equilibrar exploración y explotación.
- **Deep RL**: aproximación de la función de valor con redes; DQN y extensiones (DDQN); OpenAI Gym; entorno de trading personalizado.
- **Diferencia con el aprendizaje supervisado**: optimiza el comportamiento del agente experiencia a experiencia mediante una señal de recompensa escalar, en lugar de generalizar a partir de muestras etiquetadas. **No se detiene en la predicción**: adopta una perspectiva end-to-end de la toma de decisiones incluyendo acciones y consecuencias.
- **Definir la función de recompensa correcta es el problema central**: el RL trata precisamente de eso.

**Advertencias (repetidas aquí por su importancia para IRIS):** `[JANSEN]` entorno realista difícil de construir; ruido financiero que dificulta aprender valor con recompensas diferidas; un solo activo incrementa enormemente el overfitting; ~2.000 años de datos de entrenamiento para igualar al mercado.

**Utilidad potencial:** `[IMPLICACIÓN PARA IRIS]` El RL es la única formulación del libro que **integra nativamente la decisión de no operar** (es una acción más) y el **sizing** (si el espacio de acciones lo incluye). Eso lo hace conceptualmente muy alineado con los objetivos declarados de IRIS. Pero las advertencias de Jansen apuntan exactamente a nuestra configuración como la más peligrosa. **Queda como línea a considerar mucho más adelante, no como punto de partida.**

---

## 15. VALIDACIÓN TEMPORAL (Tarea 7, parte 1)

### 15.1 El problema fundamental

`[JANSEN]` **Un supuesto clave de la cross-validation es que las muestras son IID. Para datos financieros esto habitualmente no se cumple**, por correlación serial y heterocedasticidad.

`[JANSEN]` La naturaleza temporal implica que la CV estándar produce una situación donde **datos del futuro se usan para predecir datos del pasado**. Esto es, en el mejor de los casos, irrealista; y en el peor, data snooping, en la medida en que los datos futuros reflejan eventos pasados.

### 15.2 El esquema correcto según Jansen

**Split en tres partes.** `[JANSEN]` Una parte se usa en cross-validation y se divide repetidamente en train y validation. El resto se aparta como **hold-out que se usa una única vez, después de completar la cross-validation**, para generar una estimación insesgada del error de test.

**Por qué el hold-out es imprescindible.** `[JANSEN]` La selección de modelo implica tuning de hiperparámetros, que puede suponer muchas iteraciones de CV. El score de validación del modelo con mejor rendimiento **está sujeto a sesgo de pruebas múltiples**, que refleja el ruido muestral inherente al proceso de CV. Como resultado, **ya no es una buena estimación del error de generalización**. Para obtener una estimación insesgada hay que calcularla sobre un dataset fresco.

**TimeSeriesSplit.** `[JANSEN]` Implementa un test walk-forward con conjunto de entrenamiento **expansivo**: cada conjunto de entrenamiento es un superconjunto de los anteriores. El parámetro `max_train_size` permite mantener el tamaño del train constante (ventana deslizante), de forma similar a cómo Zipline testea un algoritmo.

**MultipleTimeSeriesCV.** `[JANSEN]` CV personalizada desarrollada en el libro que permite: entrenar sobre una muestra consecutiva de `train_length` días; validar en un período posterior de `test_length` días; y repetir un número dado de splits desplazando ambas ventanas hacia adelante, **evitando look-ahead bias**. Se adapta a frecuencia de minuto referenciando el nivel de fecha-hora del índice y calculando longitudes en base a observaciones por día.

### 15.3 Purging, embargoing y CV combinatoria

`[JANSEN]` Introduce estos conceptos y **los atribuye explícitamente a Marcos López de Prado**:

- **El problema**: en datos financieros, las etiquetas se derivan a menudo de **puntos de datos solapados**, porque los retornos se calculan a partir de precios de múltiples períodos. Y en el contexto de una estrategia, el resultado de una predicción del modelo —que puede implicar tomar una posición— sólo se conoce más tarde, cuando esa decisión se evalúa, por ejemplo al cerrar la posición.
- **El riesgo**: filtración de información del test al train, lo que **muy probablemente inflaría artificialmente el rendimiento**.
- **Purging**: eliminar puntos de entrenamiento cuya evaluación ocurre después del inicio del período de test.
- **Embargoing**: eliminar además muestras de entrenamiento que siguen al período de test.
- **CV combinatoria**: responde a que la CV walk-forward limita severamente los caminos históricos disponibles.

`[JANSEN]` Complementa con la exigencia de **point-in-time**: todos los datos deben haber estado verdaderamente disponibles y ser conocidos en el momento en que se usan como input.

`[IMPLICACIÓN PARA IRIS]` Jansen nos advierte del problema y nos nombra las soluciones, pero **no las desarrolla ni las implementa**. Esta es una de las razones estructurales por las que López de Prado es la siguiente fuente obligatoria.

### 15.4 Sesgos que Jansen cataloga

**Look-ahead bias.** `[JANSEN]` Surge cuando desarrollamos o evaluamos reglas usando información histórica antes de que fuera conocida o estuviera disponible. Causas típicas: no tener en cuenta correcciones o reexpresiones posteriores a la publicación inicial; splits; desincronización entre datos de distinta frecuencia. **Solución**: validación cuidadosa de los timestamps de todos los datos que entran al backtest; y cuando no hay datos point-in-time, hacer supuestos conservadores sobre el retardo.

**Survivorship bias.** `[JANSEN]` Ocurre cuando los datos contienen sólo valores actualmente activos y omiten los que desaparecieron. Como los desaparecidos suelen haber rendido mal, el resultado se sesga positivamente. **Solución**: verificar que el dataset incluye todos los valores disponibles en cada momento — otra forma de asegurar que los datos son point-in-time.

**Control de outliers.** `[JANSEN]` El desafío es identificar outliers que verdaderamente no son representativos del período, frente a valores extremos que son parte integral del entorno de mercado. **Solución**: análisis cuidadoso de la probabilidad de ocurrencia de valores extremos, y ajuste de los parámetros de la estrategia a esa realidad.

**Período muestral.** `[JANSEN]` Un backtest no generaliza si la muestra no refleja el entorno actual y probable futuro: puede carecer de aspectos de régimen de mercado (volatilidad, volúmenes), tener pocos datos, o contener demasiados o demasiado pocos eventos extremos. **Solución**: usar períodos que incluyan fenómenos de mercado importantes, o generar datos sintéticos que reflejen las características relevantes.

**Multiple testing / selection bias.** `[JANSEN]` Es "el desafío más prominente" para la validez de un backtest, incluidos los resultados publicados. Seleccionar una estrategia basándose en pruebas de distintos candidatos sobre los mismos datos **sesga la elección**, porque un resultado positivo es más probablemente causado por la naturaleza estocástica de la propia medida de rendimiento. La estrategia sobreajusta la muestra de test, produciendo resultados engañosamente positivos que difícilmente generalizarán.
- **El rendimiento de un backtest sólo es informativo si se reporta el número de pruebas realizadas**, para permitir evaluar el riesgo de sesgo de selección. Jansen señala que esto rara vez ocurre en investigación práctica o académica, lo que invita a dudar de la validez de muchas afirmaciones publicadas.
- El riesgo **no surge sólo de correr muchos tests**: también afecta a estrategias diseñadas con conocimiento previo de qué funciona y qué no. Y como ese riesgo incluye el conocimiento de backtests realizados por *otros* sobre los *mismos* datos, **el backtest overfitting es muy difícil de evitar en la práctica**.

**Data snooping.** `[JANSEN]` Aparece en dos sentidos: (a) usar información futura para predecir el pasado en la CV; (b) el data mining generalizado que produce significación estadística por ensayo y error a gran escala.

### 15.5 Herramientas cuantitativas contra el multiple testing

`[JANSEN]`
1. **Longitud mínima de backtest**: estimación de cuánto período de backtest debería exigir un inversor para evitar seleccionar una estrategia que alcanza cierto Sharpe con un número dado de pruebas in-sample pero cuyo Sharpe esperado out-of-sample es cero. El resultado que reporta: **2 años de datos diarios no sostienen conclusiones sobre más de ~7 estrategias; 5 años, sobre ~45 variaciones.**
2. **Deflated Sharpe Ratio**: calcula la probabilidad de que el SR sea estadísticamente significativo **controlando el efecto inflacionario del multiple testing, los retornos no normales y las muestras cortas**.
3. **Parada óptima**: del problema de la secretaria. Regla traducida al backtesting: probar una muestra aleatoria de aproximadamente el 37% (1/e) de las estrategias razonables y registrar su rendimiento; luego continuar hasta que una estrategia supere a todas las probadas antes. Esto da una probabilidad de 1/e de seleccionar la mejor, independientemente del tamaño del conjunto.
4. **Simulador de backtest-overfitting** online (referenciado por Jansen).

`[IMPLICACIÓN PARA IRIS]` La primera cifra es la que más nos afecta. Si vamos a probar decenas o cientos de combinaciones de features, targets, horizontes y modelos sobre MNQ, **necesitamos saber cuánto histórico intradiario tenemos en términos de eventos efectivamente independientes**, no en número de barras. Un millón de barras de un minuto no son un millón de observaciones independientes.

### 15.6 Curvas de diagnóstico

`[JANSEN]`
- **Curva de validación**: visualiza el impacto de un único hiperparámetro sobre el rendimiento de CV; sirve para determinar si el modelo sub- o sobreajusta. El overfitting se identifica cuando los errores de train y validación **divergen** y el rendimiento medio fuera de muestra se deteriora rápidamente.
- **Curva de aprendizaje**: muestra cómo dependen los errores de train y validación del tamaño muestral. Permite decidir entre ajustar la complejidad del modelo u obtener más datos. Reglas que da:
  - Si train y CV convergen, **más datos probablemente no ayuden**.
  - Si el error de validación sigue bajando con el tamaño del train, **más datos pueden ayudar**.
  - Si el error de entrenamiento es alto, **más datos probablemente no ayuden**; hay que añadir features o usar un algoritmo más flexible.
  - Cuanto más cerca esté el error de entrenamiento del rendimiento humano o de otro benchmark, **más probable es que el modelo sobreajuste**.
  - La variabilidad alrededor del error de CV es evidencia de **varianza**; la variabilidad en el conjunto de entrenamiento sugiere **sesgo**.

`[JANSEN]` **Optimization verification test** (atribuido a Andrew Ng): distinguir si un fallo de rendimiento se debe al algoritmo de aprendizaje o al de optimización. Si el algoritmo de aprendizaje puntúa más alto la solución correcta que la encontrada por la búsqueda, el problema está en la búsqueda; si no, el algoritmo está optimizando el objetivo equivocado.

---

## 16. OVERFITTING: "CÓMO PODEMOS ENGAÑARNOS ACCIDENTALMENTE DESARROLLANDO IRIS" (Tarea 7, parte 2)

Esta sección responde a una pregunta específica: ¿cómo podríamos obtener **resultados históricos excelentes que sean completamente falsos**?

Cada escenario es conceptual y está construido a partir de las advertencias de Jansen, aplicadas a nuestro caso concreto.

---

### Escenario 1 — El futuro se filtra por el indicador

**Qué haríamos:** calcularíamos una media móvil, un z-score o una normalización de features usando toda la serie histórica de golpe (por ejemplo, `df.rolling(20).mean()` está bien, pero `(x - x.mean()) / x.std()` sobre el dataset completo no lo está). O aplicaríamos un filtro de Kalman en modo *smoothing*, o una reconstrucción wavelet sobre la serie entera.

**Por qué engaña:** cada observación de entrenamiento contiene una traza de la media y la varianza de todo el período, incluido el futuro. El modelo aprende algo real... sobre datos que no existían.

**Cómo se ve:** IC sorprendentemente alto y estable. Curvas de equity suaves.

**Prevención:** `[JANSEN]` Validación cuidadosa de que todo dato es point-in-time. Toda transformación debe ser causal y verificable barra a barra. Regla práctica: si una feature en la barra *t* cambia de valor cuando añadimos datos posteriores a *t*, hay leakage.

---

### Escenario 2 — El target solapado contamina la validación

**Qué haríamos:** predecir el retorno a 30 minutos vista con barras de 1 minuto. Cada etiqueta consume 30 barras. Si el corte train/test cae en medio, hasta 30 observaciones de entrenamiento contienen información que ocurre dentro del período de test.

**Por qué engaña:** `[JANSEN]` Las etiquetas derivadas de puntos solapados filtran información del test al train, lo que muy probablemente infla artificialmente el rendimiento. Además, observaciones consecutivas están fuertemente correlacionadas, por lo que el número efectivo de observaciones independientes es mucho menor que el número de filas.

**Cómo se ve:** rendimiento de validación consistentemente bueno que se desploma en un hold-out realmente separado.

**Prevención:** `[JANSEN]` Purging y embargoing. Y no confundir número de filas con tamaño muestral efectivo.

---

### Escenario 3 — Probamos cien cosas y reportamos una

**Qué haríamos:** evaluar 5 timeframes × 6 horizontes × 4 targets × 8 modelos × 10 configuraciones de features. Uno de esos ~10.000 caminos dará un Sharpe excelente.

**Por qué engaña:** `[JANSEN]` Con suficientes pruebas sobre los mismos datos, un resultado positivo es más probablemente causado por la naturaleza estocástica de la propia medida que por señal real. **Y 5 años de datos no sostienen conclusiones sobre más de ~45 variaciones de estrategia.**

**Cómo se ve:** una estrategia impecable rodeada de 9.999 fracasos que no se mencionan.

**Prevención:** `[JANSEN]` (a) Priorizar hipótesis con justificación económica antes de testear; (b) **llevar un registro del número de pruebas realizadas** desde el primer día; (c) aplicar el deflated Sharpe ratio; (d) usar la regla de parada de 1/e; (e) mantener un hold-out que se toca una sola vez.

---

### Escenario 4 — El hold-out deja de ser hold-out

**Qué haríamos:** mirar el resultado del test, no gustarnos, cambiar algo, volver a mirar. Tres veces. O diez.

**Por qué engaña:** `[JANSEN]` El hold-out debe usarse **una única vez, después de completar la CV**. En cuanto se usa para decidir, se convierte en conjunto de validación y su estimación deja de ser insesgada.

**Cómo se ve:** convergencia sospechosa entre validación y test.

**Prevención:** definir por escrito el protocolo antes de mirar; registrar cada acceso al hold-out; si se agota, reservar un período nuevo y esperar.

---

### Escenario 5 — Early stopping que mira al futuro

**Qué haríamos:** entrenar una red o un GBM con early stopping sobre el conjunto de validación, y luego reportar el rendimiento de ese mismo conjunto.

**Por qué engaña:** `[JANSEN]` Lo advierte dos veces, para redes y para LightGBM: **el backtest saldrá excesivamente positivo** porque el criterio de parada usa información del outcome que no estaría disponible en la implementación real; las estimaciones de rendimiento de CV estarán sesgadas al alza.

**Prevención:** el conjunto usado para parar el entrenamiento nunca puede ser el que reporta el rendimiento. En walk-forward, la parada debe decidirse con datos anteriores al período de test.

---

### Escenario 6 — El backtest es optimista sobre la ejecución

**Qué haríamos:** generar la señal con el cierre de la barra y suponer ejecución a ese mismo cierre. Ignorar spread, comisiones y slippage. Suponer que siempre hay contraparte.

**Por qué engaña:** `[JANSEN]` Las señales pueden calcularse desde precios de cierre cuando las operaciones sólo están disponibles a la apertura siguiente, posiblemente a precios bastante distintos; los mercados no permiten ejecutar todo en cualquier momento al precio objetivo; una simulación que asume operaciones no disponibles o en términos menos favorables produce resultados sesgados.

**Cómo se ve:** una estrategia con turnover altísimo y un edge de 0.5 pb por operación que parece rentable.

**Prevención:** `[JANSEN]` Orquestación cuidadosa de la secuencia llegada-de-señal → ejecución → evaluación; supuestos realistas de coste y slippage; limitación a un universo líquido. `[IMPLICACIÓN PARA IRIS]` Para MNQ intradiario esto es *el* riesgo principal: el edge medido en el ejemplo intradiario de Jansen era de 0.5 puntos básicos por minuto, y él mismo omitió el backtest realista por coste computacional.

---

### Escenario 7 — Predecimos el reloj, no el mercado

**Qué haríamos:** incluir hora del día, minuto de la sesión, día de la semana como features de un modelo intradiario.

**Por qué engaña:** `[JANSEN]` En su modelo diario, **los indicadores de período temporal dominaron la importancia de features**. En intradiario, el patrón de volatilidad y volumen a lo largo de la sesión es fuertemente determinista. Un modelo puede obtener buenas métricas de error simplemente aprendiendo ese patrón, sin ninguna capacidad de anticipar la dirección.

**Cómo se ve:** SHAP dominado por variables de calendario; señal que desaparece si se condiciona por hora.

**Prevención:** `[INTERPRETACIÓN]` Descomponer la estacionalidad intradiaria y verificar si el modelo aporta algo **por encima** del patrón determinista. Evaluar el rendimiento condicionado a cada franja horaria.

---

### Escenario 8 — Confundimos ordenar con acertar

**Qué haríamos:** medir un IC de 0.03, declarar señal, construir la estrategia.

**Por qué engaña:** `[JANSEN]` El caso de Alpha 054: IC significativo de 0.025 y spread positivo entre quintiles, **con retornos acumulados negativos** en la cartera long-short. Además, el análisis de dispersión muestra que aunque las medias difieran, la separación de las distribuciones puede ser muy limitada, de modo que en un momento dado la diferencia de rendimiento es escasa.

**Prevención:** exigir siempre el paso de evaluación económica y el análisis de dispersión, no sólo el de medias.

---

### Escenario 9 — El período de muestra nos engaña

**Qué haríamos:** entrenar y validar sobre los últimos 3 años del MNQ.

**Por qué engaña:** `[JANSEN]` Una muestra mal elegida puede carecer de aspectos de régimen relevantes, tener pocos puntos, o contener demasiados/pocos eventos extremos. Y el *factor decay* implica que lo que funcionó tiende a dejar de funcionar.

**Prevención:** `[JANSEN]` Períodos que incluyan fenómenos de mercado importantes; testeo en contextos y escenarios variados, posiblemente con datos sintéticos.

---

### Escenario 10 — Heredamos el sesgo de otros

**Qué haríamos:** construir features basadas en indicadores técnicos "conocidos por funcionar", o en configuraciones de parámetros que la comunidad usa.

**Por qué engaña:** `[JANSEN]` El riesgo de backtest overfitting **no surge sólo de nuestras pruebas**: también afecta a estrategias diseñadas con conocimiento previo de qué funciona; y como incluye backtests hechos por otros sobre los mismos datos, **es muy difícil de evitar**.

**Prevención:** `[JANSEN]` No asumir que un indicador contiene señal. Verificarlo con nuestros propios datos y nuestro propio protocolo, contando esa verificación como una prueba más en nuestro registro de multiple testing.

---

### Escenario 11 — Nos convencemos con un solo tramo out-of-sample

**Qué haríamos:** obtener un Sharpe out-of-sample de 2.15 en 12 meses y concluir que funciona.

**Por qué engaña:** `[INTERPRETACIÓN a partir de los propios resultados de JANSEN]` Ese es exactamente el número de su ejemplo de redes neuronales, con Sharpe in-sample de 0.72. Un Sharpe out-of-sample que triplica al in-sample sobre una ventana corta es un indicio de varianza muestral, no de generalización.

**Prevención:** múltiples ventanas out-of-sample independientes; reportar la distribución del rendimiento, no un punto; cuantificar la incertidumbre (el Sharpe bayesiano del capítulo 10 es la herramienta que el propio libro ofrece).

---

### Escenario 12 — Optimizamos la métrica equivocada

**Qué haríamos:** entrenar minimizando RMSE sobre retornos y celebrar una reducción del error.

**Por qué engaña:** `[INTERPRETACIÓN]` En un entorno donde la varianza del target es casi toda irreducible, RMSE está dominada por el ruido. Se puede reducir RMSE prediciendo siempre cerca de cero, con IC nulo. De hecho, Jansen **evalúa siempre con IC, no con RMSE**, aunque entrene con pérdidas cuadráticas.

**Prevención:** `[JANSEN]` Definir objetivos de modelo focalizados; consolidar objetivos en conflicto en una métrica; usar métricas personalizadas durante el entrenamiento (él implementa una métrica IC custom para LightGBM precisamente por esto).

---

## 17. BACKTESTING (Tarea 13)

### 17.1 Qué es y qué debe lograr

`[JANSEN]` El objetivo último del workflow ML4T es **reunir evidencia a partir de datos históricos** que ayude a decidir si desplegar una estrategia candidata en el mercado real arriesgando recursos financieros. El backtest simula una estrategia sobre datos históricos con el objetivo de producir resultados que **generalicen a nuevas condiciones de mercado**.

`[JANSEN]` Incorporar una idea de inversión a una estrategia real implica un riesgo significativo que requiere **enfoque científico**: tests empíricos extensos **con el objetivo de rechazar la idea** basándose en su rendimiento en escenarios de mercado alternativos fuera de muestra. El testeo puede incluir datos simulados para capturar escenarios considerados posibles pero no presentes en el histórico.

`[INTERPRETACIÓN]` La formulación "con el objetivo de rechazar la idea" es la orientación epistemológica correcta y merece ser adoptada literalmente por IRIS: el backtest no es una demostración, es un intento de falsación.

### 17.2 Vectorizado vs event-driven

**Vectorizado.** `[JANSEN]`
- Es la forma más básica: multiplica un vector de señales que representa el tamaño de posición objetivo por un vector de retornos del horizonte de inversión, para calcular el rendimiento del período.
- Permite una evaluación rápida y aproximada.
- **Le faltan características importantes de un motor robusto**: hay que alinear manualmente los timestamps de predicciones y retornos; no hay dimensionamiento explícito de posición ni representación del proceso de trading; no hay medición de rendimiento más allá de lo que se calcule a posteriori.

**Event-driven.** `[JANSEN]`
- Simula explícitamente la dimensión temporal del entorno de trading e impone significativamente más estructura.
- Usa calendarios históricos que definen cuándo se puede operar y cuándo hay cotizaciones disponibles.
- **La imposición de timestamps ayuda a evitar look-ahead bias y otros errores de implementación** — con la salvedad explícita de que **no lo garantiza**.
- Busca capturar más de cerca las acciones y restricciones que encuentra una estrategia, e idealmente puede convertirse directamente en un motor de trading en vivo.

`[IMPLICACIÓN PARA IRIS]` Ambos tienen un lugar: el vectorizado para iterar rápido durante la investigación, el event-driven para la evidencia final. Lo peligroso es confundir el primero con el segundo.

### 17.3 Componentes de un motor de backtest

`[JANSEN]` Los aspectos que hay que resolver:

1. **Ingesta de datos**: formatos, frecuencia (diaria/minuto/tick, en orden creciente de complejidad computacional y de memoria), combinación de frecuencias, y **restricciones point-in-time**. Calendarios de trading para limitar los datos a fechas y horas legítimas. Ajustes por corporate actions antes de la ingesta.
2. **Ingeniería de factores**: integrada en el motor (ventaja: la conversión a trading en vivo aplica las mismas computaciones a los inputs) o precalculada externamente (ventaja: amortiza el coste computacional entre varios backtests).
3. **Modelos, predicciones y señales**: entrenar dentro del backtest (más realista pero costoso, y convierte el entrenamiento en parte del backtest cuando quizá sólo queremos afinar reglas) o entrenar aparte y alimentar predicciones (el enfoque que Jansen usa mayoritariamente).
4. **Reglas de trading y ejecución**: acceso a los mercados, tipos de orden disponibles, contabilización de costes (comisiones de broker, spread bid-ask, **slippage** como diferencia entre el precio objetivo y el finalmente obtenido), y ejecución con **retardos que reflejen liquidez y horario de operación**.
5. **Evaluación de rendimiento**: métricas estándar derivadas de la contabilidad de transacciones, o salida compatible con una librería especializada.

### 17.4 Condiciones que debe cumplir un backtest para constituir evidencia razonable

Sintetizo aquí, como pidió el encargo, el estándar que se deriva de Jansen:

| Condición | Fundamento en Jansen |
|---|---|
| **Todos los datos son point-in-time verificados** | Solución explícita al look-ahead bias. |
| **La secuencia señal → orden → ejecución → evaluación está explícitamente ordenada en el tiempo** | Solución al pitfall de "timing of decisions". |
| **Costes de transacción, spread y slippage modelados con supuestos realistas** | Pitfall de transaction costs; y protege contra señales inestables de alto turnover. |
| **Rendimiento marcado a mercado a lo largo del tiempo, no sólo al final** | Una estrategia debe cumplir objetivos y restricciones **en todo momento**; se resuelve graficando rendimiento en el tiempo o calculando métricas de riesgo rolling (VaR, Sortino). |
| **Período muestral que incluya regímenes relevantes** | Pitfall de sample period. |
| **Resultados reportados separadamente in-sample y out-of-sample** | Práctica sistemática del libro (pyfolio, `show_perf_stats`). |
| **Número de pruebas realizadas reportado** | "El rendimiento de un backtest sólo es informativo si se reporta el número de intentos". |
| **Métricas corregidas por multiple testing** | Deflated Sharpe ratio. |
| **Longitud del backtest suficiente para el número de variantes probadas** | Regla de longitud mínima. |
| **Estrategia justificable teóricamente, no producto de minería** | Solución propuesta al backtest overfitting. |
| **Testeo en contextos y escenarios variados** | Idem; incluye posiblemente datos sintéticos. |
| **Paper trading escalonado y monitorización estrecha antes de capital real** | Jansen lo señala como parte necesaria del proceso de implementación. |

`[INTERPRETACIÓN]` Un backtest que cumple todo lo anterior sigue sin ser una garantía. Jansen es explícito en que los riesgos son **inevitables** y que no hay respuestas fáciles. Lo que estas condiciones consiguen no es certeza, sino que el resultado sea *interpretable*.


---

## 18. PREDICCIÓN ≠ RENTABILIDAD: EVALUACIÓN ECONÓMICA (Tarea 12)

### 18.1 La cadena y dónde se pierde valor en cada eslabón

```
PREDICTION       → un número. Sin coste, sin riesgo, sin realidad.
   ↓ pérdida: la predicción es ruidosa; IC realista de 0.02–0.05
SIGNAL           → agregación, ranking, ensemble
   ↓ pérdida: la agregación puede diluir o amplificar errores
TRADING RULE     → umbral, top-N, filtro
   ↓ pérdida: el umbral es arbitrario si no se optimiza; descarta información
POSITION         → dirección y tamaño
   ↓ pérdida: sizing subóptimo; restricciones (no short, límites)
EXECUTION        → timing real, retardo, disponibilidad
   ↓ pérdida: gap entre precio de decisión y precio de ejecución
TRANSACTION COST → comisión + spread + slippage + impacto
   ↓ pérdida: proporcional al turnover; puede exceder el edge completo
PNL              → resultado bruto
   ↓ pérdida: concentración temporal, asimetría
RISK             → drawdown, volatilidad, colas
   ↓ pérdida: un PnL positivo con drawdown inaceptable no es operable
STRATEGY PERF.   → Sharpe, Calmar, alpha, beta
```

### 18.2 Por qué un buen modelo de ML no es una buena estrategia

Cinco razones que se derivan directamente del libro:

**(1) El IC es bajo y el spread es pequeño.** `[JANSEN]` Los ICs útiles están entre 0.05 y 0.15 para gestores con muchas decisiones; su ejemplo intradiario produjo un spread medio de **0.5 puntos básicos por minuto** entre deciles extremos, y su ejemplo de boosting diario un spread de **12 pb** entre quintiles. `[INTERPRETACIÓN]` Un edge de medio punto básico compite directamente con el spread bid-ask, que en muchos instrumentos es de un orden de magnitud similar o superior.

**(2) El turnover come el edge.** `[JANSEN]` Su estrategia de boosting diario tuvo un turnover diario de ~115%, y él mismo advierte que los beneficios no están garantizados "no en último lugar porque hicimos supuestos muy generosos sobre costes de transacción, dada la alta rotación". El turnover del factor se identifica desde el capítulo 4 como indicador de coste potencial y como el motivo por el que más estabilidad es preferible.

**(3) Un factor puede ser significativo y perder dinero.** `[JANSEN]` Alpha 054: IC 0.025 significativo, spread de 1.5 pb, **retornos acumulados long-short negativos**.

**(4) Las distribuciones se solapan.** `[JANSEN]` Aunque las medias por quantil difieran, la separación de las distribuciones puede ser muy limitada; en un día concreto las diferencias pueden ser mínimas. `[INTERPRETACIÓN]` Un edge estadístico poblacional no garantiza acierto en decisiones individuales, y una estrategia real ejecuta decisiones individuales.

**(5) El rendimiento in-sample no anticipa el out-of-sample.** `[JANSEN]` Su ejemplo de boosting: 27.3% anual y Sharpe 1.24 in-sample; 8.0% y Sharpe 0.61 out-of-sample. Alpha 0.25 in-sample, 0.05 out-of-sample. **El edge se redujo aproximadamente a la mitad.**

### 18.3 La ley fundamental y su límite para IRIS

`[JANSEN]` El Information Ratio se aproxima como el producto de la habilidad predictiva (IC) y la **amplitud** de la estrategia, medida por el **número independiente de apuestas** que un inversor realiza en un período dado. Extendido con el **transfer coefficient**, que refleja la eficiencia con que las restricciones de cartera permiten trasladar los insights a apuestas efectivas. El mensaje: importa tanto **jugar bien** (IC alto) como **jugar a menudo** (amplitud alta).

`[JANSEN]` Añade una advertencia crucial: **estimar la amplitud es difícil en la práctica dada la correlación cross-sectional y temporal entre las previsiones**, y recomienda ver la ley como marco analítico, no como fórmula.

`[IMPLICACIÓN PARA IRIS]` Esta advertencia es, para nosotros, el punto central. IRIS no tiene amplitud cross-sectional: opera un instrumento. Su única fuente de amplitud es **temporal**: muchas decisiones a lo largo del tiempo. Pero las decisiones consecutivas sobre el mismo instrumento están correlacionadas (señales persistentes, condiciones de mercado persistentes, autocorrelación de retornos). **El número de apuestas independientes es mucho menor que el número de operaciones.** Esto tiene tres consecuencias:

1. Un IC dado se traduce en menos IR que en una estrategia cross-sectional con el mismo IC.
2. Aumentar la frecuencia de operación no aumenta la amplitud proporcionalmente, pero **sí aumenta los costes proporcionalmente**.
3. Cualquier cálculo de significación estadística sobre nuestros resultados debe basarse en apuestas independientes, no en operaciones.

### 18.4 Métricas de Machine Learning

`[JANSEN]`

**Regresión**: RMSE (la más popular; simétrica pero pondera más los errores grandes; expresada en unidades del target), RMSLE (para targets con crecimiento exponencial; penaliza asimétricamente), MAE y MedAE (simétricas, sin sobreponderar errores grandes; MedAE robusta a outliers), varianza explicada, R² (puede ser **negativo** fuera de muestra).

**Clasificación**: matriz de confusión y todas sus derivadas; accuracy; **ROC-AUC** (varía entre 0.5 y 1; resume cómo de bien el clasificador ordena los puntos respecto a su clase; equivale a la probabilidad de que ordene una instancia positiva aleatoria por encima de una negativa aleatoria; **insensible al desbalance de clases**); precisión y recall; curvas precision-recall; F1 (media armónica, útil para optimizar el umbral numéricamente).

**Específica de trading**: **Information Coefficient** — correlación de rangos de Spearman entre predicción y retorno futuro; IC ajustado por riesgo (media / desviación estándar del IC, con test t); IC diario, medio, mediano y su evolución rolling. `[JANSEN]` Implementa una métrica IC personalizada para LightGBM, precisamente porque las pérdidas estándar no capturan lo que le importa.

**Mutual information** para evaluación de features.

### 18.5 Métricas económicas / financieras

`[JANSEN]` De pyfolio y del capítulo 5:

| Métrica | Definición según Jansen |
|---|---|
| Retorno anual y acumulado | — |
| Volatilidad anual | — |
| **Sharpe ratio** | Exceso de retorno esperado sobre su desviación estándar. Compensación media por unidad de riesgo. Escalado entre frecuencias multiplicando por la raíz del número de períodos — **con la advertencia de Lo sobre autocorrelación**. |
| **Information ratio** | Como el Sharpe pero contra un benchmark en lugar del tipo libre de riesgo; mide el alpha relativo al tracking error. |
| **Max drawdown** | Mayor pérdida porcentual desde un pico previo. |
| **Calmar ratio** | Retorno anual relativo al máximo drawdown. |
| **Omega ratio** | Ratio ponderado por probabilidad de ganancias frente a pérdidas para un objetivo de retorno. |
| **Sortino ratio** | Exceso de retorno relativo a la desviación estándar **a la baja**. |
| **Tail ratio** | Tamaño de la cola derecha frente a la izquierda (percentil 95 en valor absoluto). |
| **VaR diario** | Pérdida correspondiente a un retorno a dos desviaciones estándar. |
| **Alpha** | Retorno de cartera no explicado por el benchmark. |
| **Beta** | Exposición al benchmark. |
| Skew y curtosis | Reportadas sistemáticamente. |
| Leverage bruto | — |
| **Turnover diario** | — |
| **Deflated Sharpe ratio** | Probabilidad de que el SR sea significativo controlando multiple testing, no normalidad y muestra corta. |
| **Sharpe bayesiano** | Comparación de rendimiento con incertidumbre explícita. |

`[JANSEN]` Prácticas asociadas: bootstrapping de la variabilidad de los parámetros (`plot_perf_stats`); reporte separado in-sample / out-of-sample; análisis de períodos de drawdown; exposición rolling a factores; comparación durante eventos históricos; y el cono de intervalos de confianza expansivos que indica cuándo los retornos out-of-sample resultan improbables bajo supuestos de random walk.

`[IMPLICACIÓN PARA IRIS]` Dos métricas destacan por su pertinencia a nuestro caso: **max drawdown y Calmar** (porque un sistema intradiario apalancado en futuros vive o muere por el drawdown), y **turnover** (porque determina si el edge sobrevive). El Sharpe anualizado desde barras intradiarias debe tratarse con la máxima desconfianza.

---

## 19. INTERPRETABILIDAD (Tarea 14)

### 19.1 Por qué importa, según Jansen

`[JANSEN]` Entender por qué un modelo predice cierto resultado importa por **confianza, accionabilidad, responsabilidad y depuración**. Además, las relaciones no lineales entre features y outcome descubiertas por el modelo, y las interacciones entre features, tienen valor por sí mismas cuando el objetivo es aprender más sobre los drivers del fenómeno.

`[JANSEN]` Y en el contexto del backtest overfitting: **los valores SHAP permiten atribuir con exactitud features y sus valores a las predicciones, de modo que resulta más fácil validar la lógica de un modelo a la luz de teorías específicas sobre el comportamiento del mercado** para un objetivo de inversión dado. Además de justificación, la atribución exacta permite insights más profundos sobre los drivers del resultado.

`[JANSEN]` Presenta también el contrapunto: Geoffrey Hinton argumenta que las razones de las decisiones humanas son a menudo oscuras, y quizá las máquinas deberían juzgarse por sus resultados, como se hace con los gestores de inversión.

### 19.2 El instrumental

Ya descrito en §7.5. Resumen operativo:

| Herramienta | Alcance | Qué responde |
|---|---|---|
| Importancia por **gain** | Global | ¿Qué features redujeron más la pérdida? |
| **Split count** | Global | ¿Qué features se usan más a menudo? |
| **Permutation importance** | Global, agnóstica al modelo | ¿Cuánto se degrada el rendimiento sin esta feature? |
| **Partial dependence plots** | Global, por feature o par | ¿Cuál es la respuesta esperada del target en función del valor de la feature? |
| **SHAP — resumen** | Global | ¿Cuál es la contribución media de cada feature? |
| **SHAP — scatter** | Global con detalle local | ¿Cómo varía el impacto de una feature según su valor y entre muestras? |
| **SHAP — force plot** | Individual | ¿Por qué **esta** predicción concreta? |
| **SHAP — force plots agrupados** | Poblacional | ¿Qué patrones de influencia son recurrentes en el dataset? |

`[JANSEN]` Ejemplo de force plot que da: la salida del modelo fue 0.6 frente a un valor base de 0.13 (la salida media del modelo sobre el dataset); la variable "mes = octubre" fue la feature más importante y elevó la salida de 0.338 a 0.537, mientras que "año = 2017" la redujo.

### 19.3 Cómo usar esto para responder "¿Por qué IRIS generó esta señal?"

`[IMPLICACIÓN PARA IRIS]` La combinación que el libro habilita:

1. **Nivel de la señal individual** → *force plot* de SHAP. Produce literalmente una descomposición aditiva: partiendo del valor base (la predicción media del modelo), cada feature empuja la predicción hacia arriba o hacia abajo con una magnitud cuantificada. Esto es exactamente la respuesta a "¿qué condiciones del mercado explican esta señal?".
2. **Nivel de patrón** → *force plots agrupados por clustering jerárquico*. Permitiría descubrir que IRIS genera señales largas por, digamos, tres razones recurrentes distintas, y caracterizarlas. Esto podría eventualmente alimentar la pregunta sobre regímenes.
3. **Nivel global** → *SHAP summary + partial dependence*. Permite verificar que el modelo se apoya en variables con sentido económico y no en artefactos (por ejemplo, detectar el Escenario 7 de §16: dominancia de variables de calendario).
4. **Nivel de abstención** → `[INTERPRETACIÓN]` Si el modelo produce un score cercano al valor base con contribuciones SHAP pequeñas y contrapuestas, eso es información: el modelo no tiene una razón fuerte. Es una vía candidata para construir la condición "no operar", aunque Jansen no la propone.

### 19.4 Limitaciones con features correlacionadas

`[JANSEN]` Lo que sí dice:
- Los métodos de atribución convencionales para ensembles de árboles son **inconsistentes**: un cambio en el modelo que aumente el impacto de una feature sobre la salida puede reducir su valor de importancia. SHAP se propone precisamente para resolver esto.
- Los partial dependence plots requieren **marginalizar** el resto de features, porque la naturaleza no lineal de los árboles hace que la relación dependa de los valores de todas las demás.
- Las diferentes métricas de importancia **discrepan entre sí** (SHAP dio más peso al MACD y a medidas de retorno relativo que la importancia convencional; MI e IC correlacionan sólo ~0.16).

`[VACÍO]` Lo que Jansen **no** desarrolla:
- El problema de que, con features fuertemente correlacionadas, la importancia se **reparte arbitrariamente** entre ellas, de forma que una variable genuinamente informativa puede aparecer con importancia baja simplemente porque tiene sustitutos.
- Que la permutation importance sobre features correlacionadas genera combinaciones de valores irreales.
- Que en series temporales, permutar rompe la estructura temporal y el resultado puede ser engañoso.
- Cómo agregar SHAP a lo largo del tiempo cuando las observaciones están autocorrelacionadas.

`[IMPLICACIÓN PARA IRIS]` En un espacio de features de indicadores técnicos, la correlación es extrema (una SMA de 20 y una de 21 son casi la misma variable). Deberemos: (a) medir la correlación entre features antes de interpretar importancias; (b) considerar agrupar features correlacionadas antes de atribuir importancia; (c) no confundir "importancia baja" con "sin información".

---

## 20. JANSEN APLICADO A MNQ INTRADIARIO (Tarea 10)

### 20.1 Todo el material intradiario que contiene el libro

Es sorprendentemente poco, y conviene que quede documentado con exactitud:

| Ubicación | Contenido intradiario |
|---|---|
| Cap. 1 | Mención del HFT como tendencia; latencias CME-BATS cerca del límite teórico de 8 ms; speed bumps regulatorios. Declaración de que **el libro no se centra en el muy corto plazo dominado por latencia**. |
| Cap. 2 | Microestructura; datos ITCH; construcción de barras desde ticks; barras de minuto de AlgoSeek con quote data para NASDAQ 100 (2013-2017), incluyendo desglose de volumen por posición relativa al bid/ask, upticks/downticks, VWAP y spreads. |
| Cap. 8 | Ingesta de bundles con datos de minuto en Zipline; mención de que las estrategias algorítmicas tienden a rendir mejor a mayor frecuencia. |
| **Cap. 12** | **El único experimento intradiario completo del libro.** |
| Cap. 4 | Racional de microestructura para el momentum intradiario. |
| Apéndice | Indicadores y funciones ts_* aplicables a cualquier frecuencia. |

### 20.2 El experimento intradiario del capítulo 12, en detalle

`[JANSEN]`
- **Datos**: AlgoSeek NASDAQ 100, feed consolidado del SIP, barras de minuto con NBBO y precios de operación. 100 tickers, 2013-2017. Más de 50 variables por barra.
- **Restricción**: sólo horario oficial de mercado, 390 minutos de 9:30 a 16:00, para acotar tamaño y **evitar períodos de actividad irregular**.
- **Target**: retorno forward a 1 minuto del **VWAP**.
- **Features**: 12 variables crudas seleccionadas de las 50+, sobre más de 51 millones de observaciones, para construir **sólo 20 features** debido a la huella de memoria:
  1. Retornos rezagados de cada uno de los últimos 10 minutos.
  2. Número de acciones negociadas con uptick y con downtick durante la barra, dividido por el volumen total.
  3. Número de acciones negociadas donde el precio se repite respecto a la operación anterior.
  4. Diferencia entre acciones negociadas al ask y al bid.
  5. Varios indicadores técnicos, incluyendo Balance of Power, Commodity Channel Index y Money Flow Index.
- **Cuidado explícito**: desplazamiento de los datos para evitar look-ahead, ejemplificado con el cálculo del Money Flow Index.
- **Evaluación univariante previa**: correlación de rangos de cada feature con el retorno forward a 1 minuto. **Resultado: los retornos rezagados recientes son presumiblemente las variables más informativas.**
- **Modelo**: LightGBM.
- **Validación**: 12 meses de datos de minuto para entrenar, previsiones out-of-sample para los 21 días de trading siguientes; repetido en **24 splits train-test** cubriendo los últimos 2 años de la muestra de 5 años. `MultipleTimeSeriesCV` adaptado a frecuencia de minuto, calculando longitudes sobre 390 observaciones por ticker y día.
- **Limitación computacional declarada**: ajustes por defecto con 250 árboles; a 250 iteraciones **la IC de validación seguía mejorando en la mayoría de folds**, de modo que los resultados **no son óptimos**; el entrenamiento ya llevaba varias horas.
- **Métrica**: IC personalizada implementada como métrica custom de LightGBM.
- **Resultados**: IC positiva y estadísticamente significativa de 1.90 (en las unidades que reporta, es decir ~0.019); IC media diaria 1.98 y mediana 1.91. Retorno medio por decil: **spread medio de 0.5 puntos básicos por minuto** entre deciles extremos. Los retornos acumulados de carteras equiponderadas por decil sugerían que, **antes de costes de transacción**, una estrategia long-short parecía atractiva.
- **Lo que NO hizo**: `[JANSEN]` **omitió el backtest con datos de minuto por ser muy costoso en tiempo**, e invita al lector a experimentar con Zipline o backtrader para evaluar la estrategia bajo supuestos más realistas de costes o con controles de riesgo apropiados.

`[INTERPRETACIÓN]` Este último punto es determinante. El único ejemplo intradiario del libro **no fue backtesteado con costes**. El edge medido es de medio punto básico por minuto sobre una estrategia long-short cross-sectional de 100 acciones. No hay ninguna evidencia en el libro de que ese edge sobreviva a la ejecución.

### 20.3 Clasificación de los conceptos intradiarios

Como pidió el encargo:

#### **Directamente transferibles a MNQ intradiario**

| Concepto | Nota |
|---|---|
| **Retornos rezagados de los últimos N minutos como features** | Resultaron las variables más informativas en su experimento. No requieren nada más que OHLCV. |
| **Restringir el horario a una sesión regular bien definida** | El motivo (evitar actividad irregular) aplica igual o más a futuros, que operan casi 24h con perfiles de liquidez radicalmente distintos. |
| **`MultipleTimeSeriesCV` adaptado a frecuencia de minuto** | Patrón de validación directamente reutilizable; sólo cambia el cálculo de observaciones por día. |
| **Métrica IC personalizada dentro del entrenamiento** | Aplicable tal cual. |
| **Desplazamiento explícito de indicadores para evitar look-ahead** | Obligatorio, idéntico. |
| **Evaluación univariante previa de features por correlación de rangos con el target** | Directamente aplicable; es el primer filtro barato. |
| **Análisis por deciles del valor de la predicción frente a retorno futuro** | Aplicable a serie temporal única agrupando momentos en lugar de activos. |
| **Todas las funciones ts_\* del apéndice** | Puramente de serie temporal. |
| **Indicadores TA-Lib de precio/volumen** | Computables sobre OHLCV de MNQ. Sin garantía de contenido de señal. |
| **Todos los pitfalls de backtesting del cap. 8** | Universales. |
| **Todo el kit de diagnóstico de series temporales del cap. 9** | Universal. |

#### **Conceptualmente adaptables**

| Concepto | Cómo habría que adaptarlo |
|---|---|
| **Information Coefficient** | En Jansen es correlación de rangos *entre activos* en cada fecha. Para IRIS habría que redefinirlo como correlación de rangos *entre momentos* dentro de una ventana temporal. **Es una redefinición, no un traslado**, y sus propiedades estadísticas no son necesariamente equivalentes. |
| **Análisis por quantiles** | De quintiles de activos a deciles de momentos. La lógica (¿separa el factor los retornos futuros?) se conserva. |
| **Factor turnover** | De rotación de activos entre quantiles a **persistencia/estabilidad de la señal en el tiempo** y frecuencia de cambio de signo. |
| **Ley fundamental (IC × amplitud)** | La amplitud pasa de ser cross-sectional a temporal, con el problema serio de correlación entre apuestas consecutivas (§18.3). |
| **Barras alternativas** | El motivo de las volume/dollar bars (fragmentación de órdenes, cambios de valor) tiene análogos en futuros, pero distintos. Requiere investigación propia. |
| **Features de order flow (uptick/downtick, volumen al bid/ask)** | Conceptualmente muy relevantes para MNQ, pero **requieren datos de tick o quote que no tenemos con OHLCV**. Sustitutos aproximados desde OHLCV (posición del cierre dentro del rango, relación entre rango y volumen) son heurísticas, no equivalentes. |
| **Predicción del VWAP forward** | Aplicable, pero el VWAP de un futuro y el de una acción tienen roles distintos en la ejecución. |
| **Descomposición estacional** | En Jansen es mensual/anual; en MNQ intradiario sería el perfil de sesión. La técnica es la misma; la interpretación es distinta. |

#### **Específicos de acciones**

- Reconstrucción del libro de órdenes vía ITCH.
- NBBO, SIP, Reg NMS, fragmentación entre exchanges, dark pools, volumen reportado a FINRA.
- Ajustes por splits, dividendos y corporate actions.
- Ratios fundamentales, sectores, dummies sectoriales.
- Factores de valor, calidad y tamaño.
- Restricciones de short-selling y disponibilidad de préstamo.

#### **Específicos de portfolios / cross-sectional**

- Alphalens en su integridad (requiere universo).
- Carteras long-short por quantil; equiponderación entre activos.
- Optimización media-varianza, risk parity, HRP, eigenportfolios.
- Beta y alpha respecto a un benchmark de mercado (aplicable a MNQ sólo si definimos benchmark, y el benchmark natural sería el propio Nasdaq-100 — lo que hace el alpha casi vacío de significado).
- La "breadth" de la ley fundamental.
- Cointegración y pairs trading.
- El embedding de ticker de la LSTM.

#### **Probablemente irrelevantes para la primera etapa**

- Todo NLP (caps. 14-16).
- Imágenes satelitales y transfer learning (cap. 18, primera mitad).
- Datos fundamentales, XBRL, filings SEC.
- Datos alternativos de terceros.
- Survivorship bias (aunque su análogo, el sesgo de selección de contrato/período, sí existe).

#### **Requieren investigación adicional propia**

1. **¿Cuánta de la señal de su ejemplo intradiario provenía de features de quote que nosotros no tenemos?** Su evaluación univariante sugiere que los retornos rezagados eran lo más informativo, lo cual es alentador, pero no lo cuantifica frente a las features de order flow.
2. **¿Se traslada un edge cross-sectional de 0.5 pb/min a un instrumento único?** Una estrategia long-short de 100 acciones diversifica el ruido idiosincrático. IRIS no puede.
3. **¿Qué timeframe intradiario tiene mejor relación señal/ruido en MNQ?** El libro sólo prueba 1 minuto y sólo con un target de 1 minuto.
4. **¿Cómo se define la abstención?** No hay material.
5. **¿Cómo se etiquetan los eventos?** No hay material.
6. **¿Qué costes reales tiene operar MNQ intradiario y qué edge mínimo se necesita?** El libro omitió precisamente este cálculo.
7. **¿Cuál es el número efectivo de observaciones independientes en nuestro histórico?** Determina cuántas hipótesis podemos permitirnos probar.
8. **¿Cómo se maneja el rollover de contratos?** No hay material directo; el análogo son las corporate actions.

### 20.4 Conclusión de la sección

`[INTERPRETACIÓN]` Jansen aporta a IRIS un **método** intradiario y prácticamente ninguna **evidencia** intradiaria. Su experimento de un solo minuto es cuidadoso en validación, honesto sobre sus límites computacionales, y explícitamente incompleto en su evaluación económica. Lo valioso es el diseño experimental; lo que no podemos tomar es la conclusión.

---

## 21. ERRORES QUE PODRÍAN DESTRUIR IRIS ANTES DE EMPEZAR (Tarea 15)

Formato: **ERROR → POR QUÉ ES PELIGROSO → CÓMO PODRÍA ENGAÑARNOS → CÓMO PREVENIRLO**

### Bloque A — Datos

**A1. Usar datos que no eran conocidos en el momento.**
→ Peligro: `[JANSEN]` el look-ahead bias produce medidas de rendimiento engañosas y no representativas del futuro.
→ Engaño: métricas excelentes que se evaporan en vivo.
→ Prevención: validación de timestamps de todo dato que entra al backtest; test de causalidad de cada feature (¿cambia su valor en t si añado datos posteriores?).

**A2. No ajustar los rollovers de contrato del MNQ.**
→ Peligro: análogo funcional de las corporate actions, que `[JANSEN]` exige ajustar antes de la ingesta.
→ Engaño: saltos artificiales de precio interpretados como movimientos reales; un modelo puede "aprender" a predecir el salto de rollover, que es determinista y no operable.
→ Prevención: política explícita de continuidad de contrato (ajuste por diferencia, por ratio, o exclusión de las sesiones de rollover), documentada y consistente entre backtest y producción.

**A3. Eliminar valores extremos que eran mercado real.**
→ Peligro: `[JANSEN]` el desafío es distinguir outliers no representativos de valores extremos que son parte integral del entorno.
→ Engaño: la estrategia parece robusta porque eliminamos precisamente los días en que habría fallado.
→ Prevención: análisis de la probabilidad de ocurrencia de extremos; documentar cada exclusión; evaluar la estrategia con y sin ellos.

**A4. Ignorar gaps, barras faltantes y horarios irregulares.**
→ Peligro: los indicadores rolling se calculan sobre ventanas que atraviesan interrupciones sin sentido económico.
→ Engaño: features aparentemente informativas que sólo codifican discontinuidades.
→ Prevención: `[JANSEN]` calendarios de trading; restricción a un horario bien definido, como hace en su ejemplo intradiario.

**A5. Sobrestimar el tamaño muestral.**
→ Peligro: `[JANSEN]` los datos no son IID; hay correlación serial. Un millón de barras no son un millón de observaciones independientes.
→ Engaño: significación estadística espuria; sensación de tener datos de sobra para probar muchas hipótesis.
→ Prevención: estimar el número efectivo de observaciones independientes; aplicar la regla de longitud mínima de backtest sobre esa cifra, no sobre el número de filas.

### Bloque B — Timeframe y muestreo

**B1. Elegir el timeframe por intuición o conveniencia.**
→ Peligro: es una de las decisiones más determinantes de todo el sistema y no hay razón para acertarla a priori.
→ Engaño: si se prueban varios timeframes y se reporta el mejor sin contarlo, es multiple testing puro.
→ Prevención: `[JANSEN]` Su método para horizontes es directamente aplicable: generar varios sistemáticamente, evaluarlos con el mismo protocolo, y **contar cada uno como una prueba**.

**B2. Asumir que barras temporales son la única opción, o que las alternativas son mejores.**
→ Peligro: `[JANSEN]` documenta que las barras temporales pueden fallar ante la fragmentación de órdenes, y presenta alternativas — **pero no aporta evidencia comparativa**.
→ Engaño: adoptar dollar bars por sofisticación aparente, o descartarlas por inercia.
→ Prevención: mantener la decisión abierta; comparar empíricamente propiedades estadísticas sobre nuestros propios datos; llevar la pregunta a la siguiente fuente.

### Bloque C — Features

**C1. Asumir que los indicadores técnicos contienen señal predictiva.**
→ Peligro: `[JANSEN]` muestra explícitamente Bollinger Bands y RSI **fallando** en su propio ejemplo. Y advierte que las alphas formulaicas carecen de interpretación económica y son propensas a falsos descubrimientos.
→ Engaño: seleccionar los indicadores que funcionaron en nuestra muestra histórica es exactamente el mecanismo del data snooping.
→ Prevención: tratar cada indicador como hipótesis a falsar; exigir racional económico previo; contar cada indicador evaluado en el registro de pruebas.

**C2. Generar cientos de features "por si acaso".**
→ Peligro: `[JANSEN]` maldición de la dimensionalidad; y sobre todo, multiplicación de la superficie de multiple testing.
→ Engaño: alguna feature siempre parecerá importante por azar.
→ Prevención: `[JANSEN]` priorizar transformaciones justificables; evaluación univariante barata antes de entrenar; medir la correlación entre features y agrupar redundancias.

**C3. Normalizar o filtrar usando información futura.**
→ Peligro: z-scores globales, escaladores ajustados sobre todo el dataset, suavizado no causal (Kalman en modo smoothing, reconstrucción wavelet completa).
→ Engaño: es el leakage más difícil de detectar porque parece preprocesamiento inocuo.
→ Prevención: todo escalador se ajusta sólo con datos de entrenamiento; todo filtro debe ser causal y verificado.

**C4. Dejar que las variables de calendario dominen.**
→ Peligro: `[JANSEN]` en su modelo diario, los indicadores de período temporal dominaron la importancia de features.
→ Engaño: en intradiario, el modelo aprende el perfil determinista de la sesión y las métricas mejoran sin que exista capacidad predictiva direccional.
→ Prevención: evaluar el rendimiento condicionado a franja horaria; comparar contra un baseline que use sólo variables de calendario; considerar desestacionalizar antes de modelar.

### Bloque D — Targets

**D1. Elegir un target sin evidencia.**
→ Peligro: la elección del target determina qué puede aprender el modelo, y `[JANSEN]` reconoce que la misma tarea admite varias formulaciones.
→ Engaño: encontrar buenos resultados con un target trivialmente predecible (p.ej. algo que dependa mecánicamente del pasado).
→ Prevención: `[JANSEN]` probar varios horizontes sistemáticamente y comparar por IC; verificar que el target no es predecible por construcción.

**D2. Usar horizontes largos con datos de alta frecuencia sin purging.**
→ Peligro: `[JANSEN]` etiquetas solapadas → filtración train/test → **rendimiento artificialmente inflado**.
→ Engaño: el problema escala con el horizonte; a mayor horizonte, más contaminación.
→ Prevención: purging y embargoing; separación temporal explícita entre train y test de al menos la longitud del horizonte.

**D3. Definir clases usando estadísticos de toda la muestra.**
→ Peligro: definir los umbrales de "movimiento grande" sobre la distribución completa introduce look-ahead.
→ Prevención: definir umbrales con información disponible en el momento (volatilidad rolling, cuantiles expansivos).

### Bloque E — Leakage y validación

**E1. Usar cross-validation estándar con shuffle.**
→ Peligro: `[JANSEN]` la CV asume IID; el shuffle usa el futuro para predecir el pasado. Es data snooping.
→ Engaño: métricas excelentes y completamente ficticias.
→ Prevención: sólo splits que respeten el orden temporal.

**E2. Usar early stopping con datos de validación y luego reportar esa validación.**
→ Peligro: `[JANSEN]` advertencia explícita: el backtest saldrá excesivamente positivo; las estimaciones estarán sesgadas al alza.
→ Prevención: separar el conjunto de parada del conjunto de reporte.

**E3. Contaminar el hold-out.**
→ Peligro: `[JANSEN]` el hold-out se usa una única vez, tras completar la CV.
→ Engaño: cada mirada al test es una decisión que lo convierte en validación.
→ Prevención: protocolo escrito; registro de accesos; reservar histórico adicional intocado.

### Bloque F — Selección de modelos e hiperparámetros

**F1. Elegir el mejor modelo entre muchos y reportar su score de validación.**
→ Peligro: `[JANSEN]` ese score **ya está sujeto a sesgo de multiple testing** y no es una buena estimación del error de generalización.
→ Prevención: hold-out separado; deflated Sharpe; reportar cuántos modelos se probaron.

**F2. Interpretar diferencias pequeñas entre configuraciones como reales.**
→ Peligro: `[JANSEN]` en su propio experimento de redes, la regresión del IC sobre las opciones de arquitectura tuvo **R² prácticamente cero**: el ruido dominaba.
→ Engaño: creer que hemos "encontrado la arquitectura correcta".
→ Prevención: replicar su test — regresar la métrica sobre las opciones de diseño y ver si explican algo. Si no, admitir que la elección es arbitraria.

**F3. Asumir que el modelo más complejo será mejor.**
→ Peligro: `[JANSEN]` *no free lunch*; si la relación verdadera es simple y los datos ruidosos, el modelo complejo aprenderá el ruido como parte de la relación compleja que asume.
→ Prevención: baselines obligatorios; exigir superioridad material y robusta antes de escalar complejidad.

**F4. No fijar semillas ni controlar la variabilidad estocástica.**
→ Peligro: `[JANSEN]` en el ejemplo de CNN, modificaciones ligeras producían rendimientos significativamente peores.
→ Engaño: elegir la ejecución afortunada.
→ Prevención: múltiples semillas; reportar la distribución de resultados, no el mejor.

### Bloque G — Evaluación y backtesting

**G1. Evaluar con la métrica equivocada.**
→ Peligro: RMSE está dominada por el ruido irreducible.
→ Prevención: `[JANSEN]` métricas alineadas con el objetivo; él usa IC y llega a implementarla como métrica custom.

**G2. Ignorar costes de transacción.**
→ Peligro: `[JANSEN]` los mercados no permiten ejecutar todo al precio objetivo; una simulación que asume lo contrario produce resultados sesgados; y él mismo advierte que sus resultados asumían costes "muy generosos" dada la alta rotación.
→ Engaño: en intradiario, un edge de fracciones de punto básico parece rentable hasta que se restan spread y comisiones.
→ Prevención: modelar costes desde el primer backtest, no al final; calcular el **edge mínimo requerido** antes de empezar a modelar.

**G3. Confundir señal con orden ejecutada.**
→ Peligro: `[JANSEN]` señales calculadas al cierre y operadas a la apertura siguiente a precios distintos.
→ Prevención: secuencia explícita y auditable de señal → orden → fill.

**G4. Evaluar sólo el resultado final y no la trayectoria.**
→ Peligro: `[JANSEN]` una estrategia debe cumplir objetivos y restricciones **en todo momento**; si genera pérdidas o volatilidad inaceptables por el camino, no es practicable.
→ Prevención: marcado a mercado; métricas de riesgo rolling; análisis de períodos de drawdown.

**G5. Conclusiones económicas injustificadas a partir de métricas estadísticas.**
→ Peligro: el caso Alpha 054 — IC significativo, spread positivo, retorno acumulado negativo.
→ Prevención: nunca declarar éxito antes de la evaluación económica con costes.

**G6. Concluir desde una sola ventana out-of-sample.**
→ Peligro: los propios números del libro (Sharpe OOS de 2.15 vs IS de 0.72 en 12 meses) ilustran la varianza posible.
→ Prevención: múltiples ventanas; distribución de resultados; cuantificación de incertidumbre.

### Bloque H — Proceso e interpretación

**H1. No llevar registro del número de experimentos.**
→ Peligro: `[JANSEN]` el rendimiento de un backtest **sólo es informativo si se reporta el número de intentos**; sin ese registro no se puede corregir por sesgo de selección y **el resultado es literalmente ininterpretable**.
→ Prevención: registro desde el primer día, incluyendo experimentos abandonados. Este debería ser el primer artefacto de ingeniería del proyecto, antes que cualquier modelo.

**H2. Diseñar sobre conocimiento previo de qué funciona.**
→ Peligro: `[JANSEN]` el overfitting incluye el conocimiento de backtests hechos por otros sobre los mismos datos, y por eso es muy difícil de evitar.
→ Prevención: honestidad sobre los priors; preferir hipótesis con racional económico; validar sobre períodos y regímenes distintos.

**H3. Interpretar importancias de features correlacionadas.**
→ Peligro: la importancia se reparte entre sustitutos; las métricas discrepan entre sí.
→ Prevención: medir correlación entre features primero; agrupar; usar SHAP y contrastar con otras métricas sin asumir que coinciden.

**H4. Olvidar el decay.**
→ Peligro: `[JANSEN]` los excesos de rendimiento caen ~25% desde el descubrimiento y >50% tras la publicación; la naturaleza competitiva del trading implica que los patrones evolucionan rápido, lo que **requiere atención adicional a la monitorización y al mantenimiento del modelo**.
→ Engaño: creer que una validación inicial exitosa es permanente.
→ Prevención: monitorización continua; reentrenamiento planificado; criterios de retirada definidos antes del despliegue.

**H5. Saltarse el paper trading.**
→ Peligro: `[JANSEN]` cuando se avanza hacia una estrategia en vivo, el paper trading escalonado y la monitorización estrecha del rendimiento durante la ejecución **deben formar parte del proceso de implementación**.
→ Prevención: incluirlo en el plan desde el principio.

---

## 22. LIMITACIONES DE JANSEN PARA IRIS (Tarea 16)

### A. Lo que podemos adoptar directamente

1. El **workflow ML4T** como estructura del proyecto: idea → datos → features → target → modelo → señal → regla → posición → resultado → validación.
2. El catálogo completo de **pitfalls de backtesting** y sus remedios (cap. 8).
3. El **protocolo de validación temporal**: splits que respetan el orden, tres particiones con hold-out de un solo uso, walk-forward con ventana expansiva o deslizante, `MultipleTimeSeriesCV`.
4. Las **advertencias sobre multiple testing** y sus herramientas: deflated Sharpe, longitud mínima de backtest, regla de parada, reporte del número de pruebas.
5. El **kit de diagnóstico de series temporales**: descomposición, rolling stats, ACF/PACF, ADF, GARCH.
6. El **método de selección de horizonte**: generar múltiples forward returns y comparar por IC.
7. Las **métricas económicas** de pyfolio y la práctica de reportar in-sample y out-of-sample por separado.
8. El **instrumental de interpretabilidad**: importancias, permutación, partial dependence, SHAP en sus cuatro modalidades.
9. Las **funciones ts_\*** del apéndice y los indicadores de TA-Lib como material de construcción (no como señal validada).
10. El **diseño experimental** del capítulo 11: lookback, lookahead, test period, hiperparámetros, ensembling como decisiones explícitas.
11. La **regularización** en todas sus formas y la advertencia sobre early stopping.
12. El **bias-variance trade-off** y las curvas de aprendizaje y validación como diagnóstico.
13. La disciplina de **evaluar features univariantemente antes de entrenar**.
14. El principio de **priorizar hipótesis con racional económico**.

### B. Lo que podemos adaptar conceptualmente

1. **Information Coefficient** → redefinido sobre momentos temporales en lugar de activos. Requiere pensar sus propiedades estadísticas de nuevo.
2. **Análisis por quantiles** → deciles de momentos históricos según el valor de la feature/predicción.
3. **Factor turnover** → persistencia de la señal, frecuencia de cambio de signo, autocorrelación de la señal.
4. **Ley fundamental** → con amplitud temporal, reconociendo la correlación entre apuestas consecutivas.
5. **Alphalens** → no la librería, sino su batería de preguntas, reimplementada para serie única.
6. **Descomposición estacional** → del ciclo anual al perfil intradiario de sesión.
7. **Features de order flow** → aproximaciones desde OHLCV, con la conciencia de que son sustitutos imperfectos.
8. **Clustering** → de activos a regímenes temporales, con asignación causal.
9. **PCA** → de factores de riesgo a diagnóstico de redundancia entre features.
10. **Denoising (Kalman, wavelets, autoencoders)** → sólo en versión estrictamente causal.
11. **Alpha, beta, benchmark** → el benchmark natural de MNQ es el propio Nasdaq-100, lo que hace que "alpha" signifique algo distinto que en el libro.

### C. Lo que NO debemos trasladar directamente

1. **Todo el aparato cross-sectional**: ranking entre activos, carteras long-short por quantil, equiponderación entre activos, breadth cross-sectional.
2. **Optimización de cartera**: media-varianza, risk parity, HRP, eigenportfolios.
3. **Factores fundamentales**: valor, calidad, tamaño; y los ~200 factores del apéndice que dependen de fundamentales o de sección transversal.
4. **Infraestructura de mercado de equities US**: NBBO, SIP, Reg NMS, ITCH, dark pools, fragmentación.
5. **Corporate actions**: splits y dividendos. (Sustituir por rollover de contratos.)
6. **Survivorship bias** en su forma literal.
7. **Cointegración y pairs trading**.
8. **Todo el NLP y el procesamiento de imágenes**.
9. **Sus resultados numéricos de rendimiento**, todos ellos: obtenidos sobre universos de cientos de acciones, en su mayoría antes de costes, sobre ventanas out-of-sample cortas.
10. **La conclusión implícita de que sus ejemplos "funcionan"**. El propio autor declara que incluyó ejemplos que no dan buenos resultados deliberadamente.
11. **El enfoque de RL con un solo activo**, que él mismo señala como el de mayor riesgo de overfitting.
12. **Las configuraciones concretas de hiperparámetros**, que él advierte que aplican sólo a sus ejemplos.

### D. Lo que Jansen no cubre suficientemente

Listado explícito de vacíos, para llevarlos como preguntas a las siguientes fuentes:

1. **Labeling.** No hay teoría del etiquetado. Sin barreras, sin horizontes dinámicos, sin escalado por volatilidad, sin ponderación por unicidad de muestras, sin meta-etiquetado, sin muestreo por eventos.
2. **La decisión de no operar.** Ninguna formulación del libro la incorpora explícitamente (salvo el RL, donde es una acción más pero no se desarrolla).
3. **Purging, embargoing y CV combinatoria.** Los nombra y los atribuye a López de Prado, pero no los implementa ni los evalúa.
4. **Número efectivo de observaciones independientes.** Reconoce el problema de la no-independencia pero no ofrece método para cuantificarla.
5. **Detección y gestión de cambios de régimen.** Sin tests de ruptura estructural, sin modelos de cambio de régimen, sin política de reentrenamiento adaptativo.
6. **Comparación empírica de esquemas de muestreo.** Presenta cuatro tipos de barra y usa sólo uno.
7. **Position sizing basado en la predicción.** Casi siempre equiponderado; no hay Kelly, no hay sizing por confianza, no hay sizing por volatilidad.
8. **Gestión de riesgo a nivel de operación.** Sin stops, sin objetivos de beneficio, sin gestión de la posición dentro de la operación.
9. **Calibración de probabilidades.**
10. **Normalización de features en series no estacionarias.** No hay tratamiento sistemático de cómo estandarizar sin look-ahead ni cómo elegir ventanas.
11. **Interpretabilidad con features correlacionadas.** Ver §19.4.
12. **Modelado de costes de transacción de forma detallada.** Los menciona constantemente como crítica pero rara vez los cuantifica; y en el ejemplo intradiario los omite por completo.
13. **Futuros como clase de activo.** Rollover, apalancamiento, margen, valor de tick, horario continuo, base — nada de esto aparece.
14. **Trading de un instrumento único.** No hay un solo ejemplo completo con un solo activo, salvo el agente de RL, que él marca como problemático.
15. **Cómo agregar múltiples señales de forma no trivial.** Su ejemplo del cap. 4 promedia rankings y él mismo lo califica de bastante ingenuo, remitiendo al ML posterior — pero el ML posterior tampoco aborda la agregación de señales heterogéneas.
16. **Monitorización y mantenimiento en producción.** Señala su necesidad; no desarrolla método.

### E. Lo que deberemos investigar posteriormente

1. Todo lo del punto D, a repartir entre López de Prado (labeling, muestreo, validación, unicidad de muestras, sizing) y Murphy (racional de estructura de mercado, patrones de precio, análisis técnico como cuerpo de hipótesis).
2. Las propiedades estadísticas específicas del MNQ intradiario (§3.9).
3. El coste real de operar MNQ y el edge mínimo requerido.
4. Cuánta de la señal intradiaria documentada por Jansen depende de datos de quote que no tenemos.
5. Si un edge cross-sectional se traslada a instrumento único.
6. Cómo definir operativamente la abstención.
7. Cómo cuantificar la confianza de una señal.

### F. Nota sobre las diferencias estructurales

| Dimensión | Jansen | IRIS |
|---|---|---|
| Activos | Cientos a miles de acciones/ETFs | Un futuro (MNQ) |
| Tipo de predicción | Mayoritariamente cross-sectional | Time-series |
| Frecuencia dominante | Diaria (mensual/semanal en varios casos) | Intradiaria |
| Fuente de diversificación | Entre activos | Sólo temporal |
| Fuente de amplitud | Número de activos × períodos | Sólo períodos, correlacionados |
| Datos disponibles | OHLCV + quotes + fundamentales + alternativos | OHLCV |
| Vehículo | Acciones al contado | Futuro apalancado con rollover |
| Regla operativa típica | Top-N / Bottom-N | Por definir |
| Naturaleza | Ejemplos educativos, mayormente sin costes | Sistema destinado a ser real |
| Benchmark | Índice de mercado (S&P 500) | El propio índice subyacente |

`[INTERPRETACIÓN]` La última fila merece atención: en Jansen, "alpha" significa rendimiento no explicado por la exposición al mercado. Para una estrategia sobre MNQ, el mercado *es* el Nasdaq-100. Cualquier posición larga en MNQ tiene beta 1 por construcción. Esto significa que las métricas alpha/beta del libro **cambian de significado** en nuestro contexto y no pueden usarse mecánicamente.


---

## 23. MATRIZ DE CONOCIMIENTO PARA IRIS (Tarea 18)

| Concepto | Qué dice Jansen | Relevancia IRIS | Aplicación potencial | Riesgos | Decisión pendiente |
|---|---|---|---|---|---|
| **Workflow ML4T** | El ML es un elemento de un proceso, no un ejercicio aislado | **Muy alta** | Estructura del proyecto completo | Saltarse eslabones da resultados no interpretables | Ninguna — se adopta |
| **Bajo ratio señal/ruido** | Característica definitoria del dominio; obliga a emparejar complejidad de modelo y datos | **Muy alta** | Justifica empezar simple | Subestimarlo lleva a sobreajuste sistemático | Cuantificarlo en MNQ |
| **Alpha factors** | Transformaciones de datos crudos que predicen movimientos; un valor por activo por evaluación | Alta | Features candidatas | Data snooping; ~250 factores publicados y creciendo | Cuáles evaluar y con qué prioridad |
| **Intuición económica previa** | Requisito para evitar falsos descubrimientos | **Muy alta** | Filtro de hipótesis | Racionalizar a posteriori es autoengaño | Qué racionales aplican a MNQ intradiario |
| **Factor decay** | Excesos de retorno caen ~25% al descubrirse y >50% tras publicarse | Alta | Justifica monitorización y reentrenamiento | Creer que una validación es permanente | Política de mantenimiento |
| **Barras: tick/time/volume/dollar** | Presenta las cuatro; usa sólo temporales; no compara | Alta | Esquema de muestreo de MNQ | Adoptar una por moda o inercia | **Abierta** — comparar empíricamente y consultar LdP |
| **Bid-ask bounce** | Oscilación espuria que motiva agregar | Media-alta | Elección de frecuencia mínima | Modelar ruido de microestructura como señal | Materialidad en MNQ |
| **Microestructura como origen de momentum intradiario** | Stops, CPPI, delta hedging y risk parity crean momentum mecánico | **Alta** | Racional económico para señal intradiaria en instrumento único | Es una hipótesis, no un hecho verificado | Testear si el momentum de corto plazo existe en MNQ |
| **OHLCV vs quote data** | Su ejemplo intradiario usa 50+ variables incluyendo order flow | **Muy alta** | Determina qué features podemos construir | Asumir que su resultado se replica con OHLCV solo | **Abierta** — ¿obtenemos datos de tick/quote? |
| **Estacionariedad y raíz unitaria** | Precios normalmente no estacionarios; random walk con long memory | Alta | Elección de transformaciones | Modelar niveles produce R² alto y valor nulo | Qué transformación es estacionaria en MNQ |
| **ACF / PACF / ADF** | Kit de diagnóstico previo al modelado | **Muy alta** | Caracterización de nuestros datos | Saltarse el diagnóstico | Ninguna — se adopta |
| **Heterocedasticidad y GARCH** | La varianza cambia de forma predecible | **Alta** | Target alternativo; sizing; filtro de régimen | Confundir predecir volatilidad con predecir dirección | ¿Es la volatilidad un target de IRIS? |
| **Estacionalidad intradiaria** | Descomposición separa componentes deterministas del residuo | **Muy alta** | Desestacionalizar antes de modelar | El modelo aprende el reloj, no el mercado | Cómo tratar el perfil de sesión |
| **Kalman / wavelets** | Denoising; Kalman se adapta a no estacionariedad; supuestos gaussianos violados en finanzas | Media | Suavizado de features | **Look-ahead si no es causal** | Si se usa, en versión estrictamente causal |
| **Indicadores técnicos (TA-Lib)** | 200+ disponibles; muestra Bollinger y RSI fallando | Media | Material de construcción de features | Asumir que contienen señal | **Abierta** — evaluar sin prejuicio, contando cada prueba |
| **Funciones ts_\* (WorldQuant)** | Operadores de serie temporal componibles | Alta | Vocabulario para construir features | Minería a gran escala sin racional | Qué subconjunto usar |
| **Information Coefficient** | Spearman entre predicción y retorno futuro; 0.05–0.15 es rango realista | **Muy alta** | Métrica primaria de evaluación de señal | Es cross-sectional en origen; redefinirlo cambia sus propiedades | Cómo definirlo para serie única |
| **Mutual information** | Extiende correlación a no linealidad; discrepa mucho del IC (~0.16) | Media-alta | Evaluación complementaria de features | Sensible al tamaño de muestra; costosa | Si se usa, con qué muestreo |
| **Análisis por quantiles + dispersión** | Medias distintas pero distribuciones muy solapadas | **Muy alta** | Evaluar poder discriminante real de una feature | Mirar sólo medias y no dispersión | Ninguna — se adopta adaptado |
| **Factor turnover** | Rotación como proxy de coste; más estabilidad es preferible | **Muy alta** | Persistencia de la señal | En intradiario el turnover puede eliminar todo el edge | Cómo medir persistencia de señal |
| **Forward returns multi-horizonte** | Generar varios y elegir por IC | **Muy alta** | Método para decidir el horizonte | Contar cada horizonte como prueba | **Abierta** — qué horizontes probar |
| **Targets: precio / retorno / dirección / clases** | Misma tarea, varias formulaciones; decisión de diseño | **Muy alta** | Formulación del problema | Elegir sin evidencia | **Abierta** — decisión clave |
| **Labeling avanzado** | **No lo cubre** | **Muy alta** | — | Improvisar un esquema propio sin base | **Abierta** — llevar a López de Prado |
| **Clase "no operar"** | **No la aborda** | **Muy alta** | Núcleo del objetivo de IRIS | Definirla arbitrariamente | **Abierta** |
| **Etiquetas solapadas** | Filtran información y inflan artificialmente el rendimiento | **Muy alta** | Diseño de la validación | Es invisible si no se busca | Purging/embargo: método a definir |
| **CV asume IID; finanzas no lo es** | Correlación serial y heterocedasticidad | **Muy alta** | Prohibición de shuffle | Cualquier CV estándar invalida todo | Ninguna — es una restricción |
| **TimeSeriesSplit / MultipleTimeSeriesCV** | Walk-forward expansivo o deslizante | **Muy alta** | Esquema de validación base | Elegir longitudes arbitrariamente | Longitudes de train/test |
| **Purging / embargo / CV combinatoria** | Los nombra y atribuye a LdP; no los implementa | **Muy alta** | Validación correcta | Omitirlos por no estar desarrollados aquí | **Abierta** — llevar a López de Prado |
| **Hold-out de un solo uso** | Único estimador insesgado tras muchas iteraciones de CV | **Muy alta** | Protocolo experimental | Contaminarlo mirando repetidamente | Ninguna — se adopta |
| **Multiple testing** | 2 años diarios ≈ 7 estrategias; 5 años ≈ 45 | **Muy alta** | Presupuesto de experimentación | Sin registro, los resultados son ininterpretables | Cuántas observaciones independientes tenemos |
| **Deflated Sharpe Ratio** | Corrige por pruebas, no-normalidad y muestra corta | Alta | Reporte final | No aplicarlo y sobrevalorar el resultado | Ninguna — se adopta |
| **Regla de parada (1/e)** | Explorar ~37% y luego tomar el primero que supere | Media | Gobierno del proceso de búsqueda | Buscar indefinidamente hasta encontrar algo bonito | Si se formaliza |
| **Look-ahead bias** | Point-in-time obligatorio | **Muy alta** | Auditoría de features | Es el error más común y más invisible | Ninguna — es una restricción |
| **Early stopping** | Puede introducir look-ahead y sesgar la CV al alza | **Muy alta** | Protocolo de entrenamiento | Reportar el conjunto usado para parar | Ninguna — es una restricción |
| **Baselines** | *No free lunch*; comparar contra benchmark | **Muy alta** | Referencia obligatoria | Sin baseline no hay conclusión posible | Qué baselines exactos |
| **Modelos lineales + regularización** | Inferencia disponible; ridge preserva, lasso hace dispersión | Alta | Baseline y diagnóstico | Descartarlos por simples | Ninguna — se adoptan como baseline |
| **Árboles / RF / Boosting** | Pocos supuestos; capturan interacciones; muy tuneables | **Alta** | Modelo no lineal de referencia | Overfitting; early stopping sesgado; OOB asume intercambiabilidad | Cuándo introducirlos |
| **Bias-variance y curvas de aprendizaje** | Diagnóstico para decidir entre más datos o más complejidad | Alta | Herramienta de decisión | Ignorarlas y tunear a ciegas | Ninguna — se adoptan |
| **Deep Learning** | Presentado a fondo; resultados frágiles y no robustos | Media | Sólo si se justifica con evidencia | Complejidad sin retorno; ruido domina la arquitectura | **Abierta** — criterios en §13.3 |
| **CNN sobre series** | Requiere patrones locales y organización que importe | Baja-media | Línea futura | Fragilidad demostrada; óptimo local constante | **Abierta** |
| **RNN / LSTM** | Memoria genuina; AUC ~0.68 en su ejemplo | Media | Línea si el problema es secuencial | Datos insuficientes en serie única | **Abierta** |
| **Autoencoders (denoising)** | Compresión y limpieza no lineal | Baja-media | Línea futura de reducción de ruido | Look-ahead si no es causal | **Abierta** |
| **GANs / datos sintéticos** | Motivados por overfitting y escasez de historia; fase temprana | Baja | Stress testing futuro | Confiar en datos sintéticos no validados | **Abierta** |
| **Reinforcement Learning** | Modela mejor la tarea real; pero entorno difícil, ruido, y un solo activo dispara el overfitting | Baja-media | Línea muy posterior | Es la configuración de máximo riesgo para nuestro caso | **Abierta** — no en primera etapa |
| **PCA / clustering** | Reducción de dimensionalidad y descubrimiento de estructura | Media | Diagnóstico de redundancia; regímenes | Clusterizar con toda la historia introduce look-ahead | **Abierta** |
| **Vectorized vs event-driven backtest** | El primero es rápido pero incompleto; el segundo impone estructura temporal | **Muy alta** | Estrategia de dos fases | Confundir el rápido con evidencia | Cuál motor usar |
| **Costes, spread, slippage** | Los mercados no permiten ejecutar todo al precio objetivo | **Muy alta** | Viabilidad de la estrategia | En intradiario pueden eliminar el edge completo | Modelo de costes de MNQ |
| **Timing señal→ejecución** | Señal al cierre, ejecución a la apertura siguiente | **Muy alta** | Realismo del backtest | Sesgo directo de resultados | Convención explícita |
| **Mark to market** | Cumplir objetivos en todo momento, no sólo al final | Alta | Métricas de riesgo rolling | Estrategias con drawdowns inaceptables | Ninguna — se adopta |
| **Métricas económicas (pyfolio)** | Sharpe, Sortino, Calmar, drawdown, VaR, tail ratio, turnover | **Muy alta** | Evaluación final | Anualizar Sharpe desde intradiario con autocorrelación | Cuáles son primarias para IRIS |
| **Predicción ≠ rentabilidad** | Alpha 054: IC significativo, retorno acumulado negativo | **Muy alta** | Disciplina de evaluación | Declarar éxito con métricas de ML | Ninguna — es un principio |
| **Ley fundamental (IC × amplitud)** | Importa acertar y apostar a menudo; amplitud difícil de estimar | Alta | Entender el techo de IRIS | La amplitud temporal no equivale a la cross-sectional | Cómo estimar apuestas independientes |
| **SHAP** | Consistente, local y global; explica predicciones individuales | **Alta** | Responder "¿por qué esta señal?" | Features correlacionadas reparten importancia | Ninguna — se adopta |
| **Permutation importance** | Degradación al permutar | Media | Complemento | Rompe la estructura temporal | Con cautela |
| **Partial dependence** | Respuesta esperada marginalizando el resto | Media | Verificar forma de la relación | Engañoso con features correlacionadas | Con cautela |
| **Sharpe bayesiano** | Comparar rendimiento con incertidumbre | Media-alta | No sobreinterpretar diferencias | — | **Abierta** |
| **Monitorización / paper trading** | Parte necesaria del proceso de implementación | Alta | Fase final del proyecto | Saltarse el paso | Ninguna — se planifica |

---

## 24. PREGUNTAS QUE JANSEN NO NOS PERMITE RESPONDER TODAVÍA (Tarea 19)

Organizadas por bloque. Ninguna de estas debe cerrarse en esta etapa.

### 24.1 Sobre el problema

1. ¿Cuál debe ser el objetivo predictivo de IRIS: dirección, retorno, magnitud, volatilidad, evento, probabilidad, o decisión directa?
2. ¿Debe IRIS predecir el mercado, o clasificar situaciones (¿es este un momento operable?), que son problemas distintos?
3. ¿Es el problema principal de IRIS la predicción, o la **selección de momentos** en los que operar?
4. ¿Debe existir una única formulación, o una arquitectura de dos niveles (una decisión de dirección y otra de confianza/tamaño)?
5. ¿Qué significa exactamente "oportunidad operativa" en términos medibles?

### 24.2 Sobre los datos

6. ¿Qué timeframe (o esquema de muestreo) usaremos?
7. ¿Barras temporales, de volumen, de dólar, u otro esquema?
8. ¿Sesión regular, sesión completa Globex, o segmentación por franjas?
9. ¿Cuánto histórico necesitamos, y cuántas observaciones **independientes** contiene?
10. ¿Cómo se ajustan los rollovers de contrato?
11. ¿Podemos o debemos obtener datos de tick/quote más allá de OHLCV?
12. ¿Qué otras series (VIX, otros índices, tipos, macro) tendría sentido incorporar, y cuándo?
13. ¿Qué propiedades estadísticas tiene realmente el MNQ intradiario? (Toda la tabla de §3.9.)

### 24.3 Sobre las features

14. ¿Qué features contienen realmente información sobre MNQ?
15. ¿Contienen señal los indicadores técnicos, o sólo replican información ya presente en retornos rezagados?
16. ¿Cuántas features podemos permitirnos evaluar sin arruinar el presupuesto de multiple testing?
17. ¿Cómo normalizamos features en una serie no estacionaria sin introducir look-ahead?
18. ¿Cómo tratamos el perfil determinista de la sesión: como feature, como algo a eliminar, o como condicionante?
19. ¿Qué ventanas temporales (lookback) son relevantes?
20. ¿Aplicamos denoising? ¿Cuál, y en versión causal?
21. ¿Cómo agrupamos features correlacionadas antes de interpretar importancias?

### 24.4 Sobre el target y el etiquetado

22. ¿Qué horizonte predictivo tiene sentido?
23. ¿Debe el horizonte ser fijo o depender del estado del mercado?
24. ¿Cómo etiquetamos los eventos? — **Jansen no ofrece base para responder.**
25. ¿Los umbrales del target deben escalarse por volatilidad?
26. ¿Cómo se define la etiqueta "no operar"?
27. ¿Cómo manejamos el solapamiento de etiquetas?
28. ¿Debe el target incorporar la trayectoria del precio, no sólo el punto final?

### 24.5 Sobre la validación

29. ¿Qué longitudes de train, validación y test?
30. ¿Ventana expansiva o deslizante?
31. ¿Cómo implementamos purging y embargoing en frecuencia intradiaria?
32. ¿Cuántas observaciones independientes tenemos, y por tanto cuántas hipótesis podemos permitirnos?
33. ¿Cuánto histórico reservamos como hold-out final, y cuándo lo tocamos?
34. ¿Qué criterio de parada aplicamos a la búsqueda de estrategias?
35. ¿Cómo registramos y contabilizamos cada experimento?

### 24.6 Sobre los modelos

36. ¿Qué modelo funcionará mejor? — **No es respondible a priori** (*no free lunch*).
37. ¿Necesitamos Deep Learning? ¿Bajo qué evidencia exacta estaría justificado? (Criterios en §13.3.)
38. ¿Qué baselines exactos constituyen la referencia mínima?
39. ¿Usamos un modelo o un ensemble?
40. ¿Con qué frecuencia hay que reentrenar?
41. ¿Cómo detectamos que el modelo ha dejado de funcionar?

### 24.7 Sobre la traducción a decisiones

42. ¿Qué condiciones deberían generar LONG, SHORT o NO TRADE?
43. ¿Cómo se determina el umbral de decisión, y con qué función de coste?
44. ¿Cómo se cuantifica y calibra la confianza de una señal?
45. ¿Cómo se dimensiona la posición?
46. ¿Hay stop-loss y objetivo de beneficio? ¿Cómo se determinan? — **Jansen no aporta nada.**
47. ¿Cómo se gestiona una posición abierta cuando llega una señal contraria?
48. ¿En qué condiciones debe IRIS abstenerse por completo?
49. ¿Cómo se agrega la información si hay varias señales o varios horizontes?

### 24.8 Sobre la viabilidad económica

50. ¿Existe predictibilidad suficiente en MNQ intradiario para superar los costes?
51. ¿Cuál es el edge mínimo por operación que hace viable la estrategia?
52. ¿Cuáles son los costes reales (comisión, spread, slippage) de operar MNQ a nuestra frecuencia candidata?
53. ¿Cuántas operaciones al día son sostenibles?
54. ¿Cuál es la relación entre frecuencia de operación, edge por operación y coste total?
55. ¿Qué drawdown es aceptable y cómo se controla?

### 24.9 Sobre el marco conceptual

56. ¿Es el IC la métrica correcta para una serie temporal única, o necesitamos otra?
57. ¿Cómo se mide la amplitud (número de apuestas independientes) en un instrumento único?
58. ¿Tiene sentido hablar de alpha y beta cuando el benchmark es el subyacente del propio instrumento?
59. ¿Existen regímenes de mercado identificables en MNQ, y cómo se asignan causalmente?
60. ¿La señal, si existe, está en el primer momento (dirección), en el segundo (volatilidad), o en la condicionalidad al régimen?

---

## 25. CONOCIMIENTO DE JANSEN QUE DEBEMOS CONSERVAR PARA LA PRÓXIMA ETAPA (Tarea 20)

Lo que debe permanecer en memoria al estudiar a **Marcos López de Prado — Advances in Financial Machine Learning**. Sin comparar, sin anticipar sus soluciones: sólo lo que llevamos con nosotros.

### 25.1 Principios que deben sobrevivir a cualquier fuente posterior

1. **El ML es un elemento de un proceso**, no el proceso. Cualquier metodología nueva debe evaluarse por su lugar en la cadena idea → … → validación.
2. **El ratio señal/ruido es bajo.** Toda técnica que aumente la capacidad del modelo aumenta el riesgo, no la promesa.
3. **La prioridad de la hipótesis sobre el resultado.** Las ideas se justifican antes de testearse, no después.
4. **Predicción ≠ rentabilidad.** El caso Alpha 054 debe permanecer como recordatorio permanente.
5. **In-sample ≠ generalización.** El caso 27.3% vs 8.0% debe permanecer igualmente.
6. **El número de pruebas debe registrarse.** Sin él, ningún resultado es interpretable.
7. **No free lunch.** Ningún algoritmo es universalmente superior; la complejidad no es virtud.
8. **Las decisiones se toman con evidencia out-of-sample**, no con intuición ni con autoridad de la fuente.
9. **El objetivo del backtest es rechazar la idea**, no confirmarla.
10. **El decay es real.** Nada de lo que validemos será permanente.

### 25.2 Problemas que Jansen plantea y no resuelve — llevar como preguntas abiertas

Estos son los huecos que definen qué buscar en la siguiente fuente. Se enuncian como **problemas**, no como expectativas de solución.

1. **Etiquetado.** Todos los targets de Jansen son retornos a horizonte fijo que ignoran la trayectoria. ¿Cómo debería etiquetarse un evento de trading?
2. **Solapamiento de etiquetas y unicidad de muestras.** Jansen reconoce que las etiquetas solapadas filtran información y nombra purging y embargoing, pero no los desarrolla. ¿Cómo se implementan correctamente? ¿Cómo se pondera la información redundante?
3. **Número efectivo de observaciones independientes.** Reconoce que los datos no son IID pero no ofrece forma de cuantificar cuántas observaciones independientes hay realmente.
4. **Esquemas de muestreo.** Presenta tick, time, volume y dollar bars y usa sólo temporales. ¿Qué esquema tiene mejores propiedades y por qué?
5. **Validación fuera del walk-forward simple.** Menciona la CV combinatoria como respuesta a que el walk-forward limita severamente los caminos históricos disponibles. ¿Cómo funciona?
6. **Cuantificación del backtest overfitting.** Presenta la longitud mínima de backtest y el deflated Sharpe ratio como resultados; ¿de dónde salen y cómo se aplican rigurosamente?
7. **La decisión de abstención y el dimensionamiento por confianza.** Ninguna formulación del libro los incorpora.
8. **Detección de regímenes y cambios estructurales.** Reconoce el problema; no ofrece método.
9. **Interpretabilidad con features correlacionadas.** Documenta que las métricas discrepan; no explica cómo tratarlo.
10. **Trading de un instrumento único.** No hay un solo caso completo.
11. **Costes de transacción cuantificados.** Los invoca constantemente; casi nunca los modela, y en el único ejemplo intradiario los omite.

### 25.3 Herramientas concretas que llevamos operativas

Estas ya son utilizables y no dependen de fuentes posteriores:

- Kit de diagnóstico de series temporales: descomposición, rolling stats, ACF/PACF, ADF, GARCH.
- Generación de forward returns a múltiples horizontes y selección por IC.
- Evaluación univariante de features: correlación de rangos, mutual information, análisis por quantiles **con dispersión**.
- Evaluación multivariante: feature importance, permutation, partial dependence, SHAP.
- Estructura de validación: splits temporales, tres particiones, hold-out de un solo uso, `MultipleTimeSeriesCV`.
- Diagnósticos: curvas de validación y aprendizaje; optimization verification test.
- Métricas: IC y sus variantes; batería económica completa; deflated Sharpe.
- Catálogo de pitfalls de backtesting como checklist de auditoría.
- Familias de modelos con sus supuestos, ventajas y limitaciones.
- Regularización en todas sus formas.
- Funciones ts_* y catálogo de indicadores como material de construcción.

### 25.4 Lo que NO debemos llevar

- Ninguna conclusión sobre qué modelo funciona.
- Ningún conjunto concreto de features como "validado".
- Ningún horizonte, timeframe ni target como preferido.
- Ninguna cifra de rendimiento como referencia de lo alcanzable.
- La presunción de que el aparato cross-sectional es aplicable.
- La presunción de que el Deep Learning aporta valor en este dominio.

### 25.5 La pregunta central de esta etapa, respondida

> **"¿Qué debemos aprender de Stefan Jansen antes de intentar construir un sistema de IA capaz de extraer señales operativas útiles del mercado intradiario del MNQ?"**

Tres cosas, en orden de importancia:

**Primero, un método para no engañarnos.** El aporte más valioso de Jansen a IRIS no es ninguna técnica de modelado: es el catálogo de formas en que un investigador competente obtiene resultados históricos excelentes y completamente falsos, y el conjunto de disciplinas que reducen ese riesgo. Validación temporal, point-in-time, hold-out de un solo uso, registro de pruebas, corrección por multiple testing, costes realistas, evaluación económica. Esto es transferible en su totalidad y es la base sobre la que debe construirse todo lo demás.

**Segundo, un vocabulario y un instrumental.** Cómo se caracteriza una serie temporal, cómo se construye un dataset supervisado a partir de precios, cómo se evalúa si una variable contiene información, qué familias de modelos existen y qué supuestos hacen, cómo se interpreta un modelo, qué métricas describen una estrategia. Nada de esto decide nada por nosotros, pero sin ello no podríamos ni siquiera formular las preguntas correctamente.

**Tercero, un mapa de lo que falta.** Jansen es una fuente honesta que señala repetidamente los límites de su propio tratamiento y remite explícitamente a López de Prado para los problemas de validación financiera que no desarrolla. El etiquetado, la unicidad de muestras, el muestreo, la abstención, el sizing, los regímenes y el caso del instrumento único quedan abiertos. Saber exactamente qué falta y por qué es, en sí mismo, un resultado de esta etapa.

**Lo que Jansen explícitamente no nos permite concluir:** que exista predictibilidad explotable en MNQ intradiario, que los indicadores técnicos contengan señal, que el Deep Learning aporte valor aquí, que un edge medido estadísticamente sobreviva a los costes, ni que ninguna de sus configuraciones concretas sea un punto de partida privilegiado.

---

## APÉNDICE — REGISTRO DE DECISIONES DELIBERADAMENTE NO TOMADAS

Conforme a las reglas metodológicas del encargo, se deja constancia de que este análisis **no** ha seleccionado:

- ni el target, ni el horizonte predictivo, ni el timeframe, ni el esquema de muestreo;
- ni las features, ni el sistema de etiquetado, ni el esquema de cross-validation concreto;
- ni la familia de modelos, ni la arquitectura, ni los baselines definitivos;
- ni la regla operativa, ni el criterio LONG/SHORT/NO TRADE, ni el método de sizing;
- ni el pipeline, ni la arquitectura del sistema.

Todas estas decisiones permanecen abiertas hasta después de:

```
JANSEN  (completado)
   +
LÓPEZ DE PRADO
   +
MURPHY
        ↓
KNOWLEDGE SYNTHESIS
        ↓
ANÁLISIS DE NUESTROS DATOS REALES DE MNQ
        ↓
DISEÑO METODOLÓGICO DE IRIS
```

**Fin del documento — IRIS PROJECT KNOWLEDGE BASE 01.**
