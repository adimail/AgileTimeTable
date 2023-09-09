import numpy as np
import datetime
import pandas as pd
import division

class TimetableLoader_fe:
    def __init__(self, term="even", division="non-IT"):
        # Create an empty NumPy array to represent the timetable
        self.term = term
        self.division = division
        self.days = ['mon', 'tue', 'wed', 'thu', 'fri']
        self.time_slots = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'C30']
        self.timetable = np.empty((len(self.days), (len(self.time_slots))), dtype=object)

    def assign_lecture(self, row, col, lecture):
        self.timetable[row, col] = lecture

    def print_timetable(self):
        # Iterate over rows and columns to print only the subject name
        for i, day in enumerate(self.days):
            for j, time_slot in enumerate(self.time_slots):
                lecture = self.timetable[i, j]
                if lecture is not None and 'subject' in lecture:
                    print(f"{day}-{time_slot}: {lecture['subject']}")

    def create_dataframe(self):
        data = self.timetable
        timetable_df = pd.DataFrame(data, index=self.days, columns=self.time_slots)
        return timetable_df

    def export_to_excel(self, filename_prefix="timetable"):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_prefix}_{current_datetime}.xlsx"
        timetable_df = self.create_dataframe()
        timetable_df.to_excel(filename)

divE_semII = TimetableLoader_fe()
lecture = {"subject": "PSP-I", "faculty": "PBW", "location": "111"}
divE_semII.assign_lecture(0, 0, lecture)

# Export the timetable DataFrame to an Excel file
divE_semII.export_to_excel()

timetable = divE_semII.create_dataframe()
print(timetable)