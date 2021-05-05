def list_search(list, x):
  i = 0
  for n in list:
    if n == x:
      return i
    i += 1
  return False

list = [9, 1, 3, 7, 8, 5, 2, 6, 0, 4] 
print(list_search(list, 5))
print(list_search(list, 10))