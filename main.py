#!/bin/python
try:
    from colorama import init, Fore, Style, just_fix_windows_console
except ImportError as e:
    print(f"[-] Colorama library is not installed, please install all easyhttp dependencies.")
    exit(1)
import scripts.scripts as utilities

version = "1.3.1"
print(len("              "))

if __name__ == "__main__":
    try:
        init()
        just_fix_windows_console()
    except Exception as e:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Failed to initialize colorama: {e}")
    try:
        utilities.banner(version)
        utilities.main()
    except Exception as e:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} An error occurred: {e}")
else:
    print(f"{Fore.RED}[-]{Style.RESET_ALL} This script is meant to be run directly, not imported as a module.")
    exit(1)