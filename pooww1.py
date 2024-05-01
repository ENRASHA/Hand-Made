#using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(5, 3))  # Output: 125
print(power(4, 0))  # Output: 1