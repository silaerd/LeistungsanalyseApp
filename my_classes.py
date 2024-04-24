import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date  # Geburtsdatum als verstecktes Attribut markiert
        self.sex = sex

    def save(self, filename):
        data = self.to_dict()  
        with open(filename, 'w') as file:
            json.dump(data, file)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "birth_date": ""  
        }


class Subject(Person):
    def estimate_max_hr(self):
        birth_date = datetime.strptime(self._Person__birth_date, '%Y-%m-%d')
        age_years = (datetime.now() - birth_date).days // 365
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * age_years
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * age_years
        else:
            max_hr_bpm = int(input("Enter maximum heart rate: "))
        return int(max_hr_bpm)
    
class Experiment:
    def __init__(self, experiment_name, date, supervisor):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor

    def save(self, filename):
        data = self.to_dict()
        with open(filename, 'w') as file:
            json.dump(data, file)

    def to_dict(self):
        return {
            "experiment_name": self.experiment_name,
            "date": self.date,
            "supervisor": self.supervisor.to_dict()  # Umwandlung des Supervisor-Objekts in ein Dictionary
        }

if __name__ == "__main__":
    test_subject = Subject("Lukas", "Balog", "2002-05-09", "male")
    max_hr_bpm = test_subject.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)
    print("Personen-Daten:")
    print(json.dumps(test_subject.to_dict(), indent=4))  

    # Supervisor-Daten erstellen
    supervisor_data = {
        "first_name": "Sila",
        "last_name": "Erdogan",
        "sex": "female",
        "birth_date": "2002-06-09"
    }
    supervisor = Person(
        supervisor_data["first_name"],
        supervisor_data["last_name"],
        supervisor_data["birth_date"],
        supervisor_data["sex"]
    )

    test_experiment = Experiment("Test1", "2024-04-23", supervisor)
    print("Experiment-Daten:")
    print(json.dumps(test_experiment.to_dict(), indent=4))
