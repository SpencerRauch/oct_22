#Object Orientated Programming
#Object - a tangible thing, it can do stuff, can be described with attributes -- A NOUN

cat1_data = {
    'color': 'black',
    'name': 'Midnight',
    'size': 'chonky'
}
cat2_data = {
    'color': 'orange',
    'name': 'Garfield',
    'size': 'lasagna'
}
cat3_data = {
    'color': 'green',
    'name': 'Lucky',
    'size': 'smol'
}

#Classes are like blueprints to an object
#attributes are data we hold in our class about an instance
#methods are things our objects can do
class Cat:
    # def __init__(self,color,name,size):
    #     self.color = color
    #     self.name = name
    #     self.size = size
    def __init__(self, data):
        self.color = data['color'] #black (for cat1_data)
        self.name = data['name']
        self.size = data['size']
        self.cute = True

    def print_info(self):
        print(f"Hello my name is {self.name} I am a {self.color} {self.size} cat")
        return self

    def meow(self):
        print(f"{self.name} says MEOOOOOOOOOW")


#these lines create cat instances
cat1 = Cat({
    'color': 'black',
    'name': 'Midnight',
    'size': 'chonky'
}) 
cat2 = Cat(cat2_data)
cat3 = Cat(cat3_data)
if cat1.cute:
    print("He sure is cute!")


cat1.cute = False

if cat1.cute:
    print("He sure is cute!")
else:
    print("You really don't think so???")

# print(cat1.name)
# print(cat2.name)
# print(cat3.name)
#these lines call the print info method for each cat instance
# None.print_info()

# cat1.extra_attribute = "Wow this is extra"
# print(cat1.extra_attribute)