n = int(input("Enter the number for Fibonacci series: "))
series = []

if n <= 0:
    print("Input number should be positive")
elif n == 1:
    series = [0]
    print(series)
elif n == 2:
    series = [0, 1]
    print(series)
else:
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    print(series)

print("The nth Fibonacci number is:", series[-1])
