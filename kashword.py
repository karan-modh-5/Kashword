import time
import hashlib
import sys
import getpass
import random
import string
import math
import argparse
import shutil  

# Set these parameters:
length = 15
start_from = 1 # Plaese note that 
algorithm = "SHA256" # Please make sure that entered algorithm is available in hashlib.
version = "1.8.9"
loading_time = 0.005 # Time delay for the loading effect
terminal_width, _ = shutil.get_terminal_size()

# Variables for storing input parameters
clearpass = ""
kashword = ""

parser = argparse.ArgumentParser(description="Kashword")
parser.add_argument("-v", action="store_true", help="Print version info")
parser.add_argument("-l", type=int, help="Specify length")
parser.add_argument("-c", help="Specify Cypher")
parser.add_argument("-s", type=int, help="Specify starting point")

args = parser.parse_args()

if args.v:
    print("\nKashword version: {}".format(version))
    sys.exit(0)

if args.l:
    length = args.l

if args.c:
    clearpass = args.c

if args.s is not None:
    start_from = args.s

# Function to display a progress bar
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    terminal_width, _ = shutil.get_terminal_size()
    #print(int(terminal_width *10 /100))
    if terminal_width > 136:
        terminal_width = 136

    bar_width = int((terminal_width - int((terminal_width * 40 /100 ))) * (percent / 100))
    bar = '#' * bar_width + '-' * (terminal_width - int((terminal_width * 40 /100)) - bar_width)

    print(f"\rKashword |{bar}| {percent:.2f}%", end="\r")

# ASCII logo used in the script
roman_logo = [
    ".-------------------------------------------------------------------------------------------.",
    "| oooo    oooo                    oooo                                                  .o8 |",
    "| `888   .8P'                     `888                                                 \"888 |",
    "|  888  d8'     .oooo.    .oooo.o  888 .oo.   oooo oooo    ooo  .ooooo.  oooo d8b  .oooo888 |",
    "|  88888[      `P  )88b  d88(  \"8  888P\"Y88b   `88. `88.  .8'  d88' `88b `888\"\"8P d88' `888 |",
    "|  888`88b.     .oP\"888  `\"Y88b.   888   888    `88..]88..8'   888   888  888     888   888 |",
    "|  888  `88b.  d8(  888  o.  )88b  888   888     `888'`888'    888   888  888     888   888 |",
    "| o888o  o888o `Y888\"\"8o 8\"\"888P' o888o o888o     `8'  `8'     `Y8bod8P' d888b    `Y8bod88P |",
    "`-------------------------------------------------------------------------------------------'"
]

thick_logo = [
    ".--------------------------------------------------.",
    "| 8  dP           8                              8 |",
    "| 8wdP  .d88 d88b 8d8b. Yb  db  dP .d8b. 8d8b .d88 |",
    "| 88Yb  8  8 `Yb. 8P Y8  YbdPYbdP  8' .8 8P   8  8 |",
    "| 8  Yb `Y88 Y88P 8   8   YP  YP   `Y8P' 8    `Y88 |",
    "`--------------------------------------------------'"
]

just_K_logo = [
    ".--------------.",
    "| oooo    oooo |",
    "| `888   .8P'  |",
    "|  888  d8'    |",
    "|  88888[      |",
    "|  888`88b.    |",
    "|  888  `88b.  |",
    "| o888o  o888o |",
    "`--------------'"
]

RubiFont_logo = [
#    ".------------------------------------------.",
    " ▗▖ ▗▖ ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▖ ▗▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄  ",
    " ▐▌▗▞▘▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌  █ ",
    " ▐▛▚▖ ▐▛▀▜▌ ▝▀▚▖▐▛▀▜▌▐▌ ▐▌▐▌ ▐▌▐▛▀▚▖▐▌  █ ",
    " ▐▌ ▐▌▐▌ ▐▌▗▄▄▞▘▐▌ ▐▌▐▙█▟▌▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀ ",
#    "`------------------------------------------'"
]

tmplr_logo = [
    "┓┏┓   ┓         ┓",
    "┃┫ ┏┓┏┣┓┓┏┏┏┓┏┓┏┫",
    "┛┗┛┗┻┛┛┗┗┻┛┗┛┛ ┗┻"
]
# Function to display the loading logo
def slow_print_logo(RubiFont_logo, delay):
    if int(terminal_width) > 136:
        for line in RubiFont_logo:
            print(line)
            time.sleep(delay)  # Add delay between each line
    if int(terminal_width) < 135:
        for line in tmplr_logo:
            print(line)
            time.sleep(delay)  # Add delay between each line

def logo_loading():
    print()
    slow_print_logo(RubiFont_logo, delay=loading_time+0.01)  # Adjust delay for slower/faster printing
    print()

# Function to clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows ('cls') or Unix/Linux ('clear')

# Main function for running the loading effect
def loading():
    #clear()  # Clear the terminal screen
    logo_loading()  # Show the ASCII logo with a loading effect

def hash_size(algorithm):
    try:
        # Convert algorithm name to lowercase for consistency
        algorithm = algorithm.lower()
        # Check if the specified algorithm is supported
        if algorithm not in hashlib.algorithms_available:
            print(f"Error: '{algorithm}' is not a supported hash algorithm.")
            return

        # Calculate the hash of an empty string using the specified algorithm
        hasher = hashlib.new(algorithm)
        hasher.update(b"")
        hash_output = hasher.hexdigest()
        
        # Return the size of the hash in characters
        return len(hash_output)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if start_from + length > hash_size(algorithm):
        print("Starting point and Lenght parameters are invalid.")
        sys.exit(0)

# Function to print a string character by character with a slight delay
def slow_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.00001)

# Create strings for password generation
s = string.ascii_lowercase * 1000 + string.ascii_uppercase * 1000 + string.digits * 1000 + string.punctuation * 1000
e = "-" * 1000 + "-" * 100 + "" * 200
r = "-+" * 4000

try:
    loading()
    # Get user input for a password (masked input)
    if clearpass == "":
        clearpass = getpass.getpass(prompt='Enter Cypher: ', stream=None)
        
    # Hash the entered password 
    hash = hashlib.new(algorithm)
    hash.update(clearpass.encode())
    hash_output = hash.hexdigest()

    # Extract the substring from the hash based on the specified length and starting point
    kashword = hash_output[start_from-1:start_from-1 + length]

    # Print random samples of characters from the defined strings
    slow_print(''.join(random.sample(s, 1000)))
    slow_print(''.join(random.sample(e, 400)))
    slow_print(''.join(random.sample(r, 1000)))
    print("")

    total_steps = 100
    progress_bar(0, total_steps)
    
    # Simulate a task that takes time (e.g., reading files, processing data, etc.)
    for i in range(total_steps):
        time.sleep(loading_time)  # Simulating work (replace with real task)
        progress_bar(i + 1, total_steps)
    print()  # Print a newline after completion

except KeyboardInterrupt:
    # Handle the interruption (optional)
    print("\nKashword Stop Executing.")
    clearpass = None  # Clear password from memory
finally:
    print("\n[Kashword_v{}] (Kashword will be erased in 5 seconds)".format(version))
    print(f"\r{kashword}", end="")
    time.sleep(5)
    remove = "*" * len(kashword)  # or len(remove) if using a pattern
    print(f"\r{remove}", end="\n")
    clearpass = None  # Clear password from memory
    kashword = None
