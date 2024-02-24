def myrange(start, stop, step=1):
    """Enumerates the values from start in steps of size step that are less than stop."""
    assert step > 0, f"Only positive steps implemented in myrange: {step}"
    i = start
    while i < stop:
        yield i
        i += step

print("list(myrange(2, 30, 3)):", list(myrange(2, 30, 3)))


# Using myrange to find the sum of even numbers between 1 and 100
even_sum = sum(num for num in myrange(1, 101) if num % 2 == 0)

print("Sum of even numbers between 1 and 100:", even_sum)