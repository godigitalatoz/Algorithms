# quick sort in python

def partition (array, l, h):
  pivot = array [l]
  i = l
  j = h
  
  while (i < j):
    while i < h and array [i] <= pivot:
      i += 1
      
    while array [j] > pivot:
      j -= 1
      
    if (i < j):
      array [i], array [j] = array [j], array [i]
      
  array [l], array [j] = array [j], array [l]
  return j
  
def quickSort (array, l, h):
  if (l < h):
    j = partition (array, l, h)
    quickSort (array, l, j)
    quickSort (array, j + 1, h)


array = [10, 4, 5, 7, 3, 2, 1, 9]  

quickSort (array, 0, len(array) - 1)

print (array) 

   
