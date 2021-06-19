import pandas as pd
df = pd.read_csv("developer_survey_2020/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv", index_col='Column')
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
# print(df['Hobbyist'].value_counts(normalize=True))
# print(df['Country'].value_counts())
country_grp = df.groupby(['Country'])
# to get a dataframe with individual group
# print(country_grp.get_group('United States'))
# same thing can be done by using a filter
# print(df.loc[filt]['Employment'].value_counts())
# print(country_grp.get_group('United States')['Employment'].value_counts())
# print(country_grp.get_group('Uruguay')['ConvertedComp'].median())
# print(country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada'])
# how many people in a specific country know how to use python
filt = df['Country'] == 'India'
# print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum())
# print(country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))
# what percentage of people for each country know how to use python
# 1) get total # of respondents from each country
country_respondents = df['Country'].value_counts()
# print(country_respondents)
# 2) grab total # of people who know python per country
uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
# combine them into a df
python_df = pd.concat([country_respondents, uses_python], axis='columns', sort=False)
python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'Uses Python'}, inplace=True)
# create a 3rd column to show percentage
python_df['PctKnowsPython'] = (python_df['Uses Python'] / python_df['NumRespondents']) * 100
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
print(python_df.loc['Japan'])