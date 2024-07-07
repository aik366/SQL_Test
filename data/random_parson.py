from mimesis import Person, Address
from mimesis.enums import Gender
from mimesis.locales import Locale
import random


def get_person():
    person = Person(Locale.RU)
    job_title = ["Менеджер", "Бухгалтер", "Юрист", "Программист", "Дизайнер", "Консультант", "Секретарь"]
    person_gender, person_list = person.gender(), []
    if person_gender == "Муж.":
        person_list.append(person.name(gender=Gender.MALE))
        person_list.append(person.surname(gender=Gender.MALE))
        person_gender = "Мужчина"
    else:
        person_list.append(person.name(gender=Gender.FEMALE))
        person_list.append(person.surname(gender=Gender.FEMALE))
        person_gender = "Женщина"
    person_list.append(random.randint(18, 80))
    person_list.append(person.telephone().replace("-(", "(").replace(")-", ") "))
    person_list.append(random.choice(job_title))
    person_list.append(person_gender)
    return person_list


if __name__ == "__main__":
    print(get_person())
