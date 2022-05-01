st = input("Enter a time : ").split(" ")
t = st[0].split(":")
h = int(t[0])
m = int(t[1])

if h <= 12 and h >= 1 and m <= 60 and m >= 0:

    if st[1] == "PM":
        if h == 12:
            h = 12
        else:
            h = h + 12

    if st[1] == "AM" and h == 12:
        h = h + 12

    else:
        pass

    if m < 10:
        m = "0" + str(m)
    print(f"{h}:{m}")

else:
    print("Enter Valid time")
