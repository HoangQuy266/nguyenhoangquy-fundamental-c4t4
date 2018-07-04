
# dictionary/objest/map

# key : value
# create new dictionary
dictionary={
    "hc":"hoc",
    "pt":"piet",
    "ng":"nguoi",
    "eny":"em nguoi yeu",
    "any":"anh nguoi yeu",
    "ns":"noi",
    "ngta":"nguoi ta",
    "lm":"lam",
    "r":"roi",
    "stt":"status"
}

loop = True
while loop:
    for key in dictionary.keys():
        print(key, end="\t")
    print()
    code=input("Ur code:?")
    if code in dictionary:
        print("Translation:", dictionary[code])
    else:
        print("Not found")
        contribute=input("Want to contribute?(Y/N)")
        if contribute =="y":
            trans=input("Ur translation:")
            dictionary[code]=trans
        else:
            print("bye")
            loop=False

