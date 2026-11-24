def display(n):
    # this loop is for top butterfly pattern
    for i in range(1, n+1):
        #this loop is for row number
        for j in range(1,i+1):
            #this prints upper left butterfly pattern
            print("*", end=" ")
        for k in range(1, (n-i)* 2+1):
            #this prints blank spaces for upper butterfly pattern
            print(" ", end=" ")
        for l in range(1, i+1):
            #this prints upper right butterfly pattern
            print("*", end=" ")
        print()     #this stmt moves cursor to new line

    # this loop is for lower butterfly pattern
    for i in range(n-1, 0, -1):
        #this loop is for row number
        # n-1 is used to maintain the lower butterfly pattern
        for j in range(1, i+1):
            #this prints lower left butterfly pattern
            print("*", end=" ")
        for k in range(1, (n-i) * 2+1):
            #this prints blank spaces in lower butterfly pattern
            print(" ", end=" ")
        for l in range(1, i+1):
            #this prints lower right butterfly pattern
            print("*", end=" ")
        print()

display(5)