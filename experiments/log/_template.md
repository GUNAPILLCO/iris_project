# Plantilla de detalle de intento

Copiar este archivo a `NNNN_slug-descriptivo.md` (mismo `id` que la fila correspondiente en `experiments/registro.tsv`) y completar todos los campos antes de ejecutar el intento, no despues.

## Identificacion

- **id:**
- **fecha:**
- **tipo:** `QA` | `exploracion_autorizada` | `hipotesis_empirica` | `tuning` | `otro`
- **hipotesis_o_pregunta:** (referencia a la pregunta canonica de `IRIS_KNOWLEDGE_SYNTHESIS.md`, p. ej. `B2`, `C1`, o `NA` si es QA)
- **parent_id:** (id del intento del que este se deriva directamente, o `NA`)

## Trazabilidad de reproducibilidad

- **dataset_usado:** `investigacion` | `hold-out` (el hold-out solo con autorizacion explicita registrada aqui)
- **dataset_version:** (`version_id` de `config/dataset_manifest.yaml` vigente en el momento del intento)
- **code_version:** (commit/hash o ruta+version del script usado; `pre-src` si aun no hay codigo)
- **seed:** (semilla de aleatoriedad usada, o `NA` si no aplica)
- **config_ref:** (ruta a la configuracion congelada usada, si existe)

## Contenido

### Que se hizo

### Parametros / configuracion exacta

### Resultado

### Interpretacion

### Decision resultante

## Clasificacion de repeticion

Este intento **solo** puede marcarse como `repeticion` de otro `id` en `registro.tsv` si coinciden simultaneamente:

1. la misma hipotesis o pregunta,
2. la misma configuracion/parametros,
3. el mismo `dataset_version`,
4. el mismo `code_version`.

Si cualquiera de los cuatro cambia de forma material, este intento es un **experimento nuevo** (nuevo `id`) aunque este relacionado con uno anterior via `parent_id`. Si se clasifica como `repeticion` pese a una diferencia menor no material, debe justificarse explicitamente aqui por que esa diferencia no se considera material.

**Justificacion de la clasificacion elegida:**
