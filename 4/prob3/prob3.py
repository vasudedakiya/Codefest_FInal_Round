file = open("input.txt")
N = file.readline()
temp = file.readline()
temp = temp.split(" ")
customer = int(temp[0])
product = int(temp[1])
button_press = 0
a = 0
customers = []

for i in range(0, customer, 1):
    customer1 = sorted(file.readline().split(" "))
    customer1 = [int(i) for i in customer1]
    customers.append(customer1)

for k in range(0, len(customers) - 1, 1):
    flag = False
    for j in range(0, product):
        for x in customers[j]:
            for y in customers[j + 1]:
                print(str(x) + "  " + str(y))
                if x == y:
                    flag = True
        if flag == False:
            a = customer1[j] - a
            button_press += a
            a = customer1[j]
        print()

print(button_press)
