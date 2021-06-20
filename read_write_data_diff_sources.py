import pandas as pd
df = pd.read_csv("developer_survey_2020/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("developer_survey_2020/survey_results_schema.csv", index_col='Column')
# dataframe is just rows and columns of data
pd.set_option("display.max_columns", 61)
pd.set_option("display.max_rows", 61)
filt = df['Country'] == 'India'
india_df = df.loc[filt]
# export to csv method
# india_df.to_csv('developer_survey_2020/modified.csv')
# file that is delimited by tabs
# india_df.to_csv('developer_survey_2020/modified.tsv', sep='\t')

# to read tsv files just add the sep='\t' to read_csv

india_df.to_excel('developer_survey_2020/modified.xlsx')

# test = pd.read_excel('developer_survey_2020/modified.xlsx', index_col='Respondent')
# print(test)

# json format can change orient to make json more listlike rather than dictionary like
india_df.to_json('developer_survey_2020/modified.json', orient='records', lines=True)
# if you use those arguments making a json file you'll need them when you make it
# test = pd.read_json('developer_survey_2020/modified.json', orient='records', lines=True)
# print(test)
# the code below assumes you have SQLalchemy and psycopg2-binary
# from sqlachemy import create_engine
# import psycopg2
# next part assumes you created an engine and have credentials
# engine = create_engine('postrgresql://User:password@localhost:5432/sample_db') # for production code use config files to hide your personal data
# india_df.to_sql('sample_table', engine)
# to add over a table just add if_exists parameter and set it equal to 'replace' or something else

# now to pull data from database
# sql_df = pd.read_sql('sample_table', engine, index_col='Respondent')
# sql_df = pd.read_sql_query('SELECT * FROM sample_table', engine, index_col='Respondent')
# posts_df = pd.read_json('url for project')
