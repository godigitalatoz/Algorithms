# MergeSort in Python

def mergeSort(array):
    if len(array) > 1:
        
        # r is the mid of array
        r = len (array)//2
        L = array[:r]
        M = array[r:]
        
        # Sort the two halves
        
        mergeSort (L)
        mergeSort (M)
        
        i = j = k = 0
        
        while i < len(L) and j < len (M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                
            else:
                array[k] = M[j]
                j += 1
            k += 1
            
        # when we run out of elements in L or M
        
        while i < len (L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len (M):
             array[k] = M[j]
             j += 1
             k += 1
             
# print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=", ")
    print()
    
# driver programe
if __name__ == '__main__':
    array_str = input("Enter a list seperated by spaces: ")
    array = list(map(int, array_str.split()))
    
    mergeSort(array)
    
    print("Sorted array is: ")
    printList(array)
