# fruit colour
# green - unripe, yellow - ripe, brown - overripe

fruit = "Banana"
color = 'Yellow'

fruit = fruit.lower()
color = color.lower()


if fruit == "banana":
    if color == "green":
        val = "Unripe"
    elif color == "yellow":
        val = "Ripe"
    elif color == 'brown':
        val = "Overripe"


print(f"Fruit is {fruit}-{val}")
    
