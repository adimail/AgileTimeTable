# import pandas as pd

# class TimetableLoader:
#     def __init__(self):
#         self.days = ['mon', 'tue', 'wed', 'thu', 'fri']
#         self.time_slots = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'C30']

#         self.timetable_df = pd.DataFrame(index=self.days, columns=self.time_slots)

#     def assign_lecture(self, row_idx, col_idx, lecture):
#         self.timetable_df.at[row_idx, col_idx] = lecture

#     def print_timetable(self):
#         # Iterate over rows and columns to print only the subject name
#         for day in self.days:
#             for time_slot in self.time_slots:
#                 lecture = self.timetable_df.at[day, time_slot]
#                 if isinstance(lecture, dict) and 'subject' in lecture:
#                     print(f"{day}-{time_slot}: {lecture['subject']}")



# divE_semII = TimetableLoader()

# lecture = {"subject": "PSP-I", "faculty": "PBW", "location": "111"}

# # for i in range(0,5):
# #     for j in range(0,7):
# #         divE_semII.assign_iloc_lecture('i', 'A1', lecture)

# divE_semII.assign_lecture('mon', 'A1', lecture)
# divE_semII.print_timetable()


import numpy as np
import pandas as pd

class TimetableLoader:
    def __init__(self):
        self.days = ['mon', 'tue', 'wed', 'thu', 'fri']
        self.time_slots = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'C30']
        self.timetable_df
        
        # Create an empty NumPy array to represent the timetable
        self.timetable = np.empty((len(self.days), len(self.time_slots)), dtype=object)

    def assign_lecture(self, row, col, lecture):
        self.timetable[row, col] = lecture

    def print_timetable(self):
        # Iterate over rows and columns to print only the subject name
        for day in self.days:
            for time_slot in self.time_slots:
                lecture = self.timetable_df.at[day, time_slot]
                if isinstance(lecture, dict) and 'subject' in lecture:
                    print(f"{day}-{time_slot}: {lecture['subject']}")

    def create_timetable(self):
        data=self.timetable
        self.timetable_df = pd.DataFrame(data, index=self.days, columns=self.time_slots)


divE_semII = TimetableLoader()
lecture = {"subject": "PSP-I", "faculty": "PBW", "location": "111"}
divE_semII.assign_lecture(0, 0, lecture)
divE_semII.print_timetable()