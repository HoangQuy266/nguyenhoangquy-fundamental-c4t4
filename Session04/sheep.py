print ("Hello, my name is Hiepand these are my sheep size: ")

sheep = [5, 7, 300, 90, 24, 50 ,75]
print (sheep)

for i in range (3):
    print("MONTH", i+1)

    print ("Now one month has passed and this is my flock: ")
    new_sheep = [x+50 for x in sheep]
    print (new_sheep)

    max_sheep = max(new_sheep)
    print ("Now my biggest sheep has size", max(new_sheep), "let's shear it")

    print ("After shearing, here is my flock: ")
    index = new_sheep.index(max(new_sheep))
    new_sheep[index] = 8
    print (new_sheep)

    sheep = list(new_sheep)