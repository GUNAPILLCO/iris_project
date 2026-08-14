# 0001 — QA: inventario estructural de data/00_source

## Identificacion

- **id:** 0001
- **fecha:** 2026-08-13
- **tipo:** QA
- **hipotesis_o_pregunta:** A1 (rollover), A2 (volumen en transicion), A3 (defectos de integridad), A4 (cobertura historica) de `IRIS_KNOWLEDGE_SYNTHESIS.md`
- **parent_id:** NA

## Trazabilidad de reproducibilidad

- **dataset_usado:** investigacion (equivalente a todo el snapshot en este momento: el hold-out todavia no existia como concepto congelado cuando se ejecuto esta comprobacion)
- **dataset_version:** IRIS-MNQ-SRC-20191223_20260731-e382a75ac222 (migrado el 2026-08-14 desde IRIS-MNQ-SRC-2026-08-14-e382a75a; mismo contenido, mismo hash_snapshot_sha256 -- ver 0003)
- **code_version:** pre-src (inspeccion realizada con scripts ad hoc en la sesion, no conservados como artefacto versionado; el manifest reproducible que fija el snapshot se genera en 0002 con `src/build_dataset_manifest.py`)
- **seed:** NA
- **config_ref:** NA

## Contenido

### Que se hizo

Inspeccion de solo lectura de los 27 archivos de `data/00_source/*.Last.txt`: tamano, numero de filas, primer y ultimo timestamp por archivo, validez de formato (6 campos por linea), deteccion de timestamps duplicados o fuera de orden dentro de cada archivo, validez estructural de OHLC, deteccion de solapamientos temporales entre contratos consecutivos, y deteccion de valores de volumen atipicos.

### Parametros / configuracion exacta

Sin parametros de investigacion: comprobaciones puramente estructurales sobre el 100% de las lineas de los 27 archivos.

### Resultado

Ver `reports/00_inventario_estructural_data_source.md` para el detalle completo. Resumen: 0 lineas malformadas, 0 duplicados de timestamp, 0 desorden temporal, 0 OHLC invalido en los 27 archivos; secuencia de 27 contratos trimestrales completa sin huecos; 3 de 26 transiciones de contrato con solapamiento temporal (19-20, 20-21, 25-26, ~8-10 dias cada una); 3 barras con volumen 100-170x el maximo habitual (2 en `22_mnq_09_25`, 1 en `24_mnq_03_26`); el contrato `26_mnq_09_26` esta incompleto (54.015 filas frente a ~85.000-95.000 tipicas).

### Interpretacion

El snapshot es estructuralmente solido para iniciar la fase empirica (parseo, orden y OHLC intra-archivo sin defectos). Los dos hallazgos reales (patron de solapamiento inconsistente entre contratos, y barras de volumen atipico) son anomalias que no impiden avanzar, pero que deben explicarse o resolverse explicitamente en FASE 0 antes de construir la serie continua o de usar volumen como feature.

### Decision resultante

Se uso la existencia de 23 transiciones limpias (sin solapamiento) frente a solo 3 con solapamiento para exigir que la frontera del hold-out coincida con una transicion limpia, lo cual informo directamente la Alternativa B aprobada en `config/holdout.yaml`. No se tomo ninguna decision sobre metodo de rollover ni sobre tratamiento del volumen atipico: quedan abiertas para FASE 0.

### Exposicion pre-lock del hold-out (correccion documental, 2026-08-14)

Este intento se ejecuto **antes** de que existiera ninguna frontera de hold-out congelada, sobre los 27 archivos completos de `data/00_source/`. Eso significa que hubo exposicion estructural real -- no solo teorica -- sobre el periodo que `config/holdout.yaml` reservo despues como hold-out (`22_mnq_09_25.Last.txt` a `26_mnq_09_26.Last.txt`, frontera `2025-06-23 00:00:00` -> `2026-07-31 20:10:00`). No debe afirmarse en ningun documento del repositorio que el hold-out "nunca fue inspeccionado"; lo correcto es que fue objeto de QA pre-lock, no de analisis predictivo.

Sobre esos 5 archivos, especificamente, este intento realizo:

- Escaneo estructural completo (parseo de 6 campos, timestamps duplicados/desordenados, validez de OHLC) -- sin hallazgos de corrupcion.
- Analisis de solapamientos contractuales, incluido el solapamiento real `25_mnq_06_26 -> 26_mnq_09_26` (~10 dias), integramente dentro del hold-out.
- Deteccion de las 3 barras de volumen extremo ya conocidas: 2 en `22_mnq_09_25.Last.txt` (2025-07-01 10:08 y 2025-07-15 13:52) y 1 en `24_mnq_03_26.Last.txt` (2026-01-27 03:44).
- Conteo de filas, bytes y primer/ultimo timestamp por archivo.

Sobre esos mismos 5 archivos, este intento **no** realizo: ningun analisis de retornos, de targets/labeling, de senales, de estrategias, de predictibilidad, ni ninguna medicion de desempeno (rentabilidad, drawdown u otra metrica economica o de sistema).

**Clasificacion:** QA pre-lock (CLAUDE.md, regla 7), no experimento predictivo. Ver tambien `config/holdout.yaml` (seccion `exposicion_pre_lock`) y `experiments/log/0002_qa_congelacion_snapshot_y_holdout.md`.

## Clasificacion de repeticion

No aplica: es el primer intento registrado.
