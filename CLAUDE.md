# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con código en este repositorio.

## Estado del proyecto

IRIS es un proyecto de investigación que busca determinar si existe predictibilidad intradía explotable en MNQ (futuros Micro E-mini Nasdaq-100) suficiente para superar los costes de operar. **En este repositorio todavía no existe código fuente.** Actualmente el repositorio contiene únicamente:

- `data/` — histórico de precios crudos (ver detalle más abajo).
- `docs/` — una fase bibliográfica ya completada, compuesta por tres knowledge bases y un documento de síntesis.

El proyecto acaba de cerrar su fase bibliográfica y está a punto de iniciar la **fase de análisis empírico** sobre los datos de MNQ. Si se solicita escribir código en este repositorio, lo más probable es que se trate de herramientas para esa fase empírica: comprobaciones de integridad de datos, construcción de la serie continua (rollover), análisis de propiedades estadísticas, esquemas de muestreo, etiquetado, validación, investigación de features, etc.

Todavía no existen comandos de build, lint ni test porque no hay código ni manifiesto de dependencias en el repositorio.

## Reglas permanentes del repositorio

Estas reglas no son preferencias del proyecto: son restricciones vinculantes para cualquier sesión de trabajo en este repositorio, sea cual sea la tarea.

1. **`data/00_source/` es READ ONLY lógico.** Nunca modificar, sobrescribir, renombrar ni eliminar ningún archivo de esa carpeta, bajo ninguna circunstancia, incluidas tareas de "limpieza" o "corrección". Todo dato procesado o derivado debe escribirse en otra ubicación (ver regla 11).
2. **Los cuatro artefactos bibliográficos de `docs/` son documentación de referencia, no archivos vivos.** `IRIS_KNOWLEDGE_BASE_01_Jansen.md`, `IRIS_KNOWLEDGE_BASE_02_LopezDePrado.md`, `IRIS_KNOWLEDGE_BASE_03_Murphy.md` e `IRIS_KNOWLEDGE_SYNTHESIS.md` no deben editarse durante las etapas empíricas. Solo se tocan cuando el usuario solicita explícitamente una tarea de mantenimiento documental sobre alguno de ellos en concreto.
3. **`IRIS_KNOWLEDGE_SYNTHESIS.md` es la referencia metodológica principal de la etapa empírica.** Debe consultarse antes de proponer cualquier decisión metodológica (muestreo, etiquetado, esquema de validación, features, familia de modelo, etc.): define las restricciones vinculantes, el mapa de preguntas abiertas y el orden de dependencias que debe seguir la agenda empírica.
4. **Ninguna decisión histórica de versiones anteriores del proyecto es vinculante por defecto.** Targets OPC, horarios de sesión, definiciones de régimen, lookbacks, configuraciones de barrera, modelos, métricas o protocolos de iteraciones anteriores de IRIS deben considerarse no vinculantes salvo que vuelvan a derivarse y aceptarse explícitamente dentro de la fase empírica actual. No reutilizarlos silenciosamente "porque así estaba antes".
5. **Antes de iniciar cualquier exploración predictiva debe definirse y reservarse un hold-out final temporal.** Una vez reservado, el hold-out no puede utilizarse para exploración, estadísticas descriptivas orientadas a decisiones, selección metodológica, tuning, comparación de alternativas, evaluación predictiva ni ninguna otra decisión de investigación. Sí puede recibir comprobaciones estructurales estrictamente necesarias (por ejemplo, integridad de esquema o de timestamps) y transformaciones deterministas previamente especificadas y congeladas a partir del conjunto de investigación, siempre que sus resultados no se utilicen para modificar esas decisiones. Todo acceso al hold-out, del tipo que sea, debe quedar trazado. Cualquier acceso fuera de estos casos requiere autorización explícita del usuario para ese acceso concreto.
6. **Antes de contrastar cualquier hipótesis predictiva debe existir un registro de intentos.** Todo experimento, parametrización o variante relevante debe quedar registrado, incluidos los resultados negativos y los abandonados. No deben ejecutarse pruebas predictivas ad hoc "solo para comprobar" sin registrarlas.
7. **Las comprobaciones de integridad de datos no deben confundirse con experimentos de predictibilidad.** Validación de esquema, comprobación de timestamps, detección de duplicados, detección de gaps, verificación de contratos y rollover, comprobación de OHLC inválido y detección de barras faltantes son trabajo de preprocesado/QA, y quedan exentas del requisito de registro de intentos de la regla 6. Nunca dejar que un trabajo de integridad se convierta silenciosamente en (o se use para justificar) una afirmación predictiva.
8. **No seleccionar prematuramente target, horizonte, esquema de labeling, features, indicadores, modelo o arquitectura, hiperparámetros, mecanismo de abstención, sizing ni estrategia.** Debe seguirse la agenda y el grafo de dependencias de `IRIS_KNOWLEDGE_SYNTHESIS.md` §17–§18, no una secuencia puramente lineal: dicho grafo documenta explícitamente una circularidad entre el muestreo (C), configuraciones provisionales de horizonte/target (F) y la independencia efectiva de las observaciones (G), que debe abordarse como tal y no simplificarse en un orden estrictamente secuencial. Cualquier configuración provisional de horizonte, target, muestreo o labeling usada para resolver esa circularidad **no constituye una decisión definitiva** y debe tratarse como hipótesis de trabajo sujeta a revisión. Si una tarea parece requerir saltarse la agenda o cerrar prematuramente una decisión, debe señalarse en lugar de proceder.
9. **Toda transformación de datos debe ser causal cuando corresponda y evitar look-ahead/leakage.** La disciplina point-in-time se aplica a cualquier paso de preprocesado, cálculo de features o etiquetado.
10. **Todo artefacto derivado debe ser reproducible, trazable y almacenarse dentro del repositorio.** El script o configuración que genera un resultado debe conservarse junto a él, con metadatos suficientes (parámetros, versión de los datos de entrada, fecha) para poder regenerarlo. No deben producirse resultados puntuales no reproducibles.
11. **No inventar frameworks, dependencias, estructura de carpetas ni stack tecnológico sin necesidad.** Cuando una decisión estructural relevante no esté definida (por ejemplo, dónde viven los datos procesados, qué lenguaje o librerías usar, cómo se registra el log de experimentos), debe proponerse y justificarse al usuario antes de implementarla, no decidirse en silencio.
12. **Cualquier cambio metodológico relevante debe documentarse**: qué cambia, por qué, qué evidencia lo respalda, qué archivos se ven afectados, qué artefactos deben regenerarse como consecuencia, y qué riesgos introduce.
13. **No realizar operaciones de gobernanza de Git sin autorización explícita del usuario.** Esto incluye `git commit`, `git push`, merge, rebase, creación o eliminación de ramas, cualquier modificación destructiva del historial (reset --hard, force push, reescritura de commits, etc.) y cualquier cambio relevante a `.gitignore` o `.gitattributes`. Nunca versionar credenciales, secretos ni archivos sensibles.

## Naturaleza de este documento

`CLAUDE.md` es un documento operativo vivo del repositorio, no un artefacto congelado. Debe actualizarse a medida que aparezcan código, estructura de carpetas, comandos de build/lint/test, dependencias o convenciones efectivamente adoptadas en el proyecto, de modo que siga reflejando el estado real del repositorio.

Estas actualizaciones tienen un límite: no pueden modificar silenciosamente ninguna restricción metodológica ni ninguna decisión de proyecto ya fijada (incluidas las reglas permanentes de este documento y lo establecido en `IRIS_KNOWLEDGE_SYNTHESIS.md`). Todo cambio de ese tipo debe ser explícito, justificado y trazable, siguiendo el mismo criterio de documentación exigido en la regla 12.

## Idioma de trabajo

- Trabajar y comunicarse con el usuario siempre en español.
- Todos los informes, análisis, decisiones metodológicas, documentación, archivos Markdown y explicaciones deben redactarse en español.
- Los comentarios de código y docstrings deben escribirse preferentemente en español.
- Los nombres estándar de librerías, APIs, comandos, clases, funciones externas y terminología técnica establecida pueden conservarse en inglés cuando sea lo natural.
- Los identificadores internos de código pueden utilizar inglés si mejora la claridad o sigue convenciones estándar; no traducir artificialmente términos técnicos.
- No cambiar de idioma salvo solicitud explícita del usuario.

## Datos (`data/`)

- `data/00_source/*.Last.txt` — histórico de barras de futuros de MNQ, un archivo por contrato, con nomenclatura `NN_mnq_MM_AA.Last.txt` (índice secuencial, mes, año a dos dígitos), cubriendo contratos desde marzo de 2020 hasta septiembre de 2026. **READ ONLY — ver regla 1.** Son contratos individuales, no una serie continua: construir una serie continua (método de rollover, ajuste de gaps/ratio, precios crudos frente a ajustados) es una de las primeras preguntas empíricas abiertas (síntesis §A1, §3.12, FASE 0).
- Formato: delimitado por punto y coma, sin cabecera: `AAAAMMDD HHMMSS;open;high;low;close;volume`. Una fila por barra de un minuto. Los timestamps son la hora de sesión tal como se exportó (la zona horaria aún no está verificada — pregunta abierta, síntesis A3/D1).
- `data/ninja_trader_accounts.xlsx` — exportación de cuentas de NinjaTrader (metadato de la plataforma origen, no datos de precio). Mismo tratamiento de solo lectura que el resto de `data/`, salvo indicación contraria del usuario.
- El comentario en `.gitignore` sugiere que `/data/` estuvo en algún momento excluido del control de versiones, pero esa exclusión está actualmente comentada: los archivos de datos sí están versionados. Nunca escribir salidas procesadas o generadas dentro de `data/00_source/`; si aún no existe una ubicación para datos procesados, proponer una (regla 11) en lugar de improvisar algo ad hoc.

## Documentación (`docs/`)

`docs/` contiene la memoria de investigación del proyecto. Léase en este orden cuando se necesite contexto — cada etapa se apoya explícitamente en la anterior y ninguna de ellas diseña ni decide sobre IRIS (deliberado — ver regla 4 y las secciones §0.4/§23 de la propia síntesis):

1. `docs/IRIS_KNOWLEDGE_BASE_01_Jansen.md` — Stefan Jansen, *Machine Learning for Algorithmic Trading* (2ª ed.). Etiqueta: `[JANSEN]`.
2. `docs/IRIS_KNOWLEDGE_BASE_02_LopezDePrado.md` — Marcos López de Prado, *Advances in Financial Machine Learning*. Etiqueta: `[LDP]`.
3. `docs/IRIS_KNOWLEDGE_BASE_03_Murphy.md` — John J. Murphy, *Análisis Técnico de los Mercados Financieros*. Etiqueta: `[MURPHY]`.
4. `docs/IRIS_KNOWLEDGE_SYNTHESIS.md` — **el documento de referencia para iniciar cualquier trabajo real** (regla 3). Cruza y concilia las tres knowledge bases en un mapa canónico de 79 preguntas abiertas (20 bloques, A–T), una matriz de cobertura cruzada, principios elevados a `[RESTRICCIÓN METODOLÓGICA]` (restricciones vinculantes) y una agenda empírica de 8 fases (FASE 0–7) que debe seguirse en orden de dependencias.

Los cuatro documentos están cubiertos por la regla 2 (no editar durante la fase empírica). `docs/books_and_references/` contiene los PDFs originales de los que se derivaron las knowledge bases; está excluido en `.gitignore`, por lo que no estará presente en un clon nuevo del repositorio, y no deben añadirse ahí binarios grandes esperando que queden versionados.

### Convenciones usadas en `docs/` (todos los documentos, en español)

| Etiqueta | Significado |
|---|---|
| `[CONSENSO FUERTE]` | Las fuentes coinciden y no hay objeción material pendiente — usado con extrema parsimonia. |
| `[CONVERGENCIA]` | Las fuentes llegan a una idea similar por caminos distintos, sin demostrar necesariamente lo mismo. |
| `[COMPLEMENTARIEDAD]` | Una fuente aporta la pieza que resuelve un vacío de otra. |
| `[TENSIÓN]` | Posiciones incompatibles o parcialmente incompatibles entre fuentes. |
| `[CONTRADICCIÓN INTERNA]` | Una misma fuente sostiene posiciones incompatibles. |
| `[RESTRICCIÓN METODOLÓGICA]` | Condición que debe respetarse sea cual sea la arquitectura final. |
| `[HIPÓTESIS CANDIDATA]` | Idea razonable y falsable, aún no contrastada. |
| `[PREGUNTA EMPÍRICA]` | Solo resoluble analizando directamente los datos de MNQ. |
| `[DECISIÓN DE DISEÑO ABIERTA]` | Varias alternativas defendibles; aún no elegida. |
| `[VACÍO]` | Las tres fuentes son insuficientes en ese punto. |
| `[DESCARTABLE METODOLÓGICAMENTE]` | No debe avanzar en su forma actual (look-ahead inevitable, no falsabilidad, irreproducibilidad, etc.). |

Notación de trazabilidad: `J-n` / `L-n` / `M-n` referencian una pregunta original concreta de KB01/02/03; `KB0X §Y` referencia una sección concreta.

## Decisiones de diseño pendientes

Nada de lo siguiente está decidido todavía: timeframe/tipo de barra, esquema de muestreo, umbrales, esquema de labeling (por ejemplo, configuración de triple barrera), horizonte, features/indicadores, arquitectura LONG/SHORT/NO_TRADE, modelo primario o ensemble, sizing/stops, ni diseño final de backtest. Si una tarea requiere fijar alguno de estos puntos, debe señalarse como decisión abierta en lugar de elegirse en silencio (ver reglas 8 y 11).
