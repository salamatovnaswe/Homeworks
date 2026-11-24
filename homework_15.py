# T-1
fruits = ['apple', 'banana', 'orange', 'kiwi']
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# T-2
names = ['ali', 'vali', 'hasan', 'husan']
for name in names:
    print(name.upper())

# T-3
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']
for car in cars:
    print(car[0])

# T-4
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']
for countrie in countries:
    print(countrie.lower())

# T-5
names = ['ali', 'sardor', 'abdulloh', 'aziz']
for name in names:
    print(f"{name} - {len(name)} ta harf")

# T-6
animals = ['cat', 'dog', 'lion', 'tiger']
for i in range(len(animals)):
    animals[i] = animals[i].upper()
print(animals)

# T-7
names = ['ali', 'vali', 'sardor', 'aziz']
for i in [0, 1, 2, 3]:
    names[i] = names[i].upper()
print(names)

# T-8
names = ['ali', 'hasan', 'husan', 'sardor']
for i in range(len(names)):
    names[i] = names[i].capitalize()
print(names)

# T-9
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']
for i in range(0, len(names), 2):
    print(names[i])

# T-10
animals = ['tiger', 'lion', 'elephant', 'rabbit']
for animal in animals:
    print(f"{animal[0]} - {animal[-1]}")

# T-11
words = ['python', 'programming', 'computer', 'developer']
new_words = []
for word in words:
    ozgertiw = word[0].upper() + word[1:-1] + word[-1].upper()
    new_words.append(ozgertiw)
print(new_words)

# T-12
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']
for i in range(len(cars)):
    cars[i] =cars[i].upper()
print(cars)

# T-13
name = input("Ism kiriting: ")
count = int(input("Necha marta chiqarilsin: "))
for i in range(count):
    print(name)

# T-14
miyweler = []
sani = int(input("Nechta meva kiritmoqchisiz: "))
print()
for i in range(sani):
    miywe = input(f"{i + 1}- mevani kirirting: ")
    miyweler.append(miywe)
print()
print(f"Mevalar: {miyweler}")

# T-15
renler = []
for i in range(5):
    ren = input(f"{i + 1}-rengni kiriting: ")
    renler.append(ren)
print("\nSizning sevimli ranglaringiz: ")
for ren in renler:
    print(ren)