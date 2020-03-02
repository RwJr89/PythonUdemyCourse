number = 1

while number <= 100:
    print(number)
    number = number + 1
    
L = []

while len(L) < 5:
    new_name = input("Please add new name:").strip().capitalize()
    L.append(new_name)


print("Sorry list is full")
print(L)
