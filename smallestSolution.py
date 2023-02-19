def smallest(array):
    i = len(array) -1 
    j = len(array) - 2

    soln(array, i , j)



def soln(array, i , j):
# this will run at least the length of the array 
    for k in range(len(array)):
        if(j < 0 or i < 0):
            i = len(array) - 1
            j = len(array) - 2
            break
        if(array[i] > array[j]):
            array[i] = array[i] - array[j]
        j = j -1 # 
    i = i- 1

    soln(array, i , j)
    

array1 =  [6, 9 ,21]
smallest(array1)