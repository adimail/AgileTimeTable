import pandas as pd

file_path = 'timetable_df.xlsx'

timetable_df = pd.read_excel(file_path)
timetable_df[['s-break','l-break']]="Recess"
print(timetable_df)