import pandas as pd

def run_dq_checks(df: pd.DataFrame) -> pd.DataFrame:
    result = []

    for column in df.columns:
        col_data = df[column]

        completeness = col_data.notna().mean()
        uniqueness = col_data.nunique() / len(col_data)
        type_inference = col_data.map(type).mode()[0].__name__

        validity = check_validity(col_data)
        plausibility = check_plausibility(col_data)
        consistency = check_consistency(df, column)
        understandability = check_understandability(col_data)
        accuracy = check_accuracy(col_data)
        actuality = check_actuality(col_data)
        traceability = check_traceability(col_data)
        precision = check_precision(col_data)

        result.append({
            "Kolom": column,
            "Compleetheid (%)": round(completeness * 100, 2),
            "Uniciteit (%)": round(uniqueness * 100, 2),
            "Dominant datatype": type_inference,
            "Validiteit (%)": validity,
            "Plausibiliteit (%)": plausibility,
            "Consistentie (%)": consistency,
            "Begrijpelijkheid (%)": understandability,
            "Juistheid (%)": accuracy,
            "Actualiteit (%)": actuality,
            "Traceerbaarheid (%)": traceability,
            "Precisie (%)": precision
        })

    return pd.DataFrame(result)

def check_validity(series):
    if series.dtype == object:
        valid_pct = series.dropna().apply(lambda x: isinstance(x, str) and len(x.strip()) > 0).mean()
        return round(valid_pct * 100, 2)
    return "n.v.t."

def check_plausibility(series):
    if pd.api.types.is_numeric_dtype(series):
        plausible_pct = series.dropna().between(0, 120).mean()
        return round(plausible_pct * 100, 2)
    return "n.v.t."

def check_consistency(df, column):
    return "n.v.t."

def check_understandability(series):
    if series.dtype == object:
        unique_ratio = series.nunique() / len(series)
        if unique_ratio > 0.5:
            return 40.0
        elif unique_ratio > 0.2:
            return 70.0
        else:
            return 90.0
    return "n.v.t."

def check_accuracy(series):
    return 100.0  # demo default

def check_actuality(series):
    if pd.api.types.is_datetime64_any_dtype(series):
        max_age = (pd.Timestamp.now() - series.dropna()).dt.days.max()
        if max_age < 30:
            return 100.0
        elif max_age < 90:
            return 70.0
        else:
            return 40.0
    return "n.v.t."

def check_traceability(series):
    name = series.name.lower()
    if any(key in name for key in ["bron", "source", "id", "timestamp"]):
        return 100.0
    return "n.v.t."

def check_precision(series):
    if pd.api.types.is_numeric_dtype(series):
        decimals = series.dropna().astype(str).apply(lambda x: len(x.split(".")[1]) if "." in x else 0)
        if decimals.mean() >= 2:
            return 100.0
        else:
            return 50.0
    elif series.dtype == object:
        avg_len = series.dropna().astype(str).apply(len).mean()
        return min(round(avg_len / 10 * 100, 2), 100.0)
    return "n.v.t."
