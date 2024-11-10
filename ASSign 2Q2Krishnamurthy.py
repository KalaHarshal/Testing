n = int(input("Enter the number to check :"))
original = n
sum = 0

while n>0:
    digit = n%10
    factorial = 1
    for i in range(1, digit+1):
        factorial*=i
    sum+=factorial
    n//=10

if(sum == original):
    print ("yes, Krishnamurthy number ")
else:
    print("Not a Krishnamurthy No")
