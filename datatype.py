# Data Types
number = 45  # int
num = 56.78  # float
greeting = "Hello World"  # str
isPythonInteresting = True  # bool

# variable storing multiple values
languages = ["python", "php", "java"]  # list
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "China", "USA"}  # set
# Dictionary
details = {
    "firstname" : "Grace",
    "age" : 17,
    "course" : "MIT",
    "nationality"
    : "North America"
}

print(details["course"])
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)

# Determining the data type
print(type(details))
print(type(countries))
# type casting - converting one data type to another
print(int(num))
print(float(number))


