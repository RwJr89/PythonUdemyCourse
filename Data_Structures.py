# Data Structures Learn about Lists, Tuples and Dictionaries
our_list = [27, 46, -5, 17, 99]
print(our_list)
type(our_list)
jackson = ["A", "B", "C", 1,2,3, "Do", "Rey", "Mi", True, False]
jackson[4]
jackson[7]
jackson[-2]
x = jackson[6]
jackson[start:end:step]
jackson[0:3]
jackson
our_list = [1,2,[3,4,5], 6, 7, 8]
our_table = [[1,2,3],[4,5,6],[7,8,9]]

# Tuples are similar to Lists but cannot be changed
our_tuple = (1,2,3 "A", "B", "C")

# Conver Lists to a Tuple
A = [1,2,3] #List
A = tuple(A)
A = (1,2,3) # tuple

# Dictionaries
students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}

# Search Dictionary
students = ["Dan"]

# Add to Dictionary
students["Fred"] = 25

# Delete from Dictionary
del students["Fred"]

# Make changes to Dictionary
students["Alice"] # Current age = 25
students{"Alice"] = 26

# Dictionary Keys
students.keys() # Will print dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma']) which is not indexable

# Pulling Dictionary Values
students.values() # will print dict_values([21, 26, 27, 22, 17])

# To index students.keys/values it must be converted to a List
list(students.keys())
list(students.values())

# Created code that is able to pull dictionary information

students = {
    "Alice":{"id":"ID0001", "age":26, "grade":"A"},
    "Bob":{"id":"ID0002", "age":27, "grade":"B"},
    "Claire":{"id":"ID0003", "age":17, "grade":"C"}, 
    "Dan":{"id":"ID0004", "age":21, "grade":"D"},
    "Emma":{"id":"ID0005", "age":22, "grade":"E"}
    }

print(students["Dan"]["age"])

print(students["Emma"]["id"], students["Emma"]["grade"])


# Build Travis, Security System

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Greorgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("Whats is your name?:").strip().capitalize()

if name in known_users:
    print("Hello {}!".format(name))
    remove = input("Would you like to be removed from the system (y/n)?:").strip().lower()

if remove == "y":
    known_users.remove(name)
elif remove == "n":
    print("No problem, I didn't want you to leave anyway!")

else:
    print("Hmmm I don't think I have met you yet{}".format(name))
    add_me = input("Would you like to be added to the system (y/n)?:").strip().lower()
if add_me == "y":
    known_users.append(name)
elif add_me == "n":
    print("No worries, see you around!")


# Build a Cinema booking simulator

films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

# Film choices

while True:

    choice = input("What film would you like to watch?:").strip().title()

# Age check

    if choice in films:
        age = int(input("How old are you?:").strip())
        if age >= films[choice][0]:
            # Seat check

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")

