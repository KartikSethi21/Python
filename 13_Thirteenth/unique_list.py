item = ["apple","banana","cherry","apple","banana"]

unique = set()

for it in item:
    if it in unique:
        print("Not unique, duplicate item is ",it)
        # break
    unique.add(it)