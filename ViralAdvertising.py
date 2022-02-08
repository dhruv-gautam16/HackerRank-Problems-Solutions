import math
input_str = input()
try:
    nbr = int(input_str)
except:
    print("An exception occurred while parsing input as integer.")
if nbr <= 0 or nbr >= 51:
    print("Bad input specified")
result = 0
people = 5
for day in range(1, nbr + 1):
    half = math.floor(people / 2)
    result += half
    people = 3 * half
print(result)