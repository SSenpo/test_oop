class Dance:
    def __init__(self):
        self.name = ""

    def get_movement(self):
        pass


class Electrohouse(Dance):
    def __init__(self):
        self.name = "Electrohouse"
        self.movements = (
            "покачивание туловищем вперед-назад, почти нет "
            "движения головой, круговые движения  вращения руками, ноги "
            "двигаются в ритме."
        )

    def get_movement(self):
        return self.movements


class Rnb(Dance):
    def __init__(self):
        self.name = "Rnb"
        self.movements = (
            "покачивания телом вперед и назад, ноги в "
            "полу-присяде, руки согнуты в локтях, головой вперед-назад."
        )

    def get_movement(self):
        return self.movements


class Pop(Dance):
    def __init__(self):
        self.name = "Pop"
        self.movements = (
            "плавные движения туловищем, руками, ногами и головой."
        )

    def get_movement(self):
        return self.movements
