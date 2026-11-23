def display(n):
    for i in range(1, n+1):
        for j in range(n - i):      #this loops prints spaces 
            print(" ", end=" ")
        for k in range(2 * i - 1):  
            #this loop prints 2 extra stars in each row
            print("*", end=" ")
        print()     #this stmt moves to the next line
display(5)