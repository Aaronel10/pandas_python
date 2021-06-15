import pandas as pd
people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['corey@gmail.com', 'jane@email.com', 'john@tmail.com']
}
df = pd.DataFrame(people)
# print(df["email"])

# access multiple columns
# print(df[['last', 'email']])

# grab columns
# print(df.columns)

# to get rows use loc or iloc , i in iloc is for integer
print(df.iloc[[0, 1], 2])
# recieves two arguments first is for rows second is for columns
print("-----------------------")

print(df.loc[[0, 2], ['email', 'last']])


