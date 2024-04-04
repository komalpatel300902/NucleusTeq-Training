import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = company[company["name"] == "RED"]
    df_merge = pd.merge(sales_person , orders , on = "sales_id" , how = "inner")
    dfm = pd.merge(df_merge, df, on = "com_id", how = "inner" )
    output = sales_person[~sales_person["name"].isin(dfm["name_x"])]
    result = output[["name"]]
    return result
    