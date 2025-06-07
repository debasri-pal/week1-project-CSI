def print_lower_triangle(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

def print_upper_triangle(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()

def print_pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars.rstrip())
    print()

# Number of rows
rows = 5

# Call the functions
print_lower_triangle(rows)
print_upper_triangle(rows)
print_pyramid(rows)


