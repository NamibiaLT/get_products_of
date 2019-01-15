def get_products_of_all_ints_except_at_index(int_list):
  sample_input = [1, 7, 3, 4]
  sample_output =   [84, 12, 28, 21]

  products_of_all_integers_after_index = [None] * len(int_list)

  products_so_far = 1
  for i in range(len(int_list) - 1, -1, -1):
    products_of_all_integers_after_index[i] = products_so_far
    products_so_far *= int_list[i]

  return products_of_all_integers_after_index

print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))

# This solution is O(n)
