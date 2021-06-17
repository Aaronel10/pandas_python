import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['Corey@gmail.com', 'jane@email.com', 'john@tmail.com']
}
df = pd.DataFrame(people)
df.columns = ['first name', 'last name', 'email']
# you can also modify small specific things using list comprehensions
df.columns = [x.lower() for x in df.columns]
# print(df.columns)
# you can also remove spaces as follows:
df.columns = df.columns.str.replace(' ', '_')
df.rename(columns={'first_name': 'first',
                   'last_name': 'last'}, inplace=True)
# change a specific row
df.loc[2] = ['John', 'Smith', 'johnsmith@umail.com']
df.loc[2, ['last', 'email']] = ['Doe', 'john@tmail.com']
df.loc[2, 'last'] = 'Smith'
filt = (df['email'] == 'john@tmail.com')
df['email'] = df['email'].str.lower()


# print(df)
# 4 common methods to modify data: apply, map, applymap, replace
# apply is used for calling a function on our values , works on dataframes or a series obj

def update_email(email):
    return email.upper()

df['email'] = df['email'].apply(update_email)
df['email'] = df['email'].apply(lambda x: x.lower())

# print(df.apply(len, axis='columns'))
# print(df.apply(pd.Series.min))
# apply is for series apply map is for data frames
# print(df.applymap(len))
# print(df.applymap(str.lower))

print(df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'}))

