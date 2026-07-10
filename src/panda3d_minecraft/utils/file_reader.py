from pathlib import Path


def read_map(file_path: Path) -> list[list[int]]:
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el mapa: {file_path}")

    map_data: list[list[int]] = []

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            clean_line = line.strip()

            if not clean_line:
                continue

            try:
                row = [int(value) for value in clean_line.split()]
            except ValueError as error:
                raise ValueError(
                    f"Valor inválido en la línea {line_number}: {clean_line}"
                ) from error

            map_data.append(row)

    if not map_data:
        raise ValueError("El archivo del mapa está vacío.")

    expected_columns = len(map_data[0])

    for row_number, row in enumerate(map_data, start=1):
        if len(row) != expected_columns:
            raise ValueError(
                f"La fila {row_number} tiene {len(row)} columnas; "
                f"se esperaban {expected_columns}."
            )

    return map_data
