def display(n):
    for i in range(n):
        #this loop is for row number
        for j in range(n):
            '''
            stars prints when :-
            i == 0 -> represents first row
            j == 0 -> represents first cloumn
            i == n-1 -> represents last row
            j == n-1 -> represents last cloumn
            '''
            if i == 0 or j == n-1 or i == n-1 or j == 0:
                print("*", end=" ")
            else:
                #this prints blank spaces
                print(" ", end=" ")
        print()     #this stmt moves to next line
display(5)