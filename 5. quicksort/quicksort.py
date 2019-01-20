# python3

def quicksort(array):
  less = []
  greater = []

  if len(array) < 2:
    return array # base case
  else:
    pivot = array[0] # pick a pivot
    for i in array[1:]:
      if i <= pivot:
        less.append(i)
      else:
        greater.append(i)
      
    return quicksort(less) + [pivot] + quicksort(greater)

list = [10, 5, 20, 13, 99, 24, 80, 30, 35, 80, 85, 86, 87, 100]

print(quicksort(list))