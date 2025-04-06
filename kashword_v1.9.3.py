import time, hashlib, sys, getpass, random, string, math, argparse, shutil, os

# Set these parameters:
## Unique user input parameters:
length = 15 # Please Define Lenght Here
start_from = 1 # Plaese Set Start From Here
algorithm = "SHA256" # Please make sure that entered algorithm is available in hashlib.
plaintext_prefix = ""
plaintext_suffix = ""
after_hash_masking_prefix = ""
after_hash_masking_suffix = ""

## Script parameters:
version = "1.9.3"
password_masking = "*"
loading_time = 0.005 # Time delay for the loading effect

os_name = os.name
kashword_printed_on_terminal = False
terminal_width, _ = shutil.get_terminal_size()
after_hash_masking_prefix_lenth = len(after_hash_masking_prefix)
after_hash_masking_suffix_lenth = len(after_hash_masking_suffix)

# Variables for storing input parameters
clearpass = ""
selected_length_hash_output = ""

parser = argparse.ArgumentParser(description="Kashword")
parser.add_argument("-v", action="store_true", help="Print version info")
parser.add_argument("-l", type=int, help="Specify length")
parser.add_argument("-s", type=int, help="Specify starting point")
parser.add_argument("-C", action='store_true', help="Cypher Will Entered In Clear Text")
parser.add_argument("-R", action='store_true', help="Skip After Hash Maasking")
parser.add_argument("-P", action='store_true', help="Hide Lenght")

args = parser.parse_args()

if args.v:
    print("\nKashword version: {}".format(version))
    sys.exit(0)

if args.l:
    length = args.l

if args.C:
    clearpass = "clear"

if args.P:
    password_masking = " "
    
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
tmplr_logo = [
    "┓┏┓   ┓         ┓",
    "┃┫ ┏┓┏┣┓┓┏┏┏┓┏┓┏┫",
    "┛┗┛┗┻┛┛┗┗┻┛┗┛┛ ┗┻"
]
# Function to display the loading logo
def slow_print_logo(delay):
    for line in tmplr_logo:
        print(line)
        time.sleep(delay)  # Add delay between each line

def logo_loading():
    print()
    slow_print_logo(delay=loading_time+0.01)  # Adjust delay for slower/faster printing
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

    if clearpass == "clear":
        clearpass = input('Enter Cypher: ')

    # Hash the entered password 
    hash = hashlib.new(algorithm)
    clearpass = plaintext_prefix + clearpass + plaintext_suffix
    hash.update(clearpass.encode())
    hash_output = hash.hexdigest()

    # Extract the substring from the hash based on the specified length and starting point
    selected_length_hash_output = hash_output[start_from-1:start_from-1 + length]

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

    print("\n[Kashword_v{}] (Kashword will be erased in 5 seconds)".format(version))
    if args.R:
        kashword = selected_length_hash_output
    else:
        kashword = (after_hash_masking_prefix + selected_length_hash_output[after_hash_masking_prefix_lenth:])[:len(selected_length_hash_output) - after_hash_masking_suffix_lenth] + after_hash_masking_suffix
    print(f"\r{kashword}", end="")
    kashword_printed_on_terminal = True
    if os_name == 'nt':
        command = f'echo {kashword.rstrip()}| clip'
        os.system(command)
    time.sleep(5)
    remove = password_masking * length  # or len(remove) if using a pattern
    print(f"\r{remove}", end="\n")
    kashword_printed_on_terminal = False

except KeyboardInterrupt:
    #Handle the interruption (optional)
    if kashword_printed_on_terminal == True:
        remove = password_masking * length  # or len(remove) if using a pattern
        print(f"\r{remove}", end="\n")
        kashword_printed_on_terminal = False

    print("\nKashword Stop Executing.")

finally:
    clearpass = None  # Clear password from memory
    kashword = None
    selected_length_hash_output = None
    command = None
    start_from = None
    algorithm = None
    plaintext_prefix = None
    plaintext_suffix = None
    after_hash_masking_prefix = None
    after_hash_masking_suffix = None
    after_hash_masking_prefix_lenth = None
    after_hash_masking_suffix_lenth = None
    if kashword_printed_on_terminal == True:
        remove = password_masking * length  # or len(remove) if using a pattern
        print(f"\r{remove}", end="\n")
    length = None
    kashword_printed_on_terminal = None
