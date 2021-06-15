import pandas as pd
df = pd.read_csv("developer_survey_2020/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv", index_col='Column')
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
# pd.set_option("display.max_colwidth", None)
# find unique value results in a dataset
# print(df["Hobbyist"].value_counts())
print("---------------------------")
# using loc results in truncated result add the column option as well with a comma to get full question
# print(schema_df.loc['MiscTechDesireNextYear', 'QuestionText'])
schema_df.sort_index(inplace=True, ascending=False)
# print(schema_df.loc['ConvertedComp', 'QuestionText'])
# countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
# filt = df['Country'].isin(countries)
# print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
new_filt = (df['Age'] < 21) & (df['Country'].str.contains('United States'))
# print(df.loc[filt, 'LanguageWorkedWith '])
# print(df.loc[new_filt, ['LanguageWorkedWith', 'ConvertedComp']])
