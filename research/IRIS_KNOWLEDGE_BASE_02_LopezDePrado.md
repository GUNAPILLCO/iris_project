# IRIS PROJECT — KNOWLEDGE BASE 02
## Advances in Financial Machine Learning — Marcos López de Prado (Wiley, 2018)

**Estado:** memoria técnica permanente del proyecto.
**Etapa:** 2 de 3 (Jansen ✔ → **López de Prado** → Murphy → Knowledge Synthesis).
**Regla de esta etapa:** no se diseña IRIS. Se identifican problemas, se comprenden métodos, se filtra por disponibilidad de datos, se documentan limitaciones y se mantienen abiertas las decisiones.

---

## 0. CÓMO LEER ESTE DOCUMENTO

### 0.1 Convenciones de atribución

| Etiqueta | Significado |
|---|---|
| `[LDP]` | Afirmación que el libro sostiene explícitamente. |
| `[INTERPRETACIÓN]` | Inferencia propia a partir del libro. No aparece así en el texto. |
| `[IMPLICACIÓN PARA IRIS]` | Consecuencia potencial para el proyecto. No es una decisión. |
| `[CONOCIMIENTO EXTERNO AL LIBRO]` | Observación que NO proviene de esta fuente. Uso deliberadamente escaso. |
| `[VACÍO]` | Problema que el libro no cubre, o cubre de forma insuficiente para nuestro caso. |

Todo el contenido está reformulado con palabras propias.

### 0.2 Filtro de datos — el criterio transversal de este análisis

Toda metodología se clasifica según lo que **realmente** requiere. Nuestra fuente es una sola: `Timestamp, Open, High, Low, Close, Volume` del MNQ.

| Código | Significado |
|---|---|
| **`OHLCV-OK`** | Construible directamente desde Timestamp + OHLCV. |
| **`OHLCV-COND`** | Aproximable o parcialmente construible, bajo supuestos explícitos o con pérdida de precisión. La condición se declara siempre. |
| **`GRANULAR`** | Requiere trades individuales, ticks, bid/ask o aggressor side. **No lo tenemos.** |
| **`OTRAS FUENTES`** | Requiere otros activos, portfolios, order book, fundamentales, opciones. **Fuera de alcance.** |
| **`NO RELEVANTE`** | Técnicamente interesante, pero no responde a nuestro problema actual. |

Regla estricta aplicada: **no se fuerza artificialmente una técnica para hacerla compatible con OHLCV.** Cuando una técnica necesita información que no tenemos, se declara así sin rodeos.

### 0.3 Mapa Tarea → Sección

| Tarea | Sección |
|---|---|
| T1 Filosofía | §1 |
| T2 Mapa del libro | §2 |
| T3 Estructuras de datos / sampling / futuros | §3, §4, §5 |
| T4 Labeling | §6 |
| T5 Meta-labeling y no-trade | §7 |
| T6 Sample weights y solapamiento | §8 |
| T7 Fractional differentiation | §9 |
| T8 Ensembles | §10 |
| T9 Cross-validation | §11 |
| T10 Feature importance | §12 |
| T11 Hyper-parameter tuning | §13 |
| T12 Bet sizing | §14 |
| T13 Dangers of backtesting | §15 |
| T14 CPCV | §16 |
| T15 Datos sintéticos | §17 |
| T16 Backtest statistics | §18 |
| T17 Strategy risk | §19 |
| T18 Asset allocation | §20 |
| T19 Structural breaks | §21 |
| T20 Entropy | §22 |
| T21 Microstructural | §23 |
| T22 HPC | §24 |
| T23 LdP aplicado a IRIS (A/B/C/D) | §25 |
| T24 Mínima complejidad | §26 |
| T25 Preguntas de Jansen respondidas | §27 |
| T32 Limitaciones | §28 |
| T27 Matriz maestra | §29 |
| T28 Preguntas abiertas | §30 |
| T29 Qué llevar a Murphy | §31 |

### 0.4 Advertencia estructural previa (leer antes que nada)

`[INTERPRETACIÓN]` Este libro presenta **dos tensiones directas con el diseño declarado de IRIS**, y conviene tenerlas presentes desde la primera página en lugar de descubrirlas al final:

**Tensión 1 — el instrumento único.** Entre las recomendaciones explícitas de López de Prado contra el backtest overfitting, la primera es desarrollar modelos para **clases de activos o universos completos, no para valores individuales**, con el argumento de que si un patrón aparece sólo en el activo Y, por rentable que parezca, es probablemente un falso descubrimiento. Además prefiere sistemáticamente el *features stacking* (apilar datasets de muchos instrumentos) precisamente para reducir el riesgo de sobreajustar a un instrumento concreto. IRIS es, por diseño, un sistema de un solo instrumento.

**Tensión 2 — la escala industrial.** El libro está escrito explícitamente como manual de investigación **para equipos**, no para individuos, y su tesis central es que el fracaso en ML financiero proviene de pedir a una persona que haga sola todo el trabajo. Sostiene además que el alfa "macroscópico" accesible con herramientas simples ha desaparecido y que lo que queda requiere métodos industriales intensivos en capital.

Ninguna de las dos tensiones invalida el libro para IRIS. Pero significan que **debemos extraer los principios metodológicos y separarlos tanto de la escala organizativa como del supuesto multiactivo**. Este documento marca esa frontera sistemáticamente y la desarrolla en §28.

---

## 1. FILOSOFÍA DE FINANCIAL MACHINE LEARNING (Tarea 1)

### 1.1 Por qué el ML financiero es una disciplina distinta

`[LDP]` La tesis fundacional: el ML financiero es un tema con entidad propia, relacionado con el ML estándar pero **separado** de él. La razón no es que los algoritmos sean distintos —el libro es deliberadamente agnóstico respecto al algoritmo—, sino que existe un conjunto de **problemas genéricos compartidos** que aparecen en finanzas y que las soluciones importadas de otros dominios no resuelven: estructuración de datos, etiquetado, ponderación, transformaciones estacionarias, cross-validation, selección e importancia de features, overfitting y backtesting.

`[LDP]` Su pronóstico explícito: las firmas que inviertan usando algoritmos de ML "de estantería", importados directamente de la academia o de Silicon Valley, **perderán dinero** frente a soluciones de ML mejor adaptadas. Superar a la sabiduría del mercado es más difícil que reconocer caras o conducir coches.

`[LDP]` Los agravantes específicos del dominio, que menciona repetidamente:
- **Ratio señal/ruido bajo**, consecuencia de las fuerzas de arbitraje.
- **Series cortas** comparadas con los datasets de imagen o texto a escala web.
- **Ausencia de laboratorio**: no podemos repetir experimentos controlando las variables del entorno. Un backtest es una hipótesis, no un experimento; no demuestra nada.
- **Flexibilidad del ML como arma de doble filo**: si el overfitting ya es un problema en análisis econométrico, la flexibilidad del ML lo convierte en una amenaza constante.

### 1.2 Por qué fracasan los proyectos de Financial ML: el paradigma de Sísifo

`[LDP]` Identifica **un error crítico que subyace a todos los fracasos** que ha observado en dos décadas.

**El paradigma de Sísifo.** Los gestores discrecionales no siguen una teoría particular; consumen noticias y análisis, pero se apoyan principalmente en juicio o intuición, y racionalizan sus decisiones con alguna historia (siempre hay una historia para cada decisión). Como nadie entiende del todo la lógica de sus apuestas, las firmas les hacen trabajar aisladamente, en silos, para asegurar diversificación. Ese esquema funciona (a veces) para discrecionales.

`[LDP]` El desastre ocurre cuando ese mismo esquema se traslada a proyectos cuantitativos: contratar 50 doctores y exigir a cada uno una estrategia de inversión en seis meses. El resultado es siempre uno de dos: **(1) un falso positivo que luce espléndido en un backtest sobreajustado, o (2) factor investing estándar**, una estrategia sobrepoblada de Sharpe bajo pero con respaldo académico. Ambos decepcionan, y el proyecto se cancela.

`[LDP]` La metáfora: pedir a un investigador que produzca una estrategia entera por su cuenta es como pedir a un operario de una fábrica de coches que construya un coche completo usando todos los talleres a su alrededor —una semana soldador, otra electricista, otra ingeniero mecánico, otra pintor— y volver a empezar.

### 1.3 El paradigma de meta-estrategia y la "research factory"

`[LDP]` La alternativa: **producir una estrategia verdadera cuesta casi lo mismo que producir cien**. Toda firma cuantitativa exitosa que conoce aplica el paradigma de meta-estrategia: montar una **fábrica de investigación** con estaciones especializadas en una cadena de producción, donde cada investigador se especializa en una tarea, llega a ser el mejor en ella, y mantiene visión holística del proceso completo. Los descubrimientos salen a ritmo predecible, sin depender de golpes de suerte. El modelo de referencia que cita son los laboratorios nacionales de EE. UU.

`[LDP]` **El dinero no está en fabricar un coche, está en fabricar la fábrica de coches.** Los aficionados desarrollan estrategias individuales creyendo que existe una fórmula mágica; los profesionales desarrollan métodos para producir estrategias en serie.

### 1.4 Las estaciones de la cadena de producción

`[LDP]` La separación funcional que propone, y que es lo que aquí importa:

| Estación | Responsabilidad | Capítulos |
|---|---|---|
| **Data Curators** | Recolectar, limpiar, indexar, almacenar, **ajustar** y entregar datos. Expertos en microestructura y protocolos. Cada clase de activo tiene sus particularidades: los bonos se intercambian y amortizan, las acciones sufren splits, **los futuros y opciones deben rolarse**, las divisas no cotizan en libro centralizado. | 1 |
| **Feature Analysts** | Transformar datos crudos en **señales informativas** con poder predictivo. Expertos en teoría de la información, extracción de señal, visualización, etiquetado, ponderación, clasificadores e importancia de features. **Error común: creer que los analistas de features desarrollan estrategias.** No lo hacen: recolectan y catalogan bibliotecas de hallazgos utilizables por múltiples estaciones. | 2–9, 17–19 |
| **Strategists** | Transformar features informativas en algoritmos de inversión. Recorren las bibliotecas de features buscando ideas y **formulan una teoría general que las explique**. La estrategia es el experimento diseñado para testear la validez de esa teoría. **Una teoría debe identificar el mecanismo económico que causa que un agente nos pierda dinero: ¿sesgo conductual? ¿información asimétrica? ¿restricción regulatoria?** Las features pueden ser descubiertas por una caja negra, pero **la estrategia se desarrolla en una caja blanca**. Pegar features catalogadas no constituye una teoría. | 10, 16 |
| **Backtesters** | Evaluar la rentabilidad bajo varios escenarios. Un buen backtester incorpora **meta-información sobre cómo surgió la estrategia**: su análisis debe evaluar la probabilidad de backtest overfitting teniendo en cuenta **el número de intentos que hicieron falta para destilarla**. Sus resultados **no se reutilizan por otras estaciones**: se comunican a la dirección y no se comparten con nadie más. | 11–16 |
| **Deployment** | Integrar en producción, garantizando que lo desplegado es lógicamente idéntico al prototipo, y minimizando latencia. | 20–22 |
| **Portfolio Oversight** | El ciclo de vida: **embargo** (correr sobre datos posteriores al fin del backtest), **paper trading** (feed real, midiendo latencias y retardos), **graduación** (posición real), **reasignación** (asignación cóncava: pequeña al inicio, crece, y decae con el tiempo) y **desmantelamiento** (cuando el rendimiento cae por debajo de expectativas durante suficiente tiempo como para concluir que la teoría ya no está respaldada por la evidencia). | — |

### 1.5 Feature discovery vs strategy discovery — la distinción central

Esta separación es, en mi lectura, **el aporte filosófico más valioso del libro para IRIS**.

`[LDP]`
- **Descubrimiento de features** es investigación: pregunta *qué información predice qué*, se deriva **ex-ante**, y sus hallazgos pueden usarse de múltiples maneras (ejecución, monitorización de liquidez, market making, toma de posiciones).
- **Descubrimiento de estrategia** es *ingeniería sobre una teoría*: toma un conjunto de features informativas y formula una explicación causal que las una.
- **Un backtest no es ninguna de las dos cosas.** Es una comprobación de sanidad sobre variables como el bet sizing, el turnover, la resistencia a costes, y el comportamiento bajo un escenario dado.

`[LDP]` Consecuencias explícitas:
- Que unas features sean muy importantes **no implica** que puedan monetizarse en una estrategia.
- A la inversa, **abundan las estrategias que parecerán rentables aun estando basadas en features irrelevantes**.
- El propósito de un backtest es **descartar modelos malos, no mejorarlos**. Ajustar el modelo en función de los resultados del backtest es una pérdida de tiempo, y es peligroso.
- **Nunca hacer backtest hasta que el modelo esté completamente especificado.** Si el backtest falla, empezar de nuevo desde cero.

`[LDP]` Las tres "leyes" que enuncia (parafraseadas):
1. **El backtesting no es una herramienta de investigación; la importancia de features sí lo es.**
2. **Investigar bajo la influencia de un backtest es como conducir bebido.**
3. **Todo resultado de backtest debe reportarse junto con todos los intentos involucrados en producirlo**; sin esa información es imposible evaluar su probabilidad de falso descubrimiento.

`[LDP]` Y el dato cuantitativo que da la urgencia: típicamente hacen falta **unas 20 iteraciones** de ese ciclo (probar datos → ML → backtest → repetir) para "descubrir" una estrategia falsa al nivel de significación estándar del 5%.

### 1.6 El papel del overfitting

`[LDP]` Va más allá de lo técnico: **el overfitting es poco ético**. Produce resultados prometedores que no pueden entregarse. Hecho a sabiendas, es fraude científico. El hecho de que muchos académicos lo hagan no lo justifica: ellos no arriesgan el patrimonio de nadie, ni siquiera el propio. Y es además un desperdicio de tiempo, recursos y oportunidades, porque la industria sólo paga por retornos fuera de muestra.

`[LDP]` El backtest overfitting es, en su opinión, **el problema abierto más importante de toda la matemática financiera** —el equivalente de "P vs NP" en informática—. Si existiera un método preciso para prevenirlo, un backtest sería casi tan bueno como efectivo.

`[LDP]` Su regla operativa personal: hagas lo que hagas, **pregúntate siempre de qué manera podrías estar sobreajustando**; sé escéptico de tu propio trabajo y desafíate constantemente a demostrar que estás aportando valor.

### 1.7 El papel de la hipótesis económica

`[LDP]` Los métodos de ML financiero **no reemplazan la teoría: la guían**. Un algoritmo aprende patrones en un espacio de alta dimensión sin ser dirigido específicamente. Una vez entendemos qué features predicen un fenómeno, **podemos construir una explicación teórica, que después debe testearse sobre un dataset independiente**.

`[LDP]` Y en la estación de estrategas, la exigencia es concreta: la teoría debe identificar **el mecanismo económico por el que un agente nos pierde dinero**.

`[INTERPRETACIÓN]` Nótese la asimetría respecto a lo que muchos esperan: LdP **no** exige una hipótesis económica antes de buscar features (las features pueden descubrirse en caja negra). Exige la hipótesis económica **entre el descubrimiento de features y la construcción de la estrategia**. El orden es: descubrir → explicar → testear la explicación.

### 1.8 Cómo entiende el descubrimiento científico

`[LDP]` Aboga por **matemática experimental**: resolver problemas difíciles e intratables no mediante demostración sino mediante experimento. No hay demostración matemática para el éxito inversor; hay que apoyarse en métodos experimentales para dirigir la investigación. Un algoritmo óptimo dentro de muestra puede comportarse pésimamente fuera de muestra.

`[LDP]` Su crítica a la econometría: su herramienta esencial es la regresión lineal multivariante, tecnología del siglo XVIII. Los modelos econométricos estándar **no aprenden**. Si la caja de herramientas estadística es la regresión lineal, el investigador no reconocerá la complejidad de los datos y las teorías serán simplistas e inútiles.

### 1.9 Qué principios de esta filosofía son relevantes para IRIS

Extrayendo el **principio** y descartando la **escala organizativa**, como pide el encargo:

| Principio | Traducción a un proyecto pequeño |
|---|---|
| **Separación de estaciones** | No es una plantilla; es una **separación de fases con reglas de higiene entre ellas**. La curación de datos, el análisis de features, la formulación de la teoría y el backtest son fases distintas con criterios de éxito distintos, y **la información no debe fluir hacia atrás** (los resultados del backtest no deben modificar el diseño de features). |
| **Feature importance como herramienta de investigación** | Directamente adoptable y probablemente el cambio de método más importante que aporta esta fuente: investigar mirando qué features informan, no mirando qué combinación produce una curva bonita. |
| **La teoría entre features y estrategia** | Antes de construir la estrategia de IRIS, deberíamos poder responder: ¿qué mecanismo del mercado hace que exista esta señal? ¿quién está al otro lado y por qué pierde? |
| **Contabilizar todos los intentos** | Un registro de experimentos desde el día uno. En un proyecto pequeño es **más** factible que en uno grande, no menos. |
| **Nunca hacer backtest hasta que el modelo esté especificado** | Adoptable literalmente, y es una restricción de proceso, no de recursos. |
| **El ciclo de vida (embargo → paper → graduación → decaimiento → retirada)** | Adoptable a escala reducida: define qué hacer *después* de que el backtest salga bien, que es donde la mayoría de proyectos individuales no tiene plan. |
| **Escepticismo institucionalizado** | Preguntarse sistemáticamente por dónde estamos sobreajustando. |

`[IMPLICACIÓN PARA IRIS]` Lo que **no** debemos importar: la premisa de que hace falta una fábrica, un supercomputador o un universo multiactivo para hacer algo válido. Lo que el libro demuestra realmente es que **sin las salvaguardas metodológicas el resultado es ruido**; las salvaguardas son mayoritariamente cuestión de disciplina, no de presupuesto.

---

## 2. MAPA COMPLETO DEL LIBRO (Tarea 2)

Clasificación: **A** crítico · **B** importante · **C** complementario · **D** poco relevante ahora.

---

### Capítulo 1 — Financial ML as a Distinct Subject — **A**

1. **Problema:** por qué fracasan los proyectos de ML financiero.
2. **Metodología:** paradigma de meta-estrategia; separación en estaciones; tabla de errores comunes con su solución y capítulo correspondiente.
3. **Supuestos:** que existe una organización con varios investigadores.
4. **Conservar:** todo lo de §1. Especialmente la distinción feature discovery / strategy discovery, y la tabla de pitfalls como índice del libro.
5. **Relación con IRIS:** define el proceso y la disciplina.
6. **OHLCV:** no aplica (no es una técnica).
7. **Datos:** ninguno.
8-9. **Implementable / no implementable:** la disciplina sí; la escala organizativa no.
10. **Riesgos:** confundir "principio" con "escala"; concluir que un proyecto individual es inviable.
11. **A.** 12. Es el marco que da sentido a todo lo demás.

---

### Capítulo 2 — Financial Data Structures — **A**

1. **Problema:** cómo pasar de datos crudos a una tabla apta para ML, y cómo muestrear.
2. **Metodología:** tipos de datos financieros; barras estándar (tiempo, tick, volumen, dólar); barras dirigidas por información (imbalance y runs, en versiones tick/volumen/dólar); ETF trick; pesos PCA; **single future roll**; muestreo para reducción y **muestreo basado en eventos (filtro CUSUM)**.
3. **Supuestos:** disponibilidad de datos tick con precio y volumen por operación; para las barras de información, además la regla del tick.
4. **Conservar:** la crítica al muestreo cronológico; la jerarquía de propiedades estadísticas entre tipos de barra; el tratamiento del roll de futuros; el CUSUM como filtro de eventos.
5. **IRIS:** determina el esquema de muestreo y el tratamiento del MNQ como futuro.
6-7. **OHLCV:** mixto — ver §3, §4, §5 con detalle.
8. **Implementable:** roll (con contrato identificado), CUSUM, aproximación de barras de volumen/dólar por agregación de barras base.
9. **No implementable:** barras de tick auténticas, barras de imbalance y de runs (requieren firmar cada operación).
10. **Riesgos:** aproximar barras de volumen desde barras temporales y creer que son equivalentes; no ajustar rolls.
11. **A.** 12. Es la capa sobre la que se construye todo el resto.

---

### Capítulo 3 — Labeling — **A**

1. **Problema:** cómo etiquetar observaciones financieras.
2. **Metodología:** crítica al método de horizonte fijo; umbrales dinámicos escalados por volatilidad; **método de la triple barrera**; aprendizaje de side y size; **meta-labeling**; eliminación de etiquetas innecesarias.
3. **Supuestos:** que existe un estimador razonable de volatilidad; que la trayectoria del precio importa; que existen límites de stop-loss explícitos o implícitos.
4. **Conservar:** el capítulo entero. Es la aportación más directamente utilizable del libro para IRIS.
5. **IRIS:** responde a la pregunta que Jansen dejó abierta.
6. **OHLCV:** **`OHLCV-OK`** en su implementación de referencia (usa serie de cierres). Ver §6 para el matiz sobre High/Low.
7. **Datos:** serie de precios y una estimación de volatilidad derivable de ella.
8-9. Todo implementable.
10. **Riesgos:** asumir que triple barrera es automáticamente superior sin comparar; ambigüedad intrabar si se usan High/Low.
11. **A.** 12. Resuelve un vacío estructural de nuestra base anterior.

---

### Capítulo 4 — Sample Weights — **A**

1. **Problema:** las observaciones financieras no son IID por solapamiento de etiquetas.
2. **Metodología:** concurrencia; unicidad media; **sequential bootstrap**; atribución de retornos; **time decay**; class weights.
3. **Supuestos:** que cada observación tiene un intervalo `[t0, t1]` bien definido (lo cual exige un método de etiquetado con horizonte, como la triple barrera).
4. **Conservar:** todo. La formalización del problema es lo más valioso.
5. **IRIS:** crítico si trabajamos intradiario con horizontes que abarcan muchas barras.
6. **OHLCV:** **`OHLCV-OK`** — sólo requiere el objeto `t1`, que ya generamos al etiquetar.
7. **Datos:** ninguno adicional.
8-9. Todo implementable.
10. **Riesgos:** coste computacional del sequential bootstrap; olvidar que estos pesos usan información futura y por tanto sólo pueden aplicarse al entrenamiento.
11. **A.** 12. Sin esto, el número efectivo de observaciones de IRIS será una fracción desconocida del número de filas.

---

### Capítulo 5 — Fractionally Differentiated Features — **B**

1. **Problema:** el dilema estacionariedad vs memoria.
2. **Metodología:** operador de diferenciación fraccionaria; estimación iterativa de pesos; ventana expansiva; **FFD (ventana de ancho fijo)**; búsqueda del `d` mínimo que pasa el ADF.
3. **Supuestos:** que la memoria de la serie de precios contiene información predictiva; que la estacionariedad es necesaria para que el modelo pueda mapear observaciones nuevas a ejemplos conocidos.
4. **Conservar:** el planteamiento del dilema y el procedimiento de calibración de `d`. La evidencia empírica sobre 87 futuros.
5. **IRIS:** candidato a transformación de features de precio.
6. **OHLCV:** **`OHLCV-OK`**.
7. **Datos:** serie de precios.
8-9. Todo implementable.
10. **Riesgos:** aplicarlo automáticamente sin comprobar si aporta sobre retornos simples; la ventana expansiva introduce deriva negativa; coste computacional.
11. **B.** 12. Puede aportar mucho, pero **debe demostrar información incremental**, no adoptarse por defecto.

---

### Capítulo 6 — Ensemble Methods — **B**

1. **Problema:** cómo reducir error; y por qué bagging falla con observaciones redundantes.
2. **Metodología:** descomposición sesgo/varianza/ruido; bagging y su fórmula de reducción de varianza; Random Forest; boosting; comparación en finanzas; bagging para escalabilidad.
3. **Supuestos:** para que el bagging reduzca varianza, la correlación media entre predicciones debe ser < 1.
4. **Conservar:** la fórmula de varianza del bagging y su implicación; las tres formas de configurar un RF corrigiendo el problema de redundancia; el argumento a favor de bagging sobre boosting en finanzas.
5. **IRIS:** determina cómo configurar cualquier ensemble que usemos.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** confiar en la precisión out-of-bag, que estará inflada.
11. **B.** 12. No decide el modelo, pero condiciona cómo se configura.

---

### Capítulo 7 — Cross-Validation in Finance — **A**

1. **Problema:** por qué el k-fold estándar falla en finanzas.
2. **Metodología:** **purging** y **embargo**; clase `PurgedKFold`.
3. **Supuestos:** que las etiquetas tienen un intervalo `[t0, t1]` conocido.
4. **Conservar:** todo. Es material de higiene experimental no negociable.
5. **IRIS:** define nuestro esquema de validación.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** implementar mal el purging (el error típico: que `t1.index` caiga en train y `t1.values` en test).
11. **A.** 12. Sin esto, cualquier métrica de IRIS será ficción.

---

### Capítulo 8 — Feature Importance — **A**

1. **Problema:** investigar sin usar el backtest; y los efectos de sustitución entre features correlacionadas.
2. **Metodología:** **MDI** (in-sample, específica de árboles), **MDA** (out-of-sample, con purged CV), **SFI** (una feature aislada); ortogonalización por PCA; comparación entre importancia y ranking PCA mediante Kendall tau ponderado; paralelizada vs apilada.
3. **Supuestos:** MDI requiere clasificadores basados en árboles; la ortogonalización sólo mitiga sustituciones **lineales**.
4. **Conservar:** todo, y muy especialmente el concepto de efecto de sustitución y el uso de PCA como **evidencia confirmatoria no supervisada** de que el patrón no está enteramente sobreajustado.
5. **IRIS:** directamente central, porque nuestro espacio de features de indicadores técnicos será extremadamente redundante.
6. **OHLCV:** **`OHLCV-OK`**.
9. **No implementable:** la variante "paralelizada" (importancia por instrumento y agregación) requiere universo; el *features stacking* también.
10. **Riesgos:** interpretar importancias sin considerar sustituciones; usar MDI sola.
11. **A.** 12. Es la herramienta de investigación que sustituye al backtest.

---

### Capítulo 9 — Hyper-Parameter Tuning with CV — **B**

1. **Problema:** tunear sin reintroducir leakage ni sobreajustar hiperparámetros.
2. **Metodología:** grid search y randomized search **con `PurgedKFold`**; distribución log-uniforme; elección de función de scoring.
3. **Supuestos:** que el purged CV está correctamente implementado.
4. **Conservar:** el criterio de scoring (ver §13), la distribución log-uniforme, y el hecho de que el tuning **contribuye al overfitting a través de la propia CV**.
5. **IRIS:** define cómo tunear sin engañarnos.
6. **OHLCV:** **`OHLCV-OK`**.
11. **B.** 12. Necesario, pero es refinamiento del capítulo 7.

---

### Capítulo 10 — Bet Sizing — **A**

1. **Problema:** convertir predicciones en tamaño de posición, incluido el tamaño cero.
2. **Metodología:** sizing independiente de la estrategia (mezcla de gaussianas sobre concurrencia; enfoque de presupuesto); **sizing desde probabilidades predichas** vía estadístico z; promediado de apuestas activas; discretización; tamaños dinámicos y precios límite con función sigmoide.
3. **Supuestos:** que el clasificador produce probabilidades utilizables.
4. **Conservar:** todo, especialmente la derivación desde probabilidad y el promediado/discretización como control de turnover.
5. **IRIS:** responde a "¿qué nivel de confianza tiene la señal?" y a la abstención.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** probabilidades mal calibradas; sobretrading si no se discretiza.
11. **A.** 12. Es el eslabón que conecta predicción con decisión operativa, y estaba vacío en nuestra base anterior.

---

### Capítulo 11 — The Dangers of Backtesting — **A**

1. **Problema:** por qué casi todos los backtests están mal.
2. **Metodología:** catálogo de los "siete pecados"; argumento de que incluso un backtest impecable probablemente esté equivocado; seis recomendaciones generales; **CSCV** para estimar la probabilidad de backtest overfitting (PBO).
3. **Supuestos:** para CSCV, disponer de una matriz de PnL de N configuraciones probadas sobre T observaciones sincronizadas.
4. **Conservar:** todo el capítulo.
5. **IRIS:** es nuestro protocolo de honestidad.
6. **OHLCV:** **`OHLCV-OK`** (CSCV opera sobre resultados, no sobre datos de mercado).
10. **Riesgos:** ninguno metodológico; el riesgo es no aplicarlo.
11. **A.** 12. Es la sección que más protege a IRIS de sí mismo.

---

### Capítulo 12 — Backtesting through Cross-Validation — **A**

1. **Problema:** el walk-forward testea un único camino y es fácil de sobreajustar.
2. **Metodología:** WF y sus tres desventajas; CV backtesting; **CPCV** (combinatorial purged cross-validation), con la fórmula del número de caminos.
3. **Supuestos:** purging y embargo correctamente aplicados; el CV backtesting acepta explícitamente que el entrenamiento no precede al test.
4. **Conservar:** todo. Especialmente la crítica al WF y la idea de obtener una **distribución** de Sharpe en lugar de un número.
5. **IRIS:** candidato serio a esquema de validación final.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** coste computacional; y la ausencia de interpretación histórica clara.
11. **A.** 12. Cambia cualitativamente qué evidencia podemos obtener.

---

### Capítulo 13 — Backtesting on Synthetic Data — **C**

1. **Problema:** calibrar las reglas de salida (profit-taking y stop-loss) sin sobreajustar a la historia.
2. **Metodología:** caracterizar el proceso estocástico que genera los retornos (proceso tipo Ornstein-Uhlenbeck) y **derivar los parámetros óptimos de la regla de trading directamente del proceso**, en lugar de mediante simulación histórica; malla de escenarios.
3. **Supuestos:** que el proceso generador puede caracterizarse razonablemente; el capítulo asume que **la posición ya existe** y la pregunta es cómo salir de ella óptimamente.
4. **Conservar:** la motivación (evitar el riesgo de overfitting en la calibración de la regla) y la distinción entre "cuándo entrar" y "cómo salir".
5. **IRIS:** relevante si IRIS acaba usando barreras, porque calibrar `[PT, SL]` sobre el histórico es exactamente el tipo de sobreajuste trivial que describe.
6. **OHLCV:** **`OHLCV-OK`** en principio, pero requiere ajustar un modelo estocástico a nuestros datos.
10. **Riesgos:** el modelo sintético puede no representar bien la dinámica real; añade una capa de supuestos.
11. **C.** 12. Valioso pero no necesario para una primera versión.

---

### Capítulo 14 — Backtest Statistics — **A**

1. **Problema:** qué reportar y cómo evitar métricas infladas.
2. **Metodología:** características generales (rango temporal, AUM, capacidad, apalancamiento, ratio de largos, **frecuencia de apuestas**, **holding period medio**, turnover); rendimiento (PnL, TWRR, **hit ratio**, retorno medio de aciertos y de fallos); **runs** (concentración HHI de retornos positivos, negativos y temporal; **drawdown y time under water**); **implementation shortfall**; eficiencia (**Sharpe, PSR, DSR**); **classification scores**; atribución.
3. **Supuestos:** el Sharpe asume retornos IID gaussianos; PSR y DSR corrigen esa suposición.
4. **Conservar:** todo. Especialmente la distinción bet ≠ trade, y PSR/DSR.
5. **IRIS:** define el reporte final.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** anualizar Sharpe con la raíz cuadrada asumiendo IID.
11. **A.** 12. Sin estas métricas no podremos juzgar si IRIS funciona.

---

### Capítulo 15 — Understanding Strategy Risk — **A**

1. **Problema:** distinguir riesgo de cartera de **riesgo de estrategia**.
2. **Metodología:** modelado binomial de resultados; fórmula del Sharpe en función de precisión y frecuencia para pagos simétricos y **asimétricos**; precisión implícita; frecuencia implícita; **probabilidad de fracaso de la estrategia** vía bootstrap de la precisión.
3. **Supuestos:** apuestas IID; que la estrategia tiene salidas por profit-taking y stop-loss (explícitas o implícitas).
4. **Conservar:** todo, y las cifras concretas del ejemplo.
5. **IRIS:** **crítico** si adoptamos barreras asimétricas. Permite calcular, antes de modelar, qué precisión y qué frecuencia hacen viable un esquema `[PT, SL]` dado.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** el supuesto IID de las apuestas es fuerte.
11. **A.** 12. Es una herramienta de **viabilidad previa**: nos dice si un diseño puede funcionar antes de gastar meses entrenando.

---

### Capítulo 16 — Machine Learning Asset Allocation — **D**

1. **Problema:** inestabilidad, concentración e infrarrendimiento de los optimizadores convexos de cartera.
2. **Metodología:** la maldición de Markowitz (número de condición de la matriz de covarianzas); paso de relaciones geométricas a jerárquicas; **HRP** (tree clustering, cuasi-diagonalización, bisección recursiva).
3. **Supuestos:** múltiples activos con matriz de covarianzas.
4. **Conservar:** el principio general de que **estructura jerárquica > inversión de matriz** cuando hay multicolinealidad, y la idea de que una solución óptima in-sample puede ser mala out-of-sample.
5. **IRIS:** no aplicable a un instrumento único. Aplicable en el futuro sólo si asignamos capital **entre varias estrategias/modelos** de IRIS.
6. **OHLCV / datos:** **`OTRAS FUENTES`**.
11. **D.** 12. No forzar HRP dentro de IRIS, como indica el encargo.

---

### Capítulo 17 — Structural Breaks — **B**

1. **Problema:** detectar transiciones de régimen, que ofrecen buenas relaciones riesgo/recompensa.
2. **Metodología:** tests CUSUM (Brown-Durbin-Evans sobre residuos recursivos; **Chu-Stinchcombe-White sobre niveles**); tests de explosividad (Chow-type Dickey-Fuller; **SADF**; QADF/CADF; **tests sub/super-martingala** con penalización por longitud muestral).
3. **Supuestos:** el uso de log-precios (no precios crudos) es explícitamente preferible; SADF asume que se prueban todos los puntos de inicio.
4. **Conservar:** el racional económico (los participantes atrapados en el lado perdedor actúan irracionalmente antes de aceptar pérdidas); Chu-Stinchcombe-White y SADF como features; el parámetro φ de los tests SM como **forma natural de ajustar la señal al horizonte de tenencia buscado**.
5. **IRIS:** responde a "¿el mercado se está comportando de forma distinta?" y a "¿sigue siendo válida la relación aprendida?".
6. **OHLCV:** **`OHLCV-OK`** para Chu-Stinchcombe-White, SADF, QADF y los tests SM (sólo requieren la serie de precios). Brown-Durbin-Evans requiere además una matriz de features y un target, que sí tendríamos.
10. **Riesgos:** **coste computacional cuadrático** — ver §21; y la fragilidad del supremo como estadístico.
11. **B.** 12. Muy pertinente conceptualmente, con un obstáculo computacional real en frecuencia intradiaria.

---

### Capítulo 18 — Entropy Features — **C**

1. **Problema:** cuantificar el contenido informativo de una serie de precios.
2. **Metodología:** entropía de Shannon; estimador plug-in; estimadores Lempel-Ziv (Kontoyiannis); **esquemas de codificación** (binaria, por cuantiles, sigma); entropía de un proceso gaussiano; media generalizada; aplicaciones financieras.
3. **Supuestos:** estacionariedad y ergodicidad; convergencia asintótica (no monotonía); ventana de emparejamiento simétrica.
4. **Conservar:** la hipótesis de trabajo que propone —que las apuestas de momentum pueden ser más rentables cuando los precios llevan poca información y las de reversión cuando llevan mucha—; la conexión entropía↔volatilidad implícita; la recomendación de codificar sobre series **fraccionalmente** diferenciadas.
5. **IRIS:** familia de features candidata, derivable sólo de precios.
6. **OHLCV:** **`OHLCV-OK`**.
10. **Riesgos:** sensible al esquema de codificación, al tamaño del alfabeto y a la longitud del mensaje; con alfabetos pequeños se descarta información y se subestima la entropía.
11. **C.** 12. Prometedor y barato en datos, pero sin evidencia de utilidad en el libro.

---

### Capítulo 19 — Microstructural Features — **C (parcial) / D (mayoritariamente)**

1. **Problema:** extraer información de la mecánica del proceso de subasta.
2. **Metodología:** tres generaciones — precios (regla del tick, modelo de Roll, **estimador de volatilidad High-Low**, **Corwin-Schultz**); modelos estratégicos (lambdas de **Kyle**, **Amihud**, **Hasbrouck**); modelos secuenciales (PIN, VPIN); features adicionales (distribución de tamaños de orden, tasas de cancelación, TWAP, opciones, autocorrelación del flujo firmado); y una definición propia de información microestructural.
3. **Supuestos:** la mayoría requiere aggressor side.
4. **Conservar:** el subconjunto derivable de OHLCV, y la observación de que **los t-valores de estas estimaciones suelen ser más informativos que las estimaciones medias**, porque incorporan la desviación del error de estimación.
5. **IRIS:** ver §23 con el filtro aplicado estrictamente.
6. **OHLCV:** mixto. Parkinson y Corwin-Schultz **`OHLCV-OK`**; Roll y Amihud **`OHLCV-COND`**; el resto **`GRANULAR`** u **`OTRAS FUENTES`**.
11. **C** para lo derivable, **D** para el resto. 12. Documentamos lo que perdemos como limitación, no como recomendación de ampliar datos.

---

### Capítulos 20, 21, 22 — HPC — **D**

1. **Problema:** acelerar cálculos (multiprocessing, vectorización, particionado de tareas); optimización combinatoria y computación cuántica; infraestructura HPC.
2. **Conservar:** de los tres, únicamente el principio de **estructurar el código para que las funciones puedan llamarse en paralelo** (particiones lineales y de doble bucle anidado), útil para el sequential bootstrap, la triple barrera, MDA y SADF, que son los cuellos de botella reales.
3. **IRIS:** el capítulo 21 (computación cuántica) y el 22 (infraestructura de laboratorio nacional) son **irrelevantes** para nosotros.
11. **D**, con un elemento de nivel C (paralelización básica). 12. Nuestra prioridad es corrección y simplicidad, no infraestructura.

---

### 2.1 Resumen del mapa

| Nivel | Capítulos |
|---|---|
| **A — Crítico** | 1, 2, 3, 4, 7, 8, 10, 11, 12, 14, 15 |
| **B — Importante** | 5, 6, 9, 17 |
| **C — Complementario** | 13, 18, 19 (parcial) |
| **D — Poco relevante ahora** | 16, 19 (mayoría), 20, 21, 22 |

---

## 3. ESTRUCTURAS DE DATOS Y MUESTREO (Tarea 3-A)

### 3.1 Por qué López de Prado cuestiona el reloj cronológico

`[LDP]` Las barras temporales son las más populares entre practicantes y académicos, y **deberían evitarse**, por dos razones:

**Razón 1 — el mercado no procesa información a intervalos constantes.** La hora siguiente a la apertura es mucho más activa que la hora alrededor del mediodía (o de medianoche en el caso de futuros). Como seres biológicos, para los humanos tiene sentido organizar el día según el ciclo solar. Pero los mercados actuales están operados por algoritmos con supervisión humana laxa, para los cuales **los ciclos de CPU son más relevantes que los intervalos cronológicos**. Consecuencia directa: las barras temporales **sobremuestrean información en períodos de baja actividad y la submuestrean en períodos de alta actividad**.

**Razón 2 — malas propiedades estadísticas.** Las series muestreadas por tiempo exhiben con frecuencia correlación serial, heterocedasticidad y no-normalidad de retornos. Y añade una observación demoledora: **los modelos GARCH se desarrollaron, en parte, para lidiar con la heterocedasticidad asociada a un muestreo incorrecto.** Formar barras como proceso subordinado a la actividad de trading evita el problema de raíz.

`[INTERPRETACIÓN]` Este es un argumento de una clase distinta a la habitual. No dice "las barras de volumen funcionan mejor empíricamente"; dice que **una parte del aparato econométrico que usamos para corregir patologías de las series financieras existe porque las creamos nosotros al muestrear mal**.

### 3.2 La jerarquía de barras y qué problema resuelve cada una

| Barra | Criterio | Problema que resuelve | Problema que deja |
|---|---|---|---|
| **Tiempo** | Intervalo de reloj fijo | Simplicidad, disponibilidad universal | Sobre/submuestreo; correlación serial; heterocedasticidad; no-normalidad |
| **Tick** | Número fijo de transacciones | `[LDP]` Sincroniza el muestreo con un proxy de la llegada de información (la velocidad a la que se originan ticks). Múltiples estudios confirman que muestrear en función de la actividad acerca los retornos a IID normal, lo cual importa porque muchos métodos estadísticos asumen eso. Sólo podemos inferir de una variable aleatoria que sea invariante | `[LDP]` **Outliers de subasta**: muchas bolsas hacen subasta en apertura y cierre; el libro acumula órdenes sin casarlas y al concluir se publica una operación enorme al precio de equilibrio, que podría equivaler a miles de ticks pero se reporta como uno solo. Y la **fragmentación de órdenes** hace arbitrario el conteo de ticks |
| **Volumen** | Cantidad fija de unidades negociadas | `[LDP]` Elimina la arbitrariedad de la fragmentación (una compra de 10 lotes contra una orden de tamaño 10 es un tick; contra diez órdenes de tamaño 1 son diez ticks). Propiedades estadísticas aún mejores que las barras de tick. Además, varias teorías de microestructura estudian la interacción entre precios y volumen, por lo que muestrear en función del volumen es conveniente para esos análisis | No refleja correctamente cambios significativos de precio ni splits |
| **Dólar** | Valor fijo intercambiado | `[LDP]` El número de acciones negociadas es función del valor realmente intercambiado; vender $1.000 tras una apreciación del 100% requiere la mitad de títulos. Empíricamente, el número de barras por día **es mucho más estable a lo largo de los años** para las barras de dólar que para las de tick o volumen a tamaño constante. Y es robusto ante acciones corporativas (emisiones, recompras) que alteran ticks y volúmenes | El tamaño de barra constante puede no ser óptimo; sugiere ajustarlo dinámicamente |

`[LDP]` Además propone **barras dirigidas por información**: muestrear con más frecuencia cuando llega nueva información al mercado, en sentido microestructural. La teoría confiere importancia especial a la **persistencia de volúmenes firmados desbalanceados**, fenómeno asociado a la presencia de traders informados. Sincronizando el muestreo con su llegada, podríamos decidir antes de que los precios alcancen un nuevo equilibrio.

Las cuatro familias:
- **Tick Imbalance Bars (TIB)**: acumulan el signo de cada tick (regla del tick) y cierran barra cuando el desbalance excede lo esperado. `[LDP]` Pueden entenderse como **cubos de operaciones que contienen la misma cantidad de información**, independientemente de volúmenes, precios o ticks negociados.
- **Volume/Dollar Imbalance Bars (VIB/DIB)**: igual, ponderando por volumen o por valor. Al no depender de un tamaño de barra constante, resuelven además el problema de las acciones corporativas.
- **Tick Runs Bars (TRB)**: monitorizan secuencias (*runs*) de compras. `[LDP]` La motivación es que los grandes traders barren el libro, usan órdenes iceberg o trocean una orden madre en hijas, lo cual deja rastro de runs.
- **Volume/Dollar Runs Bars (VRB/DRB)**: la extensión ponderada.

### 3.3 Compatibilidad con nuestros datos — análisis honesto

Esta es la pregunta central del encargo en este bloque.

| Tipo de barra | Clasificación | Justificación |
|---|---|---|
| **Barras temporales** | **`OHLCV-OK`** | Es literalmente lo que nuestra API entrega. |
| **Barras de tick** | **`GRANULAR`** | Requieren contar transacciones individuales. Una barra OHLCV de un minuto no informa cuántas operaciones ocurrieron (el campo "número de trades" existe en algunos feeds, pero **no está en nuestro OHLCV declarado**). |
| **Barras de volumen** | **`OHLCV-COND`** | *Aproximables*: podemos agregar barras temporales consecutivas hasta que el volumen acumulado alcance un umbral. **Condiciones y pérdidas:** (a) la frontera de la barra queda cuantizada a la resolución de la barra base — no podemos partir una barra de un minuto por la mitad; (b) el OHLC resultante es correcto (open de la primera, close de la última, max de highs, min de lows) pero (c) **el VWAP interno se pierde** salvo que lo aproximemos; (d) si una sola barra base ya excede el umbral, la aproximación degenera. Cuanto más fina sea la barra base respecto al umbral de volumen, mejor la aproximación. |
| **Barras de dólar** | **`OHLCV-COND`** | Igual que las anteriores, acumulando `precio × volumen`. **Condición añadida:** LdP acumula el valor de cada transacción individual; nosotros sólo podemos usar un precio representativo por barra (close, o el típico `(H+L+C)/3`). El error es de segundo orden si la barra base es fina, pero existe y debe medirse. |
| **Barras de imbalance (TIB/VIB/DIB)** | **`GRANULAR`** | Requieren **firmar cada operación** mediante la regla del tick, que opera sobre la secuencia de precios de trades individuales. **Desde OHLCV esto no es reconstruible.** No existe forma de saber cuántas de las operaciones dentro de una barra fueron iniciadas por comprador. |
| **Barras de runs (TRB/VRB/DRB)** | **`GRANULAR`** | Idem, y más exigente aún: requieren la secuencia ordenada de signos. |

`[INTERPRETACIÓN]` Una tentación que conviene nombrar para rechazarla explícitamente: se podría definir un "signo de barra" como `sign(Close − Open)` y construir pseudo-barras de imbalance con él. **Eso no es una barra de imbalance.** La regla del tick clasifica cada transacción por su relación con la anterior; el signo de una barra agrega y cancela cientos o miles de esos eventos. Un desbalance de flujo firmado y una variación neta de precio son cantidades distintas: precisamente el interés microestructural del desbalance es que puede ser grande **sin** que el precio se haya movido todavía. Construir esa aproximación y llamarla barra de imbalance sería, en los términos del propio encargo, forzar artificialmente una técnica para hacerla compatible con nuestros datos. **No se recomienda.**

### 3.4 Qué información se pierde al partir de barras ya agregadas

`[LDP]` La advertencia general con la que abre el capítulo 2 es directa: **en general no conviene consumir el dataset ya procesado por otro**, porque el resultado probable es descubrir lo que otro ya sabe o descubrirá pronto. Idealmente el punto de partida es una colección de datos crudos no estructurados que procesamos nosotros.

`[IMPLICACIÓN PARA IRIS]` Nuestro diseño contradice esta recomendación por una razón deliberada (simplicidad operacional). Conviene dejar por escrito qué implica exactamente:

**Lo que perdemos irrecuperablemente al partir de barras temporales OHLCV:**
1. La **secuencia intrabar de precios** → imposibilita la regla del tick, todas las barras de información, y el orden de toque de barreras dentro de una barra.
2. El **aggressor side** → imposibilita Kyle, Hasbrouck, PIN, VPIN, y toda la segunda y tercera generación microestructural.
3. La **distribución de tamaños de orden** y las cancelaciones → imposibilita las features de la sección 19.6.
4. El **número de transacciones** → imposibilita barras de tick auténticas.
5. El **VWAP real** → sólo aproximable.
6. La granularidad de la **frontera de barra** en cualquier remuestreo → todas las barras alternativas quedan cuantizadas.

**Lo que NO perdemos:**
- La estructura de precios a la resolución de la barra base (y con ella High y Low, que son más informativos que el cierre y habilitan Parkinson y Corwin-Schultz).
- El volumen agregado, suficiente para aproximar barras de volumen/dólar.
- Todo lo que dependa únicamente de la serie de precios y su trayectoria: triple barrera, CUSUM, fracdiff, structural breaks, entropía, pesos de muestra, validación.

`[INTERPRETACIÓN]` La conclusión sobria: **la mayoría del aparato metodológico central de López de Prado (capítulos 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15) es implementable con OHLCV puro.** Lo que perdemos está concentrado en los capítulos 2 (barras de información) y 19 (microestructura). Esa es una pérdida real y significativa, pero **no es la pérdida del núcleo del libro**.

### 3.5 Nota sobre la elección de resolución base

`[INTERPRETACIÓN]` Si decidiéramos experimentar con barras de volumen o dólar aproximadas, la calidad de la aproximación depende enteramente de la relación entre la resolución de la barra base y el umbral objetivo. Esto convierte la elección de la resolución base en una decisión con consecuencias metodológicas y no sólo de conveniencia. Queda como pregunta abierta (§30).

---

## 4. FUTUROS Y ROLLOVERS (Tarea 3-B)

Este bloque tiene relevancia directa e inmediata para el MNQ.

### 4.1 El problema

`[LDP]` A veces necesitamos modelar series donde los pesos deben ajustarse dinámicamente, o productos que pagan cupones o dividendos irregulares, o sujetos a acciones corporativas. **Los eventos que alteran la naturaleza de la serie bajo estudio deben tratarse adecuadamente, o introduciremos inadvertidamente una ruptura estructural que desviará nuestros esfuerzos de investigación** (y remite explícitamente al capítulo 17 sobre structural breaks).

`[LDP]` Y una observación de campo: en su experiencia, la gente **sufre innecesariamente al manipular futuros, principalmente porque no sabe manejar bien el roll**.

`[IMPLICACIÓN PARA IRIS]` Un rollover mal tratado en MNQ produce un salto de precio artificial. Ese salto:
- Contamina cualquier cálculo de retornos.
- Puede disparar espuriamente un filtro CUSUM.
- Puede disparar espuriamente una barrera de la triple barrera, generando una etiqueta completamente falsa.
- Será detectado por los tests de ruptura estructural como una ruptura real.
- Y, si el salto es sistemático (contango/backwardation), un modelo puede **aprender a predecirlo**, produciendo un backtest excelente y absolutamente inoperable.

### 4.2 Las dos soluciones que propone

**El ETF trick.** `[LDP]` Transformar cualquier dataset multiproducto complejo en un dataset único que se parezca a un ETF de retorno total. La razón: **nuestro código puede asumir siempre que sólo operamos productos de tipo cash (instrumentos no expirables), independientemente de la complejidad y composición de la serie subyacente**.

Produce una serie que refleja el valor de $1 invertido, con tres propiedades deseables:
1. Los cambios en la serie reflejan cambios en el PnL.
2. La serie es **estrictamente positiva** (en el peor caso, infinitesimal), lo cual importa porque la mayoría de modelos asume precios positivos.
3. El *implementation shortfall* queda incorporado.

Adicionalmente, la construcción entrega tres variables que la estrategia necesita conocer: **costes de rebalanceo** (que deliberadamente **no** se incrustan en la serie de valor, porque de lo contrario ponerse corto generaría beneficios ficticios al rebalancear), **coste de bid-ask** de comprar o vender una unidad de este ETF virtual, y **volumen negociable**, determinado por el miembro menos activo de la cesta.

**El single future roll.** `[LDP]` Cuando se trata de un único contrato de futuros, el ETF trick puede manejarlo como caso particular de un spread de una sola pata, pero hay un **enfoque equivalente y más directo**: formar una serie temporal de **gaps de roll acumulados** y restarla de la serie de precios.

El procedimiento:
1. Identificar las fechas de roll (donde cambia el identificador de contrato).
2. En cada roll, calcular el gap entre el cierre previo y la apertura siguiente.
3. Acumular esos gaps.
4. Restar la serie acumulada de los precios.

El parámetro `matchEnd` determina la dirección: en un roll hacia adelante, el precio al **inicio** de la serie rolada coincide con el de la serie cruda; en un roll hacia atrás, coincide el precio del **final**.

### 4.3 Las advertencias críticas sobre el roll

`[LDP]` Tres puntos que conviene retener literalmente porque son fáciles de pasar por alto:

**(a) Precios rolados vs precios crudos tienen usos distintos.** Los precios rolados se usan para **simular PnL y valores de cartera a mercado**. Pero los **precios crudos deben seguir usándose para dimensionar posiciones y determinar consumo de capital**.

**(b) Los precios rolados pueden volverse negativos.** Particularmente en contratos que cayeron mientras estaban en contango. LdP invita a comprobarlo con futuros de algodón o gas natural.

**(c) Cómo obtener una serie no negativa.** Si queremos trabajar con series roladas no negativas: (1) calcular la serie de precios rolados; (2) calcular el retorno como **cambio del precio rolado dividido por el precio crudo anterior**; (3) formar la serie de precios acumulando esos retornos.

`[INTERPRETACIÓN]` El punto (c) es sutil y merece subrayarse: **el numerador viene de la serie rolada y el denominador de la serie cruda**. Es una construcción específica que evita simultáneamente el salto del roll y la distorsión de dividir por un precio ajustado.

### 4.4 Compatibilidad con IRIS

| Elemento | Clasificación | Nota |
|---|---|---|
| **Single future roll (método de gaps)** | **`OHLCV-COND`** | Requiere `Open`, `Close` y **un identificador de contrato o las fechas de roll**. Si nuestra API entrega OHLCV con el símbolo del contrato activo, es **`OHLCV-OK`** directamente. |
| **Serie rolada no negativa** | **`OHLCV-COND`** | Requiere conservar simultáneamente la serie cruda y la rolada. |
| **ETF trick completo** | **`OTRAS FUENTES`** para cestas; innecesario para un futuro único, según el propio autor. |
| **Pesos PCA** | **`OTRAS FUENTES`** | Requiere múltiples instrumentos. No aplicable. |

`[IMPLICACIÓN PARA IRIS]` Consecuencia de diseño que conviene registrar ahora: **debemos exigir que nuestra fuente de datos identifique el contrato**, o bien las fechas de roll. Si la API entrega una serie continua ya empalmada por un método que no controlamos ni conocemos, estamos exactamente en el escenario que el autor desaconseja —consumir el dataset procesado de otro— y con un riesgo concreto: no sabremos si los saltos residuales son mercado o artefacto.

`[VACÍO]` El libro no discute qué convención de roll es preferible para un futuro sobre índice de renta variable (¿por volumen? ¿por open interest? ¿N días antes del vencimiento?), ni el efecto de la elección sobre los resultados. Tampoco trata el efecto del roll sobre el volumen (que se reparte entre dos contratos durante la transición), lo cual es relevante si construimos barras de volumen.

---

## 5. MUESTREO BASADO EN EVENTOS (Tarea 3-A, continuación)

### 5.1 Por qué muestrear por eventos

`[LDP]` Aunque podríamos aplicar un algoritmo de ML sobre el dataset completo, en general **no sería buena idea**, por dos razones:

1. **Varios algoritmos no escalan bien con el tamaño muestral** (cita SVM como ejemplo).
2. **Los algoritmos de ML alcanzan mayor precisión cuando intentan aprender de ejemplos relevantes.**

`[LDP]` El argumento del punto 2 es el importante, y lo ilustra con un ejemplo que merece citarse en su lógica completa: supongamos que queremos predecir si el siguiente movimiento absoluto del 5% será positivo (un rally) o negativo (una liquidación). **En un instante aleatorio cualquiera, la precisión de tal predicción será baja.** Pero si pedimos al clasificador que prediga el signo del siguiente movimiento del 5% **después de ciertas condiciones catalíticas**, es más probable que encontremos features informativas que permitan una predicción más precisa.

`[LDP]` Los gestores de cartera típicamente colocan una apuesta **después de que ocurre algún evento**: una ruptura estructural (cap. 17), una señal extraída (cap. 18), un fenómeno microestructural (cap. 19), la publicación de una estadística macro, un pico de volatilidad, un desvío significativo de un spread respecto de su equilibrio.

`[LDP]` Y la formulación metodológica clave: **podemos caracterizar un evento como significativo y dejar que el algoritmo de ML aprenda si existe una función de predicción precisa bajo esas circunstancias.** Quizá la respuesta sea no, en cuyo caso redefiniríamos qué constituye un evento, o probaríamos con features alternativas.

`[INTERPRETACIÓN]` Esto reformula la pregunta. En lugar de "¿puedo predecir el mercado?", la pregunta pasa a ser **"¿existe alguna condición bajo la cual el mercado sea predecible?"**. Es una pregunta más modesta, más testeable, y estructuralmente más cercana a lo que IRIS declara querer responder ("¿existe actualmente una oportunidad operativa?").

### 5.2 Muestreo para reducción vs muestreo por eventos

`[LDP]`
- **Linspace sampling**: muestreo secuencial a paso constante. Ventaja: simplicidad. Desventajas: el paso es arbitrario y los resultados varían según la barra semilla.
- **Uniform sampling**: muestreo aleatorio uniforme. Resuelve lo anterior.
- **Crítica común a ambos**: la muestra **no contiene necesariamente el subconjunto de observaciones más relevantes** en términos de poder predictivo o contenido informativo.

### 5.3 El filtro CUSUM

`[LDP]` Método de control de calidad diseñado para detectar un desplazamiento de la media de una cantidad medida respecto de un valor objetivo. Se acumulan sumas positivas y negativas de las desviaciones respecto de la expectativa, con suelo en cero para la rama positiva y techo en cero para la negativa, y se dispara cuando el máximo entre ambas excede un umbral `h`. Tras disparar, se resetea.

`[LDP]` **La propiedad práctica que lo hace atractivo**: no se disparan múltiples eventos cuando la serie oscila alrededor de un nivel umbral, **defecto que sí sufren señales populares de mercado como las bandas de Bollinger**. Se requiere una corrida completa de longitud `h` para disparar un evento.

`[LDP]` **Uso distinto al de la literatura previa**: otros autores propusieron una estrategia de inversión con señales alternantes de compra/venta al observarse un retorno absoluto `h` respecto de un máximo o mínimo previo, equivalente a la "filter trading strategy". **El uso de LdP es diferente: sólo muestrea una barra cuando se supera el umbral.** No genera señal, genera una observación.

`[LDP]` Y la generalización importante: la variable acumulada **puede basarse en cualquiera de las features de los capítulos 17-19** —estadísticos de ruptura estructural, entropía, medidas de microestructura—. Por ejemplo, se podría declarar un evento cuando el SADF se desvía suficientemente de un nivel de reset previo. Obtenido ese subconjunto de barras dirigidas por eventos, dejamos que el algoritmo determine si la ocurrencia de tales eventos constituye inteligencia accionable.

### 5.4 Compatibilidad y relevancia para IRIS

| Elemento | Clasificación | Nota |
|---|---|---|
| **Filtro CUSUM sobre retornos** | **`OHLCV-OK`** | Sólo requiere la serie de cierres. Trivial de implementar. |
| **CUSUM sobre retornos absolutos** | **`OHLCV-OK`** | Variante que el propio autor propone como ejercicio, comparando cuál produce muestras menos heterocedásticas. |
| **CUSUM sobre fracdiff** | **`OHLCV-OK`** | Combinación que él mismo sugiere en los ejercicios del capítulo 5. |
| **CUSUM sobre SADF / entropía** | **`OHLCV-OK`** | Ambas features son derivables de precios (§21, §22). |
| **CUSUM sobre features microestructurales** | **`GRANULAR`** en su mayoría | Salvo las derivables de High/Low. |

`[IMPLICACIÓN PARA IRIS]` El muestreo por eventos es probablemente **una de las dos o tres ideas más importantes que esta fuente aporta a nuestro proyecto**, por tres razones convergentes:
1. Reduce drásticamente el número de observaciones, aliviando el problema de solapamiento (§8) y el coste computacional.
2. Concentra el aprendizaje en momentos potencialmente informativos en lugar de en el ruido de fondo.
3. **Es exactamente compatible con nuestra restricción de datos** y no añade dependencias externas.

`[LDP]` Pero conviene retener la honestidad del planteamiento: el filtro **no garantiza** que los eventos seleccionados sean informativos. Define una hipótesis testeable ("bajo estas condiciones hay predictibilidad") que puede resultar falsa, en cuyo caso se redefine el evento.

`[VACÍO]` El libro no ofrece criterio para elegir el umbral `h` ni la variable subyacente. Da ejemplos (h = desviación estándar de retornos diarios; h = 0.05) pero sin justificación general. Queda como decisión abierta, y —advertencia importante— **cada valor de `h` probado cuenta como un intento a efectos de multiple testing**.

---

## 6. LABELING Y EL MÉTODO DE LA TRIPLE BARRERA (Tarea 4)

### 6.1 El método de horizonte fijo y por qué es problemático

`[LDP]` Describe primero el método que, según él, usan **prácticamente todos los artículos de ML aplicado a finanzas**: se asigna a cada observación una etiqueta en {−1, 0, 1} según si el retorno a `h` barras vista es menor que −τ, está dentro de ±τ, o es mayor que τ, con τ una constante predefinida.

`[LDP]` Y da **tres razones para evitarlo**, en orden creciente de gravedad:

**Razón 1 — el soporte es una barra temporal.** Como se vio en el capítulo 2, las barras temporales no tienen buenas propiedades estadísticas. Como la literatura casi siempre trabaja con barras temporales, `h` implica un horizonte cronológico fijo.

**Razón 2 — el umbral constante ignora la volatilidad observada.** Ilustración concreta: supongamos τ = 1E−2, mientras que a veces etiquetamos una observación con volatilidad de barra realizada de 1E−4 (por ejemplo, durante la sesión nocturna) y otras veces de 1E−2 (por ejemplo, en torno a la apertura). **La gran mayoría de etiquetas será 0, aunque el retorno fuera predecible y estadísticamente significativo.** Y lo califica sin ambigüedad: es un error muy común etiquetar observaciones según un umbral fijo sobre barras temporales.

**Razón 3 — y aquí está el argumento decisivo — el camino seguido por los precios.** `[LDP]` **Toda estrategia de inversión tiene límites de stop-loss**, ya sean autoimpuestos por el gestor, exigidos por el departamento de riesgo, o disparados por un margin call. **Es sencillamente irrealista construir una estrategia que obtenga beneficio de posiciones que habrían sido cerradas forzosamente por la bolsa.** Y añade una observación mordaz: que prácticamente ninguna publicación tenga esto en cuenta al etiquetar dice algo sobre el estado actual de la literatura de inversión.

### 6.2 Umbrales dinámicos

`[LDP]` En la práctica queremos fijar límites de profit-taking y stop-loss que sean **función del riesgo involucrado en la apuesta**. De lo contrario, a veces apuntaremos demasiado alto (τ mucho mayor que la volatilidad prevaleciente) y a veces demasiado bajo.

La implementación de referencia: **desviación estándar móvil exponencialmente ponderada de los retornos diarios**, evaluada en los puntos intradiarios de estimación. El resultado se usa como el objetivo `trgt` que define la anchura unitaria de las barreras horizontales.

**Clasificación: `OHLCV-OK`.** Sólo requiere cierres.

### 6.3 El método de la triple barrera

`[LDP]` **Qué es:** un método de etiquetado que asigna la etiqueta según **cuál de tres barreras se toca primero**.
- **Dos barreras horizontales**: profit-taking y stop-loss, definidas como **función dinámica de la volatilidad estimada** (realizada o implícita).
- **Una barrera vertical**: número de barras transcurridas desde que se tomó la posición (límite de expiración).

Etiquetas: 1 si se toca primero la superior; −1 si se toca primero la inferior; y si se toca primero la vertical, **hay dos opciones: el signo del retorno, o un 0**. El autor declara preferir personalmente el signo del retorno —como cuestión de realizar un beneficio o pérdida dentro de límites—, pero indica explícitamente que **habría que explorar si el 0 funciona mejor en cada problema concreto**.

`[LDP]` **La propiedad definitoria: es dependiente del camino.** Para etiquetar una observación hay que considerar la trayectoria completa del intervalo. Se denota `t1` el momento del primer toque, y el retorno asociado a la feature observada es el que va del inicio al primer toque —no al final del horizonte.

`[LDP]` Las barreras horizontales **no tienen que ser simétricas**, y el momento del primer toque es siempre menor o igual que el fin del horizonte.

### 6.4 Las ocho configuraciones

`[LDP]` Denotando una configuración por el triplete `[pt, sl, t1]` con 1 = activa y 0 = desactivada:

**Tres configuraciones útiles:**
| Config | Interpretación |
|---|---|
| `[1,1,1]` | El montaje estándar: queremos realizar beneficio, pero tenemos tolerancia máxima a pérdidas y un período de tenencia máximo. |
| `[0,1,1]` | Salir tras un número de barras, salvo que nos salte el stop. |
| `[1,1,0]` | Tomar beneficio mientras no nos salte el stop. **El autor lo califica de algo irreal**, porque implica estar dispuesto a mantener la posición el tiempo que haga falta. |

**Tres configuraciones menos realistas:**
| Config | Interpretación |
|---|---|
| `[0,0,1]` | **Equivalente al método de horizonte fijo.** El autor señala que **aún puede ser útil** aplicado a barras de volumen, dólar o dirigidas por información, y con múltiples previsiones actualizándose dentro del horizonte. |
| `[1,0,1]` | Mantener hasta obtener beneficio o exceder el período máximo, ignorando pérdidas latentes intermedias. |
| `[1,0,0]` | Mantener hasta obtener beneficio. Podría implicar quedar atrapado en una posición perdedora durante años. |

**Dos configuraciones ilógicas:** `[0,1,0]` (mantener hasta que salte el stop, sin objetivo) y `[0,0,0]` (sin barreras: la posición queda bloqueada para siempre y no se genera etiqueta).

`[INTERPRETACIÓN]` La tabla es más útil de lo que parece: convierte la elección de target en un **espacio de diseño enumerado y finito**, donde el método de horizonte fijo que Jansen usa universalmente aparece como un caso particular degenerado. Eso es exactamente lo que necesitábamos para poder comparar en lugar de asumir.

### 6.5 Qué problema resuelve exactamente la triple barrera

Respondiendo directamente a la pregunta del encargo:

**Problema 1 — realismo operativo.** Un target de horizonte fijo etiqueta como ganadora una observación cuyo precio, en el camino, cayó lo suficiente como para haber cerrado la posición forzosamente. La triple barrera **etiqueta lo que realmente habría ocurrido** bajo una regla operativa concreta.

**Problema 2 — escala.** El umbral se adapta a la volatilidad del momento, evitando que la distribución de etiquetas dependa del régimen de volatilidad en lugar de la predictibilidad.

**Problema 3 — coherencia entre etiqueta y estrategia.** `[INTERPRETACIÓN]` El target y la regla de trading dejan de ser objetos independientes: la etiqueta **es** el resultado de aplicar la regla. Esto elimina un salto lógico que en el enfoque de horizonte fijo queda sin justificar (predecir el retorno a N minutos y luego, por separado, inventar cómo operar esa predicción).

**Qué información aporta considerar la trayectoria.** `[INTERPRETACIÓN]` Dos observaciones con idéntico retorno a `h` barras pueden tener trayectorias radicalmente distintas: una que sube monótonamente y otra que cae un 2% antes de recuperar. Bajo horizonte fijo son la misma etiqueta. Bajo triple barrera, con un stop razonable, **son etiquetas opuestas**. Lo que se gana es que el target codifica *la secuencia*, no sólo el extremo; y la secuencia es lo que determina si una posición sobrevive.

### 6.6 Compatibilidad con nuestros datos — con un matiz importante

**Clasificación de referencia: `OHLCV-OK`.**

`[LDP]` La implementación del libro comprueba las barreras contra **la serie de precios de cierre** del camino. Con OHLCV tenemos exactamente eso.

`[INTERPRETACIÓN]` Pero surge una decisión que el libro no discute y que en intradiario **puede ser material**: podríamos comprobar las barreras contra **High y Low** en lugar de contra Close. Ventaja: refleja mejor lo que ocurriría con órdenes stop y limit reales, que se ejecutan intrabar. Problema: **ambigüedad intrabar**. Si en una misma barra el High supera el profit-taking y el Low perfora el stop-loss, **no podemos saber cuál se tocó primero**. Con barras de un minuto en MNQ esto no es un caso raro.

Las opciones conceptuales (sin elegir ninguna):
- Usar sólo cierres, como el libro. Conservador respecto a la ambigüedad, pero optimista respecto a los stops (subestima cuántas veces habríamos sido detenidos).
- Usar High/Low con una regla de desempate pesimista (asumir que se tocó primero el stop). Conservador económicamente, pero introduce un sesgo sistemático.
- Usar barras base más finas para reducir la frecuencia de la ambigüedad.

`[VACÍO]` **El libro no aborda esto.** Y es un vacío con consecuencias reales para un sistema intradiario. Queda registrado como decisión abierta.

### 6.7 Eliminación de etiquetas innecesarias

`[LDP]` Algunos clasificadores rinden mal cuando las clases están muy desbalanceadas. En esas circunstancias es preferible **descartar etiquetas extremadamente raras** y centrarse en los resultados más comunes. Propone un procedimiento recursivo que elimina observaciones asociadas a clases que aparecen en menos de una fracción mínima de casos, **salvo que sólo queden dos clases**.

**Clasificación: `OHLCV-OK`.** Es post-procesamiento de etiquetas.

---

## 7. SIDE, SIZE Y META-LABELING (Tarea 5)

Este es el bloque de mayor relevancia estratégica para el objetivo declarado de IRIS.

### 7.1 La distinción fundamental: side vs size

`[LDP]`
- **Side** = la dirección de la apuesta: largo o corto.
- **Size** = el tamaño de la apuesta, **incluida la posibilidad de no apostar en absoluto (tamaño cero)**.

`[LDP]` **Aprender side.** Nos interesa aprender el lado cuando **no tenemos un modelo subyacente que fije el signo de la posición**. Bajo esas circunstancias hay una consecuencia técnica ineludible: **no podemos diferenciar entre una barrera de profit-taking y una de stop-loss, porque eso requiere conocer el lado.** Por tanto, aprender el lado implica **o bien que no haya barreras horizontales, o bien que las barreras horizontales sean simétricas**. Las etiquetas resultantes son {−1, 0, 1}.

`[LDP]` **Aprender size.** Supongamos que ya tenemos un modelo que fija el lado. Sólo necesitamos aprender el tamaño. **Esta es una situación que los practicantes enfrentan regularmente**: a menudo sabemos si queremos comprar o vender, y la única pregunta pendiente es cuánto dinero arriesgar. **No queremos que el algoritmo aprenda el lado, sólo que nos diga el tamaño apropiado.** Las etiquetas resultantes son {0, 1}.

`[LDP]` Y una consecuencia práctica que aparece al conocer el lado: **las barreras horizontales ya no necesitan ser simétricas**.

`[INTERPRETACIÓN]` Esta asimetría es más profunda de lo que parece. La simetría forzada de barreras al aprender el lado no es una convención: es una restricción lógica. Y significa que **la formulación del problema determina qué esquema de barreras es siquiera expresable**. No podemos elegir "triple barrera asimétrica" y "aprender el lado" a la vez.

### 7.2 Qué es meta-labeling

`[LDP]` **La definición**: dado un modelo primario que fija el lado, construir un **modelo secundario de ML que aprenda a usar ese modelo primario exógeno**. De ahí el nombre: etiquetamos las etiquetas del primer modelo.

**Mecánica del etiquetado:**
- Se conoce el lado, así que el retorno del camino se multiplica por el lado (convirtiendo todo en "retorno desde el punto de vista de la posición tomada").
- La etiqueta pasa a ser **1 si la operación habría sido rentable, 0 si no**.
- El algoritmo se entrena para decidir **si tomar la apuesta o pasar**: una predicción puramente binaria.
- Cuando la etiqueta predicha es 1, **la probabilidad de esa predicción secundaria puede usarse para derivar el tamaño de la apuesta**, mientras el signo lo fijó el modelo primario.

`[LDP]` **El propósito explícito del modelo secundario**: determinar si un positivo del modelo primario es verdadero o falso. **No es su propósito generar oportunidades de apuesta. Su propósito es determinar si debemos actuar o pasar sobre la oportunidad que se nos ha presentado.**

### 7.3 La conexión con precision y recall

`[LDP]` El razonamiento estadístico que justifica la arquitectura:

- Los problemas de clasificación binaria presentan un compromiso entre errores tipo I (falsos positivos) y tipo II (falsos negativos). En general, aumentar la tasa de verdaderos positivos tiende a aumentar la de falsos positivos.
- **Precision** es la fracción de positivos predichos que son correctos. **Recall** es la fracción de positivos reales que el clasificador captura. En general, reducir el área de falsos positivos tiene el coste de aumentar la de falsos negativos, porque mayor precisión implica típicamente menos llamadas y por tanto menor recall.
- **F1** es la media armónica de precision y recall.

`[LDP]` **La receta**: el meta-labeling es particularmente útil cuando queremos F1 altos. **Primero** construimos un modelo que alcance **recall alto, aunque la precisión no sea especialmente buena**. **Segundo**, corregimos la baja precisión aplicando meta-labeling a los positivos predichos por el modelo primario. El meta-labeling **aumenta el F1 filtrando los falsos positivos**, cuando la mayoría de positivos ya han sido identificados por el modelo primario.

`[INTERPRETACIÓN]` Esta es una idea de diseño con consecuencias operativas fuertes: **libera al modelo primario de ser preciso**. Su trabajo es no perderse oportunidades (recall), no acertarlas todas. Es una descomposición del problema, no un truco de calibración.

### 7.4 Las cuatro ventajas adicionales que declara

`[LDP]`
1. **Caja blanca por debajo.** Permite construir un sistema de ML **encima de una caja blanca** —por ejemplo un modelo fundamental fundado en teoría económica—. La capacidad de transformar un modelo fundamental en un modelo de ML lo hace útil para firmas quantamental.
2. **Menor overfitting.** **Los efectos del overfitting quedan limitados, porque el ML no decide el lado de la apuesta, sólo el tamaño.**
3. **Estructuras de estrategia sofisticadas.** Al desacoplar la predicción de lado de la de tamaño, se habilitan arquitecturas como: **las features que impulsan un rally pueden diferir de las que impulsan una liquidación**; en ese caso podríamos desarrollar una estrategia de ML exclusiva para posiciones largas, basada en las recomendaciones de compra de un modelo primario, y otra exclusiva para cortos, basada en las de venta de **un modelo primario enteramente distinto**.
4. **El tamaño importa tanto como la dirección.** Acertar mucho en apuestas pequeñas y poco en apuestas grandes lleva a la ruina. Tiene sentido dedicar un algoritmo exclusivamente a acertar esa decisión crítica.

`[LDP]` Y su valoración de campo: en su experiencia, los modelos de ML con meta-labeling pueden entregar **resultados más robustos y fiables** que los modelos de etiquetado estándar.

`[LDP]` **Puede añadirse una capa de meta-labeling a cualquier modelo primario**: un algoritmo de ML, una ecuación econométrica, **una regla técnica de trading**, un análisis fundamental, o incluso una previsión generada por un humano basada en su intuición.

### 7.5 De dónde sale naturalmente el "no operar"

`[INTERPRETACIÓN]` Recogiendo lo anterior, hay al menos **tres mecanismos distintos** por los que la abstención emerge en el marco de LdP, y conviene no confundirlos:

1. **Meta-labeling con etiqueta 0.** El modelo secundario predice directamente "pasar". Es la abstención como clasificación.
2. **Probabilidad baja en el sizing.** `[LDP]` En el capítulo 4 señala que **el caso neutro es innecesario, porque puede implicarse mediante una predicción de −1 o 1 con confianza baja**. Y en el capítulo 10 el tamaño se deriva del estadístico z de la probabilidad respecto a la hipótesis nula: **una probabilidad cercana a la del azar produce un tamaño cercano a cero**. Es la abstención como magnitud continua.
3. **Discretización del tamaño.** `[LDP]` Al redondear el tamaño a pasos discretos, los tamaños muy pequeños colapsan a cero. Es la abstención como consecuencia del control de turnover.

`[LDP]` Y una recomendación explícita en la dirección opuesta a la clase neutra: al hablar de atribución de retornos como pesos de muestra, dice que el método **no funciona si existe un caso "neutro"** (retorno por debajo del umbral), porque para ese caso los retornos menores deberían recibir pesos mayores, no lo recíproco. **Y de ahí concluye que generalmente aconsejaría eliminar los casos neutros.**

`[IMPLICACIÓN PARA IRIS]` Esto es directamente relevante para nuestra formulación tentativa LONG / SHORT / NO TRADE. López de Prado **desaconseja la clase neutra explícita** y ofrece dos alternativas: derivarla de la confianza (tamaño ≈ 0), o derivarla de un modelo secundario binario. No es una decisión que debamos tomar ahora, pero **el libro sí aporta un argumento en contra de la formulación de tres clases** que conviene registrar.

### 7.6 Las tres formulaciones planteadas en el encargo, evaluadas con los fundamentos de LdP

**Sin seleccionar ninguna**, esto es lo que la fuente permite decir sobre cada una:

---

#### Formulación 1 — Modelo único: LONG / SHORT / NO TRADE

**Fundamentos a favor que aporta LdP:** ninguno directo. Su etiquetado de "side and size" produce {−1, 0, 1}, donde el 0 aparece **sólo** cuando se toca la barrera vertical y se opta por etiquetarla como 0 en lugar de por el signo. Es decir, el 0 significa "no llegó a ninguna barrera horizontal", no "no operar".

**Fundamentos en contra:**
- Recomienda eliminar los casos neutros porque complican la ponderación por atribución de retornos.
- Sostiene que el neutro es innecesario porque se implica desde una predicción con confianza baja.
- Advierte sobre el rendimiento de clasificadores con clases desbalanceadas y propone eliminar etiquetas raras.
- **Restricción lógica:** aprender el lado obliga a barreras simétricas, lo que impide un esquema `[PT, SL]` asimétrico.

**Qué habría que verificar empíricamente:** si la clase 0 queda bien poblada y separable, o si degenera.

---

#### Formulación 2 — Primario LONG/SHORT + Secundario OPERAR/NO OPERAR

**Fundamentos a favor:** es exactamente el meta-labeling. Ventajas declaradas: menor overfitting (el ML no decide el lado), mayor F1 vía filtrado de falsos positivos, posibilidad de barreras asimétricas, probabilidad secundaria directamente convertible en tamaño, y arquitecturas separadas para largo y corto.

**Fundamentos en contra / condiciones:**
- Requiere **un modelo primario que exista y sea razonable**. Si el primario es a su vez un modelo de ML entrenado por nosotros, gran parte de la ventaja de "caja blanca" se pierde.
- `[LDP]` La receta pide que el primario tenga **recall alto** aunque su precisión sea baja. Eso es una especificación concreta que el primario debe cumplir, no un detalle.
- `[LDP]` En el tuning, para meta-labeling recomienda **F1 como función de scoring**, porque con muchos casos negativos un clasificador que prediga todo negativo lograría alta accuracy o buen log-loss sin haber aprendido nada.
- Añade una capa más al sistema, con su propio riesgo de overfitting y su propio presupuesto de multiple testing.

**Nota crítica:** `[LDP]` señala una degeneración a vigilar: si tras aplicar meta-labeling hay muchos más casos positivos que negativos, un clasificador que prediga todo positivo obtendría F1 alto sin discriminar. Su sugerencia es **intercambiar las definiciones de positivo y negativo** para que los negativos predominen, y entonces puntuar con F1.

---

#### Formulación 3 — Modelo de probabilidad de éxito de una señal exógena

**Fundamentos a favor:** es el caso puro de meta-labeling sobre una caja blanca. `[LDP]` Menciona explícitamente que el primario puede ser **una regla técnica de trading**, y sus propios ejercicios proponen exactamente eso: una estrategia de seguimiento de tendencia basada en cruce de medias móviles, y una de reversión basada en bandas de Bollinger, sobre las cuales se derivan meta-etiquetas y se entrena un Random Forest para decidir si operar o no.

**Fundamentos en contra / condiciones:**
- La calidad del sistema queda acotada por la del primario: el secundario **no genera oportunidades**, sólo filtra.
- Si el primario no tiene recall suficiente, las oportunidades perdidas son irrecuperables.

`[IMPLICACIÓN PARA IRIS]` Los ejercicios del capítulo 3 son notables por otra razón: **son el punto exacto donde este libro conecta con Murphy**. LdP propone usar análisis técnico clásico como modelo primario y ML como capa de filtrado. Eso convierte la tercera fuente bibliográfica en algo potencialmente estructural y no decorativo. Lo registramos para la etapa siguiente (§31) sin desarrollarlo ahora.

### 7.7 Limitaciones del meta-labeling

`[LDP] / [INTERPRETACIÓN]`
- No genera alfa por sí mismo; **filtra**. Un primario sin señal no se arregla con meta-labeling.
- Introduce una segunda superficie de sobreajuste.
- La utilidad depende de que existan features **predictivas de los falsos positivos del primario**, que no son necesariamente las mismas que predicen el mercado. `[LDP]` lo señala al decir que el ML secundario permite incorporar features predictivas de falsos positivos.
- `[VACÍO]` El libro no discute cómo validar conjuntamente los dos modelos (¿se entrenan sobre los mismos folds? ¿el primario se reentrena dentro de cada fold?). Es un problema real de leakage que queda sin tratar.

---

## 8. SOLAPAMIENTO, CONCURRENCIA, UNICIDAD Y PESOS DE MUESTRA (Tarea 6)

### 8.1 El problema formalizado

`[LDP]` Cuando etiquetamos según un intervalo `[t_{i,0}, t_{i,1}]`, si el intervalo de la observación `i` se solapa con el de la observación `j`, **ambas etiquetas dependen de un retorno común**. La implicación directa: **la serie de etiquetas no es IID siempre que exista solapamiento entre dos resultados consecutivos**.

`[LDP]` La salida obvia —restringir el horizonte de la apuesta para que no haya solapamiento— **es una solución terrible**. Llevaría a modelos toscos donde **la frecuencia de muestreo de las features quedaría limitada por el horizonte usado para determinar el resultado**. Si quisiéramos investigar resultados a un mes, las features tendrían que muestrearse como mucho mensualmente. Y si aplicamos una técnica dependiente del camino como la triple barrera, la frecuencia de muestreo quedaría subordinada al primer toque de barrera. **Debemos permitir el solapamiento**, lo cual nos devuelve al problema.

### 8.2 La analogía de las muestras de sangre

`[LDP]` La ilustración es tan clara que merece reproducirse en su lógica: obtenemos muestras de sangre de muchos pacientes y medimos su colesterol. Diversos factores comunes desplazan la media y la desviación, pero las muestras siguen siendo independientes: una observación por sujeto. **Ahora supongamos que alguien en el laboratorio derrama sangre de cada tubo en los nueve tubos siguientes a su derecha.** El tubo 10 contiene sangre del paciente 10, pero también de los pacientes 1 a 9. Ahora hay que determinar qué features predicen colesterol alto sin conocer con certeza el nivel de cada paciente.

`[LDP]` Y el remate: **ese es el desafío equivalente en ML financiero, con el handicap adicional de que el patrón de derrame es no determinista y desconocido.** Las finanzas no son un tema de "enchufar y usar" en cuanto a aplicaciones de ML.

### 8.3 Concurrencia y unicidad

`[LDP]`
- **Concurrencia**: dos etiquetas son concurrentes en `t` cuando ambas son función de al menos un retorno común. El solapamiento **no necesita ser perfecto**. Para cada instante `t` se construye un indicador binario por observación, y `c_t` es el número de etiquetas concurrentes en `t`.
- **Unicidad de una etiqueta en el instante t**: el recíproco de la concurrencia en ese instante.
- **Unicidad media de la etiqueta**: promedio de su unicidad a lo largo de su vida. `[LDP]` Puede interpretarse también como **el recíproco de la media armónica de la concurrencia sobre la vida del evento**.

`[LDP]` Nota crítica sobre leakage: calcular la unicidad media requiere información que no está disponible hasta un momento futuro. **Esto no es un problema, porque estos valores se usan sobre el conjunto de entrenamiento en combinación con la información de etiquetas, no sobre el de test. No se usan para prever la etiqueta, por lo que no hay fuga de información.**

`[INTERPRETACIÓN]` Esa aclaración es importante y fácil de malinterpretar. Los pesos de muestra **son** información del futuro respecto a cada observación; su legitimidad viene de que son parte del proceso de entrenamiento, igual que la propia etiqueta.

### 8.4 Por qué 100.000 filas no son 100.000 observaciones

`[LDP]` La cuantificación:
- Con muestreo con reemplazo estándar sobre `I` elementos, la probabilidad de no seleccionar un elemento concreto converge a `e⁻¹`, de modo que **el número de observaciones únicas esperado es aproximadamente 2/3**.
- Si el número máximo de resultados no solapados es `K ≤ I`, esa proporción cae a `1 − e^(−K/I)`, que es menor. **La implicación es que asumir incorrectamente extracciones IID conduce a sobremuestreo.**

`[LDP]` **Los dos efectos perjudiciales sobre el bagging:**
1. **Las muestras extraídas con reemplazo son casi idénticas entre sí**, aunque no compartan las mismas observaciones. Esto hace que la correlación media entre predicciones tienda a 1, y entonces **el bagging no reducirá la varianza, independientemente del número de estimadores**. En el caso de un Random Forest, todos los árboles del bosque serán esencialmente copias muy similares de un único árbol sobreajustado.
2. **La precisión out-of-bag quedará groseramente inflada**, porque el muestreo aleatorio coloca en el conjunto de entrenamiento muestras muy similares a las que quedan fuera de bolsa.

`[LDP]` Y una regla de dimensionamiento explícita: **si cada observación en `t` se etiqueta según el retorno entre `t` y `t+100`, deberíamos muestrear el 1% de las observaciones por estimador embolsado, no más.**

`[IMPLICACIÓN PARA IRIS]` Traducido literalmente a nuestro caso hipotético del encargo —señal cada minuto, etiqueta que observa los siguientes 30 minutos— **deberíamos muestrear en torno al 3% de las observaciones por estimador**. Con un millón de barras de un minuto, el número efectivo de observaciones independientes sería de un orden de magnitud muchísimo menor que el número de filas. Esto tiene tres consecuencias encadenadas:
1. Nuestro **presupuesto de multiple testing** es mucho más pequeño de lo que sugiere el tamaño del dataset.
2. Cualquier significación estadística calculada sobre el número de filas está inflada.
3. **El muestreo por eventos (§5) ataca este problema en la raíz**, no sólo como reducción computacional: al espaciar las observaciones, aumenta su unicidad media.

### 8.5 Las tres soluciones

`[LDP]` En orden creciente de calidad, con su valoración explícita:

**Solución 1 — eliminar resultados solapados antes del bootstrap.** Como los solapamientos no son perfectos, eliminar una observación sólo porque hay solapamiento parcial produce **una pérdida extrema de información**. **El autor desaconseja explícitamente seguir este camino.**

**Solución 2 — limitar la fracción muestreada.** Usar la unicidad media para reducir la influencia indebida de resultados con información redundante: muestrear sólo una fracción igual a la unicidad media (o un múltiplo pequeño). En sklearn esto se hace fijando `max_samples` a la unicidad media del `BaggingClassifier`. **Los Random Forest no ofrecen esa funcionalidad**; la solución es embolsar un número grande de árboles de decisión.

**Solución 3 — sequential bootstrap.** La mejor de las tres.

### 8.6 Sequential bootstrap

`[LDP]` **Qué intenta conseguir**: hacer las extracciones según una **probabilidad cambiante que controla la redundancia**.

**Mecánica:**
1. La primera extracción es uniforme.
2. Para la segunda, se reduce la probabilidad de extraer una observación cuyo resultado se solape mucho con lo ya extraído. Se recalcula la unicidad de cada candidato **condicionada a la secuencia de extracciones realizada hasta ahora**, y las probabilidades se reescalan para sumar 1.
3. Se repite hasta completar `I` extracciones.

`[LDP]` **La propiedad clave**: los solapamientos —e incluso las repeticiones— **siguen siendo posibles, pero cada vez menos probables**. La muestra resultante está mucho más cerca de IID que la del bootstrap estándar, lo cual puede verificarse midiendo el aumento de la unicidad media.

`[LDP]` **Resultado experimental**: en experimentos Monte Carlo, la mediana de la unicidad media fue **0.6 con el método estándar y 0.7 con el secuencial**, con un test ANOVA sobre la diferencia de medias que arroja una probabilidad ínfima. Estadísticamente, las muestras del bootstrap secuencial tienen una unicidad esperada mayor a cualquier nivel de confianza razonable.

`[INTERPRETACIÓN]` La mejora de 0.6 a 0.7 es real pero **modesta**. Y el coste computacional es alto: el algoritmo recalcula la unicidad media de **todos** los candidatos en **cada** extracción, lo cual es cuadrático en el número de observaciones. Sobre datos intradiarios con cientos de miles de eventos, esto es un problema serio. Es un candidato claro para la matriz de mínima complejidad (§26): **resuelve un problema real, pero la solución 2 (limitar `max_samples`) resuelve una parte importante del mismo problema a coste casi nulo.**

### 8.7 Ponderación por atribución de retornos

`[LDP]` Además de muestrear mejor, hay que **ponderar** las muestras. El razonamiento: los resultados muy solapados tendrían pesos desproporcionados si se consideraran iguales a los no solapados; y al mismo tiempo, **las etiquetas asociadas a retornos absolutos grandes deberían tener más importancia que las asociadas a retornos despreciables**. Hay que ponderar por una función de **ambas cosas**: unicidad y retorno absoluto.

**La construcción**: para cada observación, se suman los **log-retornos de cada instante de su vida divididos por la concurrencia en ese instante**, y se toma el valor absoluto. Los pesos se reescalan para sumar `I` (porque las librerías asumen peso por defecto de 1). Se usan **log-retornos porque son aditivos**.

`[LDP]` El racional: ponderar una observación en función de **los log-retornos absolutos que pueden atribuírsele de forma única**.

`[LDP]` **Y la limitación declarada**: el método **no funciona si existe un caso neutro**. Para ese caso, los retornos menores deberían recibir pesos mayores, no lo recíproco. **De ahí su consejo general de eliminar los casos neutros.** (Ver §7.5.)

### 8.8 Time decay

`[LDP]` **El racional**: los mercados son sistemas adaptativos; a medida que evolucionan, **los ejemplos antiguos son menos relevantes que los nuevos**. Por tanto queremos que los pesos decaigan conforme llegan observaciones nuevas.

**La construcción**: una función lineal a trozos gobernada por un parámetro `c`, donde la observación más reciente recibe peso 1 y las demás se ajustan relativamente. Los casos:

| Valor de `c` | Comportamiento |
|---|---|
| `c = 1` | Sin decaimiento temporal. |
| `0 < c < 1` | Decaimiento lineal, pero **toda observación recibe peso estrictamente positivo**, por antigua que sea. |
| `c = 0` | Los pesos convergen linealmente a cero al envejecer. |
| `c < 0` | **La porción más antigua de las observaciones recibe peso cero**, es decir, se borra de la memoria. |
| `c > 1` | Técnicamente posible: pesos que aumentan con la antigüedad. El autor lo señala como no necesariamente práctico. |

`[LDP]` **El detalle sutil e importante**: el decaimiento **no opera sobre tiempo cronológico**, sino sobre **unicidad acumulada**, porque un decaimiento cronológico reduciría los pesos demasiado rápido en presencia de observaciones redundantes.

`[INTERPRETACIÓN]` Esa elección tiene una consecuencia elegante: en períodos de alta actividad (muchos eventos solapados), el "tiempo" del decaimiento avanza despacio; en períodos de calma, avanza deprisa. El decaimiento se mide en unidades de información, no de reloj. Para un sistema intradiario, esto puede ser más razonable que cualquier ventana de calendario.

### 8.9 Class weights

`[LDP]` Corrigen etiquetas infrarrepresentadas, algo **crítico cuando las clases más importantes son raras**. El ejemplo: predecir crisis de liquidez como el flash crash. Estos eventos son raros frente a los millones de observaciones intermedias; **si no asignamos pesos mayores a esas muestras, el algoritmo maximizará la precisión de las etiquetas más comunes y los flash crashes serán tratados como outliers en lugar de como eventos raros**.

`[LDP]` Recomendaciones concretas: en aplicaciones financieras con etiquetas {−1, 1} **no hay razón para favorecer la precisión de una clase sobre la otra**, por lo que un buen valor por defecto es el balanceo, que reponderar para simular que todas las clases aparecen con igual frecuencia. En clasificadores de bagging, conviene considerar la variante que aplica el balanceo **a las muestras bootstrapeadas dentro de bolsa** en lugar de al dataset completo.

### 8.10 Compatibilidad y aplicabilidad a IRIS

| Elemento | Clasificación | Nota |
|---|---|---|
| Concurrencia y unicidad media | **`OHLCV-OK`** | Sólo requiere el objeto `t1` producido por el etiquetado. |
| Sequential bootstrap | **`OHLCV-OK`** | Pero coste computacional cuadrático. |
| Atribución de retornos | **`OHLCV-OK`** | Sólo requiere log-retornos y concurrencia. |
| Time decay | **`OHLCV-OK`** | — |
| Class weights | **`OHLCV-OK`** | — |

`[IMPLICACIÓN PARA IRIS]` Este capítulo es, junto con el 3 y el 7, **el que cierra el vacío más grave que dejó Jansen**. Jansen reconocía que las etiquetas solapadas filtran información y que los datos no son IID, pero no ofrecía forma de cuantificarlo. Aquí tenemos la formalización completa **y es enteramente implementable con nuestros datos**.

`[VACÍO]` Lo que sigue sin responder: **cuál es el número efectivo de observaciones independientes de nuestro histórico concreto de MNQ**. La unicidad media nos da un multiplicador, pero requiere haber fijado antes el esquema de etiquetado y el de muestreo. Es una dependencia circular que sólo se resuelve experimentando.


---

## 9. ESTACIONARIEDAD VS MEMORIA Y DIFERENCIACIÓN FRACCIONARIA (Tarea 7)

### 9.1 El dilema

`[LDP]` El planteamiento, en su forma más nítida:

- Las series financieras exhiben **ratios señal/ruido bajos** como consecuencia de las fuerzas de arbitraje.
- **Para empeorarlo, las transformaciones estacionarias estándar —la diferenciación entera— reducen aún más esa señal al eliminar memoria.**
- Las series de precios **tienen memoria**, porque cada valor depende de una larga historia de niveles previos.
- Las series diferenciadas de forma entera, como los retornos, tienen un **corte de memoria**: la historia se descarta enteramente después de una ventana muestral finita.
- Una vez que las transformaciones de estacionariedad han borrado toda la memoria, los estadísticos recurren a técnicas matemáticas complejas para extraer la señal residual que quede. **No sorprende que aplicar técnicas complejas sobre series con la memoria borrada conduzca probablemente a falsos descubrimientos.**

`[LDP]` **Por qué necesitamos estacionariedad**: los algoritmos supervisados requieren típicamente features estacionarias, porque **necesitamos mapear una observación previamente no vista a una colección de ejemplos etiquetados e inferir de ellos su etiqueta**. Si las features no son estacionarias, no podemos mapear la observación nueva a un número grande de ejemplos conocidos.

`[LDP]` **Pero**: la estacionariedad **no garantiza poder predictivo**. Es una condición **necesaria pero no suficiente** para el buen rendimiento de un algoritmo de ML.

`[LDP]` **Por qué necesitamos memoria**: rara vez en procesamiento de señales queremos que toda la memoria sea borrada, **porque esa memoria es la base del poder predictivo del modelo**. Los modelos de equilibrio necesitan algo de memoria para evaluar cuánto se ha desviado el proceso de precios de su valor esperado a largo plazo y así generar una previsión.

`[LDP]` **El dilema formulado**: los retornos son estacionarios pero sin memoria; los precios tienen memoria pero no son estacionarios. La pregunta que se plantea es: **¿cuál es la cantidad mínima de diferenciación que hace estacionaria una serie de precios preservando tanta memoria como sea posible?**

`[LDP]` Y la reformulación conceptual que se deriva: bajo este marco, **los retornos son sólo un tipo de transformación de precios entre muchas otras posibles, y en la mayoría de casos subóptimo**. La diferenciación cero es tan arbitraria como la diferenciación en un paso; entre esos dos extremos hay una región amplia que puede explorarse.

`[LDP]` Y una pregunta retórica que vale la pena registrar: **¿es la sobre-diferenciación una razón por la que la literatura ha estado tan sesgada a favor de la hipótesis de mercados eficientes?**

### 9.2 El método

`[LDP]` Se generaliza el operador de diferencia a pasos no enteros. Aplicando la expansión binomial formal al operador de retardo elevado a un exponente real `d`, se obtiene una serie de pesos que multiplican los valores rezagados de la serie.

**El comportamiento de los pesos:**
- **Con `d` entero positivo**, todos los pesos más allá de `d` son cero, y **la memoria más allá de ese punto queda cancelada**. Para `d = 1` (los retornos), los pesos son {1, −1, 0, 0, …}.
- **Con `d` real no entero**, los pesos nunca llegan exactamente a cero: **decaen asintóticamente**, como producto infinito de factores dentro del círculo unidad.
- Para `d` entre 0 y 1, todos los pesos posteriores al primero son **negativos y mayores que −1**.
- **La alternancia de signos de los pesos es lo que hace estacionaria la serie resultante**, a medida que la memoria se desvanece o se compensa a largo plazo.

**Los pesos se generan iterativamente** mediante una recursión sencilla a partir del peso anterior, lo cual hace el cálculo barato.

### 9.3 Las dos implementaciones

`[LDP]`

**Ventana expansiva.** Como la serie es finita, el valor fraccionalmente diferenciado no puede calcularse sobre una serie infinita de pesos. Los primeros puntos tendrán una cantidad de memoria distinta de los últimos. Se define la **pérdida relativa de peso** y, dado un nivel de tolerancia, se determina cuántos puntos iniciales deben descartarse.

**El problema de la ventana expansiva**: `[LDP]` **produce una deriva negativa**, causada por los pesos negativos que se van añadiendo a las observaciones iniciales conforme la ventana se expande. Sin controlar la pérdida de peso, la deriva es extrema, hasta el punto de que sólo se ve esa tendencia. Controlándola, la deriva se modera pero persiste.

**FFD — ventana de ancho fijo.** El método nuevo que propone: se fija un umbral de corte para los pesos, lo que determina un ancho de ventana constante, y se aplica esa misma ventana a toda la serie. `[LDP]` El resultado es **una mezcla sin deriva de nivel más ruido**. La distribución deja de ser gaussiana —por la asimetría y el exceso de curtosis que vienen con la memoria— **pero es estacionaria**.

### 9.4 Estacionariedad con preservación máxima de memoria

`[LDP]` El procedimiento operativo: aplicando FFD, calcular el **coeficiente mínimo `d*` tal que la serie resultante sea estacionaria**. Ese coeficiente **cuantifica cuánta memoria hay que eliminar para lograr estacionariedad**.

La interpretación de `d*`:
| Valor | Significado |
|---|---|
| `d* = 0` | La serie original ya es estacionaria. |
| `d* < 1` | La serie contiene una raíz unitaria. |
| `d* > 1` | La serie exhibe comportamiento explosivo (como en una burbuja). |
| `0 < d* ≪ 1` | **Caso de particular interés**: la serie original es "levemente no estacionaria". Aunque hace falta diferenciar, **una diferenciación entera completa elimina memoria excesiva (y poder predictivo)**. |

**La evidencia empírica que aporta** — y es la parte más contundente del capítulo:

Sobre log-precios del futuro E-mini S&P 500, rolados con el ETF trick y remuestreados a frecuencia diaria desde el inicio del contrato:
- La serie original tiene un estadístico ADF de **−0.3387**.
- La serie de retornos tiene un ADF de **−46.9114**.
- El valor crítico al 95% de confianza es **−2.8623**.
- **El estadístico cruza ese umbral en el entorno de `d = 0.35`.**
- **A `d = 0.35`, la correlación con la serie original sigue siendo 0.995.**
- **La correlación entre la serie original y la de retornos es sólo 0.03.**

`[LDP]` La conclusión que extrae: la diferenciación entera estándar **borra la memoria de la serie casi por completo**. Y sobre **87 de los futuros más líquidos del mundo**, en todos los casos el `d = 1` habitual implica **sobre-diferenciación**; en todos ellos se alcanza estacionariedad con `d < 0.6`, y la gran mayoría son estacionarios con `d < 0.3`. En algunos casos (zumo de naranja, ganado vivo) **no hacía falta diferenciación alguna**.

`[INTERPRETACIÓN]` La cifra que hay que retener es el par 0.995 / 0.03. No dice que el fracdiff prediga mejor: dice que **conserva casi toda la información de nivel mientras satisface el requisito estadístico**, mientras que los retornos conservan un 3%. Si esa información de nivel tiene contenido predictivo, la diferenciación entera lo tira. **Si no lo tiene, el fracdiff sólo añade una variable correlacionada con el precio y por tanto un canal directo para el sobreajuste.** El libro demuestra lo primero (la preservación) pero **no demuestra lo segundo** (que se traduzca en mejor predicción).

### 9.5 Qué problema podría resolver esto en IRIS, y cómo decidirlo

`[IMPLICACIÓN PARA IRIS]` El problema concreto que atacaría: si en MNQ existe información en **el nivel relativo del precio** —distancia a un equilibrio, posición dentro de un rango, memoria de niveles previos— nuestras features basadas en retornos y en indicadores normalizados la habrán descartado. El fracdiff es un candidato a recuperarla en forma utilizable por el modelo.

**Sobre qué aplicarlo — las tres opciones planteadas en el encargo:**

| Objeto | Valoración |
|---|---|
| **Precio → feature** | Es el uso que el libro describe y demuestra. `OHLCV-OK`. El candidato principal. |
| **Otras features** | `[LDP]` No lo desarrolla explícitamente para features derivadas, pero **sí recomienda, en el capítulo 18, codificar la información desde series fraccionalmente diferenciadas en lugar de enteramente diferenciadas** al estimar entropía. Eso es un uso sobre una feature. Extensible conceptualmente a cualquier feature no estacionaria. |
| **Target** | `[VACÍO]` **El libro no propone en ningún momento aplicar fracdiff al target.** Su target es la triple barrera, que opera sobre precios crudos. Aplicarlo al target sería una invención nuestra, sin respaldo en esta fuente. |

**Criterios para decidir después (no ahora):**
1. **¿Cuál es `d*` para nuestra serie de MNQ, a nuestra frecuencia?** Es un cálculo barato y una de las primeras cosas que deberíamos medir sobre nuestros datos reales.
2. **¿Qué correlación conserva con la serie original a ese `d*`?** Si es alta, el argumento del libro se replica en nuestros datos.
3. **¿Aporta información incremental sobre los retornos?** Este es el criterio decisivo, y hay una herramienta directa para medirlo: **MDA y SFI con purged CV (§12)**, comparando un conjunto de features con y sin la variable fracdiff.
4. **¿Sobrevive el aporte a la ortogonalización?** Si la contribución del fracdiff desaparece al aplicar PCA, era redundante.
5. **¿A qué coste?** El FFD tiene una ventana fija que puede ser larga para valores pequeños de `d`, lo cual consume datos al inicio de la serie y añade coste computacional.

`[INTERPRETACIÓN]` Advertencia específica de nuestro caso: la evidencia del libro es sobre **series diarias** de futuros a lo largo de décadas, donde los niveles de precio difieren enormemente entre regímenes. En **intradiario**, dentro de una sesión, el rango de precios es estrecho y la no estacionariedad es de otra naturaleza. **No hay garantía de que `d*` intradiario en MNQ se parezca a `d*` diario en ES.** Es una pregunta empírica abierta y una razón concreta para no adoptar la técnica por analogía.

`[IMPLICACIÓN PARA IRIS]` Y un riesgo que merece nombrarse: una feature con correlación 0.995 con el precio es, funcionalmente, casi el precio. En un backtest, **una feature casi idéntica al precio es un vehículo eficientísimo para memorizar la historia concreta de la muestra**. La estacionariedad estadística no protege de eso. Cualquier uso del fracdiff en IRIS debe validarse con especial dureza fuera de muestra.

---

## 10. MÉTODOS DE ENSEMBLE (Tarea 8)

### 10.1 Las tres fuentes de error

`[LDP]`
1. **Sesgo (bias)**: error causado por supuestos irrealistas. Con sesgo alto, el algoritmo no ha reconocido relaciones importantes entre features y resultados. Se dice que está *underfit*.
2. **Varianza**: error causado por la sensibilidad a cambios pequeños en el conjunto de entrenamiento. Con varianza alta, el algoritmo ha sobreajustado, y por eso cambios mínimos producen predicciones radicalmente distintas. **En lugar de modelar los patrones generales, ha confundido ruido con señal.**
3. **Ruido**: error causado por la varianza de los valores observados —cambios impredecibles o errores de medición—. **Es el error irreducible**, que ningún modelo puede explicar.

`[LDP]` Un método de ensemble combina un conjunto de aprendices débiles, todos basados en el mismo algoritmo, para crear uno más fuerte. **Los ensembles ayudan a reducir sesgo y/o varianza.**

### 10.2 Bagging: por qué funciona y cuándo deja de funcionar

`[LDP]` **Mecánica**: generar N conjuntos de entrenamiento por muestreo aleatorio con reemplazo; ajustar N estimadores independientemente (por tanto, **paralelizables**); y promediar. Para variables categóricas, la probabilidad de pertenencia a una clase es la proporción de estimadores que la votan; si el estimador base produce probabilidades, el clasificador de bagging puede promediarlas.

**Reducción de varianza — el resultado clave.** `[LDP]` La varianza de la predicción embolsada depende de tres cosas: el número de estimadores `N`, la varianza media de una predicción individual, y **la correlación media entre las predicciones**. La conclusión es inequívoca:

> **El bagging sólo es efectivo en la medida en que la correlación media sea menor que 1. Cuando esa correlación tiende a 1, la varianza de la predicción embolsada tiende a la varianza de un estimador individual, sin importar cuántos estimadores usemos.**

`[LDP]` **Y aquí se cierra el círculo con el capítulo 4**: uno de los objetivos del sequential bootstrap es **producir muestras lo más independientes posible, reduciendo así esa correlación media**, lo que debería reducir la varianza de los clasificadores de bagging.

**Mejora de la precisión.** `[LDP]` Para un `N` suficientemente grande, si la precisión individual supera el azar, la precisión del clasificador de bagging **excede la precisión media de los clasificadores individuales**. Es un argumento fuerte a favor de embolsar cualquier clasificador cuando los requisitos computacionales lo permitan.

`[LDP]` **Pero, a diferencia del boosting, el bagging no puede mejorar la precisión de clasificadores malos**: si los aprendices individuales son pobres, la votación por mayoría seguirá siendo pobre (aunque con menor varianza). Y su síntesis: **como es más fácil lograr correlación media baja que precisión individual alta, el bagging tiene más probabilidad de éxito reduciendo varianza que reduciendo sesgo.**

### 10.3 Redundancia de observaciones — el problema central en finanzas

`[LDP]` Los dos efectos perjudiciales ya expuestos en §8.4:
1. **La correlación media tiende a 1** → el bagging no reduce varianza.
2. **La precisión out-of-bag queda inflada** → porque el muestreo con reemplazo coloca en entrenamiento muestras muy similares a las que quedan fuera.

`[LDP]` Y la consecuencia práctica: en tal caso, una **k-fold estratificada correcta sin barajar antes de particionar mostrará una precisión de test mucho menor que la estimada out-of-bag**. Por esa razón, aconseja usar k-fold sin barajado **e ignorar los resultados de precisión out-of-bag**. Prefiere además un `k` bajo a uno alto, porque un particionado excesivo volvería a colocar en test muestras demasiado similares a las de entrenamiento.

### 10.4 Random Forest

`[LDP]` **Diferencia clave con el bagging**: incorpora un segundo nivel de aleatoriedad — al optimizar cada división de nodo, sólo se evalúa **un submuestreo aleatorio (sin reemplazo) de los atributos**, con el propósito de descorrelacionar aún más los estimadores.

**Ventajas**: reduce la varianza sin sobreajustar (mientras la correlación media sea menor que 1); **evalúa la importancia de features**; y proporciona estimaciones de precisión out-of-bag (que, advierte, **en aplicaciones financieras probablemente estén infladas**). Como el bagging, **no necesariamente exhibirá menor sesgo** que los árboles individuales.

`[LDP]` **El problema específico**: si hay muchas muestras redundantes, **el sobreajuste seguirá ocurriendo**: el muestreo aleatorio con reemplazo construirá un gran número de árboles esencialmente idénticos, cada uno sobreajustado. Y a diferencia del bagging, **el RF fija siempre el tamaño de las muestras bootstrapeadas al del dataset de entrenamiento**.

**Las cinco formas de corregirlo que propone:**
1. Bajar `max_features`, forzando discrepancia entre árboles.
2. **Early stopping**: fijar un valor suficientemente grande (p. ej. 5%) para la fracción mínima de peso por hoja.
3. Embolsar árboles de decisión, fijando `max_samples` a la unicidad media.
4. Embolsar un RF de un solo árbol sin bootstrap, con `max_samples` igual a la unicidad media.
5. **Modificar la clase RF para sustituir el bootstrap estándar por el sequential bootstrap.**

`[LDP]` Dos recomendaciones adicionales: **ajustar el RF sobre un PCA de las features**, porque una rotación del espacio de features alineada con los ejes reduce típicamente el número de niveles necesarios, acelerando cálculos y reduciendo algo de sobreajuste. Y usar balanceo de clases dentro de las submuestras para evitar que los árboles clasifiquen mal las clases minoritarias.

### 10.5 Boosting y la comparación en finanzas

`[LDP]` **Mecánica del boosting**: los clasificadores se ajustan **secuencialmente**; los de rendimiento pobre **se descartan**; las observaciones se ponderan de forma distinta en cada iteración (más peso a las mal clasificadas); y la previsión final es un promedio ponderado por la precisión individual.

`[LDP]` **La comparación, que es una toma de posición explícita:**

> **El boosting reduce tanto varianza como sesgo, pero corregir el sesgo tiene el coste de un mayor riesgo de sobreajuste. Podría argumentarse que en aplicaciones financieras el bagging es en general preferible al boosting. El bagging ataca el sobreajuste, mientras el boosting ataca el infraajuste. El sobreajuste suele ser una preocupación mayor que el infraajuste, porque no es difícil sobreajustar un algoritmo de ML a datos financieros, dado el bajo ratio señal/ruido. Además, el bagging puede paralelizarse, mientras que el boosting requiere generalmente ejecución secuencial.**

`[INTERPRETACIÓN]` Esta es una posición **distinta** de la que domina la práctica actual (donde el gradient boosting es el estándar de facto para datos tabulares). No es una prueba, es un argumento basado en la asimetría del riesgo. Merece ser tratado como una **hipótesis a testear** en IRIS, no como un veredicto: probar ambos y comparar bajo purged CV es barato y es exactamente la clase de decisión que el encargo pide mantener abierta.

### 10.6 Bagging para escalabilidad

`[LDP]` Un uso adicional: si el estimador base no escala bien con el tamaño muestral (cita SVM), se puede construir un bagging donde el estimador base tenga una **condición de parada temprana muy estricta**. Esto transforma una tarea secuencial grande en muchas pequeñas ejecutables simultáneamente. La parada temprana aumenta la varianza de las salidas individuales, pero **ese aumento puede quedar más que compensado por la reducción de varianza asociada al bagging**, controlable añadiendo más estimadores base independientes.

### 10.7 Compatibilidad y relevancia

**Clasificación: `OHLCV-OK`** en su totalidad.

`[IMPLICACIÓN PARA IRIS]` Lo que este capítulo aporta no es la elección de modelo, sino **una restricción de configuración**: cualquier ensemble que usemos en IRIS debe configurarse teniendo en cuenta la unicidad media de nuestras muestras, y **no debemos fiarnos de la precisión out-of-bag**. Sin esa corrección, un Random Forest sobre datos intradiarios solapados producirá un bosque de copias de un mismo árbol sobreajustado, con una métrica out-of-bag que nos dirá que todo va bien.

`[VACÍO]` El libro **no compara empíricamente** familias de modelos ni ofrece evidencia de que unas funcionen mejor que otras en finanzas. Es deliberado: declara ser agnóstico respecto al algoritmo. Por tanto **no aporta base para elegir el modelo de IRIS**, sólo para configurarlo correctamente.

---

## 11. CROSS-VALIDATION FINANCIERA: PURGING Y EMBARGO (Tarea 9)

Bloque crítico.

### 11.1 El objetivo real de la cross-validation

`[LDP]` El propósito de la CV es **determinar el error de generalización de un algoritmo, para prevenir el sobreajuste**. Y la advertencia inmediata: la CV es otra instancia donde las técnicas estándar fallan al aplicarse a problemas financieros. **El sobreajuste ocurrirá, y la CV no será capaz de detectarlo. De hecho, la CV contribuirá al sobreajuste a través del tuning de hiperparámetros.**

`[LDP]` La formulación de por qué importa: cuando se testea un algoritmo sobre el mismo dataset con el que se entrenó, los resultados son espectaculares. Usados así, **los algoritmos de ML no se distinguen de algoritmos de compresión con pérdida: resumen los datos con fidelidad extrema y poder predictivo cero.**

`[LDP]` La CV divide observaciones **extraídas de un proceso IID** en entrenamiento y test, y cada observación pertenece a uno y sólo uno de los conjuntos, **para prevenir fuga de un conjunto al otro**, que anularía el propósito de testear sobre datos no vistos.

### 11.2 Por qué el k-fold falla en finanzas

`[LDP]` **Dos razones:**

**Razón 1 — las observaciones no pueden asumirse extraídas de un proceso IID.**

**Razón 2 — el conjunto de test se usa múltiples veces** durante el desarrollo del modelo, conduciendo a multiple testing y sesgo de selección.

`[LDP]` Y una valoración sin matices: si has leído artículos financieros que presentan evidencia de k-fold CV de que un algoritmo funciona bien, **es casi seguro que esos resultados son erróneos**.

**El mecanismo de la fuga**, explicado con precisión: consideremos una feature `X` con correlación serial asociada a etiquetas `Y` formadas sobre datos solapados.
- Por la correlación serial, `X_t ≈ X_{t+1}`.
- Por el solapamiento de las etiquetas, `Y_t ≈ Y_{t+1}`.
- **Al colocar `t` y `t+1` en conjuntos distintos, se filtra información.** Un clasificador entrenado con `(X_t, Y_t)` y luego preguntado por `Y_{t+1}` dado `X_{t+1}` **tiene más probabilidad de acertar aunque `X` sea una feature irrelevante**.

`[LDP]` **Y aquí está el punto crítico**: si `X` es una feature predictiva, la fuga **mejora el rendimiento de una estrategia que ya era valiosa**. **El problema es la fuga en presencia de features irrelevantes, porque eso conduce a falsos descubrimientos.**

`[LDP]` **Precisión sobre cuándo hay fuga realmente**: si `X_i` y `X_j` se forman sobre información solapada, con `i` en entrenamiento y `j` en test, **eso no es necesariamente fuga, mientras `Y_i` e `Y_j` sean independientes**. Para que haya fuga debe ocurrir que el **par completo** `(X_i, Y_i)` sea aproximadamente igual al par `(X_j, Y_j)`; **no basta con que `X_i ≈ X_j` ni siquiera con que `Y_i ≈ Y_j`**.

`[INTERPRETACIÓN]` Este matiz es importante y suele perderse. La fuga no es "las features se parecen": es **la coincidencia conjunta de features y etiqueta**. Eso explica por qué la solución no es eliminar features correlacionadas sino purgar por solapamiento de etiquetas.

`[LDP]` **Dos vías para reducir la probabilidad de fuga:**
1. **Eliminar del entrenamiento toda observación cuya etiqueta sea función de información usada para determinar una etiqueta del test.** En particular, las etiquetas no deberían abarcar períodos solapados.
2. **Evitar sobreajustar el clasificador**, para que aunque haya algo de fuga no pueda aprovecharla: parada temprana de los estimadores base, y bagging controlando el sobremuestreo de observaciones redundantes.

### 11.3 Purging — qué se purga y por qué

`[LDP]` **Definición**: purgar del conjunto de entrenamiento **todas las observaciones cuyas etiquetas se solaparon en el tiempo con las etiquetas incluidas en el conjunto de test**.

**El criterio formal**: se elimina la observación `i` de entrenamiento siempre que `Y_i` e `Y_j` (con `j` en test) sean **concurrentes** en el sentido del capítulo 4 — es decir, que ambas etiquetas dependan de al menos una extracción aleatoria común. En el contexto de la triple barrera, esto significa que ambas etiquetas dependen del retorno entre sus respectivas barras de inicio y primer toque.

`[LDP]` Y una observación práctica: **si el conjunto de test es contiguo** —sin observaciones de entrenamiento intercaladas entre la primera y la última observación de test— **el purging puede acelerarse** tratando todo el test como un único intervalo.

`[LDP]` **La relación con `k`**: cuanto mayor sea el número de particiones de test, mayor será el número de observaciones solapadas en entrenamiento. En muchos casos el purging basta para prevenir la fuga, y entonces **el rendimiento mejorará al aumentar `k`, porque permitimos al modelo recalibrar más a menudo. Pero más allá de cierto `k*`, el rendimiento dejará de mejorar, lo que indica que el backtest ya no se está aprovechando de fugas.**

`[INTERPRETACIÓN]` Ese es un **diagnóstico operativo muy útil**: si el rendimiento sigue mejorando indefinidamente al aumentar `k`, hay fuga residual. Es una prueba que podemos ejecutar sobre IRIS.

### 11.4 Embargo — qué se embarga y por qué

`[LDP]` **Definición**: para los casos en que el purging no elimina toda la fuga, se impone un embargo sobre las observaciones de entrenamiento **posteriores** a cada conjunto de test.

**La justificación de la asimetría**, que es el punto esencial:

> **El embargo no necesita afectar a las observaciones de entrenamiento anteriores al conjunto de test, porque las etiquetas de entrenamiento que terminan antes de que empiece el test contienen información que ya estaba disponible en el momento del test. Sólo nos preocupan las etiquetas de entrenamiento que ocurren inmediatamente después del test.**

`[LDP]` **La causa de la fuga residual que el embargo ataca**: las features financieras incorporan a menudo series con correlación serial (como procesos ARMA). Por eso debemos eliminar del entrenamiento las observaciones que **siguen inmediatamente** a una observación del test.

`[LDP]` **La magnitud**: un valor pequeño, del orden de **el 1% de la longitud total de la serie**, suele bastar para prevenir toda la fuga. Y da el test de verificación: comprobar que **el rendimiento no mejora indefinidamente al aumentar `k` hacia `T`**.

### 11.5 La diferencia entre purging y embargo — resumen

| | **Purging** | **Embargo** |
|---|---|---|
| **Qué elimina** | Observaciones de entrenamiento **cuyas etiquetas se solapan temporalmente** con etiquetas del test. | Observaciones de entrenamiento **inmediatamente posteriores** al test, dentro de una ventana `h`. |
| **Dirección** | Bidireccional (antes y después del test). | **Sólo hacia adelante.** |
| **Causa que ataca** | Solapamiento de los intervalos de las etiquetas. | **Correlación serial de las features**, que sobrevive al solapamiento de etiquetas. |
| **Criterio** | Concurrencia entre `[t_i,0, t_i,1]` y `[t_j,0, t_j,1]`. | Ventana fija posterior al fin del test. |
| **Necesario en walk-forward** | **Sí.** | `[LDP]` **No**, porque en WF el entrenamiento siempre precede al test. |

### 11.6 Ejemplo conceptual aplicado al MNQ

`[IMPLICACIÓN PARA IRIS]` Instanciando el ejemplo que pide el encargo. Supongamos:
- Barras de un minuto.
- Una observación generada a las **10:00**, etiquetada por triple barrera, cuyo primer toque de barrera ocurre a las **10:30**. Es decir, su etiqueta depende del camino de precios en `[10:00, 10:30]`.
- Esa observación de las 10:00 pertenece al **conjunto de test**.

**Qué debe purgarse del entrenamiento:**
- **Toda observación de entrenamiento cuyo intervalo `[t0, t1]` intersecte `[10:00, 10:30]`.** Esto incluye:
  - Observaciones **anteriores** a las 10:00 cuya barrera aún no se había tocado a las 10:00. Ejemplo: una observación de las 09:45 cuyo primer toque fue a las 10:12. Su etiqueta depende parcialmente del mismo tramo de precios. **Se purga.**
  - Observaciones **iniciadas dentro** de `[10:00, 10:30]`, por ejemplo a las 10:10, independientemente de cuándo terminen. **Se purgan.**
- Nótese que el alcance hacia atrás **no es fijo**: depende de cuánto duraron las etiquetas previas. Con triple barrera, una observación de las 09:15 con barrera vertical larga y sin toque previo puede seguir viva a las 10:00. Purgar correctamente exige mirar `t1`, **no** aplicar una ventana constante.

**Qué debe embargarse:**
- Observaciones de entrenamiento **iniciadas justo después de las 10:30**, dentro de una ventana `h`. Por ejemplo, si `h` equivale al 1% de la muestra, y esto son 60 minutos, se eliminarían las observaciones de entrenamiento iniciadas entre las 10:30 y las 11:30.
- **Por qué**: aunque su etiqueta ya no se solapa con la del test, sus **features** —medias móviles, volatilidades, indicadores con ventana— fueron calculadas con datos que incluyen el tramo `[10:00, 10:30]`. Esa correlación serial es el canal residual de fuga.

`[INTERPRETACIÓN]` Consecuencia práctica que conviene anticipar: **en intradiario con horizontes de decenas de minutos, purging + embargo pueden eliminar una fracción sustancial del conjunto de entrenamiento alrededor de cada frontera de fold.** Cuantos más folds, más fronteras, más pérdida. Es un coste real que interactúa con la elección de `k` y con el horizonte de etiquetado, y que debemos medir sobre nuestros datos.

### 11.7 El error de implementación que el libro señala

`[LDP]` Menciona explícitamente el error frecuente en backtests walk-forward: **que el índice de inicio de la etiqueta caiga en el conjunto de entrenamiento, pero el momento de resolución de la etiqueta caiga dentro del conjunto de test**. Es decir, mirar sólo dónde empieza la observación y no dónde termina.

`[LDP]` Y advierte además de **bugs conocidos en la implementación de cross-validation de scikit-learn**, recomendando implementar la puntuación con la clase purgada propia en lugar de usar las funciones estándar de la librería. Su comentario general: hay que leer siempre el código que se ejecuta, y esta es una razón fuerte a favor del código abierto.

### 11.8 Compatibilidad

**Clasificación: `OHLCV-OK`.** Purged K-Fold requiere únicamente el objeto `t1` y el índice temporal. Nada más.

`[IMPLICACIÓN PARA IRIS]` Este capítulo cierra por completo un vacío que Jansen dejó explícitamente abierto (él nombraba purging, embargoing y CV combinatoria y las atribuía a esta fuente sin desarrollarlas). Ahora tenemos el mecanismo, el criterio y el diagnóstico. **Y es implementable con nuestros datos sin ninguna condición.**

---

## 12. FEATURE IMPORTANCE (Tarea 10)

### 12.1 Por qué importa: el argumento contra investigar con backtests

`[LDP]` Abre el capítulo con la descripción del error que considera más extendido en investigación financiera: **tomar datos, pasarlos por un algoritmo de ML, hacer backtest de las predicciones, y repetir la secuencia hasta que aparezca un backtest bonito**. Las revistas académicas están llenas de esos pseudo-descubrimientos, y grandes fondos caen constantemente en la trampa.

`[LDP]` **No importa que el backtest sea walk-forward fuera de muestra. El hecho de repetir un test una y otra vez sobre los mismos datos conducirá probablemente a un falso descubrimiento.** Este error metodológico es tan notorio entre estadísticos que lo consideran fraude científico, y la asociación estadística americana advierte contra él en sus directrices éticas.

`[LDP]` **La cifra**: típicamente hacen falta **unas 20 iteraciones** para "descubrir" una estrategia falsa al nivel de significación estándar del 5%.

### 12.2 Qué aporta la importancia de features como herramienta de investigación

`[LDP]` La secuencia correcta: ajustar un clasificador sobre `(X, y)`, evaluar el error de generalización mediante **purged k-fold CV**, y si el rendimiento es bueno, **preguntarse qué features contribuyeron a él**. Quizá podamos añadir features que refuercen la señal responsable del poder predictivo, o eliminar las que sólo añaden ruido.

`[LDP]` **Y lo que se abre a continuación** — esta lista es, en mi lectura, el programa de investigación que el libro propone como alternativa al ciclo de backtests:

> ¿Son estas features importantes **todo el tiempo**, o sólo en entornos específicos? **¿Qué desencadena un cambio de importancia en el tiempo? ¿Pueden predecirse esos cambios de régimen?** ¿Son también relevantes para otros instrumentos relacionados? ¿Para otras clases de activo? ¿Cuáles son las features más relevantes en todo el universo? ¿Cuál es el subconjunto con mayor correlación de rangos a lo largo del universo?

`[LDP]` Y su valoración: **entender la importancia de features abre la proverbial caja negra.** Podemos comprender los patrones identificados por el clasificador si entendemos qué fuente de información le resulta indispensable. La metáfora que usa: los cazadores no comen ciegamente todo lo que sus perros les traen.

`[IMPLICACIÓN PARA IRIS]` Las preguntas sobre estabilidad temporal de la importancia y predictibilidad de los cambios de régimen son **directamente traducibles a un instrumento único**, sin necesidad de universo. Son probablemente el programa de investigación más productivo que esta fuente ofrece a IRIS.

### 12.3 Efectos de sustitución — el problema clave para nosotros

`[LDP]` **Definición**: un efecto de sustitución ocurre cuando **la importancia estimada de una feature se reduce por la presencia de otras features relacionadas**. Son el análogo en ML de lo que la estadística y la econometría llaman **multicolinealidad**.

`[LDP]` Una forma de atacar los efectos de sustitución **lineales** es aplicar PCA sobre las features crudas y realizar el análisis de importancia sobre las features ortogonales.

`[LDP]` **Cuándo importa y cuándo no**: los efectos de sustitución pueden llevarnos a descartar features importantes que resultan ser redundantes. **Esto no suele ser un problema en el contexto de la predicción, pero puede conducirnos a conclusiones erróneas cuando intentamos entender, mejorar o simplificar un modelo.**

`[IMPLICACIÓN PARA IRIS]` Este es exactamente el problema que planteaba el encargo. Con features derivadas de OHLCV —EMA, SMA, MACD, momentum, ROC— estamos describiendo parcialmente el mismo fenómeno con distintas parametrizaciones. **La respuesta directa a la pregunta "¿cómo puede una feature verdaderamente útil parecer poco importante?"**: porque un árbol que ya ha dividido por la EMA de 20 no ganará casi nada dividiendo después por la SMA de 21; la reducción de impureza se la lleva la primera que llega, y el orden entre features casi equivalentes es esencialmente aleatorio entre árboles. La importancia se **reparte arbitrariamente** entre sustitutos, y una feature genuinamente informativa puede quedar sepultada bajo sus propias copias.

### 12.4 Los tres métodos

#### MDI — Mean Decrease Impurity

`[LDP]`
- **Qué es**: método **rápido, explicativo (in-sample) y específico de clasificadores basados en árboles**. En cada nodo de cada árbol, la feature seleccionada divide el subconjunto reduciendo impureza; podemos derivar cuánta de la reducción total de impureza corresponde a cada feature, promediar entre estimadores y rankear.
- **Propiedades**: las importancias **suman 1**, lo que permite un umbral natural: si todas las features fueran igualmente importantes, cada una tendría importancia `1/N`. Las que superen ese umbral se distinguen de features indistinguibles.
- **Sujeto a efectos de sustitución**: sí.
- **Detalle de implementación**: para evitar enmascaramiento, se usa `max_features=1` (cada nodo considera una única feature al azar) y se reemplazan los ceros por valores faltantes al promediar.
- **Resultado experimental sobre datos sintéticos** (10 informativas, 10 redundantes, 20 ruido, 10.000 observaciones): MDI hizo **un trabajo muy bueno** colocando todas las informativas y redundantes por encima del umbral, con una única excepción marginal. **Los efectos de sustitución hicieron que algunas informativas o redundantes se rankearan mejor que otras, lo cual era esperable.**

#### MDA — Mean Decrease Accuracy

`[LDP]`
- **Qué es**: método **lento, predictivo (out-of-sample)**. Se ajusta el clasificador, se deriva su rendimiento fuera de muestra según algún score, se **permuta cada columna de features de una en una**, y se recalcula el rendimiento tras cada permutación. La importancia es función de la pérdida de rendimiento causada por la permutación.
- **Se aplica con purged k-fold CV** y con log-loss negativo o accuracy.
- **Propiedad distintiva**: la mejora **puede ser negativa**, lo que significa que **la feature es realmente perjudicial** para el poder predictivo del algoritmo. Y **MDA puede concluir que todas las features son irrelevantes**, porque el rendimiento se evalúa fuera de muestra.
- **Sujeto a efectos de sustitución**: sí, y `[LDP]` señala que las sustituciones **subestiman significativamente** la importancia medida por MDA.
- **Resultado experimental**: también funcionó bien, con una excepción probablemente debida a sustitución. Aspecto negativo: **desviaciones estándar de las medias algo mayores**, corregible aumentando el número de particiones de la purged CV de 10 a 100, al coste de diez veces el tiempo de cómputo sin paralelización.

`[INTERPRETACIÓN]` La propiedad de que MDA puede declarar **todas** las features irrelevantes es la que lo hace valioso como test de realidad. MDI siempre repartirá importancia entre las features disponibles, aunque todas sean ruido; MDA no.

#### SFI — Single Feature Importance

`[LDP]`
- **Qué es**: método **transversal y predictivo (fuera de muestra)** que calcula el score de cada feature **en aislamiento**.
- **Ventajas**: aplicable a cualquier clasificador, no sólo árboles; no limitado a accuracy; **no hay efectos de sustitución**, porque sólo se considera una feature a la vez; y como MDA, puede concluir que todas son irrelevantes.
- **Limitación central**: `[LDP]` **se pierden los efectos conjuntos y la importancia jerárquica**. La feature B puede ser útil **sólo en combinación** con la feature A; o B puede ser útil para **explicar las divisiones generadas por A**, aunque B sola sea imprecisa. Una alternativa sería calcular el score sobre subconjuntos de features, pero el cálculo se vuelve intratable al crecer el número.

### 12.5 Features ortogonales

`[LDP]` **Procedimiento**: estandarizar la matriz de features, calcular autovalores y autovectores, y derivar las features ortogonales por proyección.

**Las dos razones para estandarizar**: (1) centrar los datos asegura que la primera componente principal está correctamente orientada en la dirección principal de las observaciones, equivalente a añadir intercepto en una regresión; (2) **reescalar hace que el PCA se centre en explicar correlaciones en lugar de varianzas** — sin reescalar, las primeras componentes estarían dominadas por las columnas de mayor varianza y no aprenderíamos mucho sobre la estructura.

`[LDP]` **Tres beneficios**:
1. Mitiga los efectos de sustitución **lineales** (no todos).
2. Permite **reducir dimensionalidad** descartando features asociadas a autovalores pequeños, lo que suele acelerar la convergencia.
3. **Y el más interesante — evidencia confirmatoria contra el sobreajuste.**

**El tercer argumento, desarrollado**: `[LDP]` un algoritmo de ML **siempre encontrará un patrón, aunque ese patrón sea una casualidad estadística**. Debemos ser siempre escépticos ante las features supuestamente importantes identificadas por cualquier método. Ahora bien: el PCA ha determinado qué features son más "principales" **sin conocimiento alguno de las etiquetas** (aprendizaje no supervisado). Es decir, **ha rankeado features sin posibilidad alguna de sobreajuste en sentido clasificatorio**. Si MDI, MDA o SFI —que sí usan la información de etiquetas— seleccionan como más importantes **las mismas features** que el PCA eligió como principales, **eso constituye evidencia confirmatoria de que el patrón identificado no está enteramente sobreajustado.** Si las features fueran enteramente aleatorias, el ranking PCA no tendría correspondencia con el ranking de importancia.

**La métrica**: la **tau de Kendall ponderada** entre las importancias y los autovalores asociados (o el rango PCA inverso). Cuanto más cerca de 1, mayor la consistencia. `[LDP]` El argumento para preferir la versión ponderada sobre la estándar: **queremos priorizar la concordancia de rango entre las features más importantes**; la concordancia entre features irrelevantes (probablemente ruidosas) no nos interesa. En su ejemplo, la correlación de Pearson entre autovalores e importancias MDI fue 0.8491 con p-valor ínfimo, y la tau de Kendall hiperbólicamente ponderada 0.8206.

`[IMPLICACIÓN PARA IRIS]` **Este test es directamente aplicable a IRIS y no requiere universo multiactivo.** Es una de las pocas comprobaciones anti-sobreajuste del libro que funciona sobre un solo instrumento. Debería estar en nuestro protocolo.

### 12.6 Paralelizada vs apilada — y la tensión con IRIS

`[LDP]` **Dos enfoques de investigación:**

**Paralelizada**: para cada instrumento del universo se forma un dataset y se deriva la importancia por separado; luego se agregan los resultados. `[LDP]` **Las features importantes a lo largo de una amplia variedad de instrumentos tienen más probabilidad de estar asociadas a un fenómeno subyacente**, particularmente cuando las importancias exhiben alta correlación de rangos entre criterios. Puede merecer la pena estudiar en profundidad el mecanismo teórico que las hace predictivas. Ventaja: rápido y paralelizable. Desventaja: por efectos de sustitución, las features importantes pueden intercambiar rangos entre instrumentos, aumentando la varianza de la estimación — **desventaja que se vuelve relativamente menor si promediamos sobre un universo suficientemente grande**.

**Apilada (features stacking)**: apilar todos los datasets en uno combinado, tras transformarlos para asegurar homogeneidad distribucional (por ejemplo, estandarización sobre ventana móvil). **El clasificador debe aprender qué features son más importantes a lo largo de todos los instrumentos simultáneamente, como si el universo entero fuera un único instrumento.** Ventajas: dataset mucho mayor; importancia derivada directamente sin esquema de ponderación; **conclusiones más generales y menos sesgadas por outliers o sobreajuste**; y las importancias no se amortiguan por promediado.

`[LDP]` **Su preferencia declarada**: prefiere habitualmente el apilado, **no sólo para importancia de features sino siempre que un clasificador pueda ajustarse sobre un conjunto de instrumentos, incluido para predicción**. Razón: **reduce la probabilidad de sobreajustar un estimador a un instrumento particular o a un dataset pequeño.**

`[IMPLICACIÓN PARA IRIS]` **Aquí la tensión con nuestro diseño es directa y no debe suavizarse.** Ambos enfoques que el autor propone requieren un universo de instrumentos, y su justificación explícita para preferir el apilado es precisamente evitar sobreajustar a un instrumento único — que es exactamente lo que IRIS es por diseño. Esta limitación se desarrolla en §28.

`[INTERPRETACIÓN]` Lo que sí podemos rescatar del principio sin el universo: la idea subyacente es **buscar consistencia de la importancia a lo largo de contextos distintos**. En un instrumento único, los "contextos" pueden ser **períodos temporales, regímenes de volatilidad o franjas horarias** en lugar de instrumentos. Comprobar que una feature es importante en 2019, en 2022 y en 2024, o en régimen de volatilidad alta y baja, es un análogo defendible —**más débil** que el original, porque los períodos del mismo instrumento están más relacionados entre sí que instrumentos distintos, pero no vacío. Esto es interpretación propia, no propuesta del libro.

### 12.7 Compatibilidad

| Elemento | Clasificación |
|---|---|
| MDI | **`OHLCV-OK`** (requiere clasificador de árboles) |
| MDA con purged CV | **`OHLCV-OK`** |
| SFI | **`OHLCV-OK`** |
| Ortogonalización PCA + Kendall tau ponderada | **`OHLCV-OK`** |
| Importancia paralelizada | **`OTRAS FUENTES`** |
| Features stacking | **`OTRAS FUENTES`** |

---

## 13. HYPER-PARAMETER TUNING (Tarea 11)

### 13.1 El problema y la conexión con el capítulo 7

`[LDP]` El tuning de hiperparámetros es un paso esencial; hecho mal, el algoritmo sobreajustará y el rendimiento en vivo decepcionará. La literatura de ML presta atención especial a validar cruzadamente cualquier hiperparámetro tuneado. **Y como la CV en finanzas es un problema especialmente difícil donde las soluciones de otros campos probablemente fallen, el tuning debe hacerse con el método purged k-fold.**

`[LDP]` La forma de evitar reintroducir fuga es directa: **pasar la clase `PurgedKFold` como generador de CV** a la búsqueda de hiperparámetros, en lugar del generador por defecto. De lo contrario, la búsqueda **sobreajustará el estimador a información filtrada**.

### 13.2 Grid search y randomized search

`[LDP]`
- **Grid search**: búsqueda exhaustiva de la combinación que maximiza el rendimiento de CV. **Enfoque razonable como primera aproximación cuando no sabemos mucho sobre la estructura subyacente de los datos.**
- **Randomized search**: para algoritmos con muchos parámetros, la búsqueda exhaustiva se vuelve computacionalmente intratable. Muestrear cada parámetro de una distribución tiene **dos beneficios**: (1) **controlamos el número de combinaciones exploradas, independientemente de la dimensionalidad del problema** —el equivalente a un presupuesto computacional—; (2) tener parámetros relativamente irrelevantes **no aumenta sustancialmente el tiempo de búsqueda**, como sí ocurriría con grid search.
- **Distribución log-uniforme**: para hiperparámetros que sólo aceptan valores no negativos y cuya respuesta no es lineal. El razonamiento: si muestreamos uniformemente entre 0 y 100, el 99% de los valores serían mayores que 1; pero un modelo puede responder tanto a un aumento de 0.01 a 1 como de 1 a 100. Muestrear de forma que **el logaritmo de las extracciones se distribuya uniformemente** explora mejor la región factible.

### 13.3 La elección de la función de scoring — un punto sustantivo

`[LDP]` Su recomendación es específica y merece registrarse con precisión:

**Para meta-labeling: `f1`.** La razón: supongamos una muestra con un número muy grande de casos negativos. Un clasificador que prediga todos los casos como negativos **alcanzará accuracy alta o buen log-loss negativo, aunque no haya aprendido nada de las features sobre cómo discriminar**. De hecho, ese modelo logra recall cero y precisión indefinida. **El F1 corrige esa inflación** puntuando en términos de precisión y recall.

**Para el resto de aplicaciones: log-loss negativo, no accuracy.** `[LDP]` En aplicaciones no de meta-labeling está bien usar accuracy o log-loss porque nos interesan igualmente todas las clases. Pero **recomienda log-loss negativo cuando se tunean hiperparámetros para una estrategia de inversión**.

`[LDP]` **La diferencia conceptual clave**, que aparece explícitamente en el capítulo 14: **el log-loss negativo tiene en cuenta no sólo si las predicciones fueron correctas, sino también la probabilidad de esas predicciones.**

`[INTERPRETACIÓN]` El razonamiento subyacente, que el libro conecta con el capítulo 10: si el tamaño de la apuesta se deriva de la probabilidad predicha, **entonces equivocarse con alta confianza es mucho más costoso que equivocarse con baja confianza, y la accuracy no distingue entre ambos casos.** La accuracy trata todas las predicciones como apuestas del mismo tamaño. En una estrategia que dimensiona por confianza, esa métrica está desalineada con el PnL. Los propios ejercicios del capítulo 9 apuntan a esto: preguntan qué método de scoring conduce a mayor Sharpe, y plantean explícitamente que si una estrategia dimensiona sus apuestas por igual independientemente de la confianza, **la función de scoring apropiada cambia**.

`[IMPLICACIÓN PARA IRIS]` Esta es una regla de diseño con consecuencias: **la métrica de tuning debe elegirse en función de cómo IRIS vaya a dimensionar las posiciones.** Si el tamaño depende de la confianza → log-loss. Si el tamaño es fijo → accuracy es defendible. Es una decisión acoplada, no independiente.

### 13.4 El riesgo de probar mil configuraciones

`[LDP]` La afirmación clave, en la apertura del capítulo 7: **la CV contribuirá al sobreajuste a través del tuning de hiperparámetros.** Y en el capítulo 8: bastan unas 20 iteraciones para encontrar una estrategia falsa al 5%.

`[INTERPRETACIÓN]` La lógica encadenada, aplicada al escenario del encargo:
1. Probamos 1.000 configuraciones bajo purged CV. El purging elimina la fuga **entre train y test dentro de cada evaluación**, pero no hace nada respecto a que **el mismo conjunto de test se está usando 1.000 veces**.
2. Aunque ninguna configuración tenga habilidad real, **el máximo de 1.000 estimaciones ruidosas será claramente positivo**. Es exactamente el fundamento del Deflated Sharpe Ratio (§18).
3. Seleccionamos ese máximo y lo interpretamos como descubrimiento.
4. **El purged CV no nos protege de esto en absoluto.** Protege contra un mecanismo distinto.

`[IMPLICACIÓN PARA IRIS]` Consecuencias operativas:
- El número de configuraciones probadas **debe registrarse** y entrar en el cálculo del DSR.
- La búsqueda aleatoria con presupuesto explícito es preferible a la búsqueda exhaustiva **no sólo por coste computacional sino por control del multiple testing**.
- El score de CV de la mejor configuración **no es un estimador insesgado** de su rendimiento; hace falta un conjunto que no haya participado en la selección.

`[VACÍO]` El libro **no ofrece un procedimiento para corregir el score de CV por el número de configuraciones probadas en el tuning**. El DSR corrige el Sharpe de estrategias, no el score de validación de hiperparámetros. Es un vacío operativo relevante.

### 13.5 Compatibilidad

**Clasificación: `OHLCV-OK`.**


---

## 14. BET SIZING (Tarea 12)

### 14.1 El problema

`[LDP]` La formulación de apertura es directa: **tu algoritmo puede alcanzar alta precisión, pero si no dimensionas bien las apuestas, tu estrategia perderá dinero inevitablemente.**

`[LDP]` El ejemplo que lo demuestra: dos estrategias sobre el mismo instrumento, ambas con previsiones que resultaron correctas (el precio subió un 25% entre el inicio y el final). La primera produjo la secuencia de tamaños [0.5, 1, 0]; la segunda [1, 0.5, 0], porque se vio forzada a reducir el tamaño cuando el mercado se movió contra la posición inicial completa. **La primera ganó dinero; la segunda perdió.** Misma previsión, mismo acierto direccional, resultados de signo opuesto.

`[LDP]` Y el principio que se deriva: **preferimos dimensionar posiciones de forma que reservemos algo de efectivo para la posibilidad de que la señal se refuerce antes de debilitarse.**

### 14.2 Enfoques independientes de la estrategia

`[LDP]` Tres alternativas:

**(1) Vía mezcla de gaussianas sobre la concurrencia de apuestas.** Se calcula la serie de concurrencia neta (apuestas largas concurrentes menos cortas concurrentes), derivada igual que la concurrencia de etiquetas del capítulo 4. Se ajusta una **mezcla de dos gaussianas** sobre esa serie, y el tamaño se deriva de su función de distribución. **La intuición**: podríamos dimensionar al 0.9 cuando la probabilidad de observar una señal de mayor valor es sólo 0.1. **Cuanto más fuerte es la señal, menor es la probabilidad de que se vuelva aún más fuerte, y por tanto mayor el tamaño.**

**(2) Enfoque de presupuesto.** Se calcula el número máximo (o algún cuantil) de apuestas largas concurrentes y de cortas concurrentes, y el tamaño se deriva como la proporción respecto de esos máximos. **El objetivo es que no se alcance la posición máxima antes de que se dispare la última señal concurrente.**

**(3) Meta-labeling.** Ajustar un clasificador para determinar la probabilidad de clasificación errónea, y usar esa probabilidad para derivar el tamaño. `[LDP]` **Dos ventajas**: primero, el algoritmo que decide los tamaños **es independiente del modelo primario**, lo que permite incorporar features predictivas de falsos positivos; segundo, **la probabilidad predicha se traduce directamente en tamaño de apuesta**.

### 14.3 De probabilidad a tamaño

`[LDP]` **Caso binario.** Denotando `p[x]` la probabilidad de que la etiqueta `x` ocurra, con dos resultados posibles, se testea la hipótesis nula de que la probabilidad es 1/2. Se calcula un **estadístico z** que sigue una normal estándar, y **el tamaño se deriva como `m = 2·Z[z] − 1`**, donde `Z[·]` es la CDF de la normal estándar. El resultado está acotado en [−1, 1].

`[LDP]` **Caso multiclase.** Se sigue un método uno-contra-el-resto. Se toma la probabilidad máxima como la probabilidad de la clase predicha, y se testea contra la hipótesis nula de equiprobabilidad (1 dividido por el número de clases). **El tamaño resultante es `m = x·(2·Z[z] − 1)`**, donde el lado viene implicado por la etiqueta `x`. Nótese que las etiquetas se identifican por el tamaño de apuesta asociado a ellas.

`[INTERPRETACIÓN]` **Este es el mecanismo exacto por el que la abstención emerge sin necesidad de una clase "no operar".** Si la probabilidad predicha es cercana a la del azar, el estadístico z es cercano a cero, la CDF vale ≈ 0.5, y el tamaño es ≈ 0. La decisión de no operar no es una categoría: es el límite continuo de la falta de confianza. Esto es la respuesta técnica al argumento de §7.5 de que la clase neutra es innecesaria.

### 14.4 Promediado de apuestas activas

`[LDP]` Toda apuesta lleva asociado un período de tenencia, desde su origen hasta el primer toque de barrera. Un enfoque posible sería **sobrescribir una apuesta antigua cuando llega una nueva; pero eso probablemente conduzca a un turnover excesivo**. Un enfoque más sensato es **promediar todos los tamaños de todas las apuestas todavía activas en un instante dado**.

**Regla**: una señal está activa si fue emitida en o antes del instante actual **y** el instante actual precede al fin de la señal (o su fin es aún desconocido). Si no hay señales activas, el tamaño es cero.

`[IMPLICACIÓN PARA IRIS]` Este mecanismo resuelve un problema que Jansen no abordaba: **qué hacer cuando llega una señal nueva mientras hay una posición abierta**. El promediado de apuestas activas es una respuesta concreta y coherente con el marco de la triple barrera.

### 14.5 Discretización

`[LDP]` El promediado reduce parte del exceso de turnover, pero **sigue siendo probable que cada predicción dispare operaciones pequeñas**. Como ese temblor causaría sobretrading innecesario, sugiere **discretizar el tamaño redondeando a un paso `d` entre 0 y 1**, que determina el grado de discretización.

`[INTERPRETACIÓN]` Con esto, la abstención aparece por tercera vía: **cualquier tamaño por debajo de medio paso colapsa exactamente a cero**. El parámetro `d` se convierte, de hecho, en un umbral implícito de "no operar", y su elección es una decisión con consecuencias económicas directas sobre el turnover.

### 14.6 Tamaños dinámicos y precios límite

`[LDP]` En el intervalo entre el origen de la apuesta y su resolución, el precio fluctúa y pueden formarse previsiones adicionales. Propone un método para **ajustar el tamaño conforme el precio de mercado y el precio previsto divergen o convergen**, y derivar en el proceso el **precio límite de la orden**.

**Mecánica**: el tamaño objetivo se define mediante una **función sigmoide** de la divergencia entre el precio previsto y el precio actual, escalada por la posición máxima absoluta y redondeada a entero. `[LDP]` **Propiedad clave: conforme el precio de mercado se acerca al previsto, el tamaño objetivo tiende a cero, porque el algoritmo quiere realizar las ganancias.**

**El precio límite** se deriva de la función inversa, y la propiedad que garantiza es que, al ser monótona, **el algoritmo no puede realizar pérdidas conforme el precio converge a la previsión**. El precio límite resultante queda entre el precio actual y el previsto.

**Calibración**: el coeficiente que regula la anchura de la sigmoide se calibra a partir de un par definido por el usuario (una divergencia de precio y el tamaño deseado para esa divergencia).

`[INTERPRETACIÓN]` Este mecanismo es notable porque **acopla el sizing con la ejecución**: no sólo dice cuánto, sino a qué precio. Para IRIS es una extensión posible, pero implica un sistema de gestión de órdenes considerablemente más complejo que "entrar y esperar a una barrera". Va a la categoría de extensión futura.

### 14.7 La relación probabilidad → confianza → tamaño → abstención

`[IMPLICACIÓN PARA IRIS]` Recogiendo la cadena completa que el libro habilita, respondiendo a la pregunta del encargo:

```
MODELO SECUNDARIO
   ↓  probabilidad p de que la apuesta del primario sea correcta
ESTADÍSTICO z
   ↓  contraste contra la hipótesis nula de ausencia de habilidad
TAMAÑO CONTINUO m ∈ [−1, 1]
   ↓  m = 2·Z[z] − 1  (o su versión multiclase)
PROMEDIADO DE APUESTAS ACTIVAS
   ↓  control de turnover, coherencia entre señales concurrentes
DISCRETIZACIÓN
   ↓  redondeo a pasos de tamaño d
TAMAÑO FINAL
   ↓  m = 0  ⟹  NO OPERAR
POSICIÓN
```

Tres observaciones sobre esta cadena:
1. **La abstención no requiere una clase propia.** Emerge tres veces: por probabilidad cercana al azar, por promediado que cancela señales opuestas, y por discretización.
2. **La confianza es una cantidad medida, no declarada.** Es el estadístico z respecto a una hipótesis nula explícita.
3. **Requiere probabilidades utilizables.** `[VACÍO]` **El libro no aborda la calibración de probabilidades.** Asume que el clasificador produce probabilidades que incorporan información sobre la bondad del ajuste o la confianza, y remite a referencias externas. Si las probabilidades de nuestro modelo están mal calibradas, toda la cadena hereda ese error. Este vacío es importante y persiste después de esta fuente.

### 14.8 Compatibilidad

| Elemento | Clasificación |
|---|---|
| Sizing desde probabilidades | **`OHLCV-OK`** |
| Promediado de apuestas activas | **`OHLCV-OK`** |
| Discretización | **`OHLCV-OK`** |
| Tamaños dinámicos y precios límite | **`OHLCV-OK`** conceptualmente; requiere infraestructura de órdenes |
| Sizing por mezcla de gaussianas sobre concurrencia | **`OHLCV-OK`** |

---

## 15. LOS PELIGROS DEL BACKTESTING (Tarea 13)

### 15.1 Misión imposible: el backtest impecable

`[LDP]` **Un backtest es una hipótesis, no un experimento.** En un laboratorio de física se puede repetir un experimento controlando las variables ambientales, para deducir una relación causa-efecto precisa. **Un backtest no es un experimento y no demuestra nada.** No garantiza nada — **ni siquiera alcanzar ese Sharpe si pudiéramos viajar atrás en el tiempo**: las extracciones aleatorias habrían sido distintas. El pasado no se repetiría.

`[LDP]` **¿Cuál es entonces el sentido de un backtest?** Es una **comprobación de sanidad sobre varias variables**: bet sizing, turnover, resistencia a costes, y comportamiento bajo un escenario dado. Un buen backtest puede ser extremadamente útil, pero hacerlo bien es extremadamente difícil.

**Los siete pecados** (recogidos de un estudio de un equipo de quants que él cita y recomienda):
1. **Survivorship bias**: usar como universo el actual, ignorando quiebras y exclusiones.
2. **Look-ahead bias**: usar información que no era pública en el momento de la decisión simulada. **Hay que tener certeza sobre el timestamp de cada dato**, teniendo en cuenta fechas de publicación, retrasos de distribución y correcciones retroactivas.
3. **Storytelling**: inventar una historia a posteriori para justificar un patrón aleatorio.
4. **Data mining y data snooping**: entrenar el modelo sobre el conjunto de test.
5. **Costes de transacción**: simularlos es difícil porque **la única forma de estar seguro del coste habría sido interactuar con el libro de órdenes**, es decir, hacer la operación real.
6. **Outliers**: basar una estrategia en unos pocos resultados extremos que pueden no repetirse.
7. **Shorting**: ponerse corto en productos cash requiere encontrar un prestamista; el coste y la disponibilidad son generalmente desconocidos.

`[LDP]` Y añade una lista de errores adicionales: calcular rendimiento con método no estándar; ignorar riesgos ocultos; centrarse sólo en retornos ignorando otras métricas; confundir correlación con causalidad; seleccionar un período no representativo; no esperar lo inesperado; ignorar la existencia de límites de stop-out o margin calls; ignorar costes de financiación.

`[IMPLICACIÓN PARA IRIS]` De los siete pecados, los que aplican directamente a nuestro caso son **look-ahead (2), storytelling (3), data snooping (4), costes (5) y outliers (6)**. El survivorship bias (1) no aplica a un instrumento único, y el shorting (7) no aplica a futuros, donde ponerse corto es simétrico. **Pero aparece un pecado análogo específico nuestro: el tratamiento del roll de contratos** (§4), que es nuestro equivalente funcional del ajuste por acciones corporativas.

### 15.2 Aunque sea impecable, probablemente esté equivocado

`[LDP]` El argumento, que es el más incómodo del libro y merece registrarse en su lógica completa:

Enhorabuena: tu backtest es impecable, reproducible, con supuestos tan conservadores que ni tu jefe podría objetarlos. Has pagado por cada operación más del doble de lo que nadie podría pedir. Has ejecutado horas después de que la información fuera conocida por medio mundo, a una tasa de participación ridículamente baja. Y aun así, tu backtest gana mucho dinero.

**Y sin embargo, ese backtest impecable probablemente esté equivocado. ¿Por qué? Porque sólo un experto puede producir un backtest impecable. Y ser experto significa haber ejecutado decenas de miles de backtests a lo largo de los años. En conclusión, este no es tu primer backtest, y hay que contabilizar la posibilidad de que sea un falso descubrimiento — una casualidad estadística que inevitablemente aparece tras ejecutar múltiples tests sobre los mismos datos.**

`[LDP]` **Lo enloquecedor del backtesting es que cuanto mejor te vuelves en ello, más probable es que aparezcan falsos descubrimientos.** Los principiantes caen en los siete pecados. **Los profesionales producen backtests impecables y siguen cayendo en multiple testing, sesgo de selección y backtest overfitting.**

### 15.3 El backtesting no es una herramienta de investigación

`[LDP]` La tesis central del capítulo:

- Que unas features sean muy importantes **no significa que puedan monetizarse** mediante una estrategia.
- **A la inversa, abundan las estrategias que parecerán rentables aun estando basadas en features irrelevantes.**
- **La importancia de features es una herramienta de investigación verdadera**, porque nos ayuda a entender la naturaleza de los patrones descubiertos por el algoritmo, **independientemente de su monetización**. Y críticamente, **se deriva ex-ante, antes de simular el rendimiento histórico**.
- **Un backtest no es una herramienta de investigación.** Nos da muy poca visión sobre la razón por la que una estrategia habría ganado dinero. **Igual que el ganador de la lotería puede sentir que hizo algo para merecer su suerte, siempre hay una historia a posteriori.**

`[LDP]` La analogía que emplea contra los cientos de "alfas" publicados: lo que esos autores han encontrado son **los boletos de lotería que ganaron el sorteo anterior**. El ganador ya ha cobrado, y esos números son inútiles para la ronda siguiente. **Nunca nos cuentan cuántos boletos se vendieron**, es decir, los millones de simulaciones que hicieron falta para encontrar esos alfas "afortunados".

`[LDP]` **Las tres reglas operativas que se derivan:**
1. **El propósito de un backtest es descartar modelos malos, no mejorarlos.**
2. **Ajustar el modelo en función de los resultados del backtest es una pérdida de tiempo... y es peligroso.**
3. **Nunca hacer backtest hasta que el modelo esté completamente especificado. Si el backtest falla, empezar de cero.**

`[LDP]` Dónde invertir el esfuerzo, entonces: en hacer bien todos los componentes —datos estructurados, etiquetado, ponderación, ensembles, cross-validation, importancia de features, bet sizing—. **Para cuando estás haciendo backtest, ya es demasiado tarde.**

### 15.4 Las seis recomendaciones generales

`[LDP]`
1. **Desarrollar modelos para clases de activos o universos completos, no para valores específicos.** Los inversores diversifican, luego no cometen el error X sólo en el valor Y. **Si encuentras el error X sólo en el valor Y, por rentable que parezca, probablemente sea un falso descubrimiento.**
2. **Aplicar bagging** como medio para prevenir el sobreajuste y reducir la varianza del error de previsión. **Si el bagging deteriora el rendimiento de una estrategia, esta estaba probablemente sobreajustada a un número pequeño de observaciones o a outliers.**
3. **No hacer backtest hasta que toda la investigación esté completa.**
4. **Registrar cada backtest ejecutado sobre un dataset**, para poder estimar la probabilidad de backtest overfitting sobre el resultado finalmente seleccionado y deflactar apropiadamente el Sharpe por el número de intentos.
5. **Simular escenarios en lugar de historia.** Un backtest estándar es una simulación histórica, fácil de sobreajustar. **La historia es sólo el camino aleatorio que se realizó, y podría haber sido enteramente distinto. La estrategia debería ser rentable bajo un rango amplio de escenarios, no sólo bajo el camino histórico anecdótico. Es más difícil sobreajustar el resultado de miles de escenarios "qué pasaría si".**
6. **Si el backtest no identifica una estrategia rentable, empezar de cero.** Resistir la tentación de reutilizar esos resultados.

`[IMPLICACIÓN PARA IRIS]` La recomendación 2 es especialmente útil porque es un **test diagnóstico ejecutable**: aplicar bagging y observar si el rendimiento se deteriora. Si se deteriora, tenemos evidencia de sobreajuste a pocas observaciones. Es barato y es aplicable a un instrumento único.

La recomendación 1 es la que choca frontalmente con nuestro diseño y se trata en §28.

### 15.5 Selección de estrategias y la probabilidad de backtest overfitting

`[LDP]` **Por qué el walk-forward no basta como validación**: sin muestreo aleatorio, **hay un único camino de testeo que puede repetirse una y otra vez hasta que aparezca un falso positivo**. Como en la CV estándar, hace falta algo de aleatorización para evitar este tipo de optimización sobre el backtest, mientras se evita la filtración de ejemplos correlacionados.

`[LDP]` **El método CSCV** (combinatorially symmetric cross-validation) para estimar la **PBO** (probability of backtest overfitting):

1. Se forma una matriz `M` recogiendo las **series de rendimiento (PnL) de los N intentos** realizados. Cada columna es una configuración probada; cada fila una observación, **sincronizadas entre intentos**.
2. Se parte `M` por filas en un número **par** `S` de submatrices disjuntas de igual dimensión.
3. Se forman **todas las combinaciones** de esas submatrices tomadas en grupos de tamaño `S/2`. Con `S = 16`, esto da **12.780 combinaciones**.
4. Para cada combinación: se forma el conjunto de entrenamiento uniendo las `S/2` submatrices; el conjunto de test es su complemento; se calcula el rendimiento de cada configuración en entrenamiento; se identifica la mejor configuración **in-sample**; y se determina el **rango relativo de esa misma configuración en el conjunto de test**.
5. Se define un logit de ese rango relativo, que vale cero cuando el rendimiento OOS de la configuración elegida coincide con la mediana.
6. **La PBO es la probabilidad de que las estrategias óptimas in-sample rindan por debajo de la mediana fuera de muestra.**

`[LDP]` Las dos condiciones que impone: que `M` sea una matriz verdadera con observaciones sincronizadas, y que la métrica de evaluación pueda estimarse sobre submuestras de cada columna (si es el Sharpe, que el supuesto IID normal se sostenga sobre distintos tramos). Si las configuraciones operan a frecuencias distintas, las observaciones se agregan a un índice común.

`[LDP]` Y el detalle metodológico importante: **las observaciones dentro de cada subconjunto preservan la secuencia temporal original. El muestreo aleatorio se hace sobre los subconjuntos relativamente no correlacionados, no sobre las observaciones.**

`[LDP]` El resultado visual que reporta: al graficar el Sharpe in-sample de la mejor estrategia seleccionada contra su Sharpe out-of-sample, se aprecia **un decaimiento del rendimiento fuerte y persistente, causado por el backtest overfitting**.

**Clasificación: `OHLCV-OK`** — CSCV opera sobre series de PnL, no sobre datos de mercado.

---

## 15.bis CÓMO PODRÍAMOS FABRICAR ACCIDENTALMENTE UN IRIS ESPECTACULAR Y COMPLETAMENTE FALSO

Sección construida a partir de las advertencias de esta fuente, instanciada sobre nuestro caso. Cada escenario está formulado como algo que **haríamos de buena fe**.

---

### Escenario 1 — El clásico: investigar con el backtest

**Qué haríamos:** probar un conjunto de features, entrenar, hacer backtest, ver que no funciona, cambiar el horizonte, volver a hacer backtest, cambiar el umbral del CUSUM, volver a hacer backtest, probar otro modelo, volver a hacer backtest.

**Por qué produce un IRIS falso:** `[LDP]` Bastan unas 20 iteraciones para descubrir una estrategia falsa al nivel de significación del 5%. **Que el backtest sea walk-forward fuera de muestra no cambia nada**: el problema es repetir el test sobre los mismos datos.

**Cómo se vería:** una curva de equity limpia obtenida tras semanas de iteración, cuyas iteraciones fallidas nadie recuerda ni ha registrado.

**Prevención:** completar toda la investigación —etiquetado, ponderación, validación, importancia de features— **antes** del primer backtest. Registrar cada intento desde el día uno. Si el backtest falla, empezar de cero en lugar de retocar.

---

### Escenario 2 — Etiquetas que no habrían sobrevivido

**Qué haríamos:** usar un target de horizonte fijo — el retorno a 30 minutos — porque es simple y es lo que hace toda la literatura.

**Por qué produce un IRIS falso:** `[LDP]` Es irrealista construir una estrategia que obtenga beneficio de posiciones que habrían sido cerradas forzosamente. Nuestro backtest contabilizaría como ganadoras operaciones que en la realidad habrían saltado por stop-loss o margin call antes de llegar al minuto 30.

**Cómo se vería:** un backtest que gana con drawdowns intra-operación que ningún operador ni ningún broker habría tolerado.

**Prevención:** evaluar el etiquetado dependiente del camino frente al de horizonte fijo, en lugar de asumir el segundo.

---

### Escenario 3 — Umbral fijo sobre barras temporales

**Qué haríamos:** etiquetar como "movimiento significativo" cualquier retorno superior a un umbral constante.

**Por qué produce un IRIS falso:** `[LDP]` La volatilidad de las barras varía enormemente entre la apertura y la sesión nocturna. Con umbral fijo, **la gran mayoría de etiquetas será neutra**, aunque el retorno fuera predecible y significativo; y las etiquetas no neutras se concentrarán sistemáticamente en las franjas horarias de alta volatilidad.

**Cómo se vería:** un modelo que parece funcionar y que en realidad **ha aprendido a reconocer la hora del día**.

**Prevención:** umbrales dinámicos escalados por volatilidad estimada.

---

### Escenario 4 — Un millón de filas que son diez mil observaciones

**Qué haríamos:** entrenar un Random Forest sobre un millón de barras de un minuto con etiquetas de 30 minutos, obtener una precisión out-of-bag excelente, y concluir que tenemos señal.

**Por qué produce un IRIS falso:** `[LDP]` Con etiquetas fuertemente solapadas, las muestras extraídas con reemplazo son casi idénticas, la correlación media entre árboles tiende a 1, **el bagging no reduce varianza en absoluto**, y todos los árboles son copias de un mismo árbol sobreajustado. **Y la precisión out-of-bag queda groseramente inflada**, porque las muestras fuera de bolsa son casi iguales a las de dentro.

**Cómo se vería:** OOB alta, k-fold sin barajar mucho más baja. Si sólo miramos la primera, no lo detectamos.

**Prevención:** calcular la unicidad media; fijar la fracción muestreada en consecuencia; **ignorar el OOB**; usar purged k-fold.

---

### Escenario 5 — Cross-validation que mira al otro lado

**Qué haríamos:** usar `TimeSeriesSplit` o un k-fold sin barajar, creyendo que respetar el orden temporal basta.

**Por qué produce un IRIS falso:** `[LDP]` Respetar el orden **no elimina el solapamiento de etiquetas**. Una observación de entrenamiento iniciada antes del corte cuya barrera se toca después del corte comparte información con el test. Y aunque no se solape, la **correlación serial de las features** mantiene el canal abierto. Y lo más pernicioso: **la fuga en presencia de features irrelevantes es lo que produce falsos descubrimientos**; con features buenas sólo infla un resultado que ya era real.

**Cómo se vería:** rendimiento de validación bueno que se desmorona en un hold-out realmente separado.

**Prevención:** purging por solapamiento de etiquetas **más** embargo posterior. Y el diagnóstico de LdP: aumentar `k` y verificar que el rendimiento **deja de mejorar** a partir de cierto punto. Si mejora indefinidamente, hay fuga residual.

---

### Escenario 6 — Mil configuraciones y un ganador

**Qué haríamos:** ejecutar una búsqueda de hiperparámetros amplia bajo purged CV —haciéndolo, creemos, todo bien— y quedarnos con la mejor.

**Por qué produce un IRIS falso:** `[LDP]` **La CV contribuye al sobreajuste a través del tuning.** El purging elimina la fuga dentro de cada evaluación, pero el mismo test se ha usado mil veces. Bajo la hipótesis nula de habilidad nula, **el máximo esperado de un conjunto de Sharpes estimados es mayor que cero, y crece rápidamente con el número de intentos independientes y con la varianza entre ellos** (§18.5).

**Cómo se vería:** una configuración "óptima" cuyo score de CV es un máximo muestral y no una estimación.

**Prevención:** presupuesto explícito de búsqueda (randomized search); registro del número de intentos; deflactar el Sharpe final; y un conjunto que no haya participado en la selección.

---

### Escenario 7 — El roll que aprendimos a predecir

**Qué haríamos:** descargar la serie continua de MNQ tal como la entrega la API, sin verificar el método de empalme.

**Por qué produce un IRIS falso:** `[LDP]` Los eventos que alteran la naturaleza de la serie introducen **rupturas estructurales** que desviarán la investigación. Un salto de roll no ajustado es un movimiento grande, en fechas conocidas y aproximadamente periódicas, **y de signo sistemático si el contrato está en contango o backwardation**. Un modelo con acceso a features de calendario o de tiempo hasta vencimiento **puede aprender a predecirlo**.

**Cómo se vería:** un backtest con beneficios concentrados en fechas próximas a los vencimientos trimestrales, con una historia a posteriori convincente sobre "efectos de vencimiento".

**Prevención:** ajustar el roll explícitamente por el método de gaps acumulados; usar precios rolados para PnL y **precios crudos para dimensionar**; y examinar la concentración temporal de beneficios (§18.3).

---

### Escenario 8 — Barreras calibradas sobre la muestra

**Qué haríamos:** probar varios pares de profit-taking y stop-loss y quedarnos con el que da mejor Sharpe.

**Por qué produce un IRIS falso:** `[LDP]` Es literalmente el ejemplo con el que abre el capítulo 13: **con sólo dos variables a maximizar sobre una muestra finita, es fácil sobreajustar la regla de trading. Un sobreajuste trivial ocurre cuando el par de barreras se ajusta a unos pocos outliers.** Y esos parámetros quedan tan atados al pasado que la estrategia se vuelve inservible para el futuro.

**Cómo se vería:** un par de umbrales sospechosamente específico, cuyo rendimiento cae drásticamente si los movemos un poco.

**Prevención:** derivar las barreras de la volatilidad estimada en lugar de optimizarlas; o derivarlas del proceso estocástico en lugar de por simulación histórica (§17); y **contar cada par probado como un intento**.

---

### Escenario 9 — La historia a posteriori

**Qué haríamos:** encontrar que una feature funciona y construir una explicación económica convincente sobre por qué.

**Por qué produce un IRIS falso:** `[LDP]` Es el tercer pecado: **storytelling — inventar una historia a posteriori para justificar un patrón aleatorio**. Y su analogía: siempre hay una explicación después del hecho, igual que el ganador de la lotería puede sentir que hizo algo para merecerlo.

**Cómo se vería:** indistinguible de un descubrimiento real, **por construcción**. Este escenario es especialmente peligroso porque la narrativa aumenta nuestra confianza sin aportar evidencia.

**Prevención:** la única defensa que ofrece el libro es de **secuencia y de test independiente**: una vez formulada la explicación teórica a partir del hallazgo, **testearla sobre un dataset independiente**. La teoría debe identificar el mecanismo por el cual otro participante nos pierde dinero, y ese mecanismo debe generar predicciones adicionales comprobables.

---

### Escenario 10 — Costes que no medimos

**Qué haríamos:** hacer el backtest ignorando comisiones y slippage, con intención de "añadirlos después".

**Por qué produce un IRIS falso:** `[LDP]` Simular costes de transacción es difícil porque **la única forma de estar seguro habría sido hacer la operación real**. Y en el capítulo 14 propone métricas específicas —**rendimiento en dólares por turnover**, que indica cuánto más caro podría volverse la ejecución antes de que la estrategia deje de ganar, y **retorno sobre costes de ejecución**, que debería ser un múltiplo grande para asegurar que la estrategia sobreviva a una ejecución peor de lo esperado—.

**Cómo se vería:** un sistema intradiario de alto turnover que gana antes de costes y pierde después.

**Prevención:** modelar costes desde el primer backtest, y **calcular el edge mínimo requerido antes de modelar**, usando el marco de riesgo de estrategia (§19).

---

### Escenario 11 — Un solo camino histórico

**Qué haríamos:** un walk-forward limpio, correctamente purgado, sobre todo nuestro histórico, obteniendo un Sharpe de 1.5.

**Por qué produce un IRIS falso:** `[LDP]` El WF testea **un único escenario, el camino histórico**, que es fácil de sobreajustar; **no es necesariamente representativo del rendimiento futuro**, porque los resultados pueden estar sesgados por la secuencia concreta de datos. Y el argumento que da es demoledor: **es tan fácil sobreajustar un backtest hacia adelante como uno hacia atrás, y el hecho de que cambiar la secuencia produzca resultados inconsistentes es evidencia de ese sobreajuste**. Si los defensores del WF tuvieran razón, deberíamos observar que los backtests hacia atrás superan sistemáticamente a los hacia adelante; y no es el caso.

**Cómo se vería:** un número. Un solo Sharpe, sin distribución, sin intervalo, sin idea de cuánto podría haber sido distinto.

**Prevención:** CPCV para obtener una **distribución** de Sharpes (§16); y el ejemplo aleccionador que el propio libro plantea como ejercicio: un WF con Sharpe 1.5 que bajo CPCV con muchos caminos arroja una media de −1 con desviación 0.5.

---

### Escenario 12 — Confundir precisión con rentabilidad

**Qué haríamos:** obtener un 70% de precisión y concluir que IRIS funciona.

**Por qué produce un IRIS falso:** `[LDP]` Con pagos asimétricos, el Sharpe depende de precisión, frecuencia **y de los propios pagos**. Su ejemplo: con 260 apuestas al año, stop en −1% y objetivo en +0.5%, una precisión del 70% da un Sharpe de 1.173; del 72%, un Sharpe de 2; **y del 67%, un Sharpe de 0** — es decir, una caída de tres puntos de precisión borra todos los beneficios. **La estrategia es intrínsecamente arriesgada aunque las posiciones no lo sean.**

**Prevención:** calcular la precisión implícita requerida y la **probabilidad de fracaso de la estrategia** antes de creer el resultado (§19).

---

### Escenario 13 — El feature que es casi el precio

**Qué haríamos:** aplicar fracdiff, encontrar el `d*` mínimo, y usar la serie resultante como feature porque conserva el 99.5% de la correlación con el precio.

**Por qué produce un IRIS falso:** `[INTERPRETACIÓN]` Una feature con correlación 0.995 con el precio es funcionalmente el precio. En una muestra concreta, el precio es un identificador casi único de cada momento histórico. **Un modelo con suficiente capacidad puede usarla para memorizar la historia**, y la estacionariedad estadística no lo impide en absoluto. El libro demuestra que el fracdiff preserva memoria; **no demuestra que esa memoria sea predictiva**.

**Prevención:** exigir que el fracdiff demuestre importancia bajo MDA y SFI fuera de muestra, y que su aporte sobreviva a la ortogonalización.

---

### Escenario 14 — Importancias que nos guían mal

**Qué haríamos:** calcular MDI, ver que la EMA de 20 es la feature más importante, y construir la teoría económica alrededor de ella.

**Por qué produce un IRIS falso:** `[LDP]` Los efectos de sustitución hacen que **la importancia estimada de una feature se reduzca por la presencia de otras relacionadas**. Con veinte medias móviles de longitudes parecidas, cuál queda arriba es en buena medida arbitrario. Construir la teoría sobre esa elección es construir sobre ruido.

**Prevención:** ortogonalizar antes de interpretar; combinar MDI con MDA y SFI; y usar la concordancia con el ranking PCA como evidencia confirmatoria.

---

## 16. BACKTESTING A TRAVÉS DE CROSS-VALIDATION: CPCV (Tarea 14)

### 16.1 Los dos sentidos de "backtest"

`[LDP]` Las observaciones pasadas pueden usarse de dos formas:
1. **En sentido estricto**: simular el rendimiento histórico como si la estrategia se hubiera ejecutado en el pasado. Es el walk-forward, tan predominante que **"backtest" se ha convertido de facto en sinónimo de "simulación histórica"**.
2. **En sentido amplio**: **simular escenarios que no ocurrieron en el pasado**. Mucho menos conocido.

### 16.2 Walk-forward: ventajas y las tres desventajas

**Ventajas.** `[LDP]`
1. **Interpretación histórica clara.** Su rendimiento puede reconciliarse con paper trading.
2. **La historia es una filtración**; usar datos previos garantiza que el test es fuera de muestra (sin fuga), **siempre que el purging se haya implementado correctamente**.
3. **El embargo no es necesario en walk-forward**, porque el entrenamiento siempre precede al test.

**Desventajas.** `[LDP]`
1. **Se testea un único escenario** —el camino histórico— **fácil de sobreajustar**.
2. **No es necesariamente representativo del rendimiento futuro**, porque los resultados pueden estar sesgados por la secuencia concreta de datos. (Ver el argumento del Escenario 11 en §15.bis.)
   - **El ejemplo concreto que da**: una estrategia de renta variable con WF sobre el S&P 500 desde enero de 2007. Hasta marzo de 2009, la mezcla de rallies y liquidaciones entrena la estrategia a ser neutral al mercado, con baja confianza en cada posición. Después, el largo rally domina el dataset, y para 2017 las previsiones de compra predominan sobre las de venta. **El rendimiento sería muy distinto si hubiéramos reproducido la información hacia atrás.** Al explotar una secuencia concreta, una estrategia seleccionada por WF puede prepararnos para un desastre.
3. **Las decisiones iniciales se toman sobre una porción menor de la muestra total.** Aunque se fije un período de calentamiento, **la mayor parte de la información es usada sólo por una porción pequeña de las decisiones**. Aumentar el calentamiento atenúa el problema pero reduce la longitud del backtest.

### 16.3 El método de cross-validation aplicado a backtesting

`[LDP]` La motivación es una pregunta que los inversores hacen a menudo: **¿cómo se comportaría esta estrategia bajo un escenario de estrés tan imprevisible como la crisis de 2008?** Una forma de responder es entrenar el clasificador sobre todo el período **excepto** 2008, y testear sobre 2008.

`[LDP]` **La aclaración metodológica esencial**: el rendimiento obtenido para 2008 **no es históricamente preciso**, puesto que el clasificador se entrenó con datos posteriores a 2008. **Pero la precisión histórica no era el objetivo del test. El objetivo era someter a una estrategia ignorante de 2008 a un escenario de estrés como el de 2008.**

> **El objetivo del backtesting mediante CV no es derivar rendimiento históricamente preciso, sino inferir rendimiento futuro a partir de un número de escenarios fuera de muestra. Para cada período, simulamos el rendimiento de un clasificador que lo sabía todo excepto ese período.**

**Ventajas.** `[LDP]`
1. **El test no es resultado de un escenario histórico particular.** La CV testea `k` escenarios alternativos, de los cuales sólo uno corresponde a la secuencia histórica.
2. **Cada decisión se toma sobre conjuntos del mismo tamaño**, lo que hace comparables los resultados entre períodos en términos de cantidad de información usada.
3. **Cada observación forma parte de uno y sólo un conjunto de test.** No hay subconjunto de calentamiento, logrando la simulación fuera de muestra más larga posible.

**Desventajas.** `[LDP]`
1. **Como el WF, simula un único camino de backtest** (aunque no el histórico). Se genera una y sólo una previsión por observación.
2. **No tiene interpretación histórica clara.** No simula cómo se habría comportado la estrategia en el pasado, sino cómo podría comportarse en el futuro bajo distintos escenarios de estrés —resultado útil por derecho propio—.
3. **Como el entrenamiento no precede al test, la fuga es posible.** Hay que tener cuidado extremo, y **aquí sí son necesarios purging y embargo**.

### 16.4 CPCV — Combinatorial Purged Cross-Validation

`[LDP]` **Qué aporta que no aportan WF ni CV**: ambos testean **un único camino**. CPCV, dado un número de caminos objetivo, **genera el número preciso de combinaciones de conjuntos entrenamiento/test necesarias para producir esos caminos**, purgando las observaciones de entrenamiento que contengan información filtrada.

**La combinatoria:**
- Se particionan `T` observaciones en `N` grupos **sin barajar**.
- Para un conjunto de test de tamaño `k` grupos, el número de particiones posibles es el número combinatorio de `N` sobre `k`.
- Como cada combinación involucra `k` grupos testeados y hemos calculado todas las combinaciones posibles, **los grupos testeados quedan uniformemente distribuidos**: cada grupo pertenece al mismo número de conjuntos de entrenamiento y de test.
- **El número de caminos de backtest resultante es `φ[N,k] = (k/N) · C(N,k)`.**

**El ejemplo del libro**: con `N = 6` y `k = 2` hay 15 particiones, y **cada grupo forma parte de 5 conjuntos de test, permitiendo calcular 5 caminos de backtest**. Los caminos se construyen combinando las previsiones de cada grupo procedentes de particiones distintas.

**El algoritmo:**
1. Particionar `T` observaciones en `N` grupos sin barajar.
2. Calcular todas las particiones entrenamiento/test posibles.
3. **Para cada par de etiquetas con una en entrenamiento y otra en test, aplicar `PurgedKFold` para purgar la de entrenamiento si abarca un período usado para determinar la de test. La clase aplicará además un embargo si algunas muestras de test preceden a algunas de entrenamiento.**
4. Ajustar los clasificadores y generar previsiones sobre los conjuntos de test correspondientes.
5. **Calcular los `φ[N,k]` caminos de backtest. Se puede obtener un Sharpe por cada camino, y de ahí derivar la distribución empírica del Sharpe de la estrategia, en lugar de un único Sharpe como en WF o CV.**

**Los casos particulares:** `[LDP]`
- Con `k = 1`, se obtiene **un** camino: **CPCV se reduce a CV**. CPCV es por tanto una generalización de CV para `k > 1`.
- Con `k = 2`, se obtienen **`N − 1` caminos**. Caso particularmente interesante, porque **entrenando sobre una porción grande de los datos podemos generar casi tantos caminos como grupos hay**.
- **La regla práctica**: particionar en `N = φ + 1` grupos, donde `φ` es el número de caminos deseado. En el límite, un grupo por observación produce `T − 1` caminos.
- Si hacen falta más caminos, se aumenta `k` hacia `N/2`, **al coste de usar una porción menor del dataset para entrenar**.

### 16.5 Cómo CPCV ataca el backtest overfitting

`[LDP]` El argumento que da, en el contexto de la revisión académica: un revisor podría pedir al investigador **que repita sus experimentos usando CPCV con un `N` y `k` dados. Como el investigador no conocía de antemano el número ni las características de los caminos que iban a backtestearse, sus esfuerzos de sobreajuste quedarían fácilmente derrotados.**

`[INTERPRETACIÓN]` Ese es el mecanismo: el sobreajuste es siempre **sobreajuste a un objetivo concreto**. Cuando el objetivo es un único camino conocido, se puede apuntar a él iterando. Cuando el objetivo es una distribución sobre múltiples caminos generados combinatoriamente, apuntar es mucho más difícil. **La aleatorización estructural que el WF no tiene, y que la CV estándar consigue de forma inaceptable (barajando), CPCV la obtiene combinando bloques temporales intactos.**

### 16.6 Qué significa obtener múltiples trayectorias

`[IMPLICACIÓN PARA IRIS]` La diferencia cualitativa es la siguiente:

| | WF / CV | CPCV |
|---|---|---|
| **Salida** | Un número (un Sharpe). | **Una distribución empírica de Sharpes.** |
| **Pregunta que responde** | "¿Cuánto habría ganado?" | "**¿Cuánto podría ganar, y con qué dispersión?**" |
| **Qué se puede afirmar** | "El Sharpe fue 1.5." | "El Sharpe medio es X con desviación Y; la fracción de caminos con Sharpe negativo es Z." |
| **Robustez del resultado** | Depende de una secuencia. | Depende de la estructura, no del orden. |

**Por qué da mejor imagen del rendimiento**: porque **la varianza entre caminos es en sí misma información**. Una estrategia con Sharpe medio 1.0 y desviación 0.2 entre caminos es cualitativamente distinta de una con Sharpe medio 1.0 y desviación 1.5, aunque el WF de ambas hubiera podido dar 1.5. Y conecta directamente con el DSR (§18.5), que necesita precisamente **la varianza entre intentos** para deflactar.

### 16.7 Compatibilidad y coste

**Clasificación: `OHLCV-OK`.**

`[INTERPRETACIÓN]` Pero el coste computacional es real y debe dimensionarse: CPCV requiere entrenar `C(N,k)` modelos. Con `N = 10` y `k = 2` son 45 entrenamientos; con `N = 20`, 190. Sobre datos intradiarios con cientos de miles de eventos y modelos no triviales, esto se convierte en el cuello de botella dominante. Es un factor a considerar en la matriz de mínima complejidad (§26).

`[LDP]` **No debemos asumir que CPCV será nuestra validación final**, como indica el encargo. Pero sí es la única propuesta del libro que **cambia cualitativamente la naturaleza de la evidencia** que un backtest puede aportar.

---

## 17. BACKTESTING SOBRE DATOS SINTÉTICOS (Tarea 15)

### 17.1 Motivación y alcance

`[LDP]` **El propósito**: usar la historia para generar un dataset sintético con características estadísticas estimadas de los datos observados. Esto permite **hacer backtest sobre un número grande de conjuntos de test sintéticos no vistos, reduciendo la probabilidad de que la estrategia haya sido ajustada a un conjunto concreto de puntos**.

**El alcance del capítulo**: es un tema muy extenso, y para alcanzar profundidad **se centra en el backtesting de las reglas de trading**.

### 17.2 El problema concreto que ataca

`[LDP]` **Definición de regla de trading**: las estrategias de inversión postulan la existencia de una ineficiencia de mercado; **las tácticas —las reglas de trading— proporcionan el algoritmo que debe seguirse para entrar y salir de una posición**. Aunque las estrategias son muy heterogéneas, **las tácticas son relativamente homogéneas**.

`[LDP]` **Y aquí está el problema**: las condiciones de salida se definen a menudo mediante **umbrales de profit-taking y stop-loss**, y esos parámetros **se calibran habitualmente mediante simulaciones históricas**. Esa práctica **conduce al problema del backtest overfitting**, porque los parámetros apuntan a observaciones específicas dentro de muestra, **hasta el punto de que la estrategia queda tan atada al pasado que se vuelve inservible para el futuro**.

`[LDP]` **La clarificación de alcance, importante**: nos interesan las condiciones del corredor de salida que maximizan el rendimiento. **En otras palabras, la posición ya existe, y la pregunta es cómo salir de ella óptimamente.** Es el dilema que enfrentan a menudo los traders de ejecución, **y no debe confundirse con la determinación de umbrales de entrada y salida para invertir en un valor**.

`[LDP]` **La propuesta**: aunque evaluar la probabilidad de backtest overfitting es útil para descartar estrategias superfluas, **sería mejor evitar el riesgo de sobreajuste, al menos en el contexto de calibrar una regla de trading**. En teoría esto puede lograrse **derivando los parámetros óptimos directamente del proceso estocástico que genera los datos, en lugar de mediante simulaciones históricas**. Usando la muestra histórica completa se caracteriza el proceso estocástico que genera el flujo de retornos observado, y se derivan los valores óptimos **sin requerir simulación histórica**.

`[LDP]` **Definición de regla de trading sobreajustada**: aquella cuyos parámetros óptimos se ajustan a unos pocos outliers. El trivial: un par de umbrales que apunta a unos pocos valores extremos.

### 17.3 Relevancia para una primera versión de IRIS

`[IMPLICACIÓN PARA IRIS]` La conexión es directa y merece registrarse aunque el capítulo se clasifique como complementario:

**Si IRIS adopta un esquema de barreras, la calibración de `[PT, SL]` es exactamente el problema que este capítulo describe.** Y López de Prado señala que optimizar dos parámetros sobre una muestra finita es un caso de sobreajuste **fácil y trivial**.

Ahora bien, el libro ya ofrece **una alternativa más simple dentro del capítulo 3**: derivar las barreras de la **volatilidad estimada** en lugar de optimizarlas. Eso convierte `[PT, SL]` de parámetros libres en funciones de una variable de estado, reduciendo drásticamente los grados de libertad.

**Clasificación de relevancia para la primera versión: C.** Razones:
1. Añade una capa completa de supuestos (caracterizar el proceso generador de MNQ intradiario) cuya validez es a su vez discutible.
2. El problema que resuelve puede mitigarse a coste mucho menor mediante barreras escaladas por volatilidad.
3. Su alcance declarado —cómo salir óptimamente de una posición que ya existe— es una capa posterior a lo que IRIS todavía no ha resuelto (si hay señal).

**Pero conservamos dos ideas:**
- **La distinción entre "cuándo entrar" y "cómo salir"** como problemas separados, con literatura y métodos distintos. Es una separación que no habíamos formulado.
- **La idea general de simular escenarios en lugar de historia** (recomendación 5 del capítulo 11), que es más amplia que este capítulo concreto y que CPCV implementa parcialmente por otra vía.

**Clasificación de datos: `OHLCV-OK`** en principio; requiere ajustar un modelo estocástico a nuestra serie.

`[VACÍO]` El libro no discute si su marco (un proceso con reversión a la media y equilibrio a largo plazo) es apropiado para un futuro sobre índice de renta variable en frecuencia intradiaria. La aplicabilidad a nuestro caso es una pregunta abierta.


---

## 18. BACKTEST STATISTICS (Tarea 16)

### 18.1 La separación que pide el encargo

`[LDP]` El libro organiza las métricas en siete categorías: características generales, rendimiento, runs/drawdowns, implementation shortfall, eficiencia riesgo-retorno, **classification scores** y atribución.

De ellas, **sólo una categoría mide el modelo**; el resto miden la estrategia. Esta es la separación:

| **MÉTRICAS DEL MODELO** | **MÉTRICAS DE LA ESTRATEGIA** |
|---|---|
| Accuracy | Retorno anualizado, PnL |
| Precision | Hit ratio, retorno medio de aciertos y de fallos |
| Recall | Sharpe ratio |
| F1 | Probabilistic Sharpe Ratio |
| Negative log-loss | Deflated Sharpe Ratio |
| | Information ratio |
| | Drawdown, Time under Water |
| | Concentración HHI (positivos, negativos, temporal) |
| | Frecuencia de apuestas, holding period, turnover |
| | Apalancamiento, capacidad, posición máxima |
| | Costes de broker, slippage, rendimiento por turnover |
| | Atribución por clase de riesgo |

`[LDP]` Y el contexto en que las métricas de clasificación son relevantes: **en estrategias de meta-labeling, es útil entender el rendimiento del algoritmo de superposición en aislamiento**. El primario identifica oportunidades; el secundario decide si perseguirlas o pasar.

### 18.2 Características generales — y la distinción bet vs trade

`[LDP]` Las más relevantes para nosotros:

- **Rango temporal**: el período usado debe ser **suficientemente largo como para incluir un número comprensivo de regímenes**.
- **Capacidad**: el AUM más alto que entrega un rendimiento ajustado por riesgo objetivo. Hace falta un AUM mínimo para asegurar bet sizing y diversificación adecuados; **más allá de ese mínimo, el rendimiento decae al aumentar el AUM, por mayores costes de transacción y menor turnover**.
- **Apalancamiento**: mide cuánto endeudamiento hace falta. **Si hay apalancamiento, deben asignarse costes.** Una forma de medirlo: ratio entre tamaño medio de posición en dólares y AUM medio.
- **Tamaño máximo de posición**: `[LDP]` **preferimos estrategias que tomen posiciones máximas cercanas al AUM medio, lo que indica que no dependen de la ocurrencia de eventos extremos (posiblemente outliers)**.
- **Ratio de largos**: en estrategias neutrales al mercado, idealmente cercano a 0.5. Si no, la estrategia puede tener sesgo de posición, **o el período backtesteado puede ser demasiado corto y no representativo**.
- **Frecuencia de apuestas**: número de apuestas por año. **Una secuencia de posiciones del mismo lado se considera parte de la misma apuesta. Una apuesta termina cuando la posición se aplana o se voltea al lado opuesto.** `[LDP]` **El número de apuestas es siempre menor que el número de operaciones. Contar operaciones sobreestimaría el número de oportunidades independientes descubiertas por la estrategia.**
- **Holding period medio**: número medio de días que se mantiene una apuesta. **Períodos cortos pueden limitar la capacidad.** Está relacionado pero es distinto de la frecuencia de apuestas.
- **Turnover anualizado**: ratio entre el importe medio negociado por año y el AUM medio anual. **Puede haber turnover alto incluso con pocas apuestas**, si la estrategia requiere ajuste constante de la posición.

`[IMPLICACIÓN PARA IRIS]` La distinción **apuesta ≠ operación** es especialmente importante para nosotros y conecta con toda la discusión de unicidad (§8): el número de **oportunidades independientes** es una cantidad mucho menor que el número de filas, de eventos muestreados o de operaciones ejecutadas. Es la magnitud correcta para juzgar significación estadística y capacidad.

### 18.3 Runs, concentración y drawdown

`[LDP]` **Por qué importan**: las estrategias de inversión rara vez generan retornos de un proceso IID. En ausencia de esa propiedad, **las series de retornos exhiben corridas (runs) frecuentes: secuencias ininterrumpidas de retornos del mismo signo. Las corridas aumentan el riesgo a la baja, que debe evaluarse con métricas apropiadas.**

**Concentración de retornos.** `[LDP]` Inspirada en el índice Herfindahl-Hirschman, se define una concentración para retornos positivos y otra para negativos, acotadas entre 0 y 1. Vale 0 cuando los retornos son uniformes, y 1 cuando toda la contribución viene de una sola observación. Es fácil derivar la expresión equivalente para la **concentración de apuestas a lo largo de los meses**.

`[LDP]` **El perfil de estrategia deseable**, tal como lo enuncia:
- Sharpe alto.
- **Número alto de apuestas por año.**
- **Hit ratio alto** (relativamente pocos retornos negativos).
- **Concentración baja de retornos positivos** (sin cola derecha gruesa).
- **Concentración baja de retornos negativos** (sin cola izquierda gruesa).
- **Concentración baja en el tiempo** (las apuestas no están concentradas en pocos períodos).

`[IMPLICACIÓN PARA IRIS]` Este conjunto de seis criterios es una **especificación de calidad completa y directamente aplicable**, mucho más informativa que un Sharpe aislado. La concentración temporal es especialmente diagnóstica para nosotros: detectaría, por ejemplo, un IRIS cuyos beneficios se acumulan en torno a los rollovers (Escenario 7 de §15.bis) o en una única franja horaria.

**Drawdown y Time under Water.** `[LDP]`
- **Drawdown**: la pérdida máxima sufrida entre dos máximos consecutivos de la curva de resultados.
- **Time under Water**: el tiempo transcurrido entre un máximo y el momento en que el resultado supera ese máximo previo.
- Se reportan el **percentil 95 de la serie de drawdowns** y el **percentil 95 de la serie de TuW**.

### 18.4 Implementation shortfall

`[LDP]` Las estrategias fracasan a menudo por supuestos erróneos sobre costes de ejecución. Las métricas:
- **Comisiones de broker por turnover.**
- **Slippage medio por turnover**: costes de ejecución excluyendo comisiones. Por ejemplo, la pérdida causada por comprar a un precio de ejecución superior al punto medio en el momento en que se envió la orden.
- **Rendimiento en dólares por turnover**: ratio entre el rendimiento (incluyendo comisiones y slippage) y el turnover total. **Significa cuánto más caro podría volverse la ejecución antes de que la estrategia deje de ser rentable.**
- **Retorno sobre costes de ejecución**: ratio entre rendimiento y costes totales de ejecución. **Debería ser un múltiplo grande, para asegurar que la estrategia sobreviva a una ejecución peor de lo esperado.**

`[IMPLICACIÓN PARA IRIS]` Estas dos últimas son exactamente las métricas que necesita un sistema intradiario de alto turnover, y son las que faltaban en nuestra base anterior. **"Cuánto margen tenemos antes de que los costes nos coman"** es una pregunta más útil que "cuánto ganamos con estos costes concretos".

### 18.5 Sharpe, PSR y DSR

**Sharpe ratio.** `[LDP]` Se define asumiendo que los retornos en exceso son **IID gaussianos**. Su propósito es evaluar la habilidad de una estrategia o un inversor. Como la media y la varianza verdaderas son desconocidas, **el valor verdadero del Sharpe no puede conocerse con certeza, y la consecuencia inevitable es que los cálculos de Sharpe pueden estar sujetos a errores de estimación sustanciales**.

`[LDP]` El **Sharpe anualizado** escala por la raíz del número medio de retornos observados por año, **método de anualización que se apoya en el supuesto de que los retornos son IID**.

**Probabilistic Sharpe Ratio (PSR).** `[LDP]` Proporciona una estimación ajustada del Sharpe **eliminando el efecto inflacionario causado por series cortas con retornos asimétricos y/o de colas gruesas**. Dado un Sharpe de referencia definido por el usuario y un Sharpe observado, **el PSR estima la probabilidad de que el Sharpe verdadero sea mayor que el de referencia**.

**Cómo se comporta:** para un umbral dado, el PSR **aumenta** con: un Sharpe observado mayor (en la frecuencia original, no anualizado), un track record más largo, o **retornos con asimetría positiva**. Y **disminuye** con **colas más gruesas**.

**Umbral de aceptación:** `[LDP]` **debería superar 0.95**, para el nivel de significación estándar del 5%.

**Deflated Sharpe Ratio (DSR).** `[LDP]` Es un PSR **donde el umbral de rechazo se ajusta para reflejar la multiplicidad de intentos**.

**El razonamiento, que es el núcleo:**
> **Dado un conjunto de estimaciones de Sharpe, su máximo esperado es mayor que cero incluso si el Sharpe verdadero es cero.** Bajo la hipótesis nula de que el Sharpe real es cero, el máximo esperado puede estimarse, y ese valor se convierte en el umbral de referencia. **Ese umbral crece rápidamente conforme se intentan más pruebas independientes, o conforme los intentos involucran mayor varianza.**

**Los ingredientes del umbral:** la **varianza entre los Sharpes estimados de los distintos intentos**, el **número de intentos independientes**, y la constante de Euler-Mascheroni.

`[LDP]` De aquí deriva su **tercera ley del backtesting** (parafraseada): **todo resultado de backtest debe reportarse junto con todos los intentos involucrados en su producción; en ausencia de esa información, es imposible evaluar la probabilidad de falso descubrimiento del backtest.** Y añade que **la mayoría de descubrimientos en finanzas son falsos por violación de esta ley**.

`[IMPLICACIÓN PARA IRIS]` Dos consecuencias operativas inmediatas:
1. **El DSR necesita dos insumos que sólo existen si los registramos desde el principio**: el número de intentos y la varianza entre sus Sharpes. Si no llevamos ese registro, **el DSR es incalculable y nuestro resultado final es literalmente ininterpretable**. Esto convierte el registro de experimentos de "buena práctica" en **requisito técnico**.
2. **CPCV y DSR encajan**: CPCV produce una distribución de Sharpes de la que sale naturalmente la varianza requerida.

### 18.6 Classification scores

`[LDP]` En contexto de meta-labeling:
- **Accuracy**: fracción de oportunidades correctamente etiquetadas.
- **Precision**: fracción de verdaderos positivos entre los positivos predichos.
- **Recall**: fracción de verdaderos positivos entre los positivos reales.
- **F1**: `[LDP]` **la accuracy puede no ser un score adecuado para meta-labeling**. Si tras aplicar meta-labeling hay muchos más casos negativos que positivos, un clasificador que prediga todo negativo alcanzará accuracy alta aunque el recall sea cero y la precisión indefinida. **El F1 corrige ese defecto** mediante la media armónica de precisión y recall.
- **La degeneración inversa**: si hay muchos más positivos que negativos, un clasificador que prediga todo positivo obtendrá F1 alto sin discriminar. `[LDP]` **La solución es intercambiar las definiciones de caso positivo y negativo, para que los negativos predominen, y entonces puntuar con F1.**
- **Negative log-loss**: `[LDP]` **la diferencia conceptual clave con la accuracy es que tiene en cuenta no sólo si las predicciones fueron correctas, sino también la probabilidad de esas predicciones.**

`[LDP]` Documenta además **los cuatro casos degenerados** de la clasificación binaria (todo observado 1, todo observado 0, todo predicho 1, todo predicho 0), en dos de los cuales **el F1 ni siquiera está definido**, y donde la accuracy colapsa a precisión o a recall.

### 18.7 Atribución

`[LDP]` Descomponer el PnL en clases de riesgo. **Estos riesgos no son ortogonales, así que siempre hay solapamiento: la suma de los PnL atribuidos no coincidirá con el PnL total, pero al menos podremos calcular el Sharpe (o el information ratio) por clase de riesgo.** El procedimiento requiere que cada miembro del universo pertenezca a una y sólo una categoría de cada clase en cada momento.

**Clasificación: `OTRAS FUENTES`** en su forma multiactivo.

`[INTERPRETACIÓN]` El principio sí es trasladable en una forma distinta: **atribuir el PnL de IRIS por condición de mercado** —franja horaria, régimen de volatilidad, dirección de la señal, cercanía al roll— particionando el histórico en categorías disjuntas y calculando el Sharpe de cada una. Esto no es lo que el libro propone, pero es el mismo principio aplicado a nuestro caso, y respondería a la pregunta "¿bajo qué condiciones funciona IRIS?".

### 18.8 Qué métricas responden a cada pregunta de IRIS

`[IMPLICACIÓN PARA IRIS]` Respondiendo directamente a la pregunta del encargo:

| Pregunta sobre IRIS | Métricas que la responden |
|---|---|
| **1. ¿Tiene capacidad predictiva?** | Accuracy, precision, recall, F1, negative log-loss — **evaluadas bajo purged CV**. Y crucialmente: **MDA y SFI**, que pueden concluir que ninguna feature es informativa. |
| **2. ¿Es operativamente viable?** | Frecuencia de apuestas, holding period medio, turnover anualizado, capacidad, apalancamiento, posición máxima, **rendimiento en dólares por turnover** y **retorno sobre costes de ejecución**. |
| **3. ¿Es estadísticamente robusto?** | **PSR** (corrige por longitud, asimetría y curtosis), **DSR** (corrige además por multiple testing), **PBO vía CSCV**, y la **distribución de Sharpes vía CPCV**. |
| **4. ¿Es rentable ajustado por riesgo?** | Sharpe, information ratio, percentil 95 del drawdown, percentil 95 del TuW, y las **tres concentraciones HHI**. |

**Clasificación general del capítulo: `OHLCV-OK`.**

---

## 19. RIESGO DE ESTRATEGIA (Tarea 17)

Este capítulo es, en mi lectura, uno de los más infravalorados del libro y de los más directamente útiles para IRIS.

### 19.1 La distinción central

`[LDP]` **El riesgo de estrategia no es el riesgo de la cartera subyacente, tal como lo calcula el director de riesgos. El riesgo de estrategia es el riesgo de que la estrategia de inversión fracase con el tiempo** — una cuestión de relevancia mucho mayor para el director de inversiones.

`[LDP]` Y la observación de campo: **la mayoría de firmas e inversores calculan, monitorizan y reportan el riesgo de cartera sin darse cuenta de que eso no nos dice nada sobre el riesgo de la estrategia en sí.**

### 19.2 El marco binomial

`[LDP]` **Por qué el modelo binomial es apropiado**: las estrategias se implementan a menudo con posiciones mantenidas hasta que se cumple una de dos condiciones: salir con beneficio (profit-taking) o salir con pérdida (stop-loss). **Incluso cuando una estrategia no declara explícitamente un stop-loss, existe siempre un límite implícito, en el que el inversor ya no puede financiar su posición (margin call) o soportar el dolor de una pérdida latente creciente.** Como la mayoría de estrategias tienen esas dos condiciones de salida, **tiene sentido modelar la distribución de resultados mediante un proceso binomial**.

`[LDP]` **La interpretación de `p`**: puede pensarse como la **precisión de un clasificador binario**, donde un positivo significa apostar por una oportunidad y un negativo significa pasar. **Los verdaderos positivos son recompensados, los falsos positivos castigados, y los negativos (verdaderos o falsos) no tienen pago directo.**

### 19.3 Pagos simétricos

`[LDP]` Con `n` apuestas IID al año, beneficio `π` con probabilidad `p` y pérdida `−π` con probabilidad `1−p`:

- El beneficio esperado por apuesta es `π(2p − 1)`.
- La varianza es `4π²p(1−p)`.
- **El Sharpe anualizado resulta ser función únicamente de `p` y `n`. El pago `π` se cancela, porque los pagos son simétricos.**
- Igual que en el caso gaussiano, el Sharpe puede entenderse como **un t-valor reescalado**.

`[LDP]` **La implicación económica del HFT, formulada explícitamente:**
> **Incluso para un `p` ligeramente superior a 1/2, el Sharpe puede hacerse alto con un `n` suficientemente grande. Esta es la base económica del trading de alta frecuencia, donde `p` puede estar apenas por encima de 0.5, y la clave de un negocio exitoso es aumentar `n`.**

`[LDP]` **Y el punto sutil**: el Sharpe es función de la **precisión**, no de la accuracy, **porque pasar de largo sobre una oportunidad (un negativo) no se recompensa ni se castiga directamente** — aunque demasiados negativos conducen a un `n` pequeño, lo que deprime el Sharpe hacia cero.

**Los números concretos que da:**
- Con `p = 0.55`, alcanzar un Sharpe anualizado de 2 requiere **396 apuestas al año**.
- Una estrategia que sólo produce apuestas semanales (`n = 52`) necesitaría una precisión bastante alta, **`p = 0.6336`**, para entregar un Sharpe anualizado de 2.

### 19.4 Pagos asimétricos — el caso relevante para IRIS

`[LDP]` Con beneficio `π₊` con probabilidad `p` y resultado `π₋` (menor que `π₊`) con probabilidad `1−p`, el Sharpe anualizado pasa a depender de **cuatro** cantidades: `p`, `n`, `π₋` y `π₊`. Se verifica que cuando `π₋ = −π₊` la expresión se reduce al caso simétrico.

**Y aquí están las cifras que conviene retener y que responden directamente a la pregunta del encargo:**

Con `n = 260` apuestas al año, `π₋ = −1%` (stop-loss) y `π₊ = +0.5%` (profit-taking):

| Precisión `p` | Sharpe anualizado |
|---|---|
| **0.67** | **≈ 0** (todos los beneficios borrados) |
| **0.70** | **1.173** |
| **0.72** | **2.000** |

`[LDP]` Su lectura, en dos direcciones:
- **Gracias al número grande de apuestas, un cambio muy pequeño en `p` —de 0.70 a 0.72— ha impulsado el Sharpe de 1.173 a 2.**
- **Pero, por lo mismo, esto nos dice que la estrategia es vulnerable a cambios pequeños en `p`.** Una caída relativamente pequeña, de 0.70 a 0.67, **borraría todos los beneficios**.
- **La estrategia es intrínsecamente arriesgada, aunque las posiciones no lo sean.**

`[LDP]` Los patrones generales que reporta: conforme `π₋` se vuelve más negativo para un `n` dado, **hace falta una `p` mayor** para lograr el Sharpe objetivo. Conforme `n` se hace más pequeño para un `π₋` dado, **hace falta una `p` mayor**. Y simétricamente, conforme `π₋` se vuelve más negativo para una `p` dada, **hace falta un `n` mayor**.

### 19.5 Cómo acertar mucho y perder dinero (y viceversa)

`[IMPLICACIÓN PARA IRIS]` Respondiendo directamente a la pregunta del encargo, con el marco del libro:

**Acertar mucho y perder dinero.** Con `π₊ = +0.5%` y `π₋ = −1%`, cada acierto gana la mitad de lo que pierde cada fallo. **El punto de equilibrio está en `p = 2/3`**. Una estrategia con precisión del 65% —que suena excelente y que la mayoría de los reportes de ML celebrarían— **pierde dinero**. Este es exactamente el perfil de un sistema con stop-loss amplio y take-profit estrecho: gana a menudo, poco, y pierde raramente, mucho.

**Acertar poco y ganar dinero.** El caso inverso: con `π₊ = +2%` y `π₋ = −0.5%`, el punto de equilibrio está en `p = 0.2`. Una precisión del 30% —que sonaría a fracaso— es rentable. Es el perfil de seguimiento de tendencia clásico.

**La conclusión metodológica:** `[INTERPRETACIÓN]` **La accuracy o la precisión, aisladas de la estructura de pagos y de la frecuencia, no contienen información sobre si la estrategia gana dinero.** Reportar un 70% de acierto sin especificar `π₊`, `π₋` y `n` es literalmente incomunicativo. Esto conecta directamente con la advertencia del capítulo 15 sobre el bet sizing: acertar mucho en apuestas pequeñas y poco en grandes lleva a la ruina.

### 19.6 La probabilidad de fracaso de la estrategia

`[LDP]` **El planteamiento**: en el ejemplo, `π₋`, `π₊` y `n` los fija el gestor (los dos primeros se pasan a los operadores con las órdenes; `n` resulta de decidir qué constituye una oportunidad digna de apuesta). **Los dos parámetros que no están bajo control del gestor son `p` —determinado por el mercado— y el Sharpe objetivo —fijado por el inversor—.**

**Como `p` es desconocido, se modela como variable aleatoria.** Se define `p_θ*` como el valor de `p` por debajo del cual la estrategia no alcanzará el Sharpe objetivo. **El riesgo de estrategia es la probabilidad de que `p` sea menor que `p_θ*`.**

**El algoritmo:**
1. De una serie temporal de resultados de apuestas, estimar `π₋` como la media de los resultados no positivos y `π₊` como la media de los positivos. (Alternativamente, derivarlos ajustando una mezcla de dos gaussianas.)
2. La frecuencia anual `n` sale del número de apuestas dividido por los años transcurridos.
3. **Bootstrapear la distribución de `p`**: en cada iteración, extraer con reemplazo un número de muestras igual a `n·k`, donde `k` es el número de años que los inversores usan para evaluar una estrategia (por ejemplo, 2 años); calcular la precisión observada en esa iteración. Ajustar la densidad de `p` con un estimador de núcleo. Para un `k` suficientemente grande, la distribución puede aproximarse por una normal.
4. Dado el Sharpe umbral que separa éxito de fracaso, derivar `p_θ*`.
5. **El riesgo de estrategia es la masa de probabilidad por debajo de `p_θ*`.**

`[LDP]` **El criterio de aceptación explícito:**
> **Típicamente descartaríamos estrategias donde la probabilidad de que `p` sea menor que `p_θ*` supere 0.05, por arriesgadas, incluso si invierten en instrumentos de baja volatilidad. La razón es que, aunque no pierdan mucho dinero, la probabilidad de que no alcancen su objetivo es demasiado alta. Para desplegarse, el desarrollador debe encontrar una forma de reducir `p_θ*`.**

`[IMPLICACIÓN PARA IRIS]` **Este capítulo aporta algo que ninguna otra parte del libro aporta: una herramienta de viabilidad *ex-ante*.** Antes de entrenar ningún modelo, podemos preguntarnos:

> *Dado un esquema de barreras candidato `[PT, SL]` y una frecuencia de eventos candidata `n` derivada de nuestro filtro CUSUM, ¿qué precisión necesitaría IRIS para alcanzar un Sharpe objetivo? ¿Es esa precisión plausible dado lo que sabemos del ratio señal/ruido en mercados líquidos?*

Si la respuesta es que necesitaríamos una precisión del 75% prediciendo el MNQ a 30 minutos, **eso es información decisiva obtenida sin escribir un modelo**. Y si la respuesta es que basta un 53% con suficientes apuestas, **entonces la pregunta se desplaza a si el edge sobrevive a los costes** — que es la pregunta correcta.

**Clasificación: `OHLCV-OK`.** Sólo requiere resultados de apuestas simulados o supuestos.

`[VACÍO]` El supuesto de apuestas IID es fuerte y el libro no lo relaja, pese a que todo el capítulo 4 argumenta que las observaciones financieras no son IID. Las apuestas consecutivas sobre un mismo instrumento están correlacionadas, lo que probablemente **infla** el Sharpe calculado por estas fórmulas. Es una inconsistencia interna que conviene registrar.

---

## 20. ASSET ALLOCATION (Tarea 18)

### 20.1 Qué problema aborda

`[LDP]` Los optimizadores convexos de cartera sufren tres problemas mayores: **inestabilidad, concentración e infrarrendimiento**.

**La maldición de Markowitz**, formulada con precisión:
- El número de condición de una matriz de correlación es el cociente entre su mayor y su menor autovalor en módulo.
- Es mínimo para una matriz diagonal, que es su propia inversa.
- **Conforme añadimos inversiones correlacionadas (multicolineales), el número de condición crece.** En algún punto es tan alto que los errores numéricos hacen la matriz inversa demasiado inestable: **un cambio pequeño en cualquier entrada conduce a una inversa muy distinta**.
- **Esa es la maldición: cuanto más correlacionadas están las inversiones, mayor la necesidad de diversificación, y sin embargo más probable es que recibamos soluciones inestables. Los beneficios de la diversificación quedan a menudo más que compensados por los errores de estimación.**

`[LDP]` Y añade que aumentar el tamaño de la matriz sólo empeora las cosas, porque cada coeficiente se estima con menos grados de libertad.

**La solución (HRP)**: usar teoría de grafos y ML para construir una cartera diversificada a partir de la información contenida en la matriz de covarianzas, **sin requerir su invertibilidad**. HRP puede calcular una cartera sobre una matriz mal condicionada o incluso singular, algo imposible para los optimizadores cuadráticos. Los experimentos Monte Carlo muestran que entrega **menor varianza fuera de muestra** que el algoritmo de línea crítica, **aunque la minimización de varianza sea el objetivo de optimización de este último**.

### 20.2 Qué es generalizable y qué no

**Qué requiere portfolios multiactivo (no aplicable a IRIS):**
- Tree clustering, cuasi-diagonalización y bisección recursiva sobre una matriz de correlaciones entre activos.
- La construcción de pesos de cartera propiamente dicha.
- Los eigenportfolios y toda la comparación con el algoritmo de línea crítica.

**Qué principios son generalizables:** `[INTERPRETACIÓN]`
1. **El principio general de que una solución óptima in-sample puede rendir pobremente out-of-sample**, y de que **la robustez es preferible a la optimalidad teórica**. Es transversal a todo el libro y aplica a cualquier decisión de IRIS, no sólo a la asignación.
2. **El diagnóstico del número de condición** como medida de multicolinealidad. Aplicable a nuestra **matriz de correlación entre features**: un número de condición alto nos avisaría de que nuestro espacio de indicadores técnicos es efectivamente de dimensión mucho menor de lo que parece, y de que cualquier método que requiera invertirla (regresión lineal, Mahalanobis) será inestable.
3. **La idea de sustituir relaciones geométricas por relaciones jerárquicas** cuando hay multicolinealidad severa. Conceptualmente, esto es lo mismo que hacer el clustering jerárquico de features antes de interpretar importancias, que ya apuntamos en §12.

**Dónde sí podría aplicarse HRP en el futuro:** `[LDP]` menciona explícitamente que **una aplicación práctica de HRP es determinar asignaciones entre múltiples estrategias de ML**. Si IRIS acabara produciendo varios modelos o varias variantes de señal, HRP sería la forma de combinarlos. **Eso es una extensión muy posterior, no un componente de IRIS.**

**Clasificación general: `OTRAS FUENTES` / `NO RELEVANTE`.**

`[IMPLICACIÓN PARA IRIS]` Siguiendo la instrucción del encargo: **no se fuerza HRP ni la optimización de cartera dentro de IRIS.** Se conserva únicamente el diagnóstico del número de condición sobre la matriz de features y el principio de preferencia por la robustez.

---

## 21. RUPTURAS ESTRUCTURALES (Tarea 19)

### 21.1 Por qué importan — el racional económico

`[LDP]` El argumento no es estadístico sino conductual, y merece registrarse:

> **Al desarrollar una estrategia basada en ML, típicamente queremos apostar cuando hay una confluencia de factores cuyo resultado previsto ofrece un retorno favorable ajustado por riesgo. Las rupturas estructurales, como la transición de un régimen de mercado a otro, son un ejemplo de esa confluencia. Por ejemplo, un patrón de reversión a la media puede dar paso a un patrón de momentum. Conforme ocurre esa transición, la mayoría de participantes son sorprendidos y cometerán errores costosos. Ese tipo de errores es la base de muchas estrategias rentables, porque los actores del lado perdedor típicamente se dan cuenta de su error cuando ya es demasiado tarde. Antes de aceptar sus pérdidas, actuarán irracionalmente, intentarán mantener la posición y esperarán una recuperación. A veces incluso aumentarán una posición perdedora, en desesperación. Eventualmente se verán forzados a cortar pérdidas o a ser expulsados. Las rupturas estructurales ofrecen algunas de las mejores relaciones riesgo/recompensa.**

`[IMPLICACIÓN PARA IRIS]` Esto es exactamente lo que el capítulo 1 pedía a un estratega: **identificar el mecanismo económico por el que un agente nos pierde dinero.** Aquí ese mecanismo está nombrado explícitamente —participantes atrapados en el lado equivocado de una transición de régimen, que actúan irracionalmente antes de ser forzados a salir—. **Es una de las pocas hipótesis económicas concretas y comprobables que el libro ofrece**, y es una hipótesis que **no requiere universo multiactivo**.

### 21.2 Las dos familias de tests

`[LDP]`
- **Tests CUSUM**: comprueban si los errores acumulados de previsión **se desvían significativamente del ruido blanco**.
- **Tests de explosividad**: más allá de la desviación respecto del ruido blanco, comprueban si el proceso **exhibe crecimiento o colapso exponencial**, lo cual es inconsistente con un random walk o con un proceso estacionario, e insostenible a largo plazo. Se subdividen en **tests de raíz unitaria de cola derecha** y **tests sub/super-martingala**.

`[LDP]` Y una distinción importante dentro de la explosividad: los tests **que permiten múltiples burbujas son más robustos**, en el sentido de que **un ciclo burbuja-estallido-burbuja hará que la serie parezca estacionaria a los tests de burbuja única**. En este contexto, **las burbujas no se limitan a subidas de precio: incluyen también liquidaciones**.

### 21.3 Los tests, uno a uno, con su compatibilidad

#### Brown-Durbin-Evans: CUSUM sobre residuos recursivos

`[LDP]` Asume que en cada observación contamos con un vector de features predictivo de un valor objetivo. Se calculan estimaciones de mínimos cuadrados recursivos sobre submuestras crecientes, se obtienen los **residuos recursivos estandarizados a un paso**, y el estadístico CUSUM es su suma acumulada estandarizada. **Bajo la hipótesis nula de que los coeficientes son constantes**, el estadístico sigue una normal con varianza creciente.

`[LDP]` **Advertencia**: el punto de inicio se elige arbitrariamente, y **los resultados pueden ser inconsistentes por ello**.

**Clasificación: `OHLCV-COND`.** Requiere una matriz de features y un target, que sí tendríamos, pero el resultado depende de qué features usemos: **no es una propiedad de la serie de precios sino de la relación features→target que hayamos definido**. Eso lo hace conceptualmente distinto del resto.

`[INTERPRETACIÓN]` Ese matiz lo hace potencialmente **el más interesante para la segunda pregunta del encargo** —"¿la relación aprendida por IRIS puede haber dejado de ser válida?"— porque es el único test que mide la estabilidad de una **relación**, no de una serie.

#### Chu-Stinchcombe-White: CUSUM sobre niveles

`[LDP]` **Simplifica el anterior descartando las features** y asumiendo que no se prevé ningún cambio. Esto **permite trabajar directamente con los niveles**, reduciendo la carga computacional. Se calcula la desviación estandarizada del log-precio actual respecto del log-precio en un instante de referencia anterior. Bajo la nula, sigue una normal estándar, y el valor crítico dependiente del tiempo se obtiene con una constante derivada por Monte Carlo.

`[LDP]` **Desventaja**: el nivel de referencia se fija de forma algo arbitraria. **La solución que propone**: estimar el estadístico sobre una serie de ventanas retrocedientes y **tomar el supremo**.

**Clasificación: `OHLCV-OK`.** Sólo requiere log-precios. Es el más barato computacionalmente de los tests de este capítulo.

#### Chow-type Dickey-Fuller

`[LDP]` La nula es que la serie sigue un random walk; la alternativa es que empieza como random walk y **cambia en un instante concreto a un proceso explosivo**. Se ajusta una especificación con una variable dummy que separa ambos regímenes.

`[LDP]` **Dos inconvenientes**: (1) **el instante de cambio es desconocido** — se resuelve probando todos los instantes posibles dentro de un intervalo, dejando fuera los extremos de la muestra para que ambos regímenes tengan observaciones suficientes; (2) **asume que hay una sola fecha de ruptura y que la burbuja se extiende hasta el final de la muestra**, sin vuelta al random walk.

**Clasificación: `OHLCV-OK`.**

#### SADF — Supremum Augmented Dickey-Fuller

`[LDP]` La motivación, citando a los autores originales: **los tests estándar de raíz unitaria y cointegración son herramientas inapropiadas para detectar comportamiento de burbuja, porque no pueden distinguir efectivamente entre un proceso estacionario y un modelo de burbuja que colapsa periódicamente.** Los patrones de burbujas que colapsan se parecen más a datos generados por una raíz unitaria o una autorregresión estacionaria que a un proceso potencialmente explosivo.

**Mecánica**: se ajusta la especificación ADF en cada punto final, **con puntos de inicio que retroceden expansivamente**, y se toma el supremo de los estadísticos.

**Las dos diferencias con el test tipo Chow:** (1) **SADF se calcula en cada instante**, no sólo al final de la muestra; (2) **en lugar de introducir una variable dummy, expande recursivamente el inicio de la muestra**. Al probar todas las combinaciones de un doble bucle anidado, **SADF no asume un número conocido de cambios de régimen ni de fechas de ruptura**.

`[LDP]` El comportamiento observado: **la línea SADF se dispara cuando los precios exhiben comportamiento de burbuja, y vuelve a niveles bajos cuando la burbuja estalla.**

**Tres refinamientos que aporta:**

**(a) Log-precios en lugar de precios crudos.** `[LDP]` El argumento: si con precios crudos se rechaza la nula, significa que los precios son estacionarios con varianza finita. **La implicación es que los retornos no serían invariantes en el tiempo**, porque su volatilidad tendría que decrecer al subir los precios y crecer al bajar, para mantener constante la varianza del precio. **Al correr ADF sobre precios crudos estamos asumiendo que la varianza de los retornos no es invariante al nivel de precios; si de hecho lo es, el modelo será estructuralmente heterocedástico.** Con log-precios, en cambio, **el nivel de precio condiciona la media de los retornos, no su volatilidad**. La diferencia puede no importar en muestras pequeñas, pero **SADF corre regresiones a lo largo de décadas y las burbujas producen niveles significativamente distintos entre regímenes**.

**(b) Complejidad computacional.** `[LDP]` **El algoritmo corre en orden cuadrático** en la longitud de la muestra. Y da cifras concretas: para una serie de dollar bars del E-mini S&P 500 con unas 356.000 observaciones y 3 variables, **una única estimación ADF requiere unos 11 millones de operaciones en coma flotante; una única actualización de SADF, alrededor de 2 TFLOPs; y la serie SADF completa, aproximadamente 242 PFLOPs.** Y advierte que esa cifra **excluye operaciones notoriamente caras como alineación, preprocesado y E/S**. Concluye que puede hacer falta un clúster HPC con una implementación eficientemente paralelizada para estimar la serie en un tiempo razonable.

**(c) Quantile ADF.** `[LDP]` **Tomar el valor extremo introduce problemas de robustez**: las estimaciones SADF pueden variar significativamente según la frecuencia de muestreo y los timestamps concretos de las muestras. Un estimador más robusto de los extremos: usar **un cuantil alto** de la distribución de estadísticos ADF como medida de centralidad, y **la diferencia entre dos cuantiles vecinos como medida de dispersión**. SADF resulta ser el caso particular con cuantil igual a 1.

**Clasificación: `OHLCV-OK`, con una salvedad computacional grave.**

`[IMPLICACIÓN PARA IRIS]` **La advertencia computacional es decisiva para nosotros.** Su ejemplo es sobre ~356.000 barras. Un histórico intradiario de MNQ en barras de un minuto puede superar ese orden de magnitud fácilmente. **Calcular la serie SADF completa sobre nuestros datos no es viable sin paralelización seria o sin reducir drásticamente la resolución.** Alternativas conceptuales (no decisiones): calcular SADF sobre una serie remuestreada más gruesa; calcularlo sólo sobre ventanas recientes; o usar el test Chu-Stinchcombe-White, que es mucho más barato, como sustituto de primera línea.

#### Tests sub/super-martingala

`[LDP]` Tests de explosividad **que no dependen de la especificación ADF estándar**. Se contrasta la existencia de una tendencia temporal explosiva bajo cuatro especificaciones alternativas: **tendencia polinómica (dos variantes), tendencia exponencial y tendencia potencial**. Como en SADF, se ajusta cada especificación en cada punto final con inicios expansivos y se toma el supremo.

`[LDP]` **Dos detalles importantes:**
- **Se toma el valor absoluto**, porque **nos interesan por igual el crecimiento explosivo y el colapso**.
- **El sesgo hacia burbujas largas y su corrección**: la varianza del coeficiente estimado de una burbuja débil y de largo plazo puede ser menor que la de una burbuja fuerte y de corto plazo, **sesgando el método hacia burbujas de largo plazo**. Para corregirlo, se **penalizan las longitudes muestrales grandes** mediante un coeficiente `φ` entre 0 y 1.

`[LDP]` **Y aquí está la propiedad más útil para nosotros:**
> **Conforme `φ` tiende a 0, el estadístico exhibe tendencias más largas, porque la compensación se desvanece y las burbujas de largo plazo enmascaran las de corto plazo. Conforme `φ` tiende a 1, el estadístico se vuelve más ruidoso, porque se seleccionan más burbujas de corto plazo sobre las de largo plazo. En consecuencia, esta es una forma natural de ajustar la señal de explosividad para que filtre oportunidades apuntando a un horizonte de tenencia particular. Las features usadas por el algoritmo de ML pueden incluir el estadístico estimado a partir de un rango amplio de valores de `φ`.**

`[IMPLICACIÓN PARA IRIS]` Esta es una idea con aplicación directa: **una familia de features parametrizada por el horizonte al que apunta**. Si IRIS opera intradiario, valores de `φ` cercanos a 1 seleccionarían las rupturas de corto plazo relevantes para nosotros. Y el propio autor sugiere incluir **varios valores de `φ` simultáneamente como features**, dejando que el modelo elija.

**Clasificación: `OHLCV-OK`**, con la misma advertencia de coste cuadrático.

### 21.4 Qué herramientas responden a las dos preguntas del encargo

`[IMPLICACIÓN PARA IRIS]`

**Pregunta A — "¿El mercado se está comportando de forma distinta a como se comportaba antes?"**

| Herramienta | Compatibilidad | Coste | Nota |
|---|---|---|---|
| Chu-Stinchcombe-White sobre log-precios | `OHLCV-OK` | Bajo | Primera línea razonable. |
| SADF / QADF | `OHLCV-OK` | **Cuadrático** | El más potente y el más caro. |
| Tests SM con familia de `φ` | `OHLCV-OK` | Cuadrático | Ajustable al horizonte. |
| Chow-type DF | `OHLCV-OK` | Alto | Superado por SADF. |

**Pregunta B — "¿La relación aprendida por IRIS puede haber dejado de ser válida?"**

| Herramienta | Nota |
|---|---|
| **Brown-Durbin-Evans** | El único test del capítulo que mide la **estabilidad de una relación features→target**, no de una serie. Conceptualmente el más adecuado para esta pregunta. Requiere que las features y el target estén ya definidos. |
| **Estabilidad temporal de la importancia de features** (§12.2) | El propio autor plantea como programa de investigación preguntar si las features son importantes todo el tiempo o sólo en entornos específicos, qué desencadena cambios de importancia, y si esos cambios de régimen pueden predecirse. |
| **Decaimiento del rendimiento en producción** | El ciclo de vida del capítulo 1 lo contempla como criterio de desmantelamiento. |

`[VACÍO]` **El libro no ofrece un procedimiento operativo para monitorizar la validez de un modelo desplegado.** Describe el ciclo de vida y da herramientas de detección de rupturas en la serie, pero no conecta ambas cosas en un protocolo. Queda abierto.

### 21.5 Doble uso: features y sampling

`[INTERPRETACIÓN]` Conviene señalar que estos estadísticos tienen **dos usos distintos** en el marco del libro, y no deben confundirse:
1. **Como features** de entrada al modelo de ML.
2. **Como variable subyacente del filtro CUSUM** para el muestreo por eventos — el propio autor sugiere declarar un evento cuando el SADF se desvía suficientemente de un nivel de reset previo (§5.3).

El segundo uso es probablemente más barato computacionalmente en la práctica (calculamos el estadístico una vez y lo usamos para seleccionar momentos) y **es el que conecta este capítulo con el problema de unicidad de muestras** (§8): eventos raros y bien espaciados tienen alta unicidad.

---

## 22. FEATURES DE ENTROPÍA (Tarea 20)

### 22.1 Qué mide realmente la entropía en una serie financiera

`[LDP]` El planteamiento conceptual:

> **Las series de precios transmiten información sobre las fuerzas de oferta y demanda. En mercados perfectos los precios son impredecibles, porque cada observación transmite todo lo que se sabe sobre un producto o servicio. Cuando los mercados no son perfectos, los precios se forman con información parcial, y como algunos agentes saben más que otros, pueden explotar esa asimetría informativa. Sería útil estimar el contenido informativo de las series de precios y formar features sobre las que los algoritmos de ML puedan aprender los resultados probables.**

`[LDP]` **Y la hipótesis de trabajo concreta que propone** — esta es la parte más accionable del capítulo:

> **Por ejemplo, el algoritmo de ML puede encontrar que las apuestas de momentum son más rentables cuando los precios llevan poca información, y que las apuestas de reversión a la media son más rentables cuando los precios llevan mucha información.**

`[IMPLICACIÓN PARA IRIS]` Esa hipótesis es **directamente comprobable con nuestros datos** y responde exactamente al tipo de pregunta que IRIS quiere responder ("¿bajo qué condiciones de mercado se genera la señal?"). No requiere ningún dato adicional. **Es una hipótesis, no un hecho: el libro la enuncia como posibilidad, no la demuestra.**

**Qué mide técnicamente.** `[LDP]` La entropía de Shannon es **la cantidad media de información producida por una fuente estacionaria de datos**; el número mínimo de bits por carácter necesarios para describir el mensaje de forma unívocamente decodificable. Es el promedio ponderado por probabilidad del contenido informativo. **La razón de medir la información como el logaritmo del inverso de la probabilidad viene de la observación de que los resultados de baja probabilidad revelan más información que los de alta probabilidad: aprendemos cuando ocurre algo inesperado.**

`[LDP]` Y las conexiones: la **redundancia** está formalmente conectada con la complejidad de una fuente markoviana de información. La **información mutua** es siempre no negativa, simétrica, y vale cero si y sólo si las variables son independientes; **para variables normalmente distribuidas está estrechamente relacionada con la correlación de Pearson**, lo que la convierte en **una medida natural de asociación entre variables, sean lineales o no lineales**.

**Respondiendo a la pregunta del encargo — ¿qué puede medir la entropía?**

| Concepto | ¿Lo mide? | Fundamento |
|---|---|---|
| **Complejidad / desorden** | **Sí, directamente.** | `[LDP]` La entropía puede interpretarse como una medida de complejidad. Una secuencia compleja contiene más información que una regular (predecible). |
| **Predictibilidad** | **Indirectamente.** | `[INTERPRETACIÓN]` Alta entropía significa que la secuencia es difícil de comprimir, es decir, que conocer el pasado ayuda poco a anticipar el siguiente símbolo. Es una medida de predictibilidad **de la secuencia codificada**, no del retorno futuro. |
| **Eficiencia de mercado** | **Sí, es una aplicación explícita.** | `[LDP]` La lista de aplicaciones financieras incluye la eficiencia de mercado. Precios perfectamente informativos ⟹ impredecibles ⟹ máxima entropía. |
| **Régimen** | **Sí, como variable de estado.** | `[INTERPRETACIÓN]` La entropía calculada sobre ventanas móviles produce una serie que puede caracterizar el estado del mercado, y alimentar tanto features como el filtro CUSUM. |
| **Volatilidad** | **Sí, con supuesto de normalidad.** | `[LDP]` Deriva la entropía de un proceso normal IID (para la normal estándar vale aproximadamente 1.42) y señala que esto permite **conectar entropía con volatilidad, obteniendo una estimación de volatilidad implícita por entropía, siempre que los retornos estén efectivamente extraídos de una normal**. |

### 22.2 Los estimadores

`[LDP]`
**Plug-in (máxima verosimilitud)**: se forma un diccionario de todas las palabras de longitud `w` en la secuencia, se estima su distribución empírica, y se calcula la tasa de entropía. **Bajo estacionariedad y ergodicidad, la ley de los grandes números garantiza que para `w` fijo y `n` grande la distribución empírica se acerque a la verdadera.** `w` debe ser suficientemente grande para que la estimación se acerque a la entropía verdadera, y `n` mucho mayor que `w`.

**Lempel-Ziv**: descompone el mensaje en subcadenas no redundantes. **La intuición: los mensajes complejos tienen entropía alta, lo que requerirá diccionarios grandes en relación con la longitud de la cadena.** La versión de Kontoyiannis usa la longitud de la coincidencia más larga: **conforme aumentamos la historia disponible, esperamos que los mensajes de alta entropía produzcan subcadenas no redundantes relativamente más cortas, y los de baja entropía relativamente más largas.**

`[LDP]` **Tres advertencias prácticas sobre el estimador de Kontoyiannis**, todas relevantes:
1. **La tasa de entropía se define en el límite.** Los teoremas prueban convergencia asintótica, **pero no se afirma en ningún sitio una propiedad de monotonía**. Cuando el mensaje es corto, una solución puede ser repetirlo varias veces.
2. **La ventana de emparejamiento debe ser simétrica** (misma longitud para el diccionario que para la subcadena), lo que implica que **el último bit sólo se considera si la longitud del mensaje es par**. Solución: eliminar el primer bit si la longitud es impar.
3. **Algunos bits finales se descartan cuando van precedidos de secuencias irregulares.** Cuando el final del mensaje es particularmente relevante, **una buena solución puede ser analizar la entropía del mensaje invertido**, lo que garantiza que los bits finales se usen y además puedan emparejarse con todos los demás.

`[LDP]` Y el compromiso sesgo/varianza para la ventana: el sesgo es de orden inverso al logaritmo de la ventana y la varianza inversa al número de emparejamientos, lo que da una regla para balancearlos.

### 22.3 Esquemas de codificación

`[LDP]` **Estimar entropía requiere codificar el mensaje**, es decir, discretizar una variable continua para asignar a cada valor un código de un alfabeto finito.

| Esquema | Mecánica | Cuándo es apropiado | Efecto |
|---|---|---|---|
| **Binaria** | 1 si el retorno es positivo, 0 si negativo, eliminando los ceros. | `[LDP]` **Surge naturalmente en series de retornos muestreadas de barras de precio** (barras cuyos precios fluctúan entre dos barreras horizontales simétricas centradas en el precio inicial), porque entonces el retorno absoluto es aproximadamente constante. | Cuando el retorno absoluto puede adoptar un rango amplio, **descarta información potencialmente útil**, especialmente con barras temporales intradiarias afectadas por la heterocedasticidad de la naturaleza inhomogénea de los ticks. |
| **Por cuantiles** | Un código por cuantil, con fronteras determinadas **sobre un período in-sample (conjunto de entrenamiento)**. | Cuando hacen falta más de dos códigos. | Igual número de observaciones por letra dentro de muestra, y aproximadamente igual fuera. **Algunos códigos abarcan una fracción mayor del rango que otros.** Esta distribución uniforme **tiende a aumentar las lecturas de entropía en promedio**. |
| **Sigma** | Se fija un paso de discretización `σ` y se asignan códigos por bandas de ese ancho; **el número de códigos lo determina el propio flujo de precios**. | Cuando queremos que el diccionario refleje la dispersión real. | **Cada código cubre la misma fracción del rango.** Como los códigos **no** están uniformemente distribuidos, las lecturas de entropía tenderán a ser menores en promedio; **pero la aparición de un código "raro" causará picos en la entropía**. |

`[LDP]` **Y una recomendación explícita que conecta capítulos**: aunque no lo desarrolla, **aconseja codificar la información a partir de series fraccionalmente diferenciadas en lugar de enteramente diferenciadas, porque aquellas todavía contienen algo de memoria.**

`[LDP]` Y una observación sobre la heterocedasticidad de las barras temporales: una forma de abordarla parcialmente es **muestrear precios según un proceso estocástico subordinado** —barras de trade o de volumen—, operando en un reloj dirigido por el mercado que **regulariza la distribución de los retornos absolutos y reduce la necesidad de un alfabeto grande**.

### 22.4 El benchmark del proceso gaussiano

`[LDP]` La entropía de un proceso normal IID se deriva analíticamente; **para la normal estándar vale aproximadamente 1.42**. Esto tiene **dos usos**:
1. **Benchmarking del estimador**: podemos extraer muestras de una normal estándar y comprobar qué combinación de estimador, longitud de mensaje y codificación nos da una estimación suficientemente próxima al valor teórico. **Su resultado experimental**: con alfabetos de al menos 10 letras sobre mensajes de longitud 100, el estimador de Kontoyiannis da la respuesta correcta. **Cuando los alfabetos son demasiado pequeños, se descarta información y la entropía se subestima.**
2. **Conexión entropía–volatilidad**: obtener una estimación de volatilidad implícita por entropía.

`[IMPLICACIÓN PARA IRIS]` El primer uso es un **protocolo de validación del estimador antes de aplicarlo a datos reales**, que es exactamente el tipo de higiene que deberíamos adoptar: verificar que nuestra implementación recupera un valor conocido antes de creer lo que nos dice sobre MNQ.

### 22.5 Compatibilidad y valoración

**Clasificación: `OHLCV-OK` en su totalidad.** Todo el capítulo opera sobre series de retornos, que derivamos de cierres. Es una de las familias de features más baratas en términos de requisitos de datos.

**Coste computacional**: el estimador plug-in es barato; el de Kontoyiannis con ventana deslizante es considerablemente más caro, aunque muy inferior al SADF.

`[IMPLICACIÓN PARA IRIS]` Como pide el encargo, **no asumimos que serán útiles**. Lo que podemos afirmar:
- Son **construibles enteramente desde nuestros datos**.
- Aportan una **hipótesis concreta y testeable** (momentum en baja entropía, reversión en alta).
- Son candidatas tanto a **features** como a **variable del filtro CUSUM**.
- **Su sensibilidad al esquema de codificación, al tamaño del alfabeto y a la longitud del mensaje es alta**, lo que significa que cada configuración probada cuenta como un intento en nuestro presupuesto de multiple testing. Ese es un coste real que debe pesarse.

`[VACÍO]` El libro **no presenta evidencia empírica** de que las features de entropía mejoren el rendimiento predictivo. Presenta el aparato y las aplicaciones potenciales, no resultados.

---

## 23. FEATURES MICROESTRUCTURALES — CON EL FILTRO APLICADO ESTRICTAMENTE (Tarea 21)

### 23.1 Lo que el libro asume y nosotros no tenemos

`[LDP]` Abre el capítulo declarando que los datasets microestructurales incluyen información primaria sobre el proceso de subasta: **cancelaciones de órdenes, libro de doble subasta, colas, ejecuciones parciales, lado agresor, correcciones, reemplazos**. La fuente principal son los mensajes FIX, que pueden comprarse a las bolsas. Y su valoración: **el nivel de detalle de los mensajes FIX proporciona la capacidad de entender cómo los participantes ocultan y revelan sus intenciones, lo que convierte a los datos microestructurales en uno de los ingredientes más importantes para construir features predictivas de ML.**

`[IMPLICACIÓN PARA IRIS]` **Ese es exactamente el ingrediente que nuestro diseño renuncia a tener.** Esta sección documenta la renuncia sin proponer revertirla.

### 23.2 Técnicas construibles desde OHLCV

#### Estimador de volatilidad High-Low (Parkinson) — **`OHLCV-OK`**

`[LDP]` **Los estimadores de volatilidad basados en precios máximo y mínimo son más precisos que los estimadores estándar basados en precios de cierre.** Para precios observados continuamente que siguen un movimiento browniano geométrico, la volatilidad puede estimarse robustamente a partir del ratio entre el máximo y el mínimo de la barra, con una constante de escala derivada analíticamente.

`[IMPLICACIÓN PARA IRIS]` **Esta es probablemente la técnica de mayor relación valor/coste de todo el capítulo para nosotros.** Usamos ya High y Low, no requiere nada adicional, y **el propio libro afirma que es más precisa que la desviación estándar de retornos de cierre** — que es la estimación por defecto usada en la triple barrera y en los umbrales dinámicos del capítulo 3. Es un candidato inmediato a mejorar un componente central.

Los ejercicios del libro plantean exactamente la comparación relevante: cómo difiere el estimador High-Low de la desviación estándar de retornos close-to-close en frecuencia semanal, diaria y sobre dollar bars.

#### Corwin-Schultz — **`OHLCV-OK`**

`[LDP]` Estimador del **bid-ask spread a partir de precios máximo y mínimo**, construido sobre dos principios:
1. **Los precios máximos se casan casi siempre contra la oferta, y los mínimos casi siempre contra la demanda.** El ratio máximo/mínimo refleja tanto la volatilidad fundamental como el bid-ask spread.
2. **La componente del ratio máximo/mínimo debida a volatilidad crece proporcionalmente con el tiempo transcurrido entre dos observaciones.**

Se calcula combinando estadísticos sobre una barra y sobre dos barras consecutivas, y **los autores recomiendan fijar a cero los valores negativos**. Como subproducto se obtiene también la **volatilidad Becker-Parkinson**.

`[LDP]` Y una nota sobre su uso: el spread resultante puede estimarse recursivamente sobre ventana móvil, y los valores suavizarse con un filtro de Kalman. Es particularmente útil en mercados sin libro de órdenes centralizado.

`[INTERPRETACIÓN]` Aquí hay un matiz importante para nuestro caso: Corwin-Schultz fue diseñado para inferir el spread donde **no se observa**. En MNQ, que es un contrato extremadamente líquido con spread típicamente de un tick, el valor de estimarlo indirectamente es menor. **Pero la estimación puede seguir siendo informativa como proxy de condiciones de liquidez cambiantes**, aunque su nivel absoluto sea poco fiable. Uso potencial: no como coste, sino como feature de estado de mercado. Los propios ejercicios del libro invitan a comprobar si los valores estimados son consistentes con lo que sabemos de un contrato tan líquido, sugiriendo que el propio autor anticipa discrepancias.

#### Lambda de Amihud — **`OHLCV-COND`**

`[LDP]` Estudia la relación positiva entre **retornos absolutos e iliquidez**, calculando **la respuesta de precio asociada a un dólar de volumen negociado**, y argumentando que su valor es un proxy del impacto de mercado. La implementación agrega, por barra, el retorno absoluto del precio de cierre dividido por el volumen en dólares.

`[LDP]` Y un dato de validación externa que reporta: las estimaciones diarias de la lambda de Amihud exhiben **alta correlación de rangos con estimaciones intradiarias del spread efectivo**.

**Por qué es `OHLCV-COND` y no `OHLCV-OK`:** la formulación original opera sobre **el conjunto de operaciones incluidas en la barra**, sumando el volumen en dólares de cada operación individual. Nosotros aproximaríamos el volumen en dólares como `precio × volumen` de la barra. **La condición**: el precio representativo elegido (cierre, o típico) introduce un error que es pequeño si la barra es fina, pero existe. **Crucialmente, y a diferencia de Kyle y Hasbrouck, la lambda de Amihud NO requiere firmar las operaciones**, lo que la hace la única de las tres lambdas accesible para nosotros.

#### Modelo de Roll — **`OHLCV-COND`**

`[LDP]` Uno de los primeros modelos en proponer una explicación del bid-ask spread efectivo. Asume que el precio medio sigue un random walk sin deriva, y que los precios observados resultan del trading secuencial contra el spread. Bajo los supuestos de que compras y ventas son igualmente probables, serialmente independientes e independientes del ruido, **el spread resulta ser función de la covarianza serial de los cambios de precio**, y el ruido verdadero función de la varianza observada y esa covarianza.

`[LDP]` Reconoce explícitamente que **los supuestos van contra toda observación empírica** —las series financieras tienen deriva, son heterocedásticas, exhiben dependencia serial y sus retornos no son normales— pero añade: **con un procedimiento de muestreo apropiado, como el del capítulo 2, estos supuestos pueden no ser tan irrealistas.**

**Por qué `OHLCV-COND`:** el modelo opera sobre **precios de operaciones individuales** y su alternancia contra bid y ask. Aplicado a cierres de barra, la covarianza serial que mediríamos ya no es principalmente el bid-ask bounce sino la autocorrelación de retornos de barra, **que es una cantidad distinta**. La condición es que la barra sea suficientemente fina para que el rebote domine, lo cual no es verificable con nuestros datos. **Además, la mayor utilidad declarada del modelo es para valores raramente negociados donde las cotizaciones publicadas no son representativas** — la situación opuesta a la de MNQ.

#### Transformaciones de la secuencia de signos — **`GRANULAR`**

`[LDP]` Menciona que transformaciones de la serie de signos de agresor pueden dar features informativas: filtro de Kalman sobre su valor esperado futuro, rupturas estructurales sobre esas previsiones, entropía de la secuencia, t-valores de tests de rachas, y diferenciación fraccionaria de la serie acumulada.

**Clasificación: `GRANULAR`.** Requiere la regla del tick.

`[INTERPRETACIÓN]` **Nota importante**: aunque no podamos construir la secuencia de signos de operaciones, **las transformaciones que él lista (Kalman, rupturas, entropía, tests de rachas, fracdiff) son en sí mismas aplicables a cualquier serie que sí tengamos.** El catálogo de transformaciones es reutilizable aunque el insumo no lo sea. Esto es lo único que rescatamos de esta sección.

### 23.3 Técnicas que requieren datos que NO tenemos

| Técnica | Clasificación | Qué requiere exactamente |
|---|---|---|
| **Regla del tick** | `GRANULAR` | Secuencia de precios de operaciones individuales. |
| **Lambda de Kyle** | `GRANULAR` | Regresión del cambio de precio sobre el **volumen firmado** (flujo de órdenes neto). Requiere el lado agresor. |
| **Lambda de Hasbrouck** | `GRANULAR` | Datos de trade-and-quote (TAQ), con indicador de si cada operación fue iniciada por comprador o vendedor, y estimación bayesiana por muestreo de Gibbs. |
| **PIN** | `GRANULAR` | Ajuste de una mezcla de tres distribuciones de Poisson sobre **volumen comprado y volumen vendido por separado**. |
| **VPIN** | `GRANULAR` | Suma de volúmenes de operaciones iniciadas por compra y por venta dentro de cada barra de volumen. |
| **Distribución de tamaños de orden** | `GRANULAR` | Tamaños de órdenes individuales. |
| **Tasas de cancelación, órdenes límite y de mercado** | `GRANULAR` | Mensajes FIX del libro. |
| **Huella de algoritmos TWAP** | `GRANULAR` | Secuencia temporal de operaciones. |
| **Mercados de opciones** | `OTRAS FUENTES` | Cotizaciones y operaciones de opciones sobre el subyacente. |
| **Autocorrelación del flujo de órdenes firmado** | `GRANULAR` | Signos de operaciones individuales. |
| **Información microestructural (definición propia)** | `OHLCV-COND` | Ver abajo. |

**Sobre esta última**, que merece un comentario. `[LDP]` Propone una definición formal de información microestructural fundada en procesamiento de señales: construir una matriz de features usada por los market makers para decidir si proveer liquidez, etiquetar cada observación según si resultó en beneficio o pérdida de market making, ajustar un clasificador, calcular la **pérdida de entropía cruzada** de sus predicciones fuera de muestra, ajustar un estimador de núcleo sobre la pérdida negativa, y definir la información como el valor de esa distribución acumulada. **La información microestructural queda entendida como la complejidad que enfrentan los modelos de decisión de los market makers.**

`[LDP]` Y la interpretación del flash crash de 2010 bajo esa lente: **la crisis no fue causada por una única predicción inexacta, sino por la acumulación de miles de errores de predicción**. Si los market makers hubieran monitorizado la creciente pérdida de entropía cruzada de sus previsiones, habrían reconocido la presencia de traders informados y la peligrosamente creciente probabilidad de selección adversa.

`[INTERPRETACIÓN]` La construcción concreta requiere features y etiquetas de market making que no tenemos. **Pero la idea abstracta —medir la información como la degradación de la capacidad predictiva de un modelo— es aplicable a cualquier modelo, incluido IRIS.** Monitorizar la pérdida de entropía cruzada de nuestras propias predicciones fuera de muestra a lo largo del tiempo sería un indicador de deterioro directamente construible, y conecta con la pregunta B de §21.4. Esto es una extensión conceptual nuestra, no una propuesta del libro para nuestro caso.

### 23.4 Qué conocimiento perdemos al limitarnos a OHLCV — la limitación documentada

Conforme pide el encargo, esto se registra **como limitación, no como recomendación de aumentar la complejidad**.

**Perdemos, en orden de importancia estimada:**

1. **Toda la capacidad de detectar desbalance de flujo de órdenes.** Es, según el libro, el fenómeno microestructural más asociado a la presencia de traders informados, y la base de las barras dirigidas por información. **Perdemos simultáneamente el esquema de muestreo más sofisticado del capítulo 2 y toda la tercera generación de modelos del capítulo 19.**

2. **La segunda generación de medidas de iliquidez (Kyle, Hasbrouck).** Retenemos Amihud, que es la más simple de las tres. `[LDP]` La iliquidez es una feature informativa importante **porque es un riesgo con prima asociada**.

3. **La capacidad de anticipar el reajuste de precios antes de que ocurra.** `[LDP]` El propósito declarado de las barras de información es sincronizar el muestreo con la llegada de traders informados **para poder decidir antes de que los precios alcancen un nuevo nivel de equilibrio**. Sin esa información, estructuralmente llegamos después.

4. **La huella de participantes concretos.** `[LDP]` Cada participante deja una huella característica en los registros de trading, y con suficiente paciencia puede anticiparse el siguiente movimiento de un competidor. Los algoritmos TWAP dejan huellas muy particulares.

5. **Las features del capítulo 19.6** (tamaños de orden, cancelaciones, autocorrelación del flujo firmado).

**Conservamos:**
- El estimador de volatilidad High-Low, **que el libro considera superior al estándar de cierres**.
- Corwin-Schultz como proxy de condiciones de liquidez.
- La lambda de Amihud como proxy de impacto de precio.
- La observación transversal de que **los t-valores de estas estimaciones suelen ser más informativos que las estimaciones medias**, porque incorporan la desviación del error de estimación — una dimensión de información ausente en las medias. `[LDP]` señala explícitamente que esto no aparece en la literatura pero es su observación práctica.
- El catálogo de transformaciones aplicables a cualquier serie.

`[IMPLICACIÓN PARA IRIS]` **Valoración honesta de la magnitud de la pérdida:** significativa pero acotada. Concentrada en un capítulo de los diecinueve principales, más las barras de información del capítulo 2. **No compromete el núcleo metodológico del libro**, que es lo que da valor a esta fuente para nuestro proyecto. Si en algún momento futuro se reconsiderara ampliar la fuente de datos, **el orden de prioridad que este análisis sugiere sería: datos de tick con precio (habilita regla del tick → barras de información → Kyle → autocorrelación de flujo), antes que datos de quote o de libro completo.** Eso no es una recomendación de hacerlo, es la documentación de dónde estaría el mayor retorno si se hiciera.

---

## 24. HIGH-PERFORMANCE COMPUTING (Tarea 22)

### 24.1 Qué contienen los capítulos 20–22

`[LDP]`
- **Capítulo 20 — Multiprocessing y vectorización**: vectorización; comparación entre hilo único, multihilo y multiproceso; **"átomos y moléculas"** (partición de tareas en unidades atómicas agrupables), con particiones lineales y particiones de doble bucle anidado; motores de multiproceso, llamadas asíncronas, serialización de objetos y reducción de salidas.
- **Capítulo 21 — Fuerza bruta y computadores cuánticos**: optimización combinatoria; enfoque de optimización entera con particiones tipo palomar; evaluación de trayectorias.
- **Capítulo 22 — Computación de altas prestaciones** (capítulo invitado): respuesta regulatoria al flash crash de 2010; hardware y software HPC (MPI, HDF5, procesado in situ); casos de uso incluyendo búsqueda de supernovas, plasma de fusión, el propio flash crash y la calibración de VPIN.

### 24.2 Valoración para IRIS

| Contenido | Valoración |
|---|---|
| **Estructurar funciones para poder llamarlas en paralelo** | **Útil conceptualmente.** `[LDP]` Su consejo general: siempre que se escriba una librería, estructurarla de modo que las funciones puedan invocarse en paralelo. Es una decisión de diseño de bajo coste que se toma al principio y que no se puede añadir fácilmente después. |
| **Particiones lineales y de doble bucle anidado** | **Útil para acelerar experimentos.** Los cuellos de botella reales identificados en este análisis son: la triple barrera (evaluar el camino de cada evento), el sequential bootstrap (cuadrático), MDA (una CV completa por feature), CPCV (un modelo por combinación) y SADF (cuadrático). **La partición de doble bucle anidado está diseñada precisamente para el tipo de estructura del SADF.** |
| **Vectorización** | **Útil**, y de coste marginal cero si se adopta desde el principio. |
| **HDF5** | **Útil** como formato de almacenamiento; mencionado tanto aquí como en el capítulo 22. |
| **Motores de multiproceso, callbacks, pickling** | **Excesivo** para nuestro proyecto en su forma detallada. Las librerías modernas de Python cubren esto con menos fricción. |
| **Computación cuántica (cap. 21)** | **Irrelevante actualmente.** |
| **Infraestructura HPC, MPI, clústeres (cap. 22)** | **Irrelevante actualmente.** |

`[IMPLICACIÓN PARA IRIS]` Siguiendo la instrucción del encargo de no adoptar infraestructura sofisticada por aparecer en el libro: **retenemos únicamente el principio de diseño paralelizable y la elección de formato de almacenamiento eficiente.** Todo lo demás se descarta para la etapa actual.

Pero conviene registrar algo que sí es una **restricción real derivada de este análisis**: varias de las técnicas de nivel A o B de este libro tienen coste computacional alto sobre datos intradiarios (SADF cuadrático, sequential bootstrap cuadrático, MDA y CPCV multiplicativos en el número de features y combinaciones). **El coste computacional no es un detalle de implementación: es un factor que condiciona qué metodologías son viables para nosotros**, y por eso entra explícitamente en la matriz de mínima complejidad (§26).


---

## 25. LÓPEZ DE PRADO APLICADO A IRIS PROJECT (Tarea 23)

Clasificación en cuatro categorías, con justificación explícita en cada caso. **No son decisiones finales**, conforme a la instrucción del encargo.

---

### A — FUNDAMENTOS PROBABLEMENTE NECESARIOS

*Técnicas o principios cuya ausencia comprometería metodológicamente el proyecto.*

| Elemento | Por qué su ausencia comprometería IRIS | Datos |
|---|---|---|
| **Purged K-Fold CV** | Sin purging por solapamiento de etiquetas, **cualquier métrica de validación de IRIS estará contaminada**. Y el mecanismo de fuga es especialmente pernicioso porque **infla el rendimiento de features irrelevantes**, que es precisamente el generador de falsos descubrimientos. No hay sustituto: un split temporal simple no elimina el solapamiento. | `OHLCV-OK` |
| **Embargo** | Ataca un canal distinto del purging: la **correlación serial de las features**, que sobrevive aunque las etiquetas no se solapen. Coste marginal casi nulo (una ventana del orden del 1% de la muestra) sobre un purging ya implementado. | `OHLCV-OK` |
| **Concurrencia y unicidad media de etiquetas** | Sin esta medida **no sabemos cuántas observaciones independientes tenemos**, y por tanto no podemos: (a) configurar correctamente ningún ensemble, (b) juzgar la significación de ningún resultado, (c) dimensionar nuestro presupuesto de multiple testing. Es una cantidad diagnóstica básica, barata de calcular. | `OHLCV-OK` |
| **Ignorar la precisión out-of-bag** | No es una técnica sino una prohibición, y es necesaria: con etiquetas solapadas el OOB está **groseramente inflado** y nos diría que todo funciona cuando no funciona nada. | — |
| **Registro exhaustivo de intentos** | Es **requisito técnico**, no buena práctica: sin el número de intentos y la varianza entre sus Sharpes, **el Deflated Sharpe Ratio es incalculable y el resultado final es literalmente ininterpretable**. Y en un proyecto pequeño es más factible que en uno grande. | — |
| **Deflated Sharpe Ratio (y PSR)** | El PSR corrige por longitud de serie, asimetría y curtosis — las tres patologías que sabemos que tienen los retornos intradiarios. El DSR corrige además por multiple testing. **Sin ellos, un Sharpe reportado no significa nada** dado el número de configuraciones que inevitablemente probaremos. | `OHLCV-OK` |
| **Umbrales de etiquetado escalados por volatilidad** | No es opcional en intradiario: la volatilidad de MNQ varía por un orden de magnitud entre la apertura y la sesión nocturna. Un umbral fijo produce un modelo que **aprende la hora del día**. La alternativa (umbral fijo) está explícitamente identificada por el autor como error común. | `OHLCV-OK` |
| **Ajuste explícito del roll de contratos** | Un salto de roll no ajustado es una ruptura estructural artificial, en fechas conocidas, potencialmente de signo sistemático, y **aprendible por el modelo**. Además contamina retornos, dispara falsamente el filtro de eventos y falsea etiquetas de barrera. Requiere identificar el contrato en la fuente. | `OHLCV-COND` (requiere identificador de contrato) |
| **Separación estricta investigación / backtest** | El principio de que el backtest no es herramienta de investigación y de no hacer backtest hasta que el modelo esté especificado. La cifra de ~20 iteraciones para producir un falso descubrimiento al 5% hace que **el ciclo iterativo de backtests sea el mecanismo de fallo más probable de todo el proyecto**. | — |
| **Feature importance como herramienta de investigación (MDA con purged CV)** | Es la alternativa que el libro ofrece al ciclo de backtests, y **MDA puede concluir que ninguna feature es informativa**, algo que ningún backtest hará nunca. Es el test de realidad más importante disponible. | `OHLCV-OK` |
| **Riesgo de estrategia (marco binomial)** | Aporta viabilidad *ex-ante*: dado un esquema de barreras y una frecuencia de eventos candidatos, calcula qué precisión haría falta. **Nos dice si un diseño puede funcionar antes de gastar meses entrenando**, y a coste computacional nulo. La demostración de que una caída de precisión de 0.70 a 0.67 borra todos los beneficios es exactamente el tipo de fragilidad que debemos conocer de antemano. | `OHLCV-OK` |
| **Métricas de implementation shortfall** | Rendimiento por turnover y retorno sobre costes de ejecución. En un sistema intradiario de alto turnover, **son la diferencia entre una estrategia y una ilusión**. | `OHLCV-OK` |
| **Concentración HHI (positivos, negativos, temporal)** | La concentración temporal es diagnóstica de varios de nuestros modos de fallo específicos (beneficios agrupados en torno a rollovers, o en una franja horaria). Barata y muy informativa. | `OHLCV-OK` |

---

### B — CANDIDATOS A EVALUAR

*Podrían aportar valor, pero deben compararse empíricamente contra alternativas más simples.*

| Elemento | Contra qué debe compararse | Criterio de decisión | Datos |
|---|---|---|---|
| **Triple barrera** | Contra el etiquetado de horizonte fijo con umbral dinámico. | ¿Produce etiquetas más separables? ¿El modelo entrenado sobre ellas rinde mejor fuera de muestra? ¿Y la estrategia resultante sobrevive mejor a costes? **No adoptarla por autoridad.** | `OHLCV-OK` |
| **Meta-labeling** | Contra un modelo único de tres clases y contra un modelo binario con umbral de probabilidad. | ¿Mejora el F1 respecto al primario solo? ¿La ganancia sobrevive al coste de una segunda superficie de sobreajuste y al presupuesto adicional de multiple testing? | `OHLCV-OK` |
| **Muestreo por eventos con CUSUM** | Contra el muestreo de todas las barras y contra el muestreo uniforme. | ¿Aumenta la unicidad media? ¿Mejora el poder predictivo condicionado? ¿O simplemente reduce el tamaño muestral sin ganar nada? Recordar que **cada umbral `h` probado es un intento**. | `OHLCV-OK` |
| **Bet sizing desde probabilidades** | Contra tamaño fijo. | ¿Mejora el Sharpe? Depende críticamente de que las probabilidades estén calibradas, cosa que el libro no aborda. | `OHLCV-OK` |
| **Promediado de apuestas activas + discretización** | Contra sobrescribir la posición con cada señal nueva. | ¿Reduce el turnover lo suficiente para que el edge sobreviva? | `OHLCV-OK` |
| **Fractional differentiation** | **Contra los retornos simples.** | Criterio explícito: ¿aporta importancia incremental bajo MDA y SFI? ¿Sobrevive a la ortogonalización? Y advertencia: una feature con correlación 0.995 con el precio es un vehículo eficiente de memorización. Además, la evidencia del libro es sobre series diarias de décadas; **no hay garantía de que `d*` intradiario se comporte igual**. | `OHLCV-OK` |
| **CPCV** | Contra walk-forward purgado. | Aporta algo cualitativamente distinto (una distribución de Sharpes en lugar de un número, y resistencia estructural al sobreajuste). Pero el coste es multiplicativo. La decisión es **si podemos permitírnoslo**, no si es mejor. | `OHLCV-OK` |
| **Sequential bootstrap** | Contra simplemente fijar `max_samples` a la unicidad media. | La mejora reportada (unicidad media de 0.6 a 0.7) es real pero **modesta**, y el coste es cuadrático. Caso claro de la matriz de mínima complejidad. | `OHLCV-OK` |
| **Ponderación por atribución de retornos y time decay** | Contra pesos uniformes. | Baratos de calcular. El time decay sobre unicidad acumulada (no cronológica) es conceptualmente elegante para intradiario. Pero cada configuración de `c` es un intento. | `OHLCV-OK` |
| **Estimador de volatilidad High-Low (Parkinson)** | Contra la desviación estándar EWM de retornos de cierre. | **Candidato inmediato**: el libro afirma que es más preciso, no requiere datos adicionales, y alimentaría directamente los umbrales dinámicos de la triple barrera. Relación valor/coste probablemente la mejor del capítulo 19. | `OHLCV-OK` |
| **Bagging vs boosting** | Entre sí. | El libro **toma posición a favor del bagging** en finanzas (el sobreajuste preocupa más que el infraajuste, y es paralelizable), pero **es un argumento, no evidencia**. Contradice la práctica dominante. Probar ambos bajo purged CV es barato. | `OHLCV-OK` |
| **Ortogonalización PCA + Kendall tau ponderada** | Contra interpretar importancias directamente. | Es una de las **pocas comprobaciones anti-sobreajuste del libro que funciona sobre un instrumento único**. Barata. Fuerte candidata a entrar en el protocolo estándar. | `OHLCV-OK` |
| **Chu-Stinchcombe-White como feature** | Contra no usar features de ruptura estructural. | Barato computacionalmente. El racional económico (participantes atrapados en transiciones de régimen) es una de las pocas hipótesis económicas concretas del libro, y no requiere multiactivo. | `OHLCV-OK` |
| **Log-loss vs accuracy como scoring** | Entre sí. | **Decisión acoplada al sizing**: si el tamaño depende de la confianza → log-loss; si es fijo → accuracy es defendible. No es una elección independiente. | — |

---

### C — POSIBLES EXTENSIONES FUTURAS

*Útiles pero no necesarias para una primera versión.*

| Elemento | Por qué se pospone |
|---|---|
| **SADF / QADF / tests sub-super-martingala** | Conceptualmente valiosos (especialmente la familia parametrizada por `φ` que ajusta al horizonte de tenencia), pero **el coste es cuadrático**: el propio libro estima ~242 PFLOPs para una serie de 356.000 barras. Sobre intradiario de MNQ no es viable sin paralelización seria o remuestreo agresivo. Chu-Stinchcombe-White es el sustituto barato de primera línea. |
| **Features de entropía** | Enteramente construibles desde OHLCV y con una hipótesis testeable atractiva (momentum en baja entropía, reversión en alta). Pero **el libro no aporta evidencia empírica de utilidad**, y la sensibilidad al esquema de codificación, tamaño de alfabeto y longitud de mensaje multiplica el presupuesto de multiple testing. |
| **Backtesting sobre datos sintéticos (cap. 13)** | El problema que resuelve (sobreajuste al calibrar `[PT, SL]`) puede mitigarse a coste mucho menor derivando las barreras de la volatilidad. Añade una capa entera de supuestos sobre el proceso generador de MNQ intradiario cuya validez es discutible. |
| **Tamaños dinámicos y precios límite** | Requiere infraestructura de gestión de órdenes considerablemente más compleja que "entrar y esperar barrera". |
| **CSCV / PBO** | Muy valioso, pero requiere una matriz de PnL de N configuraciones sincronizadas — es decir, requiere que ya hayamos ejecutado la fase de experimentación completa. Es una herramienta de cierre, no de arranque. |
| **Corwin-Schultz y lambda de Amihud como features de estado** | Construibles, pero su valor en un contrato tan líquido como MNQ es dudoso. El propio libro sugiere que sus estimaciones pueden ser inconsistentes en instrumentos muy líquidos. |
| **HRP para asignar entre estrategias** | Sólo tendría sentido si IRIS acabara produciendo varios modelos o variantes de señal que combinar. Muy posterior. |
| **Monitorización de la pérdida de entropía cruzada del propio modelo** | Extensión conceptual de la definición de información microestructural del autor, aplicada a IRIS. Indicador de deterioro en producción. Requiere que exista producción. |
| **Diseño paralelizable del código** | No es una técnica sino una decisión de arquitectura. **Coste marginal cero si se toma al principio, muy caro si se pospone.** Debería adoptarse ya aunque no se necesite todavía. |

---

### D — INCOMPATIBLES CON NUESTRA RESTRICCIÓN ACTUAL DE DATOS

*Requieren información que nuestro OHLCV no posee.*

| Elemento | Qué requiere exactamente |
|---|---|
| **Barras de tick** | Conteo de transacciones individuales. |
| **Tick Imbalance Bars / Volume Imbalance Bars / Dollar Imbalance Bars** | **Firmar cada operación** mediante la regla del tick. No reconstruible desde OHLCV. El signo de barra (`Close − Open`) **no es un sustituto**: un desbalance de flujo puede ser grande sin que el precio se haya movido, que es precisamente su interés. |
| **Tick Runs Bars / Volume Runs Bars / Dollar Runs Bars** | Secuencia ordenada de signos de operación. |
| **Regla del tick** y todas sus transformaciones (Kalman sobre el signo esperado, entropía de la secuencia de signos, tests de rachas, fracdiff de la serie acumulada de signos) | Secuencia de precios de operaciones individuales. |
| **Lambda de Kyle** | Volumen firmado (flujo de órdenes neto). |
| **Lambda de Hasbrouck** | Datos trade-and-quote con indicador de iniciador. |
| **PIN** | Volumen comprado y vendido por separado. |
| **VPIN** | Volúmenes de operaciones iniciadas por compra y por venta dentro de cada barra de volumen. |
| **Distribución de tamaños de orden, tasas de cancelación, órdenes límite vs mercado, huella de algoritmos TWAP** | Mensajes FIX del libro de órdenes. |
| **Autocorrelación del flujo de órdenes firmado** | Signos de operaciones individuales. |
| **Features de mercados de opciones** | Cotizaciones y operaciones de opciones sobre el subyacente. |
| **ETF trick completo (cestas)** | Múltiples instrumentos. Innecesario para un futuro único según el propio autor. |
| **Pesos PCA para asignación de riesgo** | Múltiples instrumentos. |
| **HRP, tree clustering, cuasi-diagonalización, bisección recursiva** | Matriz de covarianzas entre activos. |
| **Importancia de features paralelizada** | Universo de instrumentos. |
| **Features stacking** | Universo de instrumentos. **Y es el enfoque que el autor declara preferir**, incluida la predicción, precisamente para reducir el sobreajuste a un instrumento único. |
| **Recomendación de desarrollar modelos para clases de activos completas** | Universo de instrumentos. Es la **primera** de sus seis recomendaciones contra el backtest overfitting. |
| **Atribución de PnL por clases de riesgo** | Universo con clasificación por categorías disjuntas. (El principio sí es adaptable a atribución por condición de mercado — ver §18.7.) |

**Aproximaciones parciales posibles, con condiciones declaradas:**

| Elemento | Condición |
|---|---|
| **Barras de volumen** | Aproximables agregando barras temporales hasta alcanzar un umbral de volumen. Pérdidas: frontera cuantizada a la resolución base; VWAP interno perdido; degeneración si una barra base excede el umbral. |
| **Barras de dólar** | Igual, acumulando `precio × volumen` con un precio representativo por barra. Error de segundo orden si la barra base es fina, pero real y medible. |
| **Lambda de Amihud** | La única de las tres lambdas accesible: **no requiere firmar operaciones**. Condición: aproximar el volumen en dólares como `precio × volumen` de barra. |
| **Modelo de Roll** | Condición no verificable: que la barra sea suficientemente fina para que el bid-ask bounce domine la covarianza serial. Y su utilidad declarada es para instrumentos poco líquidos, lo opuesto a MNQ. |
| **Brown-Durbin-Evans** | Requiere features y target ya definidos; el resultado es propiedad de la relación, no de la serie. |

---

## 26. PRINCIPIO DE MÍNIMA COMPLEJIDAD (Tarea 24)

**Criterio**: complejidad añadida frente a problema real resuelto. **"Más sofisticado" no equivale a "mejor".**

Escalas: Complejidad y Beneficio potencial en **Baja / Media / Alta / Muy alta**.

| Metodología | Problema que resuelve | Datos requeridos | Complejidad | Beneficio potencial | ¿Necesaria para primera versión? |
|---|---|---|---|---|---|
| **Purged K-Fold** | Fuga train↔test por solapamiento de etiquetas, que **infla el rendimiento de features irrelevantes** | `OHLCV-OK` | **Media** (implementación propia, ~100 líneas) | **Muy alta** | **SÍ — no negociable.** Sin esto ninguna métrica significa nada |
| **Embargo** | Fuga residual por correlación serial de features | `OHLCV-OK` | **Baja** (un parámetro sobre el purging) | **Alta** | **SÍ.** Coste marginal casi nulo |
| **Unicidad media / concurrencia** | No saber cuántas observaciones independientes tenemos | `OHLCV-OK` | **Baja** | **Muy alta** | **SÍ.** Es diagnóstico básico, y condiciona todo lo demás |
| **Registro de intentos** | Imposibilidad de calcular PBO y DSR; resultado ininterpretable | — | **Muy baja** (disciplina) | **Muy alta** | **SÍ.** Debería ser el primer artefacto del proyecto |
| **PSR / DSR** | Sharpe inflado por muestra corta, no-normalidad y multiple testing | `OHLCV-OK` | **Baja** (fórmulas cerradas) | **Muy alta** | **SÍ** |
| **Umbrales escalados por volatilidad** | Etiquetas que codifican la hora del día en lugar de predictibilidad | `OHLCV-OK` | **Baja** | **Alta** | **SÍ** en intradiario |
| **Ajuste de roll por gaps acumulados** | Rupturas artificiales aprendibles, etiquetas falseadas, eventos espurios | `OHLCV-COND` | **Baja** | **Muy alta** | **SÍ.** Sin esto, todo lo demás está construido sobre datos corruptos |
| **Estimador de volatilidad High-Low** | Estimación de volatilidad menos precisa desde cierres | `OHLCV-OK` | **Muy baja** | **Media-alta** | **Probablemente sí.** Mejor relación valor/coste del capítulo 19 |
| **MDA con purged CV** | Investigar sin usar el backtest; **puede declarar que no hay señal** | `OHLCV-OK` | **Media** (una CV completa por feature) | **Muy alta** | **SÍ.** Es la herramienta de investigación que sustituye al ciclo de backtests |
| **SFI** | Efectos de sustitución que ocultan features útiles | `OHLCV-OK` | **Media** | **Alta** | **Probablemente sí**, dado nuestro espacio de features redundante |
| **MDI** | Ranking rápido in-sample | `OHLCV-OK` | **Baja** | **Media** | Útil como primera pasada; nunca en solitario |
| **Ortogonalización PCA + Kendall tau** | Sustituciones lineales; **y evidencia confirmatoria no supervisada contra el sobreajuste** | `OHLCV-OK` | **Baja** | **Alta** | **Probablemente sí.** Rara comprobación anti-sobreajuste válida en instrumento único |
| **Riesgo de estrategia (binomial)** | No saber si un diseño puede funcionar antes de construirlo | `OHLCV-OK` | **Muy baja** | **Muy alta** | **SÍ.** Análisis de viabilidad previo, coste casi nulo |
| **Implementation shortfall (rendimiento/turnover, retorno sobre costes)** | Estrategias intradiarias que ganan antes de costes y pierden después | `OHLCV-OK` | **Baja** | **Muy alta** | **SÍ** |
| **Concentración HHI** | Beneficios concentrados en pocos eventos o períodos | `OHLCV-OK` | **Baja** | **Alta** | **SÍ.** Diagnóstico de varios modos de fallo específicos nuestros |
| **Triple barrera** | Etiquetas que ignoran el camino y que serían imposibles de sostener operativamente | `OHLCV-OK` | **Media** (evaluación de camino por evento; caro con muchos eventos) | **Alta** | **A evaluar.** Comparar contra horizonte fijo con umbral dinámico |
| **Event sampling (CUSUM)** | Aprender de ruido de fondo; baja unicidad; coste computacional | `OHLCV-OK` | **Baja** | **Alta** | **A evaluar.** Barato y ataca la unicidad en la raíz |
| **Meta-labeling** | Aprender side y size simultáneamente; ausencia de decisión de abstención | `OHLCV-OK` | **Media-alta** (dos modelos, dos validaciones, riesgo de leakage entre ellos) | **Alta** | **A evaluar.** No adoptar por reputación |
| **Bet sizing desde probabilidades** | Acertar mucho en apuestas pequeñas y poco en grandes | `OHLCV-OK` | **Baja** | **Alta** | **A evaluar.** Depende de calibración, que el libro no cubre |
| **Promediado activas + discretización** | Sobretrading por señales sucesivas | `OHLCV-OK` | **Baja** | **Media-alta** | **A evaluar** si hay señales solapadas |
| **Ponderación por atribución de retornos** | Peso desproporcionado de observaciones redundantes | `OHLCV-OK` | **Baja** | **Media** | **A evaluar.** Barato |
| **Time decay** | Relevancia decreciente de ejemplos antiguos | `OHLCV-OK` | **Baja** | **Media** | **A evaluar.** Cada valor de `c` es un intento |
| **Class weights** | Clases raras tratadas como outliers | `OHLCV-OK` | **Muy baja** | **Media** | **Probablemente sí** si hay desbalance |
| **Fractional differentiation** | Memoria borrada por diferenciación entera | `OHLCV-OK` | **Media** (calibración de `d`, ventana FFD larga consume datos) | **Media, incierta** | **NO para la primera versión.** Debe demostrar aporte incremental sobre retornos |
| **CPCV** | Un único camino de backtest, fácil de sobreajustar | `OHLCV-OK` | **Alta** (un modelo por combinación) | **Muy alta** | **A evaluar según presupuesto computacional.** Cambia la naturaleza de la evidencia |
| **Sequential bootstrap** | Redundancia en el muestreo bootstrap | `OHLCV-OK` | **Alta** (cuadrático) | **Baja-media** (0.6 → 0.7 de unicidad) | **NO.** Usar `max_samples = unicidad media`, que resuelve gran parte a coste casi nulo |
| **Chu-Stinchcombe-White** | Detección de cambio de régimen | `OHLCV-OK` | **Baja** | **Media** | **A evaluar.** Sustituto barato del SADF |
| **SADF / QADF / SM tests** | Detección robusta de múltiples burbujas; features ajustables al horizonte | `OHLCV-OK` | **Muy alta** (cuadrático; ~242 PFLOPs para 356k barras) | **Media-alta** | **NO para la primera versión.** Inviable en intradiario sin paralelización seria |
| **Entropy features** | Caracterizar contenido informativo / régimen | `OHLCV-OK` | **Media-alta** (Kontoyiannis con ventana; muchos parámetros = muchos intentos) | **Incierta** (sin evidencia en el libro) | **NO para la primera versión** |
| **Backtesting sintético (cap. 13)** | Sobreajuste al calibrar `[PT, SL]` | `OHLCV-OK` | **Alta** (modelar el proceso generador) | **Media** | **NO.** Barreras escaladas por volatilidad resuelven gran parte a coste mínimo |
| **CSCV / PBO** | Cuantificar la probabilidad de que el resultado sea sobreajuste | `OHLCV-OK` | **Media** | **Alta** | **Al cierre**, no al arranque |
| **Corwin-Schultz / Amihud** | Proxies de liquidez e impacto | `OHLCV-COND` | **Baja** | **Baja-media** en MNQ (muy líquido) | **NO para la primera versión** |
| **Barras de volumen/dólar aproximadas** | Sobre/submuestreo del reloj cronológico | `OHLCV-COND` | **Media** | **Incierta** | **A evaluar.** Medir el error de aproximación antes de creerlas |
| **Diseño paralelizable** | Cuellos de botella en triple barrera, MDA, CPCV | — | **Baja si se hace al principio** | **Alta** | **SÍ como decisión de arquitectura**, aunque no se explote todavía |

### 26.1 Lectura de la matriz

`[INTERPRETACIÓN]` Tres observaciones que emergen al ordenar por relación beneficio/complejidad:

1. **El bloque de mayor beneficio por unidad de complejidad no son las técnicas famosas.** Son: purged CV, unicidad media, registro de intentos, DSR, ajuste de roll, umbrales por volatilidad y riesgo de estrategia. Todas de complejidad baja o media, todas de beneficio alto o muy alto, y **ninguna de ellas es por la que este libro es conocido**.

2. **Varias de las técnicas más citadas del autor caen en la zona de "coste alto, beneficio incierto o modesto para nuestro caso"**: sequential bootstrap (mejora modesta, coste cuadrático), SADF (inviable en intradiario), fracdiff (beneficio no demostrado), backtesting sintético (resoluble más barato). Esto es exactamente lo que el encargo pedía detectar.

3. **Las tres decisiones abiertas de mayor impacto** son triple barrera vs horizonte fijo, event sampling vs muestreo completo, y meta-labeling vs modelo único. Las tres son de complejidad media, beneficio potencialmente alto, y **ninguna puede resolverse sin experimentar sobre nuestros datos**.

---

## 27. PREGUNTAS ABIERTAS DE JANSEN QUE LÓPEZ DE PRADO RESPONDE (Tarea 25)

**Sin comparar autores.** El objetivo es únicamente saber qué vacíos de la Knowledge Base 01 dejan de estarlo.

| Pregunta abierta tras Jansen | ¿La aborda? | Grado | Capítulo | Qué sigue abierto |
|---|---|---|---|---|
| **¿Cómo etiquetar eventos financieros?** | Sí | **Completa** a nivel de método | 3 | Cuál esquema funciona en MNQ; la ambigüedad intrabar si se usan High/Low |
| **¿Es adecuado usar forward returns con horizonte fijo?** | Sí | **Completa** — da tres razones para evitarlo | 3 | Si en nuestro caso concreto la trayectoria aporta lo suficiente para justificar el coste |
| **¿Cómo tratar labels solapados?** | Sí | **Completa** | 4, 7 | Qué magnitud tiene el problema en nuestros datos concretos |
| **¿Cómo medir la unicidad real de una muestra?** | Sí | **Completa** — concurrencia y unicidad media | 4 | El valor numérico para MNQ, que depende del etiquetado elegido |
| **¿Cómo evitar leakage entre train y test?** | Sí | **Completa** | 7 | Nada metodológico; sí el coste de purgar en intradiario con horizontes largos |
| **¿Cómo implementar purging?** | Sí | **Completa**, con criterio formal y código | 7 | — |
| **¿Cómo implementar embargo?** | Sí | **Completa**, con justificación de la asimetría | 7 | El valor concreto de `h` para nuestra serie |
| **¿Qué alternativas al walk-forward tradicional?** | Sí | **Completa** — CV backtesting y CPCV | 12 | Si CPCV es computacionalmente viable para nosotros |
| **¿Cómo manejar que las muestras no sean IID?** | Sí | **Completa** — pesos, sequential bootstrap, configuración de ensembles | 4, 6 | Inconsistencia interna: el cap. 15 vuelve a asumir apuestas IID |
| **¿Cómo decidir cuándo NO operar?** | Sí | **Parcial** — tres mecanismos (meta-etiqueta 0, tamaño≈0 por baja confianza, discretización), y **desaconseja la clase neutra explícita** | 3, 4, 10 | **Cuál de los tres mecanismos es apropiado para IRIS**; y cómo validar los dos modelos conjuntamente |
| **¿Cómo incorporar la confianza de una predicción?** | Sí | **Parcial** — estadístico z contra hipótesis nula explícita | 10 | **Calibración de probabilidades: el libro no la aborda en absoluto** |
| **¿Cómo hacer bet sizing?** | Sí | **Completa** a nivel de método | 10 | Depende de la calibración, que sigue abierta |
| **¿Cómo detectar cambios de régimen o estructurales?** | Sí | **Completa** en detección sobre la serie | 17 | **No hay protocolo de monitorización de un modelo desplegado**; y el coste del SADF |
| **¿Cómo tratar features altamente correlacionadas?** | Sí | **Parcial** — efectos de sustitución, MDI/MDA/SFI, ortogonalización PCA | 8 | La ortogonalización **sólo mitiga sustituciones lineales**; no hay solución para las no lineales |
| **¿Qué esquema de muestreo usar?** | Sí | **Completa conceptualmente** — jerarquía de barras y muestreo por eventos | 2 | **Las barras de información requieren datos que no tenemos**; y no hay evidencia comparativa de cuál funciona mejor |
| **¿Cómo evaluar el backtest overfitting?** | Sí | **Completa** — PBO por CSCV, DSR, longitud del registro de intentos | 11, 14 | Cómo corregir el score de CV por el número de configuraciones de tuning |
| **¿Cómo tratar un único instrumento?** | **No — y advierte en contra** | **No resuelto** | 8, 11 | **Es la tensión estructural principal.** Ver §28 |
| **¿Cómo tratar futuros y rollovers?** | Sí | **Completa** — método de gaps acumulados, precios rolados vs crudos, series no negativas | 2 | Qué convención de roll es preferible; efecto sobre el volumen durante la transición |
| **¿Cuál debe ser el horizonte predictivo?** | **No** | **No resuelto** | — | La barrera vertical es un parámetro libre sin criterio de elección |
| **¿Qué timeframe utilizar?** | **Indirectamente** — argumenta contra el reloj cronológico | **Parcial** | 2 | Qué resolución base y qué esquema para MNQ |
| **¿Qué features contienen señal?** | **No** — da el método para averiguarlo | **No resuelto** | 8 | Todo. Es empírico |
| **¿Qué modelo funcionará mejor?** | **No** — declara ser agnóstico | **No resuelto** | 6 | Toma posición a favor del bagging sobre boosting, pero como argumento, no como evidencia |
| **¿Necesitamos Deep Learning?** | **No lo trata** | **No resuelto** | — | El libro es explícitamente agnóstico al algoritmo |
| **¿Cuánto histórico necesitamos?** | **Parcialmente** — el rango debe incluir un número comprensivo de regímenes; y el DSR liga intentos con longitud | **Parcial** | 14 | La cantidad concreta para MNQ |
| **¿Existe predictibilidad suficiente?** | **No** | **No resuelto** | — | Es la pregunta empírica central |

### 27.1 Balance

`[INTERPRETACIÓN]` De los vacíos que la Knowledge Base 01 dejó explícitamente abiertos, **esta fuente cierra completamente ocho, parcialmente seis, y deja abiertos siete**. Los cerrados son, casi sin excepción, **problemas de método**: cómo etiquetar, cómo ponderar, cómo validar, cómo dimensionar, cómo medir el sobreajuste. Los que quedan abiertos son, casi sin excepción, **preguntas empíricas sobre nuestros datos**: qué horizonte, qué features, qué modelo, cuánta señal hay.

Eso es coherente con lo que el libro declara ser: un manual de método agnóstico al algoritmo. **No nos dice qué funciona; nos dice cómo averiguarlo sin engañarnos.**

Y aparecen **dos vacíos nuevos** que Jansen no había planteado y que esta fuente tampoco resuelve:
1. **La calibración de probabilidades**, ahora crítica porque toda la cadena de bet sizing y abstención depende de ella.
2. **La validación conjunta de un sistema de dos modelos** (primario + meta-labeling), donde el riesgo de leakage entre capas no se aborda.

---

## 28. LIMITACIONES DE LÓPEZ DE PRADO PARA IRIS (Tarea 32)

### A. Lo que podemos adoptar directamente

1. **Purged K-Fold con embargo**, con su criterio formal de concurrencia.
2. **Concurrencia, unicidad media** y su uso para configurar ensembles.
3. **Ponderación por atribución de retornos, time decay sobre unicidad acumulada, class weights.**
4. **Umbrales de etiquetado escalados por volatilidad estimada.**
5. **El método de la triple barrera** con su enumeración de las ocho configuraciones (y el método de horizonte fijo identificado como caso particular degenerado).
6. **Meta-labeling** y la distinción side/size, incluida la restricción lógica de que aprender el lado obliga a barreras simétricas.
7. **Bet sizing desde probabilidades, promediado de apuestas activas, discretización.**
8. **Filtro CUSUM** para muestreo por eventos.
9. **Single future roll** por gaps acumulados, con la distinción precios rolados / precios crudos y la construcción de series no negativas.
10. **Diferenciación fraccionaria (FFD)** y el procedimiento de calibración de `d*`.
11. **MDI, MDA, SFI**, ortogonalización PCA y la **tau de Kendall ponderada como evidencia confirmatoria**.
12. **PSR, DSR** y la exigencia de reportar el número de intentos.
13. **El catálogo completo de estadísticos de backtest**: características generales, concentraciones HHI, drawdown, time under water, implementation shortfall, classification scores.
14. **El marco de riesgo de estrategia** (precisión implícita, frecuencia implícita, probabilidad de fracaso).
15. **CPCV**, si el presupuesto computacional lo permite.
16. **CSCV / PBO** para el cierre.
17. **El estimador de volatilidad High-Low.**
18. **Chu-Stinchcombe-White, SADF, QADF y tests SM** como features (con la salvedad de coste).
19. **Features de entropía** con sus tres esquemas de codificación.
20. **La disciplina de proceso**: separación de fases, backtest sólo al final, registro de intentos, no reutilizar backtests fallidos, ciclo de vida embargo→paper→graduación→decaimiento→retirada.

### B. Lo que podemos adaptar conceptualmente

1. **Barras de volumen y de dólar** → aproximables por agregación de barras temporales, con pérdidas declaradas (frontera cuantizada, VWAP perdido).
2. **La recomendación de buscar consistencia entre contextos** → de "entre instrumentos" a "entre períodos, regímenes de volatilidad y franjas horarias". **Es un análogo más débil**, porque los períodos del mismo instrumento están más relacionados entre sí que instrumentos distintos.
3. **Atribución de PnL por clases de riesgo** → atribución por condición de mercado (franja horaria, régimen, dirección, cercanía al roll), particionando el histórico en categorías disjuntas.
4. **El número de condición de la matriz de covarianzas** → aplicado a nuestra matriz de correlación entre features, como diagnóstico de redundancia.
5. **La definición de información microestructural** (degradación de la capacidad predictiva medida por entropía cruzada) → aplicada a **nuestro propio modelo** como indicador de deterioro.
6. **El catálogo de transformaciones sobre la secuencia de signos** (Kalman, rupturas, entropía, tests de rachas, fracdiff acumulado) → aplicable a cualquier serie que sí tengamos, aunque el insumo original no lo tengamos.
7. **Análisis por quantiles y evaluación de features** → conservando la lógica sin la sección transversal.
8. **HRP** → sólo si en el futuro hubiera varias estrategias que combinar. No dentro de IRIS.

### C. Lo que requiere validación empírica antes de adoptarse

1. **Que la triple barrera sea superior al horizonte fijo con umbral dinámico** en nuestro caso.
2. **Que el meta-labeling supere a un modelo único**, neto del coste de una segunda superficie de sobreajuste.
3. **Que el fracdiff aporte información incremental sobre los retornos.** El libro demuestra preservación de memoria, **no** poder predictivo.
4. **Que el bagging sea preferible al boosting en finanzas.** Es un argumento del autor, no evidencia, y contradice la práctica dominante.
5. **Que el muestreo por eventos mejore el poder predictivo** y no sólo reduzca el tamaño muestral.
6. **Que las barras de volumen/dólar aproximadas conserven las propiedades que el libro atribuye a las auténticas.**
7. **Que el sequential bootstrap justifique su coste cuadrático** frente a fijar `max_samples`.
8. **Que `d*` intradiario en MNQ se comporte como `d*` diario en futuros.** La evidencia del libro es sobre series diarias de décadas.
9. **Que las features de entropía contengan señal.** El libro no aporta evidencia empírica.
10. **Que el estimador High-Low sea efectivamente mejor** que la desviación EWM de cierres para nuestros umbrales.

### D. Lo que necesita datos que no tenemos

Ver la tabla completa en §25-D. Resumen: **toda la capacidad de firmar operaciones**, y con ella las barras dirigidas por información, la regla del tick y sus transformaciones, las lambdas de Kyle y Hasbrouck, PIN, VPIN, y todas las features del capítulo 19.6.

**Lo que perdemos, ordenado por importancia estimada:**
1. Detección de desbalance de flujo de órdenes — el fenómeno más asociado a traders informados según el libro, y **base simultánea del esquema de muestreo más sofisticado del capítulo 2 y de toda la tercera generación del capítulo 19**.
2. Segunda generación de medidas de iliquidez (retenemos sólo Amihud, la más simple).
3. La capacidad de decidir **antes** de que los precios alcancen nuevo equilibrio. Estructuralmente, llegamos después.
4. La huella de participantes concretos (algoritmos TWAP, etc.).
5. Las features de tamaños de orden, cancelaciones y autocorrelación del flujo firmado.

**Valoración honesta de la magnitud**: significativa pero acotada. Concentrada en un capítulo de los diecinueve principales más una sección del capítulo 2. **No compromete el núcleo metodológico**, que es lo que da valor a esta fuente. Si alguna vez se reconsiderara ampliar los datos, el mayor retorno estaría en **datos de tick con precio** (que habilitan la regla del tick y con ella barras de información, Kyle y autocorrelación de flujo), antes que en datos de quote o de libro completo. **Esto es documentación de dónde estaría el retorno, no una recomendación de hacerlo.**

### E. Lo diseñado para portfolios y no para un instrumento único

**Y aquí está la tensión estructural principal de esta fuente para IRIS**, que anticipamos en §0.4 y que debe quedar registrada sin suavizar:

`[LDP]` **La primera de sus seis recomendaciones generales contra el backtest overfitting** es desarrollar modelos para clases de activos o universos completos, no para valores específicos. Su argumento: los inversores diversifican, luego no cometen el error X sólo en el valor Y. **Si encuentras el error X sólo en el valor Y, por rentable que parezca, probablemente sea un falso descubrimiento.**

`[LDP]` Y en el capítulo 8, declara preferir el **features stacking** —apilar datasets de muchos instrumentos— **no sólo para importancia de features sino siempre que un clasificador pueda ajustarse sobre un conjunto de instrumentos, incluida la predicción**, con la razón explícita de que **reduce la probabilidad de sobreajustar un estimador a un instrumento particular o a un dataset pequeño**.

`[INTERPRETACIÓN]` **IRIS es exactamente la configuración que estas dos recomendaciones desaconsejan.** No hay forma de eludirlo, y sería deshonesto presentarlo de otro modo. Lo que sí puede decirse con precisión es **qué defensa concreta perdemos**: la diversificación entre instrumentos funciona como un test de replicación implícito. Un patrón que aparece en cien activos es más difícil de atribuir al azar que uno que aparece en uno.

**Qué defensas nos quedan en su lugar** (todas más débiles que la original, todas presentes en el propio libro):
- **Consistencia temporal**: que la importancia de features y el rendimiento se sostengan a lo largo de períodos y regímenes distintos.
- **CPCV**: múltiples caminos de backtest en lugar de uno.
- **DSR con registro de intentos**: corrección explícita por multiple testing.
- **Concordancia PCA↔importancia**: evidencia confirmatoria no supervisada.
- **El test del bagging**: si aplicar bagging deteriora el rendimiento, la estrategia estaba sobreajustada a pocas observaciones u outliers.
- **La exigencia de teoría económica**: identificar el mecanismo por el que otro participante nos pierde dinero. Y aquí hay un elemento a favor: el racional del capítulo 17 —participantes atrapados en transiciones de régimen— **es una hipótesis económica concreta que no requiere universo multiactivo**.

**Otros elementos específicamente multiactivo:** HRP y toda la asignación de cartera; pesos PCA; ETF trick para cestas; atribución por clases de riesgo; importancia paralelizada; y el propio Information Ratio contra benchmark (en MNQ el benchmark natural es el subyacente del propio contrato, lo que vacía de contenido la noción de alfa).

### F. Lo que añade demasiada complejidad para el beneficio esperado

Con el criterio de §26:

| Elemento | Motivo |
|---|---|
| **Sequential bootstrap** | Coste cuadrático para una mejora de unicidad media de 0.6 a 0.7. La solución simple (`max_samples` = unicidad media) captura gran parte del beneficio a coste casi nulo. |
| **SADF / QADF completos sobre intradiario** | Coste cuadrático; el propio libro estima ~242 PFLOPs para 356k barras. Chu-Stinchcombe-White cubre la función básica a coste bajo. |
| **Backtesting sobre datos sintéticos (cap. 13)** | Añade una capa entera de supuestos sobre el proceso generador para resolver un problema (calibración de `[PT, SL]`) que las barreras escaladas por volatilidad ya mitigan. |
| **Tamaños dinámicos y precios límite** | Requiere infraestructura de órdenes muy superior a "entrar y esperar barrera". |
| **Los capítulos 20–22 (HPC, cuántica, infraestructura)** | Retenemos sólo el principio de diseño paralelizable y la elección de formato de almacenamiento. |
| **La estructura de "research factory"** | El principio de separación de fases sí; la plantilla organizativa de estaciones especializadas con equipos, no. |
| **Features de entropía con exploración amplia de codificaciones** | Cada combinación de esquema, alfabeto y longitud es un intento en el presupuesto de multiple testing. El coste no es computacional sino estadístico. |

### G. Lo que el libro NO responde

1. **Calibración de probabilidades.** Asume que el clasificador entrega probabilidades utilizables y remite a referencias externas. **Toda la cadena de bet sizing y abstención hereda este vacío.**
2. **Validación conjunta de primario + secundario en meta-labeling.** ¿Se entrenan sobre los mismos folds? ¿El primario se reentrena dentro de cada fold? Es un problema real de leakage sin tratar.
3. **Ambigüedad intrabar en la triple barrera.** Si en una barra el máximo toca el objetivo y el mínimo el stop, no sabemos cuál se tocó primero. **En intradiario con barras de un minuto esto no es un caso raro**, y el libro no lo menciona.
4. **Criterio para elegir el umbral `h` del CUSUM** ni la variable subyacente. Da ejemplos sin justificación general.
5. **Criterio para elegir el horizonte** (la barrera vertical) más allá de que es un parámetro.
6. **Corrección del score de CV por el número de configuraciones probadas en tuning.** El DSR corrige Sharpes de estrategias, no scores de validación de hiperparámetros.
7. **Protocolo de monitorización de un modelo desplegado.** Describe el ciclo de vida y da tests de ruptura, pero no los conecta.
8. **Qué convención de roll es preferible** para un futuro sobre índice, ni el efecto de la elección, ni el efecto del roll sobre el volumen durante la transición.
9. **Comparación empírica entre familias de modelos.** Es deliberadamente agnóstico.
10. **Evidencia de que sus propias técnicas mejoren el rendimiento.** El libro presenta métodos y argumentos, **no resultados de estrategias**. Es coherente con su filosofía (no revelar estrategias concretas), pero significa que **adoptamos sus métodos sobre la base de su razonamiento, no de su evidencia**.
11. **Aplicabilidad del marco a frecuencia intradiaria en un instrumento único.** Sus ejemplos son mayoritariamente de barras diarias o de dollar bars sobre futuros a lo largo de décadas.
12. **Inconsistencia interna**: el capítulo 4 argumenta extensamente que las observaciones financieras no son IID, y el capítulo 15 vuelve a asumir apuestas IID para derivar el Sharpe. Las apuestas consecutivas sobre un mismo instrumento están correlacionadas, lo que probablemente **infla** el Sharpe calculado por esas fórmulas.

---

## 29. MATRIZ MAESTRA PARA IRIS (Tarea 27)

Diseñada para poder compararse después con las matrices de Jansen y Murphy.

| Concepto | Qué dice López de Prado | Problema que resuelve | Relevancia IRIS | Compatible OHLCV | Riesgo | Decisión pendiente |
|---|---|---|---|---|---|---|
| **Paradigma de Sísifo / meta-estrategia** | El fracaso viene de pedir a un individuo la cadena completa; la alternativa es una fábrica de investigación con estaciones | Fracaso sistemático de proyectos de ML financiero | Alta (el principio, no la escala) | — | Confundir principio con escala y concluir que un proyecto pequeño es inviable | Qué separación de fases adoptamos |
| **Feature importance ≠ backtest** | El backtest no es herramienta de investigación; la importancia de features sí. ~20 iteraciones bastan para un falso descubrimiento al 5% | Ciclo iterativo de backtests que fabrica falsos positivos | **Muy alta** | `OHLCV-OK` | Reincidir por inercia | Ninguna — es disciplina |
| **Teoría entre features y estrategia** | La teoría debe identificar el mecanismo económico por el que un agente nos pierde dinero | Storytelling a posteriori | Alta | — | La narrativa aumenta la confianza sin aportar evidencia | Qué mecanismo postulamos para MNQ |
| **Crítica al reloj cronológico** | Las barras temporales sobre/submuestrean; GARCH existe en parte por muestrear mal | Correlación serial, heterocedasticidad, no-normalidad inducidas | Alta | Parcial | Adoptar barras alternativas por moda | Qué esquema de muestreo |
| **Tick / volume / dollar bars** | Jerarquía de propiedades estadísticas; dollar bars más estables en conteo | Fragmentación de órdenes, outliers de subasta, acciones corporativas | Media-alta | `GRANULAR` / `OHLCV-COND` | Aproximar y creer que es equivalente | Si aproximamos y con qué resolución base |
| **Information-driven bars** | Muestrear cuando llega información; desbalance de flujo firmado | Llegar tarde al reajuste de precios | Alta si tuviéramos datos | **`GRANULAR`** | Fabricar un sustituto falso desde el signo de barra | Ninguna — no disponible |
| **Single future roll** | Gaps acumulados restados de precios; rolados para PnL, crudos para sizing | Rupturas artificiales aprendibles | **Muy alta** | `OHLCV-COND` | Serie continua empalmada por método desconocido | Exigir identificador de contrato a la fuente |
| **Event sampling (CUSUM)** | Muestrear sólo tras condiciones catalíticas; no dispara por oscilación en torno al umbral | Aprender de ruido de fondo; baja unicidad; coste | **Alta** | `OHLCV-OK` | Cada `h` probado es un intento | Variable subyacente y umbral |
| **Horizonte fijo (crítica)** | Tres razones para evitarlo: soporte temporal, umbral constante, **camino ignorado** | Etiquetas irrealistas operativamente | **Muy alta** | — | Adoptarlo por defecto porque es lo estándar | Ninguna — la crítica es sólida |
| **Umbrales dinámicos** | Escalados por volatilidad EWM | Etiquetas que codifican la hora del día | **Muy alta** | `OHLCV-OK` | — | Qué estimador de volatilidad |
| **Triple barrera** | Etiqueta según primera barrera tocada; ocho configuraciones enumeradas | Posiciones que habrían sido cerradas forzosamente | **Muy alta** | `OHLCV-OK` | **Ambigüedad intrabar no tratada**; coste de evaluar caminos | Cuál configuración; cierres vs High/Low |
| **Side vs Size** | Aprender el lado obliga a barreras simétricas; conocer el lado las libera | Confusión entre dirección y confianza | **Muy alta** | `OHLCV-OK` | — | Qué formulación adopta IRIS |
| **Meta-labeling** | Modelo secundario que decide actuar o pasar; primario con recall alto, secundario corrige precisión | Aprender lado y tamaño simultáneamente; ausencia de abstención | **Muy alta** | `OHLCV-OK` | Segunda superficie de sobreajuste; **leakage entre capas no tratado** | Formulación 1, 2 o 3 |
| **Clase neutra** | **La desaconseja**: innecesaria (se implica de baja confianza) y rompe la ponderación por atribución | Formulación de tres clases | Alta | — | Adoptar LONG/SHORT/NO TRADE sin examinar la alternativa | Si mantenemos la clase explícita |
| **Concurrencia y unicidad** | Formalización completa; 100k filas ≠ 100k observaciones | No saber el tamaño muestral efectivo | **Muy alta** | `OHLCV-OK` | Ignorarlo invalida ensembles, significación y presupuesto de intentos | Ninguna — se adopta |
| **Sequential bootstrap** | Probabilidades decrecientes por redundancia; unicidad 0.6→0.7 | Muestras bootstrap casi idénticas | Media | `OHLCV-OK` | **Coste cuadrático para mejora modesta** | Probablemente sustituir por `max_samples` |
| **Atribución de retornos / time decay** | Peso por unicidad y retorno absoluto; decay sobre unicidad acumulada, no cronológica | Peso desproporcionado de redundantes; ejemplos obsoletos | Media-alta | `OHLCV-OK` | Cada `c` es un intento | Si se aplican y con qué parámetros |
| **Estacionariedad vs memoria** | Los retornos borran la memoria (correlación 0.03 vs 0.995 con `d*=0.35`) | Sobre-diferenciación que destruye señal | Media-alta | `OHLCV-OK` | **Una feature con correlación 0.995 con el precio memoriza la historia**; evidencia es diaria, no intradiaria | Si aporta sobre retornos |
| **Bagging: correlación media** | El bagging sólo funciona si la correlación media < 1 | Ensembles inútiles con muestras redundantes | Alta | `OHLCV-OK` | Confiar en OOB, que estará **groseramente inflado** | Configuración concreta |
| **Bagging vs boosting** | Prefiere bagging en finanzas: el sobreajuste preocupa más que el infraajuste | Elección de familia de ensemble | Media | `OHLCV-OK` | **Es argumento, no evidencia**; contradice la práctica dominante | Probar ambos |
| **Purging** | Eliminar entrenamiento concurrente con test; bidireccional | Fuga por solapamiento de etiquetas | **Muy alta** | `OHLCV-OK` | Implementación incorrecta (mirar sólo `t1.index`) | Ninguna — es requisito |
| **Embargo** | Sólo hacia adelante; ~1% de la muestra | Fuga por correlación serial de features | **Muy alta** | `OHLCV-OK` | — | Valor de `h` |
| **Diagnóstico de `k`** | Si el rendimiento mejora indefinidamente al aumentar `k`, hay fuga residual | Detectar fuga no eliminada | Alta | `OHLCV-OK` | — | Ninguna — se adopta |
| **MDI** | Rápido, in-sample, específico de árboles; importancias suman 1 | Ranking rápido | Media | `OHLCV-OK` | Sujeto a sustitución; **siempre reparte importancia aunque todo sea ruido** | Nunca en solitario |
| **MDA** | Lento, out-of-sample, con purged CV; **puede declarar todo irrelevante** | Investigar sin backtest | **Muy alta** | `OHLCV-OK` | Coste; desviaciones altas sin muchas particiones | Ninguna — se adopta |
| **SFI** | Feature aislada; **sin efectos de sustitución** | Features útiles ocultas por sustitutos | Alta | `OHLCV-OK` | **Pierde efectos conjuntos y jerárquicos** | Complemento, no sustituto |
| **Efectos de sustitución** | La importancia se reparte arbitrariamente entre features correlacionadas | Interpretación errónea con indicadores redundantes | **Muy alta** para nosotros | — | Construir la teoría sobre una elección arbitraria | Cómo agrupamos features |
| **Ortogonalización + Kendall tau** | Concordancia PCA↔importancia como **evidencia confirmatoria no supervisada** | Sobreajuste en la selección de features | **Alta** | `OHLCV-OK` | Sólo mitiga sustituciones **lineales** | Ninguna — se adopta |
| **Features stacking** | Preferido por el autor, incluso para predicción | Sobreajuste a un instrumento | Alta conceptualmente | **`OTRAS FUENTES`** | **Tensión directa con el diseño de IRIS** | Qué análogo temporal adoptamos |
| **Tuning con purged CV** | Pasar `PurgedKFold` al buscador; log-uniforme; F1 para meta-labeling, log-loss para estrategias | Reintroducir fuga en el tuning | Alta | `OHLCV-OK` | **El purged CV no protege del multiple testing del propio tuning** | Presupuesto de búsqueda |
| **Scoring log-loss vs accuracy** | Log-loss considera la probabilidad, no sólo el acierto | Métrica desalineada con el PnL cuando se dimensiona por confianza | Alta | — | Elegir sin considerar el sizing | **Decisión acoplada al sizing** |
| **Bet sizing desde probabilidades** | Estadístico z contra hipótesis nula; tamaño = 2·Z[z] − 1 | Acertar mucho en pequeño y poco en grande | **Muy alta** | `OHLCV-OK` | **Depende de calibración, que el libro no aborda** | Si adoptamos sizing continuo |
| **Promediado activas + discretización** | Promediar apuestas vivas; redondear a pasos | Sobretrading | Alta | `OHLCV-OK` | El paso `d` es un umbral implícito de no-operar | Valor de `d` |
| **Siete pecados del backtest** | Survivorship, look-ahead, storytelling, snooping, costes, outliers, shorting | Errores básicos | Alta (5 de 7 aplican) | — | Nuestro pecado análogo propio es el **roll** | Ninguna |
| **"Aunque sea impecable, probablemente esté mal"** | Sólo un experto produce backtests impecables; ser experto significa haber hecho decenas de miles | Falsa seguridad del backtest limpio | **Muy alta** | — | — | Ninguna |
| **Seis recomendaciones** | Universos completos; bagging como test; backtest al final; registrar todo; simular escenarios; empezar de cero si falla | Backtest overfitting | Alta (5 de 6 aplicables) | — | **La primera choca con nuestro diseño** | Qué defensas sustituyen a la primera |
| **CSCV / PBO** | Combinaciones simétricas; rango OOS de la mejor IS | Cuantificar la probabilidad de sobreajuste | Alta | `OHLCV-OK` | Requiere la matriz completa de intentos | Al cierre |
| **Walk-forward: tres desventajas** | Un solo camino; sesgado por la secuencia; decisiones iniciales con poca información | Falsa confianza en un único backtest | **Muy alta** | — | El argumento del backtest invertido es demoledor | Ninguna |
| **CPCV** | φ[N,k] caminos; **distribución de Sharpes** en vez de un número | Un solo camino sobreajustable | **Muy alta** | `OHLCV-OK` | Coste multiplicativo | Si es viable computacionalmente |
| **Backtesting sintético** | Derivar `[PT,SL]` del proceso, no de simulación | Sobreajuste trivial al calibrar dos umbrales | Media | `OHLCV-OK` | Capa entera de supuestos adicionales | Probablemente no en v1 |
| **Bet ≠ trade** | Una secuencia del mismo lado es una apuesta; contar operaciones sobreestima oportunidades | Sobreestimar oportunidades independientes | Alta | `OHLCV-OK` | — | Ninguna |
| **Concentración HHI** | Positivos, negativos y temporal; perfil de estrategia deseable en seis criterios | Beneficios concentrados en pocos eventos o períodos | **Alta** | `OHLCV-OK` | — | Ninguna — se adopta |
| **Drawdown y TuW** | Percentil 95 de ambas series | Riesgo a la baja por corridas | Alta | `OHLCV-OK` | — | Ninguna |
| **Implementation shortfall** | Rendimiento/turnover; retorno sobre costes de ejecución | Estrategias que ganan sólo antes de costes | **Muy alta** | `OHLCV-OK` | — | Modelo de costes de MNQ |
| **PSR** | Corrige por longitud, asimetría y curtosis; umbral 0.95 | Sharpe inflado por serie corta y colas gruesas | **Muy alta** | `OHLCV-OK` | — | Ninguna |
| **DSR** | Corrige además por multiplicidad; el máximo esperado de N intentos es > 0 aunque el Sharpe real sea 0 | Multiple testing | **Muy alta** | `OHLCV-OK` | **Incalculable sin registro de intentos** | Ninguna — es requisito |
| **Classification scores** | F1 para meta-labeling; degeneraciones documentadas; log-loss considera probabilidad | Métricas infladas por desbalance | Alta | `OHLCV-OK` | Cuatro casos degenerados donde F1 no está definido | Ninguna |
| **Riesgo de estrategia** | Sharpe = f(precisión, frecuencia, pagos); p=0.70→SR 1.17, p=0.72→SR 2, p=0.67→SR 0 | **No saber si un diseño puede funcionar antes de construirlo** | **Muy alta** | `OHLCV-OK` | Asume apuestas IID, contradiciendo el cap. 4 | Ninguna — se adopta como filtro previo |
| **Probabilidad de fracaso** | Bootstrap de la precisión; descartar si > 0.05 | Estrategias intrínsecamente frágiles | Alta | `OHLCV-OK` | — | Umbral objetivo |
| **HRP / Markowitz's curse** | Más correlación → más necesidad de diversificar → soluciones más inestables | Optimización de cartera inestable | Baja (sólo el número de condición sobre features) | `OTRAS FUENTES` | Forzarlo dentro de IRIS | Ninguna — se descarta |
| **Rupturas estructurales: racional** | Participantes atrapados actúan irracionalmente antes de ser forzados a salir | **Hipótesis económica concreta que no requiere multiactivo** | **Alta** | — | Es hipótesis, no hecho | Testearla en MNQ |
| **Chu-Stinchcombe-White** | CUSUM sobre log-niveles; supremo sobre ventanas retrocedientes | Detección barata de cambio de régimen | Media-alta | `OHLCV-OK` | Nivel de referencia arbitrario | Si se incluye como feature |
| **SADF / QADF** | No asume número de rupturas; **log-precios, no crudos**; QADF más robusto que el supremo | Burbujas que colapsan periódicamente | Media-alta | `OHLCV-OK` | **Coste cuadrático: ~242 PFLOPs para 356k barras** | Probablemente no en v1 |
| **Tests SM con φ** | Familia de features **ajustable al horizonte de tenencia** | Sesgo hacia burbujas largas | Media-alta | `OHLCV-OK` | Coste cuadrático | Si el coste lo permite |
| **Entropía** | Hipótesis: momentum rentable con baja entropía, reversión con alta | Caracterizar contenido informativo / régimen | Media | `OHLCV-OK` | **Sin evidencia empírica**; muchos parámetros = muchos intentos | Probablemente no en v1 |
| **Codificación (binaria/cuantiles/sigma)** | Cada esquema sesga las lecturas de forma distinta; codificar sobre fracdiff | Discretizar sin perder información | Media | `OHLCV-OK` | La codificación binaria descarta magnitud en barras temporales | — |
| **Volatilidad High-Low** | **Más precisa que los estimadores basados en cierres** | Estimación de volatilidad para umbrales dinámicos | **Alta** | `OHLCV-OK` | — | Comparar contra EWM de cierres |
| **Corwin-Schultz** | Spread desde máximos y mínimos | Estimar spread donde no se observa | Baja-media en MNQ | `OHLCV-OK` | Poco valor en un contrato de spread de un tick | Probablemente no |
| **Lambda de Amihud** | Respuesta de precio por dólar negociado; **no requiere firmar operaciones** | Proxy de impacto de precio | Media | `OHLCV-COND` | Aproximación del volumen en dólares | A evaluar |
| **Kyle / Hasbrouck / PIN / VPIN** | Iliquidez y probabilidad de trading informado | Detección de traders informados | Alta si tuviéramos datos | **`GRANULAR`** | — | Ninguna — no disponible |
| **t-valores > medias** | Los t-valores incorporan la desviación del error de estimación | Features microestructurales poco informativas | Media | — | Observación no publicada del autor | Aplicable a cualquier estimación por regresión |
| **Información microestructural (definición)** | Complejidad que enfrentan los modelos de los market makers, medida por entropía cruzada | Definición operativa de "información" | Media (adaptada) | `OHLCV-COND` | — | Como indicador de deterioro de IRIS |
| **HPC** | Estructurar funciones para llamada paralela; particiones de doble bucle | Cuellos de botella en triple barrera, MDA, CPCV, SADF | Media (sólo el principio) | — | Adoptar infraestructura por aparecer en el libro | Decisión de arquitectura desde el inicio |

---

## 30. PREGUNTAS QUE LÓPEZ DE PRADO NO NOS PERMITE RESPONDER TODAVÍA (Tarea 28)

### 30.1 Sobre la existencia de señal

1. **¿Existe realmente predictibilidad explotable en MNQ intradiario?** El libro no lo responde para ningún instrumento: presenta métodos, no resultados de estrategias.
2. **¿Existe bajo alguna condición particular?** El muestreo por eventos reformula la pregunta —"¿hay alguna condición bajo la cual el mercado sea predecible?"— pero no la responde.
3. **¿Es el racional de rupturas estructurales aplicable a MNQ?** Es la hipótesis económica más concreta del libro y no está testeada en nuestro instrumento.
4. **¿Es la hipótesis de entropía (momentum en baja, reversión en alta) cierta en MNQ?**

### 30.2 Sobre datos y muestreo

5. **¿Qué resolución base de barra usar?** Condiciona la calidad de toda aproximación de barras alternativas.
6. **¿Qué esquema de muestreo funciona mejor con nuestros datos?** El libro argumenta contra el reloj cronológico pero las alternativas que prefiere (información) no están disponibles.
7. **¿Las barras de volumen/dólar aproximadas conservan las propiedades de las auténticas?** El error de cuantización es medible pero no está medido.
8. **¿Sesión regular, sesión completa Globex, o segmentación por franjas?**
9. **¿Qué convención de roll adoptar?** El libro da el método pero no el criterio de elección.
10. **¿Cuál es el efecto del roll sobre el volumen durante la transición**, si construimos barras de volumen?
11. **¿Cuánto histórico tenemos en observaciones efectivamente independientes?** Depende circularmente del etiquetado y el muestreo elegidos.
12. **¿Cuántos regímenes distintos contiene nuestro histórico?** El libro exige un número comprensivo sin definir cuántos.

### 30.3 Sobre el etiquetado

13. **¿Qué target final debe usar IRIS?**
14. **¿Triple barrera será mejor que un target simple con umbral dinámico?**
15. **¿Qué configuración de las ocho?** ¿`[1,1,1]`, `[0,1,1]` u otra?
16. **¿Barreras simétricas o asimétricas?** Está acoplado a si aprendemos el lado.
17. **¿Qué multiplicadores de volatilidad para las barreras?** Cada par probado es un intento.
18. **¿Qué horizonte (barrera vertical)?** El libro no da criterio.
19. **¿Comprobar barreras contra cierres o contra High/Low?** **Y si es contra High/Low, cómo resolver la ambigüedad intrabar**, que el libro no menciona.
20. **¿Etiquetar la barrera vertical con el signo del retorno o con 0?** El autor declara preferir el signo pero indica explícitamente que hay que explorarlo.

### 30.4 Sobre la formulación del problema

21. **¿Formulación 1, 2 o 3?** (modelo único de tres clases / primario+secundario / probabilidad sobre señal exógena).
22. **¿Meta-labeling será mejor que clasificación multiclase** neto del coste de la segunda capa?
23. **Si adoptamos meta-labeling, ¿qué modelo primario?** Y si es un modelo de ML entrenado por nosotros, ¿se pierde la ventaja de caja blanca?
24. **¿Cómo validar conjuntamente primario y secundario sin leakage?** Vacío del libro.
25. **¿Mantenemos una clase de no-operar explícita**, pese a que el autor la desaconseja?

### 30.5 Sobre features

26. **¿Qué features contienen realmente señal en MNQ?**
27. **¿Qué indicadores técnicos funcionan?** El libro no trata análisis técnico salvo como posible modelo primario.
28. **¿Necesitamos fractional differentiation?** ¿Cuál es `d*` intradiario en MNQ y aporta sobre retornos?
29. **¿Cuántas features podemos permitirnos evaluar** dado nuestro presupuesto de multiple testing?
30. **¿Cómo agrupamos features redundantes** antes de interpretar importancias?
31. **¿Es el estimador High-Low mejor que la EWM de cierres** para nuestros umbrales?
32. **¿Aportan las features de ruptura estructural?** ¿Y a qué coste computacional?
33. **¿Aportan las features de entropía?** ¿Con qué codificación?

### 30.6 Sobre muestreo por eventos

34. **¿Qué variable subyacente para el CUSUM?** (retornos, retornos absolutos, fracdiff, SADF, entropía).
35. **¿Qué umbral `h`?** Sin criterio en el libro, y cada valor es un intento.
36. **¿Mejora el poder predictivo o sólo reduce el tamaño muestral?**

### 30.7 Sobre modelos

37. **¿Qué modelo funcionará mejor?** El libro es deliberadamente agnóstico.
38. **¿Bagging o boosting?** Toma posición argumentada, no evidencia.
39. **¿Qué configuración de ensemble dada nuestra unicidad media?**
40. **¿Cómo calibrar las probabilidades?** Vacío del libro y crítico para todo el sizing.

### 30.8 Sobre validación

41. **¿Qué técnica de validación es óptima para nuestra cantidad real de datos?**
42. **¿Es CPCV computacionalmente viable para nosotros?** ¿Con qué `N` y `k`?
43. **¿Cuánto entrenamiento perdemos por purging + embargo** en intradiario con nuestros horizontes?
44. **¿Qué valor de embargo `h`?**
45. **¿Cuántas hipótesis podemos permitirnos probar** dado el número de observaciones independientes?
46. **¿Cómo corregir el score de CV por el número de configuraciones de tuning?** Vacío del libro.

### 30.9 Sobre decisión y ejecución

47. **¿Qué define exactamente una oportunidad LONG / SHORT / NO TRADE?**
48. **¿Sizing continuo o fijo?** Decisión acoplada a la métrica de scoring.
49. **¿Qué paso de discretización `d`?** Es un umbral implícito de abstención.
50. **¿Qué frecuencia de operación será viable** dados los costes reales?
51. **¿Qué costes reales tendremos en MNQ** (comisión, spread, slippage) a nuestra frecuencia candidata?
52. **¿Cuál es el edge mínimo por apuesta que hace viable la estrategia?** El marco de riesgo de estrategia permite calcularlo, pero requiere fijar antes `π₊`, `π₋` y `n`.
53. **¿Qué precisión necesitaría IRIS** para un Sharpe objetivo dado nuestro esquema de barreras candidato? ¿Es plausible?
54. **¿Qué drawdown y time under water son aceptables?**

### 30.10 Sobre el instrumento único

55. **¿Cómo compensamos la ausencia de la defensa que da un universo multiactivo?** El libro la señala como su primera recomendación y no ofrece sustituto.
56. **¿Es el análogo temporal (consistencia entre períodos y regímenes) suficientemente fuerte?** Es interpretación nuestra, no propuesta del libro.
57. **¿Qué significa "alfa" cuando el benchmark natural es el subyacente del propio contrato?**

### 30.11 Sobre producción

58. **¿Cómo monitorizar que IRIS sigue siendo válido tras el despliegue?** El libro describe el ciclo de vida y da tests de ruptura, pero no los conecta en un protocolo.
59. **¿Con qué frecuencia reentrenar?**
60. **¿Qué criterio de retirada?**

---

## 31. CONOCIMIENTO QUE DEBEMOS CONSERVAR PARA LA PRÓXIMA ETAPA (Tarea 29)

Lo que debe permanecer en memoria al estudiar **John J. Murphy — Technical Analysis of the Financial Markets**. Sin comparar, sin anticipar.

### 31.1 Principios que deben sobrevivir a cualquier fuente posterior

1. **El backtest no es herramienta de investigación.** La importancia de features sí lo es. Bastan ~20 iteraciones para fabricar un falso descubrimiento al 5%.
2. **Nunca hacer backtest hasta que el modelo esté completamente especificado.** Si falla, empezar de cero.
3. **Todo resultado debe reportarse con el número de intentos que costó producirlo.** Sin eso es ininterpretable.
4. **Las observaciones financieras no son IID.** El número de filas no es el número de observaciones.
5. **La fuga en presencia de features irrelevantes es lo que produce falsos descubrimientos**, no la fuga en presencia de features buenas.
6. **Predicción ≠ rentabilidad.** El Sharpe depende de precisión, frecuencia **y estructura de pagos**. Un 65% de acierto puede perder dinero; un 30% puede ganarlo.
7. **El camino importa.** Una estrategia no puede beneficiarse de posiciones que habrían sido cerradas forzosamente.
8. **La estacionariedad es necesaria pero no suficiente.**
9. **Un backtest impecable probablemente esté equivocado**, precisamente porque hizo falta experiencia para producirlo.
10. **Storytelling**: siempre hay una explicación a posteriori. La única defensa es formular la teoría y **testearla sobre datos independientes**.
11. **Una teoría debe identificar el mecanismo por el que otro participante nos pierde dinero.**
12. **Preferir robustez a optimalidad.** Lo óptimo in-sample puede ser malo out-of-sample.

### 31.2 Preguntas concretas que llevamos a Murphy

`[INTERPRETACIÓN]` Y aquí hay un dato estructural que conviene registrar antes de la siguiente etapa: **López de Prado propone explícitamente el análisis técnico como modelo primario de un sistema de meta-labeling.** Sus propios ejercicios plantean desarrollar una estrategia de seguimiento de tendencia basada en cruce de medias móviles, y una de reversión a la media basada en bandas de Bollinger, derivar meta-etiquetas sobre ellas, y entrenar un clasificador para decidir si operar o no. Y afirma que puede añadirse una capa de meta-labeling **a cualquier modelo primario, incluida una regla técnica de trading**.

Esto significa que la tercera fuente **puede tener un papel estructural y no decorativo**: como generador de hipótesis de lado (side) sobre las que IRIS aprendería el tamaño. **No lo decidimos ahora**, pero cambia qué debemos buscar en Murphy.

**Sobre tendencia:**
- ¿Qué define operativamente una tendencia, y en qué escala temporal?
- ¿Puede una regla de tendencia servir como modelo primario con **recall alto** aunque su precisión sea baja? Ese es el perfil que el meta-labeling requiere.
- ¿Cómo se relaciona el concepto de tendencia con la explosividad y las rupturas estructurales del capítulo 17?

**Sobre momentum:**
- ¿Qué indicadores de momentum existen y qué miden exactamente?
- ¿Son transformaciones distintas de la misma información, o capturan dimensiones separadas? (Es la pregunta de los efectos de sustitución, formulada antes de generar las features.)

**Sobre volumen:**
- ¿Qué papel atribuye el análisis técnico al volumen, y es construible desde nuestro OHLCV?
- ¿Ofrece algún sustituto conceptual del flujo de órdenes firmado que nosotros no podemos calcular?

**Sobre volatilidad:**
- ¿Qué medidas de volatilidad propone, y cómo se relacionan con los umbrales dinámicos de la triple barrera?
- ¿Hay algo mejor que la EWM de retornos o el estimador High-Low para escalar barreras?

**Sobre soportes y resistencias:**
- ¿Son niveles definibles causalmente, sin mirar el futuro? Esta es una pregunta crítica: **un nivel identificado a posteriori es look-ahead puro.**
- ¿Pueden servir como barreras de precio en un esquema de etiquetado, en lugar de múltiplos de volatilidad?
- ¿Ofrecen un mecanismo económico explicable (dónde están las órdenes, quién queda atrapado)?

**Sobre patrones:**
- ¿Son reglas reproducibles o juicios discrecionales? Sólo lo primero es programable.
- ¿Definen eventos que podrían servir como filtro de muestreo, en el sentido del capítulo 2?

**Sobre indicadores técnicos en general:**
- ¿Cuál es el **racional económico** que el análisis técnico ofrece para cada indicador? Es lo que la estación de estrategas exige.
- ¿Qué grado de redundancia hay entre ellos? (Anticipar los efectos de sustitución.)
- ¿Cuántos parámetros libres tiene cada uno? **Cada parametrización probada es un intento en nuestro presupuesto de multiple testing.**

**Y una pregunta transversal:**
- ¿El análisis técnico ofrece hipótesis **falsables**, o un vocabulario descriptivo? La diferencia determina si puede funcionar como modelo primario o sólo como fuente de features.

### 31.3 Advertencias que llevamos con nosotros

`[INTERPRETACIÓN]` Tres cautelas específicas al abordar la siguiente fuente, derivadas de lo aprendido aquí:

1. **Todo indicador técnico es un candidato a feature, no una señal validada.** Y cada uno que evaluemos consume presupuesto de multiple testing.
2. **La redundancia entre indicadores será extrema**, y los efectos de sustitución harán que el ranking de importancia entre ellos sea en buena medida arbitrario. Debemos anticipar la agrupación antes de generar.
3. **Cualquier regla que requiera identificar un nivel, un patrón o un punto de inflexión debe ser verificada como estrictamente causal.** Un soporte trazado sobre el gráfico completo es look-ahead; un soporte calculado con información disponible en cada instante no lo es. Es la misma distinción que separa un filtro de Kalman causal de un suavizado.

### 31.4 Lo que NO debemos llevar

- Ninguna conclusión sobre qué target, qué horizonte, qué features o qué modelo.
- Ninguna cifra de rendimiento como referencia (el libro no ofrece resultados de estrategias).
- La presunción de que las técnicas más citadas del autor son las más útiles para nuestro caso. La matriz de §26 sugiere lo contrario.
- La presunción de que un proyecto de instrumento único es inviable. **Es una configuración desaconsejada por el autor, con defensas sustitutivas más débiles, no una imposibilidad.**

### 31.5 La pregunta central de esta etapa, respondida

> **"¿Qué debemos aprender de Marcos López de Prado antes de intentar construir, exclusivamente a partir del comportamiento intradiario y OHLCV del MNQ, un sistema de IA capaz de generar señales operativas robustas, evitando los errores metodológicos característicos del Machine Learning financiero?"**

Cuatro cosas, en orden de importancia:

**Primero, que el problema no es predecir sino no engañarse.** El aporte central de esta fuente no es una técnica sino una arquitectura de defensas contra el autoengaño: purging y embargo contra la fuga, unicidad contra la ilusión de tamaño muestral, DSR contra el multiple testing, CPCV contra el camino único, y la prohibición de investigar con el backtest contra el mecanismo de fallo más probable de todos. **Y casi todas esas defensas son implementables con OHLCV puro y a coste bajo.**

**Segundo, una teoría del etiquetado que no teníamos.** La crítica al horizonte fijo, los umbrales escalados por volatilidad, la triple barrera con sus ocho configuraciones, la distinción side/size y el meta-labeling. Esto cierra el vacío más grave que dejó la etapa anterior, y lo hace con métodos que **operan sobre la serie de precios y nada más**.

**Tercero, la cadena completa desde la predicción hasta la decisión.** Probabilidad → estadístico z → tamaño continuo → promediado → discretización → tamaño cero. Es la primera vez que tenemos un mecanismo articulado para responder "¿qué confianza tiene la señal?" y "¿debemos abstenernos?", y la respuesta que da es que **la abstención no necesita ser una clase: emerge de la falta de confianza**.

**Cuarto, y quizá lo más valioso: la capacidad de saber si un diseño puede funcionar antes de construirlo.** El marco de riesgo de estrategia permite calcular, a coste computacional nulo, qué precisión exigiría un esquema de barreras y una frecuencia dados. Si la respuesta es implausible, lo sabemos antes de gastar meses. Si es plausible, la pregunta se desplaza a los costes — que es la pregunta correcta.

**Y lo que esta fuente explícitamente no nos permite concluir:** que exista predictibilidad explotable en MNQ; que sus técnicas mejoren el rendimiento (presenta métodos y argumentos, no resultados); que un modelo sea mejor que otro; que la triple barrera, el meta-labeling, el fracdiff, el CUSUM o el CPCV sean apropiados para nuestro caso concreto; **ni que un sistema de instrumento único sea una buena idea** — sobre lo cual, de hecho, advierte en sentido contrario.

---

## APÉNDICE — REGISTRO DE DECISIONES DELIBERADAMENTE NO TOMADAS

Conforme a las reglas metodológicas del encargo, este análisis **no** ha seleccionado:

- ni el target, ni el esquema de etiquetado, ni la configuración de barreras, ni el horizonte;
- ni el timeframe, ni la resolución base, ni el esquema de muestreo;
- ni la formulación del problema (una clase, dos modelos, o meta-labeling sobre señal exógena);
- ni las features, ni si aplicar fractional differentiation, ni el umbral del CUSUM;
- ni el modelo, ni la familia de ensemble, ni la configuración de hiperparámetros;
- ni el esquema de validación final (walk-forward purgado vs CPCV);
- ni el método de sizing, ni el criterio de abstención, ni el paso de discretización.

Se ha establecido, eso sí, un conjunto de **restricciones metodológicas** que cualquier diseño posterior deberá respetar: validación con purging y embargo, medición de la unicidad, registro de intentos, corrección por multiple testing, ajuste explícito del roll, umbrales escalados por volatilidad, y separación estricta entre investigación y backtest.

Todas las decisiones permanecen abiertas hasta después de:

```
JANSEN            (completado — Knowledge Base 01)
   +
LÓPEZ DE PRADO    (completado — Knowledge Base 02)
   +
MURPHY            (pendiente)
        ↓
IRIS PROJECT — KNOWLEDGE SYNTHESIS
        ↓
ANÁLISIS DE LOS DATOS REALES DEL MNQ
        ↓
FORMULACIÓN DEL PROBLEMA
        ↓
DISEÑO EXPERIMENTAL → BASELINES → MODELOS → VALIDACIÓN → SEÑALES
```

**Fin del documento — IRIS PROJECT KNOWLEDGE BASE 02.**
