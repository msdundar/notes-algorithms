# encoding: UTF-8

def binary_search(array, item)
  # positions to search
  minimum = 0
  maximum = array.length - 1

  while minimum <= maximum
    middle = (minimum + maximum) / 2
    guess = array[middle]

    if guess == item
      return item
    elsif guess > item
      maximum = middle - 1
    else
      minimum = middle + 1
    end
  end

  return "Not found!"
end

list = [10, 20, 23, 24, 30, 35, 80, 85, 86, 87, 100]
puts binary_search(list, 35)
