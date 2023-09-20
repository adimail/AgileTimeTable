import pandas as pd

data = ['a1', 'a2', 'a3']

days = ['mon', 'tue', 'wed', 'thu', 'fri']

df = pd.DataFrame(columns=data, index=days)

# The dictionary you want to assign to the cell
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Make sure the column dtype is 'object' to allow storing dictionaries
# df['a1'] = df['a1'].astype(object)

# Assign the dictionary to the specified cell
df.at['mon', 'a1'] = my_dict

# Display the updated DataFrame
print(df)
