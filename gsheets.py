import gspread
from google.oauth2 import service_account
import pandas as pd

# Load credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file('client_secret_292696265060-fsaoa0hsc74c168cs8o4ehnrm74n20gn.apps.googleusercontent.com.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

# Authorize and access the Google Sheet
gc = gspread.service_account(filename='client_secret_292696265060-fsaoa0hsc74c168cs8o4ehnrm74n20gn.apps.googleusercontent.com.json')
sheet = gc.open('subjects').sheet1  # Replace with your sheet's name

# Read data from the Google Sheet into a pandas DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
