# Inventario estructural de `data/00_source/`

**Tipo:** QA de integridad estructural (no es un experimento predictivo — CLAUDE.md, regla 7).
**Alcance:** exclusivamente `data/00_source/*.Last.txt`, en modo lectura. No se modifico ningun archivo de esa carpeta.
**dataset_version referenciado:** `IRIS-MNQ-SRC-20191223_20260731-e382a75ac222` (migrado el 2026-08-14 desde `IRIS-MNQ-SRC-2026-08-14-e382a75a`; mismo contenido, mismo `hash_snapshot_sha256` — ver `config/dataset_manifest.yaml`, campo `superseded_version_id`, y `experiments/log/0003_migracion_version_id_determinista.md`).
**Referenciado por:** `experiments/log/0001_qa_inventario_estructural_data_source.md`.

**Nota post-lock (anadida 2026-08-14):** esta comprobacion se ejecuto antes de que existiera ninguna frontera de hold-out. Los archivos `22_mnq_09_25.Last.txt` a `26_mnq_09_26.Last.txt` -- referenciados en las secciones 3 y 4 de este informe -- quedaron reservados despues como hold-out en `config/holdout.yaml` (frontera `2025-06-23 00:00:00` -> `2026-07-31 20:10:00`). Los hallazgos de este informe sobre esos archivos son exposicion estructural pre-lock (QA), no exploracion predictiva: no incluyen ningun analisis de retornos, targets, senales, estrategias, predictibilidad ni desempeno. Detalle completo en `config/holdout.yaml` (seccion `exposicion_pre_lock`) y en `experiments/log/0001_qa_inventario_estructural_data_source.md`.

## 1. Cobertura general

- 27 archivos, un contrato trimestral por archivo, secuencia H/M/U/Z completa desde `00_mnq_03_20` (Mar-2020) hasta `26_mnq_09_26` (Sep-2026), sin trimestre faltante.
- Rango temporal total del snapshot: `2019-12-23 03:01:00` -> `2026-07-31 20:10:00`.
- 2.329.783 filas totales, 122.523.200 bytes totales.
- `26_mnq_09_26.Last.txt` esta **incompleto**: 54.015 filas frente a las ~85.000-95.000 filas tipicas de un trimestre completo, porque el contrato Sep-2026 (U26) aun no habia expirado en la fecha del snapshot.

## 2. Formato y parseo

Verificado linea por linea en los 27 archivos:

| Comprobacion | Resultado |
|---|---|
| Campos por linea (separador `;`) | Exactamente 6 en el 100% de las lineas, en todos los archivos |
| Lineas malformadas / no parseables | 0 |
| Timestamps duplicados dentro de un mismo archivo | 0 |
| Timestamps fuera de orden dentro de un mismo archivo | 0 |
| OHLC estructuralmente invalido (H<L, H<O/C, L>O/C) | 0 |
| Volumen negativo o vacio | 0 |

No se detecto corrupcion estructural en ningun archivo.

## 3. Solapamientos temporales entre contratos consecutivos

De las 26 transiciones posibles entre archivos consecutivos, 23 son limpias (sin solapamiento, solo el hueco de fin de semana esperable). Las siguientes 3 presentan solapamiento real:

| Transicion | Contrato saliente termina | Contrato entrante empieza | Solapamiento aprox. |
|---|---|---|---|
| 19_mnq_12_24 -> 20_mnq_03_25 | 2024-12-20 21:30 | 2024-12-12 03:01 | ~8 dias |
| 20_mnq_03_25 -> 21_mnq_06_25 | 2025-03-22 15:03 | 2025-03-13 03:01 | ~9 dias |
| 25_mnq_06_26 -> 26_mnq_09_26 | 2026-06-18 13:30 | 2026-06-08 03:03 | ~10 dias |

Este patron es inconsistente con el resto del snapshot y queda pendiente de explicacion en FASE 0 (afecta directamente a las preguntas A1/A2 de `IRIS_KNOWLEDGE_SYNTHESIS.md`: metodo de rollover y tratamiento del volumen en la transicion de contratos). No se ha propuesto ni adoptado ningun metodo de rollover a partir de esta observacion.

## 4. Barras con volumen atipico

Tres barras de un minuto con volumen 100-170x el maximo habitual del resto del snapshot (que ronda 8.500-31.000):

| Archivo | Timestamp | Volumen | OHLC de la barra |
|---|---|---:|---|
| `22_mnq_09_25.Last.txt` | 2025-07-01 10:08:00 | 1.258.222 | 22816.25 / 22934 / 22780 / 22831.5 |
| `22_mnq_09_25.Last.txt` | 2025-07-15 13:52:00 | 1.451.062 | 22862 / 23222.75 / 22805 / 23159.5 |
| `24_mnq_03_26.Last.txt` | 2026-01-27 03:44:00 | 1.534.923 | 25567.75 / 25977.5 / 25543.25 / 25972.25 |

El OHLC de las tres barras es internamente valido (no dispara la comprobacion de OHLC invalido de la seccion 2); es exclusivamente el campo de volumen el que se sale por completo del rango del resto del dataset. Requiere investigacion de integridad en FASE 0 antes de usarse en cualquier analisis que dependa de volumen. No se ha interpretado como evento de mercado ni como error de datos: queda abierto.

## 5. Conclusion de esta comprobacion

No hay problemas de parseo, columnas, duplicados, desorden temporal ni OHLC invalido en ningun archivo. Los tres hallazgos de las secciones 3 y 4 (patron de solapamiento inconsistente y barras de volumen atipico) son las unicas anomalias estructurales identificadas y deben resolverse o al menos caracterizarse en FASE 0 antes de construir la serie continua o de calcular cualquier feature basada en volumen.

Esta comprobacion es la base empirica que informo la eleccion de frontera del hold-out registrada en `config/holdout.yaml` (frontera contractual limpia = una de las 23 transiciones sin solapamiento).
