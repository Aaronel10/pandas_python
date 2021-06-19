import pandas as pd
people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['Corey@gmail.com', 'jane@email.com', 'john@tmail.com']
}
df = pd.DataFrame(people)
# combine first and last columns into just name
df['full_name'] = df['first'] + ' ' + df['last']
df.drop(columns=['first', 'last'], inplace=True)

# if you wanted to recover the 2 columns
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
df.drop(columns='full_name', inplace=True)

# adding a single row of data
df = df.append({'first': 'Tony', 'last': 'Guzman', 'email': 'tony@gmail.com'}, ignore_index=True)

new_people = {
    'first': ['Steve', 'Jane'],
    'last': ['Buschemi', 'Mary'],
    'email': ['notagremlin@gmail.com', 'legalincanada@gmail.com']
}
df_2 = pd.DataFrame(new_people)

df = df.append(df_2, ignore_index=True)
df.drop(index=5, inplace=True)
filt = df['last'] == 'Doe'
df.drop(index=df[filt].index , inplace=True)
print(df)
