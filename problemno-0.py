# Iterative Fibonacci function
def fibonacci_iterative(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b


# Debugging version of the iterative Fibonacci function
def fibonacci_iterative_debug(num):
    trace_steps = []
    
    def compute_fib(n):
        a, b = 0, 1
        trace_steps.append(f'Initializing: a={a}, b={b}')
        for i in range(2, n + 1):
            a, b = b, a + b
            trace_steps.append(f'Step {i}: a={a}, b={b}')
        return b
    
    final_result = compute_fib(num)
    return trace_steps, final_result


# Testing the functions

# Test the iterative Fibonacci function
print("Iterative Fibonacci of 5:", fibonacci_iterative(5))

# Debugging the iterative Fibonacci function
trace_steps, final_result = fibonacci_iterative_debug(5)
print("Trace of Steps:")
print("\n".join(trace_steps))
print("Final Result:", final_result)
