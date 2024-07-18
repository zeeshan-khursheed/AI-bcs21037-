print("Enter lines of text (press Enter on an empty line to terminate):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

print("\nYou entered:")
for line in lines:
    print(line)
