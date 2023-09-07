import pandas as pd
import random

def generate_timetable(subjects, hours_per_week):
    # Define the days and time slots for the timetable
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['phase1A', 'phase1B', 'phase2A', 'phase2B', 'phase3A', 'phase3B', 'phase3A']

    # Create an empty timetable DataFrame
    timetable = pd.DataFrame(index=days, columns=time_slots)

    # Generate random timetable entries for each subject
    for subject, hours in zip(subjects, hours_per_week):
        for _ in range(hours):
            day = random.choice(days)
            time_slot = random.choice(time_slots)
            timetable.at[day, time_slot] = f'{subject}'

    timetable.fillna('-', inplace=True)
    return timetable

# Example inputs
subjects = ['EM-I', 'PHY', 'EG ', 'BEE', 'EM', 'PBLM-I', 'UHV-I', 'PSP-I', 'PE']
hours_per_week = [3,3,1,3,2,0,1,2,1]  # Teaching hours per week for each subject

# Generate the timetable
division_timetable = generate_timetable(subjects, hours_per_week)

# Print the generated timetable
print(division_timetable)
