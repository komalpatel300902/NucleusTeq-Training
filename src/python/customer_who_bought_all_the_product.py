import pandas as pd
def lenght_of_product_key(rows):
    rows["lenght"] = len(rows.drop_duplicates(subset = ["product_key"]))
    return rows
def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    length = len(product)
    group_df = customer.groupby(by = "customer_id")
    output = group_df.apply(lenght_of_product_key)
    output = output.drop_duplicates(subset = ["customer_id"])
    output = output[output["lenght"] == length]
    return output[["customer_id"]]    