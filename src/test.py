import sys
from tests import club_test, dance_test, people_test
from tests.customizer import print_custom as cprint


def start_test(test_name: str) -> None:
    if test_name == "club_test":
        club_test.start_club_test()
    if test_name == "dance_test":
        dance_test.start_dance_test()
    if test_name == "people_test":
        people_test.start_people_test()


def main(test_name: str):
    test_name = test_name.lower()
    case = ["club_test", "dance_test", "people_test"]

    if test_name in case:
        return start_test(test_name)
    else:
        cprint(
            "Invalid argument."
            "\nYou can try write 'python3 "
            "test.py dance_test(or club_test or people_test)'",
            "red",
        )
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        cprint(
            "Invalid number of arguments."
            "\nYou can try write 'python3 "
            "test.py dance_class(or club_class or people_class)'",
            "red",
        )
        sys.exit(1)
