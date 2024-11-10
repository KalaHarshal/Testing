n = int(input("Enter the number to check the automorphic: "))
square = n*n
print(square)
if square % (10**len(str(n)))==n:
    print ("Yes a automorphic no")
else:
    print("Not a automorphic no")
