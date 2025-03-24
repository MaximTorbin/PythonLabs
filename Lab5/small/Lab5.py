#№1
'''
with open('input1.txt', 'r') as infile:
    numbers = infile.read().split()
    numbers = [int(num) for num in numbers]

product = 1
for num in numbers:
    product *= num

with open('output1.txt', 'w') as outfile:
    outfile.write(str(product))
'''
#№2
'''
with open('input2.txt', 'r') as infile:
    numbers = [int(line.strip()) for line in infile]

sorted_numbers = sorted(numbers)

with open('output2.txt', 'w') as outfile:
    for num in sorted_numbers:
        outfile.write(str(num) + '\n')
'''
#№3
'''
with open('input3.txt', 'r') as infile:
    children = []
    for line in infile:
        parts = line.strip().split()
        surname, name, age = parts
        age = int(age)
        children.append({'surname': surname, 'name': name, 'age': age})

oldest = max(children, key=lambda x: x['age'])
youngest = min(children, key=lambda x: x['age'])

with open('output3.txt', 'w') as outfile:
    outfile.write(f"oldest:{oldest['surname']} {oldest['name']} {oldest['age']}\n")
    outfile.write(f"youngest:{youngest['surname']} {youngest['name']} {youngest['age']}\n")
'''

