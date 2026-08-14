# 0002 — QA: congelacion del snapshot y bloqueo de la frontera de hold-out

## Identificacion

- **id:** 0002
- **fecha:** 2026-08-13
- **tipo:** QA
- **hipotesis_o_pregunta:** NA (gobernanza de datos, no contraste de hipotesis)
- **parent_id:** 0001

## Trazabilidad de reproducibilidad

- **dataset_usado:** NA (esta entrada genera metadatos sobre el dataset, no consume ni analiza su contenido mas alla de lo ya hecho en 0001)
- **dataset_version:** IRIS-MNQ-SRC-20191223_20260731-e382a75ac222 (migrado el 2026-08-14 desde IRIS-MNQ-SRC-2026-08-14-e382a75a; mismo contenido, mismo hash_snapshot_sha256 -- ver 0003)
- **code_version:** src/build_dataset_manifest.py
- **seed:** NA
- **config_ref:** config/dataset_manifest.yaml; config/holdout.yaml

## Contenido

### Que se hizo

1. Se escribio y ejecuto `src/build_dataset_manifest.py` (solo dependencias de la libreria estandar de Python) sobre `data/00_source/`, en modo lectura exclusivamente, para generar `config/dataset_manifest.yaml`: nombre, bytes, filas, primer/ultimo timestamp y SHA-256 por cada uno de los 27 archivos, mas un hash combinado del snapshot completo y un `version_id`.
2. Se marco explicitamente `26_mnq_09_26.Last.txt` como `completo: false` dentro del manifest.
3. Se escribio `config/holdout.yaml` con la frontera de hold-out aprobada por el usuario (Alternativa B: `2025-06-23 00:00:00` -> `2026-07-31 20:10:00`), estado `LOCKED`, motivo de eleccion (sin afirmar regimenes ni potencia estadistica, ninguna de las dos medida), y la lista de prohibiciones de acceso derivadas de la regla permanente 5 de `CLAUDE.md`.

### Parametros / configuracion exacta

- Script: `src/build_dataset_manifest.py` (hash de cada archivo con SHA-256 por bloques de 1 MiB; timestamps leidos de la primera y ultima linea de cada archivo; hash combinado = SHA-256 de la concatenacion ordenada `nombre:sha256` de los 27 archivos).
- Frontera de hold-out: inicio `2025-06-23 00:00:00`, fin = ultimo timestamp del snapshot congelado.

### Resultado

```
version_id=IRIS-MNQ-SRC-2026-08-14-e382a75a
hash_snapshot_sha256=e382a75ac2222c0391a777d597459fab439e606a545daf73d2da2d512260d32c
primer_timestamp=2019-12-23 03:01:00
ultimo_timestamp=2026-07-31 20:10:00
filas_totales=2329783
bytes_totales=122523200
```

*(Salida literal de la ejecucion original del 2026-08-13, bajo el esquema de version_id previo a la migracion de 0003. No se reescribe con el id nuevo porque es un registro historico de lo que el script imprimio en ese momento; el `dataset_version` vigente a efectos de referencia esta en la seccion "Trazabilidad de reproducibilidad" arriba.)*

`data/00_source/` verificado sin cambios tras la ejecucion (`git status` limpio sobre esa carpeta).

### Interpretacion

El snapshot actual queda identificado de forma unica y verificable (`version_id` + SHA-256 por archivo). Cualquier reexportacion futura de `data/00_source/` producira un `version_id` distinto y no debe interpretarse como la misma version de datos; todo intento futuro debe declarar contra que `dataset_version` se ejecuto.

### Decision resultante

El hold-out queda `LOCKED`: a partir de este momento no debe inspeccionarse salvo autorizacion explicita. Esto no implica que el periodo no tuviera exposicion previa -- el escaneo estructural de 0001 (ejecutado antes de que existiera esta frontera) cubrio los 27 archivos, incluidos los 5 que aqui quedan reservados como hold-out. Ver el detalle de esa exposicion, clasificada como QA pre-lock, en `experiments/log/0001_qa_inventario_estructural_data_source.md` y en `config/holdout.yaml` (seccion `exposicion_pre_lock`). La fase de investigacion queda habilitada para operar sobre el resto del snapshot (`dataset_usado: investigacion`), identificado por el mismo `dataset_version`.

## Clasificacion de repeticion

No aplica: no repite ningun intento anterior. Se relaciona con 0001 via `parent_id` porque formaliza y congela el snapshot sobre el que se ejecuto esa comprobacion, pero no es la misma hipotesis ni la misma accion.
