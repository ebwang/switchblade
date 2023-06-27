if __name__ == '__main__':
    print("Generate a variety of lists")
    print("Insert the range of first item")
    x = int(input())
    print("Insert the range of second item")
    y = int(input())
    print("Insert the range of third item")
    z = int(input())
    print("Insert the result to avoid in the result of the sum in X + Y + Z")
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
    ## Remember list comprehension syntax
    ## newlist = [expression for item in iterable if condition == True]