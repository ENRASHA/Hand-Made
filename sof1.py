def calculate_sum():
    while True:
        number1 = float(input("Enter the first number is: "))
        number2 = float(input("Enter the second number is: "))
        number3 = float(input("Enter the third number is : "))

        if number1 == 0 or number2 == 0 or number3 == 0:
            break

        total_numbers = number1 + number2 + number3

        if number1 == number2 == number3:
            print(f"The sum is {total_numbers * 3}.")
        else:
            print(f"The sum is {total_numbers}.")

if __name__ == "__main__":
    calculate_sum()