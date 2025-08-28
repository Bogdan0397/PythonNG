def calculate_years(principal, interest, tax, desired):
    counter = 0
    P = principal
    while P < desired:
        P = P + ((P * interest) * (1-tax))
        counter += 1

    return counter

print(calculate_years(1000, 0.05, 0.18, 1100))  # Output: 3