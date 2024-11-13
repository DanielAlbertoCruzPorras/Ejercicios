## Repetitive Structures
# Exercise 1: Sum of the First N Integers
n = int(input("Enter a positive integer: "))

sum_total = 0

for i in range(1, n + 1):
    sum_total += i

print(f"The sum of the first {n} integers is: {sum_total}")

