import random

random_numbers = [random.randint(1,20) for i in range(1,11)]

filtered_numbers_less_than_10_a = [rn for rn in random_numbers if rn < 10]

filtered_numbers_less_than_10_b = list(filter(lambda x: x < 10, random_numbers))
