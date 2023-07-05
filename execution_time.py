import time

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to(n):
    for i in range(2, n + 1):
        is_prime(i)

start_time = time.time()  # Record the start time
print_primes_up_to(10000000)  # This will take a long time!
end_time = time.time()  # Record the end time

print(f"\nExecution time: {end_time - start_time} seconds")  # Print the difference (execution time)