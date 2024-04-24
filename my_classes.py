import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date  # Geburtsdatum als verstecktes Attribut markiert
        self.sex = sex

    def save(self, filename):
        data = self.to_dict()  # Benutzerdefinierte Methode aufrufen, um das Dictionary zu erstellen
        with open(filename, 'w') as file:
            json.dump(data, file)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex
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

if __name__ == "__main__":
    test_subject = Subject("Lukas", "Balog", "2003-04-22", "male")
    max_hr_bpm = test_subject.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)
    print("Personen-Daten:")
    print(json.dumps(test_subject.to_dict(), indent=4))  
