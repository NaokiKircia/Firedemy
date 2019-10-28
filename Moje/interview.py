def silnia(x):
    if x > 0:
        y = 1
        for i in range(1, x+1):
            y = y*i
        return y
    else:
        print("0! == 1")
print(silnia(6))

x = 6
y = 1
for i in range(1, x+1):
    y = y*i
print(y)


start = 2
stop = 10
def prim_or_not(start, stop):
    for num in range(start, stop + 1):
        if num > 1:
            for n in range(2, num):
                if (num % n) == 0:
                    print(str(num) + " is not prime")
                    break
            else:
                print(str(num) + " is prime")
        elif num == 1:
            print("1 is prime")

prim_or_not(start, stop)