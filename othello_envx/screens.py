from colorama import Fore, Back, Style, init

init(autoreset=True)  # Initialize colorama

def intro_screen():
    clear_screen()
    print(Back.RED + Fore.YELLOW + Style.BRIGHT + ' ' * 12 + ' Welcome to ' + ' ' * 12)
    print(Fore.WHITE + Style.NORMAL)
    print(r"""
____ ___ _  _ ____ _    _    ____ 
|  |  |  |__| |___ |    |    |  | 
|__|  |  |  | |___ |___ |___ |__| 
                                  
    """)
    print(Back.RED + Fore.YELLOW + Style.BRIGHT + ' ' * 12 + ' by Envxsion ' + ' ' * 12)
    input("Press Enter to start...")


def end_screen(winner, black_count, white_count):
    clear_screen()
    print(Back.CYAN + Fore.BLACK + Style.BRIGHT + ' ' * 15 + ' Game Over ' + ' ' * 15)
    if winner == 'Tie':
        print(Fore.WHITE + Style.BRIGHT + "It's a tie!")
    else:
        print(Fore.YELLOW + Style.BRIGHT + f"Player {winner} wins!")

    print(Fore.RED + f'Black Count: {black_count}  White Count: {white_count}')

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
