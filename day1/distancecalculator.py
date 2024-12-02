import os
from collections import Counter


current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'input_lists.md')

with open(file_path, 'r', encoding='utf-8') as file:
    stringlists = file.read()

firstcol = []
secondcol = []

for line in stringlists.split("\n")[:-1]:
    # Split the line into two parts based on spaces
    num1, num2 = line.split()
    firstcol.append(int(num1))  # Convert to integer and add to column1
    secondcol.append(int(num2)) 

print(firstcol, secondcol)
print(len(firstcol), len(secondcol))

sortedfirst, sortedsecond = sorted(firstcol), sorted(secondcol)

distance = sum(map(lambda x, y: abs(x - y), sortedfirst, sortedsecond))

instances = Counter(sortedsecond)
similarity = sum(map(lambda x: x*instances[x], sortedfirst))

print(distance)
print(similarity)


# splitting the two columns in stringlists into two lists