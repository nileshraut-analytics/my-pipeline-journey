import pandas as pd

jan_df = pd.read_csv("sales_january.csv")
feb_df = pd.read_csv("sales_february.csv")
mar_df = pd.read_csv("sales_march.csv")

final_df = pd.concat([jan_df, feb_df, mar_df]).reset_index(drop=True)

print(final_df)
print(final_df.shape)
