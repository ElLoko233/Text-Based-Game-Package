# __main__.py
import subprocess
import sys


def Playdemo():
    # Creating new project folder
    try:
        if sys.argv[1] == "Play-demo":
            subprocess.call(["..TBG_Example/main.py", "-c"])

        else:
            print("Invalid keyword: format>> python -m Play-demo")

    except IndexError:
        print("Invalid argument input: format>> python -m Play-demo")


if __name__ == "__main__":
    Playdemo()
