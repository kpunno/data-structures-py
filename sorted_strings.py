from random import randint

strings = ['By', 'Br', 'Ji', 'So', 'Sz', 'Co', 'Gr', 'Za']
# size of 8

new_strings = []
for i in range(10):
    new_strings.append(strings[randint(0, 7)])

print(new_strings)