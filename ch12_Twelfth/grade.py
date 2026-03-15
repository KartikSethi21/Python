#  A(90-100), B(80-89), C (70-79) , D (60-69), F (below 60)
score = int(input("Please enter the Score "))

if score >100:
    print("Pleae verify the score again. Not Valid")
    exit()


if score>=90:
    gr = 'A'
elif score>=80:
    gr = 'B'
elif score >=79:
    gr = 'C'
elif score >=69:
    gr = 'D'
else:
    gr = 'F'

print("Grade Obtained is",gr)