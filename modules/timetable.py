import pandas as pd

class TimetableLoader:
    def __init__(self):
        self.file_path = 'timetable_df.csv'
        self.timetable_df = None
        self.timetable_df = pd.read_csv(self.file_path)
        self.timetable_df[['s-break', 'l-break']] = "Recess"

    def print_timetable(self):
        if self.timetable_df is not None:
            print(self.timetable_df)
        else:
            print("Timetable not loaded yet.")

divA_semII = TimetableLoader()
divA_semII.print_timetable()