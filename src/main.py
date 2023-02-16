def adder_simple(a, b):
    print(f"arguments are {a} and {b}")
    return a + b


def adder_with_error_handling(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Arguments must be higher than zero")
    return a + b
