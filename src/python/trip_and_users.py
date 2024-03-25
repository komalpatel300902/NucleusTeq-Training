import pandas as pd
def cancellation_rate(rows):
    rows["cancelation_rate"] = round((rows["status"].count() - rows["status"].value_counts().get("completed",0))/rows["status"].count(),2)
    return rows.head(1)
def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    df =pd.DataFrame({"Day":[],
    "Cancellation Rate":[]})
    if trips.empty or users.empty:
        return df
    ban_user_id = users[users["banned"] == "Yes"]["users_id"]
    refined_df = trips[ ~trips["client_id"].isin(ban_user_id)]
    refined_df = refined_df[ ~refined_df["driver_id"].isin(ban_user_id)]
    refined_df = refined_df[refined_df["request_at"] >= "2013-10-01"]
    refined_df = refined_df[refined_df["request_at"] <= "2013-10-03"]
    if not refined_df.empty:
        group_data = refined_df.groupby(by = ["request_at"])
        output_df = group_data.apply(cancellation_rate)
        df1 = output_df[["request_at","cancelation_rate"]].rename(columns = {"request_at":"Day","cancelation_rate":"Cancellation Rate"})
        df =  df1
        # df1= output_df.apply(lambda x : x.iloc[0])
    return df
