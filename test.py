from my_classes import Person, Experiment

def test_case_1():
    # Testfall 1: Eine Person und ein Experiment erstellen und speichern
    first_name = "Lukas"
    last_name = "Balog"
    sex = "male"
    age = 21

    experiment_name = "First Experiment"
    date = "10.04.2024"
    supervisor = "Sila"

    person = Person(first_name, last_name, age, sex)
    max_hr_bpm = person.estimate_max_hr()

    experiment = Experiment(experiment_name, date, supervisor)
    experiment.save("test_experiment.json")

def test_case_2():
    # Testfall 2: Eine andere Person und ein anderes Experiment erstellen und speichern
    first_name = "Sila"
    last_name = "Erdogan"
    sex = "female"
    age = 21

    experiment_name = "Second Experiment"
    date = "11.04.2024"
    supervisor = "Lukas"

    person = Person(first_name, last_name, age, sex)
    max_hr_bpm = person.estimate_max_hr()

    experiment = Experiment(experiment_name, date, supervisor)
    experiment.save("second_experiment.json")

if __name__ == "__main__":
    # Führe die Testfälle aus
    test_case_1()
    test_case_2()
