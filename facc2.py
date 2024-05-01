#f you want to calculate the factorial of a large number, you can use a recursive function instead of a for loop. Here's the code:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial of the given number is: ", factorial(n))
