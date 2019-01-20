# Quicksort

## Python

```python
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
```

## Ruby

```ruby
# encoding: UTF-8

def quicksort(array)
  less = []
  greater = []

  if array.length < 2
    return array
  else
    pivot = array[0]

    array[1..-1].each do |i|
      if i <= pivot
        less << i
      else
        greater << i
      end
    end

    return quicksort(less) + [pivot] + quicksort(greater)
  end
end

list = [10, 5, 20, 13, 99, 24, 80, 30, 35, 80, 85, 86, 87, 100]

print quicksort(list)
```
