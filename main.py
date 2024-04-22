from my_functions import build_person, build_experiment, estimate_max_hr
from my_classes import Experiment, Person

def main():
    # Patienten daten anlegen
    first_name = input("Enter Patients first name: ")
    last_name = input("Enter Patients last name: ")
    sex = input("Enter Patients sex: ")
    age = int(input("Enter Patients age: "))

    # Experimentendaten anlegen
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date: ")
    supervisor = input("Enter supervisor name: ")

    # Berechnung der maximalen Herzfrequenz
    max_hr_bpm = person.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Dictionary für den Patienten erstellen
    person_info = build_person(first_name = first_name, last_name = last_name, sex = sex, age = age)

    # Dictionary für das Experiment erstellen
    experiment = build_experiment(experiment_name = experiment_name, date = date, supervisor = person_info, subject = person_info)

    # Dictionary für die Experiment-Informationen erstellen
    experiment_info = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "sex": sex
        }

    # Experimenten-Information ausgeben
    print("Experimenten Information:", experiment_info)
    
    # Experimenten-Information in einer Datei speichern
    with open("experiment.json", "w") as outfile:
        json.dump(experiment_info, outfile)

if __name__ == "__main__":
    main()




