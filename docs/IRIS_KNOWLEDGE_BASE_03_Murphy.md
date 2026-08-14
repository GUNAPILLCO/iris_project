# IRIS PROJECT — KNOWLEDGE BASE 03
## Análisis Técnico de los Mercados Financieros — John J. Murphy

**Estado:** memoria técnica permanente del proyecto.
**Etapa:** 3 de 3 (Jansen ✔ → López de Prado ✔ → **Murphy** → Knowledge Synthesis).
**Fuente:** PDF con capa OCR, 547 páginas. Utilizada directamente; no se ejecutó OCR adicional.
**Regla de esta etapa:** no se diseña IRIS. Se extraen conceptos e hipótesis, se evalúa formalizabilidad, causalidad y disponibilidad de datos, y se mantienen abiertas todas las decisiones.

---

## CHECKPOINT DE EJECUCIÓN

```
PDF: Murphy OCR — 547 páginas (índice interno 0–547)
Última página efectivamente revisada: idx 529 (libro completo)
Último capítulo completado: LIBRO COMPLETO (19 capítulos + 4 apéndices)
Última sección del KB completada: §33 (control de calidad) — TODAS COMPLETADAS
Siguiente capítulo/sección: — (ninguna)
Pendientes: ninguno
Estado: COMPLETE
```

---

## 0. CÓMO LEER ESTE DOCUMENTO

### 0.1 Convenciones de atribución

| Etiqueta | Significado |
|---|---|
| `[MURPHY]` | Afirmación, definición o técnica que el libro sostiene explícitamente. |
| `[INTERPRETACIÓN]` | Inferencia propia razonable a partir del libro. No aparece formulada así. |
| `[IMPLICACIÓN PARA IRIS]` | Consecuencia potencial para el proyecto. **No es una decisión.** |
| `[CONOCIMIENTO EXTERNO AL LIBRO]` | Observación que no proviene de Murphy. Uso deliberadamente escaso. |
| `[VACÍO]` | Pregunta relevante que el libro no responde o trata insuficientemente. |

### 0.2 Filtro de disponibilidad de datos

Fuente única de IRIS: `Timestamp + Open + High + Low + Close + Volume` del MNQ.

| Código | Significado |
|---|---|
| **`OHLCV-OK`** | Construible causalmente sólo con Timestamp + OHLCV. |
| **`OHLCV-COND`** | Construible bajo aproximaciones, supuestos o pérdida de información **declarados**. |
| **`GRANULAR`** | Requiere ticks, trades individuales, bid/ask, aggressor side o secuencia intrabar. **No disponible.** |
| **`OTRAS FUENTES`** | Requiere otros instrumentos, índices, open interest, opciones, sentimiento o fundamentales. |
| **`NO RELEVANTE`** | No responde al problema actual. |

**Regla estricta:** no se fuerza ninguna técnica para hacerla compatible con OHLCV. Si requiere información que no tenemos, se declara.

### 0.3 Escala de causalidad y look-ahead

Aplicada a toda técnica potencialmente cuantificable. Pregunta única: *¿podría calcularse exactamente en `t` con información disponible hasta `t`?*

| Código | Significado |
|---|---|
| **`CAUSAL`** | Calculable en `t` sin ambigüedad. |
| **`CAUSAL-CONF`** | Calculable en `t` sólo tras un evento de confirmación posterior; la señal existe pero **llega con retardo estructural**. |
| **`LOOK-AHEAD-LEVE`** | Requiere confirmación de barras futuras para fijar un punto (p. ej. pivote); formalizable con retardo explícito, al coste de retrasar la señal. |
| **`LOOK-AHEAD-GRAVE`** | El patrón sólo es identificable una vez conocido el desenlace. Formalización causal dudosa o imposible sin reformular el concepto. |

### 0.4 Distinción descripción / predicción / operación

Aplicada a cada concepto importante, conforme al encargo:

- **(A) Descripción** — la variable caracteriza el estado actual del mercado.
- **(B) Hipótesis predictiva** — se afirma que ese estado contiene información sobre el futuro.
- **(C) Regla operativa** — se transforma en comprar / vender / no operar.

`[INTERPRETACIÓN]` Adelanto una observación que recorrerá todo el documento: **Murphy pasa de (A) a (C) con enorme frecuencia y casi nunca se detiene en (B) para someterla a prueba.** El libro es rico en descripciones y en reglas operativas, y estructuralmente pobre en evidencia de la hipótesis predictiva intermedia. Esto no lo invalida como fuente de hipótesis; sí determina cómo debemos usarlo.

### 0.5 Advertencia estructural previa (leer antes que nada)

`[INTERPRETACIÓN]` Esta tercera fuente es **cualitativamente distinta** de las dos anteriores, y conviene fijar la diferencia antes de entrar en detalle:

1. **No contiene evidencia estadística.** No hay una sola prueba de significación, ni un backtest, ni una tasa de acierto medida en todo el libro. Murphy argumenta mediante ejemplos gráficos seleccionados y mediante razonamiento psicológico.
2. **Es un libro visual.** Muchos conceptos centrales se definen mostrando un gráfico, no mediante una regla. Esto tiene una consecuencia directa: **la formalización es tarea nuestra, no suya**, y cada formalización introduce grados de libertad que Murphy nunca tuvo que declarar.
3. **Su horizonte natural es diario, semanal y mensual.** Las excepciones intradiarias son escasas y están señaladas en §29.
4. **Su valor para IRIS no es el catálogo de indicadores** —que Jansen ya cubría con más precisión matemática— **sino el racional de mercado**: por qué debería existir una regularidad, qué participantes la producen y qué los obliga a actuar. Ese es exactamente el ingrediente que López de Prado exige a la estación de estrategas y que ninguna de las dos fuentes anteriores aportaba.

---

## MAPA COMPLETO DEL LIBRO

Índices de página del PDF (0–547) verificados por localización de encabezados.

| # | Capítulo | Idx PDF | Tema / problema | Datos requeridos | Nivel |
|---|---|---|---|---|---|
| 1 | Filosofía del análisis técnico | 26–49 | Las tres premisas; técnico vs fundamental; aplicabilidad | — | **A** |
| 2 | Teoría de Dow | 50–61 | Antecedente conceptual; tendencias, fases, confirmación | `OTRAS FUENTES` (parcial) | **B** |
| 3 | Construcción de gráficos | 62–75 | Tipos de gráfico; barras; velas; escala; volumen; interés abierto | `OHLCV-OK` / `OTRAS FUENTES` | **B** |
| 4 | Conceptos básicos de tendencia | 76–125 | Tendencia, soportes/resistencias, líneas, canales, retrocesos, gaps | `OHLCV-OK` | **A** |
| 5 | Modelos de cambio | 126–157 | Patrones de reversión (H-C-H, dobles, triples, platillos, púas) | `OHLCV-OK` | **B** |
| 6 | Modelos de continuidad | 158–185 | Triángulos, banderas, cuñas, rectángulos, movimiento medido | `OHLCV-OK` | **B** |
| 7 | Volumen e interés abierto | 186–209 | Volumen como indicador secundario; OI en futuros; opciones | `OHLCV-OK` / `OTRAS FUENTES` | **A** |
| 8 | Gráficos a largo plazo | 210–221 | Perspectiva multitemporal; **contratos continuos de futuros** | `OHLCV-COND` | **B** |
| 9 | Medias móviles | 222–249 | SMA/EMA/ponderada, cruces, envolventes, Bollinger, adaptativas | `OHLCV-OK` | **A** |
| 10 | Osciladores e impulso | 250–289 | Momento, TDC, IMM, IFR/RSI, estocástico, %R, CDMM/MACD, sentimiento | `OHLCV-OK` / `OTRAS FUENTES` | **A** |
| 11 | Puntos y figuras | 290–319 | Filtrado del ruido por movimiento de precio, no por tiempo | `OHLCV-COND` | **C** |
| 12 | Velas japonesas | 320–343 | Geometría OHLC de una o pocas barras; patrones nominales | `OHLCV-OK` / `GRANULAR` | **B** |
| 13 | Ondas de Elliott | 344–363 | Estructura ondulatoria, Fibonacci, retrocesos y objetivos | `OHLCV-OK` (nominal) | **C** |
| 14 | Ciclos temporales | 364–397 | Periodicidad, ciclos dominantes, traslación, estacionalidad | `OHLCV-OK` / `OTRAS FUENTES` | **C** |
| 15 | Ordenadores y sistemas | 398–413 | Sistemas mecánicos, ADX/DMI, parabólico SAR, optimización | `OHLCV-OK` | **A** |
| 16 | Gestión monetaria y tácticas | 414–435 | Riesgo por operación, recompensa/riesgo, stops, órdenes, **pivotes intradía** | `OHLCV-OK` | **A** |
| 17 | Análisis entre mercados | 436–453 | Bonos, acciones, materias primas, dólar, fuerza relativa | `OTRAS FUENTES` | **D** |
| 18 | Indicadores bursátiles | 454–475 | Amplitud: A/D, McClellan, máximos/mínimos, TRIN, equivolumen | `OTRAS FUENTES` | **D** |
| 19 | Resumen y lista de comprobación | 476–483 | Integración de todo el aparato; checklist operativa | — | **B** |
| A | Indicadores técnicos avanzados | 484–495 | Índice de demanda, IRH, bandas Cams y canales de Keltner | `OHLCV-OK` / `OTRAS FUENTES` | **C** |
| B | Market Profile | 496–513 | Distribución de precio por tiempo; estructura de subasta | `GRANULAR` | **C** |
| C | Creación de un sistema de contratación | 514–523 | Plan de 5 pasos: concepto → reglas → verificación → prueba → evaluación | — | **A** |
| D | Contratos de futuros continuos | 524–529 | Métodos de empalme: más cercano, siguiente, Gann, plazo constante | `OHLCV-COND` | **A** |

### Resumen del mapa

| Nivel | Capítulos |
|---|---|
| **A — Crítico** | 1, 4, 7, 9, 10, 15, 16, Ap. C, Ap. D |
| **B — Importante** | 2, 3, 5, 6, 8, 12, 19 |
| **C — Complementario** | 11, 13, 14, Ap. A, Ap. B |
| **D — Poco relevante ahora** | 17, 18 |

---

## 1. FILOSOFÍA DEL ANÁLISIS TÉCNICO (Cap. 1 — Nivel A)

### 1.1 Las tres premisas

`[MURPHY]` El enfoque técnico se apoya en tres premisas declaradas:

1. **Los movimientos del mercado lo descuentan todo.**
2. **Los precios se mueven por tendencias.**
3. **La historia se repite.**

### 1.2 Premisa 1 — "El mercado lo descuenta todo"

`[MURPHY]` La formula como piedra angular: cualquier cosa que pueda afectar al precio —fundamental, política, psicológica u otra— **ya se refleja en el precio**. Por tanto basta con estudiar el movimiento del precio.

El argumento explícito que da: los movimientos de precio deberían reflejar cambios de oferta y demanda; si la demanda supera la oferta el precio sube. El técnico **invierte la implicación**: si los precios suben, la demanda debe superar a la oferta y los fundamentos deben ser alcistas. En sus propias palabras, **el técnico estudia los fundamentos de forma indirecta**; los gráficos no mueven los mercados, sólo reflejan la psicología del mercado.

`[MURPHY]` Añade un matiz importante: el precio de mercado **tiende a anticipar los fundamentos conocidos**; los fundamentos ya conocidos están descontados y los precios reaccionan a los desconocidos. Varios de los mayores mercados alcistas y bajistas empezaron con cambios apenas perceptibles en los fundamentos.

**Análisis de la premisa:**

| Dimensión | Valoración |
|---|---|
| **¿Hipótesis empírica, definición o supuesto?** | `[INTERPRETACIÓN]` Es un **supuesto de suficiencia informacional**, no una hipótesis empírica. Afirma que el conjunto informativo relevante está contenido en el precio. No especifica *cómo* se refleja ni con qué retardo, lo que la hace **muy difícil de falsar**: cualquier movimiento inexplicado confirma la premisa (era información desconocida descontándose). |
| **Mecanismo causal propuesto** | Oferta y demanda agregadas, mediadas por la psicología de los participantes. |
| **¿Qué parte es cuantificable?** | La versión falsable sería: *el precio pasado contiene información predictiva sobre el precio futuro por encima de un baseline*. Esa sí es comprobable. |
| **¿Qué parte no lo es?** | La afirmación de que *toda* la información está descontada. Un fallo predictivo nunca refuta la premisa. |

`[IMPLICACIÓN PARA IRIS]` Esta premisa es, curiosamente, **el argumento filosófico que respalda nuestra restricción de datos**: si Murphy tiene razón, un sistema OHLCV-only no está estructuralmente incapacitado. Pero es un argumento, no evidencia, y **no debemos tratarlo como justificación de la decisión** — la decisión es de simplicidad operativa, y su validez sigue siendo una pregunta empírica.

`[INTERPRETACIÓN]` Nótese además la tensión interna: Murphy sostiene simultáneamente que el mercado descuenta todo **y** que el análisis técnico permite anticipar movimientos. Si todo está descontado en el precio actual, el precio actual es el mejor estimador disponible del valor, que es precisamente la conclusión de la hipótesis de mercado eficiente que él rechaza. Su salida es temporal: el precio descuenta **antes** que el conocimiento público. Esa formulación es coherente, pero convierte la premisa en una afirmación sobre **velocidades relativas de incorporación de información**, que es algo bastante más específico y más frágil de lo que el enunciado sugiere.

### 1.3 Premisa 2 — "Los precios se mueven por tendencias"

`[MURPHY]` La declara **absolutamente esencial**: el propósito único de graficar precios es identificar tendencias en etapas tempranas para operar en su dirección. La mayoría de las técnicas del libro son, por naturaleza, **seguidoras de tendencia**: su intención es identificar y seguir tendencias existentes.

`[MURPHY]` El **corolario**, que él mismo presenta como adaptación de la primera ley de Newton: **una tendencia en movimiento tiene más probabilidad de continuar que de retroceder**. Formulación alternativa que él ofrece: una tendencia seguirá en la misma dirección hasta que empiece a volver atrás.

`[MURPHY]` Y una honestidad notable: reconoce explícitamente que esta conclusión **"parece casi circular"**, pero sostiene que todo el enfoque de seguimiento de tendencia se basa en seguirla hasta que muestre señales de revertir.

**Análisis de la premisa:**

| Dimensión | Valoración |
|---|---|
| **Tipo** | `[INTERPRETACIÓN]` La versión débil ("una tendencia continúa hasta que se revierte") es **una tautología**, y Murphy lo admite. La versión fuerte ("una tendencia en movimiento es más probable que continúe que que revierta") **sí es una hipótesis empírica falsable y cuantificable**. |
| **Mecanismo** | Inercia por analogía física. **No aporta mecanismo de mercado en este capítulo**; el mecanismo aparece más tarde y de forma dispersa (memoria de participantes atrapados, ver §4 y §12). |
| **Cuantificable** | **Sí, y es la premisa más cuantificable de las tres.** La forma testeable: autocorrelación positiva de retornos en algún horizonte; o probabilidad condicional de continuación superior a la de reversión dada una definición operativa de tendencia. |
| **Riesgo** | La definición operativa de "tendencia" no es única, y cada definición introduce grados de libertad (ver §4.6). |

`[IMPLICACIÓN PARA IRIS]` Esta es **la única de las tres premisas convertible directamente en una hipótesis experimental sobre MNQ**. Pero ojo: la hipótesis no es "existe tendencia" sino "**dada una definición X de tendencia, la continuación es más probable que la reversión en el horizonte H, con magnitud suficiente para superar costes**". Los tres cuantificadores (X, H, magnitud) son nuestros, no de Murphy.

### 1.4 Premisa 3 — "La historia se repite"

`[MURPHY]` Buena parte del análisis técnico es estudio de psicología humana. Los patrones gráficos clasificados a lo largo de un siglo revelan la psicología alcista o bajista del mercado, y **dado que funcionaron bien en el pasado se asume que seguirán funcionando**, porque se basan en psicología humana que tiende a no cambiar.

**Análisis de la premisa:**

`[INTERPRETACIÓN]` Esta es la premisa **metodológicamente más problemática** de las tres, y conviene decirlo sin rodeos:

1. **La inferencia es explícitamente inductiva sin control**: "funcionó en el pasado → seguirá funcionando". Es exactamente el razonamiento que las dos fuentes anteriores identifican como el mecanismo generador de falsos descubrimientos.
2. **El anclaje en la psicología invariante es la parte no falsable**: si un patrón deja de funcionar, siempre puede argumentarse que el patrón estaba mal identificado, no que la premisa sea falsa.
3. **No hay cuantificación de "funcionó bien"**. No se ofrece tasa de acierto, muestra ni período.

`[VACÍO]` **Murphy nunca define qué significa que un patrón "funcione".** No hay criterio de éxito, ni tasa de acierto, ni comparación contra azar en todo el libro. Este es el vacío más grande de la fuente y condiciona todo lo demás.

`[IMPLICACIÓN PARA IRIS]` La parte utilizable de esta premisa es la **estabilidad temporal como hipótesis a comprobar**, no como supuesto: si un patrón refleja psicología invariante, su capacidad predictiva debería ser estable entre períodos y regímenes. Eso es exactamente comprobable, y es además el análogo temporal de la defensa multiactivo que perdimos en la etapa anterior.

### 1.5 Análisis vs cálculo del tiempo (timing)

`[MURPHY]` Desglosa la decisión en **dos etapas separadas: análisis y cálculo del tiempo (timing)**. Y hace tres afirmaciones relevantes:

1. **Es posible estar en la tendencia correcta y perder dinero igualmente.**
2. En futuros, por el apalancamiento (margen típicamente inferior al 10%), un movimiento pequeño en dirección contraria puede **forzar la salida del operador** con pérdida de todo o gran parte del margen. La estrategia de comprar y mantener **no se aplica a futuros**.
3. En la fase de pronóstico puede usarse tanto lo técnico como lo fundamental, pero **la cuestión del timing —los momentos específicos de entrada y salida— es casi puramente técnica**.

`[IMPLICACIÓN PARA IRIS]` Este pasaje es **una de las conexiones más directas de Murphy con las otras dos fuentes**, y merece registrarse con precisión:
- La afirmación 1 es, en otro vocabulario, **"predicción ≠ rentabilidad"**.
- La afirmación 2 es el racional del stop-loss implícito por margin call, que es exactamente el argumento con el que López de Prado justifica el etiquetado dependiente del camino.
- La separación análisis / timing es una descomposición del problema **distinta pero relacionada** con side / size.

**No se resuelve aquí la relación entre las tres descomposiciones.** Se registra en §40.

### 1.6 Especificidades de futuros que Murphy señala

`[MURPHY]` Diferencias entre el análisis técnico de valores y el de futuros:

| Aspecto | Qué dice |
|---|---|
| **Estructura de precios** | Más compleja en futuros: cada producto cotiza en unidades e incrementos distintos; hay que conocer incremento mínimo y su valor monetario. |
| **Duración limitada** | Los contratos vencen. Vida útil típica de ~18 meses, con media docena de meses contractuales operando simultáneamente. **Crea problemas para previsiones de largo alcance**: los gráficos de contratos vencidos pierden utilidad, y la rotación constante obliga a obtener nuevos datos históricos. |
| **Margen y apalancamiento** | Menos del 10% del valor del contrato. El apalancamiento magnifica movimientos pequeños y **hace que los mercados de futuros parezcan más volátiles de lo que son**. |
| **Horizonte temporal más corto** | Los operadores de futuros quieren saber dónde estarán los precios la semana que viene, mañana **o incluso dentro de unas horas**. Esto ha obligado a afinar las herramientas de timing a muy corto plazo. |
| **Parámetros más cortos** | Ejemplo explícito: en valores las medias más comunes son 50 y 200 días; **en materias primas casi todas están por debajo de 40 días**, con una combinación corriente de 4, 9 y 18 días. |
| **Menos indicadores de opinión y flujo de fondos** | El análisis técnico en futuros es "análisis de precio mucho más puro"; se da más importancia a la tendencia básica y a los indicadores tradicionales. |
| **Los modelos gráficos se completan menos** | `[MURPHY]` En futuros, **los modelos de gráficos tienden con frecuencia a no completarse tanto como en valores**. |

`[IMPLICACIÓN PARA IRIS]` Cuatro observaciones:
1. **Murphy reconoce él mismo que los parámetros no son transferibles entre clases de activo y horizontes.** Esto es una autorización explícita del propio autor para **no** adoptar sus valores de parámetros en MNQ intradiario.
2. La observación de que los patrones se completan menos en futuros es una advertencia del autor **contra su propio catálogo de patrones** aplicado a nuestro tipo de instrumento.
3. La afirmación sobre el apalancamiento que hace parecer más volátiles a los futuros es **conceptualmente incorrecta si se toma literalmente** `[INTERPRETACIÓN]`: el apalancamiento amplifica el resultado del operador, no la volatilidad del precio. La volatilidad del MNQ es una propiedad de la serie, no de nuestro margen.
4. El problema de duración limitada y rotación de contratos es el mismo que trata el Apéndice D y que López de Prado formaliza (ver §17 y §23).

### 1.7 Chartista vs técnico estadístico — y la confesión sobre subjetividad

`[MURPHY]` Distingue dos tipos de profesional:
- El **chartista tradicional**, cuya herramienta principal es el gráfico. Y aquí es explícito: **"por necesidad, la realización de gráficos es algo subjetivo, y el éxito del enfoque depende en general de la habilidad del individuo"**. Lo llama *grafismo artístico* porque la interpretación de gráficos es mayoritariamente un arte.
- El **analista estadístico o cuantitativo**, que toma esos principios subjetivos, **los cuantifica, prueba y optimiza** para desarrollar sistemas mecánicos, con la intención de reducir o eliminar el elemento humano subjetivo.

`[MURPHY]` Y en la respuesta a las críticas es todavía más directo: **"la realidad de la cuestión es que los gráficos son muy subjetivos"**; interpretar gráficos es un arte o habilidad; **los patrones pocas veces son tan claros como para que chartistas experimentados coincidan en su interpretación**; siempre hay un elemento de duda y desacuerdo; y **existen muchos enfoques distintos del análisis técnico que a menudo no concuerdan entre sí**.

`[IMPLICACIÓN PARA IRIS]` **Esta es la admisión más importante del capítulo para nosotros.** El propio autor sitúa la cuantificación de sus conceptos como una tarea distinta de la suya, y reconoce que la versión original es irreproducible entre operadores. Consecuencia directa: **cuando formalicemos un concepto de Murphy no estaremos implementando a Murphy; estaremos creando un objeto nuevo cuya validez es una pregunta abierta independiente.** Esa distinción atraviesa todo este documento y es la razón de separar sistemáticamente `[MURPHY]` de `[INTERPRETACIÓN]`.

### 1.8 Cómo responde Murphy a las críticas

**Profecía autocumplida.** `[MURPHY]` Cita la crítica doble (los patrones son tan conocidos que se autocumplen / los patrones son completamente subjetivos) y señala correctamente que **ambas se contradicen**: si son subjetivos y existen "en la mente de quien los ve", no puede ser que todos vean lo mismo a la vez. Añade que aunque fuera un problema **se autocorregiría**: los operadores ajustarían tácticas o dejarían de usar los gráficos. Y que los mercados alcistas o bajistas sólo se sostienen si los justifica la oferta y la demanda.

`[MURPHY]` Manifiesta más preocupación por **la concentración de capital en sistemas computerizados seguidores de tendencia**, con potencial de distorsionar el precio a corto plazo, aunque estima que esas distorsiones son de corto plazo y se autocorrigen.

`[INTERPRETACIÓN]` Su respuesta a la contradicción es lógicamente válida, pero **resuelve la crítica escogiendo el cuerno subjetivo**, lo que refuerza el problema de reproducibilidad en lugar de disolverlo.

**Uso del pasado para predecir el futuro.** `[MURPHY]` Argumenta que todo método de pronóstico conocido se basa en datos pasados, distingue estadística descriptiva (el gráfico) de inductiva (el análisis), y concluye que el análisis de gráficos es **otra forma de análisis de series temporales**.

`[INTERPRETACIÓN]` El argumento es correcto pero débil: establece que usar el pasado es legítimo, no que **este** uso del pasado tenga capacidad predictiva. Es un argumento de posibilidad, no de evidencia.

**Paseo aleatorio.** `[MURPHY]` La rechaza. Sus argumentos:
- Reconoce que **existe cierta cantidad de aleatoriedad o ruido en todos los mercados**, pero considera irreal que todos los movimientos lo sean.
- Sostiene que en esta área **la observación empírica y la experiencia práctica resultan más útiles que las técnicas estadísticas sofisticadas**, que "parecen capaces de probar cualquier cosa que el usuario tenga en mente".
- Argumenta que **la aleatoriedad sólo puede definirse negativamente**, como incapacidad de descubrir patrones sistemáticos; que los académicos no los hayan descubierto no prueba que no existan.
- Apela a la visibilidad de las tendencias en cualquier libro de gráficos.
- Señala una coincidencia real: **la hipótesis de mercado eficiente está muy cerca de la premisa técnica de que los mercados lo descuentan todo**; la diferencia está en si puede sacarse partido de ello.
- Analogía del electrocardiograma: un proceso parece aleatorio a quien no conoce sus reglas.
- Menciona con esperanza la aparición de las **finanzas conductuales** como disciplina que relaciona psicología y precios.

`[INTERPRETACIÓN]` Aquí conviene ser preciso porque es un punto de fricción metodológica central:
- El punto sobre la **asimetría de la falsación** (no encontrar patrones no prueba que no existan) es **lógicamente correcto**.
- El **rechazo de las técnicas estadísticas** por poder "probar cualquier cosa" es exactamente el argumento inverso al que sostienen las dos fuentes anteriores: para ellas el problema no es que la estadística pruebe demasiado, sino que sin corrección por multiple testing **el investigador** prueba demasiado. Murphy identifica el síntoma correcto y le atribuye la causa opuesta.
- El **argumento visual** ("mire cualquier libro de gráficos") es precisamente el mecanismo de sesgo de selección que las otras fuentes advierten: las tendencias son visibles *a posteriori* en cualquier serie, incluida una generada aleatoriamente.
- **No aporta ninguna prueba estadística** que contradiga el paseo aleatorio.

`[VACÍO]` Murphy **no distingue entre "los precios no son un paseo aleatorio puro" y "existe estructura explotable neta de costes"**. Son afirmaciones muy distintas y sólo la segunda importa a IRIS.

### 1.9 Qué queda de este capítulo para IRIS

`[IMPLICACIÓN PARA IRIS]`

**Utilizable:**
- La premisa 2 como **hipótesis experimental** (persistencia > reversión bajo una definición operativa).
- La premisa 3 como **criterio de estabilidad temporal** a comprobar.
- La separación análisis / timing y el reconocimiento de que se puede acertar la dirección y perder dinero.
- La advertencia sobre no transferir parámetros entre horizontes y clases de activo, hecha por el propio autor.
- La observación de que en futuros los patrones se completan menos.
- La constatación explícita de subjetividad, que fija nuestra tarea: formalizar es crear algo nuevo.

**No utilizable como evidencia:**
- La premisa 1, por no falsable en su forma general.
- El rechazo del paseo aleatorio, por no estar respaldado con datos.
- Cualquier afirmación de que una técnica "funciona".

**Categoría descripción/predicción/operación:** el capítulo entero opera en **(A) descripción** y salta directamente a **(C) regla operativa** mediante la afirmación de que el enfoque técnico es superior. **(B) no se somete a prueba en ningún momento.**


---

## 2. TEORÍA DE DOW (Cap. 2 — Nivel B)

### 2.1 Los seis principios

`[MURPHY]` Presenta la Teoría de Dow como el antecedente del que deriva "gran parte" del análisis técnico moderno:

**1. Las medias lo descuentan todo.** Los mercados reflejan cada factor conocido que afecta a la oferta y la demanda. `[MURPHY]` Incluso los "actos de Dios": los mercados no pueden anticipar terremotos, pero **los descuentan rápidamente y asimilan casi instantáneamente sus efectos**.

**2. El mercado tiene tres tendencias.** Y aquí está **la definición operativa más importante de todo el libro**:

> `[MURPHY]` Una **tendencia ascendente** es una situación en la que cada sucesiva recuperación **cierra** más alto que el nivel alto de la recuperación previa, y cada sucesivo nivel bajo también **cierra** más alto que el nivel bajo previo. En otras palabras: **un patrón de picos y valles cada vez más altos**. La situación opuesta define la tendencia descendente.

`[MURPHY]` Las tres escalas, con la metáfora marea / olas / ondas:
- **Primaria**: duración superior a un año, posiblemente varios.
- **Secundaria o intermedia**: correcciones de la primaria; **de tres semanas a tres meses**; retroceden habitualmente **entre un tercio y dos tercios** del movimiento previo, y **con mayor frecuencia alrededor del 50%**.
- **Menor**: **menos de tres semanas**; fluctuaciones dentro de la intermedia.

**3. Las tendencias principales tienen tres fases**: acumulación (compra informada de los inversores más astutos, cuando el mercado ya asimiló las malas noticias), participación pública (los seguidores de tendencia entran, los precios avanzan rápido y las noticias mejoran) y distribución (prensa progresivamente alcista, noticias económicas mejores que nunca, volumen especulativo y participación pública crecientes, mientras los informados distribuyen).

**4. Las medias deben confirmarse entre ellas.** Ninguna señal importante era válida salvo que **ambas medias (Industrial y Ferrocarriles) dieran la misma señal**. Cuando divergían, se asumía que la tendencia previa seguía vigente. No exigía simultaneidad, pero un intervalo corto daba mayor confirmación.

**5. El volumen debe confirmar la tendencia.** `[MURPHY]` **Volumen como factor secundario pero importante.** La regla: el volumen debería expandirse en la dirección de la tendencia principal — en tendencia ascendente aumenta al subir los precios y disminuye al bajar; en descendente, aumenta al caer y disminuye al subir. **Dow basaba sus señales de compra y venta enteramente en los precios de cierre.**

**6. Se presume que una tendencia está en vigor hasta que da señales definitivas de retroceso.** Analogía newtoniana explícita.

### 2.2 Buenas y malas oscilaciones — la formalización de la reversión

`[MURPHY]` Reconoce que **la tarea más difícil es distinguir una corrección secundaria normal del primer tramo de una nueva tendencia opuesta**, y que **los seguidores de Dow frecuentemente están en desacuerdo** sobre cuándo hay una señal genuina de retroceso.

Describe dos configuraciones (verificadas en las figuras 2.3a y 2.3b del libro):

- **Mala oscilación**: el rebote en C **no supera** el pico previo A, y después el precio perfora el mínimo B. Dos picos más bajos y dos valles más bajos → señal de venta clara en la ruptura de B.
- **Buena oscilación**: el rebote en C **sí supera** A, y luego el precio perfora B. `[MURPHY]` **Aquí los seguidores de Dow discrepan**: algunos venden en la ruptura de B (S1), otros exigen ver antes un máximo más bajo en E y un nuevo mínimo bajo D (S2), porque quieren dos máximos más bajos *y* dos mínimos más bajos.

`[IMPLICACIÓN PARA IRIS]` Este pasaje es más valioso de lo que parece porque **muestra exactamente dónde se rompe la objetividad**. La definición de tendencia por secuencia HH/HL es objetiva; **la regla de cambio de tendencia no lo es**, y el propio Murphy documenta que dos operadores competentes producirían señales distintas en el mismo gráfico. Si formalizamos esto, estaremos eligiendo entre S1 y S2 —una decisión con consecuencias operativas grandes— y **esa elección es nuestra, no de Murphy**. Es un grado de libertad que debe contabilizarse.

`[MURPHY]` Precisión adicional relevante: **Dow no consideraba válidas las penetraciones intradía**; exigía cierre por encima del pico previo o por debajo del valle previo.

`[IMPLICACIÓN PARA IRIS]` Aparece aquí, y por primera vez en el libro, una decisión de formalización que reaparecerá constantemente: **¿cierre o extremo?** Murphy/Dow toman posición explícita a favor del **cierre**. Es exactamente la misma disyuntiva que dejamos abierta en la Knowledge Base 02 sobre comprobar barreras contra cierres o contra High/Low. **No se resuelve aquí**; se registra que Murphy aporta un argumento (la penetración intradía no cuenta) que no está respaldado por evidencia pero sí es una convención coherente.

### 2.3 La única cifra empírica del capítulo

`[MURPHY]` Reconoce la crítica de que **la Teoría de Dow pierde de media entre un 20% y un 25% de un movimiento antes de generar señal**, y que la señal de compra aparece típicamente en la segunda fase. Añade que **ahí es también donde casi todos los sistemas técnicos de seguimiento de tendencias empiezan a identificar y participar en las tendencias existentes**.

Y aporta el único dato cuantitativo del capítulo, atribuido a *Barron's*: **de 1920 a 1975, las señales de la Teoría de Dow capturaron el 68% de los movimientos de los promedios industriales y de transportes, y el 67% del S&P 500**.

`[INTERPRETACIÓN]` Conviene leer esta cifra con precisión: **"capturar el 68% del movimiento" no es una tasa de acierto ni un rendimiento neto**. No dice cuántas señales falsas hubo, ni cuál fue el resultado económico, ni si sobrevive a costes. Es una métrica de captura de tendencia sobre un período de 55 años en índices bursátiles. **No es evidencia transferible a MNQ intradiario en ningún sentido.**

`[IMPLICACIÓN PARA IRIS]` Lo que sí es transferible es **el reconocimiento estructural del retardo**: un sistema seguidor de tendencia sacrifica por diseño el primer 20-25% del movimiento. Esto tiene una consecuencia directa sobre la viabilidad económica que las otras fuentes permiten calcular: si el edge por operación es pequeño y el retardo estructural consume un cuarto del movimiento, **el marco de riesgo de estrategia de López de Prado nos diría si eso deja algo utilizable**. No lo calculamos aquí.

### 2.4 Clasificación y aplicabilidad

| Principio | Datos | Formalizable | Causal | Clasificación |
|---|---|---|---|---|
| Las medias lo descuentan todo | — | No (no falsable) | — | `NO RELEVANTE` como técnica |
| **Definición de tendencia por HH/HL sobre cierres** | Cierres | **Sí, alta** | `LOOK-AHEAD-LEVE` (requiere identificar picos y valles, ver §4.3) | **`OHLCV-OK`** |
| Tres escalas temporales | Cierres | Sí (multi-horizonte) | `CAUSAL` | **`OHLCV-OK`** |
| Retroceso de 1/3 a 2/3, típicamente 50% | Cierres | Sí | `LOOK-AHEAD-LEVE` (requiere el extremo del movimiento previo) | **`OHLCV-OK`** |
| Tres fases (acumulación/participación/distribución) | — | **No** | `LOOK-AHEAD-GRAVE` | **`NO RELEVANTE`** — sólo identificable a posteriori |
| **Confirmación entre medias** | Dos índices | Sí | `CAUSAL` | **`OTRAS FUENTES`** |
| Volumen confirma la tendencia | OHLCV | Sí | `CAUSAL` | **`OHLCV-OK`** |
| Tendencia vigente hasta señal de retroceso | Cierres | Sí, con la ambigüedad S1/S2 | `CAUSAL-CONF` | **`OHLCV-OK`** |

`[IMPLICACIÓN PARA IRIS]` **El principio 4 (confirmación entre medias) requiere múltiples instrumentos y queda fuera de alcance**, conforme a la instrucción de no ampliar el proyecto. Conviene notar qué se renuncia: la idea de exigir que dos series relacionadas coincidan es un **mecanismo de reducción de falsos positivos** conceptualmente atractivo. Se documenta como renuncia, no como recomendación de ampliar.

`[INTERPRETACIÓN]` Las fases de mercado son el ejemplo más nítido del libro de **reconocimiento retrospectivo puro**: la fase de distribución sólo se sabe que era distribución cuando el mercado ya cayó. Formalizarlas causalmente equivaldría a resolver el problema predictivo entero, que es lo que se pretendía usar la fase para resolver. Circular.

---

## 3. CONSTRUCCIÓN DE GRÁFICOS (Cap. 3 — Nivel B)

### 3.1 Los cuatro tipos de gráfico y qué información conserva cada uno

`[MURPHY]`

| Tipo | Información usada | Qué descarta |
|---|---|---|
| **Línea** | Sólo cierres | Apertura, máximo, mínimo, y toda la estructura intrabar |
| **Barras** (el más usado) | O, H, L, C | La secuencia intrabar |
| **Velas** | Los mismos cuatro precios; presentación distinta | Idem; **la clave está en la relación entre apertura y cierre** |
| **Puntos y figuras** | Sólo movimientos de precio, **sin eje temporal** | El tiempo por completo |

`[MURPHY]` Sobre las velas hace dos observaciones útiles: registran exactamente los mismos cuatro precios que las barras, y **todas las herramientas e indicadores válidos para barras lo son también para velas**. Es decir, **el gráfico de velas no aporta información nueva; aporta una codificación visual distinta de la misma información**.

`[IMPLICACIÓN PARA IRIS]` Esta observación del propio autor es decisiva para el capítulo 12 y merece registrarse ahora: **si las velas contienen exactamente los mismos datos que las barras, cualquier información que aporte un patrón de velas es una función de OHLC** — y por tanto potencialmente representable como variable continua sin recurrir a categorías nominales. Se desarrolla en §12.

### 3.2 Escala aritmética vs logarítmica

`[MURPHY]` En escala aritmética la distancia vertical es igual para cada unidad de cambio de precio; en logarítmica, **distancias iguales representan cambios porcentuales iguales**. Un movimiento de 10 a 20 (100%) ocupa la misma distancia que de 20 a 40 o de 40 a 80. Señala que **los servicios bursátiles suelen usar escala logarítmica y los de futuros escala aritmética**, y que en su ejemplo la línea de tendencia de tres años **funcionó mejor en el gráfico logarítmico**.

`[IMPLICACIÓN PARA IRIS]` `OHLCV-OK`. La consecuencia práctica es que **cualquier objeto geométrico (línea de tendencia, canal, pendiente) depende de la escala en que se trace**. Una recta en escala logarítmica es una exponencial en aritmética. Si formalizamos pendientes o líneas, **la elección log/aritmética es un grado de libertad que Murphy señala pero no resuelve** — y en intradiario, donde el rango de precios dentro de una sesión es estrecho, la diferencia probablemente sea pequeña, aunque eso es una conjetura a verificar, no un hecho del libro.

### 3.3 Volumen

`[MURPHY]` **El volumen representa la suma total de operaciones de un mercado en un día**: la cantidad total de contratos de futuros negociados, o el número de acciones que cambian de manos.

`[IMPLICACIÓN PARA IRIS]` **`OHLCV-OK`**, y es exactamente lo que tenemos. Registrar la definición importa porque delimita: es una **magnitud agregada sin dirección**. No informa de quién fue agresor, ni de cuánto se ejecutó al bid o al ask. Toda la sección §15 depende de esta limitación.

### 3.4 Interés abierto — y por qué queda fuera

`[MURPHY]` El interés abierto es la cantidad de contratos de futuros en circulación. Cuatro observaciones que hace:

1. **Se usan las cifras totales, no las del mes individual.** Razón: en las primeras etapas de vigencia de un contrato, volumen e interés abierto son pequeños, aumentan al acercarse el vencimiento, y **un par de meses antes vuelven a disminuir** porque los operadores liquidan. **Ese incremento inicial y declive final no tienen nada que ver con la dirección del mercado: son una función de la duración limitada del contrato.**
2. **Volumen e interés abierto se informan con un día de retraso** en futuros; sólo hay estimaciones de volumen el mismo día. Los chartistas de valores no tienen ese problema.
3. El interés abierto **individual** sí es valioso para una cosa: **indica qué contratos son los más líquidos**. Regla que da: operar sólo en los meses de entrega con mayor interés abierto y evitar los de cifras bajas.
4. Los gráficos de valores reflejan volumen total pero **no incluyen interés abierto**.

**Clasificación: `OTRAS FUENTES`.** No forma parte de `Timestamp + OHLCV`. **No se propone incorporarlo.**

`[IMPLICACIÓN PARA IRIS]` Tres observaciones que sí son aprovechables sin el dato:
- La observación 1 es **exactamente el fenómeno de contaminación por ciclo de contrato** que hay que neutralizar en la construcción de la serie continua de MNQ. Murphy la describe para interés abierto; el mismo mecanismo afecta al **volumen**, que sí tenemos: el volumen de un contrato individual crece y decae por razones de calendario, no de mercado.
- La observación 3 define un criterio de selección de contrato (**el más líquido**) que es relevante para nuestro método de roll y que **podemos aproximar con el volumen** aunque no tengamos interés abierto.
- La observación 2 (retardo de un día) es una advertencia de **causalidad de datos** que no nos afecta con OHLCV, pero ilustra que Murphy es consciente de la disponibilidad temporal de la información.

`[VACÍO]` Murphy **no discute en ningún momento la contaminación del volumen durante la transición de contratos**, que es un problema real para IRIS si el histórico se construye empalmando contratos. Sólo lo trata para interés abierto.

### 3.5 Multi-escala: el gráfico de barras es indiferente al período

`[MURPHY]` Afirmación explícita y directamente relevante: **puede confeccionarse un gráfico de barras para cualquier período**. El gráfico de barras intradía **mide máximos, mínimos y últimos precios de períodos tan cortos como cinco minutos**. El diario común cubre de seis a nueve meses; para tendencias de mayor alcance se recurre a semanales (≈5 años) y mensuales, y **el método de construcción y actualización es esencialmente el mismo**.

`[IMPLICACIÓN PARA IRIS]` Es la afirmación que Murphy hace más cercana a autorizar la aplicación intradiaria de su aparato. Pero conviene ser exacto sobre su alcance: **afirma que el gráfico se construye igual, no que las técnicas conserven capacidad predictiva a esa escala.** Es una afirmación sobre la representación, no sobre la señal. `[VACÍO]` **La transferencia de las técnicas a barras de un minuto no está demostrada en ningún punto del libro.**


---

## 4. TENDENCIA, SOPORTES Y RESISTENCIAS (Cap. 4 — Nivel A)

Bloque prioritario. Es el capítulo con mayor densidad de material formalizable de todo el libro.

### 4.1 Definición y direcciones

`[MURPHY]` La definición operativa, heredada de Dow:
- **Tendencia ascendente**: patrón de **picos y valles cada vez más altos**.
- **Tendencia descendente**: picos y valles cada vez más bajos.
- **Tendencia lateral**: los precios se mueven en una línea horizontal, la *banda de fluctuación*, que refleja **un período de equilibrio donde oferta y demanda están en relativa igualdad**.

`[MURPHY]` Y una precisión terminológica que él mismo hace: aunque define el mercado plano como tendencia lateral, **es más frecuente decir que no tiene ninguna tendencia**.

`[MURPHY]` **La advertencia operativa más importante del capítulo**, y aparece de inmediato:

> Las herramientas y sistemas técnicos **siguen tendencias por naturaleza**. Cuando los mercados están en fases laterales, **esas herramientas funcionan poco o mal**. Durante esos períodos los operadores técnicos experimentan **sus mayores frustraciones** y los operadores de sistemas **sufren sus mayores pérdidas**. El fallo no está en el sistema, sino en aplicar un sistema pensado para mercados con tendencia a un mercado que no la tiene.

`[MURPHY]` Y la formulación explícita de las tres decisiones: **comprar, vender, o no hacer nada (apartarse)**. Cuando el mercado sube, comprar; cuando baja, vender; **cuando se mueve lateralmente, mantenerse fuera del mercado es generalmente lo más sensato**.

`[IMPLICACIÓN PARA IRIS]` Esto es **notable y hay que registrarlo con precisión**: Murphy formula explícitamente un espacio de tres decisiones LONG / SHORT / NO OPERAR, y ofrece **un criterio para la abstención que es una variable de estado del mercado, no una medida de confianza del modelo**. Es una vía conceptualmente distinta de las tres que ofrecía López de Prado (meta-etiqueta 0, tamaño≈0 por baja confianza, discretización): aquí **la abstención se deriva del régimen**, no de la señal.

**No se resuelve la tensión** entre ambas concepciones. Se registra en §40 como material para la síntesis.

### 4.2 Las tres escalas y la ambigüedad de sus fronteras

`[MURPHY]`
- **Principal**: Dow la fijaba en más de un año. **Murphy la acorta explícitamente a "cualquier período mayor de seis meses" en mercados de productos**, razonando que los operadores de futuros trabajan con dimensión temporal más corta.
- **Intermedia o secundaria**: de tres semanas a varios meses.
- **Corta duración**: menos de dos o tres semanas.

`[MURPHY]` Y tres observaciones de gran valor metodológico:

1. **"En realidad, hay un número casi infinito de tendencias que interactúan, desde las de muy corta duración que cubren minutos y horas hasta las larguísimas que pueden durar 50 o 100 años."**
2. **"Existe una cierta ambigüedad con respecto a la definición de cada tendencia que hacen los distintos analistas."**
3. **Cada tendencia es parte de la tendencia mayor siguiente y está formada por tendencias menores.** Estructura recursiva. En un punto dado, la principal puede ser ascendente y la intermedia y corta descendentes.

`[MURPHY]` Y la observación que más directamente nos concierne:

> **"Para los operadores de posiciones largas, los movimientos de precios que duran desde unos pocos días hasta unas pocas semanas pueden ser insignificantes. Para un operador de posiciones a un día, un avance de dos o tres días puede representar una tendencia principal."**

`[IMPLICACIÓN PARA IRIS]` Tres consecuencias:
1. **La tendencia no es una propiedad del mercado sino una propiedad del par (mercado, escala).** Preguntar "¿cuál es la tendencia del MNQ?" está mal formulado sin especificar escala. Esto convierte el análisis multi-horizonte en algo estructural, no opcional.
2. **La clasificación en tres es una convención, no una propiedad**. El propio autor lo dice: hay un continuo. Cualquier discretización en tres escalas que hagamos es un grado de libertad nuestro.
3. **Los umbrales concretos (6 meses, 3 semanas) son de Murphy para futuros diarios y no tienen ninguna base para MNQ intradiario.** El propio autor los ajusta al pasar de valores a futuros, lo que ilustra que son convencionales.

`[MURPHY]` Añade una generalización operativa útil: **casi todos los enfoques seguidores de tendencia se centran en la intermedia**, y **la de corta duración se usa básicamente por cuestiones de timing** — en una tendencia intermedia ascendente, los retrocesos de corto plazo se usan para iniciar posiciones largas.

`[INTERPRETACIÓN]` Esta es una arquitectura de dos escalas con roles asimétricos: **una escala define la dirección, otra define el momento de entrada.** Es formalizable y es distinta de "usar muchas ventanas como features". Se registra como posibilidad conceptual sin adoptarla.

### 4.3 Soporte y resistencia: definición

`[MURPHY]`
- **Apoyo (soporte)**: un nivel o área **por debajo del mercado** donde el interés comprador es suficientemente fuerte como para vencer la presión vendedora; la bajada se detiene y los precios vuelven a subir. **Se identifica de antemano por un mínimo de reacción previo.**
- **Resistencia**: nivel o área **por encima del mercado** donde la presión vendedora vence a la compradora. **Se identifica por un pico anterior.**

`[MURPHY]` La conexión con tendencia es explícita y estructural: **para que una tendencia ascendente continúe, cada mínimo sucesivo (nivel de apoyo) debe ser más alto que el anterior**. Si la bajada correctiva alcanza el mínimo previo, es advertencia anticipada de que la tendencia está terminando o pasando a lateral. Si se viola el apoyo, es probable un cambio completo de tendencia.

`[MURPHY]` Y la formulación del primer aviso: **la imposibilidad de superar un pico anterior en tendencia ascendente, o la capacidad de los precios de perforar el mínimo de apoyo anterior en tendencia descendente, es generalmente la primera advertencia de que la tendencia está cambiando.**

`[INTERPRETACIÓN]` **Soporte/resistencia y tendencia son el mismo objeto descrito dos veces.** La secuencia HH/HL *es* la secuencia de resistencias y soportes crecientes. Esto importa para el problema de redundancia de features (§36): una feature de "estructura de tendencia" y una feature de "distancia al soporte" no son informaciones independientes, son transformaciones de la misma estructura de pivotes.

### 4.4 La psicología del soporte y la resistencia — el mecanismo económico

Esta es, en mi lectura, **la aportación conceptual más valiosa de Murphy para IRIS**, porque es lo que las dos fuentes anteriores no podían aportar: un mecanismo causal explícito.

`[MURPHY]` Divide a los participantes en tres grupos: **posiciones largas, posiciones cortas, y no comprometidos** (subdivididos en quienes nunca tuvieron posición y quienes liquidaron prematuramente).

El argumento, tras un movimiento al alza desde una zona de apoyo:
- **Los largos** están satisfechos pero **lamentan no haber comprado más**; si el precio volviera al apoyo, añadirían.
- **Los cortos** se dan cuenta de que están en el lado equivocado y **esperan una bajada hasta su punto de entrada para salir en su umbral de rentabilidad**.
- **Los que liquidaron prematuramente** están enfadados consigo mismos y **buscan reinstalar posiciones cerca de donde vendieron**.
- **Los indecisos** ven que los precios suben y **resuelven entrar largos en la primera buena oportunidad**.

> `[MURPHY]` **"Los cuatro grupos están decididos a comprar en la próxima bajada. Todos tienen un interés personal en esa área de apoyo."**

`[MURPHY]` **Los tres determinantes de la importancia de un nivel**, formulados explícitamente:

| Determinante | Formulación de Murphy |
|---|---|
| **Tiempo** | Cuanto más tiempo opere el precio en un área, más significativa. Tres semanas de congestión > tres días. |
| **Volumen** | Si el nivel se formó con fuerte volumen, muchas unidades cambiaron de manos y el nivel es más importante. |
| **Cercanía temporal** | **Cuanto más reciente sea la actividad, más potente.** Razón: estamos considerando la reacción de operadores a posiciones que ya tomaron o no pudieron tomar. |

`[MURPHY]` **El cambio de polaridad y su mecanismo:** si los precios caen por debajo del apoyo previo, **todos los que compraron ahí se dan cuenta de su error**. Y añade el detalle específico de futuros: **los corredores piden frenéticamente más dinero al margen; dada la naturaleza apalancada, los operadores no pueden mantener las pérdidas mucho tiempo y deben aportar margen adicional o liquidar**.

> `[MURPHY]` **"Lo que creó el apoyo previo fue la predominancia de órdenes de compra por debajo del mercado. Ahora todas las órdenes previas de compra por debajo del mercado se han transformado en órdenes de venta por encima del mercado. El apoyo ahora es resistencia."**

`[MURPHY]` Y cierra con una declaración metodológica notable: los patrones funcionan **no porque las líneas sean mágicas**, sino porque **proporcionan imágenes de lo que están haciendo los participantes**. Lamenta que la terminología abreviada de los gráficos "pase por alto las fuerzas básicas que dieron lugar a las imágenes".

`[IMPLICACIÓN PARA IRIS]` **Esto es exactamente el tipo de mecanismo que la estación de estrategas de López de Prado exige: identificar quién está al otro lado y qué lo obliga a actuar.** Y tiene tres propiedades que lo hacen especialmente relevante para nosotros:

1. **No requiere universo multiactivo.** Es un mecanismo de un solo instrumento.
2. **Es específicamente más fuerte en futuros apalancados**, por el margin call — que es exactamente MNQ.
3. **Es el mismo mecanismo que López de Prado invoca para las rupturas estructurales** (participantes atrapados en el lado perdedor que actúan irracionalmente antes de ser forzados a salir). **Convergencia entre dos fuentes independientes sobre el mismo mecanismo.** No la resolvemos aquí; se registra en §40.

`[INTERPRETACIÓN]` La versión falsable del mecanismo sería: *el precio muestra comportamiento anómalo (reversión, aceleración, expansión de volumen) al aproximarse a niveles donde previamente hubo concentración de actividad, y ese efecto decae con el tiempo transcurrido.* Los tres determinantes de Murphy (tiempo, volumen, recencia) son **directamente parametrizables desde OHLCV** y dan una hipótesis comprobable. Pero es una formalización nuestra.

### 4.5 El grado de penetración — donde aparece la subjetividad

`[MURPHY]` **Reconocimiento explícito**: "es bastante subjetivo determinar el grado de significación de una penetración". Como referencia:
- **Algunos chartistas usan un 3% de penetración**, especialmente para niveles importantes.
- **Áreas de más corto plazo probablemente necesitarían un porcentaje mucho menor, tal vez un 1%.**
- **"En realidad, cada analista debe decidir por sí mismo qué constituye una penetración significativa."**

Y el racional: las áreas cambian de papel **sólo cuando el mercado se aleja lo suficiente como para convencer a los operadores de que han cometido un error. Cuanto más se aleje, más convencidos quedarán.**

`[IMPLICACIÓN PARA IRIS]` El umbral de penetración es **un parámetro libre reconocido como tal por el propio autor**, cuyo valor depende de la escala. En MNQ intradiario no tenemos ninguna base en Murphy para elegirlo. Cada valor probado será un intento a efectos de multiple testing. `[INTERPRETACIÓN]` Una formalización defendible sería **escalarlo por volatilidad** en lugar de por porcentaje fijo, lo que reduciría el parámetro a un multiplicador adimensional — pero eso es una idea nuestra, no de Murphy.

### 4.6 Números redondos

`[MURPHY]` Los números redondos **tienden a detener subidas y bajadas**; los operadores piensan en ellos como objetivos de precio y actúan en consecuencia, por lo que actúan como niveles "psicológicos". Ejemplos que da: el oro en 300, 400 y 500 dólares en distintos episodios; el Dow atascándose en múltiplos de 1000.

`[MURPHY]` **La aplicación táctica**: evitar colocar órdenes justo en números redondos. Comprar con órdenes limitadas **justo por encima** de un número redondo importante (porque otros intentarán comprar en el número y el mercado puede no alcanzarlo); vender **justo por debajo**. Y para stops, la regla inversa: **stops de posiciones largas por debajo de números redondos y de cortas por encima**.

**Clasificación: `OHLCV-OK`. Causalidad: `CAUSAL`.** Es de los pocos conceptos del libro con **cero grados de libertad de detección** (un número redondo es un número redondo) — aunque cuál nivel de redondez importa (¿múltiplos de 10, 50, 100?) sí es un parámetro.

`[IMPLICACIÓN PARA IRIS]` Conceptualmente atractivo por su objetividad, con dos reservas: (a) los ejemplos de Murphy son de niveles absolutos en índices y materias primas a escala de años, **no de niveles intradiarios**; (b) `[VACÍO]` no aporta ninguna evidencia, sólo anécdotas seleccionadas.

### 4.7 Líneas de tendencia

`[MURPHY]` **Construcción**: una línea de tendencia ascendente es una recta inclinada hacia arriba y a la derecha que sigue **mínimos sucesivos de reacción**; la descendente sigue **picos sucesivos**.

**El procedimiento exacto y sus condiciones:**
1. **Tiene que haber evidencia de tendencia.** Para trazar una línea ascendente hacen falta **al menos dos mínimos de reacción, y el segundo más alto que el primero**.
2. `[MURPHY]` **"El chartista sólo puede estar razonablemente seguro de que se ha formado un mínimo de reacción después de que los precios hayan comenzado a subir a partir del punto 3."**
3. **Línea orientativa vs válida**: con dos puntos se traza una línea *orientativa*; **para confirmar su validez debe ser tocada una tercera vez** por precios que reboten desde ella. **"Se necesitan dos puntos para trazar la línea y un tercero para transformarla en válida."**

`[MURPHY]` **Y documenta la discrepancia entre practicantes** sobre cuándo puede trazarse: algunos exigen que el pico intermedio sea penetrado antes de dibujarla; **otros sólo necesitan seguir el 50% de la onda, o que los precios se aproximen al máximo previo**. Textualmente: **"Los criterios pueden diferir."**

**El punto crítico de causalidad.** `[INTERPRETACIÓN]` Aquí está el problema central de formalización de todo el capítulo, y Murphy lo enuncia sin darse cuenta de sus consecuencias:

> **Un mínimo de reacción sólo se sabe que era un mínimo cuando el precio ya ha subido desde él.**

Esto significa que:
- **Identificar un pivote requiere `k` barras de confirmación posteriores.** Con `k` barras de confirmación, el pivote en `t` sólo es conocible en `t+k`.
- Una línea de tendencia trazada sobre pivotes **no es utilizable en el instante en que se formaron los pivotes**, sino `k` barras después.
- **Si `k` no se declara y se fija explícitamente, cualquier backtest de líneas de tendencia tiene look-ahead**, porque el pivote se selecciona sabiendo lo que pasó después.

**Clasificación: `LOOK-AHEAD-LEVE`.** Es formalizable causalmente **sólo declarando `k` explícitamente y aceptando el retardo**. La formalización es posible; la versión ingenua no lo es.

`[IMPLICACIÓN PARA IRIS]` **Este mismo problema afecta a todo lo que dependa de pivotes**: definición de tendencia por HH/HL, soportes y resistencias, canales, retrocesos porcentuales, líneas de velocidad, divergencias, patrones chartistas y ondas de Elliott. **Es el único problema de causalidad más importante de todo el libro**, y conviene tenerlo presente en cada sección posterior.

### 4.8 Grados de libertad de una línea de tendencia

`[INTERPRETACIÓN]` Enumerados explícitamente, porque el libro no lo hace:

| Grado de libertad | Origen |
|---|---|
| `k` = barras de confirmación de pivote | No especificado por Murphy |
| Umbral mínimo de amplitud para que un pivote cuente | No especificado |
| ¿Sobre cierres o sobre extremos? | Dow decía cierres; Murphy dibuja bajo mínimos |
| ¿Escala aritmética o logarítmica? | Murphy señala que importa (§3.2) |
| ¿Dos puntos u obligar a tres? | Murphy: dos orienta, tres valida |
| Cuántos pivotes atrás mirar | No especificado |
| Filtro de ruptura (% o tiempo) | Ver §4.9 |

**Siete grados de libertad como mínimo, ninguno fijado por la fuente.** `[IMPLICACIÓN PARA IRIS]` Formalizar "línea de tendencia" **no es implementar a Murphy**: es elegir un punto en un espacio de siete dimensiones que Murphy dejó abierto. Cada elección es un intento experimental.

### 4.9 Filtros de ruptura

`[MURPHY]` Distingue dos tipos:
- **Filtro de precio**: exigir una penetración de cierto porcentaje. Da el ejemplo del 3% para tendencias importantes y sugiere que **un 1% sería más útil para operaciones de más corta duración**. Menciona que los chartistas de valores pedirían **un punto entero**.
- **Filtro de tiempo**: **la regla de dos días** — los precios deben cerrar más allá de la línea **durante dos días sucesivos**; la violación de un solo día no cuenta. Menciona también una variante que exige que **el cierre de un viernes** esté más allá del punto de ruptura para una señal semanal.

`[MURPHY]` **Y formula explícitamente el compromiso**, que merece registrarse porque es un razonamiento correcto y transferible:

> **"Si el filtro es demasiado pequeño, no será muy útil para reducir el impacto de las malas señales (*whipsaws*). Si es demasiado grande, gran parte del movimiento inicial pasará desapercibido antes de que se reciba una buena señal."**

`[IMPLICACIÓN PARA IRIS]` Es la misma estructura de compromiso que rige la elección del umbral en el filtro CUSUM y la anchura de barreras: **sensibilidad frente a falsas señales**. Murphy identifica correctamente el trade-off y **no ofrece criterio para resolverlo**. `[VACÍO]`

### 4.10 Cambio de papel de las líneas de tendencia

`[MURPHY]` El mismo principio de polaridad: una línea de tendencia ascendente rota **se transforma en resistencia**; una descendente rota, en apoyo. Recomienda **proyectar todas las líneas de tendencia lo más a la derecha posible del gráfico, incluso después de rotas**, porque "resulta sorprendente la frecuencia con la que viejas líneas vuelven a actuar en el papel opuesto".

**Regla de medición.** `[MURPHY]` Una vez rota una línea, los precios generalmente se separan de ella **una distancia igual a la distancia vertical máxima que alcanzaron al otro lado antes de la ruptura**. Y señala que esto es similar a la regla de medición del patrón de cabeza y hombros.

`[INTERPRETACIÓN]` Esta regla de medición es **una simetría postulada sin justificación**. No hay mecanismo psicológico que la respalde en el texto, a diferencia del cambio de polaridad, que sí lo tiene. Categoría: **(B) hipótesis predictiva sin evidencia**.

### 4.11 Principio abanico, inclinación y líneas internas

`[MURPHY]`
- **Principio abanico**: tras romperse la primera línea, el precio rebota y se traza una segunda, más plana; rota ésta, una tercera. **La rotura de la tercera línea es la señal válida de cambio de tendencia.** Las líneas rotas 1 y 2 suelen funcionar en el papel opuesto.
- **La importancia del número tres**: `[MURPHY]` dedica una sección a observar cuántas veces aparece el número tres en el análisis técnico (tres líneas del abanico, tres fases, tres tipos de gaps, tres picos en cabeza y hombros, tres clasificaciones de tendencia, tres direcciones, tres tipos de triángulo, tres fuentes de información: precio, volumen e interés abierto). Y concluye: **"Cualquiera que sea la razón, el número tres juega un papel muy prominente."**
- **Inclinación**: la mayoría de líneas de tendencia al alza **tiende a aproximarse a una inclinación media de 45 grados**; algunos chartistas trazan directamente una línea de 45° desde un extremo destacado. Era técnica favorita de W. D. Gann. Refleja una situación donde **precio y tiempo están en perfecto equilibrio**. Demasiado inclinada → avance insostenible; demasiado plana → tendencia débil que no genera confianza.
- **Líneas internas**: se trazan **atravesando el movimiento del precio**, conectando tantos máximos y mínimos como sea posible, en lugar de por debajo o por encima.

`[INTERPRETACIÓN]` Tres observaciones críticas:

1. **La "importancia del número tres" no es un hallazgo, es una observación sobre convenciones de la disciplina.** Murphy mismo dice "cualquiera que sea la razón". No aporta mecanismo. Es un ejemplo claro de patrón percibido en el propio vocabulario, no en el mercado.
2. **La inclinación de 45 grados no es una propiedad del mercado: depende enteramente de la escala del gráfico.** Un ángulo sobre un gráfico requiere fijar la relación entre unidades de precio y unidades de tiempo en el eje, que es arbitraria. **Esto hace que el concepto no sea invariante y por tanto no formalizable de manera reproducible sin fijar convenciones adicionales.** `[VACÍO]` Murphy no aborda esta objeción. `[INTERPRETACIÓN]` La versión invariante sería **pendiente normalizada por volatilidad**, que sí es adimensional y sí es formalizable — pero es una reconstrucción nuestra, no la idea de Gann ni de Murphy.
3. **Las líneas internas maximizan explícitamente el ajuste a datos pasados** ("conectando tantos máximos y mínimos como sea posible"). Es una descripción de ajuste retrospectivo. **Riesgo de look-ahead alto y grados de libertad no acotados.**

### 4.12 Canales

`[MURPHY]` **Construcción**: trazada la línea de tendencia básica sobre los mínimos, se dibuja una **paralela desde el primer pico prominente**. Si la siguiente subida alcanza la línea de canal y rebota, probablemente existe un canal; si luego el precio vuelve a la línea básica, **es casi seguro**.

**Interpretaciones que ofrece:**
- La línea básica sirve para iniciar largos; la de canal para **realizar beneficios a corto plazo**. Operar contra la tendencia desde la línea superior es "una táctica peligrosa y generalmente costosa".
- **Cuanto más tiempo permanezca intacto el canal y más veces se ponga a prueba, más importante y seguro.**
- **Asimetría importante**: romper la línea de tendencia básica indica **cambio de tendencia**; romper la línea de canal (superior, en alza) indica **aceleración de la tendencia actual**. Significados opuestos.
- **Fracaso en alcanzar la línea de canal**: `[MURPHY]` "como regla empírica, cuando un movimiento no puede alcanzar el otro lado del canal, generalmente es porque la tendencia está cambiando, lo que incrementa la posibilidad de que el otro lado se rompa". Es una **señal anticipada**.
- **Regla de medición**: rota una línea del canal, los precios se desplazan **una distancia igual al ancho del canal**.
- **Jerarquía explícita**: "de las dos líneas, la línea de tendencia básica es de largo la más importante y la más confiable. La línea de canal es un uso secundario."

`[IMPLICACIÓN PARA IRIS]` **El "fracaso en alcanzar el otro lado del canal" es conceptualmente interesante** porque es una señal de debilitamiento que no requiere que ocurra nada — se define por lo que *no* pasó. `[INTERPRETACIÓN]` Formalizado sin canal, equivale a: **la amplitud del último impulso es menor que la del anterior**, que es una medida continua, causal (con el retardo de pivote) y sin necesidad de trazar rectas. Registrar la idea sin la geometría es probablemente más robusto. Es reconstrucción nuestra.

`[INTERPRETACIÓN]` Hay además una **tensión interna**: Murphy describe que los chartistas **redibujan la línea básica** para hacerla paralela a la nueva línea de canal cuando la tendencia se acelera, y también cuando se debilita (figuras 4.18 y 4.19). Es decir, **la línea se ajusta a posteriori a lo que el precio ya hizo**. Eso es un procedimiento de ajuste continuo a los datos, no una regla predictiva fija. Documentado como tensión.

### 4.13 Retrocesos porcentuales

`[MURPHY]` **Los parámetros**:
- **Retroceso mínimo: un tercio (33%).**
- **Retroceso típico: la mitad (50%).**
- **Retroceso máximo: dos tercios (66%)** — "un área que se vuelve especialmente crítica".

`[MURPHY]` **La regla operativa**: para que se mantenga la tendencia anterior, **la corrección debe detenerse en el punto de los dos tercios**, que se convierte en área de compra de riesgo relativamente bajo. **Si los precios exceden los dos tercios, hay más posibilidades de cambio de tendencia que de simple retroceso**, y el movimiento generalmente vuelve atrás el 100%.

`[MURPHY]` **Reconciliación con Fibonacci**, que es explícita: los parámetros 50/33/66 salen de la Teoría de Dow; los seguidores de Elliott usan **38% y 62%**. **"Yo prefiero combinar ambos enfoques para una zona de retroceso mínimo entre 33 y 38% y una zona máxima de 62-68%."** Y añade que algunos técnicos redondean aún más a **una zona entre 40 y 60%**. Menciona que Gann desglosaba en octavos, dando importancia especial a 3/8, 4/8 y 5/8.

`[INTERPRETACIÓN]` **Esta sección es un caso de estudio sobre proliferación de parámetros.** En dos páginas aparecen como niveles relevantes: 33, 38, 40, 50, 60, 62, 66, 68, y los octavos de Gann (12.5, 25, 37.5, 50, 62.5, 75, 87.5). **Con suficientes niveles candidatos, casi cualquier retroceso cae cerca de alguno.** Y la conversión de niveles en *zonas* (33-38%, 62-68%) amplía aún más la cobertura. Esto es exactamente el mecanismo que hace una hipótesis difícil de falsar.

`[IMPLICACIÓN PARA IRIS]` La formalización útil no es "¿respeta el precio el 61.8%?" sino la variable continua subyacente: **la profundidad del retroceso como fracción del impulso previo**. Eso es `OHLCV-OK`, causal con el retardo de pivote, adimensional, y con **un solo grado de libertad** (la definición del impulso). Convierte una familia de niveles mágicos en una **distribución empírica comprobable**: ¿existe estructura en la distribución de profundidades de retroceso en MNQ? Es una pregunta bien planteada. **No la respondemos aquí ni adoptamos la feature.**

### 4.14 Líneas de velocidad, Gann y Fibonacci

`[MURPHY]` **Líneas de velocidad** (Edson Gould): se mide la distancia vertical del extremo al inicio de la tendencia, se divide en tercios, y se trazan líneas desde el inicio hasta los puntos de 1/3 y 2/3. **Miden el ritmo de ascenso o descenso.** Deben actuar como apoyo en correcciones; rotas, cambian de papel. **Cada vez que se establece un nuevo extremo hay que trazar un conjunto nuevo de líneas.**

`[MURPHY]` **Líneas de abanico de Fibonacci**: igual, pero con ángulos de 38% y 62%.

`[MURPHY]` **Líneas de Gann**: trazadas desde extremos con ángulos geométricos específicos; la más importante a 45°, con variantes a 63°, 75°, 26° y 15°. **Se pueden trazar hasta nueve líneas de Gann diferentes.**

Y aquí Murphy hace **la crítica más directa que formula contra una técnica en todo el capítulo**:

> `[MURPHY]` **"Las líneas de Gann resultan algo controvertidas, porque aunque una de ellas funcione, no se puede estar seguro por adelantado cuál será. Hay chartistas que cuestionan la validez de trazar líneas de tendencia geométricas."**

`[IMPLICACIÓN PARA IRIS]` **El propio autor identifica el problema exacto: nueve líneas, y sólo se sabe cuál importaba después.** Eso es la definición operativa de una técnica no falsable. Registrado como tal. Además, las líneas de Gann heredan el problema de la dependencia de escala de §4.11.

**Clasificación**: líneas de velocidad y Fibonacci — `OHLCV-OK` en datos, `LOOK-AHEAD-LEVE` en causalidad (dependen de extremos), **alta parametrización**. Líneas de Gann — **grados de libertad no acotados; formalización causal defendible dudosa.**

### 4.15 Días de cambio (reversal days)

`[MURPHY]` **Definición operativa, y es de las más limpias del libro:**
- **Día de cambio por arriba**: **nuevo máximo en una tendencia al alza, seguido de un cierre más bajo el mismo día** (por debajo del cierre del día anterior).
- **Día de cambio por abajo**: nuevo mínimo durante el día seguido de un cierre más alto.

`[MURPHY]` **Modificadores de significación**: cuanto más amplio el rango del día y mayor el volumen, más significativa. Si además **máximo y mínimo exceden el rango del día anterior** (día externo), tiene más significación, aunque no es requisito.

`[MURPHY]` **Racional del clímax vendedor**: un giro radical por abajo donde **todas las desalentadas posiciones largas se han visto forzadas a salir en grandes cantidades. La consiguiente ausencia de presión vendedora crea un vacío que los precios se apresuran a llenar subiendo.** Aunque no marque el mínimo último, generalmente indica que se ha visto un mínimo significativo.

`[MURPHY]` **Escalabilidad**: los cambios semanales tienen más significado que los diarios, y los mensuales más aún. Un cambio semanal al alza ocurre cuando el mercado opera más bajo durante la semana, alcanza nuevo mínimo, **pero cierra el viernes por encima del cierre del viernes anterior**.

`[MURPHY]` Y una valoración honesta: **"En sí misma, esta formación no tiene gran importancia, pero en el contexto de otra información técnica, a veces puede ser significativa."**

`[IMPLICACIÓN PARA IRIS]` **Este es probablemente el concepto más limpiamente formalizable de todo el capítulo**, y merece destacarse:
- **`OHLCV-OK`** — usa exactamente O, H, L, C y volumen.
- **`CAUSAL`** — calculable al cierre de la barra, sin necesidad de barras futuras. **No depende de pivotes.**
- **Grados de libertad mínimos**: la definición base tiene cero parámetros; los modificadores (rango amplio, volumen alto, día externo) añaden umbrales pero son opcionales y continuos.
- **Escalable a cualquier frecuencia** por construcción, incluida la intradiaria.
- **Tiene mecanismo económico explícito** (liquidación forzada de posiciones apalancadas), que además coincide con el mecanismo de soporte/resistencia.

`[INTERPRETACIÓN]` Y nótese que un "día de cambio" es exactamente **una relación continua entre O, H, L, C de dos barras consecutivas** — es decir, es lo mismo que un patrón de velas, descrito con otro vocabulario. Esto anticipa la tesis central de §21.

### 4.16 Huecos (gaps)

`[MURPHY]` **Definición**: áreas del gráfico donde no ha habido operaciones. En tendencia alcista, el precio abre por encima del máximo del día anterior dejando un espacio que no se rellena durante el día.

`[MURPHY]` **Desmiente explícitamente un mito**: "existen varios mitos sobre la interpretación de los huecos. Una de las máximas que se escucha con frecuencia es que **los huecos siempre se llenan, pero esto no es así**. Algunos deberían llenarse, otros no."

**Los tres tipos:**

| Tipo | Cuándo aparece | Volumen | ¿Se llena? | Función |
|---|---|---|---|---|
| **Separación** (breakaway) | Al completarse un patrón importante; inicio de movimiento significativo | **Mucho volumen** | **Normalmente no**; puede cerrarse parcialmente pero queda parte sin rellenar. **Cuanto más volumen tras el hueco, menos posibilidades de llenarse** | Los huecos al alza actúan como apoyo en correcciones posteriores. Un cierre por debajo es señal de debilidad |
| **Escape / medida** (runaway) | **Hacia la mitad del movimiento**; el mercado se mueve sin esfuerzo | **Volumen moderado** | Frecuentemente no | **Permite estimar la extensión restante doblando la distancia ya recorrida** desde la primera señal |
| **Agotamiento** (exhaustion) | **Cerca del final del movimiento** | — | — | Si va seguido de un hueco contrario en poco tiempo, forma una **isla de cambio máximo** |

`[IMPLICACIÓN PARA IRIS]` Análisis por partes:

- **La detección de un hueco es `OHLCV-OK` y `CAUSAL`**: comparar el rango de la barra actual con el de la anterior es inmediato y sin parámetros (salvo un umbral mínimo de tamaño).
- **La clasificación en los tres tipos es `LOOK-AHEAD-GRAVE`.** Un hueco de agotamiento sólo se sabe que era de agotamiento cuando el movimiento terminó. Un hueco de medida sólo se sabe que estaba a mitad de camino cuando el movimiento acabó. **La taxonomía entera se define por su posición dentro de un movimiento cuya extensión total sólo se conoce a posteriori.**
- `[INTERPRETACIÓN]` Por tanto: **el evento "hueco" es formalizable; la etiqueta "tipo de hueco" no lo es.** La distinción es exactamente la que el encargo pide entre reconocimiento retrospectivo y detección causal. Lo utilizable sería el hueco como **evento** más variables continuas de contexto (tamaño relativo, volumen, posición dentro del rango reciente), dejando que un modelo aprenda si esas condiciones discriminan — en lugar de imponer la taxonomía.
- **Advertencia intradiaria** `[VACÍO]`: en un futuro que opera casi 24 horas, los huecos entre barras consecutivas de un minuto son raros; los huecos relevantes ocurren en la transición de sesiones. Murphy no discute esto en absoluto. **El concepto puede tener frecuencia muy distinta en MNQ intradiario que en gráficos diarios de acciones.**

### 4.17 Síntesis del capítulo 4: clasificación de todos los conceptos

| Concepto | Datos | Causalidad | Grados de libertad | Descripción/Predicción/Operación |
|---|---|---|---|---|
| Dirección de tendencia (HH/HL) | `OHLCV-OK` | `LOOK-AHEAD-LEVE` (pivotes) | Medio (k, umbral, cierre/extremo) | A → C, sin B |
| Tres escalas | `OHLCV-OK` | `CAUSAL` | Alto (fronteras arbitrarias) | A |
| Mercado lateral = no operar | `OHLCV-OK` | `CAUSAL-CONF` | Medio | A → C explícito |
| **Soporte/resistencia** | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C, con mecanismo |
| **Mecanismo psicológico (3 grupos)** | — | — | — | **Racional causal, el más valioso** |
| Determinantes (tiempo, volumen, recencia) | `OHLCV-OK` | `CAUSAL` | Medio | B formalizable |
| Cambio de polaridad | `OHLCV-OK` | `CAUSAL-CONF` | Medio (umbral de penetración) | A → C, con mecanismo |
| Números redondos | `OHLCV-OK` | `CAUSAL` | **Bajo** | A → C, sin evidencia |
| Líneas de tendencia | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | **Alto (≥7)** | A → C |
| Filtros de ruptura (% / 2 días) | `OHLCV-OK` | `CAUSAL-CONF` | Medio | Trade-off bien identificado |
| Regla de medición de línea rota | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | B sin justificación |
| Principio abanico | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C |
| Inclinación 45° / Gann | `OHLCV-COND` | — | **No acotado; no invariante de escala** | Criticado por el propio autor |
| Líneas internas | `OHLCV-OK` | `LOOK-AHEAD-GRAVE` | No acotado (ajuste máximo) | Ajuste retrospectivo |
| Canales | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C |
| Fracaso en alcanzar el canal | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | **B interesante** |
| Retrocesos porcentuales | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | **Alto (proliferación de niveles)** | A → C |
| Líneas de velocidad / Fibonacci | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C |
| **Días de cambio** | **`OHLCV-OK`** | **`CAUSAL`** | **Muy bajo** | **A, con mecanismo** |
| Hueco (evento) | `OHLCV-OK` | `CAUSAL` | Bajo | A |
| Tipo de hueco (separación/escape/agotamiento) | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | Alto | Clasificación retrospectiva |


---

## 5. PATRONES DE CAMBIO (Cap. 5 — Nivel B)

### 5.1 Los seis principios comunes a todos los patrones de cambio

`[MURPHY]` Los enuncia explícitamente antes de entrar en patrones individuales:

1. **Requisito previo: la existencia de una tendencia anterior.** `[MURPHY]` "Un mercado obviamente debe tener algo que cambiar... si ese patrón no viene precedido de una tendencia, no hay nada que cambiar y el patrón es sospechoso."
2. **La primera señal es a menudo la ruptura de una línea de tendencia importante.** Con matiz: la violación de una línea principal **no anuncia necesariamente un cambio de dirección, sino un cambio dentro de la tendencia** — puede anunciar el inicio de un patrón lateral que después resultará ser de cambio o de continuidad.
3. **Cuanto más grande el patrón, mayor el movimiento subsiguiente.** "Grande" = **altura (volatilidad) y ancho (tiempo de construcción)**.
4. **Los patrones superiores son de duración más corta y más volátiles** que los inferiores.
5. **Los inferiores tienen bandas de precio menores y llevan más tiempo.**
6. **El volumen es más importante del lado ascendente.** `[MURPHY]` En los máximos, los mercados "caen por su propio peso" y el volumen no es fundamental. **En los mínimos, la recuperación del volumen es absolutamente esencial: si el volumen no muestra incremento significativo en la apertura al alza, todo el patrón debería cuestionarse.**

`[MURPHY]` Y una regla de acotación de objetivos: **el objetivo máximo es la extensión total del movimiento anterior.** "Los patrones de cambios sólo pueden volver hacia atrás lo que previamente han ido para adelante."

`[IMPLICACIÓN PARA IRIS]` El principio 3 es el más formalizable y el más interesante: convierte "tamaño del patrón" en **dos variables continuas medibles — amplitud del rango y duración** — con una hipótesis asociada (mayor tamaño → mayor movimiento posterior). Esa hipótesis **es directamente comprobable sobre MNQ sin necesidad de identificar ningún patrón nominal**. El principio 6 introduce una **asimetría entre techos y suelos** que también es comprobable. Ambos son ejemplos de lo que este capítulo puede aportar sin su taxonomía.

### 5.2 Cabeza y hombros — la anatomía completa

`[MURPHY]` Lo presenta como "probablemente el más conocido patrón principal de cambios y el de mayor confianza", y declara que **la mayoría de los demás patrones de cambio son sólo variaciones de este**.

**Los siete ingredientes, tal como los enumera:**
1. Una tendencia al alza previa.
2. Hombro izquierdo con **volumen mayor** (A), seguido de bajada correctiva (B).
3. Subida a nuevos máximos **con volumen más ligero** (C = cabeza).
4. Caída que **desciende por debajo del pico anterior (A)** y se acerca al mínimo previo (D).
5. Tercera subida (E) **con volumen marcadamente escaso** que no alcanza la cabeza.
6. **Un cierre por debajo de la base del cuello.**
7. Movimiento de retorno a la base del cuello (G) seguido de nuevos mínimos.

`[MURPHY]` **Lo importante es cómo lo explica**: el patrón "no es más que una revisión adicional de los conceptos de tendencia del capítulo 4". La secuencia de advertencias que describe es, punto por punto, la **degradación de la estructura HH/HL**:
- Volumen decreciente en cada nuevo máximo → presión compradora decreciente.
- La caída a D perfora el pico A, que **debería haber funcionado como apoyo** → violación del principio de polaridad.
- El fracaso de E en superar C → **cumple la mitad del requisito de nueva tendencia bajista (picos descendentes)**.
- Ruptura de la línea de tendencia en D.
- `[MURPHY]` "A pesar de todas las advertencias, todo lo que sabemos en este punto es que la tendencia ha cambiado de ascendente a lateral."

`[MURPHY]` **Confirmación**: el patrón **no queda completo hasta que la base del cuello queda claramente rota en base al cierre**. Se pueden aplicar los mismos filtros del cap. 4: penetración del 1-3% o la regla de dos días. **"Hasta que suceda esa violación, siempre existe la posibilidad de que el patrón no sea de cabeza y hombros y la tendencia alcista pueda reanudarse."**

`[MURPHY]` **Volumen, en detalle**: la cabeza debería darse con menos volumen que el hombro izquierdo (**"no es un requisito, sino una tendencia fuerte"**); **la señal de volumen más importante es el hombro derecho**, que debería tener volumen notoriamente menor; el volumen debería expandirse en la ruptura del cuello, bajar en el movimiento de retorno, y expandirse de nuevo al reanudarse el movimiento. Añade un matiz de segundo orden: si la ruptura del cuello se da con **fuerte volumen, las posibilidades de movimiento de retorno disminuyen**; con volumen ligero, aumentan.

`[MURPHY]` **Objetivo de precio**: distancia vertical de la cabeza a la base del cuello, proyectada desde el punto de ruptura. Alternativa equivalente: medir la primera onda de descenso (C a D) y doblarla. **Es un objetivo mínimo**; el máximo es el retroceso total del movimiento previo.

`[MURPHY]` **Y un pasaje metodológicamente muy revelador — el ajuste de objetivos:**

> **"Cuando existe una ligera discrepancia entre un objetivo de precio proyectado y un claro nivel de apoyo o resistencia, no es arriesgado ajustar el objetivo al nivel."** Hay que considerar dónde están los apoyos previos, los retrocesos del 50 y 66%, los huecos, las líneas de tendencia de larga duración... **"El analista técnico más habilidoso será aquel que sepa mezclar correctamente todas esas herramientas."**

`[INTERPRETACIÓN]` Este pasaje **documenta la irreproducibilidad del método mejor que cualquier crítica externa**. El objetivo de precio no es una salida de la regla: es un punto de partida que después se ajusta discrecionalmente combinando media docena de herramientas cuyos niveles rara vez coinciden. **Dos analistas competentes producirían objetivos distintos.** No es un defecto de exposición; es la naturaleza declarada del método ("mezclar correctamente").

### 5.3 Triples y dobles

`[MURPHY]`
- **Triple techo/suelo**: similar a cabeza y hombros **excepto que los tres picos están al mismo nivel**. Mismas reglas de volumen y de medición.
- **Doble techo/suelo** ("M" y "W"): **dos picos aproximadamente al mismo nivel**; el volumen tiende a ser mayor en el primero y menor en el segundo; **el patrón se completa cuando el valle intermedio se rompe en base al cierre**, con mayor volumen. Medición: altura del patrón proyectada desde la ruptura, o la altura de la primera pata (A→B) proyectada desde B.

`[MURPHY]` **Y aquí hace la advertencia más autocrítica del capítulo**, en una sección titulada *Abuso de la expresión "superior doble"*:

> **"En los mercados financieros se abusa de las referencias a los patrones superiores e inferiores dobles, que en la mayoría de los casos acaban siendo otra cosa diferente. La razón es que los precios tienen una fuerte tendencia a volver atrás desde un pico previo o a saltar desde un mínimo previo. Estos cambios son una reacción natural y en sí mismos no [constituyen el patrón]."**

Y añade: **"Al chartista le resulta muy difícil determinar si el retroceso a partir del pico anterior es un obstáculo temporal en la tendencia actual o el comienzo de un patrón de cambio."** Su recomendación: como las posibilidades técnicas favorecen la continuidad, **conviene esperar a que el patrón esté completo antes de actuar**.

`[MURPHY]` **Criterio de tamaño temporal**: la mayoría de los dobles válidos **deberían tener como mínimo un mes entre los dos picos**; en algunos casos dos o tres meses; en gráficos semanales y mensuales pueden cubrir varios años.

`[IMPLICACIÓN PARA IRIS]` Dos observaciones:
1. **Murphy identifica él mismo el sesgo de confirmación en el reconocimiento de patrones**: la gente ve dobles techos porque el precio *normalmente* retrocede desde un pico previo. Es decir, **el patrón se confunde con el comportamiento base**. Ese es exactamente el problema de no tener un baseline.
2. **El criterio de "mínimo un mes" no es transferible.** En barras de un minuto, un mes son ~30.000 barras. Escalarlo requeriría una convención (¿mismo número de barras? ¿misma proporción de la ventana?) **que Murphy no proporciona**. `[VACÍO]`

### 5.4 Trampas alcistas y filtros

`[MURPHY]` **Apertura falsa / trampa alcista**: no es infrecuente que la onda final de un mercado alcista **marque un nuevo máximo antes de cambiar de dirección**. Los filtros disponibles son los mismos del cap. 4: exigir cierre (no penetración intradía), filtro de precio (1-3%), regla de dos días, cierre de viernes, o confirmación por volumen.

Y una valoración honesta: **"Estos filtros no son ciertamente infalibles, pero sí sirven para reducir el número de señales falsas. A veces son útiles y otras no. El analista debe darse cuenta de que está tratando con porcentajes y probabilidades, y que habrá momentos en que se den malas señales."**

`[INTERPRETACIÓN]` **Es el pasaje del libro que más se acerca a un marco probabilístico.** Murphy reconoce que trabaja con probabilidades y que las señales fallan. Pero **nunca cuantifica ninguna de esas probabilidades** en todo el libro. Es la frontera exacta entre lo que aporta (el marco conceptual) y lo que no (la medición).

### 5.5 Platillos y púas

`[MURPHY]`
- **Platillo / fondo redondeado**: cambio muy lento y gradual de descendente a lateral a ascendente. **"Es difícil establecer exactamente cuándo el platillo queda completo o medir la distancia que los precios se desplazarán."** Se detecta en gráficos semanales o mensuales de varios años. Cuanto más dura, más importante.
- **Púa (patrón en V)**: **"los cambios en el mercado más difíciles de tratar"**, porque aparece muy rápidamente con un período de transición muy corto o inexistente. Ocurre en un mercado sobreextendido cuando una información adversa repentina lo revierte abruptamente. **"A veces, la única advertencia es un cambio diario o semanal con fuerte volumen."**

`[IMPLICACIÓN PARA IRIS]` **El platillo se autodescalifica**: el propio autor dice que no se puede establecer cuándo está completo ni medir su objetivo. `LOOK-AHEAD-GRAVE`, sin criterio de finalización. **La púa es especialmente relevante en sentido negativo**: es el caso donde el análisis de patrones no aporta ninguna anticipación, y Murphy lo admite. Y nótese que la única advertencia que ofrece —**un día de cambio con fuerte volumen**— es precisamente el concepto que identificamos en §4.15 como el más limpiamente formalizable y causal del libro.

### 5.6 Evaluación de formalizabilidad de los patrones de cambio

`[INTERPRETACIÓN]` Análisis por componentes, siguiendo la instrucción del encargo de no dar por sentado que el nombre de la figura sea lo importante.

**Qué necesita un detector de cabeza y hombros:**

| Elemento | Grado de libertad |
|---|---|
| Definición de pivote (k barras de confirmación) | Sí, y con `LOOK-AHEAD-LEVE` |
| Tolerancia de altura entre hombros ("aproximadamente a la misma altura") | Sí — ¿qué % de tolerancia? |
| Cuánto debe sobresalir la cabeza | Sí |
| Trazado de la base del cuello (recta entre dos mínimos, posiblemente inclinada) | Sí |
| Ventana de búsqueda (cuántas barras atrás) | Sí |
| Umbral de "tendencia previa" | Sí |
| Umbrales de volumen decreciente en cada pico | Sí (tres relaciones) |
| Filtro de ruptura (% o tiempo) | Sí |
| Criterio de proximidad temporal entre los tres picos | Sí |

**Nueve o más grados de libertad**, ninguno especificado numéricamente por Murphy. `[IMPLICACIÓN PARA IRIS]` Un detector de cabeza y hombros no es una técnica: **es una familia de detectores parametrizada en ≥9 dimensiones**. Buscar en ese espacio hasta encontrar la parametrización que "funciona" es la definición operativa de sobreajuste, y consumiría el presupuesto de multiple testing entero.

**La alternativa que el propio material sugiere.** `[INTERPRETACIÓN]` Murphy dice literalmente que el patrón "no es más que una revisión adicional de los conceptos de tendencia" y que los demás patrones son variaciones de este. Si eso es cierto, entonces la información no está en la figura sino en sus componentes, que **sí son medibles de forma continua y con muy pocos parámetros**:

- **Degradación de la estructura de impulsos**: ¿la amplitud del último impulso al alza es menor que la del anterior?
- **Violación del apoyo previo**: ¿la última corrección perforó el pico anterior que debía funcionar como soporte?
- **Divergencia precio-volumen**: ¿el volumen en cada máximo sucesivo es decreciente?
- **Contracción o expansión del rango.**
- **Duración de la fase lateral.**

Todas son `OHLCV-OK`, todas son continuas, todas tienen 1–2 parámetros. **Un modelo podría aprender si esas condiciones conjuntas tienen valor predictivo, sin que nadie tenga que definir qué es un "hombro".** Esta es una reformulación nuestra, no una propuesta de Murphy, y **no se adopta**: se registra como la forma en que este capítulo podría aportar algo sin importar su taxonomía.

### 5.7 Clasificación

| Concepto | Datos | Causalidad | GL | A/B/C |
|---|---|---|---|---|
| Necesidad de tendencia previa | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | Requisito |
| **Tamaño del patrón (altura × duración) → magnitud posterior** | **`OHLCV-OK`** | `LOOK-AHEAD-LEVE` | **Bajo** | **B comprobable** |
| Asimetría techos/suelos | `OHLCV-OK` | — | Bajo | **B comprobable** |
| **Volumen esencial en suelos, no en techos** | **`OHLCV-OK`** | `CAUSAL` | Bajo | **B comprobable** |
| Cabeza y hombros (figura completa) | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | **≥9** | A → C |
| Triple techo/suelo | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C |
| Doble techo/suelo | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | A → C |
| Objetivo de precio por altura | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | B sin evidencia |
| **Ajuste discrecional de objetivos** | — | — | **No acotado** | **No formalizable** |
| Trampa alcista / apertura falsa | `OHLCV-OK` | `CAUSAL-CONF` | Medio | A |
| Platillo | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | No acotado | Sin criterio de finalización |
| Púa (V) | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | — | El propio autor admite que no se anticipa |


---

## 6. PATRONES DE CONTINUIDAD (Cap. 6 — Nivel B)

`[MURPHY]` Distinción de partida: los patrones de continuidad **reflejan pausas en la tendencia actual más que cambios**, y **habitualmente se califican como intermedios y menores, en oposición a los principales**.

### 6.1 Triángulo simétrico

`[MURPHY]`
- **Requisito mínimo: cuatro puntos de cambio.** Razón geométrica explícita: hacen falta dos puntos por línea, y hay dos líneas convergentes.
- **La línea superior sólo se puede trazar una vez que los precios han bajado desde el punto 3**; la inferior, una vez han subido desde el punto 4. **Sólo entonces el analista comienza a sospechar que se trata de un triángulo.**
- Muchos triángulos tienen **seis puntos** (tres picos y tres valles = cinco ondas internas).

**Límite temporal — el elemento más original del patrón.** `[MURPHY]` **Existe un límite temporal para la resolución: el vértice donde se encuentran las líneas.** Regla: los precios deberían tomar la dirección de la tendencia previa **aproximadamente entre los dos tercios y los tres cuartos del ancho horizontal del triángulo**. **Si los precios permanecen dentro del triángulo más allá del punto de los tres cuartos, el triángulo comienza a perder su potencia.** Ejemplo que da: un triángulo de 18 semanas con salida en la semana 13.

`[MURPHY]` **"El triángulo proporciona una interesante combinación de precio y tiempo":** las líneas marcan los límites de precio e indican cuándo el patrón está completo; y **también proporcionan un objetivo de tiempo** midiendo el ancho.

`[MURPHY]` **Volumen**: debería **disminuir a medida que el precio oscila estrechamente** —"esta tendencia del volumen a contraerse es válida para todos los modelos de consolidación"— y **recuperarse notoriamente con la penetración**. Observación de segundo orden: aunque el volumen baje globalmente, **una inspección detallada suele indicar si el volumen más fuerte se da en los movimientos al alza o a la baja**; en una tendencia alcista tiende a ser ligeramente mayor en las subidas.

`[MURPHY]` **Medición**: (a) altura de la base proyectada desde el punto de salida — *"la técnica que yo prefiero"*; o (b) trazar una paralela a la línea inferior desde el punto alto de la base, que se convierte en objetivo.

`[IMPLICACIÓN PARA IRIS]` **El límite temporal es la idea más aprovechable de este capítulo**, porque introduce una dimensión que ningún otro concepto de Murphy tiene: **una hipótesis con caducidad**. Formulada sin geometría: *la contracción de rango tiene una duración característica; si se prolonga más allá de cierta fracción, la resolución esperada pierde fuerza.* `[INTERPRETACIÓN]` Eso es formalizable como **duración de la compresión relativa a su magnitud**, y es una hipótesis falsable sin necesidad de trazar dos rectas convergentes.

### 6.2 Triángulos ascendente y descendente

`[MURPHY]`
- **Ascendente**: línea superior plana, línea inferior ascendente. **"Indica que los compradores son más agresivos que los vendedores."** Se considera alcista.
- **Descendente**: el espejo. Bajista.

`[MURPHY]` **Y la diferencia crucial que él subraya**: ascendente y descendente **"con independencia del lugar de la estructura de la tendencia en el que aparezcan, tienen implicaciones de pronóstico muy definidas"**. El simétrico, en cambio, **es neutral por naturaleza**: hay que mirar la tendencia previa y asumir continuación.

`[INTERPRETACIÓN]` Esta distinción es lógicamente significativa. **El triángulo ascendente es el único patrón del libro que afirma tener contenido direccional propio, independiente del contexto.** Eso lo hace falsable de forma más limpia que el resto: la hipótesis es *tras una compresión con techo plano y suelo ascendente, la resolución al alza es más probable que a la baja* — comprobable sin conocer la tendencia previa.

`[INTERPRETACIÓN]` Y el racional que ofrece es de oferta y demanda: un techo plano significa **oferta concentrada en un nivel fijo**, mientras que los suelos ascendentes significan **demanda dispuesta a pagar cada vez más**. Es un mecanismo concreto y es compatible con el mecanismo de soporte/resistencia de §4.4.

### 6.3 Formación expansiva (broadening)

`[MURPHY]` Es el patrón invertido: **el volumen tiende a expandirse siguiendo oscilaciones de precio cada vez más amplias**. Representa **"un mercado fuera de control e inusualmente inestable"** y una cantidad inusual de participación pública. **Lo más frecuente es que ocurra en los máximos principales del mercado**, por lo que **generalmente es una formación bajista**.

`[INTERPRETACIÓN]` Reformulado sin geometría: **expansión simultánea de rango y volumen**. Ambas son variables continuas `OHLCV-OK` y `CAUSAL`, sin necesidad de trazar líneas divergentes. La hipótesis asociada (expansión de volatilidad + volumen → probabilidad elevada de techo) es directamente comprobable.

### 6.4 Banderas y banderines

`[MURPHY]` Los trata juntos porque comparten apariencia, ubicación y criterios.

**Los ocho puntos de su resumen:**
1. Ambos van precedidos de **un movimiento casi en línea recta (el "mástil") con fuerte volumen**.
2. Los precios hacen una pausa **de una a tres semanas con volumen muy débil**.
3. La tendencia se reanuda **con una explosión de operaciones**.
4. **Ambos aparecen aproximadamente a mitad de camino del movimiento.**
5. El banderín se parece a un pequeño triángulo simétrico horizontal.
6. La bandera es un pequeño paralelogramo **inclinado en dirección opuesta a la tendencia**.
7. **Ambos se desarrollan más rápidamente en tendencias bajistas** (una o dos semanas).
8. Ambos son muy comunes.

`[MURPHY]` Los califica como **"dentro de los patrones de continuidad más confiables"**, que "muy raramente producen un cambio de tendencia". Y **un requisito explícito: el volumen debe disminuir notoriamente durante la formación**.

`[MURPHY]` **Medición ("a media asta")**: el movimiento tras la reanudación **duplicará el mástil**. Más precisamente: medir la distancia del movimiento precedente desde el punto de ruptura original, y proyectarla desde el punto de salida de la bandera.

`[IMPLICACIÓN PARA IRIS]` **Advertencia de escala explícita**: "de una a tres semanas" en gráficos diarios. Y `[MURPHY]` señala en §5 que el requisito de duración es esencial. **No hay ninguna base en el libro para traducir "una a tres semanas" a barras de un minuto.** `[VACÍO]`

`[INTERPRETACIÓN]` La estructura subyacente, despojada de geometría, es: **impulso fuerte con volumen alto → contracción de rango con volumen bajo → expansión**. Eso es una secuencia de tres estados medibles con variables continuas y **sin ningún parámetro de forma**. Es la misma estructura que el encargo sugiere (`compresión → ruptura → confirmación/fallo`), y aparece de forma recurrente en todos los patrones de continuidad de este capítulo.

### 6.5 Cuñas

`[MURPHY]` Similar al triángulo simétrico en forma y tiempo (**dura más de un mes pero no más de tres**), pero distinguida por **su notoria inclinación**. Regla: **la cuña se inclina en dirección contraria a la tendencia prevaleciente**; por tanto **una cuña descendente es alcista y una ascendente es bajista**.

### 6.6 Rectángulos

`[MURPHY]` Banda horizontal entre soporte y resistencia bien definidos; duración típica de uno a tres meses.

**Diferencia de volumen respecto a otros patrones de continuidad:** `[MURPHY]` **las amplias fluctuaciones del precio previenen el habitual descenso de actividad** que caracteriza a triángulos y banderas. En su lugar, **hay que vigilar en qué dirección se da el volumen mayor**: si las subidas tienen fuerte volumen y los retrocesos menor, probablemente sea continuación alcista; si el volumen fuerte se da a la baja, es advertencia de cambio.

`[MURPHY]` **Tres estrategias distintas que documenta para el mismo patrón:**
1. **Operar las oscilaciones dentro de la banda** (comprar abajo, vender arriba). "Si la zona permanece intacta, este enfoque a contracorriente funciona bastante bien"; los riesgos están bien definidos porque se entra en los extremos. **Los osciladores resultan particularmente útiles en mercados laterales.**
2. **Asumir continuidad** y tomar largos cerca del suelo en tendencia alcista.
3. **Evitar completamente los mercados sin tendencia** y esperar la salida.

Y repite la advertencia: **"casi todos los sistemas que siguen tendencias obtienen pobres resultados durante estos períodos de movimientos laterales"**.

`[IMPLICACIÓN PARA IRIS]` **Este pasaje documenta explícitamente que la misma configuración admite tres reglas operativas incompatibles**, dos de ellas de signo opuesto (comprar en el suelo de la banda vs esperar la ruptura al alza). Murphy no ofrece criterio para elegir. `[INTERPRETACIÓN]` Es la ilustración más clara del libro de que **la descripción del estado no determina la regla operativa** — el paso (A) → (C) requiere una decisión adicional que la fuente no proporciona.

`[INTERPRETACIÓN]` También es donde Murphy más se acerca a la idea de **régimen condicionante**: en banda lateral funcionan los osciladores y fallan los seguidores de tendencia. Esa es una **hipótesis de régimen falsable** y directamente relevante para la pregunta de IRIS sobre en qué condiciones abstenerse. La registramos; no la adoptamos.

### 6.7 Movimiento medido

`[MURPHY]` Un avance importante **se divide en dos movimientos iguales y paralelos**: si el precio sube de A a B, corrige de B a C (retrocediendo entre un tercio y la mitad de AB), **el siguiente tramo CD prácticamente duplicará AB**. Requiere que los movimientos sean **"bastante ordenados y estar bien definidos"**.

Y él mismo lo sitúa: **"el movimiento medido es sólo una variación de algunas de las técnicas que ya hemos presentado"** — banderas a mitad de camino, retrocesos de un tercio a la mitad.

`[INTERPRETACIÓN]` Es la **misma hipótesis de simetría** que aparece en la regla de medición de líneas de tendencia (§4.10), en cabeza y hombros (§5.2), en los huecos de medida (§4.16) y en las banderas (§6.4). **Cinco formulaciones distintas de una única hipótesis: los movimientos tienden a repetir su magnitud.** Eso es en realidad una buena noticia metodológica: significa que **una sola variable continua —la magnitud del impulso previo— subyace a media docena de reglas nominalmente distintas**, y que la hipótesis puede comprobarse una vez en lugar de cinco.

`[MURPHY]` La condición "movimientos bastante ordenados y bien definidos" es `[INTERPRETACIÓN]` **una condición no operacionalizada** que en la práctica se evalúa a posteriori: se aplica el movimiento medido a los casos donde el gráfico ya se ve ordenado. Riesgo de selección.

### 6.8 Cabeza y hombros de continuidad

`[MURPHY]` El mismo patrón puede aparecer **como continuidad**: en tendencia alcista, el valle intermedio está más abajo que los dos hombros (cabeza y hombros invertido dentro de una tendencia al alza). **"Como aparece al revés, no hay posibilidad de confundirlo con el patrón de cambio."**

`[INTERPRETACIÓN]` Esto merece registrarse como **tensión interna**: el patrón de cambio más importante del libro **también funciona como patrón de continuidad**, con la orientación como único discriminante. Significa que la misma geometría de tres picos puede implicar reversión o continuación según su orientación relativa a la tendencia previa — lo que hace que la identificación de la tendencia previa (que ya tenía `LOOK-AHEAD-LEVE`) sea determinante para el significado del patrón. **Los grados de libertad se acumulan.**

### 6.9 Confirmación y divergencia

`[MURPHY]` Introduce ambos conceptos como "uno de los temas comunes a la totalidad del análisis de mercados":
- **Confirmación**: comparar todas las señales e indicadores **para asegurarse de que apuntan en la misma dirección y se confirman unos a otros**.
- **Divergencia**: situación en la que **diferentes indicadores no pueden confirmarse unos a otros**. Aunque se usa en sentido negativo, **es "una de las mejores señales anticipadas de inminentes cambios de tendencia"**.

`[IMPLICACIÓN PARA IRIS]` `[INTERPRETACIÓN]` Aquí hay una tensión metodológica que conviene nombrar ahora y que se desarrollará en §20:

**Si los indicadores son en su mayoría transformaciones del mismo historial de precios (cuestión abierta hasta §19), entonces "confirmación" entre ellos aporta mucha menos información de la que sugiere.** Que el RSI y el estocástico coincidan no es evidencia independiente: es la consecuencia esperada de que ambos midan aproximadamente lo mismo. La confirmación tiene valor informativo real sólo entre fuentes **genuinamente independientes** — que es exactamente lo que Dow buscaba al exigir dos índices distintos (§2), y lo que perdemos al trabajar con un solo instrumento y una sola fuente de datos.

Es una tensión que **no se resuelve aquí**; se registra para §40.

### 6.10 Clasificación de los patrones de continuidad

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| **Contracción de rango + contracción de volumen** | **`OHLCV-OK`** | **`CAUSAL`** | **Bajo** | Núcleo común de triángulos, banderas y cuñas, sin geometría |
| **Expansión de rango + expansión de volumen** | **`OHLCV-OK`** | **`CAUSAL`** | **Bajo** | Formación expansiva, sin geometría |
| **Límite temporal de la compresión (2/3–3/4)** | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | **Hipótesis con caducidad, original** |
| Triángulo simétrico (figura) | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto (≥6) | Neutral; requiere tendencia previa |
| **Triángulo ascendente/descendente** | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | **Único con dirección propia declarada** |
| Bandera / banderín | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | Escala no transferible a intradiario |
| Cuña | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Alto | Dirección = contraria a la inclinación |
| Rectángulo | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | **Tres reglas operativas incompatibles** |
| Volumen direccional dentro de la banda | `OHLCV-OK` | `CAUSAL` | Bajo | Comprobable |
| **Simetría de impulsos (movimiento medido)** | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Bajo | **Hipótesis única tras 5 reglas** |
| Cabeza y hombros de continuidad | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Muy alto | Significado depende de la tendencia previa |
| Confirmación / divergencia entre indicadores | `OHLCV-OK` | Depende | — | **Valor informativo condicionado a independencia** |


---

## 7. VOLUMEN E INTERÉS ABIERTO (Cap. 7 — Nivel A)

### 7.1 Jerarquía declarada

`[MURPHY]` Declaración inequívoca y repetida: **"El precio es, de lejos, el indicador más importante. El volumen y el interés abierto tienen una importancia secundaria."** El enfoque es tridimensional (precio, volumen, interés abierto), pero **el volumen no genera señales por sí mismo: confirma o advierte.**

`[IMPLICACIÓN PARA IRIS]` Registrar esta jerarquía importa porque acota la expectativa: **Murphy no sostiene que el volumen prediga; sostiene que valida o invalida lo que hace el precio.** Categoría (A) descripción con función de filtro, no (B) hipótesis predictiva independiente.

### 7.2 Qué mide el volumen, según Murphy

`[MURPHY]` **"El nivel de volumen mide la intensidad o la urgencia que hay detrás del movimiento de precios."** Un volumen mayor refleja mayor grado de intensidad o presión. Vigilándolo junto al precio, el técnico mide **la presión compradora o vendedora detrás del movimiento**.

**La regla básica:** `[MURPHY]` **el volumen debería aumentar o expandirse en la dirección de la tendencia actual.** En tendencia al alza, mayor al subir y menor al bajar. Mientras eso ocurra, **el volumen confirma la tendencia**.

**Divergencia:** `[MURPHY]` ocurre si **la penetración de un máximo anterior tiene lugar con volumen en declive**. Si además el volumen se recupera en las bajadas, la tendencia alcista tiene problemas.

`[MURPHY]` **Y la afirmación más fuerte del capítulo, que es una hipótesis predictiva explícita:**

> **"El volumen precede al precio. Los cambios en la presión vendedora o compradora a menudo se detectan antes en el volumen que en el precio."**

`[IMPLICACIÓN PARA IRIS]` **Esta sí es una afirmación de categoría (B), falsable y directamente comprobable sobre MNQ**: ¿el volumen contiene información sobre el retorno futuro por encima de la que contiene el propio precio pasado? Es una pregunta bien planteada y `OHLCV-OK`. `[VACÍO]` **Murphy no aporta ninguna evidencia de ella.**

### 7.3 El volumen como confirmación de patrones

`[MURPHY]` Recopila la regla transversal: **la resolución de todos los patrones de precios (el punto de ruptura) debería ir acompañada por mayor cantidad de operaciones si la señal es real.**

Y el patrón de volumen específico por figura: menor volumen en la cabeza que en el hombro izquierdo; volumen decreciente en cada pico sucesivo en dobles y triples; **descenso gradual durante los triángulos**; expansión en la ruptura.

`[INTERPRETACIÓN]` Nótese que esto convierte el volumen en **un filtro de calidad de la señal de precio**, no en una señal. Es exactamente la estructura de un sistema de dos niveles: el precio propone, el volumen valida. **Registramos la analogía estructural sin resolverla** (ver §33 y §40).

### 7.4 Volumen Total Acumulativo (OBV) y sus limitaciones

`[MURPHY]` **Construcción**: a cada día se le asigna el volumen total con signo positivo o negativo **según el cierre sea más alto o más bajo que el anterior**; se acumula. **"Lo importante es la dirección de la línea, no los números reales."** La línea debería seguir la misma dirección que el precio; cuando no lo hace, hay divergencia.

`[MURPHY]` **Y expone él mismo sus dos inconvenientes con precisión:**
> **"Asigna un valor positivo o negativo al volumen de todo un día. Suponga que el mercado cierra al alza por una cantidad mínima... ¿Es razonable asignar un valor positivo a la actividad de todo ese día? O considere una situación en la que el mercado está casi todo el día en posición ascendente pero cierra ligeramente más abajo. ¿Debe darse un valor negativo al volumen de todo ese día?"**

**Variantes que menciona:** ponderar el volumen por la magnitud del cambio de precio; el Índice de Demanda de Sibbet (precio + volumen); el Índice de Rentabilidad de Herrick (usa interés abierto); y el **Flujo Monetario de Birinyi**, versión en tiempo real que **vigila el volumen en cada cambio de precio a lo largo del día** para determinar si el dinero entra o sale.

`[MURPHY]` **Y la observación decisiva para nosotros:** **"La información sobre volumen es mucho más útil en el mercado de valores que en el de futuros. El volumen de las operaciones con valores se conoce de forma inmediata, mientras que en futuros se conoce con un día de demora. También se dispone de los niveles al alza y a la baja para los valores, pero no para los futuros."**

`[IMPLICACIÓN PARA IRIS]` **Clasificación del OBV: `OHLCV-OK` y `CAUSAL`.** Es construible exactamente como Murphy lo define, con cero parámetros libres.

**Pero el Flujo Monetario de Birinyi es `GRANULAR`**: requiere volumen asociado a cada cambio de precio intradía. Y esto conecta con una distinción que el encargo pide subrayar:

> **El `Volume` de nuestras barras OHLCV es una magnitud agregada sin dirección.** No es order flow, no es volumen al bid o al ask, no es delta, no informa del aggressor side. El OBV **infiere** una dirección a partir del signo del cierre, que es una aproximación grosera —y Murphy mismo explica por qué es grosera con sus dos ejemplos—. **Ninguna transformación de OHLCV puede recuperar la dirección real del flujo.**

`[INTERPRETACIÓN]` Y hay un matiz favorable que conviene registrar: **la crítica de Murphy al OBV se debilita al aumentar la frecuencia.** Con barras de un minuto, la objeción "el mercado estuvo todo el día subiendo pero cerró abajo" es mucho menos grave, porque el intervalo dentro del cual se pierde información es mucho menor. **Esto es una hipótesis nuestra, no de Murphy**, y sugiere que la calidad de aproximación del OBV depende de la resolución de barra — cuestión abierta a comprobar empíricamente.

### 7.5 Limitaciones del volumen en futuros que Murphy señala

`[MURPHY]`
1. **Desfase de un día** en las cifras oficiales de volumen (sólo hay estimaciones el mismo día).
2. **Uso de volumen total en lugar del contrato individual**, con la justificación explícita: *"¿Cómo se trata una situación en la que algunos contratos cierran más altos y otros más bajos en el mismo mercado y el mismo día?"*
3. **Días límite**: cuando el mercado se mueve al límite máximo, el volumen es **bajo** — y eso es señal de **fuerza**, porque hay tantos compradores que el precio topa y deja de operar. **"Según las normas tradicionales, poco volumen durante una subida es una situación bajista. El poco volumen de los días límite es una violación de tal principio y puede distorsionar los números del VTA."**

`[IMPLICACIÓN PARA IRIS]` **Los tres puntos son relevantes de forma distinta para nosotros:**
- El punto 1 **no nos afecta**: los datos de volumen de barras intradiarias de MNQ están disponibles en tiempo real, a diferencia del interés abierto.
- El punto 2 **sí nos afecta directamente**: es el problema de qué volumen usar durante la transición de contratos. Si construimos una serie continua empalmando contratos, el volumen del contrato saliente decae y el del entrante crece por razones de calendario. **Murphy identifica el problema pero su solución (usar el total del mercado) requiere datos de todos los contratos, que no tenemos.** `[VACÍO]` **Queda como problema abierto y es una limitación real de nuestra fuente.**
- El punto 3 **es un ejemplo de excepción que invierte la regla**: una condición de mercado (límite de precio) donde el volumen bajo significa lo contrario de lo habitual. Es una tensión interna documentada por el propio autor.

### 7.6 Interés abierto

`[MURPHY]` **Definición y mecánica**: número total de contratos pendientes al final del día. Cada operación tiene comprador y vendedor; el OI aumenta si **ambos** inician posición nueva, disminuye si **ambos** liquidan, y no cambia si uno entra y otro sale. **Son los cambios netos los que dan al chartista pautas sobre el carácter cambiante de la participación.**

**La tabla de interpretación conjunta:**

| Precio | Volumen | Interés abierto | Mercado |
|---|---|---|---|
| En alza | En alza | En alza | **Fuerte** |
| En alza | En descenso | En descenso | **Débil** |
| En descenso | En alza | En alza | **Débil** |
| En descenso | En descenso | En descenso | **Fuerte** |

`[MURPHY]` **Reglas específicas de OI** (las que él marca como aplicables sólo a futuros):
- Una **estabilización o disminución repentina del OI** dentro de una tendencia al alza es advertencia de cambio.
- **OI muy alto en máximos del mercado es peligroso** y puede intensificar la presión a la baja.
- **Crecimiento del OI durante consolidaciones intensifica la ruptura posterior.**
- OI creciente al final de un patrón confirma la señal. **Con una advertencia propia**: como el ímpetu tras la señal inicial lo provocan a menudo los que están en el lado equivocado, **a veces el OI cae al principio de una nueva tendencia**, lo que puede confundir. Y de ahí concluye: **"da argumentos en contra de concentrar demasiada atención en los cambios del interés abierto en períodos de muy corta duración."**

**Clasificación: `OTRAS FUENTES`.** El interés abierto **no forma parte de `Timestamp + OHLCV`**. **No se propone incorporarlo.**

`[IMPLICACIÓN PARA IRIS]` Dos observaciones para documentar la renuncia:
1. **Lo que perdemos**: la capacidad de distinguir si un movimiento de precio viene acompañado de **entrada de dinero nuevo** o de **liquidación de posiciones existentes**. Es información conceptualmente distinta de la que aporta el volumen: el volumen dice cuánto se negoció; el OI dice si el resultado neto fue crear o destruir posiciones. **No hay ninguna transformación de OHLCV que recupere esa distinción.**
2. **Lo que atenúa la pérdida**: la propia advertencia de Murphy de que el OI es poco fiable en períodos de muy corta duración, y el desfase de un día en su publicación, hacen que su utilidad en un sistema intradiario sea cuestionable incluso si lo tuviéramos. `[INTERPRETACIÓN]` **La renuncia es menos costosa en intradiario que en horizontes largos.**

### 7.7 Descargas y clímax de ventas

`[MURPHY]` **Descarga (blowoff)** en máximos: tras un largo avance, los precios **suben de forma destacada con un gran salto de operaciones y alcanzan su máximo de forma abrupta**. En futuros, va acompañada con frecuencia por **descenso del interés abierto** durante la última subida.

**Clímax de ventas** en mínimos: los precios **caen mucho de forma repentina con fuertes operaciones y vuelven a subir de forma igualmente rápida**.

`[INTERPRETACIÓN]` Reformulado con nuestras variables: **expansión extrema simultánea de rango y volumen tras un movimiento direccional extendido**. Es `OHLCV-OK` y `CAUSAL` en el momento de la barra; lo que **no** es causal es saber que ese pico fue *el* máximo. **El evento es detectable; la etiqueta "fue el techo" es retrospectiva.** Misma distinción que en los huecos (§4.16).

Y nótese la convergencia: descarga, clímax de ventas y día de cambio (§4.15) describen **la misma configuración desde vocabularios distintos**: rango amplio + volumen alto + reversión del cierre respecto al extremo.

### 7.8 Informe de Compromisos de los Operadores (COT)

`[MURPHY]` Publicado por la CFTC dos veces al mes; desglosa el interés abierto en **grandes coberturas (comerciales), grandes especuladores y pequeños operadores**. El principio: **"los grandes comerciales de la cobertura normalmente tienen razón y los operadores están equivocados"**. La idea es posicionarse con los comerciales y contra las otras dos categorías.

**Clasificación: `OTRAS FUENTES`.** Además: **frecuencia quincenal, publicación diferida**. **No aplicable a un sistema intradiario ni construible desde OHLCV.** No se propone incorporarlo.

### 7.9 Clasificación del capítulo 7

| Concepto | Datos | Causalidad | GL | Categoría |
|---|---|---|---|---|
| Volumen como medida de intensidad | **`OHLCV-OK`** | `CAUSAL` | Cero | (A) descripción |
| **Volumen confirma la tendencia** | **`OHLCV-OK`** | `CAUSAL` | Bajo | (A)→filtro |
| Divergencia precio-volumen | `OHLCV-OK` | `LOOK-AHEAD-LEVE` (requiere extremos) | Medio | (B) sin evidencia |
| **"El volumen precede al precio"** | **`OHLCV-OK`** | `CAUSAL` | Bajo | **(B) falsable, sin evidencia** |
| Expansión de volumen en la ruptura | `OHLCV-OK` | `CAUSAL` | Bajo | Filtro |
| Contracción de volumen en consolidación | `OHLCV-OK` | `CAUSAL` | Bajo | (A) |
| **OBV / VTA** | **`OHLCV-OK`** | **`CAUSAL`** | **Cero** | (A), con limitación admitida por el autor |
| OBV ponderado por magnitud | `OHLCV-OK` | `CAUSAL` | Bajo | Variante |
| Flujo Monetario (Birinyi) | **`GRANULAR`** | — | — | Requiere volumen por cambio de precio |
| Volumen al alza / a la baja | **`GRANULAR`** | — | — | Murphy: no disponible en futuros |
| **Interés abierto (todas sus reglas)** | **`OTRAS FUENTES`** | — | — | No disponible; el autor lo desaconseja en corto plazo |
| Descarga / clímax de ventas (evento) | `OHLCV-OK` | `CAUSAL` | Bajo | (A) |
| Descarga / clímax (como techo/suelo) | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | — | Etiqueta retrospectiva |
| Informe COT | **`OTRAS FUENTES`** | — | — | Quincenal y diferido |
| Problema del volumen en transición de contratos | — | — | — | **`[VACÍO]` sin solución con nuestros datos** |


---

## 8. GRÁFICOS A LARGO PLAZO, FUTUROS Y CONTRATOS CONTINUOS (Cap. 8 + Apéndice D — Nivel A/B)

Se tratan juntos porque el Apéndice D (redactado por Greg Morris) desarrolla lo que el capítulo 8 introduce. Es el bloque más directamente relevante para la construcción de nuestro histórico de MNQ.

### 8.1 El problema de la continuidad en futuros

`[MURPHY]` El método básico es **encadenar los contratos más próximos a vencer**: cuando el contrato actual deja de operar, el siguiente pasa a ser el más próximo y es el que se registra.

**Y expone los problemas del método con precisión:**
1. **"A veces, puede ser que el contrato que vence esté operando por encima de la par o con descuento, y el cambio al nuevo contrato cause una repentina caída o subida del precio en el gráfico."**
2. **"Otra posible distorsión es la extrema volatilidad que experimentan algunos contratos al contado justo antes de vencer."**

**Las cuatro soluciones que documenta:**
- Dejar de representar el contrato más próximo **uno o dos meses antes del vencimiento**, para evitar la volatilidad del mes al contado.
- **Ignorar el contrato siguiente y usar el segundo o el tercero.**
- **Usar el contrato con el interés abierto más alto**, sobre la teoría de que es "la representación más verdadera del valor del mercado".
- Unir **meses naturales específicos** (todos los contratos de noviembre de cada año). Técnica que atribuye a W. D. Gann.
- Promediar precios de varios contratos o construir índices que **suavicen el cambio mediante ajustes de la prima o el descuento**.

`[MURPHY]` **Contrato Perpetuo™** (Pelletier / CSI): construye una serie basada en **un período constante hacia adelante** (por ejemplo, 3 o 6 meses), tomando **la media ponderada de los dos contratos que rodean ese período**. **"El valor del Contrato Perpetuo no es un precio real, sino una media ponderada de otros dos precios."** Ventaja: elimina la necesidad de usar sólo el contrato más próximo y **allana la serie eliminando las distorsiones de la transición**.

`[MURPHY]` **Y una distinción de uso muy relevante para nosotros:**

> **"A efectos del análisis de gráficos, los gráficos de continuidad del mes más cercano son más que adecuados. Una serie continuada de precios, sin embargo, es más útil para reexaminar sistemas de contratación e indicadores."**

`[IMPLICACIÓN PARA IRIS]` **Esa frase distingue exactamente nuestro caso.** IRIS no hace análisis visual: entrena y valida un sistema sobre histórico. Según el propio Murphy, ese uso **requiere una serie continua construida deliberadamente**, no el encadenamiento simple del contrato más cercano.

### 8.2 Apéndice D — los cuatro tipos de contrato derivado

`[MURPHY / Greg Morris]`

| Tipo | Construcción | Propiedad clave |
|---|---|---|
| **Más cercano (nearest)** | Encadena contratos reales, con una **fecha de renovación parametrizable** (0, 5, 12, 15, 21 días antes del vencimiento). | **Contiene datos contractuales reales.** La única diferencia entre variantes es de qué contrato provienen los datos. |
| **Siguiente (next)** | Siempre el contrato posterior al más cercano; existen next-1 y next-2. | Datos reales de un vencimiento más lejano. |
| **Gann** | Usa siempre el mismo mes natural, renovando al año siguiente. | Datos reales; captura estacionalidad de un mes concreto. |
| **Continuo a plazo constante** | **Extrapolación lineal entre los dos (o N) contratos más cercanos**, referida a un número fijo de semanas hacia el futuro. | **No es un precio real.** Se aplica de forma idéntica a apertura, máximo, mínimo y cierre. |

**Y dos observaciones operativas importantes:**

`[MURPHY / Morris]` **"Es bastante probable que nadie opere con el contrato más cercano en el plazo que va de los 15 a los 30 días previos al vencimiento, debido a que la liquidez se agota muy rápidamente en los últimos días."** El número de días antes del vencimiento en que se renueva es **función del bien y del sistema de contratación del individuo**.

`[MURPHY / Morris]` **El criterio de renovación**: **"La renovación hacia el contrato siguiente probablemente se base en el volumen del contrato actual. Cuando comienza a erosionarse, es el momento de seguir adelante."**

`[MURPHY / Morris]` **La motivación explícita de los contratos continuos**: **"se desarrollaron para ayudar a los analistas a superar el problema de la desaparición de la liquidez y los huecos en la prima (o descuento)... Este problema aparece cuando un analista está probando un modelo o sistema de contratación con información correspondiente a muchos años. Los contratos continuos permiten una corriente ininterrumpida de datos en la que se compensan los saltos por renovación."**

### 8.3 Evaluación para IRIS

`[IMPLICACIÓN PARA IRIS]` Este material es **directamente relevante y hay que ser preciso sobre qué aporta y qué no**.

**Lo que aporta:**

1. **Un criterio de rollover basado en volumen**, que es `OHLCV-OK`. Morris propone renovar cuando el volumen del contrato actual empieza a erosionarse. **Esto es exactamente el sustituto del criterio de interés abierto de Murphy (§3.4) que nosotros no podemos aplicar** — y es construible con nuestros datos, siempre que dispongamos del volumen por contrato durante la transición.
2. **La confirmación de que el problema es real y conocido en la disciplina**: los saltos de prima/descuento en la renovación distorsionan las pruebas de sistemas sobre histórico largo.
3. **La distinción entre series de precios reales y series construidas**: los tipos "más cercano", "siguiente" y "Gann" contienen precios reales; el "continuo a plazo constante" **no es un precio real**.
4. **La advertencia de liquidez**: 15 a 30 días antes del vencimiento la liquidez se agota. Aplicable al MNQ (ciclo trimestral).

**Lo que NO aporta:**

`[VACÍO]` **Ni Murphy ni Morris explican cómo compensar los saltos.** Dicen que los contratos continuos "compensan los saltos por renovación", pero el único método que desarrollan en detalle —el de plazo constante— **no compensa saltos: interpola entre contratos**, produciendo una serie que no corresponde a ningún precio operable. **No hay ninguna descripción de un ajuste por diferencia ni por ratio.**

`[VACÍO]` **No se discute el efecto del método de empalme sobre los retornos ni sobre las pruebas de sistemas**, más allá de constatar que el problema existe.

`[VACÍO]` **No se discute el tratamiento del volumen durante la transición**, que es el problema que ya identificamos en §7.5.

`[VACÍO]` **Nada de esto está tratado en frecuencia intradiaria.** El ejemplo del apéndice usa precios de cierre y proyecciones de semanas.

`[INTERPRETACIÓN]` Conviene registrar una tensión de fondo: **el contrato de plazo constante resuelve el problema de continuidad al precio de producir una serie sintética que no es negociable.** Para análisis visual eso puede ser aceptable; **para un sistema que debe simular PnL, una serie de precios no operables es problemática**, porque las señales se generarían sobre precios que nunca existieron. La distinción entre "serie para modelar" y "serie para simular ejecución" queda planteada pero **no resuelta**, y coincide temáticamente con una distinción que apareció en la etapa anterior. **No se cierra ninguna decisión sobre el método de rollover de IRIS.**

### 8.4 Análisis multitemporal: el enfoque top-down

`[MURPHY]` **La regla de orden es explícita**: **"El orden adecuado a seguir en el análisis de gráficos es comenzar por los de largo alcance y gradualmente pasar a los de corto plazo."**

**El razonamiento que da:**
> **"Si el analista comienza solamente con la información a corto plazo, se verá forzado a revisar sus conclusiones constantemente a medida que considere más informaciones sobre el precio. Después de mirar los gráficos de largo alcance, un análisis completo y detallado de un gráfico diario puede tener que rehacerse completamente. Pero si se comienza con la visión completa... todos los datos a considerar ya están incluidos en el gráfico y se obtiene una perspectiva adecuada."**

**La secuencia concreta:** mensual de 20 años → semanal de 5 años → diario de 6-9 meses → **intradía si se quiere seguir adelante**, "para un estudio más microscópico".

`[MURPHY]` **Y la separación funcional entre escalas, que es la afirmación más importante de la sección:**

> **"Los gráficos a largo plazo no están pensados para contratar. Se tiene que hacer la distinción entre análisis del mercado con el fin de hacer pronósticos y el cálculo del momento adecuado para los compromisos con el mercado. Los gráficos a largo plazo son útiles para ayudar a determinar la tendencia principal y los objetivos de precios, pero no son adecuados para calcular el momento de entrar o salir, y no deberían usarse con tal fin. Para esa tarea deberían utilizarse los gráficos diarios e intradía."**

`[IMPLICACIÓN PARA IRIS]` **Esta es la formulación más clara del libro de una arquitectura de escalas con roles asimétricos:**

```
ESCALA LARGA   →  determina la DIRECCIÓN y los objetivos
ESCALA CORTA   →  determina el MOMENTO de entrada y salida
```

Tres observaciones:
1. **Es formalizable sin comprometer ventanas concretas**: la idea es que información calculada sobre horizontes distintos cumple funciones distintas, no que exista una jerarquía privilegiada de 20 años / 5 años / 9 meses. **Las escalas concretas de Murphy son de análisis visual humano y no tienen ninguna base para MNQ intradiario.**
2. **Conecta con la separación análisis/timing del cap. 1** (§1.5) y da una implementación concreta a esa distinción.
3. `[INTERPRETACIÓN]` La formulación "una escala decide la dirección, otra decide el momento" **tiene una analogía estructural evidente con la separación side/size** de la fuente anterior, y con la estructura primario/secundario. **No la resolvemos aquí**; queda registrada en §33 y §40 como una de las tensiones/convergencias más importantes de la síntesis pendiente.

`[VACÍO]` **Murphy no explica qué hacer cuando las escalas se contradicen**, más allá de decir que la tendencia menor es una corrección de la mayor. No hay regla de resolución de conflictos entre escalas.

### 8.5 Tendencias de largo plazo y aleatoriedad

`[MURPHY]` **"La característica más sorprendente de los gráficos de largo alcance es que no sólo están claramente definidas las tendencias, sino que las de largo alcance a menudo duran años."**

Y de ahí extrae un argumento contra el paseo aleatorio: **"la aleatoriedad que existe en los movimientos del precio probablemente es un fenómeno de muy corta duración. La persistencia de las tendencias existentes en largos períodos, en muchos casos años, es un argumento contundente contra lo sostenido por los teóricos del Paseo Aleatorio."**

`[INTERPRETACIÓN]` **Esta afirmación es directamente adversa a la premisa operativa de IRIS y debe registrarse como tal.** Murphy sostiene que la estructura predecible está en el largo plazo y que **el ruido domina el corto plazo**. Si tuviera razón, un sistema intradiario estaría operando precisamente en la franja que él considera menos estructurada.

Dos matices:
- No aporta ninguna evidencia de esa afirmación; es una impresión derivada de la inspección visual de gráficos de largo plazo.
- Es además **circular en el mismo sentido que el argumento del cap. 1**: las tendencias de años son visibles a posteriori en cualquier serie, incluida una generada aleatoriamente, precisamente porque un paseo aleatorio produce trayectorias con largos tramos aparentemente direccionales.

**Pero la registramos íntegra**, conforme a la instrucción de no forzar a Murphy a confirmar decisiones previas: **es una fuente que, leída literalmente, desaconseja el horizonte que IRIS ha elegido.** Ver §38 y §40.

### 8.6 Ajuste por inflación

`[MURPHY]` Sostiene que **no es necesario** ajustar los gráficos de largo plazo por inflación, porque **"los propios mercados ya han hecho los ajustes necesarios"**, y remite a la premisa de que el precio lo descuenta todo, incluida la inflación.

`[IMPLICACIÓN PARA IRIS]` **`NO RELEVANTE`** para un horizonte intradiario. Se registra únicamente porque ilustra cómo el autor usa la premisa 1 para resolver cuestiones metodológicas: **la premisa no falsable se emplea como argumento para no hacer un ajuste.** Es un ejemplo del problema señalado en §1.2.

### 8.7 Cambios semanales y mensuales

`[MURPHY]` En el gráfico mensual, **un nuevo máximo mensual seguido de un cierre por debajo del cierre del mes anterior** a menudo representa un punto de inflexión destacado, **especialmente si ocurre cerca de un área principal de apoyo o resistencia**. Son el equivalente del día de cambio clave, **"donde estos cambios conllevan bastante más significación"**.

`[INTERPRETACIÓN]` **Confirma que el día de cambio (§4.15) es un concepto invariante de escala** por construcción: sólo requiere comparar el extremo y el cierre de la barra actual con el cierre de la anterior. Murphy lo aplica a barras diarias, semanales y mensuales con la misma definición. `[IMPLICACIÓN PARA IRIS]` **La aplicabilidad a barras de un minuto es estructuralmente inmediata; su valor predictivo a esa escala es una pregunta empírica abierta que el libro no responde.**

### 8.8 Clasificación

| Concepto | Datos | Causalidad | Observación |
|---|---|---|---|
| Encadenamiento del contrato más cercano | **`OHLCV-COND`** | `CAUSAL` | Requiere identificador de contrato; produce saltos |
| **Renovación por erosión del volumen** | **`OHLCV-COND`** | `CAUSAL` | Requiere volumen por contrato en la transición |
| Renovación por interés abierto | **`OTRAS FUENTES`** | — | No disponible |
| Renovación N días antes del vencimiento | **`OHLCV-COND`** | `CAUSAL` | Requiere calendario de vencimientos |
| Contrato "siguiente" / Gann | `OHLCV-COND` | `CAUSAL` | Datos reales de otro vencimiento |
| **Contrato continuo a plazo constante** | `OHLCV-COND` | `CAUSAL` | **No es precio real; no operable** |
| Método de compensación de saltos | — | — | **`[VACÍO]` no descrito** |
| Volumen durante la transición | — | — | **`[VACÍO]` no tratado** |
| **Top-down multiescala (dirección vs timing)** | **`OHLCV-OK`** | `CAUSAL` | **Arquitectura formalizable; escalas concretas no transferibles** |
| Resolución de conflictos entre escalas | — | — | **`[VACÍO]`** |
| Persistencia de tendencias largas | — | — | Afirmación sin evidencia; **adversa al horizonte de IRIS** |
| Ajuste por inflación | — | — | `NO RELEVANTE` |
| Cambios semanales/mensuales | `OHLCV-OK` | `CAUSAL` | Invariante de escala |


---

## 9. MEDIAS MÓVILES (Cap. 9 — Nivel A)

### 9.1 Qué es y qué no es

`[MURPHY]` **La definición funcional, y es una de las afirmaciones más honestas del libro:**

> **"La media móvil es esencialmente una forma de seguir una tendencia. Su propósito es hacer saber que ha comenzado una tendencia nueva o que una vieja ha finalizado o ha cambiado de dirección... pero no pronostica la acción del mercado en el mismo sentido que intenta hacerlo el análisis gráfico común. La media móvil es un seguidor, no un líder. Nunca anticipa, sólo reacciona. La media móvil sigue un mercado y nos dice que ha comenzado una tendencia, pero sólo después de producirse el hecho."**

`[MURPHY]` Es un **mecanismo de suavizado** que produce una línea más suave para facilitar la visión de la tendencia subyacente, **al coste de un desfase cronológico que se reduce con medias más cortas pero nunca se elimina del todo**. Y la califica de **"línea de tendencia curva"**.

`[IMPLICACIÓN PARA IRIS]` Registrar esta caracterización importa: **el propio autor sitúa la media móvil en la categoría (A) descripción, no (B) predicción.** "Nunca anticipa, sólo reacciona." Cualquier valor predictivo que la media móvil pueda tener en IRIS **no está respaldado por Murphy**, que explícitamente niega que anticipe.

### 9.2 Qué precios promediar

`[MURPHY]` El cierre es lo más común, pero documenta alternativas: el **punto medio del rango** (`(H+L)/2`); el **precio típico** (`(H+L+C)/3`); y **promediar máximos y mínimos por separado**, produciendo dos líneas que actúan como "amortiguador de volatilidad o zona neutra".

`[IMPLICACIÓN PARA IRIS]` `OHLCV-OK`, y es un grado de libertad más que suele pasar desapercibido. **La elección de la serie de entrada es un parámetro, no un detalle.**

### 9.3 Los tres tipos de media y la comparación honesta

| Tipo | Construcción | Crítica que recoge Murphy |
|---|---|---|
| **Simple (aritmética)** | Media de los últimos N cierres | **Dos críticas**: (1) sólo considera el período cubierto; (2) **da el mismo peso a cada día** |
| **Ponderada linealmente** | Multiplica cada precio por su posición (10, 9, 8...) y divide por la suma de multiplicadores | Corrige la ponderación, pero **"no solventa el problema de incluir sólo los movimientos del precio cubiertos por la duración de la media misma"** |
| **Exponencial** | Peso porcentual al último precio sumado al complemento del valor previo | **Resuelve los dos problemas**: pondera lo reciente **e incluye toda la historia**. El usuario puede ajustar la carga |

`[MURPHY]` **Y el veredicto empírico, que conviene retener literalmente:**

> **"Aunque las medias exponenciales se han hecho populares, no hay evidencia real que demuestre que funcionan mejor que la media simple."**

`[IMPLICACIÓN PARA IRIS]` **Es una de las poquísimas veces en el libro donde Murphy declara ausencia de evidencia sobre una elección concreta.** Y es directamente aplicable: la elección SMA/EMA/WMA **no está resuelta por la fuente**, y las tres son transformaciones lineales del mismo historial de precios con perfiles de ponderación distintos. Ver §36.

### 9.4 El compromiso sensibilidad/ruido

`[MURPHY]` La formulación es clara y correcta:
- Media **muy corta** (5-10 días): sigue el precio de cerca, **muchos cruces**, más operaciones, comisiones más altas, **muchas señales falsas (whipsaws)**; el ruido aleatorio de corto plazo activa malas señales.
- Media **larga**: menos señales falsas, pero **"da mucho más cuando la tendencia cambia"**.

Y el corolario que enuncia: **"las medias más largas funcionan mejor siempre que la tendencia siga en marcha, pero una media más corta es mejor cuando la tendencia está en proceso de cambiar."**

`[MURPHY]` **"El truco está en encontrar la media que sea lo bastante sensible como para generar señales tempranas, pero lo bastante insensible como para evitar la mayor parte del ruido aleatorio."**

`[INTERPRETACIÓN]` Es exactamente el mismo compromiso que ya apareció en los filtros de ruptura (§4.9). **Murphy identifica correctamente el trade-off tres veces en el libro y nunca ofrece un criterio para resolverlo.** `[VACÍO]` La elección del período queda como parámetro libre sin criterio, y **cada período probado es un intento experimental**.

### 9.5 Las reglas operativas — y la separación que pide el encargo

Conforme a la instrucción de distinguir regla clásica de representación informativa:

**REGLAS OPERATIVAS que documenta Murphy:**

| Sistema | Regla |
|---|---|
| **Una media** | Señal de compra cuando el cierre **sobrepasa** la media. Confirmación adicional: que la línea de la media **se mueva en la dirección del cruce** |
| **Doble cruce** | Compra cuando la media corta cruza por encima de la larga. Combinaciones que cita: **5/20 y 10/50** |
| **Triple cruce (4-9-18)** | **Alerta** cuando la de 4 cruza por encima de la de 9 y la de 18; **señal confirmada** cuando la de 9 cruza por encima de la de 18, dejando la alineación 4 > 9 > 18. Atribuido a R. C. Allen (1972) |
| **Sobres (envelopes)** | Bandas a **porcentaje fijo** por encima y debajo. Ejemplos: 3% sobre SMA de 21 días (corto plazo); 5% sobre media de 10 semanas; 10% sobre 40 semanas. Alcanzar el sobre = **tendencia sobreextendida** |
| **Bandas de Bollinger** | **Dos desviaciones típicas** sobre una media de 20 días. Tocar la banda superior = sobrecomprado; la inferior = sobrevendido |
| **Bollinger como metas** | Si el precio rebota desde la banda inferior y **cruza por encima de la media de 20**, la banda superior pasa a ser el objetivo |
| **Regla de 4 semanas (Donchian)** | Comprar cuando el precio **supera el máximo de las 4 semanas anteriores completas**; vender cuando cae por debajo del mínimo. **Sistema continuo** (siempre en posición) |

**REPRESENTACIONES INFORMATIVAS derivables** `[INTERPRETACIÓN]`, sin comprometer ninguna:

- **Distancia precio-media**, preferiblemente normalizada (por la propia media o por volatilidad) para ser adimensional y comparable en el tiempo.
- **Pendiente de la media** — Murphy la usa como confirmación ("que la línea se mueva en la dirección del cruce"), lo que la convierte en una variable con contenido propio.
- **Separación entre dos medias**, que es una variable continua de la que el cruce es sólo el cruce por cero.
- **Persistencia**: número de barras consecutivas por encima o por debajo.
- **Alineación de N medias** — el sistema 4-9-18 es, informativamente, **el orden de un vector de medias**, que puede codificarse de forma continua u ordinal.
- **Ancho de banda de Bollinger** — ver §9.6.
- **Posición del precio dentro del canal de Donchian**, de la que la ruptura es sólo el valor extremo.

`[IMPLICACIÓN PARA IRIS]` La observación estructural: **cada regla operativa de Murphy es la binarización de una variable continua subyacente.** Cruce = signo de la separación. Ruptura de canal = posición relativa dentro del rango = 0 o 1. Tocar la banda = z-score ≥ 2. **Conservar la variable continua preserva información que la regla descarta**, y evita fijar el umbral. Es una reformulación nuestra, coherente con el principio general de §5.6 y §6.10.

### 9.6 Bandas de Bollinger — el ancho como medida de volatilidad

`[MURPHY]` Distinción explícita con los sobres: **los sobres mantienen un ancho porcentual constante; las Bandas de Bollinger se expanden y contraen según la volatilidad de los últimos 20 días.**

Y la afirmación clave:

> **"Hay una tendencia de las bandas a que se alternen entre expansión y contracción. Cuando las bandas están inusualmente separadas, es señal de que la tendencia actual puede estar cambiando, y cuando se han acercado mucho, es señal de que el mercado puede estar iniciando una nueva tendencia."**

`[IMPLICACIÓN PARA IRIS]` **Esta es la aportación más valiosa del capítulo y responde directamente a una pregunta heredada (§41: ¿aporta Murphy alguna forma relevante de medir contexto de volatilidad?).** Tres razones:

1. **El ancho de banda es una medida de volatilidad `OHLCV-OK`, `CAUSAL` y con un solo parámetro** (la ventana).
2. **La hipótesis de alternancia expansión/contracción es falsable y directamente comprobable**: ¿la volatilidad realizada exhibe agrupamiento y alternancia predecibles en MNQ intradiario?
3. **Es una hipótesis sobre régimen, no sobre dirección.** Dice cuándo esperar un cambio de estado, no hacia dónde. Eso la sitúa naturalmente como candidata a **variable de contexto o de filtro**, no a generadora de `side`.

`[INTERPRETACIÓN]` Y nótese la coherencia con lo hallado en §6: contracción de rango → expansión (triángulos, banderas) y expansión de rango + volumen → agotamiento (formación expansiva, descargas). **El ancho de banda de Bollinger es la versión continua y sin geometría de todos esos patrones.** Convergencia notable: media docena de figuras del libro se reducen a una única variable de volatilidad con su dinámica de alternancia.

`[MURPHY]` Añade que las bandas **"tienen su mejor rendimiento cuando se las combinan con los osciladores sobrecomprados/sobrevendidos"** del capítulo siguiente, y que la técnica es aplicable a gráficos semanales y mensuales usando 20 semanas o 20 meses.

`[INTERPRETACIÓN]` **Invariancia de escala declarada**: al ser un z-score móvil, la construcción es adimensional y se traslada mecánicamente a barras de un minuto. **Que conserve significado a esa escala es una pregunta empírica abierta.**

### 9.7 Centrado de la media

`[MURPHY]` **"La forma estadísticamente más correcta de representar una media móvil es centrarla"** — colocarla en el centro del período que cubre. Pero **tiene el inconveniente de producir señales atrasadas**, por lo que en la práctica se coloca al final. **"La técnica de centrar la media la usan casi exclusivamente los analistas cíclicos."**

`[IMPLICACIÓN PARA IRIS]` **Advertencia de causalidad crítica.** Una media centrada es **`LOOK-AHEAD-GRAVE`**: para colocar el valor de una media de 20 barras diez barras atrás, se necesitan las diez barras posteriores. Murphy la menciona como "estadísticamente más correcta", lo cual es cierto en análisis descriptivo retrospectivo, **pero la haría inutilizable en un sistema causal**. Registrado explícitamente para evitar el error. **Toda media en IRIS debe ser rezagada, nunca centrada.**

### 9.8 La regla de 4 semanas y la evidencia que Murphy aporta

Este es **el único lugar del libro donde Murphy cita resultados de pruebas sistemáticas comparativas**, y merece registrarse con precisión:

`[MURPHY]`
- **Dunn & Hargitt (1970), *Trader's Notebook***: comparó por ordenador los sistemas de contratación más conocidos. **"La conclusión final fue que el sistema de más éxito de todos los probados era el de la regla de 4 semanas, desarrollado por Richard Donchian."**
- **Lukac et al.**: de **12 sistemas examinados entre 1975 y 1984, sólo 4 generaron beneficios significativos**. De esos 4, **2 eran sistemas de canal y uno era de cruce doble de media móvil**.
- **Lukac y Brorsen (The Financial Review, noviembre 1990)**: estudio sobre 1976-86 comparando **23 sistemas técnicos**. **"Una vez más, a la cabeza de la lista aparecían los sistemas de canal y de media móvil."**
- **La conclusión de Lukac que Murphy recoge**: **"un sistema de canal de ruptura de precios era el mejor punto de partida para todas las pruebas y el desarrollo del sistema técnico de operaciones."**

`[IMPLICACIÓN PARA IRIS]` **Es la única evidencia cuantitativa de rendimiento comparativo en todo el libro, y apunta a la ruptura de canal (Donchian) y al cruce doble de medias como los sistemas más robustos.** Conviene ser preciso sobre su alcance y sus límites:

**Lo que dice**: en dos estudios independientes sobre futuros, en períodos 1975-1986, dos familias de sistemas destacaron sobre 12 y 23 competidores respectivamente.

**Lo que NO dice** `[VACÍO]`:
- No se reportan magnitudes, Sharpe, drawdown ni costes.
- **De 12 sistemas, sólo 4 fueron rentables.** Es decir, **dos tercios de los sistemas probados fracasaron** — dato que también hay que retener.
- Los períodos son de hace cuatro décadas y **anteriores a la generalización del trading algorítmico**.
- Son **futuros de materias primas en frecuencia diaria**, no un índice bursátil en intradiario.
- **No hay corrección por el número de sistemas y parámetros probados.** Un estudio que compara 23 sistemas y reporta el mejor es exactamente la estructura de selección que las fuentes anteriores identifican como generadora de falsos descubrimientos.

`[MURPHY]` **Las propiedades de la regla de 4 semanas que él destaca**: señales mecánicas y muy definidas; **"prácticamente garantiza la participación desde el lado correcto de cualquier tendencia importante"**; sigue la máxima de "deje que los beneficios sigan, pero frene rápidamente las pérdidas"; **opera con menor frecuencia, luego comisiones más bajas**.

**Y sus debilidades, que él mismo señala**: como sistema **continuo**, "permanecen en el mercado y obtienen señales equivocadas durante los períodos en los que el mercado no tiene tendencia". **La modificación que propone**: usar 4 semanas para entrar pero **una o dos semanas para liquidar**, quedando fuera del mercado hasta la siguiente ruptura de 4 semanas.

`[IMPLICACIÓN PARA IRIS]` Esa modificación es notable: **convierte un sistema siempre-en-mercado en uno con estado de no-posición**, mediante umbrales asimétricos de entrada y salida. Es una tercera vía para el "no operar", distinta de las de §4.1 (régimen lateral) y de las de la fuente anterior. **Registrada, no adoptada.**

`[MURPHY]` **Ajustes de sensibilidad**: acortar el período para mayor sensibilidad; extender a 8 semanas en bandas de fluctuación para evitar señales prematuras. Y **usar las rupturas de 1-2 semanas como filtro de confirmación de otras técnicas**, como los cruces de medias.

### 9.9 Optimización — la posición de Murphy

`[MURPHY]` Reporta que Merrill Lynch (1978-82) probó extensamente parámetros de medias y rupturas de canal **para encontrar las mejores combinaciones para cada mercado de futuros**, obteniendo **un conjunto distinto de valores optimizados para cada mercado**.

**Y su posición sobre el procedimiento correcto es explícita y metodológicamente sólida:**

> **"El meollo de la cuestión está en cómo se optimiza la información. Los investigadores resaltan que el procedimiento correcto es usar sólo parte de la información sobre precios para elegir los mejores parámetros, y otra parte para examinar los resultados. La prueba de los parámetros optimizados usando información sobre precios 'fuera de muestra' ayuda a asegurar que los resultados finales se acercarán más a lo que se podría experimentar con las operaciones reales."**

`[MURPHY]` Y una valoración cauta: **"La mayor parte de la evidencia sugiere que la optimización no es el Santo Grial que algunos creen que es."** Su consejo práctico: quien sigue pocos mercados puede experimentar con optimización; quien sigue muchos, debería usar los mismos parámetros para todos.

`[IMPLICACIÓN PARA IRIS]` **Este pasaje es sorprendentemente moderno y es la afirmación metodológica más fuerte del libro.** Murphy formula correctamente la separación in-sample / out-of-sample como requisito de la optimización. `[VACÍO]` **Lo que no aporta**: nada sobre multiple testing, sobre cuántos parámetros pueden probarse, ni sobre cómo corregir el resultado por el número de intentos. Reconoce el problema del ajuste pero no su dimensión combinatoria.

`[INTERPRETACIÓN]` Y hay una tensión con nuestro caso: su consejo de optimizar es **para quien sigue pocos mercados** — que es exactamente IRIS. Pero el argumento contrario (que optimizar sobre un solo instrumento maximiza el riesgo de sobreajustar a ese instrumento) es precisamente el que sostenía la fuente anterior. **Tensión registrada para §40; no resuelta.**

### 9.10 Media móvil adaptable de Kaufman

`[MURPHY]` Presenta la **AMA de Perry Kaufman** como solución al problema de elegir entre media rápida y lenta: **su velocidad se ajusta automáticamente al nivel de ruido (o volatilidad) del mercado**. Se mueve **más lentamente cuando el mercado es lateral y se acelera cuando hay tendencia**.

**El mecanismo**: un **coeficiente de eficiencia** que **compara la dirección del precio con el nivel de volatilidad**. Coeficiente alto = más dirección que volatilidad → media más rápida. Coeficiente bajo = más volatilidad que dirección → media más lenta.

`[IMPLICACIÓN PARA IRIS]` **El coeficiente de eficiencia es, por sí solo, uno de los conceptos más interesantes del capítulo para nosotros**, con independencia de la media adaptativa que lo usa:

- Es **`OHLCV-OK`** y **`CAUSAL`**.
- Tiene **un solo parámetro** (la ventana).
- Es **adimensional** — un ratio entre desplazamiento neto y camino recorrido — por tanto **invariante de escala y comparable entre regímenes**.
- **Mide exactamente lo que el encargo pregunta bajo el nombre "eficiencia del movimiento"** en la lista de posibles formalizaciones de tendencia (§11 del encargo).
- **Distingue tendencia de lateralidad de forma continua**, que es precisamente la variable que Murphy usa cualitativamente en todo el libro ("mercado con tendencia" vs "mercado lateral") **y que nunca define de otro modo**.

`[INTERPRETACIÓN]` Es la respuesta más concreta que el libro ofrece a la pregunta *"¿puede el concepto de tendencia convertirse en una variable cuantitativa?"* — no como dirección, sino como **grado de tendencialidad**. Registrado como candidato conceptual de alta prioridad. **No se adopta.**

### 9.11 Medias móviles unidas a ciclos y armonía

`[MURPHY]` Sostiene que existe una relación entre los ciclos dominantes de un mercado y las medias móviles correctas a usar, y que **el ciclo de 4 semanas (20 días) es un ciclo dominante que influye en todos los mercados**, lo que podría explicar el éxito del período de 4 semanas. Menciona el **principio de armonía**: cada ciclo está relacionado con sus vecinos por un factor 2 (de ahí 1, 2, 4, 8 semanas). También menciona **números de Fibonacci usados como medias móviles**.

`[INTERPRETACIÓN]` Esta es una **racionalización a posteriori**: se observa que 4 semanas funciona bien y se postula un ciclo de 4 semanas para explicarlo. **El argumento es circular** y el propio Murphy lo presenta con cautela ("puede ayudar a explicar"). Se desarrolla en §24 (ciclos).

### 9.12 El límite declarado de las medias móviles

`[MURPHY]` Cierra el capítulo con una limitación explícita:

> **"Las medias móviles no funcionan siempre. Logran sus mejores resultados cuando el mercado está en fase de seguir una tendencia. No son muy útiles durante los períodos sin tendencia, que es cuando los precios operan lateralmente. Por suerte, hay otra clase de indicador que funciona mucho mejor... Se llaman osciladores."**

`[IMPLICACIÓN PARA IRIS]` **Esta es la formulación más explícita de una hipótesis de régimen en todo el libro**: *el instrumento apropiado depende del estado del mercado*. Medias móviles en tendencia, osciladores en lateralidad. Es directamente relevante para la pregunta de IRIS sobre condiciones de abstención y sobre selección condicional de señales. **Y es falsable.** Se registra; ver §19 y §37.

### 9.13 Clasificación del capítulo 9

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| SMA / EMA / WMA | **`OHLCV-OK`** | **`CAUSAL`** | 1–2 (período, tipo) | **Murphy: sin evidencia de que EMA supere a SMA** |
| Elección de la serie de entrada (C, (H+L)/2, (H+L+C)/3) | `OHLCV-OK` | `CAUSAL` | 1 | GL frecuentemente ignorado |
| **Media centrada** | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | — | **Nunca usable causalmente** |
| Cruce simple / doble / triple | `OHLCV-OK` | `CAUSAL` | 1–3 | Binarización de una variable continua |
| **Distancia precio-media normalizada** | `OHLCV-OK` | `CAUSAL` | 1–2 | Representación continua |
| **Pendiente de la media** | `OHLCV-OK` | `CAUSAL` | 1–2 | Murphy la usa como confirmación |
| Sobres de porcentaje fijo | `OHLCV-OK` | `CAUSAL` | 2 | Ancho constante |
| **Bandas de Bollinger** | `OHLCV-OK` | `CAUSAL` | 2 | Ancho adaptado a volatilidad |
| **Ancho de banda como medida de volatilidad** | **`OHLCV-OK`** | **`CAUSAL`** | **1** | **Hipótesis de alternancia falsable** |
| **Canal de Donchian / regla de 4 semanas** | **`OHLCV-OK`** | **`CAUSAL`** | **1–2** | **Único con evidencia comparativa citada** |
| Regla 4 semanas con salida a 1-2 semanas | `OHLCV-OK` | `CAUSAL` | 2 | **Genera estado de no-posición** |
| **Coeficiente de eficiencia (Kaufman)** | **`OHLCV-OK`** | **`CAUSAL`** | **1** | **Tendencialidad como variable continua** |
| Media móvil adaptable | `OHLCV-OK` | `CAUSAL` | 2–3 | Construida sobre el coeficiente |
| Optimización in/out-of-sample | — | — | — | **Metodológicamente correcta; sin multiple testing** |
| Medias ligadas a ciclos / Fibonacci | `OHLCV-OK` | `CAUSAL` | Alto | Racionalización circular |
| **Régimen determina el instrumento** | — | — | — | **Hipótesis falsable de alto valor** |


---

## 10. OSCILADORES E IMPULSO (Cap. 10 — Nivel A)

### 10.1 El encuadre: subordinación explícita a la tendencia

`[MURPHY]` **"El oscilador es sólo un indicador secundario, en el sentido de que debe subordinarse al análisis básico de tendencias."**

Y una afirmación de aplicabilidad condicional que es central:

> **"Cerca del principio de movimientos importantes, el análisis del oscilador no es muy útil y puede incluso llevarnos en la dirección equivocada. En cambio, hacia el final de los movimientos de un mercado, los osciladores se vuelven extremadamente útiles."**

`[IMPLICACIÓN PARA IRIS]` Esta es la segunda formulación explícita de una **hipótesis de régimen** (la primera fue medias-en-tendencia / osciladores-en-lateral, §9.12). Aquí el condicionante no es el tipo de mercado sino **la fase de madurez del movimiento**. `[INTERPRETACIÓN]` Y aquí está el problema: **"principio" y "final" de un movimiento sólo se conocen cuando el movimiento ha terminado.** La condición de aplicabilidad del oscilador es, en su formulación literal, `LOOK-AHEAD-GRAVE`. Registrado como tensión (§38).

### 10.2 Estructura común e interpretación general

`[MURPHY]` **"Aunque hay muchas formas diferentes de construir osciladores de ímpetu, su interpretación difiere muy poco de una técnica a otra. Casi todos los osciladores se parecen mucho."**

`[IMPLICACIÓN PARA IRIS]` **Esta frase del propio autor es la respuesta más directa a la pregunta del encargo (§19 y §36) sobre si los osciladores aportan dimensiones informativas distintas o son transformaciones redundantes.** Murphy afirma la similitud en la *interpretación*; no la analiza en términos de información. Se desarrolla en §10.11 y §36.

**Los tres usos que declara comunes a casi todos:**
1. **Lectura extrema** cerca del límite superior (sobrecomprado) o inferior (sobrevendido): advertencia de que la tendencia está **sobreextendida y es vulnerable**.
2. **Divergencia** entre oscilador y precio cuando el oscilador está en posición extrema: **"generalmente es una advertencia importante"**.
3. **Cruce de la línea cero** (o media): señales para operar **en la dirección de la tendencia**.

### 10.3 Momento (momentum)

`[MURPHY]` **Fórmula: `M = V − Vx`**, donde V es el último cierre y Vx el cierre de hace x períodos. Es una **diferencia**, representada alrededor de una línea cero.

**Qué mide, explicado con precisión:** **"El momento mide la velocidad del cambio de precios en oposición al nivel de precios en sí."** El desarrollo que hace es el punto clave del capítulo:
- Línea de momento por encima de cero y ascendente → la tendencia alcista **se está acelerando**.
- Línea que se aplana → las ganancias recientes igualan las de hace x períodos; **aunque los precios sigan subiendo, la velocidad se ha estabilizado**.
- Línea que cae hacia cero → la tendencia sigue vigente pero **pierde momento**.
- Cruce por debajo de cero → el último cierre está por debajo del de hace x períodos.

`[MURPHY]` Y la observación de equivalencia: **"(Por cierto, la media móvil de 10 días también ha comenzado a bajar)"** — reconoce que el cruce de cero del momento de 10 días coincide con un giro de la media de 10 días.

`[MURPHY]` **La afirmación predictiva:**
> **"Por la forma en que está construida, la línea del momento siempre está un paso por delante del movimiento del precio. Encabeza el avance o el retroceso de los precios, luego se estabiliza mientras la tendencia actual del precio está todavía en efecto, y finalmente comienza a moverse en la dirección opuesta cuando los precios comienzan a estabilizarse."**

`[INTERPRETACIÓN]` **Esta afirmación es matemáticamente trivial, no empírica.** El momento es una diferencia primera: por construcción alcanza su máximo cuando la velocidad es máxima, lo que ocurre necesariamente antes del máximo del nivel. **Decir que "el momento se adelanta al precio" es decir que la derivada se anula antes que la función alcanza su extremo.** No es una propiedad descubierta del mercado; es una propiedad del operador diferencia. `[IMPLICACIÓN PARA IRIS]` **Esto no la hace inútil, pero sí impide tratarla como evidencia de capacidad predictiva.** La pregunta empírica real —¿la desaceleración observada predice la reversión?— es distinta y el libro no la aborda.

`[MURPHY]` **Determinación de los límites extremos**: **"La forma más sencilla de solucionar este problema es con la inspección visual. Compruebe la historia anterior de la línea del momento y trace líneas horizontales a lo largo de sus límites superior e inferior. Estas líneas se tendrán que ajustar periódicamente."**

`[IMPLICACIÓN PARA IRIS]` **Punto crítico de causalidad.** Los umbrales de sobrecompra/sobreventa del momento **no están normalizados** y se fijan por inspección visual del histórico, ajustándose periódicamente. Eso es:
- **`LOOK-AHEAD-GRAVE`** si los umbrales se trazan mirando toda la serie.
- Formalizable causalmente **sólo** sustituyendo la inspección visual por un **cuantil móvil calculado sobre ventana pasada**, lo que introduce dos parámetros nuevos (ventana y cuantil). Reformulación nuestra.
- **La razón de fondo**: el momento como diferencia absoluta **no es adimensional** — depende del nivel de precio y de la volatilidad, y por eso sus límites deben reajustarse. Este defecto es precisamente lo que motiva los osciladores acotados (§10.5).

### 10.4 Tasa de cambio (TDC / ROC)

`[MURPHY]` **Fórmula: `TDC = 100 × (V / Vx)`**. La línea media es 100. Es la versión **cociente** del momento, que es la versión **diferencia**.

`[MURPHY]` Nota práctica: los programas usan a veces variaciones de las fórmulas, **"pero aunque las técnicas pueden variar, la interpretación sigue siendo la misma"**.

`[INTERPRETACIÓN]` **Momento y TDC son la misma información en escalas distintas**: uno es `P_t − P_{t−x}`, el otro `P_t / P_{t−x}`. Para variaciones pequeñas, el log del segundo es aproximadamente proporcional al primero dividido por el precio. **La TDC tiene la ventaja de ser adimensional respecto al nivel de precio** (aunque no respecto a la volatilidad). **No son dos fuentes de información: son dos normalizaciones de una.**

### 10.5 Oscilador de dos medias móviles (histograma)

`[MURPHY]` Se representa **la diferencia entre dos medias** como histograma alrededor de una línea cero. **Tres usos declarados:**
1. Detectar divergencias.
2. Identificar cuando la media corta se desplaza **muy por encima o muy por debajo** de la larga.
3. **Señalar con precisión los cruces de las dos medias**, que ocurren cuando el oscilador cruza cero.

`[MURPHY]` Y el racional de reversión: **"Cuando las líneas de ambas medias se separan demasiado, se crea una situación extrema del mercado que requiere una pausa en la tendencia."**

`[IMPLICACIÓN PARA IRIS]` **Confirmación explícita, por el propio autor, de la tesis de §9.5**: el cruce de medias **es** el cruce por cero de una variable continua (la separación), y **conservar la variable continua da estrictamente más información que el cruce**. Murphy lo formula al decir que el histograma "cambia mucho antes que las señales reales".

### 10.6 Índice del Canal de Mercancías (ICM / CCI)

`[MURPHY]` De Donald Lambert. **Compara el precio actual con una media móvil (normalmente 20 días) y normaliza los valores usando un divisor basado en una desviación media.** Resultado: fluctúa en **banda constante de +100 a −100**.

**Dos interpretaciones incompatibles que Murphy documenta:**
- **La original de Lambert**: posiciones **largas** por encima de +100, cortas por debajo de −100. Es decir, **seguimiento de ruptura**.
- **La de la mayoría de los chartistas**: por encima de +100 = **sobrecomprado**, por debajo de −100 = **sobrevendido**. Es decir, **reversión**.

`[IMPLICACIÓN PARA IRIS]` **Este es el caso más nítido del libro de una misma variable con dos reglas operativas de signo opuesto.** Es la misma situación que en los rectángulos (§6.6), pero aquí sobre un indicador cuantitativo exacto. **Demuestra que la variable (A) no determina la regla (C)**, y que el paso intermedio (B) —qué predice realmente un valor extremo del CCI— no está resuelto en la fuente. `[VACÍO]`

`[INTERPRETACIÓN]` Estructuralmente, **el CCI es un z-score móvil del precio respecto a su media**, usando desviación media en lugar de desviación típica. **Es, por tanto, casi la misma información que la posición dentro de las Bandas de Bollinger** (§9.6), que es el z-score con desviación típica. Dos indicadores con nombres distintos, autores distintos y capítulos distintos, midiendo casi lo mismo.

### 10.7 Índice de Fuerza Relativa (IFR / RSI)

`[MURPHY]` De J. Welles Wilder (1978). **Y su motivación está declarada explícitamente**, lo que es valioso:

> **Problema 1 del momento**: **"el movimiento errático causado con frecuencia por cambios bruscos en los valores que se dejan de lado. Un fuerte avance o retroceso hace 10 días puede causar cambios repentinos en la línea del momento incluso si los precios actuales no muestran modificaciones."**
> **Problema 2**: **"existe la necesidad de una banda constante a efectos comparativos."**

**Fórmula:** `IFR = 100 − 100/(1+FR)`, donde `FR = media de cierres al alza de x días / media de cierres a la baja de x días`. Wilder usó **14 períodos**.

`[MURPHY]` Aclara además que **el nombre es inapropiado**: "fuerza relativa" normalmente designa un cociente entre dos entidades distintas (un valor contra el S&P 500), y **el IFR de Wilder no mide fuerza relativa entre entidades**.

**Interpretación:**
- Escala 0–100. **>70 sobrecomprado, <30 sobrevendido.**
- **"Debido al desplazamiento que tiene lugar en los mercados alcistas y bajistas, el nivel 80 generalmente se transforma en el nivel sobrecomprado en los mercados alcistas y el nivel 20 en el sobrevendido en los bajistas."**
- **El nivel 50** sirve a menudo de apoyo en retrocesos y resistencia en recuperaciones; algunos operadores usan sus cruces como señales.
- Períodos alternativos que menciona: 9, 5, 7 (más volátil), 21, 28 (más suave).

`[MURPHY]` **Oscilaciones de fracaso (failure swings)**, el concepto propio de Wilder: ocurren cuando el IFR está por encima de 70 o por debajo de 30. **Por abajo**: el segundo valle del IFR es más alto que el primero mientras está bajo 30 **y los precios siguen cayendo**; la penetración al alza del pico intermedio del IFR indica un mínimo. **Por arriba**: el espejo.

`[MURPHY]` **Y su valoración personal, que es una toma de posición explícita:**
> **"En mi propia experiencia personal con el oscilador del IFR, su mayor valor radica en las oscilaciones de fracaso o divergencias que tienen lugar cuando el IFR está por encima de 70 o por debajo de 30."**

**La advertencia más importante del capítulo:**
> `[MURPHY]` **"Cualquier tendencia fuerte, al alza o a la baja, normalmente produce una lectura de oscilador extrema antes de que pase mucho tiempo. En tales casos, decir que un mercado está sobrecomprado o sobrevendido suele ser prematuro y puede llevar a una salida anticipada de una tendencia rentable. En tendencias al alza fuertes, los mercados sobrecomprados pueden permanecer así durante algún tiempo."**

Y la regla que deriva: **el primer movimiento a zona extrema es sólo una advertencia; la señal a vigilar es el segundo movimiento**, y si éste no confirma un nuevo extremo de precio, hay posible divergencia.

`[IMPLICACIÓN PARA IRIS]` Tres puntos:
1. **El IFR sí resuelve un problema real que el momento tiene**: acotación y suavizado. Es una mejora estructural, no cosmética.
2. **Pero "sobrecomprado" no significa "va a bajar"** — el propio autor lo dice. La lectura extrema es una **condición de estado**, no una señal direccional. Categoría (A), no (B).
3. **El desplazamiento de umbrales (70/30 → 80/20 según el mercado) es un parámetro dependiente del régimen que Murphy no operacionaliza.** `[VACÍO]` ¿Cómo se sabe causalmente si estamos en un "mercado alcista" para saber qué umbral aplicar? Circularidad.

### 10.8 Estocástico (%K / %D)

`[MURPHY]` De George Lane. **Basado en una observación estructural concreta y falsable**:

> **"A medida que los precios se incrementan, los precios de cierre tienden a acercarse más al extremo superior de la banda de precios. Por el contrario, en las tendencias a la baja, el precio de cierre tiende a acercarse al extremo inferior."**

**Fórmula:** `%K = 100 × (C − L14) / (H14 − L14)`. Mide **en base porcentual dónde está el cierre dentro del rango total** del período. `%D` es una media móvil de 3 períodos de `%K` (versión rápida); una media adicional de 3 produce la **estocástica lenta**, que **"casi todos los operadores prefieren debido a que sus señales son de mayor confianza"**.

**Interpretación**: extremos en 80 y 20. **La señal principal es la divergencia entre la línea %D y el precio cuando %D está en zona extrema**; la señal de operación se dispara cuando **%K cruza %D**.

`[MURPHY]` **Y una nota de escala directamente relevante**: **"El oscilador estocástico se puede usar con gráficos semanales y mensuales... pero también se puede usar de forma eficaz con gráficos intradía de operaciones a más corto plazo."**

`[IMPLICACIÓN PARA IRIS]` **El estocástico es, de todos los osciladores del capítulo, el que tiene la construcción más distinta:**
- **Usa High y Low, no sólo cierres** — es el único que incorpora el rango.
- Es **intrínsecamente adimensional y acotado por construcción** (posición relativa dentro de un rango), sin necesidad de normalización adicional.
- **Su premisa es una hipótesis empírica concreta y comprobable**: ¿tiende el cierre a situarse en el extremo superior del rango durante tendencias alcistas en MNQ intradiario?
- `OHLCV-OK`, `CAUSAL`, dos parámetros (ventana y suavizados).
- **Murphy declara explícitamente su aplicabilidad intradiaria**, cosa que hace con muy pocas técnicas.

`[INTERPRETACIÓN]` Nótese además que `%K` es **exactamente la posición del precio dentro del canal de Donchian** (§9.8) expresada en porcentaje. **El sistema de ruptura de canal y el estocástico son la misma variable**: la ruptura es `%K = 100`, y el estocástico es su versión continua. **Una de las convergencias más significativas del libro**, y llega desde dos capítulos y dos autores distintos.

### 10.9 Williams %R

`[MURPHY]` **"Se basa en un concepto similar"**: el cierre se resta del máximo de la banda y se divide entre la banda total. **Es el estocástico invertido**, y por eso los programas ofrecen una versión invertida para corregirlo.

`[INTERPRETACIÓN]` **Redundancia exacta declarada por el propio autor.** `%R = 100 − %K`. **No es una fuente de información adicional; es una transformación afín del estocástico.** Es el ejemplo más limpio del problema de sustitución que preocupa al encargo.

### 10.10 CDMM / MACD e histograma

`[MURPHY]` De Gerald Appel. **Tres líneas en el cálculo, dos visibles:**
- **Línea CDMM (rápida)**: diferencia entre dos medias exponenciales de cierres, normalmente **12 y 26** períodos.
- **Línea de señal (lenta)**: media exponencial de **9 períodos** de la línea CDMM.
- **"La mayoría de los operadores utiliza los valores de 12, 26 y 9 en todos los casos."**

**Interpretación híbrida, que Murphy subraya:** los cruces entre las dos líneas dan señales **como el doble cruce de medias**; pero los valores fluctúan alrededor de cero, lo que **"comienza a parecerse a un oscilador"**, con lecturas extremas de sobrecompra/sobreventa. **"Las mejores señales aparecen cuando los precios están bien por debajo de la línea cero (sobrevendidos)."** Los cruces de la línea cero son otra fuente de señales.

**Histograma CDMM**: barras verticales que miden **la diferencia entre las dos líneas CDMM**, con su propia línea cero.
> `[MURPHY]` **"El verdadero valor del histograma es detectar cuándo se estrecha o se amplía la diferencia entre las dos líneas... los cambios del histograma proporcionan advertencias más tempranas de que la tendencia actual está perdiendo momento. Los cambios en el histograma para dirigirse otra vez a la línea cero siempre preceden las señales de cruces."**

Y la advertencia: **"Es mucho más peligroso usar los cambios del histograma como excusa para iniciar nuevas posiciones en contra de la tendencia prevaleciente"** — sirven para **salidas tempranas**, no para entradas contrarias.

`[INTERPRETACIÓN]` **El MACD es la diferencia de dos EMAs; el histograma es la derivada suavizada de esa diferencia.** Es decir: **la segunda derivada del precio, suavizada dos veces.** Y la observación de Murphy de que "siempre precede las señales de cruce" es, otra vez, **una propiedad matemática de las derivadas, no un hallazgo empírico** (§10.3).

`[IMPLICACIÓN PARA IRIS]` La distinción funcional que sí es sustantiva y útil: **el histograma sirve como señal de salida pero no de entrada contraria.** Eso es una asimetría operativa concreta, y es coherente con la subordinación general del oscilador a la tendencia.

### 10.11 Redundancia informativa entre osciladores — respuesta a la pregunta del encargo

`[INTERPRETACIÓN]` Reuniendo lo anterior, se puede responder la pregunta del encargo (§19: *¿dimensiones informativas diferentes o transformaciones redundantes?*) con considerable precisión, y la respuesta es matizada:

**Grupo 1 — Diferencia/cociente sobre cierres (misma información, distinta normalización):**
- Momento (`P_t − P_{t−x}`)
- TDC/ROC (`P_t / P_{t−x}`)
- Cruce de dos medias / histograma de medias
- CDMM y su histograma (diferencia de EMAs y su derivada)

Todos derivan de **la variación del precio de cierre sobre una ventana**, con distintos esquemas de ponderación y de escalado. `[MURPHY]` mismo señala equivalencias parciales (momento de 10 días ↔ giro de la media de 10 días; CDMM ↔ doble cruce).

**Grupo 2 — Posición relativa dentro de un rango (misma información):**
- Estocástico `%K`
- Williams `%R` (= `100 − %K`, redundancia exacta y declarada)
- Posición dentro del canal de Donchian (§9.8)

**Grupo 3 — Desviación normalizada respecto a una referencia central:**
- CCI (z-score con desviación media respecto a SMA)
- Posición dentro de Bandas de Bollinger (z-score con desviación típica)
- Sobres porcentuales (desviación con umbral fijo)

**Grupo 4 — Asimetría de ganancias y pérdidas:**
- **IFR/RSI** — es el único que separa explícitamente los movimientos al alza de los movimientos a la baja y calcula un cociente entre sus magnitudes medias.

`[INTERPRETACIÓN]` **Conclusión provisional**: los aproximadamente diez osciladores del capítulo se reducen a **cuatro familias informativas**, y sólo dos de ellas (grupo 2 y grupo 4) usan información que no está en la simple variación de cierres — el grupo 2 usa High y Low, el grupo 4 usa la descomposición asimétrica. **Esto es interpretación nuestra, derivada de la construcción de las fórmulas, no una afirmación de Murphy** — aunque él declara que "casi todos los osciladores se parecen mucho".

**Y una advertencia sobre el alcance de esta conclusión**: dos indicadores pueden estar altamente correlacionados y aun así no ser intercambiables si su relación con el objetivo es no lineal o depende del régimen. **La redundancia estructural es un indicio fuerte, no una demostración.** La verificación empírica corresponde a etapas posteriores.

### 10.12 Divergencias — análisis del concepto (respuesta a §20 del encargo)

Recopilando de este capítulo, §6.9 y §7.2.

`[MURPHY]` **Variantes que documenta:**

| Divergencia | Variables comparadas | Dónde |
|---|---|---|
| Precio ↔ oscilador de impulso | Extremos de precio vs extremos del oscilador **en zona extrema** | Cap. 10 |
| Precio ↔ volumen | Nuevo máximo de precio **con volumen en declive** | Cap. 7 |
| Precio ↔ OBV/VTA | La línea acumulada no sigue la dirección del precio | Cap. 7 |
| Precio ↔ CDMM | Líneas CDMM se debilitan mientras el precio sube | Cap. 10 |
| Entre índices | Un promedio no confirma al otro | Cap. 2 (`OTRAS FUENTES`) |
| Oscilación de fracaso | Estructura **interna del oscilador**, sin comparar con el precio | Cap. 10 |

**Cómo se seleccionan los extremos:** `[MURPHY]` mediante **picos y valles sucesivos** del precio y del oscilador. Requisito adicional: **el oscilador debe estar en zona extrema (>70/<30, >80/<20)** para que la divergencia cuente.

**Cuándo se confirma:** `[MURPHY]` **"Si el oscilador se mueve en la dirección opuesta, superando un máximo o un mínimo previo, se confirma la existencia de una divergencia o una oscilación de fracaso."** Es decir, **la confirmación exige un evento posterior en el propio oscilador**.

`[IMPLICACIÓN PARA IRIS]` **Análisis de causalidad y subjetividad, punto por punto:**

1. **Requiere identificar dos picos (o valles) en el precio y dos en el oscilador.** Hereda íntegro el problema de pivotes de §4.7: **`LOOK-AHEAD-LEVE`**, formalizable sólo declarando `k` barras de confirmación.
2. **Requiere emparejar los extremos del precio con los del oscilador.** Y aquí hay un grado de libertad adicional no trivial: **los extremos del oscilador no coinciden temporalmente con los del precio** (esa es precisamente la razón de ser del indicador). ¿Qué ventana de tolerancia define que un pico del oscilador "corresponde" a un pico del precio? `[VACÍO]` **Murphy no lo especifica.**
3. **Requiere un umbral de "zona extrema"**, que es otro parámetro y que además Murphy declara variable según el régimen (70/30 vs 80/20).
4. **La confirmación es `CAUSAL-CONF`**: existe, pero llega con retardo estructural.
5. **La subjetividad reside en (1) y (2)**, no en el cálculo del oscilador, que es exacto.

`[INTERPRETACIÓN]` **Formalización causal posible, como reconstrucción nuestra**: en lugar de comparar extremos discretos, medir de forma continua **la discrepancia entre la variación del precio y la variación del oscilador sobre una ventana móvil** — por ejemplo, el signo de la diferencia entre el cambio del precio y el cambio del oscilador normalizados. Esto sería `CAUSAL` sin retardo, con un parámetro (la ventana), y **conservaría el contenido informativo sin requerir detección de pivotes**. Pero **no es la divergencia de Murphy**: es un objeto distinto cuya relación con el concepto original tendría que verificarse.

**Y la observación de fondo, que conecta con §6.9:** si los osciladores son mayoritariamente transformaciones del mismo historial de precios (§10.11), entonces **una divergencia entre precio y oscilador es una relación entre una serie y una función de sí misma** — no entre dos fuentes independientes. Eso no la invalida (mide un cambio en la estructura interna de la serie), pero **sí acota lo que puede significar**: no es evidencia corroborante externa.

### 10.13 Elección de períodos y ciclos

`[MURPHY]` **"La duración del oscilador se puede relacionar con los ciclos del mercado subyacente. Se usa un período de la mitad de la duración del ciclo."** Períodos comunes 5, 10 y 20 días, basados en ciclos naturales de 14, 28 y 56 días. **El IFR de Wilder usa 14, que es la mitad de 28.** Y sostiene que 28 días naturales (20 de contratación) representan **un ciclo mensual dominante**.

`[INTERPRETACIÓN]` Misma racionalización circular que en §9.11: se observa que 14 funciona y se postula un ciclo de 28 para explicarlo. **Y hay un problema adicional**: 14 días es la mitad de 28 días *naturales*, pero el IFR se calcula sobre días de *contratación*. La correspondencia numérica requiere mezclar dos calendarios. `[VACÍO]` No hay justificación independiente del ciclo de 28 días en este capítulo; se remite al capítulo 14.

### 10.14 La regla de subordinación y los momentos de mayor utilidad

`[MURPHY]` **La regla operativa maestra del capítulo:**
> **"La mayor parte de las señales de compra del oscilador funciona mejor en las tendencias alcistas, y las señales de venta del oscilador son más rentables en las tendencias a la baja... Compre cuando el mercado esté sobrevendido en una tendencia alcista. Venda al descubierto cuando el mercado esté sobrecomprado en una tendencia bajista."**

Y la advertencia: **"El peligro de darle demasiada importancia a los osciladores por sí mismos es la tentación de usar la divergencia como excusa para iniciar operaciones contrarias a la tendencia general. Esta acción normalmente resulta costosa y dolorosa."**

`[MURPHY]` **El dilema de la ruptura**, que documenta explícitamente: en mercados laterales, precio y oscilador se mueven juntos; cuando llega la ruptura, **el oscilador ya está en posición extrema en el mismo momento en que la ruptura ocurre**. ¿Comprar la ruptura alcista con oscilador sobrecomprado?

**Su respuesta**: **"En tales casos, es mejor ignorar el oscilador por el momento y tomar la posición."** Razón: en las primeras etapas de una nueva tendencia los osciladores alcanzan extremos muy rápido y se quedan ahí. **"Preste menos atención al oscilador en las primeras etapas de un movimiento importante, pero preste mucha atención a las señales que hace a medida que los movimientos alcanzan la madurez."**

`[IMPLICACIÓN PARA IRIS]` **Este pasaje es de los más importantes del capítulo y merece registrarse como problema, no como solución.** Murphy identifica una situación en la que **dos de sus propias herramientas dan señales opuestas simultáneamente** (ruptura alcista vs oscilador sobrecomprado), y la resuelve con una regla jerárquica ("la tendencia manda") condicionada a una variable —la madurez del movimiento— **que no es observable causalmente**.

**Lo que sí es aprovechable:** la observación de que **la relación entre el valor extremo de un oscilador y el retorno futuro cambia de signo según el contexto** (en lateral, reversión; en ruptura, continuación). Eso es una **hipótesis de interacción falsable**, y es exactamente el tipo de relación no lineal condicionada al régimen que un modelo puede aprender **sin necesidad de que nosotros especifiquemos la regla**. `[INTERPRETACIÓN]`

### 10.15 Combinación semanal-diaria

`[MURPHY]` **"La mejor forma de combinarlos es usar señales semanales para determinar la dirección del mercado y señales diarias para afinar los puntos de entrada y salida. La señal diaria se sigue sólo cuando coincide con la señal semanal, y usadas de esa forma, las señales semanales se transforman en filtros de tendencia para las señales diarias."** Señala que esto es especialmente cierto para CDMM y estocástico.

`[IMPLICACIÓN PARA IRIS]` **Tercera formulación de la arquitectura de escalas asimétricas** (tras §1.5 y §8.4), y la más operativa: **escala larga como filtro, escala corta como disparador, con regla de coincidencia obligatoria.** Es formalizable, `OHLCV-OK` y `CAUSAL`. Las escalas concretas (semanal/diario) no son transferibles; **la estructura sí**. Registrada en §33.

### 10.16 Opinión Contraria y sentimiento

`[MURPHY]` La describe como **"una forma de análisis psicológico"** que añade un tercer elemento al análisis. Mide el grado de posicionamiento alcista o bajista entre participantes. Fuentes que cita: Investors Intelligence (sondeo semanal de asesores; **>55% alcistas = demasiado optimismo, negativo; <35% = demasiado pesimismo, positivo**), índice de consenso alcista, índice AAII, y el porcentaje de valores por encima de sus medias de 10 y 30 semanas (>70% sobrecomprado, <30% sobrevendido).

**Regla de combinación**: operar en la dirección del consenso **hasta alcanzar un extremo**, momento en que se vigilan las herramientas técnicas convencionales (ruptura de soportes, líneas, medias) para confirmar el cambio.

**Clasificación: `OTRAS FUENTES`.** Sondeos de sentimiento, publicación semanal, específicos de renta variable. **No construibles desde OHLCV. No se propone incorporarlos.**

`[IMPLICACIÓN PARA IRIS]` Lo que se renuncia: una medida de posicionamiento **genuinamente independiente del precio**. `[INTERPRETACIÓN]` Es, junto con el interés abierto (§7.6) y la confirmación entre índices (§2), **la tercera fuente de información no derivada del precio que el libro considera valiosa y que nuestra restricción de datos excluye**. Las tres comparten la misma función: aportar corroboración desde un canal distinto. Documentado como limitación en §39.

### 10.17 Clasificación del capítulo 10

| Concepto | Datos | Causalidad | GL | Familia informativa | Observación |
|---|---|---|---|---|---|
| **Momento** | `OHLCV-OK` | `CAUSAL` | 1 | Variación de cierres | **No acotado; umbrales por inspección visual = look-ahead si no se sustituye por cuantil móvil** |
| **TDC / ROC** | `OHLCV-OK` | `CAUSAL` | 1 | Variación de cierres | Versión cociente del momento |
| Histograma de dos medias | `OHLCV-OK` | `CAUSAL` | 2 | Variación de cierres | El cruce es su paso por cero |
| **CCI / ICM** | `OHLCV-OK` | `CAUSAL` | 1–2 | Desviación normalizada | **Dos interpretaciones de signo opuesto** |
| **IFR / RSI** | `OHLCV-OK` | `CAUSAL` | 1–2 | **Asimetría alza/baja** | Acotado; resuelve defectos reales del momento |
| Oscilación de fracaso | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | 3+ | — | Estructura interna del oscilador |
| **Estocástico %K/%D** | **`OHLCV-OK`** | **`CAUSAL`** | 2–3 | **Posición en rango (usa H y L)** | **Premisa falsable; aplicabilidad intradiaria declarada** |
| Williams %R | `OHLCV-OK` | `CAUSAL` | 1 | Posición en rango | **= 100 − %K. Redundancia exacta** |
| **CDMM / MACD** | `OHLCV-OK` | `CAUSAL` | 3 | Variación de cierres | Híbrido cruce/oscilador |
| Histograma CDMM | `OHLCV-OK` | `CAUSAL` | 3 | Variación de cierres | Útil para salida, no para entrada contraria |
| Umbrales sobrecompra/sobreventa | `OHLCV-OK` | `CAUSAL` | 1–2 | — | **Desplazables según régimen; circularidad** |
| **Divergencia (todas las variantes)** | `OHLCV-OK` | **`LOOK-AHEAD-LEVE`** | **≥4** | — | **Emparejamiento de extremos no especificado** |
| Períodos ligados a ciclos | `OHLCV-OK` | `CAUSAL` | — | — | Racionalización circular |
| **Subordinación a la tendencia** | — | — | — | — | **Regla jerárquica condicionada a variable no observable** |
| Filtro semanal / disparo diario | `OHLCV-OK` | `CAUSAL` | 2+ | — | **Arquitectura de escalas asimétricas** |
| Opinión Contraria / sentimiento | **`OTRAS FUENTES`** | — | — | — | Sondeos semanales; no derivable de OHLCV |


---

## 11. GRÁFICOS DE PUNTOS Y FIGURAS (Cap. 11 — Nivel C)

### 11.1 El principio: eliminar el tiempo del eje

`[MURPHY]` Fue **la primera técnica de gráficos utilizada por los operadores bursátiles**, a finales del siglo XIX. Se representa mediante **columnas alternas de x (precios ascendentes) y o (precios descendentes)**. **Cada vez que una columna de x sube un espacio por encima de una columna de x previa, hay una ruptura al alza**; y simétricamente a la baja.

`[MURPHY]` **La ventaja que declara**: **"estas rupturas son mucho más precisas que las reflejadas en el gráfico de barras"**, con **"una mayor precisión y facilidad para reconocer señales de tendencias"**.

`[INTERPRETACIÓN]` **La idea estructural, despojada de la notación x/o, es la siguiente: el muestreo se realiza en función del movimiento del precio, no del paso del tiempo.** Un período de baja actividad no genera columnas nuevas; un movimiento amplio genera muchas. Es decir, **el reloj se sustituye por un criterio de desplazamiento de precio**.

`[IMPLICACIÓN PARA IRIS]` Esta es la aportación conceptualmente más relevante del capítulo, y **es la única técnica del libro que cuestiona el muestreo cronológico**. Registrada como tal. Conviene ser preciso sobre su alcance: Murphy la presenta como una **técnica de representación gráfica**, no como una teoría del muestreo; el argumento a favor es de nitidez visual de las señales, no estadístico.

### 11.2 Los dos parámetros y su efecto

`[MURPHY]` **Dos formas de variar el gráfico:**
1. **Tamaño del registro (caja)**: cuánto debe moverse el precio para marcar una x o una o.
2. **Criterio de inversión**: cuántos registros en dirección contraria hacen falta para abrir columna nueva. **"Cuanto mayor sea el número de registros necesarios para que haya una inversión, menos sensible será el gráfico."**

**El ejemplo cuantitativo que da** sobre el mismo período del S&P 500:
- Registro de **5 puntos**, inversión 3 → **44 columnas**.
- Registro de **10 puntos** → **16 columnas**. "Menos señales, pero permite concentrarse en la tendencia principal e ignorar las señales de corto plazo."
- Registro de **3 puntos** → la última subida se separa en **11 columnas**, produciendo **6 señales de compra** donde el gráfico de 10 puntos no daba ninguna.

`[MURPHY]` **"Lo esencial es que se puede alterar la apariencia del gráfico de modo que su sensibilidad se adecue a las propias necesidades que usted tenga."**

`[IMPLICACIÓN PARA IRIS]` **Este pasaje es simultáneamente lo más valioso y lo más peligroso del capítulo.**

- **Valioso**: el par (tamaño de registro, criterio de inversión) es un **filtro de ruido explícito y con sólo dos parámetros**, ambos interpretables. Y produce el efecto de sensibilidad de forma mucho más transparente que, por ejemplo, la longitud de una media móvil.
- **Peligroso**: **el mismo período histórico produce entre 0 y 6 señales según los parámetros elegidos.** Es la demostración más nítida del libro de que **el número de señales que un método genera es esencialmente una elección del analista**. Con un espacio de dos parámetros y un criterio de selección basado en el resultado, **el sobreajuste es trivial**.

`[INTERPRETACIÓN]` Y la variante logarítmica que Murphy documenta (Ken Tower) **agrava y a la vez mitiga el problema**: define el tamaño del registro **como porcentaje** (3,6% para AOL, 3,2% para Intel) **determinado por un proceso que mide la volatilidad del valor en los últimos 3 años**. Mitiga porque hace el parámetro adimensional y adaptado al instrumento; agrava porque **introduce una ventana de calibración de 3 años cuya causalidad habría que verificar**. `[VACÍO]` El procedimiento exacto de esa calibración no se describe.

### 11.3 Construcción intradía y la información que requiere

`[MURPHY]` **"El gráfico intradía fue el tipo de gráfico original que usaron los chartistas de puntos y figuras."** La intención era **"capturar y registrar en papel cada movimiento de un punto de los valores"**, porque **"se creía que la acumulación (compra) y la distribución (venta) se podían detectar mejor de esta manera"**. El ejemplo que desarrolla usa **secuencias de precios reales intradía** de un contrato de francos suizos: series de valores sucesivos dentro de cada día.

**Y aquí está la distinción crítica:**

`[MURPHY]` **El método de inversión de 3 registros de A. W. Cohen (1947)** fue una **condensación** del método de 1 registro. **"Cohen pensó que como había tan pocos cambios de 3 registros en los valores durante el día, no era necesario usar precios intradía para construir el gráfico de inversión de 3 registros. De ahí parte la decisión de usar sólo los precios máximo y mínimo."**

**Las reglas de actualización diaria que documenta** (figura 11.8):
- Si la columna actual es de x, mirar **primero el máximo del día**; si permite marcar x, hacerlo **e ignorar el mínimo**. Sólo si no puede marcarse ninguna x, mirar el mínimo para ver si hubo inversión.
- Si la columna actual es de o, mirar **primero el mínimo**; si permite marcar o, hacerlo e ignorar el máximo.
- **"En el mismo día no pueden haber x y o."**

`[IMPLICACIÓN PARA IRIS]` **Análisis de compatibilidad, que es el punto central del encargo para este capítulo:**

| Variante | Clasificación | Justificación |
|---|---|---|
| **P&F de inversión de 1 registro (original)** | **`GRANULAR`** | Requiere la **secuencia de precios dentro de la barra**. Con OHLCV no sabemos el orden en que se recorrieron los precios. |
| **P&F de inversión de 3 registros (Cohen)** | **`OHLCV-OK`** | **Usa exclusivamente máximo y mínimo**, con reglas de prioridad explícitas. Directamente construible con nuestros datos. |

`[INTERPRETACIÓN]` **Esto es un hallazgo relevante y merece subrayarse**: el método de 3 registros **fue diseñado precisamente para prescindir de datos intradía**, y sus reglas de actualización son un algoritmo determinista sobre `(H, L)`. Es decir, **la propia disciplina ya resolvió el problema de reconstruir un muestreo por movimiento a partir de barras agregadas**, y lo hizo con la misma lógica de aproximación que tendríamos que aplicar nosotros.

**Pero la aproximación tiene un coste declarado por la propia construcción:** la regla de prioridad ("mirar primero el máximo si estamos en columna de x, e ignorar el mínimo") **es una convención arbitraria que resuelve la ambigüedad intrabar suponiendo una continuación**. Es exactamente el mismo problema que identificamos en la etapa anterior sobre comprobar barreras contra High/Low sin conocer el orden. **Murphy documenta una solución convencional; no demuestra que sea la correcta.** `[VACÍO]`

### 11.4 Cuenta horizontal y objetivos

`[MURPHY]` **La técnica de medición propia del P&F**: en lugar de medir la altura del patrón (como en gráficos de barras), **se cuenta el ancho** — el número de columnas de la zona de congestión — y se proyecta ese número de registros desde la línea de medición.

**La regla para elegir la línea**: **"la línea horizontal a partir de la cual se comienza a medir está cerca del medio de la zona de congestión. Una regla más precisa es usar la línea que contenga el menor número de registros vacíos, o dicho de otro modo, la línea que tenga la mayor cantidad de x y de o."** Hay que contar **todas** las columnas, incluidas las vacías.

`[MURPHY]` Y reconoce la dificultad: **"La clave está en determinar cuál es la línea a partir de la cual se ha de medir, algo que a veces es fácil y otras, más difícil."**

`[INTERPRETACIÓN]` La cuenta horizontal introduce una hipótesis distinta de todas las anteriores: **la magnitud del movimiento posterior es proporcional a la duración de la congestión previa, no a su amplitud**. Es una hipótesis independiente y falsable, y **conecta con el límite temporal del triángulo** (§6.1) y con el principio general de que "cuanto más grande el patrón, mayor el movimiento" (§5.1), del que aquí se aísla la componente temporal.

**Grados de libertad**: identificar la zona de congestión, elegir la línea de medición (regla parcialmente objetiva: la fila con más registros ocupados), más los dos parámetros del gráfico. **`LOOK-AHEAD-LEVE`** — la zona de congestión sólo se delimita cuando ha terminado.

### 11.5 Patrones, líneas de tendencia y señales

`[MURPHY]` **Los patrones de P&F "no son muy diferentes de los ya vistos al tratar los gráficos de barras. La mayor parte de ellos son variaciones de los patrones dobles y triples superiores e inferiores, de cabeza y hombros, en V y en V invertida, y de platillo."**

Introduce el término **punto de apoyo (fulcrum)**: **"un área de congestión bien definida que aparece después de un avance o retroceso importante y que forma una base de acumulación o un tope de distribución"**; queda completo con **una ruptura (catapulta) por encima de la zona**.

**Señales operativas exactas** (Chartcraft, figura 11.8):
- **Compra**: cuando una columna de x **supera en un registro** la x más alta de la columna de x anterior.
- **Venta**: cuando una columna de o queda **un registro por debajo** de la o más baja de la columna de o anterior.
- **El punto de cobertura de corto es exactamente el mismo que la señal de compra**; la liquidación de largo, el mismo que la señal de venta.
- **"Dado que todos los puntos de entrada y salida se pueden determinar de antemano, las órdenes también se pueden fijar con antelación."**
- **Estado**: alcista tras una señal de compra hasta que aparezca una de venta. **Sistema continuo.**

`[MURPHY]` **Líneas de tendencia**: en el P&F simplificado **se utilizan líneas de 45 grados** y se representan de forma distinta que en gráficos de barras.

`[IMPLICACIÓN PARA IRIS]` Dos observaciones:

1. **Las señales de P&F son las más objetivas de todo el libro.** Una vez fijados los dos parámetros, **la señal es determinista y anticipable**: no hay interpretación, no hay confirmación posterior, y el punto exacto se conoce antes de que ocurra. `[INTERPRETACIÓN]` Es, estructuralmente, **un sistema de ruptura de máximos/mínimos locales con filtro de movimiento** — muy próximo conceptualmente al canal de Donchian (§9.8), pero con el filtro definido en unidades de precio en lugar de en unidades de tiempo.
2. **Las líneas de tendencia a 45° heredan íntegro el problema de dependencia de escala de §4.11** — y aquí es aún más agudo, porque en un gráfico P&F el eje horizontal **no es tiempo**, de modo que un ángulo de 45° carece de interpretación en unidades naturales. **Formalización causal defendible: dudosa.**

### 11.6 Indicadores y medias móviles sobre P&F

`[MURPHY]` Menciona indicadores técnicos específicos de P&F desarrollados por Chartcraft, y **medias móviles de 10 y 20 columnas** (no de períodos) aplicadas por Ken Tower.

`[INTERPRETACIÓN]` Una media móvil sobre columnas es una media sobre un índice de eventos de movimiento, no de tiempo. **Es el análogo exacto de aplicar un indicador sobre un esquema de muestreo no cronológico.** Conceptualmente interesante y `OHLCV-COND` (dependiente de la aproximación por H/L), pero **sin ninguna evidencia de utilidad en el libro**.

### 11.7 Evaluación para IRIS

`[IMPLICACIÓN PARA IRIS]` Balance del capítulo:

**Lo que aporta:**
- **La idea de muestrear por movimiento de precio en lugar de por reloj** — la única del libro en esa dirección.
- **Una implementación concreta y determinista de esa idea que sólo requiere H y L** (método de 3 registros), con reglas de prioridad explícitas.
- **Señales objetivas y anticipables**, sin confirmación posterior ni interpretación.
- **La cuenta horizontal** como hipótesis de que la duración de la congestión predice la magnitud del movimiento.

**Lo que cuesta:**
- **Dos parámetros que determinan cuántas señales existen**, con demostración explícita en el propio texto de que el número de señales varía de 0 a 6 sobre el mismo período. Alto riesgo de sobreajuste.
- **La conversión desde OHLCV es una aproximación con una convención arbitraria** para la ambigüedad intrabar.
- **Ninguna evidencia de rendimiento** en el libro.
- Introduce una **transformación completa del dataset** (deja de haber correspondencia uno a uno entre observaciones y barras temporales), lo que complicaría cualquier alineación posterior con targets definidos en tiempo de reloj.

**Nivel: C — complementario.** Conceptualmente valioso, prácticamente costoso, sin evidencia. **No se adopta ninguna decisión.**

### 11.8 Clasificación

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| **Muestreo por movimiento de precio (principio)** | — | — | — | **Única alternativa al reloj en todo el libro** |
| P&F inversión de 1 registro | **`GRANULAR`** | — | 2 | Requiere secuencia intrabar |
| **P&F inversión de 3 registros (Cohen)** | **`OHLCV-OK`** | `CAUSAL` | 2 | **Diseñado para prescindir de datos intradía; usa sólo H y L** |
| Regla de prioridad H antes que L (o viceversa) | `OHLCV-COND` | `CAUSAL` | 0 | **Convención arbitraria ante ambigüedad intrabar** |
| Tamaño de registro / criterio de inversión | `OHLCV-OK` | `CAUSAL` | 2 | **Determinan el número de señales; riesgo de sobreajuste alto** |
| Registro porcentual calibrado por volatilidad | `OHLCV-COND` | Verificar | 2+ | Adimensional; calibración de 3 años no descrita |
| **Señales de ruptura de columna** | **`OHLCV-COND`** | **`CAUSAL`** | 2 | **Deterministas y anticipables** |
| Cuenta horizontal | `OHLCV-COND` | `LOOK-AHEAD-LEVE` | 3+ | **Hipótesis duración → magnitud** |
| Punto de apoyo (fulcrum) | `OHLCV-COND` | `LOOK-AHEAD-LEVE` | Alto | Variante de dobles/triples |
| Líneas de tendencia a 45° en P&F | `OHLCV-COND` | — | — | **Ángulo sin interpretación: el eje x no es tiempo** |
| Medias móviles sobre columnas | `OHLCV-COND` | `CAUSAL` | 2+ | Indicador sobre muestreo no cronológico |


---

## 12. VELAS JAPONESAS (Cap. 12 — Nivel B)

Capítulo redactado por Greg Morris.

### 12.1 La misma información, otra codificación visual

`[MURPHY / Morris]` La vela registra **exactamente los mismos cuatro precios que la barra**: apertura, máximo, mínimo y cierre. Elementos:
- **Cuerpo**: distancia entre apertura y cierre. **Blanco (abierto) si el cierre es mayor que la apertura; negro si es menor.**
- **Sombras (pabilos)**: las líneas superior e inferior, que **representan los precios máximo y mínimo**.

`[MURPHY / Morris]` **"Los precios de apertura y cierre tienen mucha importancia en las velas japonesas."** Y una observación reveladora sobre las sombras: **"la literatura japonesa de referencia utiliza muchos nombres diferentes para estas pequeñas líneas, lo cual resulta extraño, ya que representan los precios máximos y mínimos del día y en general, es una información que los japoneses no consideran vital."**

`[IMPLICACIÓN PARA IRIS]` Esto confirma y precisa lo anticipado en §3.1: **las velas no aportan información nueva respecto a las barras; aportan un énfasis distinto.** Concretamente, **priorizan la relación apertura-cierre sobre el rango máximo-mínimo.** Eso es una elección de qué relaciones destacar dentro del mismo vector `(O, H, L, C)`, no una fuente de datos adicional.

### 12.2 Velas básicas — la geometría elemental

`[MURPHY / Morris]` Las categorías primarias, definidas **exclusivamente por relaciones entre O, H, L, C**:

| Vela | Definición geométrica |
|---|---|
| **Día largo** | Diferencia **grande** entre apertura y cierre (cuerpo grande) |
| **Día corto** | Diferencia **pequeña** entre apertura y cierre |
| **Perinola (spinning top)** | **Cuerpo pequeño con sombras superior e inferior más largas que el propio cuerpo**. "Días de indecisión"; el color es relativamente importante |
| **Doji** | **Apertura y cierre iguales**. Sombras de largo variable |
| **Doji pernilarga** | Doji con **largas sombras superior e inferior** — "considerable indecisión" |
| **Doji lápida** | Doji con **sólo sombra superior larga**; cuanto más larga, **más bajista** |
| **Doji libélula** | Doji con **sólo sombra inferior larga**; "bastante alcista" |

`[MURPHY / Morris]` Y explicita que **"todos los patrones de velas japonesas se hacen con combinaciones de estas velas básicas"**.

`[MURPHY / Morris]` **Sobre el Doji, una admisión importante**: **"se discute si el precio de apertura y el de cierre debe ser exactamente el mismo. Es un momento en el que los precios deben ser casi iguales, especialmente cuando se trata de grandes movimientos de los precios."**

`[IMPLICACIÓN PARA IRIS]` **Ese "casi iguales" es exactamente el punto donde la categoría nominal se disuelve en una variable continua.** Definir un Doji requiere un umbral (¿cuerpo menor que el X% del rango?), y ese umbral es un parámetro libre. **Lo que se está midiendo en realidad es `|C − O| / (H − L)`** — el tamaño relativo del cuerpo respecto al rango — que es una variable continua, `OHLCV-OK`, `CAUSAL` y **sin ningún parámetro**. El Doji es esa variable binarizada por un umbral arbitrario.

`[INTERPRETACIÓN]` **La geometría elemental de una vela se reduce a un pequeño conjunto de ratios adimensionales**, todos ellos derivables de `(O, H, L, C)` sin parámetros:
- **Cuerpo relativo**: `(C − O) / (H − L)` — con signo, captura dirección y convicción.
- **Sombra superior relativa**: `(H − max(O,C)) / (H − L)`.
- **Sombra inferior relativa**: `(min(O,C) − L) / (H − L)`.
- **Posición del cierre en el rango**: `(C − L) / (H − L)` — que es exactamente `%K` del estocástico con ventana 1 (§10.8).
- **Rango relativo**: `(H − L)` normalizado por volatilidad reciente.

Estas cinco variables **agotan la información geométrica de una vela individual** y de ellas se derivan todas las categorías nominales de la tabla anterior. Es reconstrucción nuestra; no la propone el libro.

### 12.3 Los patrones nominales

`[MURPHY / Morris]` Un patrón consiste en **una sola línea o una combinación, normalmente nunca más de cinco**. **"La literatura japonesa se refiere una y otra vez a alrededor de cuarenta patrones de vela de cambio."**

El catálogo completo que el capítulo lista incluye, entre cambios alcistas y bajistas y continuidad: martillo, ahorcado, estrella fugaz, martillo invertido, sujeción por cinturón, envolvente, harami, cruz harami, línea penetrante, cubierta de nube oscura, estrella doji, líneas de encuentro, tres soldados blancos, tres cuervos negros, estrella matutina, estrella vespertina, bebé abandonado, tri-estrella, escapada, tres dentro/fuera arriba/abajo, patadas, tres ríos único, tres estrellas en el sur, golondrina escondida, sandwich de palo, paloma mensajera, peldaño inferior/superior, mínimo/máximo a juego, dos cuervos, líneas de separación, tres métodos ascendentes/descendentes, hueco Tasuki, líneas blancas costado a costado, golpe tres líneas, línea on neck, línea in neck, deliberación, bloque de avance, el último tope, tres cuervos idénticos.

**El número de velas de cada patrón se indica entre paréntesis en el catálogo: de 1 a 5.**

`[MURPHY / Morris]` **Ejemplo de definición completa — cubierta de nube oscura** (2 velas, bajista):
1. Primer día: **vela larga y blanca**, que confirma la tendencia alcista.
2. Segundo día: **abre por encima del máximo del día anterior**.
3. Cierra **al menos a media altura del cuerpo del primer día**, con cuerpo negro.

**Ejemplo de patrón de 5 velas — tres métodos ascendentes:**
1. Largo cuerpo blanco.
2. Tres días de cuerpos pequeños que **como grupo tienden a la baja**, **todos dentro del alcance del largo cuerpo blanco**, con **al menos dos de cuerpo negro**.
3. Quinto día: **largo cuerpo blanco que cierra a un nuevo máximo**.

`[MURPHY / Morris]` **Y a continuación admite explícitamente la elasticidad de la definición:**
> **"Un patrón de cinco días, como el de los tres métodos ascendentes, necesita una definición detallada. El escenario descrito más arriba es el ejemplo perfecto... Se puede aplicar la flexibilidad con un cierto grado de éxito, algo que sólo da la experiencia. Por ejemplo, los tres días de pequeñas reacciones podrían mantenerse dentro de la banda máxima-mínima del primer día en lugar de la banda del cuerpo. Los días de pequeñas reacciones no siempre tienen que ser predominantemente negros. Y finalmente, el concepto de 'período de descanso' se podría extender para incluir más de tres días de reacción."**

`[IMPLICACIÓN PARA IRIS]` **Este párrafo documenta que la definición del patrón es negociable en al menos tres dimensiones simultáneas**, y que el criterio para negociarlas es **la experiencia del analista**. Para un sistema automático eso significa: **tres parámetros adicionales sin valor especificado**, encima de los umbrales de "largo", "pequeño" y "al menos a media altura". `[VACÍO]`

### 12.4 El requisito de tendencia previa y su circularidad

`[MURPHY / Morris]` **"No es posible tener un patrón de cambio alcista en una tendencia ascendente. Puede haber una serie de velas que se parezcan al patrón alcista, pero si la tendencia es al alza, no se trata de un patrón japonés de velas ascendente."**

Y reconoce el problema que esto genera:
> **"Esto presenta uno de los problemas recurrentes cuando se analizan los mercados: ¿cuál es la tendencia? Antes de usar los patrones de velas de manera efectiva, hay que determinar la tendencia."**

**Su solución práctica**: **"la media móvil funciona bastante bien con las velas japonesas. Una vez determinada la tendencia a corto plazo (diez períodos, más o menos), los patrones de velas ayudarán a identificar el cambio de dicha tendencia."**

`[IMPLICACIÓN PARA IRIS]` Dos observaciones:
1. **La identidad del patrón depende de una variable externa (la tendencia).** Las mismas cinco velas son o no son un patrón según el contexto. Eso significa que **un detector de patrones de velas es en realidad un detector condicional**, y hereda todos los grados de libertad de la definición de tendencia (§4.8).
2. **Pero la solución propuesta es operacionalizable y barata**: una media de ~10 períodos como definidor de tendencia de corto plazo. `OHLCV-OK`, `CAUSAL`, un parámetro. Es de las pocas veces que el libro ofrece una regla concreta para una condición contextual.

### 12.5 Patrones filtrados — la aportación de Morris

`[MURPHY / Morris]` **"Un concepto revolucionario desarrollado por Greg Morris en 1991, llamado filtro para patrones de velas, proporciona un método sencillo de mejorar la confianza global en los patrones de velas."**

**El mecanismo, descrito con precisión:**
- Se usa un oscilador, por ejemplo el estocástico `%D`.
- **La "zona pre-señal"** es el área por encima de 80 o por debajo de 20: **"cuando entre en el área por encima de 80 o por debajo de 20, eventualmente generará una señal. En otras palabras, es sólo una cuestión de tiempo que aparezca una señal."**
- **"Los patrones de velas sólo se consideran cuando %D está en su área pre-señal."** Si aparece un patrón con `%D` en 65, **se ignora**.
- **"Usando este concepto, sólo se consideran los patrones de velas de cambio."**
- Funciona igual con IFR, ICM o %R.

`[MURPHY / Morris]` Y la afirmación de cierre: **"Los patrones de velas japoneses, usados en conjunción con otros indicadores técnicos en el concepto de filtro, casi siempre ofrecen una señal de compra o venta antes que otros indicadores basados en el precio."**

`[IMPLICACIÓN PARA IRIS]` **Este es el pasaje más estructuralmente relevante del capítulo**, y merece registrarse con cuidado:

Es una **arquitectura de dos componentes con roles asimétricos**, donde:
- **Un componente define la condición de admisibilidad** (el oscilador en zona pre-señal).
- **Otro componente genera el evento** (el patrón de velas).
- **La señal existe sólo en la intersección.**

`[INTERPRETACIÓN]` Es la cuarta arquitectura de dos niveles que aparece en el libro, tras: análisis/timing (§1.5), escala larga/corta (§8.4, §10.15), y precio/volumen como confirmación (§7.3). **Y es la más explícita de todas.** Registramos la convergencia estructural sin resolverla (§33, §40).

**Y una precisión crítica sobre la afirmación de anticipación**: `[INTERPRETACIÓN]` decir que el filtro produce señales "antes que otros indicadores basados en el precio" **es esperable por construcción**: el patrón de velas usa 1–5 barras, mientras que un cruce de medias de 10/50 usa decenas. **Comparar la latencia de un detector de ventana corta con la de uno de ventana larga no dice nada sobre su calidad.** El libro no aporta ninguna medición de tasa de acierto de ninguna de las dos.

### 12.6 La limitación intrabar — punto que el encargo pide registrar

`[IMPLICACIÓN PARA IRIS]` **Nuestro OHLCV no permite saber si dentro de una barra ocurrió primero el máximo o el mínimo.**

Consecuencias concretas para este capítulo:
- **La geometría de una vela individual no se ve afectada**: cuerpo, sombras y posición del cierre se calculan sin conocer el orden interno.
- **Sí se ve afectada la interpretación psicológica.** Una vela con cuerpo pequeño y sombras largas ("perinola", "indecisión") es compatible con al menos dos trayectorias muy distintas: subida seguida de caída y recuperación, o caída seguida de subida y retroceso. **Murphy/Morris atribuyen a esa forma un significado psicológico unívoco ("indecisión") que la geometría no determina.**
- **Los patrones multivela heredan el problema en cada una de sus barras.**

`[VACÍO]` **El libro no menciona esta limitación en ningún momento.** Trata la forma de la vela como si codificara la dinámica interna del período, cuando sólo codifica cuatro estadísticos de orden.

`[INTERPRETACIÓN]` Conviene notar que la gravedad de esta limitación **decrece al aumentar la frecuencia**: en barras de un minuto de MNQ, el espacio de trayectorias internas compatibles con un `(O,H,L,C)` dado es mucho más reducido que en una barra diaria. **Es una conjetura razonable, no un hecho del libro, y su verificación requeriría datos de tick que no tenemos.**

### 12.7 Evaluación: ¿el nombre o las relaciones continuas?

Respondiendo directamente a la pregunta central del encargo para este capítulo:

`[INTERPRETACIÓN]` **La evidencia interna del propio capítulo apunta a que la información está en las relaciones continuas, no en la categoría nominal.** Cuatro argumentos, todos derivados del texto:

1. **Morris declara que todos los patrones se construyen a partir de velas básicas**, y las velas básicas se definen por relaciones de tamaño entre cuerpo, sombras y rango — es decir, **por los ratios de §12.2**.
2. **Las fronteras entre categorías son explícitamente elásticas** ("casi iguales" para el Doji; tres dimensiones negociables en los tres métodos ascendentes). Una categoría con fronteras negociables es una discretización de un continuo.
3. **El significado del patrón depende del contexto** (tendencia previa, zona pre-señal del oscilador). Es decir, **la etiqueta nominal no es autosuficiente**: necesita variables externas continuas.
4. **La observación sobre los pixels** —que a baja resolución muchas velas parecen Doji sin serlo, y que **"un programa informático que identifique patrones basados en una relación matemática resolverá esta anomalía visual"**— es, literalmente, **la constatación de que el patrón es una relación matemática y la forma visual sólo su representación imperfecta**.

**Contrapunto honesto**: `[INTERPRETACIÓN]` que las categorías sean discretizaciones de un continuo **no implica automáticamente que la discretización carezca de valor**. Una categoría podría capturar una interacción no lineal entre varios ratios que un modelo lineal no encontraría. **Lo que sí implica es que la categoría no es información adicional, sino una hipótesis sobre la forma funcional** — y una hipótesis con muchos parámetros libres frente a la alternativa de dar los ratios crudos al modelo.

`[IMPLICACIÓN PARA IRIS]` La formulación de la disyuntiva, sin resolverla:
- **Opción A**: proporcionar los ratios continuos de una o varias barras y dejar que el modelo aprenda las combinaciones relevantes. Cero parámetros de forma, `OHLCV-OK`, `CAUSAL`.
- **Opción B**: implementar detectores nominales de patrones. Decenas de parámetros de umbral, misma información de base, más una hipótesis de forma funcional impuesta.

**No se elige ninguna.** Se registra que la opción B tiene un coste de grados de libertad muy superior y que el libro no aporta evidencia que lo justifique.

### 12.8 Clasificación

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| **Cuerpo relativo `(C−O)/(H−L)`** | **`OHLCV-OK`** | **`CAUSAL`** | **0** | Base de días largos/cortos y Doji |
| **Sombra superior / inferior relativa** | **`OHLCV-OK`** | **`CAUSAL`** | **0** | Base de martillo, lápida, libélula |
| **Posición del cierre en el rango** | **`OHLCV-OK`** | **`CAUSAL`** | **0** | **= `%K` con ventana 1** |
| **Rango relativo a volatilidad reciente** | `OHLCV-OK` | `CAUSAL` | 1 | Base de "largo"/"corto" |
| Relaciones entre barras consecutivas (envolvente, harami, huecos) | `OHLCV-OK` | `CAUSAL` | 0–1 | Comparaciones de O,H,L,C entre barras |
| Doji | `OHLCV-OK` | `CAUSAL` | **1 (umbral)** | Binarización del cuerpo relativo |
| Patrones nominales de 1–2 velas | `OHLCV-OK` | `CAUSAL` | 2–5 | Umbrales de tamaño y solapamiento |
| Patrones nominales de 3–5 velas | `OHLCV-OK` | `CAUSAL` | **5–10+** | **Definición explícitamente elástica** |
| **Requisito de tendencia previa** | `OHLCV-OK` | `LOOK-AHEAD-LEVE` o `CAUSAL` con MA | 1+ | Media de ~10 períodos como solución propuesta |
| **Filtro por zona pre-señal de oscilador** | **`OHLCV-OK`** | **`CAUSAL`** | 2 | **Arquitectura de dos componentes explícita** |
| Interpretación psicológica de la forma | — | — | — | **`[VACÍO]` No determinada por la geometría; requiere secuencia intrabar** |


---

## 13. ONDAS DE ELLIOTT Y FIBONACCI (Cap. 13 — Nivel C)

### 13.1 La estructura básica

`[MURPHY]` **Tres aspectos, en orden declarado de importancia: patrón, coeficiente (ratio) y tiempo.**

**La forma básica:** un ciclo completo de mercado alcista tiene **ocho ondas: cinco de avance y tres de retroceso**. Las ondas 1, 3 y 5 son **impulsoras**; las 2 y 4, **correctoras**. Tras el avance de cinco ondas viene la corrección a-b-c.

**La regla de subdivisión, que es el mecanismo generativo de la teoría:**
> `[MURPHY]` **"El hecho de que una onda determinada se divida en cinco o tres ondas viene determinado por la dirección de la siguiente onda más grande."** Las ondas que se mueven en la dirección de la onda mayor se subdividen en cinco; las que van en contra, en tres.

`[MURPHY]` **"Una de las reglas más importantes a tener presente es que una corrección nunca puede ocurrir en cinco ondas."** Consecuencia práctica: en un mercado alcista, un descenso de cinco ondas indica que hay más caída por venir; una subida de cinco ondas en mercado bajista avisa de un movimiento sustancial y posiblemente de una nueva tendencia.

`[MURPHY]` Señala la **conexión con Dow**: las tres ondas ascendentes con dos correcciones intermedias encajan con las tres fases del mercado alcista de Dow, y ambas teorías usan la metáfora marítima.

### 13.2 Ondas correctoras

`[MURPHY]` **"En general, no están tan claramente definidas y por lo tanto tienden a ser más difíciles de identificar y predecir."** Tres clasificaciones:

| Tipo | Estructura | Características |
|---|---|---|
| **Zigzag** | **5-3-5** | La onda B cae casi hasta el comienzo de A; **la onda C va mucho más allá del final de A** |
| **Plana** | **3-3-5** | "Más una consolidación que una corrección"; en mercado alcista **se considera señal de fuerza**. La onda C acaba justo en la parte inferior de A o poco por debajo |
| **Triángulo** | — | **Excepción a la regla de tres ondas.** Suelen ser cuartas ondas y siempre preceden a la onda final; también pueden ser ondas correctoras B |

**Variantes documentadas**: zigzag doble (dos zigzags 5-3-5 conectados por un a-b-c intermedio), y **dos variaciones "irregulares" de la corrección plana** — en una, B sobrepasa el techo de A y C viola el suelo de A; en otra, B alcanza el techo de A pero C no llega al suelo de A.

`[INTERPRETACIÓN]` **Contabilidad de configuraciones correctoras**: zigzag, zigzag doble, plana normal, plana irregular tipo 1, plana irregular tipo 2, y triángulos (que además son la excepción declarada a la regla fundamental). **Seis estructuras alternativas para el mismo fenómeno "corrección", más una excepción a la regla que define la teoría.** Esto es directamente relevante para la evaluación de falsabilidad (§13.5).

### 13.3 Reglas objetivas frente a reglas flexibles

Conforme pide el encargo, separo lo que es regla estricta de lo que es guía:

**Reglas presentadas como estrictas:**
1. **Las correcciones nunca ocurren en cinco ondas** — pero con la excepción explícita de los triángulos.
2. **La onda 4 no debe solaparse con la onda 1** — pero `[MURPHY]` **"no es tan rígido en futuros"**; en gráficos de futuros **"pueden haber penetraciones intradía"**.
3. **Los mercados bajistas no deben caer por debajo de la parte inferior de la cuarta onda previa** — pero `[MURPHY]` **"hay excepciones a la regla"**.

**Guías flexibles:**
4. **Regla de la alternancia**: "no se ha de esperar que suceda lo mismo dos veces seguidas".
5. **Extensión**: "a veces, una de las ondas de impulso se extiende. Las otras dos deben ser iguales en tiempo y magnitud."
6. **Canalización** y la onda 4 como área de apoyo.

`[IMPLICACIÓN PARA IRIS]` **Las tres reglas presentadas como estrictas admiten excepción declarada por el propio autor, y dos de las tres excepciones se refieren específicamente a futuros** — que es nuestro caso. Una regla con excepción no especificada no es falsable: cualquier violación observada puede clasificarse como excepción.

### 13.4 Fibonacci: ratios, objetivos y retrocesos

`[MURPHY]` La secuencia 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144… con sus propiedades: cociente de un número respecto al siguiente → **0,618**; respecto al anterior → **1,618**; entre alternos → **2,618** o **0,382**.

**Argumento de conexión**: un ciclo completo tiene 8 ondas (5+3), y subdivisiones sucesivas dan 34 y 144 — todos números de Fibonacci.

**Los ocho usos de ratios que enumera para objetivos de precio:**
1. Si la onda 5 se extiende, las ondas 1 y 3 deben ser aproximadamente iguales; si se extiende la 3, las ondas 1 y 5 tienden a la igualdad.
2. Objetivo mínimo del techo de la onda 3: **extensión de la onda 1 × 1,618**, sumado al suelo de la onda 2.
3. Techo de la onda 5: **onda 1 × 3,236 (2×1,618)**, sumado al máximo **o** al mínimo de la onda 1 "para alcanzar objetivos máximos y mínimos".
4. Si 1 y 3 son iguales y se espera extensión de la 5: distancia del suelo de 1 al techo de 3, **× 1,618**, sumada al suelo de la onda 4.
5. En zigzag, la onda c **a menudo es aproximadamente igual** a la onda a.
6. Otra medida de la onda c: **0,618 × longitud de a**, restado del suelo de a.
7. En plana con b sobrepasando el techo de a: **c = a × 1,618**.
8. En triángulo simétrico, cada onda sucesiva se relaciona con la anterior por **0,618**.

**Retrocesos porcentuales**: los más usados son **61,8% (redondeado a 62%), 38% y 50%**. Y `[MURPHY]` observa que **"el famoso retroceso del 50 por ciento es en realidad una ratio de Fibonacci, igual que el retroceso de dos tercios"**, porque los primeros cocientes de la secuencia son 1/1 = 100%, 1/2 = 50%, 2/3 = 66%.

`[INTERPRETACIÓN]` **Este último argumento merece atención crítica.** Sostiene que 50% y 66% "son en realidad ratios de Fibonacci" porque aparecen entre los primeros términos de la sucesión de cocientes. Pero **los primeros términos son precisamente los que aún no han convergido a 0,618** — el propio Murphy lo dice en §13.4 ("se acercan a 0,618 sólo después de los cuatro primeros números"). **El argumento incorpora al marco de Fibonacci exactamente los valores que se desvían de la constante que define ese marco.** Con esa licencia, la cobertura de niveles se amplía a 38, 50, 62, 66 y 100%, más los de Dow (33, 66) y los de Gann (octavos). **Es el mismo mecanismo de proliferación que ya se documentó en §4.13, aquí llevado más lejos.**

### 13.5 Evaluación de formalizabilidad — respuesta a la pregunta del encargo

`[INTERPRETACIÓN]` El encargo pide determinar qué reglas son objetivas, cuáles interpretativas, cuántos grados de libertad hay, qué riesgo de ajuste retrospectivo existe, y si hay alguna representación cuantitativa defendible. Análisis por partes:

**Qué requiere una identificación de ondas de Elliott:**

| Requisito | Grado de libertad |
|---|---|
| Identificar pivotes en el precio | `LOOK-AHEAD-LEVE`; parámetro `k` |
| Determinar el **grado** de la onda (¿de qué escala estamos hablando?) | **No acotado** — la teoría es explícitamente fractal e infinita en ambas direcciones |
| Contar las subondas de cada onda | Depende del grado elegido; recursivo |
| Decidir si una corrección es zigzag, zigzag doble, plana normal o plana irregular (dos variantes) | **≥6 alternativas** |
| Decidir si un triángulo es la excepción aplicable | Sí |
| Decidir si estamos ante una extensión y de cuál onda | 3 alternativas |
| Aplicar excepciones a las reglas "estrictas" | **No especificado cuándo** |
| Elegir entre ocho fórmulas de objetivo de precio | 8 alternativas |
| Elegir nivel de retroceso entre 38/50/62/66/100 | ≥5 |

**Y el problema decisivo, que es de naturaleza distinta a los anteriores:**

`[INTERPRETACIÓN]` **El recuento de ondas no es único.** Como la estructura es fractal, un mismo tramo de precio admite múltiples etiquetados válidos según el grado que se asuma; y **el etiquetado sólo se resuelve cuando el desarrollo posterior descarta las alternativas**. Esto no es `LOOK-AHEAD-LEVE` (un retardo fijo de confirmación), sino algo más severo: **la interpretación se revisa continuamente a medida que llegan datos**. Es la misma estructura del problema que Murphy documentó para las líneas de canal redibujadas (§4.12), pero aquí es el mecanismo central de la teoría, no un detalle.

**Riesgo de ajuste retrospectivo**: máximo. Con ≥6 estructuras correctoras, excepciones no especificadas, grado ajustable y 8 fórmulas de objetivo, **prácticamente cualquier trayectoria admite un recuento consistente a posteriori**.

**Conclusión, conforme al encargo (que pide decirlo explícitamente si procede):**

> `[INTERPRETACIÓN]` **La teoría de las ondas de Elliott, tal como Murphy la presenta, no admite una formalización causal y reproducible.** No porque sus conceptos sean vagos —muchas de sus reglas son geométricamente precisas— sino porque **el número de configuraciones admisibles, unido a excepciones declaradas y a la ambigüedad de grado, hace que el conjunto de trayectorias incompatibles con la teoría sea prácticamente vacío**. Una teoría que no puede ser contradicha por ninguna observación no genera predicciones comprobables. **No se fuerza ninguna aplicación.**

**Lo que sí puede rescatarse** `[INTERPRETACIÓN]`, y conviene separarlo con nitidez:

- **Los niveles de retroceso de Fibonacci como variable continua**: la profundidad del retroceso relativa al impulso previo es `OHLCV-OK`, tiene un parámetro (la definición del impulso) y produce una **distribución empírica comprobable**. Es exactamente lo mismo que se registró en §4.13, y **no requiere ninguna teoría de ondas**. La pregunta falsable es si esa distribución tiene estructura en MNQ, no si respeta el 61,8%.
- **La alternancia entre impulso y corrección** como observación de que los movimientos direccionales se intercalan con retrocesos de menor magnitud. Esto es una afirmación sobre la **estructura de autocorrelación a distintas escalas** y es medible sin etiquetar ondas.
- **La onda 4 como soporte**: reformulada, es la afirmación de que **el suelo de la última consolidación dentro de una tendencia tiende a contener el retroceso posterior** — una hipótesis de soporte/resistencia ordinaria (§4.3), no una aportación de Elliott.

### 13.6 Las advertencias de aplicabilidad del propio Murphy

`[MURPHY]` **Y aquí el libro es notablemente honesto sobre los límites de su propio capítulo:**

1. **"Es importante tener presente que la teoría de las ondas fue pensada en su origen para aplicarse a las medias del mercado de valores. Con los valores corrientes individuales no funciona tan bien, y es posible que tampoco lo haga en algunos de los mercados de futuros más sofisticados, porque la psicología de masas es uno de los cimientos importantes sobre los que descansa la teoría."**
2. **"La teoría encuentra su mejor aplicación en los mercados de bienes que tienen un gran seguimiento público, como por ejemplo el del oro."**
3. **"El uso de los gráficos de continuidad en los mercados de bienes de futuros también produce distorsiones que pueden afectar los patrones tipo Elliott a largo plazo."**
4. En futuros, la regla del no solapamiento entre ondas 1 y 4 **no es rígida**.
5. **"A veces, las imágenes que produce Elliott son claras y a veces, no. Intentar traducir una acción de mercado que no está clara al formato de Elliott... es hacer una aplicación inadecuada de la teoría."**
6. **"La clave está en considerar la Teoría de las Ondas de Elliott como una respuesta parcial al rompecabezas."**

`[IMPLICACIÓN PARA IRIS]` **Los puntos 1, 2 y 4 desaconsejan explícitamente la aplicación a nuestro caso**: un futuro sobre índice, sofisticado, sin el "gran seguimiento público" que el autor señala como condición favorable. **Y el punto 3 es una advertencia adicional pertinente**: el propio método de construcción de la serie continua que necesitamos (§8) distorsiona los patrones de Elliott según el autor.

**El punto 5 es el más problemático metodológicamente**: la teoría se aplica cuando la imagen es clara y no se aplica cuando no lo es, sin criterio previo de claridad. **Eso convierte la selección de casos en un acto discrecional posterior a la observación.**

### 13.7 Clasificación

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| Estructura 5-3 y recuento de ondas | `OHLCV-OK` nominalmente | **`LOOK-AHEAD-GRAVE`** | **No acotado** | Etiquetado no único; revisable con datos nuevos |
| Regla de subdivisión por dirección | — | `LOOK-AHEAD-GRAVE` | — | Requiere conocer el grado superior |
| "Las correcciones nunca son de cinco ondas" | — | — | — | **Excepción declarada: triángulos** |
| "Onda 4 no solapa con onda 1" | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | — | **"No tan rígido en futuros"** |
| "Bajista no cae bajo la onda 4 previa" | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | — | "Hay excepciones" |
| Zigzag / plana / irregulares / triángulos | `OHLCV-OK` | `LOOK-AHEAD-GRAVE` | **≥6 alternativas** | Cubren casi todo el espacio de correcciones |
| Regla de alternancia | — | — | — | Guía cualitativa, no regla |
| Ocho fórmulas de objetivo por ratios | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | **8 alternativas** | Requieren ondas identificadas |
| **Retroceso relativo al impulso (variable continua)** | **`OHLCV-OK`** | `LOOK-AHEAD-LEVE` | **1** | **Comprobable sin teoría de ondas** |
| Niveles 38/50/62/66/100% | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | **≥5** | Proliferación de niveles candidatos |
| Onda 4 como soporte | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Medio | **Es soporte/resistencia ordinario** |
| Aplicabilidad a futuros sofisticados | — | — | — | **Desaconsejada por el propio autor** |


---

## 14. CICLOS TEMPORALES (Cap. 14 — Nivel C)

### 14.1 Las tres cualidades de un ciclo

`[MURPHY]` Basándose en el trabajo de J. M. Hurst:

| Cualidad | Definición |
|---|---|
| **Amplitud** | Altura de la onda, expresada en unidades de precio |
| **Período** | Lapso entre valles |
| **Fase** | **Medida del emplazamiento temporal del valle de una onda.** Permite estudiar relaciones entre ciclos de distinta duración e **identificar la fecha del último mínimo** para proyectar el siguiente |

`[MURPHY]` **Y una precisión metodológica relevante**: los ciclos se miden **de valle a valle**, no de cresta a cresta, porque **"esta medida no se considera tan estable y de confianza como la que se toma entre valle y valle"**. La razón aparece más adelante: **"casi todas las variaciones de los ciclos ocurren en las crestas y no en los valles"**.

### 14.2 Los principios cíclicos

`[MURPHY]`

| Principio | Contenido |
|---|---|
| **Acumulación (sumación)** | Las ondas se suman: la onda compuesta es la suma punto a punto de sus componentes |
| **Armonía** | Ondas vecinas se relacionan por un **factor 2** (la onda B tiene la mitad de longitud que la A) |
| **Sincronización** | **"Fuerte tendencia de las ondas de diferente duración a alcanzar su parte más baja aproximadamente al mismo tiempo."** También implica que ciclos de longitud similar **en distintos mercados** tienden a girar juntos |
| **Proporcionalidad** | **Ciclos de período más largo tienen amplitudes proporcionalmente mayores.** Un ciclo de 40 días debería tener el doble de amplitud que uno de 20 |
| **Variación** | **"Todos los otros principios... son simplemente tendencias fuertes y no reglas puras y duras. En el mundo real pueden ocurrir variaciones, y de hecho, ocurren"** |
| **Nominación** | Existe **"un grupo nominal de ciclos relacionados armónicamente que afectan a todos los mercados"**, utilizable como punto de partida para cualquier mercado |

**El modelo nominal simplificado** que presenta: 18 años → 9 años → 54 meses → 18 meses → 40 semanas → 20 semanas → 80 días → 40 → 20 → 10 → 5. Cada nivel es la mitad del anterior, **"la única excepción es la relación entre 54 y 18 meses, que es un tercio en lugar de la mitad"**.

`[IMPLICACIÓN PARA IRIS]` **El principio de variación es, metodológicamente, el más importante y el más problemático.** Declara explícitamente que **ninguno de los otros principios es una regla**, sino una tendencia con excepciones no especificadas. Combinado con el principio de nominación —que además admite ya una excepción en su propia tabla— el conjunto **no genera predicciones falsables**: cualquier desviación observada queda cubierta por el principio de variación.

### 14.3 El ciclo de 28 días y la circularidad de los parámetros

`[MURPHY]` **"Casi todos los mercados tienen la tendencia a alcanzar un mínimo en el ciclo de transacciones cada 4 semanas."** Una explicación posible que menciona: **el ciclo lunar**, citando a Burton Pugh (1933) sobre el trigo — comprar con luna llena, vender con luna nueva. Y añade que **"Pugh reconocía que los efectos lunares eran débiles y que podían quedar anulados por los efectos de ciclos más largos"**.

**Y el argumento de cierre del ciclo:**
> `[MURPHY]` **"Tenga o no tenga algo que ver la luna, el ciclo de 28 días existe y explica muchos de los números usados en el desarrollo de indicadores de más corta duración."** 28 días naturales = 20 de contratación; de ahí las medias de 5, 10, 20 y 40 días, las variantes 4-9-18, los osciladores de 5-10-20, y las reglas de 2, 4 y 8 semanas.

Y aplicado a Donchian: **"El conocimiento de la existencia de un ciclo de transacciones de 4 semanas... ayuda a comprender por qué la regla de las 4 semanas ha funcionado tan bien durante tantos años."**

`[INTERPRETACIÓN]` **Esto cierra la circularidad que se detectó en §9.11 y §10.13, y ahora puede describirse completa:**

1. Se observa empíricamente que ciertos períodos (4, 9, 10, 14, 18, 20, 40) son populares y parecen funcionar.
2. Se postula un ciclo dominante de 20 días de contratación para explicarlos.
3. **La evidencia ofrecida a favor del ciclo de 20 días es que esos períodos son populares y funcionan.**

**No hay ninguna medición independiente del ciclo de 28 días en el libro** — ni un periodograma, ni un test de significación, ni una estimación de amplitud. La única fuente externa citada es un estudio sobre trigo de 1933 cuyo propio autor calificaba el efecto de débil. `[VACÍO]`

`[IMPLICACIÓN PARA IRIS]` **La consecuencia práctica es que los períodos "estándar" de los indicadores del libro no tienen justificación empírica demostrada, sino una justificación circular.** Esto refuerza —desde otro ángulo— la conclusión de §9.4: **no hay base para trasladar los parámetros de Murphy a MNQ intradiario**, ni siquiera reescalándolos.

### 14.4 Traslación izquierda/derecha

`[MURPHY]` **"El concepto de traslación tal vez sea el aspecto más útil del análisis de los ciclos."**

En un ciclo de 20 días medido de mínimo a mínimo, el pico ideal debería estar en el día 10. **"Pero los picos ideales de los ciclos raramente se dan."** Y las crestas se desplazan según la tendencia del ciclo mayor:
- **Tendencia mayor ascendente → cresta desplazada a la derecha → traslación derecha → alcista.**
- **Tendencia mayor descendente → cresta desplazada a la izquierda → traslación izquierda → bajista.**

**Y aquí Murphy hace la observación más lúcida del capítulo:**
> **"Deténgase un momento a pensar en esto. Lo único que estamos diciendo aquí es que en una tendencia al alza, los precios pasarán más tiempo subiendo que bajando. En una tendencia a la baja, los precios pasan más tiempo bajando que subiendo. ¿No es ésta la definición de tendencia? Sólo que en este caso estamos hablando del tiempo en lugar del precio."**

`[IMPLICACIÓN PARA IRIS]` **Esta es la aportación aprovechable del capítulo, y es notable porque el propio autor la despoja de su envoltorio cíclico.**

La reformulación que él mismo ofrece es directamente cuantificable: **la asimetría temporal entre tiempo pasado subiendo y tiempo pasado bajando** dentro de una ventana. Eso es:
- **`OHLCV-OK`** y **`CAUSAL`** (basta contar barras de retorno positivo y negativo, o el tiempo entre extremos locales).
- **Un solo parámetro** (la ventana).
- **Adimensional** y comparable entre regímenes.
- **Conceptualmente distinto de la variación neta de precio**: dos series con el mismo retorno acumulado pueden tener asimetrías temporales opuestas.

`[INTERPRETACIÓN]` Y es interesante notar que esto **no requiere identificar ningún ciclo**. Es una medida de la estructura temporal de la tendencia que sobrevive al colapso del marco cíclico. Registrada como candidata conceptual; **no se adopta**.

### 14.5 Cómo aislar ciclos — y por qué es el punto débil

`[MURPHY]` **"La más sencilla es por medio de la inspección visual. Estudiando los gráficos de barras diarios es posible identificar los máximos y mínimos obvios de un mercado. Calculando los lapsos medios entre esos máximos y mínimos cíclicos, se pueden encontrar ciertas longitudes medias."**

Herramientas que documenta: el **Ehrlich Cycle Finder** (dispositivo físico en forma de acordeón que se superpone al gráfico, **"se puede extender o contraer para que se ajuste a cualquier longitud de ciclo"**), su versión electrónica, y arcos superpuestos en pantalla cuyos períodos **"se pueden alargar, acortar, mover a la izquierda o a la derecha hasta encontrar el ajuste adecuado en el gráfico"**.

`[IMPLICACIÓN PARA IRIS]` **La frase "hasta encontrar el ajuste adecuado en el gráfico" describe literalmente un procedimiento de ajuste retrospectivo.** El período del ciclo no se estima con un criterio estadístico: se ajusta hasta que las líneas verticales coinciden con los mínimos ya observados. **Con un parámetro de período libre y otro de fase libre, encontrar coincidencias en cualquier serie —incluida una aleatoria— es trivial.**

Los ejemplos que da lo ilustran: ciclo de **49 días** en el S&P 500, **133 días** en Boeing, **75 meses** y **55 días** en bonos. `[INTERPRETACIÓN]` **Cuatro instrumentos, cuatro períodos distintos, ninguno perteneciente al modelo nominal** (que predecía 5, 10, 20, 40, 80 días). El propio material contradice el principio de nominación que el capítulo defiende.

`[MURPHY]` **Y él mismo reconoce el problema de fondo**: **"la búsqueda de los ciclos dominantes adecuados en cualquier mercado es complicada por la creencia de que las duraciones de los ciclos no son estáticas, o dicho de otro modo, que cambian continuamente. Algo que funcionaba el mes pasado, tal vez no funcione dentro de un mes."**

**Respondiendo a la pregunta del encargo** (*¿cómo diferenciar un ciclo persistente de una coincidencia histórica seleccionada retrospectivamente?*):

`[INTERPRETACIÓN]` **Murphy no ofrece ningún criterio.** El único método que describe es la inspección visual con ajuste de parámetros hasta la coincidencia, y admite que los períodos cambian con el tiempo. **Sin un test de significación que compare contra la hipótesis nula de ausencia de periodicidad, y sin corrección por el número de períodos probados, la distinción es indecidible con las herramientas del capítulo.** Es un `[VACÍO]` central.

### 14.6 MESA y la conexión tendencia/ciclo

`[MURPHY]` Menciona el **Maximum Entropy Spectral Analysis** de John Ehlers como **enfoque estadístico** para la detección de ciclos, cuya ventaja declarada es **"su medida de alta resolución de ciclos con períodos relativamente pequeños, algo que es crucial para operar a plazos cortos"**.

**Y lo que Murphy destaca de Ehlers es lo más relevante para nosotros:**
> **"Ehlers también trata el problema de la distinción entre un mercado en un ciclo en oposición a un mercado en una tendencia. Cuando un mercado está en una cierta tendencia, se necesita un indicador que la siga, como la media móvil. En cambio, un mercado que está en un cierto ciclo favorecería el uso de indicadores tipo oscilador. La medida de los ciclos puede ayudar a determinar en qué etapa está el mercado actualmente, y qué tipo de indicador técnico es el más adecuado."**

`[IMPLICACIÓN PARA IRIS]` **Tercera aparición de la hipótesis de régimen** (tras §9.12 y §10.1), y la primera que propone **una forma medible de determinar el régimen** en lugar de dejarlo al juicio. La idea —clasificar el estado del mercado como tendencial o cíclico, y condicionar las herramientas a esa clasificación— es formalizable. `[INTERPRETACIÓN]` Y conviene notar que **el coeficiente de eficiencia de Kaufman (§9.10) hace exactamente eso con un solo parámetro y sin análisis espectral**. `[VACÍO]` El libro sólo remite a la obra de Ehlers; no describe el método.

### 14.7 Ciclos estacionales

`[MURPHY]` **"Todos los mercados se ven afectados de algún modo por un ciclo estacional anual"**: tendencia a moverse en cierta dirección en ciertos momentos del año. Los más obvios están en los cereales (cosecha), pero **"prácticamente todos los mercados experimentan patrones estacionales"**.

Ejemplos que documenta con gráficos estacionales de 14-15 años (Moore Research Center): soja (máximos abril-junio, mínimos agosto-octubre), cobre (mínimo octubre y febrero, máximo abril-mayo), crudo (máximo octubre), oro (mínimo agosto), dólar (mínimo enero), bonos del tesoro (máximo en enero, primer semestre débil, segundo fuerte).

**Ciclos del mercado bursátil**: trimestre más fuerte de noviembre a enero; febrero débil; marzo y abril fuertes; junio suave; julio fuerte (subida estival); **septiembre el mes más débil**; **diciembre el más fuerte** con la subida de Santa Claus. Menciona también el **barómetro de enero** y el **ciclo presidencial de 4 años**.

`[IMPLICACIÓN PARA IRIS]` **Clasificación: `OHLCV-OK`** — los patrones estacionales se calculan sobre la propia serie de precios agregando por posición en el calendario.

**Pero la relevancia para IRIS es baja y conviene precisar por qué:**
1. **La escala es anual.** Un patrón estacional mensual es irrelevante para decisiones intradiarias, salvo como variable de contexto de muy baja frecuencia.
2. **El mecanismo declarado es la oferta física** (cosechas), que no aplica a un índice bursátil.
3. **Los ejemplos bursátiles no tienen mecanismo propuesto**, sólo regularidad observada — y sobre 14-15 años, es decir, **14-15 observaciones independientes por mes**. Con 12 meses probados, **la corrección por multiple testing sería severa** y el libro no la contempla en absoluto.

`[INTERPRETACIÓN]` **Lo que sí puede ser relevante para IRIS, y que Murphy no trata, es la estacionalidad intradiaria** — el patrón sistemático de volatilidad, volumen y comportamiento del precio a lo largo de la sesión. Es un fenómeno de la misma naturaleza (regularidad ligada a la posición en un ciclo temporal) pero a una escala completamente distinta, y **con mecanismos plausibles bien conocidos** (apertura, solapamiento de sesiones, cierres, publicaciones programadas). `[VACÍO]` **El libro no menciona la estacionalidad intradiaria en ningún momento.**

### 14.8 Evaluación del capítulo

`[IMPLICACIÓN PARA IRIS]` Balance:

**Aprovechable:**
- **La traslación izquierda/derecha reformulada como asimetría temporal** (§14.4). Es la única idea del capítulo que sobrevive intacta al colapso del marco cíclico, y el propio autor la traduce.
- **La conexión régimen tendencial / régimen cíclico → herramienta apropiada** (§14.6), aunque el método de determinación quede sin describir.
- **La distinción entre las tres cualidades** (amplitud, período, fase) como vocabulario para caracterizar cualquier oscilación, cíclica o no.

**No aprovechable:**
- **El aparato cíclico completo**, por ausencia de método causal de identificación y de criterio para distinguir ciclo real de coincidencia.
- **El modelo nominal**, contradicho por los propios ejemplos del capítulo.
- **La justificación de los parámetros de indicadores por el ciclo de 28 días**, circular.
- **La estacionalidad anual**, por escala y por ausencia de control de multiple testing.

**Nivel: C.** Conceptualmente sugerente, metodológicamente el capítulo más débil del libro junto con el 13.

### 14.9 Clasificación

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| Amplitud / período / fase | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | 1+ | Vocabulario útil |
| Medición valle a valle | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | 1 | Justificado por menor variación en los valles |
| Principios de armonía / sincronización / proporcionalidad | — | — | — | Anulados por el **principio de variación** |
| **Principio de variación** | — | — | — | **Declara que ninguno es regla; impide la falsación** |
| Modelo nominal (18a → 5d) | — | — | — | **Contradicho por los ejemplos del propio capítulo** |
| Ciclo de 28 días | — | — | — | **Justificación circular; sin medición independiente** |
| **Traslación izq/der → asimetría temporal** | **`OHLCV-OK`** | **`CAUSAL`** | **1** | **Reformulada por el propio autor; candidata sólida** |
| Aislamiento de ciclos por inspección/ajuste | `OHLCV-OK` | **`LOOK-AHEAD-GRAVE`** | **No acotado** | **"Ajustar hasta encontrar el ajuste adecuado"** |
| MESA / análisis espectral | `OHLCV-OK` | Verificar | Alto | **No descrito; sólo referenciado** |
| **Régimen cíclico vs tendencial → herramienta** | — | — | — | **Hipótesis valiosa; método no descrito** |
| Ciclos estacionales anuales | `OHLCV-OK` | `CAUSAL` | 1 | **Escala irrelevante para intradiario; sin control de multiple testing** |
| Barómetro de enero / ciclo presidencial | `OTRAS FUENTES` / `OHLCV-OK` | `CAUSAL` | — | Pocas observaciones independientes |
| **Estacionalidad intradiaria** | — | — | — | **`[VACÍO]` No tratada en absoluto** |


---

## 15. ORDENADORES Y SISTEMAS DE CONTRATACIÓN (Cap. 15 — Nivel A)

### 15.1 El encuadre: el ordenador como herramienta

`[MURPHY]` **"Un ordenador puede ayudar a que un buen analista técnico sea incluso mejor, pero no puede transformar a un mal técnico en uno bueno."** Y señala que **"algunas funciones se pueden cumplir más fácilmente con un simple gráfico y una regla que con una máquina"**.

`[MURPHY]` **Y plantea explícitamente el problema de la proliferación**, en una sección titulada *Demasiado de lo mismo*:
> **"Tal vez le parezca que hay demasiados indicadores entre los que elegir. En lugar de simplificar nuestras vidas, ¿el ordenador nos la ha complicado presentándonos tantos elementos más a consideración? Los programas informáticos de gráficos ponen 80 estudios diferentes a disposición del técnico. ¿Cómo se pueden alcanzar conclusiones (y encontrar el tiempo necesario para operar) con tanta información?"**

**Su recomendación práctica**: empezar por las herramientas básicas (precio, volumen, líneas de tendencia, retrocesos, medias, osciladores); **"hay un gran número de osciladores a disposición, elija uno o dos con los que se sienta cómodo y trabaje con ellos"**; usar ciclos y Fibonacci como insumos secundarios.

`[IMPLICACIÓN PARA IRIS]` **Murphy identifica el problema de la proliferación de indicadores y su solución es la selección por comodidad personal del operador.** Es una respuesta razonable para un analista discrecional y **completamente inadecuada para un sistema automático**: no ofrece criterio de selección, y "elegir uno o dos con los que se sienta cómodo" es exactamente la clase de decisión que un procedimiento cuantitativo debe sustituir por evidencia. `[VACÍO]`

### 15.2 Sistema parabólico (SAR / PYR)

`[MURPHY]` De Welles Wilder. **"Un sistema del cambio tiempo/precio siempre presente en el mercado."** Las siglas significan **"paro y retroceso"**: la posición **se da la vuelta cuando se alcanza el límite de protección**. Es un sistema seguidor de tendencia; el nombre viene de la curvatura parabólica de los límites.

**Mecánica**: los puntos de stop se desplazan cada día en la dirección de la tendencia. **Al principio el movimiento es lento, para que la tendencia tenga tiempo de establecerse; a medida que el factor de aceleración aumenta, el SAR se mueve más rápido y en un momento dado alcanza el precio.** Si la tendencia falla o no se materializa, se produce la señal de paro y retroceso. **Los valores se calculan y quedan disponibles para el día siguiente.**

`[IMPLICACIÓN PARA IRIS]` Dos propiedades relevantes:
- **`OHLCV-OK` y `CAUSAL`** — el SAR de mañana se conoce hoy, lo que Murphy subraya explícitamente. **Es una de las poquísimas técnicas del libro donde el valor futuro del indicador es conocido de antemano.**
- **Es un sistema continuo**: siempre en posición, larga o corta. Comparte por tanto la debilidad que Murphy ya señaló para la regla de 4 semanas (§9.8).
- **Parámetros**: factor de aceleración inicial, incremento y máximo. Tres grados de libertad, no especificados numéricamente en el capítulo.

### 15.3 La cifra del 30% y el problema central de los sistemas de tendencia

`[MURPHY]` **El dato más importante del capítulo:**

> **"Como muestran los gráficos, el sistema parabólico funciona muy bien en mercados con una tendencia definida. Obsérvese que mientras las partes con tendencia se capturaban bien, el sistema no paraba de cambiar durante los períodos laterales o de no-tendencia. Esto demuestra la fuerza y la debilidad de la mayoría de los sistemas que siguen la tendencia. Funcionan bien cuando hay períodos de tendencia fuerte, algo que el propio Wilder estima que sucede sólo alrededor del 30 por ciento de las veces. Si dicha estimación se acerca siquiera a la realidad, significaría que un sistema que sigue la tendencia no funcionaría un 70 por ciento de las veces."**

`[IMPLICACIÓN PARA IRIS]` **Esta es la afirmación cuantitativa más consecuente de todo el libro para nuestro proyecto, y merece registrarse con precisión sobre lo que dice y lo que no dice.**

**Lo que dice**: según una estimación de Wilder recogida por Murphy, **los mercados están en tendencia fuerte aproximadamente el 30% del tiempo**, y por tanto todo el aparato seguidor de tendencia —que constituye "la mayoría de las técnicas del libro" (§1.3)— **es inaplicable el 70% del tiempo**.

**Lo que no dice** `[VACÍO]`: no se indica sobre qué mercados, qué período, qué escala temporal ni con qué definición de "tendencia fuerte" se obtuvo esa estimación. **Es una cifra citada sin fuente metodológica.** Y desde luego no hay ninguna medición para futuros sobre índices en frecuencia intradiaria.

`[INTERPRETACIÓN]` **Pero incluso tratada como orden de magnitud, tiene tres consecuencias directas:**
1. **Convierte la identificación del régimen en el problema principal**, no en un refinamiento. Si el 70% del tiempo la herramienta principal no funciona, **saber en qué régimen estamos vale más que perfeccionar la herramienta**.
2. **Refuerza que la abstención es estructural**, no marginal. Conecta directamente con §4.1 (mercado lateral → mantenerse fuera).
3. **Da una escala de expectativa realista**: cualquier sistema seguidor de tendencia que se pruebe sobre MNQ debería evaluarse por separado en los tramos tendenciales y en los laterales, porque el agregado mezcla dos poblaciones muy distintas.

### 15.4 DMI y ADX — el filtro de régimen

`[MURPHY]` **La solución que propone al problema anterior**: **"usar algún tipo de filtro o dispositivo que determine si el mercado está en fase de tendencia."**

**Construcción del DMI**: dos líneas, **+DI** (mide movimientos ascendentes) y **−DI** (descendentes). **Cuando +DI cruza por encima de −DI hay señal de compra; por debajo, señal de venta.**

**La línea ADX**: **"valora el movimiento direccional de los diferentes mercados en una escala de 0 a 100"**. Y su naturaleza: **"La línea ADX es, en esencia, una diferencia suavizada entre las líneas +DI y −DI."**

**Interpretación:**
- **ADX ascendente → el mercado tiene tendencia → candidato para sistemas seguidores de tendencia.**
- **ADX descendente → entorno sin tendencia → inadecuado para ese enfoque.**
- **Umbrales que documenta**: cuando el ADX **empieza a caer desde más arriba de 40**, la tendencia se está debilitando; cuando **vuelve a subir y traspasa el nivel 20**, señal de comienzo de nueva tendencia.

**Uso como filtro**: **"usando el movimiento direccional como filtro, se podrían evitar muchas de las malas señales del sistema parabólico siguiendo sólo aquellas señales que vayan en la misma dirección que las líneas del movimiento direccional."** Y añade: **"todas las señales parabólicas de venta se pueden ignorar"** cuando +DI está por encima de −DI.

`[IMPLICACIÓN PARA IRIS]` **El ADX es, junto con el coeficiente de eficiencia de Kaufman (§9.10), la mejor respuesta del libro a la pregunta de cómo medir el grado de tendencialidad de forma causal.** Propiedades:
- **`OHLCV-OK`** — usa máximo, mínimo y cierre (los movimientos direccionales se calculan sobre diferencias de máximos y mínimos entre barras consecutivas).
- **`CAUSAL`**, sin retardo de pivote.
- **Acotado 0–100 y adimensional.**
- **Un parámetro principal** (la ventana, típicamente 14).
- **Mide magnitud de tendencia sin dirección** — el ADX sube tanto en tendencias alcistas como bajistas. **Eso lo convierte en una variable de contexto pura, no en una señal direccional.**

`[INTERPRETACIÓN]` **Y aquí aparece la quinta arquitectura de dos componentes del libro**, ahora completamente explícita y cuantificada:
```
COMPONENTE DE RÉGIMEN (ADX)  → determina si operar y con qué familia de herramientas
COMPONENTE DE SEÑAL (SAR, +DI/−DI, osciladores) → determina la dirección
```
Es la misma estructura que: análisis/timing (§1.5), escala larga/corta (§8.4, §10.15), precio/volumen (§7.3) y patrón de velas filtrado por oscilador (§12.5). **Cinco formulaciones de la misma idea arquitectónica, provenientes de cinco capítulos y varios autores distintos.** Se registra la convergencia en §33 y §40; **no se resuelve aquí**.

### 15.5 Ventajas y desventajas de los sistemas mecánicos

`[MURPHY]` **Ventajas declaradas (7):**
1. Se elimina la emotividad humana.
2. Mayor disciplina.
3. Mayor consistencia.
4. Las operaciones se hacen en la dirección de la tendencia.
5. **"La participación queda prácticamente garantizada en la dirección de cada una de las tendencias importantes."**
6. Los beneficios pueden circular.
7. Las pérdidas se minimizan.

`[MURPHY]` **Desventajas declaradas (4):**
1. Casi todos los sistemas mecánicos se basan en seguir tendencias.
2. Dependen de las tendencias principales para ser rentables.
3. **No son rentables cuando los mercados no tienen tendencias.**
4. **"Hay largos períodos durante los que los mercados no tienen tendencias."**

**Y el diagnóstico que él considera principal:**
> `[MURPHY]` **"El problema mayor es la imposibilidad del sistema de reconocer cuándo no hay tendencia en el mercado y su incapacidad para detenerse por sí mismo. La medida de un buen sistema es no sólo su capacidad de hacer dinero en mercados con tendencias, sino también su capacidad de conservar el capital durante aquellos períodos en los que no hay tendencias. Esta incapacidad del sistema de autocontrolarse es su mayor debilidad."**

`[IMPLICACIÓN PARA IRIS]` **"La medida de un buen sistema es su capacidad de conservar el capital cuando no hay tendencia"** es un criterio de evaluación explícito y directamente relevante. Reformulado: **el rendimiento debe evaluarse condicionado al régimen, y el desempeño en el régimen desfavorable es tan informativo como el del favorable.** Registrado.

`[MURPHY]` **Segunda desventaja que señala**: los sistemas **"generalmente no tienen en cuenta los posibles cambios del mercado. No reconocen cuándo un mercado ha alcanzado un nivel de apoyo o resistencia a largo plazo, cuándo se dan las divergencias del oscilador, ni un quinto patrón de ondas de Elliott, aunque sea claramente visible. La mayoría de los operadores se pondrían a la defensiva y comenzarían a realizar beneficios, y sin embargo, el sistema se mantendría con la posición."**

`[INTERPRETACIÓN]` **Este pasaje es una defensa del juicio discrecional frente al sistema, y su fuerza depende enteramente de una premisa no demostrada**: que esos elementos (soportes de largo plazo, divergencias, quinta onda) tienen valor predictivo. Si lo tienen, la conclusión correcta **no** es que el operador debe intervenir, sino que **esos elementos deberían incorporarse al sistema como variables**. Murphy no considera esa opción. Registrado como tensión (§38).

### 15.6 Usos alternativos de las señales del sistema

`[MURPHY]` Propone dos usos que no son operar el sistema:

**Como dispositivo disciplinario**: **"las señales se pueden usar como una forma disciplinada de mantener al operador en el lado adecuado de la tendencia principal. No se tomarían posiciones cortas mientras la tendencia del ordenador fuera ascendente."** Razón: **"La dirección de la tendencia puede ser cuestión de opiniones, y las señales del ordenador alivian al operador de un cierto grado de incertidumbre, ya que pueden evitar que caiga en la trampa de 'elegir máximos y mínimos'."**

**Como alerta**: filtro que avisa de cambios de tendencia recientes, permitiendo revisar candidatos rápidamente.

`[IMPLICACIÓN PARA IRIS]` El primer uso es **exactamente la función de filtro direccional** de las arquitecturas de dos componentes. Nótese que aquí el sistema mecánico ocupa el papel de **componente de contexto** y el juicio humano el de **componente de señal** — la asignación inversa a la del §15.4. **Murphy usa la misma estructura con los roles intercambiables según el contexto**, lo que sugiere que la estructura es más robusta que la asignación concreta de papeles.

### 15.7 Software y desarrollo de sistemas propios

`[MURPHY]` Documenta las capacidades de las plataformas de la época: bibliotecas de sistemas habituales que **"se pueden probar, cambiar o crear los suyos propios"**; lenguajes de alto nivel para no programadores; y **"es difícil sobrestimar el valor de ser capaz de desarrollar, probar, incluso optimizar, y luego automatizar nuestras propias ideas sobre operaciones sin ser programador"**.

También menciona **"Herramientas Expertas"**: un indicador que **traza automáticamente líneas de tendencia** y otro que **interpreta patrones de velas**.

`[IMPLICACIÓN PARA IRIS]` `[INTERPRETACIÓN]` La existencia de trazadores automáticos de líneas de tendencia confirma que **la formalización algorítmica de esos objetos es posible** — pero también que **cada implementación fija de una manera concreta los siete grados de libertad identificados en §4.8**, sin que el libro discuta cuál es correcta. El capítulo celebra la capacidad de optimizar sin mencionar en ningún momento el riesgo de sobreajuste asociado, a diferencia del capítulo 9 (§9.9), donde sí lo hacía. **Inconsistencia interna registrada.**

### 15.8 Clasificación

| Concepto | Datos | Causalidad | GL | Observación |
|---|---|---|---|---|
| **Sistema parabólico (SAR)** | **`OHLCV-OK`** | **`CAUSAL`** (valor conocido de antemano) | 3 | Sistema continuo; "inútil en bandas de fluctuación" |
| **+DI / −DI** | **`OHLCV-OK`** | **`CAUSAL`** | 1 | Señal direccional; usa H, L, C |
| **ADX** | **`OHLCV-OK`** | **`CAUSAL`** | 1 | **Magnitud de tendencia sin dirección; variable de contexto pura** |
| Umbrales ADX 20 / 40 | `OHLCV-OK` | `CAUSAL` | 2 | Sin justificación empírica |
| **DMI/ADX como filtro del SAR** | `OHLCV-OK` | `CAUSAL` | 4+ | **Arquitectura de dos componentes explícita** |
| **Estimación del 30% de tiempo en tendencia** | — | — | — | **Sin fuente metodológica; consecuencias mayores si es correcta** |
| Criterio "conservar capital sin tendencia" | — | — | — | **Criterio de evaluación condicionado al régimen** |
| Sistema como filtro disciplinario | `OHLCV-OK` | `CAUSAL` | — | Roles de la arquitectura invertidos |
| Selección de indicadores por comodidad | — | — | — | **`[VACÍO]` Sin criterio objetivo** |
| Optimización de sistemas | — | — | — | **Sin mención del sobreajuste, a diferencia del cap. 9** |


---

## 16. GESTIÓN MONETARIA, TÁCTICAS E INTRADÍA (Cap. 16 — Nivel A)

### 16.1 Los tres elementos de la contratación — la descomposición del problema

`[MURPHY]` La distinción más importante del capítulo, y la formulación más clara del libro sobre la estructura de la decisión:

> **"El pronóstico del precio le dice al operador QUÉ debe hacer (comprar o vender), el cálculo del tiempo le ayuda a decidir CUÁNDO conviene hacerlo, y la gestión monetaria determina QUÉ CANTIDAD debe comprometer en la operación."**

`[MURPHY]` Y sobre el timing repite la advertencia del capítulo 1: **"Es posible estar en la dirección correcta del mercado y perder dinero igualmente en una operación, si el momento no es el adecuado."** Además: **"Por naturaleza, el cálculo del momento es completamente técnico."**

`[IMPLICACIÓN PARA IRIS]` **Esta es una descomposición en tres componentes —dirección, momento, tamaño— que no coincide exactamente con ninguna de las arquitecturas de dos componentes registradas antes, y que conviene mantener separada de ellas.** Es una tercera dimensión del problema que las cinco arquitecturas de §15.4 no cubrían: **el tamaño**. Registrada en §33 y §40 sin resolver su relación con otras descomposiciones.

### 16.2 Gestión monetaria: la valoración del autor

`[MURPHY]` Un pasaje personal que merece registrarse porque es de los pocos donde declara haber cambiado de opinión por la experiencia:

> **"Rápidamente descubrí la diferencia principal entre recomendar una estrategia y ponerla en marcha yo mismo. Lo que me sorprendió fue que la parte más difícil de la transición tenía poco que ver con las estrategias de mercado... Lo que sí cambió fue mi percepción de la importancia de la gestión del dinero. Realmente me sorprendió el impacto que aspectos como el tamaño de la cuenta, la combinación de la cartera y la cantidad de dinero comprometido en cada operación podían tener sobre los resultados finales."**

Y: **"Algunos operadores creen que la gestión monetaria es el ingrediente más importante de un programa de contratación, incluso más importante que la propia manera de operar. No estoy seguro de llegar hasta ese extremo, pero sí creo que no se puede sobrevivir mucho tiempo sin ese elemento."**

`[IMPLICACIÓN PARA IRIS]` **Convergencia notable**: es exactamente la misma tesis que ya aparecía en la etapa anterior sobre bet sizing —que un modelo preciso con mal dimensionamiento pierde dinero—, llegando desde una fuente completamente distinta y por vía de la experiencia práctica en lugar del análisis formal. **No se resuelve la relación entre ambas formulaciones**; se registra en §40.

### 16.3 Las reglas normativas de asignación

`[MURPHY]` Cuatro pautas, declaradas **"bastante normales en el sector de los futuros"**:

| Regla | Contenido |
|---|---|
| **50% del capital** | Total invertido limitado al 50% del capital; el resto en reserva "durante los períodos de adversidad" |
| **10-15% por mercado** | Compromiso en un mercado dado limitado a esa fracción como depósito de margen |
| **5% de riesgo por operación** | **"La cantidad total arriesgada en un mercado determinado debe limitarse al 5% del capital propio."** Determina cuántos contratos operar y dónde colocar el stop |
| **20-25% por grupo** | Protección contra participación excesiva en un grupo correlacionado |

`[IMPLICACIÓN PARA IRIS]` **Clasificación: recomendaciones normativas, no resultados demostrados.** El propio texto las presenta como convención sectorial ("bastante normales en el sector"), no como conclusión de análisis. **No hay derivación, ni justificación, ni referencia a evidencia.** Conforme al encargo: **no se adopta ninguna.**

De las cuatro, **sólo la tercera (riesgo por operación) es conceptualmente aplicable** a un sistema de un instrumento; las otras tres presuponen cartera multiactivo. Y su valor concreto (5%) `[INTERPRETACIÓN]` es alto para los estándares habituales, lo que ilustra que es una convención de época y sector, no una constante.

### 16.4 Coeficiente recompensa/riesgo y la tasa de acierto

`[MURPHY]` **El dato más importante de la sección:**

> **"Los mejores operadores de futuros ganan dinero solamente en el 40 por ciento de sus operaciones. Sí, ha leído bien. La mayor parte de las operaciones acaba en pérdidas."**

**Su explicación**: como el margen es bajo, **"incluso un mínimo movimiento en la dirección equivocada lleva a una liquidación forzosa"**, de modo que un operador **"puede tener que sondear un mercado varias veces antes de encontrar el movimiento que está buscando"**.

**Y la consecuencia**: **"Como casi todos los operadores pierden, la única forma de salir airoso es asegurarse de que la cantidad de dinero de las operaciones ganadoras sea mayor que la de las perdedoras."** De ahí el coeficiente recompensa/riesgo, con **"una vara de medir corriente de 3 a 1"**: el potencial de beneficio debe ser al menos tres veces la pérdida posible.

`[IMPLICACIÓN PARA IRIS]` **Este pasaje es directamente relevante y conviene ser preciso sobre su alcance.**

**Lo que aporta**: la afirmación de que **una tasa de acierto del 40% es compatible con rentabilidad si los pagos son asimétricos**. Es exactamente la relación entre precisión, frecuencia y estructura de pagos que ya se registró en la etapa anterior — aquí llegando desde la práctica del sector y sin formalización. **Convergencia entre fuentes registrada; no resuelta.**

**Lo que no aporta** `[VACÍO]`: la cifra del 40% no tiene fuente, período ni muestra. Y **la regla de 3:1 no se deriva de nada**: no se explica por qué 3 y no 2 o 4, ni cómo se relaciona con la tasa de acierto esperada. Nótese que con acierto del 40%, el punto de equilibrio está en una relación de 1,5:1, de modo que 3:1 es una convención conservadora, pero **el texto no hace ese cálculo**.

`[MURPHY]` También registra el problema práctico: **"El objetivo de beneficio (la recompensa) se compara con la pérdida potencial si el negocio va mal (el riesgo)"** — lo que requiere **estimar el objetivo de beneficio antes de operar**, es decir, depende de las técnicas de objetivo de precio de los capítulos 4–6, con todos sus grados de libertad.

### 16.5 Stops: el compromiso declarado

`[MURPHY]` **"Poner límites es un arte."** El operador debe combinar factores técnicos con gestión monetaria, y **considerar la volatilidad del mercado: "a mayor volatilidad de éste, menor rigidez del límite a emplear"**.

**Y formula el compromiso con claridad:**
> **"El operador quiere un límite de protección para estar cerca, de modo que las operaciones con pérdidas sean lo más pequeñas posible, pero los límites de protección puestos demasiado cerca pueden llevar a una liquidación no buscada en las oscilaciones del mercado a corto plazo (o 'ruido'). Los límites de protección puestos demasiado lejos pueden evitar el factor ruido, pero darán pérdidas mayores, o sea que el truco está en encontrar el punto medio adecuado."**

`[IMPLICACIÓN PARA IRIS]` **Es la cuarta vez que Murphy formula correctamente el mismo compromiso sensibilidad/ruido** (tras filtros de ruptura §4.9, longitud de media §9.4, y parámetros de P&F §11.2) **y la cuarta vez que no ofrece criterio para resolverlo.** Lo que sí aporta aquí, y es nuevo: **la indicación de escalar el stop por la volatilidad**, que convierte un parámetro absoluto en un multiplicador adimensional. `OHLCV-OK`, `CAUSAL`.

**Y una conexión relevante**: el uso de **niveles de apoyo y resistencia para colocar stops** (§16.7) es una alternativa a escalarlos por volatilidad. **Son dos criterios distintos e incompatibles entre sí**, y el libro los presenta ambos sin criterio de elección.

### 16.6 Tácticas de entrada: anticipación, ruptura o reacción

`[MURPHY]` **Plantea el dilema con las tres opciones y sus consecuencias:**

| Táctica | Ventaja | Coste |
|---|---|---|
| **Anticipar la ruptura** | Precio mejor si ocurre | **"Las posibilidades de realizar una mala operación aumentan"** |
| **Entrar en la ruptura** | **"Aumenta las posibilidades de éxito"** | Precio de entrada peor |
| **Esperar la reacción posterior** | "Compromiso sensato" | **"Muchos mercados dinámicos (generalmente los más rentables) no siempre ofrecen una segunda oportunidad"** → riesgo de perder el movimiento |

**Su respuesta**: operar con **múltiples unidades**, tomando una posición pequeña anticipando, comprando más en la ruptura, y añadiendo en la corrección posterior.

`[IMPLICACIÓN PARA IRIS]` **Este es un trade-off explícito entre precisión de entrada y probabilidad de captura, y la solución que ofrece es fraccionar la posición.** `[INTERPRETACIÓN]` Formalizado, equivale a **una función de tamaño creciente con el grado de confirmación** — lo que es conceptualmente distinto de un tamaño único basado en confianza. Registrado como posibilidad conceptual; **no se adopta**.

### 16.7 Las cinco tácticas técnicas de timing

`[MURPHY]` **"El cálculo del tiempo cubre un plazo muy corto... el marco temporal que nos interesa aquí se mide en días, horas y minutos."** Las herramientas son las mismas de los capítulos anteriores:

1. **Tácticas sobre rupturas** (§16.6).
2. **Ruptura de líneas de tendencia** — "una de las señales de entrada o salida más útiles"; también sirven como apoyo/resistencia para entradas.
3. **Apoyo y resistencia** — **"las herramientas gráficas más eficaces para localizar los puntos de entrada y salida"**. La ruptura de resistencia señala nueva posición larga, con stop debajo del apoyo más cercano, o más ajustado justo debajo del punto de ruptura (que ahora funciona como apoyo). **"A efectos de colocar límites protectores, los niveles de apoyo y resistencia son muy valiosos."**
4. **Retrocesos porcentuales** — **"las reacciones que retroceden del 40 al 60 por ciento del avance anterior se pueden utilizar para posiciones nuevas"**. Y explícitamente: **"Los retrocesos porcentuales también se pueden aplicar a los gráficos intradía."**
5. **Huecos de precios.**

`[IMPLICACIÓN PARA IRIS]` **La afirmación de que soportes y resistencias son "las herramientas más eficaces" para entrada, salida y colocación de stops es la valoración más fuerte que Murphy hace de ninguna técnica en todo el libro.** Contrasta con su tratamiento `LOOK-AHEAD-LEVE` (§4.7): son eficaces según él, y a la vez dependientes de pivotes cuya identificación causal requiere retardo. **Tensión registrada.**

Y nótese que **el rango 40-60% aquí no coincide** con los rangos de los capítulos 4 (33-38% mínimo, 62-68% máximo) y 13 (38/50/62). **Tercera parametrización distinta del mismo concepto en el mismo libro.**

### 16.8 Intradía — la sección específicamente relevante

`[MURPHY]` **"Debido a que el cálculo del momento adecuado se relaciona con una acción del mercado a muy corto plazo, los gráficos de precios intradía son especialmente útiles. Resultan imprescindibles para las operaciones diarias, aunque no nos centraremos en este aspecto."**

**Y reitera la jerarquía top-down**: mensual y semanal para perspectiva → **diario, que es "la base de la decisión de operar en sí"** → **"el gráfico intradía es el último al que se recurre, para una precisión aún mayor"**.

**Los ejemplos intradiarios que muestra** (figuras 16.1–16.3): gráficos de **5 minutos** (futuros del S&P 500), **10 minutos** (bonos del tesoro) y **60 minutos** (marco alemán), **todos con estocásticos de 14 barras**.

`[IMPLICACIÓN PARA IRIS]` **Esto es lo más cercano a evidencia intradiaria que ofrece el libro**, y hay que ser exacto sobre su valor:
- **Confirma que el aparato se aplica mecánicamente a barras de 5, 10 y 60 minutos**, con el mismo parámetro (14) que en diario y semanal.
- **Pero son tres gráficos ilustrativos con flechas señalando señales que funcionaron.** No hay conteo de señales fallidas, ni tasa de acierto, ni período de muestra. **Es exposición, no evidencia.**
- **El papel declarado del intradía es subordinado**: refinar el timing de una decisión ya tomada en diario. **IRIS propone lo contrario: que la decisión misma se tome en intradiario.** `[VACÍO]` **El libro no respalda ese uso.**

### 16.9 Puntos pivote intradía — la única técnica intradiaria propia

`[MURPHY]` **La técnica combina siete niveles de precio con cuatro períodos.**

**Los siete puntos pivote:**
- **Del día anterior**: máximo, mínimo y cierre.
- **Del día actual**: apertura, máximo, mínimo y cierre.

**Los cuatro períodos de la sesión actual**: la apertura, **30 minutos después de la apertura**, **el mediodía** (alrededor de las 12:30 de Nueva York) y **35 minutos antes del cierre**. Y precisa: **"Son horarios medios que se pueden ajustar a los mercados individuales."**

**El propósito**: **"lograr entrar antes y tener unos límites de protección muy firmes"**, tratando de **anticipar el nivel al que cerrará el mercado**. **"Las señales de compra o venta aparecen a medida que los puntos pivotes se quiebran a lo largo del día. Cuanto más tarde aparezca la señal, más fuerte será."**

**El ejemplo completo de señal de compra que da:**
1. Si el mercado **abre por encima del cierre del día anterior pero por debajo del máximo del día anterior**, se coloca una **orden stop de compra por encima del máximo del día anterior**.
2. Si se ejecuta, **stop de protección por debajo del mínimo del día actual**.
3. **35 minutos antes del cierre, si no se ha tomado posición**, se coloca **orden de compra por encima del máximo del día actual**, con **stop por debajo de la apertura de la sesión actual**.
4. **"Generalmente, no hay movimientos durante los primeros 30 minutos de la sesión, pero a medida que el día avanza, los puntos pivotes se van ajustando al igual que los límites de protección."**
5. **Requisito final**: los precios deben **cerrar por encima del cierre del día anterior y también de la apertura del día actual**.

`[IMPLICACIÓN PARA IRIS]` **Esta es la única técnica del libro diseñada específicamente para operar dentro de la sesión, y merece una evaluación detallada:**

| Dimensión | Valoración |
|---|---|
| **Datos** | **`OHLCV-OK`** — usa exclusivamente O, H, L, C de la sesión anterior y de la actual en curso |
| **Causalidad** | **`CAUSAL`** — todos los niveles se conocen en el momento; los del día actual se actualizan progresivamente, lo que es legítimo |
| **Objetividad** | **Alta.** Los siete niveles son deterministas, sin pivotes, sin interpretación, sin confirmación posterior |
| **Grados de libertad** | **Los cuatro períodos** (declarados ajustables), la elección de qué niveles usar como disparador, y la regla de escalonamiento |
| **Estructura temporal** | **Introduce el tiempo dentro de la sesión como variable**, con una hipótesis explícita: **"cuanto más tarde aparezca la señal, más fuerte será"** |

`[INTERPRETACIÓN]` **Tres observaciones:**

1. **Es la única técnica del libro donde la hora de la sesión es parte constitutiva de la regla.** Eso conecta con el vacío señalado en §14.7 sobre estacionalidad intradiaria: aquí Murphy usa implícitamente la estructura de la sesión (los primeros 30 minutos son distintos, el cierre es distinto) **sin desarrollar en ningún momento por qué**.
2. **La hipótesis "señal más tardía = señal más fuerte" es falsable y comprobable** con OHLCV. Y tiene un mecanismo plausible implícito: cuanto más avanzada la sesión, más información acumulada y menos tiempo para revertir.
3. **La técnica presupone una sesión con apertura y cierre bien definidos.** MNQ opera casi 24 horas; aplicarla exigiría definir qué constituye "la sesión", lo que es una decisión no trivial que el libro no contempla. `[VACÍO]`

### 16.10 El resumen de 20 puntos

`[MURPHY]` Las que considero relevantes para registrar, de su lista final:

- **"Operar en la dirección de la tendencia intermedia."**
- **"En las tendencias al alza, comprar las caídas; en las tendencias a la baja, vender las subidas."**
- **"Dejar que las ganancias corran y frenar las pérdidas."**
- **"Emplear un coeficiente recompensa/riesgo de 3 a 1 como mínimo."**
- **Pirámide**: cada nivel sucesivo más pequeño; **añadir sólo a posiciones ganadoras; nunca a una perdedora**; ajustar stops al umbral de rentabilidad.
- **"Liquidar antes las posiciones con pérdidas que las que dan ganancias."**
- **"Pasar del plazo largo al corto."**
- **"Utilizar gráficos intradía para afinar los momentos de entrada y salida."**
- **"Dominar las operaciones interdía antes de probar las operaciones intradía."**
- **"Hacerlo todo de manera sencilla. Lo que es más complicado, no siempre es mejor."**

`[IMPLICACIÓN PARA IRIS]` **Todas son recomendaciones normativas sin derivación ni evidencia**, conforme al encargo de distinguir norma de resultado demostrado. **No se adopta ninguna.**

Dos merecen comentario:
- **"Dominar las operaciones interdía antes de probar las intradía"** es otra indicación —la tercera tras §8.5 y §16.8— de que **el autor considera el intradiario más difícil, no equivalente**.
- **"Lo más complicado no siempre es mejor"** coincide con el principio de mínima complejidad que el encargo exige aplicar. Es de las pocas afirmaciones metodológicas transversales del libro.

### 16.11 Qué hacer tras rachas — la única idea contraintuitiva

`[MURPHY]` **"El peor momento para aumentar el tamaño de los compromisos es después de una época de ganancias, porque es como comprar en un mercado sobrecomprado en una tendencia al alza. Lo más inteligente (aunque va en contra de la naturaleza humana) es comenzar a incrementar los compromisos después de una caída de los valores, porque esto aumenta las posibilidades de que los compromisos más fuertes se verifiquen cerca de los valles en lugar de los picos."**

`[INTERPRETACIÓN]` **Es una hipótesis de reversión a la media aplicada a la propia curva de resultados del sistema**, y es falsable: ¿está la rentabilidad de la estrategia autocorrelacionada negativamente? **Pero es directamente contraria a la práctica habitual de escalar con el capital, y el libro no aporta evidencia.** Además, presupone que las rachas de pérdidas son transitorias y no señal de degradación del edge —supuesto que las otras fuentes tratan con mucha más cautela. **Tensión registrada.**

### 16.12 Clasificación

| Concepto | Datos | Causalidad | Tipo | Observación |
|---|---|---|---|---|
| **Descomposición qué / cuándo / cuánto** | — | — | Marco conceptual | **Tres componentes, incluido el tamaño** |
| Reglas 50% / 10-15% / 5% / 20-25% | — | — | **Normativa sectorial** | Sin derivación; tres presuponen cartera |
| **Tasa de acierto del 40%** | — | — | Afirmación sin fuente | **Acierto bajo compatible con rentabilidad** |
| **Coeficiente recompensa/riesgo 3:1** | `OHLCV-OK` si se fija objetivo | `CAUSAL` | **Normativa** | No derivado; requiere objetivo de precio |
| **Stop escalado por volatilidad** | **`OHLCV-OK`** | **`CAUSAL`** | Principio | **Convierte parámetro absoluto en multiplicador** |
| Stop en soporte/resistencia | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Principio | **Criterio incompatible con el anterior** |
| Anticipar / entrar / esperar la ruptura | `OHLCV-OK` | `CAUSAL` | Trade-off | Solución: fraccionar posición |
| Retrocesos 40-60% para entrada | `OHLCV-OK` | `LOOK-AHEAD-LEVE` | Táctica | **Tercera parametrización distinta en el libro** |
| **Puntos pivote intradía** | **`OHLCV-OK`** | **`CAUSAL`** | **Técnica intradiaria propia** | **Única del libro; objetiva; usa hora de sesión** |
| "Señal más tardía = más fuerte" | `OHLCV-OK` | `CAUSAL` | **Hipótesis falsable** | Sin evidencia |
| Definición de "sesión" en un mercado 24h | — | — | — | **`[VACÍO]`** |
| Pirámide y reglas de la lista final | — | — | **Normativa** | Sin evidencia |
| Aumentar tamaño tras pérdidas | `OHLCV-OK` | `CAUSAL` | **Hipótesis falsable** | Contraria a la práctica; sin evidencia |
| "Dominar interdía antes que intradía" | — | — | Advertencia | **Tercera señal de que el autor ve el intradía como más difícil** |


---

## 17. ANÁLISIS ENTRE MERCADOS (Cap. 17 — Nivel D)

### 17.1 Contenido

`[MURPHY]` El capítulo desarrolla las relaciones sistemáticas entre cuatro sectores: **obligaciones, acciones, materias primas y el dólar**. Las relaciones principales que documenta:

| Relación | Signo | Mecanismo declarado |
|---|---|---|
| **Obligaciones ↔ acciones** | Positiva | Los precios de las obligaciones se mueven en dirección opuesta a los tipos; tipos a la baja son positivos para las acciones. **"Los futuros de obligaciones se pueden considerar como un importante indicador para el mercado de valores"** |
| **Obligaciones ↔ materias primas** | Negativa | Inflación |
| **Materias primas ↔ dólar** | Negativa | — |
| **Futuros ↔ contado (S&P 500)** | Prima que **"se reduce a medida que el contrato llega a su vencimiento"** | Arbitraje |

`[MURPHY]` **Fuerza relativa**: cociente entre dos series, usado para seleccionar sectores y valores. El proceso que describe es descendente: determinar si el clima favorece obligaciones, bienes o valores → sectores con mejor fuerza relativa → valores individuales dentro de esos sectores.

`[MURPHY]` **Correlación entre mercados**: los programas permiten medirla; **"midiendo el grado de correlación, el operador puede establecer cuánto énfasis debe poner en una determinada relación"**. Más peso a las correlaciones altas, menos a las cercanas a cero.

`[MURPHY]` **Y una advertencia de estabilidad que es la parte más valiosa del capítulo:**
> **"Los principios entre mercados descritos aquí se basan en las tendencias que han tenido los mercados a partir de 1970."** Y sobre el escenario deflacionario: **"el resultado fue que los mercados de obligaciones y valores comenzaron a separarse... Si hay deflación, y cuando la haya, las relaciones entre mercados seguirán presentes, pero de modo diferente."**

### 17.2 Evaluación

**Clasificación: `OTRAS FUENTES`** en su totalidad. Requiere series de bonos, índices, materias primas y divisas. **Conforme al encargo, no se amplía el alcance del proyecto.**

`[IMPLICACIÓN PARA IRIS]` **Lo que se renuncia**, documentado:
- **Información sobre el estado macro-financiero** que, según Murphy, **anticipa movimientos del mercado de valores** — y el MNQ es un futuro sobre índice bursátil, de modo que la relación bonos→acciones sería directamente pertinente si tuviéramos los datos.
- **Corroboración desde una fuente genuinamente independiente del propio precio.** Es la cuarta renuncia de este tipo, tras la confirmación entre índices de Dow (§2), el interés abierto (§7.6) y los indicadores de sentimiento (§10.16).

`[INTERPRETACIÓN]` **Y lo que rescatamos como principio, no como técnica:**
1. **La advertencia sobre inestabilidad de las relaciones.** Murphy declara que sus relaciones se basan en el régimen 1970-1998 y que un cambio de régimen (deflación) **las altera sin anularlas**. Es un reconocimiento explícito de **no estacionariedad de las relaciones aprendidas** — y el más claro del libro. Aplicable a cualquier relación que IRIS aprenda.
2. **La idea de ponderar una relación por su correlación medida** en lugar de asumirla constante.

**Nivel: D.** No aplicable, pero la advertencia de inestabilidad se conserva.

---

## 18. INDICADORES BURSÁTILES (Cap. 18 — Nivel D)

### 18.1 Contenido

`[MURPHY]` El capítulo trata la **amplitud de mercado**: medidas construidas a partir del comportamiento del conjunto de valores, no de un índice.

**El ejemplo que abre el capítulo es ilustrativo del propósito**: un día en que el Dow ganó 12,20 puntos, pero **había más valores descendentes (1.559) que ascendentes (1.327)**, más volumen descendente que ascendente, y un tick de cierre de −135. **"La amplitud del mercado en realidad fue negativa para aquel día en particular, aunque el propio índice Dow cerrara más alto."**

**Y la comparación entre índices el mismo día**: Dow +0,16%, S&P 500 −0,07%, Nasdaq compuesto −0,92%, Russell 2000 −0,89%. **"Cuanto más amplio era el promedio, peor había funcionado."**

**Los indicadores que documenta:**

| Indicador | Construcción | Datos |
|---|---|---|
| **Línea Avance/Declive** | Diferencia acumulada entre valores que suben y bajan | `OTRAS FUENTES` |
| **Divergencia AD** | La línea AD no confirma el nuevo máximo del índice | `OTRAS FUENTES` |
| **Oscilador de McClellan / índice acumulativo** | Derivados de la línea AD | `OTRAS FUENTES` |
| **Nuevos máximos vs nuevos mínimos** | Valores en máximo/mínimo de 52 semanas | `OTRAS FUENTES` |
| **Volumen al alza vs a la baja** | Volumen de los valores que suben frente a los que bajan | `OTRAS FUENTES` |
| **Índice Arms (TRIN)** | Combina ratios de avance/declive y de volumen. **Media de 10 días: >1,20 sobrevendido, <0,70 sobrecomprado** | `OTRAS FUENTES` |
| **TICK** | **"Mide la diferencia entre el número de valores que operan en una fluctuación al alza y el de los que operan a la baja"**; **"una versión minuto a minuto de la línea diaria de avance-declive"** | `OTRAS FUENTES` |
| **Equivolumen** | Formato gráfico donde el ancho de la barra representa el volumen | `OHLCV-OK` |

`[MURPHY]` **Uso intradiario**: **"El índice Arms se puede usar junto con el indicador TICK para las operaciones intradía. Cuando se combinan ambos durante el día, un indicador TICK ascendente y un índice Arms descendente son positivos."**

### 18.2 Evaluación

**Clasificación: `OTRAS FUENTES`** salvo el equivolumen.

`[IMPLICACIÓN PARA IRIS]` **Conforme al encargo, no se intenta recrear estos indicadores artificialmente usando sólo MNQ. No es posible: miden la dispersión del comportamiento entre miles de valores, y un futuro sobre índice es un único precio agregado.**

**Lo que se renuncia, y por qué importa especialmente en nuestro caso:**

`[INTERPRETACIÓN]` **El MNQ es un futuro sobre un índice de 100 valores.** Toda la información de amplitud —cuántos de esos 100 suben, con qué volumen, cuántos en máximos— **existe y es directamente relevante para el instrumento que operamos**, y el capítulo entero argumenta que **el índice puede subir mientras la amplitud subyacente se deteriora**. Esa es precisamente la clase de divergencia que Murphy considera **"una de las mejores señales anticipadas de inminentes cambios de tendencia"** (§6.9).

**Es, de las cuatro renuncias documentadas, la que tiene el vínculo más directo con nuestro instrumento**, porque no requeriría un mercado distinto sino la descomposición del propio índice. **Se documenta como limitación; no se propone incorporarla.**

**Y el TICK merece mención aparte**: es el único indicador del libro que Murphy describe explícitamente como **minuto a minuto** y de uso intradiario. `[VACÍO]` **No hay ningún sustituto construible desde OHLCV.**

**Nivel: D.**

---

## 19. RESUMEN Y LISTA DE COMPROBACIÓN (Cap. 19 — Nivel B)

### 19.1 La lista de comprobación técnica

`[MURPHY]` **23 preguntas de análisis** más **7 de ejecución**. Las de análisis, agrupadas:

**Contexto y escala** (1–4): dirección del mercado general y de los sectores; qué indican los gráficos semanales y mensuales; si las tendencias principal, intermedia y menor son ascendentes, descendentes o laterales.

**Estructura de precio** (5–9): niveles de apoyo y resistencia; líneas de tendencia y canales; **si volumen e interés abierto confirman el movimiento**; dónde están los retrocesos de 33, 50 y 66%; si hay huecos y de qué tipo.

**Patrones** (10–12): patrones de cambio; de continuidad; sus objetivos de precio.

**Indicadores** (13–16): dirección de las medias móviles; si los osciladores están sobrecomprados o sobrevendidos; **si hay divergencias**; si los números de opinión contraria indican extremos.

**Elliott y ciclos** (17–21): patrón de ondas; patrones de 3 o 5 ondas; retrocesos o proyecciones de Fibonacci; máximos o mínimos cíclicos próximos; **traslación a derecha o izquierda**.

**Sistemas y formatos alternativos** (22–23): dirección de la tendencia informatizada; qué indican los gráficos de puntos y figuras o de velas.

**Las 7 de ejecución**: cuál será la tendencia en los próximos meses; comprar o vender; cuántas unidades; cuánto arriesgar si me equivoco; cuál es el objetivo de beneficios; por dónde entrar; qué tipo de orden; dónde el stop.

`[MURPHY]` **Y la valoración que hace de su propia lista:**
> **"Seguir la lista de comprobación no es garantía de llegar a las conclusiones adecuadas, ya que sólo está pensada para ayudarle a hacerse las preguntas pertinentes."**

`[IMPLICACIÓN PARA IRIS]` **La lista es la síntesis operativa del libro y revela su estructura real:**

1. **Es una lista de preguntas, no un algoritmo.** No hay pesos, no hay reglas de combinación, no hay procedimiento de resolución cuando las respuestas se contradicen. `[VACÍO]` **El libro no explica en ningún momento cómo agregar 23 lecturas potencialmente discordantes en una decisión.**
2. **Confirma el orden top-down** (contexto → estructura → patrones → indicadores) que aparecía en §8.4.
3. **Separa nítidamente análisis (23 preguntas) de ejecución (7 preguntas)**, y las siete de ejecución son **exactamente los componentes que un sistema debe especificar**: dirección, tamaño, riesgo, objetivo, entrada, tipo de orden, stop.
4. `[INTERPRETACIÓN]` **La agregación discrecional de 23 señales es precisamente el punto donde un enfoque cuantitativo aporta algo distinto**: no una respuesta mejor a cada pregunta, sino **un procedimiento reproducible de combinación**. Esta es, en mi lectura, la diferencia funcional más clara entre lo que Murphy ofrece y lo que IRIS necesita.

### 19.2 Coordinación con el análisis fundamental

`[MURPHY]` **"Yo creo que los factores técnicos van por delante de los fundamentos conocidos, pero también creo que cualquier movimiento importante del mercado debe tener su origen en factores fundamentales subyacentes."** Sugerencia práctica: el técnico puede preguntar **"qué tendría que pasar fundamentalmente para justificar un movimiento significativo"**; y **"ver la forma en que el mercado reacciona a noticias fundamentales puede ser una excelente indicación técnica"**.

`[INTERPRETACIÓN]` **Esta última observación es interesante y no está desarrollada en el libro**: la reacción del precio a una noticia conocida es información sobre el estado del mercado. Requeriría un calendario de eventos (`OTRAS FUENTES`), pero **un proxy parcial —el comportamiento del precio en torno a horas de publicación conocidas— sería `OHLCV-OK`**. Es reconstrucción nuestra.

### 19.3 La evidencia externa que cita — el único respaldo empírico del libro

`[MURPHY]` **Dos referencias a estudios de la Reserva Federal**, y son la única evidencia estadística externa que el libro invoca en 547 páginas:

1. **Banco de la Reserva Federal de Nueva York, agosto de 1995** (Osler y Chang, *"Head and Shoulders: Not Just a Flaky Pattern"*), sobre la validez del patrón de cabeza y hombros en divisas. La frase que Murphy cita: **"El análisis técnico, la predicción del movimiento de los precios basada en movimientos anteriores, ha demostrado originar beneficios estadísticamente significativos a pesar de su incompatibilidad con la idea de mercado eficaz."**

2. **Banco de la Reserva Federal de St. Louis, otoño de 1997** (Neely), citado así: **"El éxito de las reglas de las operaciones técnicas... es típico de un cierto número de estudios recientes que demuestran que la sencilla hipótesis del mercado eficaz falla de manera importante al describir el funcionamiento real del mercado de divisas."**

`[IMPLICACIÓN PARA IRIS]` **Conviene ser preciso sobre qué respaldan y qué no:**

**Lo que respaldan**: que existen estudios académicos publicados por bancos centrales que encuentran rentabilidad estadísticamente significativa en reglas técnicas.

**Lo que no respaldan** `[VACÍO]`:
- **Ambos estudios son sobre el mercado de divisas.** Ninguno sobre futuros de índices bursátiles.
- **Ninguno es intradiario.**
- **Murphy no reporta magnitudes, ni si los resultados son netos de costes, ni el período, ni si sobreviven a corrección por multiple testing.**
- **Son citas de dos frases introductorias**, no un examen de la metodología ni de los resultados.
- **Son de 1995 y 1997**, es decir, anteriores a la generalización del trading algorítmico.

`[INTERPRETACIÓN]` **Registro esto con neutralidad**: la existencia de estos estudios es un dato real y contrasta con la ausencia total de evidencia propia en el libro. Pero **citar la frase introductoria de dos artículos no equivale a aportar evidencia**, y el libro no la examina. Para IRIS, la conclusión operativa es que **existen antecedentes académicos que merecerían consultarse directamente en la etapa de síntesis**, no que las técnicas de Murphy estén validadas.

### 19.4 El análisis técnico bajo otros nombres

`[MURPHY]` Observa que la disciplina se practica bajo denominaciones distintas: **analistas cuantitativos** que buscan valores sobrecomprados o sobrevendidos ("los números que utilizan son los mismos que estudian los técnicos"); **operadores del momento** que usan fuerza relativa; economistas que hablan de la "tendencia" de sus gráficos; e incluso el P/E, porque **"cuando se introduce el precio en la ecuación, se está entrando en la esfera del análisis técnico"**. Y las **finanzas conductuales** como reinvención académica.

`[INTERPRETACIÓN]` **El argumento es en parte retórico** — llamar análisis técnico a cualquier uso de precios diluye la definición hasta hacerla vacía. Pero contiene una observación válida y pertinente para IRIS: **momento y fuerza relativa son conceptos que la literatura cuantitativa también usa**, lo que sugiere que el solapamiento entre este cuerpo de conocimiento y el de las fuentes anteriores es mayor de lo que la diferencia de vocabulario sugiere. **Se registra para la síntesis.**


---

## 20. APÉNDICES A, B Y C

### 20.A — Indicadores técnicos avanzados (Apéndice A — Nivel C)

#### 20.A.1 Índice de la Demanda (Sibbet)

`[MURPHY]` Combina **precio y volumen** calculando dos valores —**presión compradora (PC)** y **presión vendedora (PV)**— y su cociente. La fórmula que reproduce:

- **Si los precios suben**: `PC = Volumen`; `PV = V/P`, donde P es el porcentaje de cambio del precio.
- **Si los precios bajan**: se invierten.
- P se modifica multiplicándolo por una constante `K = (3 × C) / VM`, donde **C es el cierre y VM es la media de 10 días del rango de dos días** (máximo más alto menos mínimo más bajo).
- Si PC > PV, entonces `ID = PV/PC`.

**Interpretación**: valores por encima de cero positivos, por debajo negativos. Se usa para **divergencias** y para **trazar líneas de tendencia sobre el propio indicador**, que según Murphy **"generalmente se rompen bastante antes que las líneas de tendencia del precio"**.

`[IMPLICACIÓN PARA IRIS]` **Clasificación: `OHLCV-OK`, `CAUSAL`.** Es notable porque **VM se construye con máximos y mínimos de dos barras** — usa el rango, no sólo cierres. Estructuralmente es **una medida de volumen normalizada por movimiento de precio, escalada por volatilidad reciente**, lo que la sitúa en la familia de medidas de "esfuerzo frente a resultado". `[INTERPRETACIÓN]` Conceptualmente próxima a la lambda de Amihud registrada en la fuente anterior, aunque con construcción distinta. **Dos parámetros** (la ventana de 10 y la constante 3).

La afirmación de que sus líneas de tendencia se rompen antes que las del precio es **la misma propiedad matemática de las derivadas ya señalada en §10.3**: un indicador construido sobre tasas de cambio necesariamente gira antes que el nivel. `[VACÍO]` Sin evidencia de que ese adelanto se traduzca en valor predictivo.

#### 20.A.2 Índice de Rentabilidad de Herrick (IRH)

`[MURPHY]` Usa **precio, volumen e interés abierto** para determinar flujos monetarios. Positivo = precios al alza con interés abierto subiendo; negativo = fondos retirándose. Su utilidad declarada es detectar divergencias entre precio e interés abierto, porque **"el pánico comprador o vendedor normalmente se puede identificar con el análisis del interés abierto"**.

`[MURPHY]` Advertencia práctica: **"es más eficaz cuando se usa en la información semanal, porque hay menos señales falsas evidentes"**; en información diaria **"cruzará la línea cero por encima y por debajo varias veces antes de que aparezca una señal de compra o de venta que dure más"**.

**Clasificación: `OTRAS FUENTES`.** Requiere interés abierto. **No se propone incorporarlo.** Y nótese que su propio autor lo desaconseja en frecuencia diaria, lo que lo hace aún menos pertinente en intradiario.

#### 20.A.3 Bandas STARC y canales de Keltner — el hallazgo del apéndice

`[MURPHY]`

| | **Bandas STARC (Stoller)** | **Canales de Keltner** |
|---|---|---|
| **Construcción** | **Fluctuación real media (ATR) × 2**, sumada/restada de una **media móvil de 6 períodos** | **ATR de 10 períodos × 2**, sumado/restado de una **EMA de 20 períodos** |
| **Interpretación** | **Reversión**: "cuando los precios están cerca o por encima de STARC+, es un momento de alto riesgo para comprar y de bajo riesgo para vender" | **Continuación**: "cuando los precios cierran por encima de la banda +, aparece una señal positiva que indica una **ruptura en la volatilidad al alza**" |
| **Uso declarado** | **Filtro** para no perseguir el mercado | **Señal de ruptura**; "en muchos aspectos, se trata de una representación gráfica del sistema de canal de cuatro semanas del capítulo 9" |

`[MURPHY]` Sobre STARC: **"Estas bandas funcionan bien en todo tipo de marco temporal, incluso en gráficos de barras de 5 a 10 minutos."** Y sobre ambas: **"Ninguna de ellas es un sistema de contratación en sí, son herramientas adicionales."**

`[IMPLICACIÓN PARA IRIS]` **Esto es lo más relevante del apéndice A, y merece subrayarse:**

**Dos indicadores estructuralmente casi idénticos —ATR multiplicado por dos alrededor de una media— reciben interpretaciones operativas exactamente opuestas.** STARC dice que tocar la banda superior es señal de venta; Keltner dice que cerrar por encima es señal de compra. **La única diferencia técnica es la longitud de la media (6 vs 20) y del ATR (implícito vs 10).**

`[INTERPRETACIÓN]` Esto es **el tercer caso documentado en el libro de una misma variable con reglas de signo opuesto**, tras el CCI (§10.6) y el rectángulo (§6.6). Y es el más nítido, porque aquí la construcción matemática es prácticamente la misma. La conclusión que extraigo:

> **La distancia normalizada del precio a una media es una variable de estado bien definida y `OHLCV-OK`. Lo que no está definido —ni en este apéndice ni en el resto del libro— es qué predice.** Que el análisis técnico haya producido dos indicadores casi idénticos con doctrinas contrarias indica que **la relación entre esa variable y el retorno futuro no es monótona ni estable, o depende de un contexto que ninguno de los dos especifica.**

`[IMPLICACIÓN PARA IRIS]` Esa observación es directamente aprovechable como **hipótesis de interacción**: la relación entre desviación normalizada y retorno futuro **cambia de signo según el régimen** — reversión en rango, continuación en ruptura. Es exactamente la misma estructura que Murphy describe en el "dilema de la ruptura" (§10.14) y que subyace a la oposición medias/osciladores (§9.12). **Es formalizable y falsable; no se adopta.**

**Clasificación de ambas: `OHLCV-OK`, `CAUSAL`, 2 parámetros.** El ATR usa máximo, mínimo y cierre previo, todo disponible.

`[INTERPRETACIÓN]` Nótese además que **el ATR es la medida de volatilidad más económica del libro** — un parámetro, causal, usa el rango completo — y aparece sólo en este apéndice y en la advertencia sobre stops de §16.5, nunca en el cuerpo principal.

---

### 20.B — Market Profile (Apéndice B — Nivel C)

#### 20.B.1 Qué es

`[MURPHY]` **"Visualícelo simplemente como una distribución de la frecuencia de precios representada como un histograma, pero apoyado sobre un costado."** El elemento central es **la curva normal** usada para mostrar la evolución de la distribución de precios; aceptado ese supuesto, se puede identificar un precio modal, computar una dispersión y **"hacer declaraciones de probabilidad con respecto a la distribución de precios"**.

**Construcción**: se asigna **una letra a cada precio dentro del rango de cada período** (A al primero, B al segundo…) y se colapsan todos los rangos hacia la izquierda. Cada letra es una **TPO (Time Price Opportunity)**: **"el precio específico al que operó un mercado en un período concreto"**. El CBOT asigna una letra a **cada período de media hora, las 24 horas del día**.

#### 20.B.2 El modelo de comportamiento

`[MURPHY]` La estructura conceptual, que es lo verdaderamente distintivo del apéndice:

**Dos clases de participantes por marco temporal:**
- **Corto plazo**: **"obligados a realizar las operaciones hoy"** (locales, operadores del día). **"Como su tiempo para actuar es limitado, el operador a corto plazo busca un precio justo."** Compradores y vendedores de corto plazo **operan entre sí al mismo tiempo y al mismo precio**.
- **Largo plazo**: **"No están obligados a operar hoy y tienen al tiempo de aliado, por lo tanto pueden buscar un precio más ventajoso."** Los compradores buscan precios más bajos y los vendedores más altos; **"como su objetivo de precios no coincide, no operan los unos con los otros al mismo precio y al mismo tiempo"**.

**Consecuencia estructural declarada**: **"El equilibrio inicial generalmente queda establecido en la primera hora de actividad por los compradores y vendedores a corto plazo en su búsqueda de un precio justo."** Los precios por encima y por debajo del área de valor **"ofrecen oportunidades ventajosas para los operadores a más largo plazo"**, que al entrar con volumen **extienden el rango**. Y: **"el papel del operador a más largo plazo es mover al mercado de forma direccional"**.

**Precio contra valor:**
- **Precios aceptados**: **"un área de precios en la que el mercado opera sin restricción de tiempo"**.
- **Precios rechazados**: **"un área de precios en la que el mercado pasa muy poco tiempo"**; se consideran **excesivos**, un **"máximo o mínimo injusto"**.
- **"El precio es observable y objetivo, mientras que el valor es percibido y subjetivo."**

**Actividad correspondiente vs de iniciación**: **"los precios ascendentes hacen publicidad a favor de los vendedores, y los precios descendentes a favor de los compradores"**. Si el operador de largo plazo responde como se espera, la actividad es **correspondiente**; si hace lo contrario (comprar tras subidas, vender tras bajadas), es **de iniciación**, y **"cuanto más confiado se vuelva, más posibilidades hay de que realice acciones de iniciación"**.

`[MURPHY]` **Y la declaración de alcance**: **"Market Profile no es un sistema de contratación ni proporciona recomendaciones para operar. La meta del gráfico de perfil es permitirle al usuario ser testigo de la repetición de precios en el tiempo, por lo cual es una herramienta de apoyo a la decisión que requiere que el usuario aplique su opinión personal."**

#### 20.B.3 Compatibilidad con OHLCV — análisis cuidadoso

`[IMPLICACIÓN PARA IRIS]` **Clasificación: `OHLCV-COND`.** Y conviene ser preciso, porque es más aproximable de lo que parece a primera vista **y a la vez la aproximación tiene un supuesto no verificable**.

**Por qué es aproximable:** la construcción TPO **no pondera por volumen ni por tiempo real de permanencia**: asigna una marca binaria a cada nivel de precio que fue tocado durante cada período de media hora. Con barras de un minuto de OHLCV podemos hacer exactamente eso —marcar los niveles entre `L` y `H` de cada barra— **y a resolución más fina que el estándar de 30 minutos del CBOT**.

**El supuesto que introduce**: asumir que **todos los niveles de precio entre `L` y `H` fueron efectivamente negociados** dentro de la barra. En un instrumento líquido como MNQ con barras de un minuto es plausible, **pero es un supuesto no verificable sin datos de tick**. Con barras más largas, el supuesto se vuelve progresivamente peor.

**Lo que se pierde irremediablemente:**
- El **tiempo real de permanencia** en cada nivel dentro de la barra (aunque, como se ha dicho, el TPO original tampoco lo usa).
- La **secuencia intrabar**, que impide reconstruir el orden en que se exploró el rango.
- El **volumen por nivel de precio** — que no forma parte del Market Profile clásico, pero sí de sus derivados modernos. `[CONOCIMIENTO EXTERNO AL LIBRO]` Esta variante no la trata Murphy; la menciono sólo para delimitar qué estamos y qué no estamos aproximando.

**Lo que sí es construible y no requiere supuestos adicionales:**
- **Área de valor** (rango que concentra ~70% de las marcas) y **precio modal**.
- **Asimetría del perfil** — el propio apéndice define equilibrio como distribución simétrica y desequilibrio como distribución sesgada. **Es una variable continua, `OHLCV-COND`, con un parámetro.**
- **Extensión del rango respecto al equilibrio inicial** — Murphy define el equilibrio inicial como el rango de la primera hora, y la extensión posterior como huella del operador de largo plazo. **Eso es directamente medible con OHLCV** una vez definida la sesión.

#### 20.B.4 Valoración

`[IMPLICACIÓN PARA IRIS]` **Lo más valioso del apéndice no es la técnica sino el modelo de mercado**, y por dos razones:

1. **Es el único lugar del libro que ofrece un mecanismo específicamente intradiario y de estructura de sesión.** El equilibrio inicial en la primera hora, la extensión del rango, la distinción entre precios aceptados y rechazados, y el papel direccional del participante sin apremio temporal: todo eso es un relato causal sobre **cómo se forma el rango de una sesión**. Y IRIS opera exactamente en esa escala.
2. **Conecta con el mecanismo de soporte/resistencia de §4.4 desde otro ángulo**: allí el nivel importa por la memoria de los participantes atrapados; aquí importa por el tiempo que el mercado aceptó operar en él. **Son dos hipótesis distintas sobre por qué un nivel debería tener efecto**, y ambas son `OHLCV`-compatibles y falsables.

**Lo que limita su prioridad:**
- El **supuesto de normalidad** de la distribución de precios está declarado y no justificado. `[VACÍO]`
- El propio apéndice declara que **no es un sistema y requiere juicio personal**.
- **Presupone una sesión bien delimitada**, lo que en MNQ (casi 24 horas) es una decisión no trivial — la misma que ya quedó abierta en §16.9.
- **Ninguna evidencia** de valor predictivo.

**Nivel: C.**

---

### 20.C — Creación de un sistema de contratación (Apéndice C — Nivel A)

Redactado por Fred G. Schutzman. **Es, metodológicamente, la sección más importante de todo el libro para IRIS**, y también la que contiene sus tensiones más agudas.

#### 20.C.1 El objetivo declarado

`[MURPHY / Schutzman]` La frase de apertura es una declaración metodológica completa:

> **"Nuestra meta no es desarrollar un sistema que logre los rendimientos más altos usando datos históricos, sino formular un concepto fundado que haya funcionado razonablemente bien en el pasado y que pueda seguir haciéndolo en el futuro."**

**Y la definición operativa de "mecánico"**: **"Mecánico significa objetivo: si 10 personas siguen las mismas reglas y alcanzan los mismos resultados, se dice que esas reglas son objetivas."**

`[IMPLICACIÓN PARA IRIS]` **Ese criterio —reproducibilidad entre operadores independientes— es el estándar exacto que aplicamos en todo este documento para separar lo formalizable de lo interpretativo.** Y nótese que **el propio libro reconoce en el capítulo 1 que el chartismo tradicional no lo cumple** ("los patrones pocas veces son tan claros como para que chartistas experimentados coincidan", §1.7). **El apéndice C es, de hecho, la refutación interna del método principal del libro.**

**Los tres beneficios del enfoque mecánico** que declara: poder probar ideas antes de arriesgar dinero; objetividad frente a la emotividad; y mayor capacidad de trabajo (más mercados, más sistemas, más marcos temporales).

#### 20.C.2 El plan de cinco pasos

`[MURPHY / Schutzman]`

| Paso | Contenido |
|---|---|
| **1. Comenzar con un concepto** | Estudiar gráficos buscando **"elementos de evidencia objetiva que tienen lugar antes de los grandes movimientos"**, y también **"las señales que proporcionan advertencias anticipadas sobre movimientos que probablemente fracasarán"** |
| **2. Transformarlo en normas objetivas** | **"Se trata del paso más difícil de los 5, mucho más difícil de lo que cualquiera de nosotros podría esperar."** Criterio: **"que 100 personas que sigan nuestras normas lleguen exactamente a las mismas conclusiones"** |
| **3. Verificarlo visualmente en los gráficos** | Proceso informal, con dos metas: comprobar que la idea se expresó correctamente, y **"antes de ponernos a crear un complicado código informático, queremos tener pruebas de que la idea es potencialmente rentable"** |
| **4. Comprobarlo formalmente por ordenador** | Codificar y ejecutar sobre datos históricos |
| **5. Evaluar los resultados** | **"¿Tiene sentido o simplemente es una coincidencia?"** |

`[IMPLICACIÓN PARA IRIS]` **El paso 2 es exactamente el problema que este documento ha estado inventariando capítulo por capítulo.** Que el propio autor lo califique de "mucho más difícil de lo que cualquiera podría esperar" **corrobora la contabilidad de grados de libertad** que hemos ido registrando: siete para una línea de tendencia, nueve para cabeza y hombros, no acotados para Elliott.

#### 20.C.3 Los principios de diseño

`[MURPHY / Schutzman]` **Cuatro afirmaciones que merecen registro literal:**

1. **Sobre la coincidencia**: **"Los buenos conceptos generalmente tienen sentido. Si un sistema parece que funciona bien, pero tiene poco sentido para usted, posiblemente se trate de una coincidencia, lo que reduce la probabilidad de que dicho concepto siga funcionando bien en el futuro."**
2. **Sobre las salidas**: **"Diseñar las entradas es difícil, pero diseñar las salidas es incluso más difícil y más importante... Dedique mucho trabajo a mejorar sus salidas, y sus rendimientos mejorarán en relación con su riesgo."** Y su preferencia: **"prefiero los sistemas que no dan marcha atrás automáticamente, prefiero salir de un mercado primero antes de entrar en otro en la dirección opuesta."**
3. **Sobre la optimización**: **"Trate de optimizar lo menos posible. La optimización en base a datos históricos a menudo nos lleva a esperar rendimientos irreales que no se pueden dar en la contratación real. Trate de usar pocos parámetros y aplique la misma técnica a unos cuantos mercados diferentes, porque así mejorará sus posibilidades de éxito a largo plazo al reducir los riesgos del exceso de optimización."**
4. **Sobre la tasa de éxito de las ideas**: **"Recuerde que muy pocas ideas se transformarán en beneficios, generalmente menos del 5 por ciento, y por una u otra razón, la mayoría de las ideas 'brillantes' ni siquiera podrá ser aplicable a una transacción."**

`[IMPLICACIÓN PARA IRIS]` **Los cuatro puntos son directamente aplicables y ninguno requiere datos que no tengamos:**
- El punto 1 es una **exigencia de mecanismo previo**, coincidente con lo que las fuentes anteriores exigen a una estrategia.
- El punto 2 —**la salida importa más que la entrada**— es una afirmación que **ninguna de las dos fuentes anteriores hace con esta rotundidad**, y su preferencia por salir antes de invertir la posición (en lugar de dar la vuelta automáticamente) **es exactamente el mecanismo que genera un estado de no-posición**, ya registrado en §9.8.
- El punto 3 es un **principio de parsimonia paramétrica** coincidente con el criterio de mínima complejidad del encargo.
- El punto 4 es una **tasa base**: menos del 5% de las ideas resultan rentables. `[VACÍO]` Sin fuente, pero es la única estimación del libro sobre la productividad esperada de la investigación, y es un dato de calibración útil.

#### 20.C.4 Las tres categorías de sistemas

`[MURPHY / Schutzman]`

| Categoría | Contenido |
|---|---|
| **Seguimiento de tendencia** | **"Las medias móviles y la regla semanal de Donchian son las metodologías más frecuentes entre los directores financieros"** |
| **Contra tendencia** | (a) **Apoyo/resistencia**: comprar descensos en apoyo, vender subidas en resistencia. (b) **Retrocesos**: comprar retiradas en mercado alcista — **"El peligro de este sistema es que uno nunca sabe hasta dónde llegará el retroceso, lo que dificulta la implementación de una técnica aceptable de salida."** (c) **Osciladores**: comprar sobrevendido, vender sobrecomprado, más fuerte con divergencia — **"es preferible esperar a que haya alguna señal de retroceso en el precio antes de comprar o vender"** |
| **Reconocimiento de patrones** | Visual (cabeza y hombros) y estadístico (patrones de precios temporales) |

`[MURPHY / Schutzman]` Y una observación de cartera: los sistemas contra tendencia **"no deben pasarse por alto, porque aportan un grado de correlación negativa... el resultado es una curva de valor más suave para ambos sistemas combinados que para cada uno de ellos por separado"**.

`[IMPLICACIÓN PARA IRIS]` **La taxonomía en tres categorías es útil y coincide con la estructura que ha ido emergiendo en este análisis**: seguimiento (medias, canales, SAR, ADX), reversión (osciladores, bandas STARC, retrocesos, soportes) y reconocimiento de configuraciones (patrones, velas).

Y la observación sobre correlación negativa entre familias es **una hipótesis falsable con nuestros datos**: si las señales de tendencia y de reversión son negativamente correlacionadas en su resultado, combinarlas reduce varianza. `[INTERPRETACIÓN]` Es la misma lógica que subyace a la hipótesis de régimen (§9.12, §15.4): **funcionan en condiciones complementarias**.

#### 20.C.5 La tensión metodológica central del apéndice

`[MURPHY / Schutzman]` **Y aquí está la afirmación más problemática del libro entero, que debe registrarse íntegra:**

> **"A continuación, debemos decidir cuánta información utilizar al construir nuestro sistema. Yo uso la totalidad de las series de datos, sin guardar nada para hacer la prueba fuera de la muestra (se trata de crear el sistema con una parte de la información y luego probarlo con el resto que no se ha visto). Muchos expertos no estarían de acuerdo con este enfoque, pero yo creo que es el mejor para mi metodología, que descansa sobre conceptos firmes, prácticamente ninguna optimización y un procedimiento de prueba que cubre una amplia gama de parámetros y mercados."**

**Y su justificación epistemológica:**
> **"Yo empiezo con una metodología que creo que es buena y la pongo a prueba para confirmar o desestimar mi teoría, pero he descubierto que casi todos los demás hacen lo contrario, es decir, ponen a prueba una serie de datos para llegar a un sistema de contratación."**

**Los tres criterios de robustez que propone en sustitución del out-of-sample:**
1. **Estabilidad paramétrica**: **"Si considero el uso de un sistema de cruce de medias de 5/20, también espero que funcione razonablemente bien la proporción 6/18, 6/23, 4/21 y 5/19. Si no es así, miro los resultados de 5/20 con escepticismo."**
2. **Estabilidad temporal**: **"Un sistema que funciona bien con el yen japonés en un período reciente de cinco años, también debería funcionar razonablemente bien en cualquier otro intervalo igual."**
3. **Estabilidad entre mercados**: **"Un sistema que ha funcionado bien en el crudo también debería funcionar bien en el gasoil para calefacción y en la gasolina sin plomo durante el mismo período. Si no es así, buscaré una explicación y generalmente descartaré el sistema."**

`[IMPLICACIÓN PARA IRIS]` **Esta sección requiere un análisis cuidadoso porque contiene simultáneamente lo mejor y lo peor del apéndice.**

**El rechazo del out-of-sample es indefendible tal como está formulado**, y conviene decirlo con precisión:
- Contradice directamente lo que el propio libro afirma en el capítulo 9 (§9.9), donde Murphy declara que **"el procedimiento correcto es usar sólo parte de la información sobre precios para elegir los mejores parámetros, y otra parte para examinar los resultados"**. **El cuerpo del libro y su apéndice C sostienen posiciones opuestas sobre la misma cuestión.** `[VACÍO]` La contradicción no se aborda.
- La justificación —que su metodología "descansa sobre conceptos firmes y prácticamente ninguna optimización"— **es circular**: la ausencia de sobreajuste es precisamente lo que el out-of-sample serviría para comprobar, y no puede presuponerse como razón para no comprobarlo.
- La distinción que traza entre su método y el de "casi todos los demás" es **conceptualmente correcta y relevante** (partir de una teoría y testearla, frente a minar datos hasta encontrar un sistema), **pero no sustituye a la validación fuera de muestra**: una teoría formulada tras haber observado los mismos datos sobre los que se testea sigue estando contaminada.

**Los tres criterios de robustez sí son valiosos y merecen conservarse:**
- **La estabilidad paramétrica** es un test operativo excelente y barato: si el resultado se desploma al mover ligeramente los parámetros, era ajuste a ruido. `[IMPLICACIÓN PARA IRIS]` **Es aplicable a IRIS sin ninguna adaptación y no requiere multiactivo.**
- **La estabilidad temporal** es igualmente aplicable, y es **el análogo temporal de la validación cruzada entre contextos** que ya identificamos como la defensa sustitutiva disponible para un instrumento único.
- **La estabilidad entre mercados requiere universo** → `OTRAS FUENTES` para nosotros. **Registrada como cuarta renuncia estructural de este documento** (tras confirmación entre índices, interés abierto, sentimiento y amplitud).

`[INTERPRETACIÓN]` **La lectura correcta, en mi opinión, es que los tres criterios de robustez son un complemento necesario del out-of-sample, no un sustituto.** El apéndice los presenta como alternativa; funcionan mejor como capa adicional. **No resuelvo aquí la tensión con el capítulo 9; la registro en §26.**

#### 20.C.6 Costes y métricas de evaluación

`[MURPHY / Schutzman]` **Sobre costes**: **"Cuando pruebo sistemas no considero los costes de transacción (por ejemplo, comisiones) pero los incluyo como factores al final. Pienso que así el proceso de evaluación es más puro y mis resultados seguirán siendo útiles en caso de que algunos supuestos cambien en el futuro."**

**Tres métricas clave que propone:**

| Métrica | Definición | Umbral |
|---|---|---|
| **Factor beneficio** | Beneficio bruto de operaciones ganadoras / pérdida bruta de las perdedoras. **"Nos dice cuántos dólares ganó nuestro sistema por cada dólar que perdió"** | **"Los operadores a más largo plazo deben buscar factores de beneficio de 2,00 o más, pero los operadores a corto plazo pueden aceptar cifras ligeramente inferiores"** |
| **Promedio de las operaciones** | **"Es la expectativa matemática de nuestro sistema"** | **"Como mínimo debe ser suficiente para cubrir los costes de la transacción, porque si no, perderemos dinero"** |
| **Reducción máxima intradía** | Mayor caída desde un pico hasta un valle. Prefiere calcularla en porcentaje, y **distingue entre reducciones desde el comienzo fijo (dinero propio perdido) y desde un pico de valor (beneficios devueltos)** |

**Preguntas de evaluación cualitativa que plantea**: ¿tiene sentido el concepto o es coincidencia? ¿podemos superar las reducciones? ¿con cuánta rapidez sale el sistema de las operaciones perdedoras? ¿cuánto tiempo permanece en las ganadoras?

`[IMPLICACIÓN PARA IRIS]` **Dos observaciones:**

1. **El criterio del promedio por operación es el más importante y el más directamente aplicable a nuestro caso.** Formulado al revés: **el edge medio por operación debe superar el coste de transacción**. En un sistema intradiario de alta frecuencia de operación, **ese es el criterio que decide la viabilidad antes que ningún otro**, y coincide exactamente con lo que la fuente anterior formalizaba como análisis de viabilidad previa.
2. **Excluir costes durante las pruebas es defendible como diagnóstico e indefendible como evaluación.** El argumento de "pureza" tiene sentido para comparar variantes entre sí; **no lo tiene para decidir si operar**. Y el propio apéndice reconoce implícitamente el problema al exigir que el promedio por operación cubra los costes. `[INTERPRETACIÓN]` En intradiario, donde el edge por operación es pequeño por construcción, **medir sin costes puede invertir el orden de preferencia entre sistemas**, no sólo desplazar todos los resultados por igual: un sistema de alto turnover y otro de bajo turnover no se ven afectados en la misma medida.

#### 20.C.7 Gestión monetaria y diversificación

`[MURPHY / Schutzman]` **"Es la clave de las operaciones rentables, tan importante como un buen sistema de contratación en sí."** Y una recomendación de alcance más amplio de lo habitual: **"Diversifique entre mercados, sistemas, parámetros y marcos temporales."**

`[IMPLICACIÓN PARA IRIS]` De las cuatro dimensiones de diversificación que propone, **tres son accesibles a un proyecto de instrumento único**: sistemas, parámetros y marcos temporales. **Sólo la primera (mercados) queda excluida por nuestra restricción.** `[INTERPRETACIÓN]` Es la formulación más útil de la diversificación en todo el libro precisamente por eso: reconoce que la diversificación no es únicamente entre activos.

#### 20.C.8 Clasificación del Apéndice C

| Concepto | Aplicable a IRIS | Observación |
|---|---|---|
| **Criterio de objetividad (100 personas, mismo resultado)** | **Sí, directamente** | **Estándar de formalizabilidad usado en todo este documento** |
| Plan de 5 pasos | Sí | El paso 2 es donde reside toda la dificultad |
| **"Si funciona pero no tiene sentido, es coincidencia"** | **Sí** | Exigencia de mecanismo previo |
| **"Las salidas importan más que las entradas"** | **Sí** | Afirmación no presente en las fuentes anteriores |
| Salir antes de invertir posición | Sí | **Genera estado de no-posición** |
| **"Optimizar lo menos posible; pocos parámetros"** | **Sí** | Principio de parsimonia |
| Tasa base: <5% de ideas rentables | Sí, como calibración | Sin fuente |
| Tres categorías de sistemas | Sí | Taxonomía coherente con este análisis |
| Correlación negativa entre familias | **Hipótesis falsable** | Base de la combinación de sistemas |
| **Rechazo del out-of-sample** | **NO** | **Contradice al cap. 9; justificación circular** |
| **Estabilidad paramétrica** | **Sí, directamente** | Test barato y valioso |
| **Estabilidad temporal** | **Sí, directamente** | Análogo disponible para instrumento único |
| Estabilidad entre mercados | **`OTRAS FUENTES`** | Cuarta renuncia estructural |
| **Promedio por operación > costes** | **Sí, crítico** | Criterio de viabilidad en intradiario |
| Excluir costes en las pruebas | **NO como evaluación** | Puede invertir el orden entre sistemas de distinto turnover |
| Factor beneficio ≥ 2,00 | Sí, con reservas | Umbral convencional sin derivación |
| Reducción máxima, distinguiendo origen | Sí | Distinción útil |
| Diversificar entre sistemas, parámetros y marcos | **Sí, tres de cuatro** | Diversificación no exclusivamente entre activos |


---
---

# PARTE II — SECCIONES TRANSVERSALES

---

## 21. DESCRIPCIÓN ≠ PREDICCIÓN ≠ OPERACIÓN

Conforme al encargo, esta sección determina **hasta dónde llega realmente Murphy** con cada concepto importante.

### 21.1 Las tres categorías

- **(A) Descripción** — la variable caracteriza el estado actual del mercado. *Ejemplo: "el ADX está en 35 y ascendiendo".*
- **(B) Hipótesis predictiva** — se afirma que ese estado contiene información sobre el futuro. *Ejemplo: "con ADX ascendente, la continuación es más probable que la reversión".*
- **(C) Regla operativa** — se transforma en comprar / vender / no operar.

### 21.2 El patrón general del libro

`[INTERPRETACIÓN]` Tras recorrer los 19 capítulos y los 4 apéndices, el patrón es consistente y merece enunciarse con claridad:

> **Murphy define (A) con precisión considerable, salta a (C) con frecuencia, y prácticamente nunca somete (B) a prueba.**

La estructura típica de una sección del libro es: definición geométrica o algebraica del concepto → explicación psicológica de por qué debería funcionar → uno o varios gráficos con flechas señalando casos en que funcionó → regla operativa. **El eslabón ausente es siempre el mismo: ninguna medición de con qué frecuencia funciona, ninguna comparación contra un baseline, ningún conteo de los casos en que falla.**

### 21.3 Clasificación de los conceptos principales

| Concepto | Murphy llega a | Observación |
|---|---|---|
| **Las tres premisas** | (C) sin pasar por (B) | La premisa 2 es la única formulable como (B) falsable |
| **Definición de tendencia HH/HL** | (A) → (C) | (A) rigurosa; (B) nunca testeada |
| **Mercado lateral → no operar** | (A) → (C) | Criterio de abstención derivado del régimen |
| **Soporte y resistencia** | (A) → (C), **con mecanismo** | El mecanismo psicológico es un (B) implícito y falsable |
| **Determinantes del nivel (tiempo, volumen, recencia)** | **(B) formalizable** | Tres variables continuas con hipótesis asociada |
| **Números redondos** | (A) → (C) | Sin evidencia, sólo anécdotas |
| **Líneas de tendencia y canales** | (A) → (C) | ≥7 grados de libertad no especificados |
| **Fracaso en alcanzar el canal** | **(B) interesante** | Señal definida por lo que *no* ocurrió |
| **Retrocesos porcentuales** | (A) → (C) | Proliferación de niveles impide falsación |
| **Días de cambio** | **(A) con mecanismo** | Murphy es honesto: "en sí misma no tiene gran importancia" |
| **Huecos (evento)** | (A) | La *taxonomía* es retrospectiva |
| **Tamaño del patrón → magnitud posterior** | **(B) comprobable** | Dos variables continuas: altura y duración |
| **Volumen esencial en suelos, no en techos** | **(B) comprobable** | Asimetría falsable |
| **Patrones de cambio y continuidad** | (A) → (C) | ≥9 grados de libertad |
| **Compresión → ruptura** | **(B) comprobable** | Núcleo común sin geometría |
| **Límite temporal del triángulo (2/3–3/4)** | **(B) con caducidad** | Hipótesis original |
| **"El volumen precede al precio"** | **(B) explícita** | La afirmación predictiva más clara del libro; sin evidencia |
| **Volumen confirma la tendencia** | (A) → filtro | Función de validación, no de señal |
| **OBV** | (A) | Limitación admitida por el propio autor |
| **Top-down: escala larga = dirección, corta = timing** | (A) → (C) | Arquitectura, no predicción |
| **Medias móviles** | **(A) declarada** | "Nunca anticipa, sólo reacciona" — el autor lo niega explícitamente como (B) |
| **Ancho de banda de Bollinger** | **(B) falsable** | Alternancia expansión/contracción |
| **Canal de Donchian / regla de 4 semanas** | (C) **con evidencia externa citada** | Único con estudios comparativos referidos |
| **Coeficiente de eficiencia (Kaufman)** | (A) | Tendencialidad como variable continua |
| **Osciladores: lectura extrema** | (A) | **El autor niega que implique reversión inminente** |
| **Momento "se adelanta al precio"** | Propiedad matemática, no (B) | Trivial por construcción de la derivada |
| **Divergencias** | (A) → (C) | Murphy la considera "el valor más grande del oscilador"; sin medición |
| **Premisa del estocástico (cierre cerca del extremo)** | **(B) explícita y falsable** | Afirmación estructural comprobable |
| **CCI / STARC vs Keltner** | (A) con **(C) contradictorias** | Misma variable, reglas opuestas |
| **Velas: geometría** | (A) | Ratios continuos sin parámetros |
| **Velas: patrones nominales** | (A) → (C) | Definiciones explícitamente elásticas |
| **Filtro de patrón por zona pre-señal** | (A) → (C) | Arquitectura de dos componentes |
| **Elliott** | (C) | (B) no falsable |
| **Ciclos** | (A) → (C) | Identificación por ajuste retrospectivo |
| **Traslación izq/der = asimetría temporal** | **(A) reformulada por el autor** | Variable continua causal |
| **ADX** | **(A) pura** | Magnitud de tendencia sin dirección |
| **"30% del tiempo hay tendencia"** | **(B) cuantitativa** | Sin fuente metodológica |
| **Régimen determina la herramienta** | **(B) falsable** | Aparece tres veces (§9.12, §10.1, §14.6, §15.4) |
| **Puntos pivote intradía** | (A) → (C) | Objetiva; con hipótesis "señal tardía = más fuerte" |
| **Tasa de acierto del 40%** | Dato sin fuente | Acierto bajo compatible con rentabilidad |
| **Recompensa/riesgo 3:1** | Normativa | Sin derivación |
| **Market Profile** | (A) | El propio apéndice declara que no es sistema |
| **Estabilidad paramétrica y temporal** | **Criterio metodológico** | Aplicable directamente |

### 21.4 Los conceptos que sí alcanzan (B) de forma falsable

`[INTERPRETACIÓN]` Filtrando la tabla anterior, **los siguientes son los únicos casos donde Murphy formula una hipótesis predictiva comprobable con nuestros datos**, y constituyen el conjunto real de material experimental que esta fuente aporta:

1. **Persistencia > reversión** bajo una definición operativa de tendencia (premisa 2).
2. **La distancia, el tiempo y el volumen acumulados en un nivel** condicionan el comportamiento del precio al reaproximarse (§4.4).
3. **La amplitud del último impulso comparada con la del anterior** anticipa debilitamiento (§4.12).
4. **Tamaño del patrón (altura × duración) → magnitud del movimiento posterior** (§5.1).
5. **El volumen es esencial en suelos y prescindible en techos** — asimetría (§5.1).
6. **Contracción de rango y volumen precede a expansión**, con caducidad temporal (§6.1, §9.6).
7. **El volumen precede al precio** (§7.2).
8. **El cierre tiende al extremo superior del rango en tendencias alcistas** (§10.8).
9. **La relación entre desviación normalizada y retorno futuro cambia de signo según el régimen** (§10.14, §20.A.3).
10. **Existe un régimen tendencial (~30% del tiempo) donde funcionan las medias, y uno lateral donde funcionan los osciladores** (§9.12, §15.3).
11. **Asimetría temporal**: en tendencia alcista se pasa más tiempo subiendo que bajando (§14.4).
12. **En intradiario, una señal más tardía en la sesión es más fuerte** (§16.9).
13. **Los sistemas de tendencia y contra tendencia están negativamente correlacionados** en su resultado (§20.C.4).

**Trece hipótesis falsables, todas `OHLCV`-compatibles, ninguna verificada en el libro.** `[IMPLICACIÓN PARA IRIS]` **Este es, en mi lectura, el producto principal de esta tercera fuente**: no un catálogo de indicadores —que Jansen ya proporcionaba con más rigor matemático— sino **un conjunto de hipótesis de mercado con mecanismo propuesto, formuladas por alguien con conocimiento profundo del dominio, y que nadie ha sometido a prueba en las condiciones que nos interesan.**

---

## 22. TAXONOMÍA DE INFORMACIÓN Y REDUNDANCIA DE FEATURES

Respondiendo al encargo: agrupar los conceptos según **qué información económica o estadística intentan representar**, no según su nombre.

### 22.1 El problema

`[INTERPRETACIÓN]` Un inventario ingenuo de los indicadores del libro produciría fácilmente cincuenta o más variables candidatas. Pero el análisis capítulo por capítulo ha mostrado repetidamente que **muchos son transformaciones de la misma información**, y en algunos casos el propio Murphy lo declara ("casi todos los osciladores se parecen mucho"; "%R es el estocástico invertido"; "el momento de 10 días coincide con el giro de la media de 10 días").

### 22.2 Las ocho familias informativas

| # | Familia | Qué mide | Instrumentos del libro que la representan | Datos |
|---|---|---|---|---|
| **1** | **Dirección / desplazamiento neto** | Cuánto y hacia dónde se ha movido el precio en una ventana | Momento, ROC, pendiente de media, distancia precio-media, histograma de dos medias, MACD y su histograma, cruces de medias, +DI/−DI, línea de tendencia | `OHLCV-OK` |
| **2** | **Tendencialidad / eficiencia** | Qué proporción del camino recorrido se convirtió en desplazamiento neto — magnitud de tendencia **sin dirección** | **ADX**, **coeficiente de eficiencia de Kaufman**, asimetría temporal (traslación), persistencia sobre/bajo una media | `OHLCV-OK` |
| **3** | **Volatilidad / dispersión** | Amplitud de la fluctuación | **ATR**, ancho de Bollinger, ancho de STARC y Keltner, rango de barra, sobres porcentuales, VM del Índice de Demanda | `OHLCV-OK` |
| **4** | **Posición relativa dentro de un rango** | Dónde está el precio respecto a los extremos recientes | **Estocástico %K/%D**, **Williams %R** (=100−%K), canal de Donchian, posición del cierre en la barra, retrocesos porcentuales | `OHLCV-OK` |
| **5** | **Desviación normalizada respecto a una referencia central** | A cuántas unidades de dispersión está el precio de su media | **CCI**, posición dentro de Bollinger, STARC, Keltner | `OHLCV-OK` |
| **6** | **Asimetría alza/baja** | Cómo se reparte la magnitud del movimiento entre subidas y bajadas | **RSI/IFR**, volumen direccional en rectángulos, asimetría del perfil de Market Profile | `OHLCV-OK` |
| **7** | **Actividad / participación** | Intensidad de la negociación y su relación con el movimiento | **Volumen**, OBV, Índice de Demanda, volumen en rupturas y consolidaciones, equivolumen | `OHLCV-OK` |
| **8** | **Estructura de niveles y memoria** | Dónde ha habido concentración previa de actividad y cómo se comporta el precio al volver | Soportes y resistencias, cambio de polaridad, números redondos, área de valor de Market Profile, huecos como niveles, onda 4 como soporte | `OHLCV-OK` con `LOOK-AHEAD-LEVE` |

**Dos dimensiones adicionales que no son familias de indicadores sino ejes de contexto:**

| Eje | Contenido | Datos |
|---|---|---|
| **Escala temporal** | Cada familia puede calcularse sobre múltiples ventanas; el análisis top-down y la combinación semanal/diaria explotan esto | `OHLCV-OK` |
| **Posición en la sesión** | Hora del día, tiempo transcurrido desde la apertura, proximidad al cierre — implícito en puntos pivote y en Market Profile | `OHLCV-OK` |

### 22.3 Observaciones sobre la taxonomía

`[INTERPRETACIÓN]`

**1. Sólo las familias 4, 6, 7 y 8 usan información que no está en la serie de cierres.** Las familias 1, 2, 3 y 5 pueden construirse casi enteramente con cierres (aunque el ATR y el ADX usan máximo y mínimo). **La familia 4 usa High y Low de forma esencial**; la 6 descompone el signo; la 7 usa volumen; la 8 usa estructura histórica.

**2. La redundancia más severa está dentro de la familia 1.** Momento, ROC, MACD, histograma de medias, cruces y pendientes son todos función de la misma cantidad —la variación del precio sobre una ventana— con distintos esquemas de ponderación. `[IMPLICACIÓN PARA IRIS]` **Incluir varios de ellos simultáneamente aportaría poca información y mucha multicolinealidad**, que es exactamente el problema de efectos de sustitución identificado en la etapa anterior.

**3. Las familias 2 y 3 se confunden a menudo pero son distintas.** La volatilidad mide amplitud; la tendencialidad mide qué fracción de esa amplitud es direccional. **Dos mercados con idéntico ATR pueden tener ADX opuestos.** Es una distinción que el libro usa implícitamente (medias en tendencia, osciladores en rango) sin nombrarla así.

**4. La familia 8 es la única con problema de causalidad estructural.** Todas las demás son `CAUSAL` sin retardo; la estructura de niveles requiere identificar pivotes, con el retardo `k` documentado en §4.7.

**5. La familia 2 es la menos poblada y probablemente la más valiosa.** Sólo dos instrumentos del libro la representan bien (ADX y coeficiente de eficiencia), ambos con un parámetro, ambos causales, ambos adimensionales. **Y es la familia sobre la que descansa la hipótesis de régimen**, que es la hipótesis más recurrente del libro.

`[IMPLICACIÓN PARA IRIS]` **Conforme al encargo, no se decide cuáles conservar.** Lo que la taxonomía establece es que **el espacio informativo real del análisis técnico clásico tiene alrededor de ocho dimensiones, no cincuenta**, y que cualquier selección posterior debería razonarse por familia antes que por indicador.

---

## 23. FORMALIZACIÓN PARA MACHINE LEARNING

Tabla de conceptos cuantificables. **Todas las formalizaciones son posibilidades, no decisiones.** "GL" = grados de libertad.

| Concepto Murphy | Qué representa | Formalización posible | Datos | Causal | GL | Look-ahead | Posible función |
|---|---|---|---|---|---|---|---|
| Dirección de tendencia | Familia 1 | Signo y magnitud del retorno sobre ventana | `OHLCV-OK` | Sí | 1 | No | Feature continua / contexto |
| Estructura HH/HL | Familia 8 | Secuencia de pivotes confirmados con retardo `k` | `OHLCV-OK` | Con retardo | 3–4 | **Leve** | Feature categórica / estado |
| **Tendencialidad** | Familia 2 | **ADX**; **coeficiente de eficiencia** = desplazamiento neto / camino recorrido | `OHLCV-OK` | Sí | 1 | No | **Régimen / filtro** |
| Mercado lateral | Familia 2 | Tendencialidad por debajo de umbral | `OHLCV-OK` | Sí | 2 | No | **Filtro de abstención** |
| Soporte/resistencia | Familia 8 | Densidad de actividad previa por nivel, ponderada por recencia | `OHLCV-OK` | Con retardo | 3–5 | **Leve** | Feature continua / contexto |
| Distancia a nivel | Familia 8 | Distancia normalizada por ATR al nivel más próximo | `OHLCV-OK` | Con retardo | 3–5 | Leve | Feature continua |
| Cambio de polaridad | Familia 8 | Indicador de perforación + tiempo desde ella | `OHLCV-OK` | Con confirmación | 2–3 | Leve | Evento |
| Números redondos | Familia 8 | Distancia normalizada al múltiplo más cercano | `OHLCV-OK` | **Sí** | 1 | **No** | Feature continua |
| Línea de tendencia | Familia 8 | Regresión sobre pivotes; distancia y pendiente | `OHLCV-OK` | Con retardo | **≥7** | **Leve** | Feature continua |
| Canal | Familias 3+8 | Ancho y posición dentro | `OHLCV-OK` | Con retardo | ≥7 | Leve | Feature continua |
| **Fracaso en alcanzar el canal** | Familia 1 | Amplitud del último impulso / amplitud del anterior | `OHLCV-OK` | Con retardo | 2 | Leve | **Feature continua** |
| Retroceso porcentual | Familia 4 | Profundidad del retroceso / amplitud del impulso previo | `OHLCV-OK` | Con retardo | 2 | Leve | Feature continua |
| **Día de cambio** | Familias 4+3 | Nuevo extremo + cierre contrario; modulado por rango y volumen | **`OHLCV-OK`** | **Sí** | **0–2** | **No** | **Evento** |
| Hueco | Familia 8 | Tamaño del gap normalizado por ATR | `OHLCV-OK` | **Sí** | 1 | **No** | Evento |
| Tipo de hueco | — | — | — | — | — | **GRAVE** | **No aplicable** |
| **Compresión** | Familia 3 | Ancho de banda / ATR relativo a su propia historia | **`OHLCV-OK`** | **Sí** | **1–2** | **No** | **Régimen / evento** |
| Duración de la compresión | Familia 3 + tiempo | Barras consecutivas bajo umbral de volatilidad | `OHLCV-OK` | Sí | 2 | No | Feature continua |
| Tamaño del patrón | Familias 3+tiempo | Altura × duración de la formación | `OHLCV-OK` | Con retardo | 3+ | Leve | Feature continua |
| Patrones nominales (H-C-H, dobles, banderas) | Familia 8 | Detector paramétrico | `OHLCV-OK` | Con retardo | **≥9** | **Leve** | Evento (alto coste) |
| Volumen | Familia 7 | Volumen relativo a su media reciente | `OHLCV-OK` | **Sí** | 1 | No | Feature continua |
| Volumen en ruptura | Familia 7 | Volumen relativo condicionado a evento | `OHLCV-OK` | Sí | 2 | No | Filtro |
| **OBV** | Familia 7 | Acumulación de volumen con signo del cierre | **`OHLCV-OK`** | **Sí** | **0** | **No** | Feature continua |
| Índice de Demanda | Familia 7 | Presión compradora / vendedora escalada por VM | `OHLCV-OK` | Sí | 2 | No | Feature continua |
| Interés abierto | — | — | **`OTRAS FUENTES`** | — | — | — | **No disponible** |
| Rollover | — | Empalme con ajuste; renovación por erosión de volumen | `OHLCV-COND` | Sí | 2 | No | **Preprocesado obligatorio** |
| Multi-escala | Eje temporal | Mismas features sobre varias ventanas | `OHLCV-OK` | Sí | k | No | Feature / arquitectura |
| SMA/EMA/WMA | Familia 1 | Media y su pendiente | `OHLCV-OK` | Sí | 1–2 | No | Feature continua |
| **Media centrada** | — | — | `OHLCV-OK` | **NO** | — | **GRAVE** | **Prohibida** |
| Distancia precio-media | Familias 1+5 | Normalizada por ATR o por desviación típica | `OHLCV-OK` | Sí | 2 | No | Feature continua |
| **Ancho de Bollinger** | Familia 3 | Desviación típica móvil / media | **`OHLCV-OK`** | **Sí** | **1** | **No** | **Régimen** |
| **ATR** | Familia 3 | Media del rango verdadero | **`OHLCV-OK`** | **Sí** | **1** | **No** | **Normalizador universal** |
| **Canal de Donchian** | Familia 4 | Posición del precio en el rango de N barras | **`OHLCV-OK`** | **Sí** | **1** | **No** | **Feature / evento** |
| Momento / ROC | Familia 1 | Diferencia o cociente sobre lag | `OHLCV-OK` | Sí | 1 | No | Feature continua |
| Umbrales de sobrecompra del momento | — | Cuantil móvil sobre ventana pasada | `OHLCV-OK` | Sí | 3 | **Leve si por inspección** | Feature categórica |
| CCI | Familia 5 | Z-score con desviación media | `OHLCV-OK` | Sí | 1–2 | No | Feature continua |
| **RSI** | Familia 6 | Cociente de medias de ganancias y pérdidas | **`OHLCV-OK`** | **Sí** | **1** | **No** | Feature continua |
| **Estocástico %K** | Familia 4 | (C−L_n)/(H_n−L_n) | **`OHLCV-OK`** | **Sí** | **1–3** | **No** | Feature continua |
| Williams %R | Familia 4 | **= 100 − %K** | `OHLCV-OK` | Sí | 1 | No | **Redundante** |
| MACD / histograma | Familia 1 | Diferencia de EMAs y su derivada | `OHLCV-OK` | Sí | 3 | No | Feature continua |
| **Divergencia** | Familias 1+8 | Discrepancia entre variación del precio y del indicador sobre ventana | `OHLCV-OK` | **Sí si continua**; con retardo si por pivotes | 2–4 | **Leve si por pivotes** | Feature continua |
| Velas: geometría | Familias 4+3 | Cuerpo, sombras y posición del cierre, relativos al rango | **`OHLCV-OK`** | **Sí** | **0** | **No** | **Features continuas** |
| Velas: patrones nominales | — | Detector con umbrales | `OHLCV-OK` | Sí | 5–10 | No | Evento (alto coste) |
| **Interpretación psicológica de la vela** | — | — | **`GRANULAR`** | — | — | — | **No determinable** |
| P&F (3 registros) | Muestreo | Remuestreo por movimiento sobre H/L | `OHLCV-COND` | Sí | 2 | No | **Esquema de muestreo alternativo** |
| Elliott | — | — | — | **NO** | **No acotados** | **GRAVE** | **No aplicable** |
| Ciclos por inspección | — | — | `OHLCV-OK` | **NO** | No acotados | **GRAVE** | **No aplicable** |
| **Asimetría temporal (traslación)** | Familia 2 | Tiempo subiendo / tiempo bajando en ventana | **`OHLCV-OK`** | **Sí** | **1** | **No** | Feature continua |
| Estacionalidad anual | Eje temporal | Dummies de mes | `OHLCV-OK` | Sí | 1 | No | Escala inadecuada |
| **Estacionalidad intradiaria** | Eje temporal | Hora, minuto de sesión, tiempo desde apertura | **`OHLCV-OK`** | **Sí** | **0–1** | **No** | **Contexto — no tratada por Murphy** |
| **SAR parabólico** | Familia 1 | Stop dinámico acelerado | `OHLCV-OK` | **Sí, conocido de antemano** | 3 | No | Feature / regla de salida |
| **ADX** | Familia 2 | Diferencia suavizada de +DI y −DI | **`OHLCV-OK`** | **Sí** | **1** | **No** | **Régimen / filtro** |
| +DI / −DI | Familia 1 | Movimiento direccional normalizado | `OHLCV-OK` | Sí | 1 | No | Feature continua |
| **Puntos pivote intradía** | Familias 8 + sesión | Siete niveles de O,H,L,C de sesión previa y actual | **`OHLCV-OK`** | **Sí** | **1–3** | **No** | **Evento intradiario** |
| Stop por volatilidad | Familia 3 | Múltiplo de ATR | `OHLCV-OK` | Sí | 1 | No | **Regla de riesgo** |
| Recompensa/riesgo | — | Objetivo / distancia al stop | `OHLCV-OK` | Depende del objetivo | 1+ | Depende | Regla de riesgo |
| **STARC / Keltner** | Familias 3+5 | ATR×k alrededor de una media | **`OHLCV-OK`** | **Sí** | **2–3** | **No** | Feature / evento |
| **Market Profile (TPO)** | Familia 8 | Frecuencia de barras que tocaron cada nivel | `OHLCV-COND` | **Sí** | 2 | No | Contexto / estructura |
| Área de valor | Familia 8 | Rango que concentra ~70% de TPOs | `OHLCV-COND` | Sí | 2 | No | Feature continua |
| Extensión del rango inicial | Familias 3+sesión | Rango actual / rango de la primera hora | `OHLCV-COND` | Sí | 1 | No | Feature continua |
| Amplitud de mercado (A/D, TICK, TRIN) | — | — | **`OTRAS FUENTES`** | — | — | — | **No disponible** |
| Sentimiento / opinión contraria | — | — | **`OTRAS FUENTES`** | — | — | — | **No disponible** |
| Intermercado / fuerza relativa | — | — | **`OTRAS FUENTES`** | — | — | — | **No disponible** |


---

## 24. CANDIDATOS CONCEPTUALES A REGLA PRIMARIA

`[IMPLICACIÓN PARA IRIS]` **Encuadre obligatorio antes de la matriz.** La fuente anterior planteaba que una regla técnica **puede** funcionar como modelo primario en una arquitectura de dos niveles. **Esto no significa que IRIS deba adoptar esa arquitectura**, y este documento no la adopta. Lo que sigue es un inventario de qué reglas de Murphy **producirían un `side` inequívoco de forma causal**, con sus propiedades, para que la decisión pueda tomarse más adelante con información.

**Criterio de "recall alto" que la arquitectura requeriría** `[INTERPRETACIÓN]`: la regla primaria debe **no perderse oportunidades**, aunque su precisión sea baja. Eso favorece reglas que **generan muchas señales** y penaliza las que exigen confirmaciones múltiples.

### 24.1 Matriz de candidatos

| # | Regla | Información usada | Familia | Parámetros | Causal | Subjetividad | Frecuencia potencial | ¿Side inequívoco? | Mecanismo propuesto por Murphy | OHLCV | ¿Falsable experimentalmente? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Ruptura de canal de Donchian** (máximo/mínimo de N barras) | H, L | 4 | **1** | **Sí** | **Nula** | Media-baja (ajustable con N) | **Sí** | Ruptura de extremos previos = superación de resistencia/apoyo | **`OHLCV-OK`** | **Sí** |
| **2** | **Cruce de dos medias móviles** | C | 1 | 2–3 | **Sí** | **Nula** | Media | **Sí** | Cambio en la relación entre ritmo corto y largo | **`OHLCV-OK`** | **Sí** |
| **3** | **Precio cruza una media, con pendiente confirmatoria** | C | 1+2 | 2 | **Sí** | Nula | Media-alta | **Sí** | Idem | **`OHLCV-OK`** | **Sí** |
| **4** | **+DI cruza −DI** | H, L, C | 1 | 1 | **Sí** | Nula | Media | **Sí** | Predominio del movimiento direccional en un sentido | **`OHLCV-OK`** | **Sí** |
| **5** | **SAR parabólico (paro y retroceso)** | H, L | 1 | 3 | **Sí** (valor conocido de antemano) | Nula | Alta | **Sí** (siempre en mercado) | Stop dinámico que acelera con la tendencia | **`OHLCV-OK`** | **Sí** |
| **6** | **Cierre fuera de canal de Keltner** | H, L, C | 3+5 | 3 | **Sí** | Nula | Media | **Sí** | Ruptura de volatilidad | **`OHLCV-OK`** | **Sí** |
| **7** | **Cruce de cero del momento / MACD** | C | 1 | 1–3 | **Sí** | Nula | Media-alta | **Sí** | Cambio de signo en la aceleración | **`OHLCV-OK`** | **Sí** |
| **8** | **Cruce %K/%D en zona extrema** (estocástico) | H, L, C | 4 | 2–3 | **Sí** | Baja | Media-alta | **Sí** | El cierre se aleja del extremo del rango | **`OHLCV-OK`** | **Sí** |
| **9** | **RSI cruza de vuelta 30 / 70** | C | 6 | 2 | **Sí** | Baja | Media | **Sí** | Agotamiento de la presión dominante | **`OHLCV-OK`** | **Sí** |
| **10** | **Toque de banda STARC** (reversión) | H, L, C | 3+5 | 2–3 | **Sí** | Nula | Media | **Sí** | Precio excesivo respecto al rango medio | **`OHLCV-OK`** | **Sí** |
| **11** | **Día de cambio** (nuevo extremo + cierre contrario) | O, H, L, C, V | 4+3 | **0–2** | **Sí** | **Nula** | Media | **Sí** | **Liquidación forzada de posiciones apalancadas; vacío de presión** | **`OHLCV-OK`** | **Sí** |
| **12** | **Puntos pivote intradía** | O, H, L, C de sesión previa y actual | 8+sesión | 1–3 | **Sí** | Baja | **Alta (intradiaria)** | **Sí** | Niveles de referencia de la sesión; señal más fuerte cuanto más tarde | **`OHLCV-OK`** | **Sí** |
| **13** | **Ruptura de soporte/resistencia con filtro** | H, L, C | 8 | 3–5 | **Con retardo** | **Media** | Media | **Sí** | **Cambio de polaridad; participantes atrapados y margin call** | **`OHLCV-OK`** | Sí, con `k` declarado |
| **14** | **Ruptura de línea de tendencia** | H, L, C | 8 | **≥7** | **Con retardo** | **Alta** | Media | **Sí** | Idem | **`OHLCV-OK`** | Con dificultad |
| **15** | **Señal de P&F (3 registros)** | H, L | 4+muestreo | 2 | **Sí** | **Nula** | Ajustable (0 a muchas) | **Sí** | Ruptura de columna previa | `OHLCV-COND` | **Sí** |
| **16** | **Divergencia precio-oscilador** | C + indicador | 1+8 | **≥4** | **Con retardo** | **Alta** | Baja | Sí | Debilitamiento del impulso antes del giro del precio | **`OHLCV-OK`** | Con dificultad |
| **17** | **Patrón de velas nominal (filtrado por oscilador)** | O, H, L, C | 4+3 | **5–10** | **Sí** | Media | Baja-media | **Sí** | Psicología de una a cinco sesiones | **`OHLCV-OK`** | Con dificultad |
| **18** | **Patrón chartista (H-C-H, dobles, banderas)** | H, L, C, V | 8 | **≥9** | **Con retardo** | **Alta** | **Baja** | **Sí** | Degradación de la estructura de impulsos | **`OHLCV-OK`** | Con gran dificultad |
| **19** | **Ondas de Elliott** | — | — | **No acotados** | **NO** | **Máxima** | — | **No** (recuento no único) | Psicología de masas fractal | — | **No** |
| **20** | **Ciclos temporales** | C | — | No acotados | **NO** | Alta | — | Sí | Periodicidad subyacente | `OHLCV-OK` | **No** |

### 24.2 Lectura de la matriz

`[INTERPRETACIÓN]` Ordenando por las propiedades que la arquitectura requeriría —**causalidad sin retardo, subjetividad nula, pocos parámetros, `side` inequívoco, frecuencia suficiente**— emergen tres grupos claramente separados:

**Grupo A — cumplen todos los criterios (candidatos 1–12, 15).** Trece reglas causales, objetivas, con entre cero y tres parámetros, `OHLCV-OK` (salvo P&F, condicional), todas falsables. **Notablemente, incluyen las dos que reciben respaldo empírico externo en el libro** (canal de Donchian y cruce de medias, §9.8) y **la única técnica intradiaria propia del libro** (puntos pivote).

**Grupo B — causales sólo con retardo declarado y subjetividad media-alta (13, 14, 16, 17, 18).** Todos dependen de identificar pivotes o de umbrales de forma. Utilizables, pero **con un coste de grados de libertad entre uno y dos órdenes de magnitud mayor**, y con retardo estructural que reduce el recall.

**Grupo C — no formalizables causalmente (19, 20).** Excluidos por las razones desarrolladas en §13.5 y §14.5.

`[IMPLICACIÓN PARA IRIS]` **Tres observaciones sobre esta matriz, sin decidir nada:**

1. **La objetividad y la subjetividad no se distribuyen por "sofisticación" sino por dependencia de pivotes.** Todas las reglas que no requieren identificar máximos y mínimos locales son limpiamente causales; todas las que sí, arrastran `LOOK-AHEAD-LEVE`. **Esa es la línea divisoria real del libro**, y no coincide con la distinción entre indicadores y chartismo.

2. **Las reglas con mecanismo económico más convincente no coinciden con las más objetivas.** El mecanismo mejor argumentado del libro —participantes atrapados, cambio de polaridad, margin call (§4.4)— sostiene precisamente las reglas del grupo B, que son las más difíciles de formalizar. Y el día de cambio (11) es la excepción interesante: **comparte ese mecanismo y es de las más objetivas.**

3. **Ninguna de las veinte tiene evidencia de rendimiento en el libro.** Las dos con respaldo externo citado (Donchian y cruce de medias) lo tienen sobre futuros de materias primas en frecuencia diaria, en períodos de 1975–1986, sin corrección por multiple testing y sin costes. **No se selecciona ninguna.**

---

## 25. MÍNIMA COMPLEJIDAD

Criterio del encargo: `información potencial / complejidad / grados de libertad / subjetividad / riesgo de overfitting`. **"No confundir sofisticación con utilidad."**

### 25.1 Alta prioridad conceptual

*OHLCV directo, pocos parámetros, causal sin retardo, reproducible, información claramente definida.*

| Concepto | GL | Por qué está aquí |
|---|---|---|
| **ATR** | 1 | **Normalizador universal.** Permite hacer adimensional casi cualquier otra variable (stops, umbrales, distancias, tamaños de barra). Su ausencia obliga a usar parámetros absolutos no transferibles entre regímenes |
| **ADX** | 1 | Tendencialidad sin dirección; variable de contexto pura; soporta la hipótesis de régimen más recurrente del libro |
| **Coeficiente de eficiencia** | 1 | Misma familia que ADX, construcción más simple (desplazamiento neto / camino recorrido) |
| **Ancho de banda de volatilidad** | 1 | Régimen de compresión/expansión; hipótesis de alternancia falsable |
| **Posición en el rango de N barras** (`%K` / Donchian) | 1 | Adimensional por construcción; premisa estructural falsable; unifica estocástico, %R y ruptura de canal |
| **Geometría de vela** (cuerpo y sombras relativos) | **0** | Cinco ratios sin ningún parámetro; agotan la información de una barra |
| **Día de cambio** | 0–2 | Evento causal, sin pivotes, con mecanismo económico, invariante de escala |
| **Hueco (evento, no tipo)** | 1 | Detección trivial y causal |
| **Volumen relativo** | 1 | Única fuente no derivada del precio que poseemos |
| **OBV** | **0** | Cero parámetros; limitación conocida y declarada por el autor |
| **RSI** | 1 | Única familia que descompone asimetría alza/baja |
| **Estacionalidad intradiaria** | 0–1 | Hora y tiempo desde apertura; **no tratada por Murphy pero implícita en sus pivotes intradía** |
| **Puntos pivote intradía** | 1–3 | Única técnica intradiaria propia; niveles deterministas |
| **Números redondos** | 1 | Distancia normalizada al múltiplo; sin ambigüedad de detección |
| **Multi-escala** (mismas features, varias ventanas) | k | Estructura, no indicador; soporta la arquitectura top-down |
| **Ajuste de rollover** | 2 | **Preprocesado obligatorio, no opcional** |

### 25.2 Prioridad experimental

*Cuantificables, más parámetros, requieren validación cuidadosa.*

| Concepto | GL | Reserva |
|---|---|---|
| Medias y sus derivados (distancia, pendiente, cruces, MACD) | 1–3 | **Familia 1: alta redundancia interna.** Elegir representantes, no acumular |
| CCI / posición en bandas | 1–2 | Redundante con ancho de banda + distancia a media |
| STARC / Keltner | 2–3 | **Misma construcción, interpretaciones opuestas** — usar como variable, no como regla |
| SAR parabólico | 3 | Causal y anticipable, pero sistema continuo |
| Soportes y resistencias como densidad de actividad | 3–5 | **`LOOK-AHEAD-LEVE`**; requiere declarar `k`. Mecanismo económico fuerte |
| Divergencia como discrepancia continua | 2–4 | Reformulación causal; **no es la divergencia de Murphy** |
| Compresión → ruptura (sin geometría) | 2 | Núcleo común de media docena de patrones |
| Tamaño del patrón (altura × duración) | 3 | Hipótesis del cap. 5 aislada de la taxonomía |
| Asimetría temporal (traslación) | 1 | Reformulada por el propio autor |
| Retroceso relativo al impulso | 2 | Como distribución, no como niveles mágicos |
| P&F de 3 registros | 2 | Esquema de muestreo alternativo; **transforma el dataset entero** |
| Market Profile aproximado (TPO, área de valor) | 2 | Supuesto de continuidad intrabar; requiere definir sesión |
| Índice de Demanda | 2 | Volumen normalizado por movimiento y volatilidad |
| Estabilidad paramétrica y temporal | — | **Criterio de validación, no feature** |

### 25.3 Baja prioridad

*Altamente subjetivos, muchos grados de libertad, difícilmente falsables, fuerte riesgo retrospectivo, o datos inexistentes.*

| Concepto | Motivo |
|---|---|
| **Ondas de Elliott** | Recuento no único; excepciones no especificadas; **no falsable** |
| **Ciclos por inspección visual** | "Ajustar hasta encontrar el ajuste adecuado"; sin criterio de significación |
| **Líneas de tendencia geométricas / Gann / abanico** | ≥7 GL; **no invariantes de escala**; el propio autor critica las de Gann |
| **Líneas internas** | Maximizan explícitamente el ajuste a datos pasados |
| **Patrones chartistas nominales** | ≥9 GL; el autor advierte que en futuros **se completan menos** |
| **Patrones de velas nominales** | 5–10 GL; definiciones declaradas elásticas; misma información que la geometría continua |
| **Taxonomía de huecos** | Clasificación retrospectiva por definición |
| **Platillo y púa** | El propio autor admite que no se puede medir ni anticipar |
| **Media centrada** | **`LOOK-AHEAD-GRAVE`** — prohibida |
| **Umbrales de oscilador fijados por inspección visual** | Look-ahead si no se sustituyen por cuantiles móviles |
| **Estacionalidad anual** | Escala inadecuada; 14–15 observaciones por mes; sin control de multiple testing |
| **Interés abierto, IRH, COT** | `OTRAS FUENTES` |
| **Amplitud de mercado (A/D, TICK, TRIN, McClellan)** | `OTRAS FUENTES` |
| **Sentimiento / opinión contraria** | `OTRAS FUENTES` |
| **Intermercado y fuerza relativa** | `OTRAS FUENTES` |
| **Interpretación psicológica de la forma de la vela** | Requiere secuencia intrabar (`GRANULAR`) |

### 25.4 Observación de conjunto

`[INTERPRETACIÓN]` **El resultado del filtro de mínima complejidad es marcadamente asimétrico respecto a la reputación de las técnicas.** Lo que queda en alta prioridad son mayoritariamente **medidas escalares simples con cero, uno o dos parámetros** —ATR, ADX, posición en rango, ratios de vela, volumen relativo— mientras que **lo que se descarta es precisamente aquello por lo que el análisis técnico es conocido públicamente**: figuras chartistas, ondas, ciclos, líneas trazadas.

Y hay una regularidad detrás: **las técnicas de alta prioridad son las que se definen por una fórmula; las de baja prioridad son las que se definen por un dibujo.** El criterio de Schutzman —"si 100 personas siguen las normas y llegan al mismo resultado"— separa el libro casi exactamente por esa línea.

---

## 26. CONTRADICCIONES Y TENSIONES INTERNAS

Búsqueda deliberada, conforme al encargo. **No se resuelven con conocimiento externo.**

### 26.1 Contradicciones directas entre secciones del libro

| # | Tensión | Dónde |
|---|---|---|
| **1** | **Out-of-sample.** El cap. 9 afirma que **"el procedimiento correcto es usar sólo parte de la información para elegir los parámetros y otra parte para examinar los resultados"**. El apéndice C declara: **"Yo uso la totalidad de las series de datos, sin guardar nada para hacer la prueba fuera de la muestra."** | §9.9 vs §20.C.5 |
| **2** | **Optimización.** El cap. 9 advierte que **"la optimización no es el Santo Grial"** y expone el procedimiento correcto; el cap. 15 celebra la capacidad de **"desarrollar, probar, incluso optimizar"** sin mencionar el riesgo | §9.9 vs §15.7 |
| **3** | **Mismo indicador, reglas opuestas.** CCI: Lambert dice comprar por encima de +100; **"la mayoría de los chartistas"** lo usa como sobrecompra para vender. STARC y Keltner tienen construcción casi idéntica (ATR×2 sobre una media) e interpretaciones contrarias | §10.6, §20.A.3 |
| **4** | **Misma configuración, tres reglas incompatibles.** Para un rectángulo, Murphy documenta operar las oscilaciones internas, asumir continuidad, o esperar la ruptura — sin criterio de elección | §6.6 |
| **5** | **El mercado lo descuenta todo, pero se puede anticipar.** La premisa 1 es prácticamente la hipótesis de mercado eficiente que el libro rechaza; la salida es temporal (el precio descuenta *antes* que el conocimiento público), lo que convierte la premisa en una afirmación sobre velocidades de incorporación, mucho más específica de lo que enuncia | §1.2, §1.8 |
| **6** | **Retrocesos: tres parametrizaciones distintas.** Cap. 4: mínimo 33-38%, máximo 62-68%. Cap. 13: 38/50/62. Cap. 16: **40-60% para entrada** | §4.13, §13.4, §16.7 |
| **7** | **Stops: dos criterios incompatibles.** Escalar por volatilidad (§16.5) frente a colocar en soportes y resistencias (§16.7). Ambos recomendados, sin regla de prioridad | §16 |
| **8** | **El sistema mecánico ocupa papeles opuestos.** En §15.4 el sistema es el componente de contexto y la señal viene de otro indicador; en §15.6 el sistema es el filtro disciplinario y el juicio humano genera la señal | §15 |
| **9** | **Modelo nominal de ciclos contradicho por los propios ejemplos.** El modelo predice 5, 10, 20, 40, 80 días; los ejemplos del capítulo detectan ciclos de 49, 55, 133 días y 75 meses | §14.2 vs §14.5 |
| **10** | **Cabeza y hombros es simultáneamente patrón de cambio y de continuidad**, distinguidos sólo por orientación relativa a una tendencia previa que a su vez tiene `LOOK-AHEAD-LEVE` | §5.2 vs §6.8 |

### 26.2 Reglas que se anulan a sí mismas

| # | Problema |
|---|---|
| **11** | **El principio de variación (ciclos)** declara que armonía, sincronización, proporcionalidad y sumación **"son simplemente tendencias fuertes y no reglas puras y duras"**. Con eso, ninguna desviación observada refuta el marco |
| **12** | **Elliott**: las tres reglas "estrictas" tienen excepción declarada, y **dos de las tres excepciones son específicamente para futuros** — nuestro caso |
| **13** | **"Aplicar Elliott sólo cuando la imagen es clara"** convierte la selección de casos en un acto discrecional posterior a la observación |
| **14** | **Condición de uso del oscilador circular**: son útiles "hacia el final de los movimientos" — pero el final sólo se conoce cuando el movimiento terminó |
| **15** | **Umbrales de RSI desplazables según el régimen** (70/30 en general, 80/20 en mercados alcistas/bajistas): saber qué umbral aplicar requiere saber antes en qué régimen estamos, que es parte de lo que se quería determinar |
| **16** | **La justificación del ciclo de 28 días** se apoya en la popularidad y aparente éxito de períodos como 14 o 20; y esos períodos se justifican por el ciclo de 28 días |

### 26.3 Conceptos declarados importantes y no operacionalizados

| # | Concepto | Problema |
|---|---|---|
| **17** | **"Movimientos bastante ordenados y bien definidos"** (movimiento medido) | Condición evaluada a posteriori |
| **18** | **"Cada analista debe decidir por sí mismo qué constituye una penetración significativa"** | Parámetro delegado explícitamente |
| **19** | **Grado de las ondas de Elliott** | No acotado; fractal en ambas direcciones |
| **20** | **"Elija uno o dos osciladores con los que se sienta cómodo"** | Criterio de selección subjetivo, inaplicable a un sistema |
| **21** | **Ajuste discrecional de objetivos de precio** mezclando media docena de herramientas | "El analista más habilidoso será aquel que sepa mezclar correctamente" |
| **22** | **Agregación de las 23 preguntas de la lista de comprobación** | **No hay procedimiento de combinación ni de resolución de conflictos** |

### 26.4 Afirmaciones sin evidencia que el libro presenta como establecidas

| # | Afirmación | Estado |
|---|---|---|
| **23** | "El volumen precede al precio" | Sin ninguna medición |
| **24** | "Los precios se mueven por tendencias" (versión fuerte) | Argumento visual únicamente |
| **25** | "La aleatoriedad es un fenómeno de muy corta duración" | Impresión derivada de gráficos de largo plazo |
| **26** | Reglas de medición por simetría (línea rota, H-C-H, banderas, movimiento medido, huecos de medida) | Postuladas sin mecanismo |
| **27** | "Los mejores operadores ganan sólo en el 40% de sus operaciones" | Sin fuente |
| **28** | "Hay tendencia el 30% del tiempo" (Wilder) | Sin fuente metodológica |
| **29** | "Menos del 5% de las ideas se transforman en beneficios" | Sin fuente |
| **30** | Recompensa/riesgo de 3:1 | Convención, sin derivación |
| **31** | Reglas de asignación 50% / 10-15% / 5% / 20-25% | Declaradas "normales en el sector" |
| **32** | Inclinación de 45 grados como equilibrio precio-tiempo | **No invariante de escala** |
| **33** | "La importancia del número tres" | El propio autor: "cualquiera que sea la razón" |

### 26.5 Tensiones con el propio proyecto IRIS

`[INTERPRETACIÓN]` Registradas aparte porque no son defectos del libro sino **desacuerdos entre la fuente y nuestro diseño**:

| # | Tensión |
|---|---|
| **34** | **Murphy sostiene que la estructura está en el largo plazo y el ruido domina el corto.** Leído literalmente, desaconseja el horizonte de IRIS (§8.5) |
| **35** | **El intradía tiene papel subordinado**: refinar el timing de una decisión tomada en diario, no tomar la decisión (§16.8) |
| **36** | **"Dominar las operaciones interdía antes de probar las intradía"** (§16.10) |
| **37** | **Cuatro de sus fuentes de corroboración más valoradas requieren datos que no tenemos**: confirmación entre índices, interés abierto, sentimiento, amplitud de mercado |
| **38** | **La estabilidad entre mercados**, uno de los tres criterios de robustez del apéndice C, exige universo multiactivo |
| **39** | **En futuros, "los modelos gráficos tienden a no completarse tanto como en valores"** (§1.6) — advertencia del autor contra su propio catálogo aplicado a nuestro tipo de instrumento |

---

## 27. QUÉ MURPHY NO PUEDE DECIRNOS

Sección explícita conforme al encargo. **No se atribuyen al libro respuestas que no contiene.**

### 27.1 Sobre validez estadística

| Pregunta | Respuesta |
|---|---|
| **¿Alguna técnica tiene edge estadístico?** | **No lo establece.** No hay una sola prueba de significación, tasa de acierto medida ni comparación contra baseline en 547 páginas. Las dos únicas referencias externas (§19.3) son citas de frases introductorias de estudios sobre **divisas**, no examinadas |
| **¿Cuántas señales falsas produce cada técnica?** | **No se cuentan en ningún caso.** Los gráficos señalan con flechas los aciertos |
| **¿Cómo controlar el multiple testing?** | **`[VACÍO]` total.** El concepto no aparece. El cap. 9 reconoce el problema de la optimización pero no su dimensión combinatoria |
| **¿Cómo evitar el backtest overfitting?** | Sólo mediante los tres criterios de robustez del apéndice C (paramétrica, temporal, entre mercados), **y ese mismo apéndice rechaza el out-of-sample** |
| **¿Cómo hacer purging, embargo o estimar unicidad de muestras?** | **`[VACÍO]` total.** Ninguno de los tres conceptos existe en el libro |
| **¿Cómo calibrar probabilidades?** | **`[VACÍO]`.** El libro nunca produce una probabilidad. Sus salidas son binarias o cualitativas |
| **¿Cómo seleccionar modelos de ML?** | **`[VACÍO]`.** Fuera de alcance de la obra |

### 27.2 Sobre generalización

| Pregunta | Respuesta |
|---|---|
| **¿Generaliza a MNQ?** | **No lo establece.** Sus ejemplos son bonos del tesoro, S&P 500 contado, oro, café, cobre, crudo, divisas, valores individuales e índices sectoriales. **No hay ningún ejemplo sobre futuros de índices tecnológicos**, y sí advertencias de que los patrones se completan menos en futuros |
| **¿Generaliza a barras de un minuto?** | **No lo establece.** Los ejemplos intradiarios son tres gráficos ilustrativos de 5, 10 y 60 minutos (§16.8), con flechas sobre señales acertadas. **La escala mínima que muestra es 5 minutos** |
| **¿Se mantiene estable 2020–2026?** | **Imposible de saber desde el libro** (edición de 1999). Y él mismo advierte que las relaciones intermercado **cambian con el régimen** (§17.1), y que las duraciones de los ciclos **"cambian continuamente"** (§14.5) |
| **¿Sobrevive a costes?** | **No lo evalúa.** El apéndice C explícitamente excluye costes de las pruebas. La única mención cuantitativa relacionada es que el promedio por operación debe cubrirlos |

### 27.3 Sobre información incremental

| Pregunta | Respuesta |
|---|---|
| **¿Un indicador es mejor que otro?** | **No lo establece**, y en un caso declara ausencia de evidencia: **"no hay evidencia real que demuestre que [las EMA] funcionan mejor que la media simple"** (§9.3) |
| **¿Una combinación de indicadores mejora sobre OHLCV simple?** | **No lo establece.** La lista de comprobación de 23 preguntas **no tiene procedimiento de agregación** |
| **¿Los patrones son realmente predictivos?** | **No lo establece.** Y advierte contra el abuso del doble techo porque **"los precios tienen una fuerte tendencia a volver atrás desde un pico previo"** — es decir, reconoce que el patrón se confunde con el comportamiento base, sin medir la diferencia |
| **¿Qué parámetros usar en MNQ intradiario?** | **No lo establece**, y él mismo cambia los parámetros al pasar de valores a futuros (50/200 → 4/9/18), lo que demuestra que son convencionales |
| **¿Cómo resolver conflictos entre escalas o entre indicadores?** | **`[VACÍO]`.** Prescribe jerarquía (la tendencia mayor manda) pero sin criterio operativo cuando las lecturas discrepan |

### 27.4 Los vacíos nuevos que este análisis identifica

`[VACÍO]` **Cuestiones relevantes para IRIS que el libro no aborda en absoluto:**

1. **Estacionalidad intradiaria** — el patrón sistemático de volatilidad y volumen a lo largo de la sesión. Lo usa implícitamente en los puntos pivote (§16.9) sin desarrollarlo nunca.
2. **Definición de sesión en un mercado de casi 24 horas.** Toda su estructura de apertura, cierre y "día" presupone un horario acotado.
3. **La limitación intrabar de las velas** — que `(O,H,L,C)` no determina la trayectoria interna. Trata la forma de la vela como si codificara la dinámica del período.
4. **El efecto del rollover sobre el volumen** durante la transición de contratos.
5. **Cómo compensar los saltos de empalme** — los apéndices describen tipos de contrato continuo pero no un método de ajuste por diferencia o ratio.
6. **Agregación de señales múltiples** en una decisión.
7. **Cuantificación de la incertidumbre** de cualquier señal.
8. **Coste computacional o factibilidad** de cualquier procedimiento.


---

## 28. RELACIÓN CON JANSEN Y LÓPEZ DE PRADO

**No es la Knowledge Synthesis.** Se registran coincidencias y conflictos **sin resolverlos**, conforme al encargo.

### 28.1 CONFIRMA

*Conceptos de Murphy compatibles con problemas ya identificados en las fuentes anteriores.*

| # | Murphy | Coincide con |
|---|---|---|
| **C1** | **"Es posible estar en la dirección correcta del mercado y perder dinero igualmente"** (§1.5, §16.1) | El principio de que predicción ≠ rentabilidad, presente en ambas fuentes anteriores |
| **C2** | **Descomposición qué / cuándo / cuánto** (§16.1) | La separación entre dirección y tamaño de la segunda fuente, y la cadena predicción → señal → posición de la primera |
| **C3** | **"La gestión monetaria es tan importante como un buen sistema"** (§16.2, §20.C.7) | La tesis de que un modelo preciso con mal dimensionamiento pierde dinero |
| **C4** | **Tasa de acierto del 40% compatible con rentabilidad si los pagos son asimétricos** (§16.4) | La relación entre precisión, frecuencia y estructura de pagos ya formalizada en la etapa anterior |
| **C5** | **Existencia de stop-loss implícito por apalancamiento y margin call** (§1.6, §4.4, §16.4) | El argumento que justifica el etiquetado dependiente del camino |
| **C6** | **Mecanismo de participantes atrapados en el lado perdedor** (§4.4) | El racional de rupturas estructurales de la segunda fuente. **Convergencia desde fuentes independientes sobre el mismo mecanismo** |
| **C7** | **"Si un sistema funciona bien pero tiene poco sentido, posiblemente sea coincidencia"** (§20.C.3) | La exigencia de mecanismo económico previo a la estrategia |
| **C8** | **Separación in-sample / out-of-sample** (§9.9) | La práctica estándar de ambas fuentes — **aunque el apéndice C la contradice** |
| **C9** | **Estabilidad paramétrica y temporal como criterios de robustez** (§20.C.5) | El diagnóstico de que un resultado frágil ante perturbaciones del diseño no es un resultado |
| **C10** | **"Optimizar lo menos posible; usar pocos parámetros"** (§20.C.3) | El principio de mínima complejidad |
| **C11** | **Criterio de objetividad: 100 personas, mismo resultado** (§20.C.1) | El requisito de reproducibilidad de cualquier procedimiento cuantitativo |
| **C12** | **"El promedio por operación debe cubrir los costes"** (§20.C.6) | El análisis de viabilidad previa por edge mínimo |
| **C13** | **Escalar stops por volatilidad** (§16.5) | Los umbrales de etiquetado escalados por volatilidad |
| **C14** | **Reconocimiento explícito de subjetividad del chartismo** (§1.7) | La distinción entre patrón reconocible retrospectivamente y detectable causalmente |
| **C15** | **Las relaciones cambian con el régimen** (§17.1) y las duraciones cíclicas **"cambian continuamente"** (§14.5) | La no estacionariedad y el decaimiento de las relaciones aprendidas |

### 28.2 COMPLEMENTA

*Conocimiento que las fuentes anteriores no aportaban.*

| # | Aportación | Por qué es nueva |
|---|---|---|
| **P1** | **Mecanismos de mercado explícitos** | Las fuentes anteriores exigían identificar "por qué otro participante nos pierde dinero" **sin ofrecer candidatos**. Murphy proporciona varios: memoria de participantes en niveles, liquidación forzada por margin call, agotamiento tras movimientos extendidos, asimetría de urgencia temporal entre participantes (Market Profile) |
| **P2** | **Un catálogo de hipótesis falsables sobre un instrumento único** | Las trece hipótesis de §21.4. **Ninguna requiere universo multiactivo** — precisamente la limitación estructural que arrastrábamos |
| **P3** | **La hipótesis de régimen como principio organizador** | Aparece cuatro veces desde capítulos distintos: medias en tendencia / osciladores en rango; la estimación del 30%; ADX como discriminador; ciclo vs tendencia en MESA. **Ninguna fuente anterior articulaba esto** |
| **P4** | **Vocabulario de estructura de precio** | Soporte, resistencia, polaridad, compresión, expansión, ruptura, retroceso, impulso. Es el lenguaje que faltaba para describir estados de mercado |
| **P5** | **La familia de tendencialidad (ADX, coeficiente de eficiencia)** | Magnitud de tendencia **sin dirección** como variable de contexto. No aparecía en las fuentes anteriores |
| **P6** | **"Las salidas importan más que las entradas"** (§20.C.3) | Afirmación que **ninguna de las dos fuentes anteriores hace con esta rotundidad** |
| **P7** | **Los puntos pivote intradía** | Única técnica del libro con la hora de la sesión como parte constitutiva de la regla |
| **P8** | **Market Profile como modelo de formación del rango de sesión** | Relato causal específicamente intradiario: equilibrio inicial, extensión del rango, precios aceptados y rechazados |
| **P9** | **Diversificación entre sistemas, parámetros y marcos temporales** (§20.C.7) | Reconoce que la diversificación **no es únicamente entre activos** — tres de las cuatro dimensiones son accesibles a IRIS |
| **P10** | **Muestreo por movimiento de precio (P&F)** | Cuestiona el reloj cronológico desde una tradición completamente distinta |
| **P11** | **Métricas de evaluación de sistema** (factor beneficio, promedio por operación, reducción distinguiendo origen) | Complementan las métricas ya conocidas con una distinción útil: pérdidas de capital propio frente a beneficios devueltos |

### 28.3 TENSIONA

*Conflictos aparentes. **No se resuelven.***

| # | Tensión | Murphy | Fuentes anteriores |
|---|---|---|---|
| **T1** | **Validación fuera de muestra** | El apéndice C la **rechaza explícitamente**, sustituyéndola por robustez paramétrica, temporal y entre mercados | Requisito no negociable; el hold-out se usa una sola vez |
| **T2** | **Horizonte donde reside la estructura** | **"La aleatoriedad es un fenómeno de muy corta duración"**; la estructura está en el largo plazo | Una sostiene que las estrategias algorítmicas rinden mejor a frecuencias más altas; la otra construye todo su aparato sobre eventos de corto plazo |
| **T3** | **Papel del intradía** | Subordinado: refinar el timing de una decisión tomada en diario. **"Dominar interdía antes que intradía"** | IRIS propone que la decisión misma se tome en intradiario |
| **T4** | **Multiple testing** | **Concepto ausente.** El libro presenta decenas de indicadores, cada uno con parámetros ajustables, sin ninguna contabilidad de intentos | Es el mecanismo de fallo principal; el número de intentos debe registrarse y corregirse |
| **T5** | **Instrumento único** | El apéndice C exige **estabilidad entre mercados** como criterio de robustez y descarta sistemas que no la cumplen | Una de ellas también recomienda universos completos frente a valores individuales. **Tres fuentes coinciden en desaconsejar el instrumento único** |
| **T6** | **Costes en la evaluación** | El apéndice C los **excluye de las pruebas** por "pureza", incluyéndolos al final | Deben modelarse desde el primer backtest; en alta frecuencia pueden invertir el orden entre sistemas |
| **T7** | **Papel del juicio discrecional** | §15.5 defiende que el operador intervenga cuando el sistema no reconoce soportes de largo plazo, divergencias o quintas ondas | Un sistema debe ser completamente especificado antes de evaluarse; la intervención discrecional impide reproducibilidad |
| **T8** | **Selección de features** | **"Elija uno o dos osciladores con los que se sienta cómodo"** | Selección por importancia medida fuera de muestra, con control de efectos de sustitución |
| **T9** | **Qué constituye evidencia** | Argumento visual e inspección de gráficos: **"la observación empírica y la experiencia práctica resultan más útiles que las técnicas estadísticas sofisticadas"** | La inspección visual de series es precisamente el mecanismo que genera falsos descubrimientos |
| **T10** | **Optimización** | El cap. 9 la trata con cautela; el cap. 15 la celebra; el apéndice C la minimiza. **Tres posiciones distintas dentro del mismo libro** | Posición única: contribuye al sobreajuste a través de la propia validación cruzada |

`[INTERPRETACIÓN]` **Observación sobre T5, que es la tensión de mayor consecuencia**: es la primera vez en las tres etapas que **las tres fuentes coinciden en una advertencia contra el diseño de IRIS**. Murphy llega a ella por una vía distinta (robustez entre mercados como test de que el hallazgo no es específico de una serie), pero el contenido es el mismo. **Se registra sin resolver**; corresponde a la síntesis decidir qué defensas sustitutivas son suficientes.

### 28.4 NO RESPONDE

*Preguntas previas que siguen abiertas tras esta fuente.*

| # | Pregunta |
|---|---|
| **N1** | ¿Existe predictibilidad explotable en MNQ intradiario? |
| **N2** | ¿Qué timeframe, resolución base o esquema de muestreo? |
| **N3** | ¿Qué target y qué horizonte? |
| **N4** | ¿Cómo etiquetar eventos? |
| **N5** | ¿Qué features contienen realmente señal? |
| **N6** | ¿Qué modelo funcionará mejor? |
| **N7** | ¿Cómo validar sin leakage en frecuencia intradiaria? |
| **N8** | ¿Cómo calibrar probabilidades y cuantificar confianza? |
| **N9** | ¿Cuál es el coste real de operar MNQ y el edge mínimo necesario? |
| **N10** | ¿Cómo agregar múltiples señales en una decisión? |
| **N11** | ¿Cómo definir operativamente la abstención? — **Murphy aporta una vía nueva** (derivarla del régimen), pero no resuelve cuál elegir |
| **N12** | ¿Cómo monitorizar un sistema desplegado? |
| **N13** | ¿Cuánto histórico se necesita y cuántas observaciones independientes contiene? |

---

## 29. PREGUNTAS HEREDADAS DE LAS ETAPAS ANTERIORES

Estado: **RESPONDIDA POR MURPHY** / **RESPUESTA PARCIAL** / **`[VACÍO]`**.

### 29.1 Tendencia

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Cómo define una tendencia? | **RESPONDIDA** | Secuencia de picos y valles crecientes o decrecientes, **medida sobre cierres** (Dow). §2.1, §4.1 |
| ¿Cómo cambia según la escala? | **RESPONDIDA** | Principal / intermedia / menor, estructura recursiva; **"un número casi infinito de tendencias que interactúan"**; la clasificación es convencional, no una propiedad. §4.2 |
| ¿Puede expresarse objetivamente? | **PARCIAL** | La dirección sí (HH/HL, con retardo de pivote). La **magnitud** sí y mejor: ADX y coeficiente de eficiencia, causales y con un parámetro. **Pero las fronteras entre escalas son arbitrarias** |
| ¿Hay alguna regla de tendencia candidata a producir `side`? | **RESPONDIDA** | Trece candidatas causales y objetivas en §24.1 |

### 29.2 Momentum

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Qué indicadores existen? | **RESPONDIDA** | Momento, ROC, histograma de medias, CCI, RSI, estocástico, %R, MACD e histograma. §10 |
| ¿Qué mide cada uno? | **RESPONDIDA** | Fórmulas y construcción documentadas en §10.3–§10.10 |
| ¿Cuánto se solapan? | **RESPONDIDA, y más de lo esperado** | Se reducen a **cuatro familias informativas** (§10.11); `%R = 100 − %K` es redundancia exacta declarada por el propio autor; el propio Murphy afirma que **"casi todos los osciladores se parecen mucho"** |

### 29.3 Volumen

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Qué función cumple? | **RESPONDIDA** | **Indicador secundario**: confirma o advierte, no genera señal. Mide **"la intensidad o la urgencia que hay detrás del movimiento"**. §7.1–7.3 |
| ¿Qué podemos construir con volumen OHLCV? | **RESPONDIDA** | Volumen relativo, OBV (cero parámetros), Índice de Demanda, volumen en rupturas y consolidaciones, volumen direccional en bandas |
| ¿Qué no puede sustituir al order flow? | **RESPONDIDA, explícitamente** | El propio Murphy señala que **"se dispone de los niveles al alza y a la baja para los valores, pero no para los futuros"**, y que el Flujo Monetario de Birinyi requiere volumen por cada cambio de precio intradía → `GRANULAR`. **El OBV infiere dirección del signo del cierre, y el autor explica por qué esa inferencia es grosera** |

### 29.4 Volatilidad

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Qué herramientas utiliza? | **RESPONDIDA** | **ATR** (fluctuación real media), ancho de Bollinger, bandas STARC y Keltner, rango de barra, VM del Índice de Demanda |
| ¿Cómo conceptualiza expansión y contracción? | **RESPONDIDA** | **"Hay una tendencia de las bandas a que se alternen entre expansión y contracción"**; bandas muy separadas anuncian posible cambio de tendencia, muy juntas anuncian inicio de nueva tendencia. §9.6 |
| ¿Aporta forma relevante de medir contexto de volatilidad? | **RESPONDIDA** | **Sí: el ancho de banda y el ATR.** Ambos causales, un parámetro, adimensionales. **El ATR es además el normalizador que hace transferibles los demás umbrales entre regímenes** |

### 29.5 Soporte y resistencia

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Son causalmente definibles? | **PARCIAL** | **No sin retardo.** Requieren identificar pivotes, y Murphy es explícito: **"el chartista sólo puede estar razonablemente seguro de que se ha formado un mínimo de reacción después de que los precios hayan comenzado a subir"**. Formalizables declarando `k` |
| ¿Pueden formalizarse? | **PARCIAL** | Sí, como **densidad de actividad previa por nivel ponderada por recencia**, usando los tres determinantes que él mismo enumera |
| ¿Qué mecanismo psicológico propone? | **RESPONDIDA, y es lo mejor del libro** | Cuatro grupos de participantes con interés en el nivel; cambio de polaridad por reconocimiento del error; **margin call como forzador en instrumentos apalancados**. §4.4 |
| ¿Qué riesgo de look-ahead existe? | **RESPONDIDA** | `LOOK-AHEAD-LEVE`, cuantificado: `k` barras de confirmación, más el umbral de penetración que **el propio autor delega en el analista** |

### 29.6 Patrones

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Son reglas reproducibles o juicios visuales? | **RESPONDIDA: mayoritariamente juicios visuales** | El propio autor: **"los patrones pocas veces son tan claros como para que chartistas experimentados coincidan en su interpretación"**. Contabilidad: ≥9 GL para cabeza y hombros; definiciones **declaradas elásticas** en velas de 3-5 barras |
| ¿Cuáles pueden convertirse en eventos definidos? | **RESPONDIDA** | Los que no dependen de pivotes ni de forma: **día de cambio, hueco, compresión de rango, ruptura de canal, geometría de vela individual, puntos pivote**. Los chartistas nominales, no sin coste alto |

### 29.7 Indicadores técnicos

| Pregunta | Estado | Contenido |
|---|---|---|
| ¿Qué racional ofrece para cada familia? | **PARCIAL** | Ofrece racional psicológico para soportes, momento y volumen. **Para muchos indicadores concretos el racional es la construcción misma**, no un mecanismo de mercado |
| ¿Cuántos parámetros libres introducen? | **RESPONDIDA** | Contabilizado en §23: de 0 (geometría de vela, OBV) a ≥9 (patrones) y no acotados (Elliott, ciclos) |
| ¿Qué redundancia existe? | **RESPONDIDA** | Ocho familias informativas (§22.2), con redundancia severa dentro de la familia 1 |

### 29.8 Preguntas adicionales del encargo

| Pregunta | Estado | Contenido |
|---|---|---|
| **Divergencias** | **PARCIAL** | Variantes, criterios y confirmación documentados (§10.12). **`[VACÍO]`: cómo emparejar temporalmente los extremos del precio con los del oscilador no se especifica** |
| **Velas** | **RESPONDIDA** | La información está en relaciones continuas entre O,H,L,C; el propio capítulo lo corrobora por cuatro vías (§12.7). **`[VACÍO]`: la limitación intrabar no se menciona en ningún momento** |
| **Multi-timeframe** | **RESPONDIDA** | Top-down explícito; escala larga = dirección, corta = timing; regla de coincidencia obligatoria. **`[VACÍO]`: qué hacer cuando las escalas se contradicen** |
| **Reglas técnicas como modelo primario** | **RESPONDIDA** | Matriz de 20 candidatos en §24.1 |
| **Futuros y rollover** | **PARCIAL** | Tipos de contrato continuo, criterio de renovación por erosión de volumen, advertencia de liquidez. **`[VACÍO]`: método de compensación de saltos; efecto sobre el volumen en la transición** |
| **Timing** | **RESPONDIDA** | Cinco tácticas técnicas; separación análisis/timing; papel del intradía |
| **Sistemas** | **RESPONDIDA** | Plan de 5 pasos; tres categorías; criterios de robustez; métricas de evaluación (§20.C) |

---

## 30. MATRIZ MAESTRA DE CONOCIMIENTO — MURPHY

Diseñada para entrar directamente en la Knowledge Synthesis junto a las matrices de las dos fuentes anteriores.

| Concepto | Qué sostiene Murphy | Racional | Datos | Formalizable | Causal | Parámetros | Riesgo | Relevancia IRIS | Pendiente |
|---|---|---|---|---|---|---|---|---|---|
| **Premisa 1: descuenta todo** | El precio refleja toda la información | Oferta y demanda | — | No | — | — | **No falsable** | Baja | — |
| **Premisa 2: precios en tendencia** | Una tendencia en curso es más probable que continúe | Inercia (por analogía) | `OHLCV-OK` | **Sí** | Con retardo | 1–3 | Definición no única | **Alta** | ¿Se cumple en MNQ intradiario? |
| **Premisa 3: la historia se repite** | Los patrones funcionan porque la psicología no cambia | Psicología invariante | — | Sólo como estabilidad temporal | — | — | Inducción sin control | Media | ¿Es estable la importancia en el tiempo? |
| **Tendencia HH/HL** | Picos y valles crecientes sobre cierres | Estructura de Dow | `OHLCV-OK` | **Sí** | **Con retardo `k`** | 3–4 | Look-ahead leve | **Alta** | Valor de `k`; cierre vs extremo |
| **Tres escalas** | Principal, intermedia, menor; recursivas | Continuo de horizontes | `OHLCV-OK` | Sí | Sí | k | Fronteras arbitrarias | **Alta** | Qué escalas para MNQ |
| **Mercado lateral → no operar** | Las herramientas de tendencia fallan en rango | Naturaleza de las herramientas | `OHLCV-OK` | **Sí** | Con confirmación | 2 | Umbral arbitrario | **Muy alta** | **Vía de abstención por régimen** |
| **Soporte/resistencia** | Niveles con memoria de participantes | **4 grupos con interés en el nivel; margin call** | `OHLCV-OK` | Parcial | **Con retardo** | 3–5 | Look-ahead; penetración delegada | **Muy alta** | Formalización de densidad y `k` |
| **Determinantes: tiempo, volumen, recencia** | Definen la importancia de un nivel | Idem | `OHLCV-OK` | **Sí** | Sí | 3 | — | **Alta** | Parametrización |
| **Cambio de polaridad** | Apoyo roto se vuelve resistencia | Órdenes de compra se transforman en venta | `OHLCV-OK` | Sí | Con confirmación | 2–3 | Umbral de penetración | **Alta** | Umbral por volatilidad |
| **Números redondos** | Detienen movimientos | Objetivos psicológicos | `OHLCV-OK` | **Sí** | **Sí** | **1** | Sin evidencia | Media | ¿Aplica en intradiario? |
| **Líneas de tendencia** | Rectas sobre pivotes sucesivos | Geometría de la tendencia | `OHLCV-OK` | Sí | Con retardo | **≥7** | **Alto sobreajuste** | Media | ¿Compensan su coste? |
| **Canales** | Paralela a la línea básica | Idem | `OHLCV-OK` | Sí | Con retardo | ≥7 | Redibujado a posteriori | Media | — |
| **Fracaso en alcanzar el canal** | Aviso de cambio de tendencia | Debilitamiento del impulso | `OHLCV-OK` | **Sí, sin geometría** | Con retardo | 2 | — | **Alta** | Amplitud relativa de impulsos |
| **Retrocesos porcentuales** | 33/38/40/50/60/62/66% | Reversión parcial | `OHLCV-OK` | Como distribución | Con retardo | **≥5 niveles** | **Proliferación de niveles** | Media | ¿Tiene estructura la distribución? |
| **Días de cambio** | Nuevo extremo + cierre contrario | **Liquidación forzada; vacío de presión** | **`OHLCV-OK`** | **Sí** | **Sí** | **0–2** | **Mínimo** | **Alta** | ¿Predice a 1 minuto? |
| **Huecos** | Evento con tres tipos | Desequilibrio | `OHLCV-OK` | Evento sí, **tipo no** | Sí / **GRAVE** | 1 | Taxonomía retrospectiva | Media | Frecuencia en MNQ 24h |
| **Tamaño del patrón → movimiento** | Altura × duración predicen magnitud | Acumulación de desequilibrio | `OHLCV-OK` | **Sí** | Con retardo | 3 | — | **Alta** | Comprobar sin taxonomía |
| **Volumen esencial en suelos** | Asimetría techos/suelos | "Los máximos caen por su propio peso" | `OHLCV-OK` | **Sí** | Sí | 1 | — | Media | Comprobar asimetría |
| **Patrones de cambio** | H-C-H, dobles, triples, platillos, púas | Degradación de impulsos | `OHLCV-OK` | Con dificultad | Con retardo | **≥9** | **Muy alto** | Media | ¿Aportan sobre sus componentes? |
| **Compresión → ruptura** | Contracción de rango y volumen precede expansión | Equilibrio que se rompe | **`OHLCV-OK`** | **Sí** | **Sí** | **1–2** | Bajo | **Muy alta** | Umbral y ventana |
| **Límite temporal (2/3–3/4)** | La compresión caduca | Vértice del triángulo | `OHLCV-OK` | **Sí** | Con retardo | 2 | — | **Alta** | **Hipótesis con caducidad** |
| **Triángulo ascendente** | Dirección propia independiente del contexto | **Oferta fija frente a demanda creciente** | `OHLCV-OK` | Con dificultad | Con retardo | Alto | — | Media | Único patrón con dirección propia |
| **Volumen** | Mide intensidad; confirma, no señala | Presión compradora/vendedora | **`OHLCV-OK`** | **Sí** | **Sí** | 1 | — | **Alta** | Única fuente no-precio disponible |
| **"El volumen precede al precio"** | Afirmación predictiva explícita | Detección temprana de presión | `OHLCV-OK` | **Sí** | Sí | 1 | **Sin evidencia** | **Alta** | **Falsable directamente** |
| **OBV** | Acumulación con signo del cierre | Flujo neto inferido | **`OHLCV-OK`** | **Sí** | **Sí** | **0** | Inferencia grosera (admitida) | Media | ¿Mejora con barras finas? |
| **Interés abierto** | Dinero nuevo vs liquidación | Participación neta | **`OTRAS FUENTES`** | — | — | — | — | **No disponible** | Renuncia documentada |
| **Contratos continuos** | Cuatro tipos; renovación por volumen | Liquidez y saltos de prima | `OHLCV-COND` | Sí | Sí | 2 | **Saltos artificiales aprendibles** | **Muy alta** | **Método de ajuste** |
| **Top-down multiescala** | Larga = dirección, corta = timing | Perspectiva antes que precisión | `OHLCV-OK` | **Sí** | Sí | k | Escalas no transferibles | **Muy alta** | Qué escalas |
| **Medias móviles** | Seguidor, **"nunca anticipa"** | Suavizado | **`OHLCV-OK`** | **Sí** | **Sí** | 1–2 | **Familia 1: redundancia** | Media | SMA vs EMA sin evidencia |
| **Ancho de banda / ATR** | Volatilidad; alternancia expansión-contracción | Ciclo de volatilidad | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | Bajo | **Muy alta** | **Normalizador universal** |
| **Canal de Donchian** | Ruptura de extremos de N barras | Superación de niveles previos | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | Bajo | **Muy alta** | **Única con evidencia externa citada** |
| **Coef. de eficiencia** | Tendencialidad = neto / camino recorrido | Ruido vs dirección | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | Bajo | **Muy alta** | — |
| **ADX** | Magnitud de tendencia sin dirección | Movimiento direccional neto | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | Umbrales sin justificar | **Muy alta** | **Filtro de régimen** |
| **SAR parabólico** | Stop dinámico acelerado | Tendencia con tiempo límite | `OHLCV-OK` | **Sí** | **Sí (anticipable)** | 3 | Sistema continuo | Media | — |
| **"30% del tiempo hay tendencia"** | Los sistemas de tendencia fallan el 70% | — | — | — | — | — | **Sin fuente** | **Muy alta si es cierto** | Medir en MNQ |
| **Osciladores (4 familias)** | Extremos, divergencias, cruces de cero | Sobreextensión | **`OHLCV-OK`** | **Sí** | **Sí** | 1–3 | **Redundancia; reglas opuestas** | **Alta** | Qué familias conservar |
| **RSI** | Cociente de medias de ganancias/pérdidas | Asimetría alza-baja | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | Umbrales desplazables | **Alta** | Única familia asimétrica |
| **Estocástico** | Posición del cierre en el rango | **El cierre tiende al extremo en tendencia** | **`OHLCV-OK`** | **Sí** | **Sí** | 1–3 | — | **Muy alta** | **Premisa falsable; usa H y L** |
| **CCI / STARC / Keltner** | Desviación normalizada | Precio excesivo o ruptura | `OHLCV-OK` | **Sí** | **Sí** | 1–3 | **Reglas de signo opuesto** | **Alta** | **Hipótesis de interacción con régimen** |
| **Divergencia** | "El valor más grande del oscilador" | Impulso se debilita antes que el precio | `OHLCV-OK` | Parcial | Con retardo | ≥4 | **Emparejamiento no especificado** | Media | Reformulación continua |
| **Velas: geometría** | Cuerpo, sombras, posición del cierre | Psicología del período | **`OHLCV-OK`** | **Sí** | **Sí** | **0** | **Interpretación requiere intrabar** | **Alta** | ¿Aportan sobre retornos? |
| **Velas: patrones nominales** | ~40 patrones de cambio | Idem | `OHLCV-OK` | Con dificultad | Sí | **5–10** | Definiciones elásticas | Baja | ¿Aportan sobre la geometría? |
| **Filtro por zona pre-señal** | Patrón sólo cuenta si el oscilador está en extremo | Condición de admisibilidad | `OHLCV-OK` | **Sí** | **Sí** | 2 | — | **Alta** | **Arquitectura de dos componentes** |
| **P&F (3 registros)** | Muestreo por movimiento, no por reloj | Filtrado de ruido | `OHLCV-COND` | **Sí** | **Sí** | **2** | **Nº de señales lo fija el parámetro** | Media | Alternativa de muestreo |
| **Elliott** | 5-3 fractal con ratios de Fibonacci | Psicología de masas | — | **No** | **No** | **No acotados** | **No falsable** | **Baja** | Descartado |
| **Ciclos** | Periodicidad con armonía y sincronización | "Pulso" universal | `OHLCV-OK` | **No** (por inspección) | **No** | No acotados | **Ajuste retrospectivo** | Baja | — |
| **Asimetría temporal** | En tendencia se pasa más tiempo subiendo | **Reformulada por el propio autor** | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | — | **Alta** | — |
| **Estacionalidad anual** | Patrones por mes | Oferta física / calendario | `OHLCV-OK` | Sí | Sí | 1 | Pocas observaciones | Baja | Escala inadecuada |
| **Estacionalidad intradiaria** | **No tratada** | — | `OHLCV-OK` | **Sí** | **Sí** | 0–1 | — | **Muy alta** | **`[VACÍO]` del libro** |
| **Puntos pivote intradía** | 7 niveles × 4 momentos de sesión | Referencias de la sesión | **`OHLCV-OK`** | **Sí** | **Sí** | 1–3 | Requiere definir sesión | **Muy alta** | **Única técnica intradiaria propia** |
| **Recompensa/riesgo 3:1** | Mínimo exigible | Acierto del 40% | `OHLCV-OK` | Sí | Depende | 1+ | **Normativa sin derivar** | Media | Derivar de nuestra tasa real |
| **Stop por volatilidad** | Mayor volatilidad, stop más amplio | Evitar ruido | **`OHLCV-OK`** | **Sí** | **Sí** | **1** | — | **Alta** | Multiplicador |
| **Market Profile** | Distribución de precio por tiempo | **Urgencia asimétrica entre participantes** | `OHLCV-COND` | Parcial | Sí | 2 | Supuesto de continuidad intrabar | Media | Modelo de sesión |
| **Amplitud / sentimiento / intermercado** | Confirmación desde fuera del precio | Diversas | **`OTRAS FUENTES`** | — | — | — | — | **No disponible** | Cuatro renuncias documentadas |
| **Plan de 5 pasos** | Concepto → reglas → visual → prueba → evaluación | Objetividad | — | — | — | — | — | **Muy alta** | Marco de proceso |
| **Estabilidad paramétrica/temporal** | Robustez ante perturbación | Evitar ajuste a ruido | — | **Sí** | — | — | — | **Muy alta** | **Test barato y aplicable** |
| **Rechazo del out-of-sample** | "Uso la totalidad de las series" | Conceptos firmes, poca optimización | — | — | — | — | **Circular; contradice al cap. 9** | **No adoptable** | Tensión registrada |
| **"Salidas > entradas"** | Las salidas son más difíciles e importantes | Gestión de imprevistos | — | — | — | — | — | **Alta** | Aportación propia |
| **Promedio por operación > costes** | Criterio de viabilidad | Aritmética | `OHLCV-OK` | **Sí** | — | — | — | **Muy alta** | Edge mínimo en MNQ |


---

## 31. PREGUNTAS ABIERTAS PARA LA KNOWLEDGE SYNTHESIS

Lista numerada y exhaustiva de decisiones que **no pueden cerrarse sólo con Murphy**. Incluye las tensiones entre las tres fuentes. **No se resuelven aquí.**

### 31.1 Tensiones entre las tres fuentes

1. **¿Es exigible la validación fuera de muestra, o bastan los criterios de robustez paramétrica, temporal y entre mercados?** El apéndice C de Murphy la rechaza explícitamente; el capítulo 9 del propio Murphy la exige; las dos fuentes anteriores la consideran no negociable.
2. **¿Dónde reside la estructura explotable: en el corto o en el largo plazo?** Murphy afirma que la aleatoriedad domina el corto plazo; una fuente anterior sostiene que las estrategias algorítmicas rinden mejor a frecuencias más altas.
3. **¿Es viable un sistema de instrumento único?** **Las tres fuentes lo desaconsejan, cada una por una vía distinta** (falso descubrimiento específico de un activo; preferencia por apilar universos; estabilidad entre mercados como criterio de robustez). ¿Qué defensas sustitutivas son suficientes?
4. **¿Debe la decisión tomarse en intradiario o refinarse en intradiario?** Murphy asigna al intradía un papel subordinado y advierte tres veces que es más difícil.
5. **¿Cómo se contabiliza el multiple testing cuando la fuente de hipótesis (Murphy) ofrece decenas de indicadores parametrizables y ninguna contabilidad de intentos?**
6. **¿Se modelan los costes desde el primer backtest o al final?** Murphy los excluye de las pruebas por "pureza"; las fuentes anteriores exigen lo contrario.
7. **¿Qué papel tiene el juicio discrecional?** Murphy defiende la intervención del operador cuando el sistema no reconoce estructuras visibles.
8. **¿Cómo se seleccionan las features?** Murphy: por comodidad del operador. Fuentes anteriores: por importancia medida fuera de muestra con control de sustitución.
9. **¿Qué constituye evidencia?** Murphy privilegia la observación empírica y desconfía de las técnicas estadísticas; las fuentes anteriores sostienen lo inverso.

### 31.2 Formulación del problema

10. ¿Debe IRIS predecir dirección, magnitud, volatilidad, evento o decisión?
11. ¿Arquitectura de un componente o de dos? **Murphy aporta cinco formulaciones distintas de arquitectura bicomponente** (análisis/timing, escala larga/corta, precio/volumen, patrón filtrado por oscilador, ADX/señal) y una tricomponente (qué/cuándo/cuánto). ¿Se corresponden con la separación side/size de la segunda fuente, o son ejes distintos?
12. **¿Cómo se define la abstención?** Ahora existen al menos cinco vías registradas: régimen lateral (Murphy), umbral de confianza, meta-etiqueta, discretización del tamaño, y umbrales asimétricos de entrada/salida.
13. ¿Es la identificación del régimen el problema principal, dado que —si la cifra del 30% es aproximadamente correcta— las herramientas de tendencia fallarían la mayor parte del tiempo?
14. ¿Debe una regla técnica actuar como componente primario, o como feature entre otras?

### 31.3 Datos y muestreo

15. ¿Qué resolución base y qué esquema de muestreo? Ahora hay tres candidatos de tres fuentes: barras temporales, barras de volumen/dólar, y **muestreo por movimiento de precio (P&F)**.
16. ¿Qué método de rollover? Murphy describe cuatro tipos de contrato continuo y un criterio de renovación por erosión de volumen; ninguna fuente describe un método de compensación de saltos completo.
17. ¿Cómo se define "la sesión" en un instrumento de casi 24 horas? Condiciona puntos pivote, Market Profile, estacionalidad intradiaria y la propia noción de "día".
18. ¿Cómo se trata el volumen durante la transición de contratos?
19. ¿Cuánto histórico se necesita y cuántas observaciones efectivamente independientes contiene?

### 31.4 Features

20. ¿Qué familias informativas de las ocho identificadas se conservan, y con qué representante cada una?
21. ¿Cuál es el valor de `k` (barras de confirmación de pivote) y compensa el retardo que introduce?
22. ¿Se usa la geometría continua de las velas o detectores de patrones nominales?
23. ¿Se incorpora la estructura de niveles (familia 8), única con problema de causalidad, o se prescinde de ella pese a tener el mejor mecanismo económico del libro?
24. ¿Se incorpora la estacionalidad intradiaria como contexto, y cómo se evita que el modelo aprenda el reloj en lugar del mercado?
25. ¿Se prueba el muestreo P&F como transformación alternativa del dataset?

### 31.5 Hipótesis a testear

26. De las **trece hipótesis falsables de §21.4**, ¿cuáles se testean, en qué orden, y cómo se contabilizan en el presupuesto de multiple testing?
27. ¿Es cierta la hipótesis de régimen —que la relación entre desviación normalizada y retorno futuro cambia de signo según el contexto— en MNQ intradiario?
28. ¿Cuál es la fracción real de tiempo en régimen tendencial en MNQ, y cómo se mide causalmente?
29. ¿Precede el volumen al precio en nuestros datos?
30. ¿Tiene estructura la distribución de profundidades de retroceso?

### 31.6 Validación y evaluación

31. ¿Qué esquema de validación, y cómo se integran los criterios de robustez de Murphy (estabilidad paramétrica y temporal) con los procedimientos de las fuentes anteriores?
32. ¿Cuál es el edge mínimo por operación que hace viable la estrategia, dados los costes reales de MNQ?
33. ¿Qué métricas son primarias? Ahora hay tres conjuntos: métricas de ML, métricas económicas de riesgo-retorno, y las de sistema de Murphy (factor beneficio, promedio por operación, reducción distinguiendo origen).
34. ¿Cómo se agregan múltiples señales en una decisión, problema que **ninguna de las tres fuentes resuelve**?

### 31.7 Decisión y ejecución

35. ¿Sizing fijo o proporcional a la confianza?
36. ¿Stops escalados por volatilidad o situados en niveles estructurales? Murphy recomienda ambos sin criterio de prioridad.
37. ¿Se adoptan salidas asimétricas, dado que Murphy sostiene que **las salidas importan más que las entradas** y que un esquema de entrada/salida asimétrico genera naturalmente el estado de no-posición?
38. ¿Cómo se determina el objetivo de beneficio, requisito del criterio recompensa/riesgo?

### 31.8 Producción

39. ¿Cómo se monitoriza la validez del sistema desplegado, dado que Murphy documenta que las relaciones cambian con el régimen y las duraciones cíclicas "cambian continuamente"?
40. ¿Con qué frecuencia se reentrena y bajo qué criterio se retira?

---

## 32. REGISTRO DE DECISIONES DELIBERADAMENTE NO TOMADAS

Conforme al encargo, este estudio **NO ha seleccionado**:

- ni el timeframe, ni el horario, ni el tipo de barra, ni el esquema de muestreo, ni las ventanas;
- ni el target, ni el sistema de etiquetado, ni las barreras, ni los umbrales de PT/SL;
- ni las features definitivas, ni los indicadores definitivos, ni los patrones definitivos;
- ni una regla LONG/SHORT, ni el criterio de NO TRADE;
- ni la arquitectura (un componente, dos o tres), ni el modelo primario, ni el secundario;
- ni el algoritmo de aprendizaje, ni los hiperparámetros;
- ni el método de validación, ni el sizing, ni la ejecución, ni la estrategia final;
- ni el método de rollover, ni la definición de sesión.

**Lo que este estudio sí ha establecido son restricciones y clasificaciones**, no decisiones:

- **Prohibiciones de causalidad**: media centrada, umbrales fijados por inspección visual del histórico completo, clasificación retrospectiva de huecos, cualquier objeto que requiera conocer el desenlace.
- **Exclusiones por datos**: interés abierto, amplitud de mercado, sentimiento, intermercado, order flow, secuencia intrabar.
- **Exclusiones por no falsabilidad**: ondas de Elliott, identificación de ciclos por ajuste visual.
- **Contabilidad de grados de libertad** de cada técnica formalizable.
- **Trece hipótesis falsables** derivadas de la fuente.

Todo permanece abierto hasta:

```text
JANSEN            (completado — Knowledge Base 01)
+
LÓPEZ DE PRADO    (completado — Knowledge Base 02)
+
MURPHY            (completado — Knowledge Base 03)
        ↓
IRIS PROJECT — KNOWLEDGE SYNTHESIS
        ↓
ANÁLISIS DE LOS DATOS REALES DEL MNQ
        ↓
FORMULACIÓN DEL PROBLEMA
        ↓
DISEÑO EXPERIMENTAL → BASELINES → MODELOS → VALIDACIÓN → SEÑALES
```

---

## 33. CONTROL DE CALIDAD

| Requisito del encargo | Estado |
|---|---|
| 19 capítulos revisados | ✔ §1–§19 |
| Apéndices A, B, C, D revisados | ✔ §20 (A, B, C) y §8 (D) |
| Libro completo cubierto (547 págs.) | ✔ |
| Mapa completo con niveles A/B/C/D | ✔ Cabecera |
| Atribución `[MURPHY]` / `[INTERPRETACIÓN]` / `[IMPLICACIÓN]` / `[VACÍO]` / `[CONOCIMIENTO EXTERNO]` | ✔ Sistemática |
| Disponibilidad de datos clasificada | ✔ Toda técnica relevante |
| Causalidad y look-ahead evaluados | ✔ Escala de 4 niveles en §0.3 |
| Subjetividad documentada | ✔ Incluidas las admisiones del propio autor |
| Grados de libertad identificados | ✔ §23, §25 |
| Figuras consultadas cuando eran esenciales | ✔ Buenas/malas oscilaciones de Dow (§2.2) y anatomía de cabeza y hombros (§5.2) |
| Limitaciones identificadas | ✔ §26, §27 |
| Tensiones con fuentes anteriores registradas | ✔ §28.3 |
| Matriz maestra completa | ✔ §30 |
| Preguntas para la síntesis | ✔ §31 (40 preguntas) |
| Ninguna decisión de IRIS cerrada | ✔ §32 |
| OCR no reejecutado | ✔ Se usó la capa de texto del PDF |

---

## CHECKPOINT FINAL

```
PDF: Murphy OCR — 547 páginas (índice interno 0–547)
Última página efectivamente revisada: idx 529 (libro completo)
Último capítulo completado: LIBRO COMPLETO — 19 capítulos + apéndices A, B, C, D
Última sección del KB completada: §33 (control de calidad)
Siguiente capítulo/sección: — (ninguna; estudio finalizado)
Pendientes: ninguno
Estado: COMPLETE
```

**Fin del documento — IRIS PROJECT KNOWLEDGE BASE 03.**
