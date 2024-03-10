lst = [1,3,5,2,1,2,6,3,2]
def count_items(lst):
  # Base case: if the list is empty, there are no items to count
  if not lst:
    return 0
  # Recursive case: the number of items in the list is 1 plus the number of items in the rest of the list
  else:
    return 1 + count_items(lst[1:])


print(count_items(lst))