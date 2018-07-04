string = input("Letter: ").lower()

alphabet = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", 
"n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

count = {}

for character in string:
    if character in alphabet: 
        if character in count:
            count[character] +=+ 1
        else:
            count[character] = 1

keys =  count.keys()
for character in keys:
    print(character,count[character])