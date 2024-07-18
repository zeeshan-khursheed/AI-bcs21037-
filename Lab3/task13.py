string = str(input("Enter a string:   "))

digit = letter = 0

for c in string:
    if c.isdigit():
       digit += 1
    elif c.isalpha():
       letter += 1

print("Digits:  " , digit)
print("Letters: ", letter)