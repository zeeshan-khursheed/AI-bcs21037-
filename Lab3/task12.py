nums = list(input("Please enter a 4 digit number made from 0 and 1 : ").split(','))
# example: 0101,1000,1001,1010

res = [num for num in nums if not int(num, 2) % 5]

print(res)