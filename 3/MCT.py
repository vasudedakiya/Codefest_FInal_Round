from turtle import pensize


m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(m1)
r1 = int(input("Enter initial row number of the choosen card: "))
m2 = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
print(m2)
r2 = int(input("Enter later row number of the choosen card: "))

x1 = m1[r1 - 1]
x2 = m2[r2 - 1]

for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        if x1[i] == x2[j]:
            print(f"Your card is {x1[i]}")
