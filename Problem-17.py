def factorial_digits(n):
    fact = 1
    
    # Calculate factorial
    for i in range(1, n + 1):
        fact *= i
    
    # Convert number into list of digits
    return [int(d) for d in str(fact)]
print(factorial_digits(5))   
print(factorial_digits(10))  
print(factorial_digits(1))   
