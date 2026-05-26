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


def group_by(data, column):
    groups = {}
    for row in data:
        key = row.get(column, "")
        if key not in groups:
            groups[key] = []
        groups[key].append(row)
    return groups


def aggregate(groups, agg_column, func="count"):
    results = {}
    for key, rows in groups.items():
        if func == "count":
            results[key] = len(rows)
        else:
            values = []
            for r in rows:
                try:
                    values.append(float(r[agg_column]))
                except (ValueError, KeyError):
                    continue
            if not values:
                results[key] = 0
            elif func == "sum":
                results[key] = sum(values)
            elif func == "avg":
                results[key] = sum(values) / len(values)
            elif func == "min":
                results[key] = min(values)
            elif func == "max":
                results[key] = max(values)
    return results
