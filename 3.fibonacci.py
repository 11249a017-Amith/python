a=0
b=1
time=int(input("enter the sequence number:\n"))
for seq in range(time):
    print(a,end="")
    a,b=b,a+b
