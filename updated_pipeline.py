import pandas as pd
import glob

files = glob.glob("sales_*.csv")
all_dfs = []
for file in files:
    df = pd.read_csv(file)
    all_dfs.append(df)

final_df = pd.concat(all_dfs).reset_index(drop=True)

print(final_df)
print(final_df.shape)


