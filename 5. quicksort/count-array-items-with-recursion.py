# python3

def count(list):
  if list == []:
    return 0
  return 1 + count(list[1:])

list = [1, 2, 3, 4, 5]

print(count(list))
