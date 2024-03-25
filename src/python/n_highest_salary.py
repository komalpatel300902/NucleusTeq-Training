import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    a = employee["salary"].drop_duplicates()
    a = a.sort_values(ascending = False)
    length = len(a)
    result_data = None
    if length >= N and N > 0:
        
        result_data = a.iat[N-1]
    df = pd.DataFrame({
        f"getNthHighestSalary({N})":[result_data]
    })
    return df