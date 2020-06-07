import os
import subprocess
import sys
import getpass


def goToDesktop(username):
    os.chdir("/")
    os.chdir("Users/" + username + "/Desktop")


if __name__ == "__main__":
    username = getpass.getuser()
    goToDesktop(username)
    os.system("echo 'Gotcha'>test.txt")
