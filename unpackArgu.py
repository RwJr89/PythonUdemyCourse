numbers = [1, 2, 3, 4, 5]

def add(*numbers):
    total = 0
    for numbers in numbers:
        total = total + numbers
    return (total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers)
print(*numbers)
print("abc")
print(* "abc")
print("a", "b", "c")
