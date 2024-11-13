## Repetitive Structures
# Exercise 7: Sum of Even Numbers Until an Odd is Entered
sum_even = 0

while True:
    num = int(input("Enter an integer: "))
    
    if num % 2 == 0:
        sum_even += num
    else:
        print("An odd number was entered. Stopping.")
        break

print(f"The sum of the even numbers entered is: {sum_even}")


