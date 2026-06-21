from colorama import Fore, Style
class colorful_print():
    def __init__(self):
        self.codes={"+": f"{Fore.GREEN}[+]{Style.RESET_ALL}",
            "-": f"{Fore.RED}[-]{Style.RESET_ALL}",
            "!": f"{Fore.YELLOW}[!]{Style.RESET_ALL}",
            "i": f"{Fore.CYAN}[i]{Style.RESET_ALL}"}
        self.codes_nocolor={"+": "[+]",
            "-": "[-]",
            "!": "[!]",
            "i": "[i]"}
        self.code_list=["+","-","!","i"]
    def getprint(code,color=True):
        code=str(code)
        if not code in code_list:
            print(f"{self.getprint('-', color=color)} Invalid color code: {code}.")
            exit(9)
        if color:
            return self.codes[code]
        else:
            return self.codes_nocolor[code]