import pandas as pd
df = pd.read_csv("developer_survey_2020/survey_results_public.csv")
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv")
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
# find unique value results in a dataset
# print(df["Hobbyist"].value_counts())
print("---------------------------")
print(df.loc[0:2, "Hobbyist":"Employment"])

