import os 

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def option_wait():
    if os.name == "nt":
        import msvcrt

        while True:
            input = msvcrt.getch()
            if input.decode(errors="ignore").isdecimal():
                return input.decode(errors="ignore")

    else:
        print("Not supported on UNIX systems yet.")
        exit(1)