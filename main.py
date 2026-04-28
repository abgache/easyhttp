#!/bin/python
from colorama import init, Fore, Style, just_fix_windows_console
import scripts.scripts as utilities

version = "1.0.0"

if __name__ == "__main__":
    try:
        init()
        just_fix_windows_console()
        utilities.banner(version)
        utilities.main()
    except Exception as e:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} An error occurred: {e}")