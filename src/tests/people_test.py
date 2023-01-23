from nightclub import club, dance, people
from .customizer import print_custom as cprint


def start_people_test():
    cprint("Тестируем класс People...", "green")
    try:
        rnb = dance.Rnb()
        pop = dance.Pop()
        electro = dance.Electrohouse()

        first_man = people.Dancer(name="Joe", styles=[rnb, pop])
        second_man = people.Dancer(name="Aloha", styles=[pop])
        last_man = people.Dancer(name="Alice", styles=[electro])

    except Exception as e:
        print(e)
