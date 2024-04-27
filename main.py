import json
from my_functions import build_person, build_experiment, estimate_max_hr
from my_classes import Experiment, Person, Subject

def main():
    # Patientendaten anlegen
    first_name = input("Enter patient's first name: ")
    last_name = input("Enter patient's last name: ")
    sex = input("Enter patient's sex: ")
    age = int(input("Enter patient's age: "))
    
    # Patienteninstanz erstellen
    person = Subject(first_name, last_name, age, sex)

    # Experimentendaten anlegen
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date: ")
    supervisor_name = input("Enter supervisor name: ")
    supervisor = build_person(supervisor_name, 'Mustermann', 50, 'male')  # Annahme eines weiteren Details für den Supervisor

    # Berechnung der maximalen Herzfrequenz
    max_hr_bpm = person.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Experimenteninstanz erstellen
    experiment = build_experiment(experiment_name, date, supervisor, person)

    # Dictionary für die Experiment-Informationen erstellen
    experiment_info = {
        'experiment_name': experiment_name,
        'date': date,
        'supervisor': supervisor.dictionary(),  # Umwandlung in ein Dictionary, falls `supervisor` ein Objekt ist
        'subject': {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'sex': sex,
            'max_hr_bpm': max_hr_bpm
        }
    }

    # Experimenten-Information ausgeben
    print("Experiment Information:", json.dumps(experiment_info, indent=4))
    
    # Experimenten-Information in einer Datei speichern
    with open("experiment.json", "w") as outfile:
        json.dump(experiment_info, outfile, indent=4)

if __name__ == "__main__":
    main()
