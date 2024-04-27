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
    
    def dictionary(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'sex': self.sex,
            'age': self.age
        }

class Subject(Person):
    def estimate_max_hr(self):
        if self.sex == "male":
            return 223 - 0.9 * self.age
        elif self.sex == "female":
            return 226 - 1.0 * self.age
        else:
            return 220 - self.age  # Fallback estimation, kann durch eine detailliertere Logik ersetzt werden

class Experiment:
    def __init__(self, experiment_name, date, supervisor):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor

    def save(self, filename):
        data = self.__dict__
        with open(filename, 'w') as file:
            json.dump(data, file)
    
    def dictionary(self):
        return {
            'experiment_name': self.experiment_name,
            'date': self.date,
            'supervisor': self.supervisor.dictionary()
        }

if __name__ == '__main__':
    test_subject = Subject('Sila', 'Erdogan', 21, 'female')
    max_hr_bpm = test_subject.estimate_max_hr()
    print('Max Heart Rate (bpm):', max_hr_bpm)
    print('Subject Data:')
    print(json.dumps(test_subject.dictionary(), indent=4))

    #Daten für den Supervisor
    supervisor = Person('Lukas', 'Balog', 21, 'male')
    
    test_experiment = Experiment('Test_1', '26.04.2024', supervisor)
    print('Experiment Data:')
    print(json.dumps(test_experiment.dictionary(), indent=4))
