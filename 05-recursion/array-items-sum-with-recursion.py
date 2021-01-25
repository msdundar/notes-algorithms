# python3

def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])

list = [1, 2, 3, 4, 5]

print(sum(list))
