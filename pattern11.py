def display(n):
    for i in range(1, n+1):
        #this loop is for row number
        for j in range(1, i+1):
            '''
            stars prints when :-
            j == 1 -> denotes first column
            j == i -> denotes last column for each row
            i == n -> denotes last row
            '''
            if j==1 or j==i or i==n:
                print("*", end=" ")
            else:
                # this prints blank spaces
                print(" ", end=" ")
        print()     #this stmt moves to next line

display(5)
