"""Genera un manifest reproducible del snapshot de data/00_source/.

data/00_source/ es READ ONLY (CLAUDE.md, regla permanente 1): este script
solo lee esos archivos, nunca los modifica, copia ni reorganiza. La salida
es config/dataset_manifest.yaml, que actua como huella de integridad
versionable del snapshot (nombre, tamano, filas, rango temporal y SHA-256
por archivo, mas un hash combinado y un version_id para todo el snapshot).

version_id es completamente determinista respecto del contenido: se deriva
unicamente del rango de cobertura de los propios datos (primer y ultimo
timestamp del snapshot) y de un hash de contenido, nunca del reloj de
ejecucion. Dos ejecuciones sobre exactamente los mismos 27 archivos producen
siempre el mismo version_id, aunque se ejecuten en dias distintos.

fecha_generacion_utc es metadata de ejecucion independiente (cuando se
genero este manifest concreto, en UTC): no participa en version_id.

Nota sobre zonas horarias: el rango de cobertura usado en version_id
(primer_timestamp/ultimo_timestamp) proviene de los timestamps tal como
estan exportados en data/00_source/, cuya zona horaria aun no esta
verificada (ver CLAUDE.md / IRIS_KNOWLEDGE_SYNTHESIS.md, preguntas A3/D1).
No debe asumirse que ese rango esta en UTC; solo fecha_generacion_utc lo
esta, porque se genera con datetime.now(timezone.utc).

Uso:
    python src/build_dataset_manifest.py
"""

import hashlib
import os
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(REPO_ROOT, "data", "00_source")
OUTPUT_PATH = os.path.join(REPO_ROOT, "config", "dataset_manifest.yaml")


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def first_and_last_timestamp(path):
    with open(path, "r") as fh:
        first_line = fh.readline()
    first_ts = first_line.split(";")[0]
    with open(path, "rb") as fh:
        fh.seek(0, os.SEEK_END)
        size = fh.tell()
        buf = min(size, 4096)
        fh.seek(size - buf)
        tail = fh.read().decode(errors="ignore")
    last_line = tail.strip().splitlines()[-1]
    last_ts = last_line.split(";")[0]
    return first_ts, last_ts


def count_lines(path):
    n = 0
    with open(path, "rb") as fh:
        for _ in fh:
            n += 1
    return n


def fmt_ts(raw):
    date_part, time_part = raw.split(" ")
    return (
        f"{date_part[0:4]}-{date_part[4:6]}-{date_part[6:8]} "
        f"{time_part[0:2]}:{time_part[2:4]}:{time_part[4:6]}"
    )


def main():
    files = sorted(f for f in os.listdir(SOURCE_DIR) if f.endswith(".Last.txt"))
    entries = []
    for name in files:
        path = os.path.join(SOURCE_DIR, name)
        size = os.path.getsize(path)
        rows = count_lines(path)
        first_ts, last_ts = first_and_last_timestamp(path)
        digest = sha256_of_file(path)
        entries.append(
            {
                "nombre": name,
                "bytes": size,
                "filas": rows,
                "primer_timestamp": fmt_ts(first_ts),
                "ultimo_timestamp": fmt_ts(last_ts),
                "sha256": digest,
            }
        )

    total_bytes = sum(e["bytes"] for e in entries)
    total_rows = sum(e["filas"] for e in entries)
    global_first = min(e["primer_timestamp"] for e in entries)
    global_last = max(e["ultimo_timestamp"] for e in entries)

    combined_input = "\n".join(f"{e['nombre']}:{e['sha256']}" for e in entries)
    combined_hash = hashlib.sha256(combined_input.encode()).hexdigest()

    # version_id es puramente funcion del contenido: fecha de cobertura de los
    # propios datos (no del reloj) + 12 caracteres del hash combinado. No usa
    # datetime.now() en absoluto.
    global_first_date = global_first[:10].replace("-", "")
    global_last_date = global_last[:10].replace("-", "")
    version_id = f"IRIS-MNQ-SRC-{global_first_date}_{global_last_date}-{combined_hash[:12]}"

    # now es exclusivamente metadata de ejecucion (fecha_generacion_utc, mas
    # abajo): registra cuando se genero este manifest concreto, y no participa
    # en version_id ni en ningun otro campo derivado del contenido.
    now = datetime.now(timezone.utc)

    # El ultimo contrato por indice de nombre es siempre el contrato vigente
    # (el mas reciente aun no expirado en la fecha del snapshot), y por tanto
    # el unico archivo estructuralmente incompleto en cualquier regeneracion
    # futura de este manifest.
    incomplete_name = files[-1]

    lines = []
    lines.append("# GENERADO AUTOMATICAMENTE por src/build_dataset_manifest.py -- no editar a mano.")
    lines.append("# Manifest reproducible del snapshot de data/00_source/. data/00_source/ es READ ONLY;")
    lines.append("# este archivo es la huella de integridad de ese snapshot, no una copia de los datos.")
    lines.append("")
    lines.append("snapshot:")
    lines.append(f"  version_id: {version_id}")
    lines.append(
        "  version_id_esquema: \"IRIS-MNQ-SRC-<primer_timestamp:YYYYMMDD>_"
        "<ultimo_timestamp:YYYYMMDD>-<12 caracteres de hash_snapshot_sha256>\""
    )
    lines.append(
        "  version_id_nota: \"Determinista respecto del contenido: no usa "
        "datetime.now() en ningun punto. Dos ejecuciones sobre el mismo contenido "
        "exacto de data/00_source/ producen siempre el mismo version_id, aunque "
        "fecha_generacion_utc difiera entre ejecuciones. El rango de fechas viene "
        "de los timestamps tal como estan exportados en los datos (zona horaria "
        "aun no verificada, ver CLAUDE.md / IRIS_KNOWLEDGE_SYNTHESIS.md A3/D1); "
        "fecha_generacion_utc si es UTC real porque se genera con "
        "datetime.now(timezone.utc).\""
    )
    lines.append(f"  fecha_generacion_utc: \"{now.strftime('%Y-%m-%dT%H:%M:%SZ')}\"")
    lines.append(f"  n_archivos: {len(entries)}")
    lines.append(f"  filas_totales: {total_rows}")
    lines.append(f"  bytes_totales: {total_bytes}")
    lines.append("  cobertura_calendario:")
    lines.append(f"    primer_timestamp: \"{global_first}\"")
    lines.append(f"    ultimo_timestamp: \"{global_last}\"")
    lines.append(f"  hash_snapshot_sha256: {combined_hash}")
    lines.append("  contrato_incompleto:")
    lines.append(f"    archivo: {incomplete_name}")
    lines.append(
        "    motivo: \"Contrato vigente aun no expirado en la fecha del snapshot; "
        "el archivo crecera en una futura exportacion.\""
    )
    lines.append(
        "  nota_versionado: \"Una exportacion futura con mas datos constituye una "
        "nueva version del snapshot (nuevo version_id) y no sobrescribe conceptualmente "
        "esta version.\""
    )
    lines.append("")
    lines.append("archivos:")
    for e in entries:
        lines.append(f"  - nombre: {e['nombre']}")
        lines.append(f"    bytes: {e['bytes']}")
        lines.append(f"    filas: {e['filas']}")
        lines.append(f"    primer_timestamp: \"{e['primer_timestamp']}\"")
        lines.append(f"    ultimo_timestamp: \"{e['ultimo_timestamp']}\"")
        lines.append(f"    sha256: {e['sha256']}")
        lines.append(f"    completo: {'false' if e['nombre'] == incomplete_name else 'true'}")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"version_id={version_id}")
    print(f"hash_snapshot_sha256={combined_hash}")
    print(f"primer_timestamp={global_first}")
    print(f"ultimo_timestamp={global_last}")
    print(f"filas_totales={total_rows}")
    print(f"bytes_totales={total_bytes}")
    print(f"salida={OUTPUT_PATH}")


if __name__ == "__main__":
    main()
