from .dance import Rnb, Electrohouse, Pop


class People:
    def __init__(self, name="Вася_Танцор"):
        self.name = name

    def activity(self):
        pass

    def say_hello(self):
        pass


class Dancer(People):
    def __init__(self, name, styles):
        People.__init__(self, name)
        self.styles = styles
        self.view_styles = []
        for item in self.styles:
            self.view_styles.append(item.name)
        print(self.say_hello())

    def say_hello(self):
        return (
            f"Танцор {self.name} пришел в клуб. {self.name} танцует в "
            f"стиле {self.view_styles}\n"
        )

    def activity(self, current_song):
        for item in self.styles:
            if item.name == current_song:
                print(f"{self.name} - {item.get_movement()}\n")
        if current_song not in self.view_styles:
            print(f"{self.name} - пьёт водку\n")

    def __del__(self):
        print(f"Деструктор вызван для {self.name}")
