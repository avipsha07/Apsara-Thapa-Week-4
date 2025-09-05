def sum_even_numbers():
    n = int(input("Enter a positive integer: "))
    total = 0

    for i in range(2, n + 1, 2):  # step 2 to get even numbers
        total += i

    print("Sum of even numbers from 1 to", n, "is:", total)

def main():
    sum_even_numbers()

main()
