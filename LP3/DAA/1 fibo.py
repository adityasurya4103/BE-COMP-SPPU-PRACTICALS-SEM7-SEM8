import timeit

def fibonacci(n):
    """Non-recursive Fibonacci function that returns the series up to n"""
    fib_list = [0] * (n + 1)
    fib_list[0] = 0
    if n > 0:
        fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list

def fibonacci_recursive(n):
    """Recursive Fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Taking user input
N = int(input("Enter the value of N for Fibonacci series: "))
RUNS = 1000

print(f"Given N = {N}\n{RUNS} runs")

# Non-recursive Fibonacci
non_recursive_series = fibonacci(N)
print(f"Fibonacci series (non-recursive): {non_recursive_series}")
print(
    f"Fibonacci non-recursive: {non_recursive_series[-1]}"
    f"\tTime: {timeit.timeit(f'fibonacci({N})', setup='from __main__ import fibonacci', number=RUNS):5f} seconds"
    f"\tO(n)\tSpace: O(1)"
)

# Recursive Fibonacci
fib_recur_series = [fibonacci_recursive(i) for i in range(N + 1)]
print(f"Fibonacci series (recursive): {fib_recur_series}")
print(
    f"Fibonacci recursive: {fib_recur_series[-1]}"
    f"\tTime: {timeit.timeit(f'fibonacci_recursive({N})', setup='from __main__ import fibonacci_recursive', number=RUNS):5f} seconds"
    f"\tO(2^n)\tSpace: O(n)"
)


# RUNS specifies the number of times the fibonacci(N) function will be executed to measure its average runtime. This is controlled by the timeit.timeit function, where the number parameter (set to RUNS) defines how many times fibonacci(N) should run.

# Purpose of RUNS: By setting a high value (e.g., RUNS = 1000), the code repeatedly calls fibonacci(N) 1000 times, giving a more accurate measure of average runtime. This reduces fluctuations in timing and gives a stable performance estimate for the function.