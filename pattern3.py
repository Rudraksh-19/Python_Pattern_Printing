#Inverted Right Angled Triangle
def display(n):
    for i in range(n): 
        for j in range(i, n): 
            print('*', end=' ')
        print()
display(5)