
# [-2, -1, 0, 2, 3]

def square(arr):

    j = 0
    i = 0

    while arr[j] < 0:
        j += 1

    pos_start = j
    res = []

    while i < pos_start or j < len(arr):

        if arr[i]*arr[i] < arr[j]* arr[j]:
            res.append(arr[i]*arr[i])
            i += 1
        
        else:
            res.append(arr[j]* arr[j])
            j += 1
    
    while j < len(arr):
        res.append(arr[j]* arr[j])
        j += 1
    
    while i < pos_start:
        res.append(arr[i]*arr[i])
        i += 1
    
    return res


print(square([-2, -1, 0, 2, 3]))
    