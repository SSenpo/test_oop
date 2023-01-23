def print_custom(text: str, color: str) -> None:
    check_color = ["yellow", "green", "red"]
    if color not in check_color:
        raise ValueError("\n\033[31m\033[1mInvalid [color] value\033[0m")
    elif color == "yellow":
        print("\n\033[33m\033[1m{}".format(text))
        print(
            "------------------------------"
            "------------------------------\033[0m"
        )
    elif color == "green":
        print("\033[32m\033[1m {}".format(text))
        print(
            "--------------------------------------------------"
            "----------\033[0m"
        )
    elif color == "red":
        print(
            "\n\033[31m\033[1m----------------------------------------"
            "--------------------"
        )
        print("{}\033[0m".format(text))
