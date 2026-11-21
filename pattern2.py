#Right Angled Triangle Pattern
def display(n):
    for i in range(n): 
        for j in range(i+1): 
            print('*', end=' ')
        print()
display(5)