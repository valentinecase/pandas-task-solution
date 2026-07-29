import re
import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not isinstance(new_column, str) or not re.fullmatch(r"[a-zA-Z_]+", new_column):
        return pd.DataFrame([])

    for col in df.columns:
        if not isinstance(col, str) or not re.fullmatch(r"[a-zA-Z_]+", col):
            return pd.DataFrame([])

    pattern = r"^\s*([a-zA-Z_]+)\s*([\+\-\*])\s*([a-zA-Z_]+)\s*$"
    match = re.match(pattern, role)
    if not match:
        return pd.DataFrame([])

    col1, operator, col2 = match.groups()

    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])

    result_df = df.copy()

    if operator == '+':
        result_df[new_column] = result_df[col1] + result_df[col2]
    elif operator == '-':
        result_df[new_column] = result_df[col1] - result_df[col2]
    elif operator == '*':
        result_df[new_column] = result_df[col1] * result_df[col2]

    return result_df