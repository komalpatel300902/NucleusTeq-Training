import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    a = employee["salary"].drop_duplicates()
    a = a.sort_values(ascending = False)
    result_data = None
    length = len(a)
    if  length >=2:
        result_data = a.iloc[1]
    

    df = pd.DataFrame({
        "SecondHighestSalary":[result_data]
    })
    return df