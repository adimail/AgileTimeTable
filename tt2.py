import pandas as pd
import numpy as np

# Given data
subjects = ['EM-I', 'PHY', 'EG', 'BEE', 'EM', 'PBLM-I', 'UHV-I', 'PSP-I', 'PE']
lectures_per_week = [3, 3, 1, 3, 2, 0, 1, 2, 1]

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_slots = ['phase1A', 'phase1B', 'phase2A', 'phase2B', 'phase3A', 'phase3B', 'phase3A']

# Create an empty timetable DataFrame
timetable = pd.DataFrame(index=days, columns=time_slots)

# Create a DataFrame to store lectures
lecture_schedule = pd.DataFrame(index=subjects, columns=["Total Lectures"])
lecture_schedule["Total Lectures"] = lectures_per_week

# Fill the timetable with lectures
for subject, lectures in zip(subjects, lectures_per_week):
    for _ in range(lectures):
        day, time_slot = np.where(timetable.isna().values)  # Find empty slots
        if len(day) > 0:
            day = day[0]
            time_slot = time_slot[0]
            timetable.iloc[day, time_slot] = subject

# Display the final timetable
print("Final Timetable:")
print(timetable)
