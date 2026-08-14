# 0003 — QA: migracion a un version_id determinista respecto del contenido

## Identificacion

- **id:** 0003
- **fecha:** 2026-08-14
- **tipo:** QA
- **hipotesis_o_pregunta:** NA (correccion de gobernanza/reproducibilidad, no contraste de hipotesis)
- **parent_id:** 0002

## Trazabilidad de reproducibilidad

- **dataset_usado:** NA (esta entrada corrige metadatos de identificacion del dataset; no analiza su contenido)
- **dataset_version:** IRIS-MNQ-SRC-20191223_20260731-e382a75ac222
- **code_version:** src/build_dataset_manifest.py
- **seed:** NA
- **config_ref:** config/dataset_manifest.yaml; config/holdout.yaml

## Contenido

### Que se hizo

Se detecto que el esquema previo de `version_id` (`IRIS-MNQ-SRC-<fecha_de_ejecucion>-<hash8>`) dependia de `datetime.now(timezone.utc)`, por lo que regenerar el manifest en una fecha distinta sobre el mismo contenido exacto habria producido un `version_id` diferente, rompiendo la propiedad de que un mismo contenido debe tener una identidad de snapshot estable.

Se corrigio `src/build_dataset_manifest.py` para que `version_id` se derive exclusivamente del contenido: `IRIS-MNQ-SRC-<primer_timestamp:YYYYMMDD>_<ultimo_timestamp:YYYYMMDD>-<12 caracteres de hash_snapshot_sha256>`, sin usar `datetime.now()` en ningun punto de su calculo. `fecha_generacion_utc` se mantiene como metadata de ejecucion independiente, sin participar en `version_id`.

Se regenero `config/dataset_manifest.yaml` con el script corregido (dos veces consecutivas, para verificar determinismo) y se anadio a mano el campo `superseded_version_id` con el identificador anterior, documentando que representa exactamente el mismo contenido.

Se actualizaron todas las referencias a `dataset_version` en `config/holdout.yaml`, `experiments/registro.tsv`, `experiments/log/0001_...md`, `experiments/log/0002_...md` y `reports/00_inventario_estructural_data_source.md`, preservando como registro historico literal el bloque de salida de consola original de 0002 (que imprimio el `version_id` bajo el esquema anterior, correctamente, porque asi ocurrio en ese momento).

### Parametros / configuracion exacta

- Formato aprobado: `IRIS-MNQ-SRC-<global_first:YYYYMMDD>_<global_last:YYYYMMDD>-<combined_hash[:12]>`.
- `global_first`/`global_last`: min/max de `primer_timestamp`/`ultimo_timestamp` de los 27 archivos, tal como estan exportados en `data/00_source/` (zona horaria no verificada, ver CLAUDE.md / IRIS_KNOWLEDGE_SYNTHESIS.md A3/D1).
- `combined_hash`: SHA-256 de la concatenacion ordenada `nombre:sha256` de los 27 archivos (sin cambios respecto de la version anterior del script).

### Resultado

Ejecucion 1:
```
version_id=IRIS-MNQ-SRC-20191223_20260731-e382a75ac222
hash_snapshot_sha256=e382a75ac2222c0391a777d597459fab439e606a545daf73d2da2d512260d32c
```

Ejecucion 2 (inmediatamente despues):
```
version_id=IRIS-MNQ-SRC-20191223_20260731-e382a75ac222
hash_snapshot_sha256=e382a75ac2222c0391a777d597459fab439e606a545daf73d2da2d512260d32c
```

`version_id` identico en ambas ejecuciones; `hash_snapshot_sha256` identico entre ambas ejecuciones y respecto del valor original de 0002; unicamente `fecha_generacion_utc` difirio entre ejecuciones (metadata de ejecucion, como se esperaba). `data/00_source/` verificado sin cambios (`git status` limpio sobre esa carpeta) antes y despues de ambas ejecuciones.

El `version_id` obtenido coincide exactamente con el valor esperado indicado por el usuario antes de ejecutar el script: `IRIS-MNQ-SRC-20191223_20260731-e382a75ac222`.

### Interpretacion

La propiedad buscada queda verificada empiricamente, no solo argumentada: mismo contenido exacto -> mismo `version_id`, con independencia del momento de ejecucion. El identificador anterior (`IRIS-MNQ-SRC-2026-08-14-e382a75a`) no queda huerfano: permanece accesible como `superseded_version_id` en `config/dataset_manifest.yaml`, con nota explicita de que corresponde al mismo `hash_snapshot_sha256`.

### Decision resultante

`IRIS-MNQ-SRC-20191223_20260731-e382a75ac222` queda como `dataset_version` vigente para toda referencia futura (FASE 0 incluida). El hold-out, su frontera, `hash_snapshot_sha256`, todos los hashes por archivo y los hallazgos de QA de 0001/0002 permanecen exactamente iguales; solo cambio el identificador legible del snapshot.

## Clasificacion de repeticion

No aplica: es una correccion de gobernanza sobre el esquema de identificacion, no una repeticion de 0001 ni de 0002. Se relaciona con 0002 via `parent_id` porque corrige el artefacto que 0002 genero.
