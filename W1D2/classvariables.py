class TestClass:
    all_names = []
    def __init__(self, name):
        self.name = name;
        TestClass.all_names.append(name)

class TestClass2:
    the_string = "the original string"

    def __init__(self, name):
        self.name = name;
        self.the_string = "init string"

class TestClass3:
    the_string = "the original string"

    def __init__(self, name):
        self.name = name;
        TestClass3.the_string = "init string"


test1 = TestClass("test1")
test2 = TestClass("test2")

print("*"*16,"Starting Values", "*"*16)
print("test 1", test1.all_names)  #test 1 ['test1', 'test2']
print("test 2", test2.all_names) #test 2 ['test1', 'test2']
print("TestClass",TestClass.all_names) # TestClass ['test1', 'test2']


test1.all_names = 'test 1 unique all names' #updating through the instance updates only that instance

print("*"*16,"After Updating Through Instance", "*"*16)
print("test 1", test1.all_names) #test 1 test 1 unique all names
print("test 2", test2.all_names) #test 2 ['test1', 'test2']
print("TestClass",TestClass.all_names) #TestClass ['test1', 'test2']

#test1 now has a unique instanced version of .all_names

TestClass.all_names.append('test3')

print("*"*16,"After Updating At Class Level", "*"*16)
print("test 1",test1.all_names) # test 1 test 1 unique all names
print("test 2",test2.all_names) # test 2 ['test1', 'test2', 'test3']
print("TestClass",TestClass.all_names) # TestClass ['test1', 'test2', 'test3']

#test 1 no longer updates with the rest of the class

test4 = TestClass("test4")

print("*"*16,"After Making Another Instance", "*"*16) 
print("test 1",test1.all_names) #test 1 test 1 unique all names
print("test 2",test2.all_names) #test 2 ['test1', 'test2', 'test3', 'test4']
print("test 3",test4.all_names) #test 3 ['test1', 'test2', 'test3', 'test4']
print("TestClass",TestClass.all_names) #TestClass ['test1', 'test2', 'test3', 'test4']

test1.all_names = TestClass.all_names

print("*"*16,"Attempting to reset to class level value", "*"*16)
print("test 1",test1.all_names) #test 1 ['test1', 'test2', 'test3', 'test4']
print("test 2",test2.all_names) #test 2 ['test1', 'test2', 'test3', 'test4']
print("test 3",test4.all_names) #test 3 ['test1', 'test2', 'test3', 'test4']
print("TestClass",TestClass.all_names) #TestClass ['test1', 'test2', 'test3', 'test4']

TestClass.all_names = "WIPED"

print("*"*16,"Are they in sync again?", "*"*16)
print("test 1",test1.all_names) # test 1 ['test1', 'test2', 'test3', 'test4']
print("test 2",test2.all_names) # test 2 WIPED
print("test 3",test4.all_names) # test 3 WIPED
print("TestClass",TestClass.all_names) # TestClass WIPED
# NO! 

del test1.all_names

print("*"*16,"Are they in sync after deletion?", "*"*16)
print("test 1",test1.all_names) # test 1 WIPED
print("test 2",test2.all_names) # test 2 WIPED
print("test 3",test4.all_names) # test 3 WIPED
print("TestClass",TestClass.all_names) # TestClass WIPED
#YES!

print("*"*16,"The String Test", "*"*16)
stringTest = TestClass2("Spencer")
print(stringTest.the_string) #init string
print(TestClass2.the_string) #the original string
#these are different

print("*"*16,"The String Test 2", "*"*16)
stringTest2 = TestClass3("Spencer")
print(stringTest2.the_string) #init string
print(TestClass3.the_string) #init string

# Conclusion: Access class attributes using cls or the class name and not self or instance names if you intend to update for all instances,
#  otherwise you will make a new instance attribute no longer tracking with the class
# What if I do it on accident??
# del test1.all_names deletes the instance variable, resetting to class value