def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        print("Collatz sequence:")
        while number != 1:
            print(number, end=" ")
            number = collatz(number)
        print(1)  # Print the last number in the sequence

except ValueError:
    print("Please enter a valid integer.")