import pandas as pd
def average(rows):
    rows["average_years"] = round(rows["experience_years"].mean(),2)
    return rows.head(1)
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(project , employee , how = "inner", on = "employee_id")
    group_df = merged_df.groupby(by = ["project_id"])
    output = group_df.apply(average)
    return output[["project_id","average_years"]]