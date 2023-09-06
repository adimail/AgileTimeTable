import pandas as pd

class DivisionTimetable:
    def __init__(self):
        columns = ['Week Day'] + [f'{hour}:00-{hour+1}:00' for hour in range(8, 16)]

        self.timetable_df = pd.DataFrame(columns=columns)

        self.timetable_df['Week Day'] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

        for hour in range(8, 16):
            self.timetable_df[f'{hour}:00-{hour+1}:00'] = [0] * 5

    def assign_lecture(self, weekday, start_hour, end_hour):
        if self.is_slot_available(weekday, start_hour, end_hour):
            for hour in range(start_hour, end_hour):
                self.timetable_df.loc[self.timetable_df['Week Day'] == weekday, f'{hour}:00-{hour+1}:00'] = ['Lecture'] * 5

    def is_slot_available(self, weekday, start_hour, end_hour):
        weekday_row = self.timetable_df[self.timetable_df['Week Day'] == weekday]
        for hour in range(start_hour, end_hour):
            if 'Lecture' in weekday_row[f'{hour}:00-{hour+1}:00'].values:
                return False
        return True

    def display_timetable(self):
        print(self.timetable_df)

if __name__ == "__main__":
    division_timetable = DivisionTimetable()

    division_timetable.assign_lecture('Mon', 8, 9)

    division_timetable.display_timetable()
