import random


class NightClub:
    def __init__(self, name="Ugly Coyote", capasity=50):
        print("Инициализация обьекта класса NightClub\n")
        self.name = name
        self.capasity = capasity
        self.music_style = ["Electrohouse", "Rnb", "Pop"]
        self.current_song = "тишина"
        print(self.about_club())

    def get_music_style(self):
        return self.music_style

    def set_music_style(self, new_music: list):
        self.music_style = new_music

    def get_current_song(self):
        return "Сейчас в зале {} звучит [{}].".format(
            self.name, self.current_song
        )

    def set_current_song(self) -> str:
        random_music = random.randrange(len(self.music_style))
        self.current_song = self.music_style[random_music]
        return (
            "На связи клуб {}!"
            " Следующий трек номер {}. Будем зажигать под {}!".format(
                self.name,
                random.randrange(100),
                self.music_style[random_music],
            )
        )

    def about_club(self):
        return (
            "Ночной клуб {} создан! Может принять {} посетителей, "
            "сегодня играют следующие жанры: {}".format(
                self.name, self.capasity, self.music_style
            )
        )

    def __del__(self):
        print("Клуб {} закрыт(вызван деструктор)".format(self.name))
