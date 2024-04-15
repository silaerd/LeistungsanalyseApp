from my_functions import build_person, build_experiment, estimate_max_hr
from my_classes import Experiment, Person

def main():
    # Benutzer nach den benötigten Daten für die Person fragen
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    sex = input("Enter sex: ")
    age = int(input("Enter age: "))

    # Benutzer nach den benötigten Daten für das Experiment fragen
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date: ")
    supervisor = input("Enter supervisor name: ")

    # Erstellen einer Instanz der Klasse Person
    person = Person(first_name, last_name, age, sex)

    # Berechnung der maximalen Herzfrequenz
    max_hr_bpm = person.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Erstellen einer Instanz der Klasse Experiment
    experiment = Experiment(experiment_name, date, supervisor)

    experiment.save("experiment.json")

if __name__ == "__main__":
    main()




