number = int(input("Number: "))
count = 0
while(number>0): 
    number = number//10
    count += 1
print("Total digits: ", count)