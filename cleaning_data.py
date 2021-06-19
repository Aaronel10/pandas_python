import pandas as pd
import numpy as np
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['Corey@gmail.com', 'jane@email.com', 'john@tmail.com', None, np.nan, 'anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
# df = pd.DataFrame(people)
# drop custom messages and replace them with NaN
# df.replace('NA', np.nan, inplace=True)
# df.replace('Missing', np.nan, inplace=True)
# df = df.dropna(axis='columns', how='all') # axis can be index or columns, how= is the criteria to drop something can be any or all
# df.dropna(axis='index', how='all', subset=['last', 'email'], inplace=True)
# print(df.isna())
# change nas to some value
# df.fillna(0, inplace=True)
#print(df)

# casting data types
# print(df.dtypes)
# df['age'] = df['age'].astype(float)
# print(df['age'].mean())
df = pd.read_csv("developer_survey_2020/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv", index_col='Column')
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
# print(df['YearsCode'].head(10))
# print(df['YearsCode'].value_counts())
# print(df['YearsCode'].unique())
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)
df['YearsCode'] = df['YearsCode'].astype(float)
print(df['YearsCode'].median())
