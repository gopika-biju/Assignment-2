def c2f(celsius):
    """
    Convert Celsius to Fahrenheit
    F = ((9 * C) / 5.0) + 32
    """
    return ((9 * celsius) / 5.0) + 32

def f2c(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    C = (F - 32) * (5.0 / 9)
    """
    return (fahrenheit - 32) * (5.0 / 9)

# Simple test code
if __name__ == "__main__":
    # Test Celsius to Fahrenheit
    c = 100
    f = c2f(c)
    print(f"{c} Celsius is {f:.2f} Fahrenheit")

    # Test Fahrenheit to Celsius
    f = 212
    c = f2c(f)
    print(f"{f} Fahrenheit is {c:.2f} Celsius")