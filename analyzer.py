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


def basic_stats(data, column):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except (ValueError, KeyError):
            continue
    if not values:
        return {}
    values.sort()
    n = len(values)
    return {
        "count": n,
        "mean": sum(values) / n,
        "min": values[0],
        "max": values[-1],
        "median": values[n // 2] if n % 2 else (values[n//2 - 1] + values[n//2]) / 2
    }


def filter_rows(data, column, op, value):
    results = []
    for row in data:
        cell = row.get(column, "")
        try:
            cell_val = float(cell)
            value_f = float(value)
            if op == ">" and cell_val > value_f: results.append(row)
            elif op == "<" and cell_val < value_f: results.append(row)
            elif op == ">=" and cell_val >= value_f: results.append(row)
            elif op == "<=" and cell_val <= value_f: results.append(row)
            elif op == "==" and cell_val == value_f: results.append(row)
        except ValueError:
            if op == "==" and cell == value: results.append(row)
    return results


def sort_data(data, column, reverse=False):
    def key_fn(row):
        val = row.get(column, "")
        try:
            return (0, float(val))
        except ValueError:
            return (1, val)
    return sorted(data, key=key_fn, reverse=reverse)
