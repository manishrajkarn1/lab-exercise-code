# take input
u_n = int(input("Enter the number: "))

# assume number is prime initially
is_prime = True

# numbers <= 1 are not prime
if u_n <= 1:
    is_prime = False
else:
    for i in range(2, u_n):
        if u_n % i == 0:
            is_prime = False
            break

# final result
if is_prime:
    print(f"{u_n} is a prime number.")
else:
    print(f"{u_n} is not a prime number.")
