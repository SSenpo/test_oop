from nightclub import club as nc
from .customizer import print_custom as cprint


def start_club_test():
    cprint("Тестируем класс NightClub...", "green")
    try:
        club = nc.NightClub()
        print(club.get_current_song() + "\n")
        club1 = nc.NightClub("Bazzar", 500)
        print(club1.get_current_song())
        cprint("Попробуем поставить музыку!", "yellow")
        print(club.set_current_song())
        print(club.get_current_song() + "\n")
        print(club1.set_current_song())
        print(club1.get_current_song() + "\n")

        print(
            "Текущий плейлист по жанрами - {}".format(club.get_music_style())
        )
        club.set_music_style(["Jazz", "Blues", "Metall", "Phonk"])
        print(
            "Новый плейлист, если захотеть - {}\n".format(
                club.get_music_style()
            )
        )
        print(club.set_current_song())
        print(club.get_current_song() + "\n")

        del club, club1
    except Exception as e:
        print(e)
