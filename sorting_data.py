import pandas as pd
people = {
    'first': ['Corey', 'Jane', 'John', 'Adam'],
    'last': ['Schafer', 'Doe', 'Doe', 'Doe'],
    'email': ['Corey@gmail.com', 'jane@email.com', 'john@tmail.com', 'a@email.com']
}
df = pd.DataFrame(people)
df.sort_values(by='last', inplace=True, ascending=False)

# to sort on more than one pass a list of columns to sort by
df.sort_values(by=['last', 'first'], inplace=True, ascending=[False, True])
# to sort indexes after sorting your rows
# df.sort_index()

# print(df['last'].sort_values())

df = pd.read_csv("developer_survey_2020/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv", index_col='Column')
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
# df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
# df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})

# sort by country example
df.sort_values(by=['Country', 'ConvertedComp'], inplace=True, ascending=[True, False])
# print(df[['Country', 'ConvertedComp']].head(50))
# easiest way to grab 10 largest of something
# print(df.nlargest(10, columns='ConvertedComp'))
smallest = df.nsmallest(10, 'ConvertedComp')
print(smallest)