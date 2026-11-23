'''
# Outer loop prints the upper half of the diamond
for i in range(1, 6):
    # Prints spaces before stars to center the pattern
    for j in range(5 - i):
        print(" ", end=" ")
    # Prints odd numbers of stars in increasing order
    for k in range(2 * i - 1):
        print("*", end=" ")
    # Moves to the next line
    print()
# Outer loop prints the lower half of the diamond
for i in range(4, 0, -1):
    # Prints spaces before stars to center the pattern
    for j in range(5 - i):
        print(" ", end=" ")
    # Prints odd numbers of stars in decreasing order
    for k in range(2 * i - 1):
        print("*", end=" ")
    # Moves to the next line
    print()

'''
def display(n):
    #this loop prints verticle pyramid
    for i in range(1,n+1):
        #this loop is for row number
        for j in range(n - i):
            #this loop prints spaces
            print(" ", end=" ")
        for k in range(2 * i - 1):
            #this loop prints 2 stars in each row
            print("*", end=" ")
        print()

    #this loop prints inverted pyramid
    for i in range(n-1, 0, -1):
        #this loop is for row number
        # this loop starts from n-1 to maintain diamon pattern
        # inshort n-1 avoids printing largest no
        for j in range(n - i):
            #this loop prints spaces
            print(" ", end=" ")
        for k in range(2 * i - 1):
            #this loop prints 2 extra stars in each row
            print("*", end=" ")
        print()

display(5)
