a = [1, 7, 3, 4]
new_list = len(a) * [1] # take len of a and instantiate value of one to each index in the new array
# instantiate = alocate "whatever you are asking" to the memory
for i, _ in enumerate(a):
  for j, value in enumerate(a):
    if i == j:
      continue
    new_list[i] *= value


# This solution is O(n^2)
