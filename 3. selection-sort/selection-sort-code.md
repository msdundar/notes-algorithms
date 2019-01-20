# Selection Sort

## Python

```python
# python3

def find_smallest(array):
  smallest = array[0]
  smallest_index = 0

  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest = array[i]
      smallest_index = i
  return smallest_index

def selection_sort(array):
  ordered_list = []

  for i in range(len(array)):
    smallest = find_smallest(array)
    ordered_list.append(array.pop(smallest))
  return ordered_list

list = [10, 1, 20, 23, 24, 100, 30, 35, 80, 85, 86, 87, 100, 0]

print(selection_sort(list))
```

## Ruby

```ruby
# encoding: UTF-8

def find_smallest(array)
  smallest = array[0]
  smallest_index = 0

  for i in (1..(array.length - 1))
    if array[i] < smallest
      smallest = array[i]
      smallest_index = i
    end
  end

  return smallest_index
end

def selection_sort(array)
  ordered_list = []

  array.length.times do
    smallest = find_smallest(array)
    ordered_list << array[smallest]
    array.delete_at(smallest)
  end

  print ordered_list
end

list = [10, 1, 20, 23, 24, 100, 30, 35, 80, 85, 86, 87, 100, 0]

puts selection_sort(list)
```
