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
    all_cats = []
    cute = True
    def __init__(self, data, owner_name):
        self.color = data['color'] #black (for cat1_data)
        self.name = data['name']
        self.size = data['size']
        self.cute = True
        self.owner = Human(owner_name)
        Cat.all_cats.append(self)

    def __repr__(self):
        return f"Cat class object: Name:{self.name} Color: {self.color} Size: {self.size} Owned by: {self.owner.name}"

    def print_info(self):
        print(f"Hello my name is {self.name} I am a {self.color} {self.size} cat, I live with {self.owner.name}")
        return self

    def meow(self):
        print(f"{self.name} says MEOOOOOOOOOW")

    def bite_owner(self):
        print(f"{self.name} takes a bite out of {self.owner.name}")
        self.owner.yell()

    @classmethod #classmethods have access to and can change attributes on the class level
    def print_all_cat_info(cls):
        for cat in cls.all_cats:
            cat.print_info()
        
    @classmethod
    def revolt(cls):
        for cat in cls.all_cats:
            cat.bite_owner()

    @staticmethod #cannot change anything (STATIC) hold some related functionality to the class
    def years_to_cat_years(years):
        return years * 7

class Human:
    def __init__(self, name):
        self.name = name

    def yell(self):
        print(f"{self.name} yells out in pain")

# human_1 = Human("Jasmine")
# human_2 = Human("Kevin")
# human_3 = Human("Joe")
#cat1.owner = (owner instance here)
#these lines create cat instances
cat1 = Cat({
    'color': 'black',
    'name': 'Midnight',
    'size': 'chonky'
},"Jasmine") 
cat2 = Cat(cat2_data,"Kevin")
cat3 = Cat(cat3_data, "Joe")
# if cat1.cute:
#     print("He sure is cute!")
print(cat1)
# cat1.cute = False
# print(cat1.cute)
# print(cat2.cute)
# cat1.cute = False

# if cat1.cute:
#     print("He sure is cute!")
# else:
#     print("You really don't think so???")

# Cat.print_all_cat_info()
Cat.revolt()


# print(cat1.name)
# print(cat2.name)
# print(cat3.name)
#these lines call the print info method for each cat instance
# None.print_info()

# cat1.extra_attribute = "Wow this is extra"
# print(cat1.extra_attribute)