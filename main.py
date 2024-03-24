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

    # Experiment ausgeben
    print("Experiment erstellt:")
    print("Experiment Name:", experiment['experiment_name'])
    print("Datum:", experiment['date'])
    print("Supervisor:", experiment['supervisor'])
    print("Versuchsperson:")
    print("Vorname:", experiment['subject']['first_name'])
    print("Nachname:", experiment['subject']['last_name'])
    print("Geschlecht:", experiment['subject']['sex'])
    print("Alter:", experiment['subject']['age'])

if __name__ == "__main__":
    main()
