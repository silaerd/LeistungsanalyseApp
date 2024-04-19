from my_classes import Person, Experiment

def test_experiment1():
    # Testfall 1: Eine Person und ein Experiment erstellen und speichern
    first_name = "Sila"
    last_name = "Erdogan"
    sex = "female"
    age = 21

    experiment_name = "First Experiment"
    date = "10.04.2024"
    supervisor = "Lukas"

    person = Person(first_name, last_name, age, sex)
    max_hr_bpm = person.estimate_max_hr()

    experiment = Experiment(experiment_name, date, supervisor)
    experiment.save("test_experiment.json")
    return max_hr_bpm

def test_experiment2():
    # Testfall 2: Eine andere Person und ein anderes Experiment erstellen und speichern
    first_name = "Zoltan"
    last_name = "Balog"
    sex = "male"
    age = 45

    experiment_name = "Second Experiment"
    date = "11.04.2024"
    supervisor = "Lukas"

    person = Person(first_name, last_name, age, sex)
    max_hr_bpm = person.estimate_max_hr()

    experiment = Experiment(experiment_name, date, supervisor)
    experiment.save("second_experiment.json")
    return max_hr_bpm

if __name__ == "__main__":
    max_hr_person1 = test_experiment1()
    max_hr_person2 = test_experiment2()
    print('Die Maximale Herzfrquenz von Person 1 beträgt:', max_hr_person1)
    print('Die Maximale Herzfrquenz von Person 1 beträgt:', max_hr_person2)
