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
version = "1.8.7"

# defined
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
#else:
#    try:
#        start_from = int(input("Enter starting point (default 0): "))  # Prompt user for starting point
#    except:
#        start_from = 0

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

# Function to display a progress bar
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the number of '#' characters based on the completion percentage
    bar_width = int((terminal_width - 10) * (percent / 100))
    bar = '#' * bar_width + '-' * (terminal_width - 10 - bar_width)

    # Display the progress bar
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

# Generate a list of numbers, each multiplied by 5
numbers = [x * 5 for x in range(2000, 2300)]
results = []

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
    slow_print(''.join(random.sample(s, 4000)))
    slow_print(''.join(random.sample(e, 400)))
    slow_print(''.join(random.sample(r, 2000)))
    print("")

    # Display a progress bar for the calculation of factorials
    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i + 1, len(numbers))

except KeyboardInterrupt:
    # Handle the interruption (optional)
    print("\nKashword Stop Executing.")
    clearpass = None  # Clear password from memory
finally:
    print("\n[Kashword_v{}]:".format(version))
    print(kashword)
    clearpass = None  # Clear password from memory
    kashword = None
