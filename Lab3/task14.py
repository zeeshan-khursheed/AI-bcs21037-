import re

print("Password Requirements:")
print("At least 1 letter between [a-z] and 1 letter between [A-Z]")
print("At least 1 number between [0-9]")
print("At least 1 character from [$#@]")
print("Minimum length: 6")
print("Maximum length: 16")

password = input("Enter your password:  ")

x = True

while x:
    if (len(password)<6) or (len(password)>16):
       break
    elif not re.search("[a-z]",password):
       break
    elif not re.search("[A-Z]",password):
       break
    elif not re.search("[0-9]",password):
       break
    elif not re.search("[$#@]",password):
       break
    elif re.search("\s",password):
       break
    else:
       print("Valid Password!")
       x = False
       break

if x:
    print("Not a Valid Password!")



l, u, p, d = 0, 0, 0, 0
s = input("Enter password:  ")
if (len(s) >= 8):
	for i in s:

		# counting lowercase alphabets 
		if (i.islower()):
			l+=1		

		# counting uppercase alphabets
		if (i.isupper()):
			u+=1		

		# counting digits
		if (i.isdigit()):
			d+=1		

		# counting the mentioned special characters
		if(i=='@'or i=='$' or i=='_'):
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")