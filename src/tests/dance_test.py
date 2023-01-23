from nightclub.dance import Rnb, Electrohouse, Pop
from .customizer import print_custom as cprint


def start_dance_test():
    cprint("Тестируем класс Dance...", "green")
    try:
        first_obj = Rnb()
        print("Создали класс Rnb(Dance)")
        print(f"Движения стиля Rnb -> {first_obj.get_movement()}\n")
        second_obj = Pop()
        print("Создали класс Pop(Dance)")
        print(f"Движения стиля Pop -> {second_obj.get_movement()}\n")
        last_obj = Electrohouse()
        print("Создали класс Electrohouse(Dance)")
        print(f"Движения стиля Electrohouse -> {last_obj.get_movement()}\n")

    except Exception as e:
        print(e)
