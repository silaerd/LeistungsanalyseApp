import json
from my_functions import build_person, build_experiment, estimate_max_hr

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

    max_hr_bpm = estimate_max_hr(age, sex)
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Dictionary für die Person erstellen
    person_info = build_person(first_name=first_name, last_name=last_name, sex=sex, age=age)

    # Dictionary für das Experiment erstellen
    experiment = build_experiment(experiment_name=experiment_name, date=date, supervisor=person_info, subject=person_info)

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


    # Experimenten-Dictionary ausgeben
    print("Experiment Information:")
    print(experiment_info)

    # Experimenten-Dictionary in einer Datei speichern
    with open("experiment.json", "w") as outfile:
        json.dump(experiment_info, outfile)

if __name__ == "__main__":
    main()
