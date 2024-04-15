import json

class Person:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex
    
    def save(self, filename):
        data = self.__dict__
        with open(filename, 'w') as file:
            json.dump(data, file)

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
             max_hr_bpm = 226 - 1.0 *  self.age
        else:
        # der input() öffnet ein Eingabefensterx für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
class Experiment:
    def __init__(self, experiment_name, date, supervisor):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor

    def save(self, filename):
        data = self.__dict__
        with open(filename, 'w') as file:
            json.dump(data, file)


if __name__ == "__main__":
    test_person = Person("Lukas ", "Balog", 21, "male")
    max_hr_bpm = test_person.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)