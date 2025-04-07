import time
import os
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama for colored text
init(autoreset=True)

# Generate large "I MISS YOU" text
large_text = pyfiglet.figlet_format("I MISS YOU")

# Heart ASCII Art
heart_frames = [
    "  .:::.   .:::.",
    " :::::::.:::::::",
    " :::::::::::::::",
    " ':::::::::::::'",
    "   ':::::::::'  ",
    "     ':::::'    ",
    "       ':'      "
]

def clear_screen():
    """Clears the console screen for smooth animation."""
    os.system("cls" if os.name == "nt" else "clear")

def animate_text_with_heart():
    """Displays large 'I MISS YOU' with a continuously bouncing heart."""
    spaces = 0
    direction = 1
    heart_offset = 30  # Position heart to the right of the text

    while True:  # Infinite loop for continuous animation
        clear_screen()

        # Print large "I MISS YOU" in red
        print(Fore.RED + Style.BRIGHT + large_text)

        # Print bouncing heart
        for i, line in enumerate(heart_frames):
            print(" " * heart_offset + Fore.RED + line)

        time.sleep(0.1)  # Pause to create animation effect

        # Move heart up and down
        heart_offset += direction
        if heart_offset >= 35 or heart_offset <= 30:
            direction *= -1  # Reverse direction

# Run the animation (infinite loop)
try:
    animate_text_with_heart()
except KeyboardInterrupt:
    clear_screen()
    print(Fore.YELLOW + "Animation stopped. Have a great day! ❤️")
