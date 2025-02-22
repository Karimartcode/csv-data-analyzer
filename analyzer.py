import csv


def load_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def display_head(data, n=5):
    for row in data[:n]:
        print(row)


def get_columns(data):
    if not data:
        return []
    return list(data[0].keys())


def get_info(data):
    cols = get_columns(data)
    return {
        "rows": len(data),
        "columns": len(cols),
        "column_names": cols
    }
