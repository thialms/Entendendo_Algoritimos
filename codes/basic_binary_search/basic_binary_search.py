def binarySearch(arr, index):
    first = 0
    last = len(arr) - 1 
    while first <= last:
        mid = (first + last) // 2
        guess = arr[mid]
        if guess == index:
            return guess
        if guess > index:
            last = mid - 1
        else:
            first = mid + 1 
    return None
        
my_list = [1, 2, 3, 5, 7, 9, 10, 12, 15, 16, 25, 67]

print(binarySearch(my_list, 7))
print(binarySearch(my_list, 15))
print(binarySearch(my_list, 43))
            
