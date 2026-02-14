def polynomial_evaluate(coeffs, x):
    result = 0
    for coefficient in coeffs:
        result = result * x + coefficient
    return result

coefficients = [3,-2,0,5]
x = 701.125

print(polynomial_evaluate(coefficients, x))