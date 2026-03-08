# defined the prime_number as 'p_n'.

def p_n(num):
    """Define the fucntion for the cheking the value prime or not."""
    if num < 1:
        print("This is not the prime number.")
        is_prime = True

    for i in range(1,num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("This is the prime number")
    else:
        print("This is not prime number.")

prime_number = p_n(4)

        