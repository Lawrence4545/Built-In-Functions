message = ("corona vaccines are now ready at the warehouse")
print(message)

print(message.capitalize())
Message = message.capitalize()
print(Message)
print()

print(Message.isupper())
print(Message)
print()


message = ("corona vaccines are now ready at the warehouse")
print(message.islower())
print(message)
print()

# Find Fuctions:This fuctions are use to find values for a particular words that we might want to search for
message = ("corona vaccines are now ready at the warehouse")
print(message.find("ready"))
print()

# slicing
print(message[24:29])

# join functions:This are used to concatenate elements of an iterable (such as a list, tuple, or string) into a single string.
seq1 = ("192", "168", "69", "40")
print((".".join)(seq1))

seq1 = ("192", "168", "69", "40")
print(("-".join)(seq1))

seq1 = ("192", "168", "69", "40")
print(("/".join)(seq1))
print()

# Joining characters of a string with a hyphen separator
word = ("hello")
print(",".join(word))
# Output: "h-e-l-l-o"

# Joining elements of a list with a comma separator
colors = ('red', 'green', 'blue')
print(",".join(colors))
# Output: "red, green, blue"
print()
mountain = ["Everst", "k2", "sahadri"]
print(mountain)

mountain.append("oregon mount, Kilimanjaro,")
print(mountain)

mountain.extend(["Olympus"])
print(mountain)
print()

# function is used to remove and return an element from a list or a dictionary. The behavior of the pop() function differs slightly between lists and dictionaries.
# Synthex: element = list.pop(index)
fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: 'banana'
print(fruits)         # Output: ['apple', 'cherry']
print()
fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: 'cherry'
print(fruits)         # Output: ['apple', 'banana']

person = {'name': 'Lawrence', 'age': 30, 'city': 'Benin City'}
age = person.pop('age')
print(age)          # Output: 30
print(person)       # Output: {'name': 'John', 'city': 'New York'}

person = {'name': 'Lawrence', 'age': 30, 'city': 'Benin City'}
person.pop('city')
print(city)          # Output: Benin City
print(person)
