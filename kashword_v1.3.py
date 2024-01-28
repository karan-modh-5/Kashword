import time
import hashlib
import sys
import getpass
import random
import string
import math

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent / 3) + '-' * (33 - int(percent / 3))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

def slow_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.00001)

def loading_animation():
    for i in range(10):
        print('#', end='', flush=True)
        time.sleep(0.5)

numbers = [x * 5 for x in range(2000, 2300)]
results = []

s = string.ascii_lowercase * 1000 + string.ascii_uppercase * 1000 + string.digits * 1000 + string.punctuation * 1000
e = "-" * 1000 + "-" * 100 + "" * 200
r = "-+" * 4000

clearpass = getpass.getpass(prompt='Enter your password: ', stream=None)
hash = hashlib.new("SHA256")
hash.update(clearpass.encode())
sixteen = hash.hexdigest()

s = string.ascii_lowercase * 1000 + string.ascii_uppercase * 1000 + string.digits * 1000 + string.punctuation * 1000
e = "-" * 1000 + "-" * 100 + "" * 200
r = "-+" * 4000

slow_print(''.join(random.sample(s, 4000)))
slow_print(''.join(random.sample(e, 400)))
slow_print(''.join(random.sample(r, 2000)))
print("")
progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
print("\n[Kashword_v1.3]:")

print(sixteen[:16])