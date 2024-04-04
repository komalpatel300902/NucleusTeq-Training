import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # step 1: saperate data which is before 2019-08-16
    df = products[products["change_date"] <= "2019-08-16"]
    # step 2: fetch distinct id
    ids = products["product_id"].unique()
    id_df = pd.DataFrame(ids, columns = ["product_id"])
    id_df.reset_index(drop = True , inplace = True)
    # step 3 : make group based on product id
    group_data = df.groupby(by = ["product_id"],axis = 0)
    #step 4 :filter the group and get max of each id
    output = group_data.apply(lambda x : x[x["change_date"] == x["change_date"].max()])
    output.reset_index(drop = True , inplace = True)
    # step 5: merge the ids and output (how : left join)
    result = pd.merge(id_df , output, left_on = "product_id", right_on = "product_id",how = "left")
    result.fillna(10,inplace = True)
    main_output = result[["product_id","new_price"]]
    main_output.rename(columns = {"new_price" : "price"},inplace = True)
    return main_output