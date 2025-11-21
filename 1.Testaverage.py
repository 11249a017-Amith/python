1.test1=int(input("enter marks for test1:"))
test2=int(input("enter marks for test2:"))
test3=int(input("enter marks for test3:"))
total = test1+test2+test3
average1=(test1+test2)/2
print("average1:",average1)
average2=(test2+ test3)/2
print ("average2:" ,average2)
average3=(test3+test1)/2
print("average3:",average3)
best_two_average_marks=max(average1,average2,average3)
print("the best two-test average :",best_two_average_marks)
