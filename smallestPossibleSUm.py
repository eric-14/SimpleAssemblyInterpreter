def solution(array):
    
    if(len(array) == 1):
        return array[0]

    while True:
        array.sort()
        if(array[0] == 1):
            return len(array)

        if(array[-1] == array[0]):
            return array[0] * len(array)


        for index, x in enumerate(array):
            result = x % array[0]
            #print("line 5 ", result)
            if(result != 0 ):
                array[index] = result
            else:
                array[index] = array[0]
    print("line 7", array)

array1 = [1, 21, 55]


print("the solution is ",solution(array1))