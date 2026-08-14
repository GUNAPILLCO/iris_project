# data/01_processed/

Destino de todo dato derivado o procesado a partir de `data/00_source/` (serie continua, datasets intermedios, etc.).

Reglas aplicables (CLAUDE.md):

- `data/00_source/` nunca se modifica, copia ni reorganiza para producir estos archivos; solo se lee.
- Todo artefacto que se escriba aqui debe ser reproducible y trazable: el script y la configuracion que lo generan deben conservarse (en `src/` y `config/`) junto con metadatos suficientes para regenerarlo, incluyendo el `dataset_version` de `config/dataset_manifest.yaml` usado como entrada.
- Ningun archivo aqui debe derivarse del hold-out definido en `config/holdout.yaml` salvo autorizacion explicita registrada en `experiments/registro.tsv`.
- Si los artefactos generados aqui llegan a ser voluminosos, debe proponerse un cambio de `.gitignore` al usuario antes de aplicarlo (no hacerlo de forma silenciosa).

Vacio por ahora: FASE 0 aun no ha comenzado.
