numbers = [1,2,3,4,5,6,7,8,9]

count_even = 0
count_odd = 0

for i in numbers:
  if i % 2 == 0:
    count_even += 1
  else:
    count_odd += 1

print(f"{count_odd} Odd Numbers.")
print(f"{count_even} Even Numbers.")

count_even = [i for i in numbers if i%2==0]
count_odd = [i for i in numbers if i%2!=0]

print(f"{count_even} Even Numbers ",len(count_even))
print(f"{count_odd} Odd Numbers ",len(count_odd))