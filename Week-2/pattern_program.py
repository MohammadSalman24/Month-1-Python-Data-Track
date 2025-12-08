# Week 2 - Pattern Programs

def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

def number_pattern(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

# Demo
if __name__ == "__main__":
    print("Right Triangle")
    right_triangle(5)
    print("\nPyramid")
    pyramid(5)
    print("\nInverted Triangle")
    inverted_triangle(5)
    print("\nNumber Pattern")
    number_pattern(5)
    print("\nFloyd Triangle")
    floyd_triangle(5)
