def display(n):
    for i in range(1, n+1):     
        for j in range(n - i):  #this loops print spaces
            print("  ", end="")
        for k in range(i):      #this loops prints the stars
            print("*", end=" ")
        print()                 #this stmt used to start new line 

display(5)