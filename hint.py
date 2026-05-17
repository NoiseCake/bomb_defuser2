import random
from number_generator import first, second, number

if first%2 == 0:
    first_eo = "Even"
else:
    first_eo = "Odd"

if second%2 == 0:
    second_eo = "Even"
else:
    second_eo = "Odd"

first_range=[
    first - 1, first , first + 1
]
if first == 1:
    first_range = [1,2,3]
if first == 9:
    first_range = [7,8,9]

second_range=[
    second - 1, second, second + 1
]
if second == 0:
    second_range = [0,1,2]
if second == 9:
    second_range = [7,8,9]

lower_bound = number - random.randint(1,10)
upper_bound = number + second + random.randint(1,10)

if lower_bound < 10:
    lower_bound=10
if upper_bound > 99:
    upper_bound=99

btwn = [
    lower_bound,
    upper_bound
]

hint=[
    f"You get the feeling that one of the numbers is {first}",
    f"You get the feeling that one of the numbers is {second}",
    f"You get the feeling that the first number is {first_eo}",
    f"You get the feeling that the second number is {second_eo}",
    f"You get the feeling that first number is between {first_range}",
    f"You get the feeling that second number is between {second_range}",
    f"You get the feeling that the number is between {btwn[0]} and {btwn[1]}"
]

def give_hint():
    give_hint1 = random.choice(hint)
    hint.remove(give_hint1)
    print (give_hint1)