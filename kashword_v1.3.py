import time
import hashlib
import sys
import getpass
import random
import string
import math

# Function to display a progress bar
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    # Calculate the number of '#' characters based on the completion percentage
    bar = '#' * int(percent / 3) + '-' * (33 - int(percent / 3))
    # Display the progress bar
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

# Function to print a string character by character with a slight delay
def slow_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.00001)

# Generate a list of numbers, each multiplied by 5
numbers = [x * 5 for x in range(2000, 2300)]
results = []

# Create strings for password generation
s = string.ascii_lowercase * 1000 + string.ascii_uppercase * 1000 + string.digits * 1000 + string.punctuation * 1000
e = "-" * 1000 + "-" * 100 + "" * 200
r = "-+" * 4000

# Get user input for a password (masked input)
clearpass = getpass.getpass(prompt='Enter Cypher: ', stream=None)
# Hash the entered password using SHA256
hash = hashlib.new("SHA256")
hash.update(clearpass.encode())
sixteen = hash.hexdigest()[:16]  # Extract the first 16 characters of the hash

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
print("\n[Kashword_v1.3]:")
print(sixteen)
