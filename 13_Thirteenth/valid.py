# keep asking user to enter a number till number is between 1 to 10
while True:
    numb = int(input("Enter a number "))
    if 1<=numb<=10:
        print("Thanks dude")
        break
    else:
        print("Invalid number try again")

