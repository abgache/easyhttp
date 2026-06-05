#!/bin/python
from colorama import init, Fore, Style, just_fix_windows_console
import scripts.scripts as utilities
from log.logger import logger

version = "1.3.1"

if __name__ == "__main__":
    # Terminal colors initialization
    try:
        init()
        just_fix_windows_console()
    except Exception as e:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Failed to initialize colorama: {e}")
    # Logger initialization
    try:
        log = logger()
    except Exception as e:
        if "--logs" in __import__("sys").argv:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Failed to initialize logger: {e}")
            exit(5)
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Failed to initialize logger: {e}")
        log = None
    try:
        utilities.banner(version)
        utilities.main()
    except Exception as e:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} An error occurred: {e}")
else:
    print(f"{Fore.RED}[-]{Style.RESET_ALL} This script is meant to be run directly, not imported as a module.")
    exit(1)