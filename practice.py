num = int (input("Enter the number of rows"))
for i in range (1, num+1):
    print(" "*(num-i), end=" ")
    for j in range(1, i+1):
        print(i, end=" ")
    print()