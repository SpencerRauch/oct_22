print("Hello October 2022")

# comments!
#Variables -- a container where you can keep data

name = "Spencer"
number_of_dogs = 2
#variables are names using snake case -- all lower case separated by underscores
#exception: classes will be capitalized 
# let var const <-- no need to these in python


#Datatypes
#primitive
#numbers
num = 8
float_num = 8.5
#strings
string = "Collection of characters"
string2 = 'String 2'
f_string = f'{name} has {number_of_dogs} dogs'
#type casting functions
num5 = int("5")

string5 = str(5)
None #like null in js, it is nothing

print(f_string)
#booleans true or false
bool1 = True
bool2 = False

#composite
#tuples IMMUTABLE list of values accessed by index
my_tuple = (1,2,3,4,5)
print(my_tuple[3])
# my_tuple[3] = 12 #type error
 
#lists
list = [1,7,3,8,5]
#zero indexed
list[2] = 100
print(list)

#list functions:
len(list) #returns length of the list (JS array.length)
min(list) #return lowest value from the list
max(list) #highest value

#list methods
# list.reverse()
# list.sort(reverse=True)
list.append(98457) #append to add a value to a list
list.remove(100) #removes a VALUE
list.pop(0) # optionally take an INDEX to pop
print(list)



#dictionaries
# KEY VALUE PAIRS! 
dog = {
    'name': 'Wiley',
    'age': 4,
    'breed': "Chihuahua / Pomeranian mix"
}

#access
print(dog['name'])
#assignment
# dog['color'] = 'Orangey tan'
print(dog)

#check if key exists
if 'color' in dog:
    print(dog['color'])
else:
    print("Key not found")

#removing from dict
# del dog['breed']
# breed = dog.pop('breed')
# dog.clear()
# print(breed)
# print(dog)

# string = "Don't tell me what to do"

#Conditionals --an expression returns a boolean value that we will use to determine logic
# <, <=, >, >=, ==, not, !=, or, and THERE IS NO TRIPLE EQUALS

"""
None instead of null
not instead of !
or instead of ||
and instead of &&
== instead of ===
"""
#use pass for empty code blocks

x = 8
if x == 5:
    print("x is 5")
elif x > 5:
    print("greater than 5")
else:
    print("x is not 5 and not greater than 5")




