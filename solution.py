import re
import pandas as pd

def add_virtual_column(df, role, new_column):
    if not isinstance(new_column, str) or not new_column.replace('_', '').isalpha():
        return pd.DataFrame()
    
    for col in df.columns:
        if not isinstance(col, str) or not str(col).replace('_', '').isalpha():
            return pd.DataFrame()

    match = re.match(r"^([a-zA-Z_]+)\s*([\+\-\*])\s*([a-zA-Z_]+)$", role.strip())
    if not match:
        return pd.DataFrame()

    col1, op, col2 = match.groups()

    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame()

    res_df = df.copy()

    if op == '+':
        res_df[new_column] = res_df[col1] + res_df[col2]
    elif op == '-':
        res_df[new_column] = res_df[col1] - res_df[col2]
    elif op == '*':
        res_df[new_column] = res_df[col1] * res_df[col2]

    return res_df
