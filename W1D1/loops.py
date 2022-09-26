#LOOPS!

#FOR

# for ___ in ___ :

# First blank ? iterative variable
# Second blank ? collection we iterating over

#range(start,stop,step) takes up to 3 arguments
#start is inclusive  (optional) defaults to 0
#stop is exclusive
#step is optional the increment or decrement amount defaults 1
# for i in range(100,-5,-5):
#     print(i)

#iterative variable will represent each number from the sequence of numbers that range returns

foods = ['steak','calamari','tacos','chicken cutlets']

for one_food in foods:
    # one_food = "cake"
    print(f"Hmmm should I eat {one_food}?")

#iterative variable will represent each element of a list

for i in range(len(foods)):
    foods[i] = "cake"

# print(foods)

food_one = {
    "spicy": True,
    "name": "curry",
    "protein": 'chicken',
    'veggies': True
}
food_two = {
    "spicy": False,
    "name": "potato chips",
    "protein": 'none',
    'veggies': True
}

foods = [food_one, food_two]

print(foods[0]['name'])


# for food in foods:
#     print(food)
#     if food['spicy'] == True:
#         print(f"I'm gonna eat this spicy {food['name']}")

# for key in food_one:
#     print(f"Key: {key} Value: {food_one[key]}")

#iterating over a dictionary will produce each key!



#WHILE
"""
while(condition):
    pass
"""
# x =5
# while(x>0):
#     # x = x-1
#     x -= 1
#     print(x)

#any while loop should be working towards invalidating itself