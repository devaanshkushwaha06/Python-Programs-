import random

# Generate 5 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random Numbers:", random_numbers)

# Define a given list
given_list = [1, 2, 3, 4, 5]

# Shuffle the given list
shuffled_list = given_list[:]
random.shuffle(shuffled_list)
print("Shuffled List:", shuffled_list)