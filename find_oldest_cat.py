class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
cat1 = Cat('Mittens', 9)
cat2 = Cat('Maxi', 3)
cat3 = Cat('Baby Mich', 5)


# Find the oldest cat
def oldest_cat(*args):
    return max(args)


# Output
print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
