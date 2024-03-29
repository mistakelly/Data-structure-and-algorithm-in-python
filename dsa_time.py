import time
import time

def sum_of_first_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Test the function with larger values of n
input_sizes = [10**i for i in range(1, 6)]  # input sizes from 10 to 100000
for n in input_sizes:
    start_time = time.time()
    result = sum_of_first_n(n)
    end_time = time.time()
    print(f"n = {n}, Result = {result}, Time = {end_time - start_time} seconds")
