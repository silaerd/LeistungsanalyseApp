import json
from my_functions import build_person, build_experiment

def main():
    # Benutzer nach den erforderlichen Daten für die Versuchsperson fragen
    first_name = input("Vornamen der Versuchsperson eingeben: ")
    last_name = input("Nachnamen der Versuchsperson eingeben: ")
    sex = input("Geschlecht der Versuchsperson eingeben: ")
    age = int(input("Alter der Versuchsperson eingeben: "))

    # Versuchsperson erstellen
    subject = build_person(first_name, last_name, sex, age)

    # Benutzer nach den erforderlichen Daten für das Experiment fragen
    experiment_name = input("Namen des Experiments eingeben: ")
    date = input("Datum des Experiments eingeben: ")
    supervisor = input("Namen des Supervisors eingeben: ")

    # Experiment erstellen
    experiment = build_experiment(experiment_name, date, supervisor, subject)

    # Speichern des Experiments in einer Datei
    with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile, indent=4)


if __name__ == "__main__":
    main()
