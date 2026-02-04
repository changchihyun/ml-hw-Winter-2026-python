n = int(input("Enter N: "))

numbers = []

i = 0
while i < n:
    num = int(input("Enter a number: "))
    numbers.append(num)
    i += 1

x = int(input("Enter X: "))

index = -1

for i in range(len(numbers)):
    if numbers[i] == x:
        index = i + 1
        break

print(index)
