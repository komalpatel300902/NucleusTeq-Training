import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_dataset = pd.merge(employee,department,how = "inner",left_on = "departmentId",right_on = "id")
    group_data = merged_dataset.groupby(by = "departmentId" , sort = False)
    output = group_data.apply(lambda x : x[x["salary"] == x["salary"].max()])
    df = pd.DataFrame({})
    df[["Department","Employee","Salary"]] =  output.sort_values(by = "id_x")[["name_y","name_x","salary"]]
    return df