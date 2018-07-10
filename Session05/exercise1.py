inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["pocket"] = ["seashell", "strangeberry", "lint"]
del inventory["backpack"]
inventory["gold"] = [500]
inventory["gold"]
print(inventory,end="\t")