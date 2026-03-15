# suggest activity
# sunny - go for a walk, rainy - read a book , snowy - build a snoman


weather = 'rainy'

if weather =='rainy':
    print("Read a Book, sleep")
elif weather == 'sunny':
    print("Go for a walk but stil sleep")
elif weather == 'snowy':
    print("Build a snowman and sleep")

match weather.lower():
    case "rainy":
        print("Raining from clouds let it rain u cant do anything")
    case "snowy":
        print("Snow falling from sky u still can to anything")
    case "sunny":
        print("Nothing falling from sky just sun up there still cant do anything")
    case _:
        print("You can do anything now")
