items =["Sweater", "T-Shirt"]
while True: 
    n = input("Welcome to our shop, what do you want? (C, R, U, D)").lower()
    if n == "R":
        print("Our items: ", *items, sep=",")
        
    elif n == "C":
        create = input("Enter new item:")
        items.append(create)
        print("Our items: ", *items, sep=",")
        
    elif n == "U":
        position = int(input("Update position:"))
        new = input ("New item :")
        del our_item[update_pos-1]
        our_item.append(new)
        print ("Our item:",*our_item, sep = ", ")
        
    elif n == "D":
        delete = int(input("Delete position: "))
        del items[delete-1]
        print("Our items:", *items)        

    else:
        asking = False
    
