from __future__ import barry_as_FLUFL


num = list(input("Enter number : "))
m = 1
for i in range(0, len(num), 1):
    m *= int(num[i])


for i in range(1, m + 1, 1):
    if i % 3 == 0 or i % 5 == 0 or (i % 5 == 0 and i % 3 == 0):
        print(i, end=" ")
