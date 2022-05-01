N = int(input("Enter Value : "))
a = 2
b = 3
for i in range(0, N, 1):
    print(b, end=" ")
    t = b
    b = b + a
    a = t
