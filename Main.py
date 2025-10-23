import time
import sys
from colorama import init, Fore, Style
from lyrics import lyrics , Song_Name


init()

neon_colors = [
    Fore.CYAN,
    Fore.MAGENTA,
    Fore.YELLOW,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX
]

print(f"\n--- {Song_Name} ---\n")

for i, item in enumerate(lyrics):
    line_text = item['line']
    typing_speed = item['typing_speed']
    delay_after = item['delay_after']

    current_color = neon_colors[i % len(neon_colors)]

    for char in line_text:
        sys.stdout.write(current_color + char)

        sys.stdout.flush()

        time.sleep(typing_speed)

    print(Style.RESET_ALL)

    time.sleep(delay_after)

print("\n--- Song Finished ---")

