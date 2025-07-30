import pandas as pd

def run_dq_checks(df: pd.DataFrame) -> pd.DataFrame:
    result = []

    for column in df.columns:
        col_data = df[column]

        completeness = col_data.notna().mean()
        uniqueness = col_data.nunique() / len(col_data)
        type_inference = col_data.map(type).mode()[0].__name__

        # Voorbeeld extra dimensies
        plausibility = check_plausibility(col_data)
        validity = check_validity(col_data)
        consistency = check_consistency(df, column)
        understandability = check_understandability(col_data)

        result.append({
            "Kolom": column,
            "Compleetheid (%)": round(completeness * 100, 2),
            "Uniciteit (%)": round(uniqueness * 100, 2),
            "Dominant datatype": type_inference,
            "Validiteit (%)": validity,
            "Plausibiliteit (%)": plausibility,
            "Consistentie (%)": consistency,
            "Begrijpelijkheid (%)": understandability
        })

    return pd.DataFrame(result)

def check_validity(series):
    # Voorbeeld: strings zonder rare tekens
    if series.dtype == object:
        valid_pct = series.dropna().apply(lambda x: isinstance(x, str) and len(x.strip()) > 0).mean()
        return round(valid_pct * 100, 2)
    return "n.v.t."

def check_plausibility(series):
    # Voorbeeld: leeftijd tussen 0-120 als plausibel
    if pd.api.types.is_numeric_dtype(series):
        plausible_pct = series.dropna().between(0, 120).mean()
        return round(plausible_pct * 100, 2)
    return "n.v.t."

def check_consistency(df, column):
    # Placeholder – afhankelijk van samenhang tussen kolommen
    return "n.v.t."

def check_understandability(series):
    # Simpel voorbeeld: lange strings of veel unieke waarden = minder begrijpelijk
    if series.dtype == object:
        unique_ratio = series.nunique() / len(series)
        if unique_ratio > 0.5:
            return 40.0
        elif unique_ratio > 0.2:
            return 70.0
        else:
            return 90.0
    return "n.v.t."
