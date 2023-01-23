from nightclub import club, dance, people
from tests.customizer import print_custom as cprint
from time import sleep


def main():
    cprint("Создаём обьекты классов...", "green")
    rnb = dance.Rnb()
    pop = dance.Pop()
    electro = dance.Electrohouse()

    alice = people.Dancer(name="Alice", styles=[rnb, electro])
    bob = people.Dancer(name="Bob", styles=[pop])
    michael = people.Dancer(name="Michael", styles=[electro])
    lisa = people.Dancer(name="Lisa", styles=[rnb, pop, electro])

    my_club = club.NightClub("BazZar", 300)

    cprint("Начало симуляции...", "green")
    for i in range(10):
        cprint("__" + my_club.set_current_song() + "__\n", "red")
        song = my_club.current_song
        alice.activity(current_song=song)
        bob.activity(current_song=song)
        michael.activity(current_song=song)
        lisa.activity(current_song=song)
        sleep(2)

    cprint("Конец симуляции...", "green")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
