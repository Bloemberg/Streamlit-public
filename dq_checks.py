import pandas as pd

def run_dq_checks(df: pd.DataFrame) -> pd.DataFrame:
    result = []

    for column in df.columns:
        col_data = df[column]

        completeness = col_data.notna().mean()
        uniqueness = col_data.nunique() / len(col_data)
        type_inference = col_data.map(type).mode()[0].__name__

        result.append({
            "Kolom": column,
            "Compleetheid (%)": round(completeness * 100, 2),
            "Uniciteit (%)": round(uniqueness * 100, 2),
            "Dominant datatype": type_inference,
        })

    return pd.DataFrame(result)
