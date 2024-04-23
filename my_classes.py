import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, sex):
        self._first_name = first_name
        self._last_name = last_name
        self.__birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        self._sex = sex

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

    def save(self, filename):
        data = {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "birth_date": self.__birth_date.strftime('%Y-%m-%d'),
            "sex": self._sex
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

class Subject(Person):
    def estimate_max_hr(self):
        age_years = self.calculate_age()
        if self._sex == "male":
            max_hr_bpm = 223 - 0.9 * age_years
        elif self._sex == "female":
            max_hr_bpm = 226 - 1.0 * age_years
        else:
            max_hr_bpm = int(input("Enter maximum heart rate: "))
        return int(max_hr_bpm)

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.get_birth_date().year - ((today.month, today.day) < (self.get_birth_date().month, self.get_birth_date().day))
        return age

class Supervisor(Person):
    def __init__(self, first_name, last_name, birth_date, sex):
        super().__init__(first_name, last_name, birth_date, sex)

class Experiment:
    def __init__(self, experiment_name, date, supervisor):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor

    def save(self, filename):
        data = {
            "experiment_name": self.experiment_name,
            "date": self.date,
            "supervisor": self.supervisor
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

if __name__ == "__main__":
    test_subject = Subject("Lukas", "Balog", "2003-04-22", "male")
    max_hr_bpm = test_subject.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)
