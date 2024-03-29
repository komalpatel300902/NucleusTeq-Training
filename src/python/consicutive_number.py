import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs.copy()
    df["num1"] = df["num"].shift(-1)
    df["num2"] = df["num"].shift(-2)
    df = df[df["num"] == df["num1"]]
    df = df[df["num1"] == df["num2"]]
    result = pd.DataFrame({"ConsecutiveNums":[]})
    if not df.empty:
        result["ConsecutiveNums"] = df["num"].unique()
    return result[["ConsecutiveNums"]]