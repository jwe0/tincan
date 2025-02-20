from datetime import datetime
from colorama import Fore

def success(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.GREEN}[+]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def error(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.RED}[-]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def info(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.YELLOW}[~]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def inpt(message):
    return input( f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.BLUE}[?]{Fore.RESET}\t{message}")