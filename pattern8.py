def display(n):
    for i in range(n, 0, -1):
        for j in range(5 - i):      #this loop prints spaces
            print(" ", end=" ")
        for k in range(2*i-1):
            #this loop prints two extra stars
            print("*", end=" ")
        print()     #this stmt moves starts new line
display(5)