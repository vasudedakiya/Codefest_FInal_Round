file = open("input.txt")
N = int(file.readline())

colour = {
    "R": [1],
    "Y": [2],
    "B": [3],
    "O": [1, 2],
    "P": [1, 3],
    "G": [2, 3],
    "A": [1, 2, 3],
    "U": [],
    "\n": [],
}


for i in range(0, N, 1):
    count = int(file.readline())
    ele = list(file.readline())
    flist = []
    ishu = 0
    for i in ele:
        flist.append(colour.get(i))
    for i in range(1, 4):
        x = 0
        for j in flist:
            if i in j:
                print(i)
                temp = list(flist[x])
                temp.remove(i)
                flist[x] = temp
                ishu += 1
            else:
                break
            x = x + 1

    print(flist)
