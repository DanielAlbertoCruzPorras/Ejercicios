## Repetitive Structures
# Exercise 4: Even Numbers in a Range
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")


