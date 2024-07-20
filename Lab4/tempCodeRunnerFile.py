def find(start, end, val, list):
    while start <= end:
        mid = (start + end) // 2
        if val == list[mid]:
            return mid
        elif val > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.")

#recursive method
""" def find(start, end, val, list):
    if start > end:
        return -1
    mid = (start + end) // 2
    if val == list[mid]:
        return mid
    elif val > list[mid]:
        return find(mid + 1, end, val, list)
    else:
        return find(start, mid - 1, val, list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.") """

print("===============================================================================")
