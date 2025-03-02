def all_elements_true(tuple_data):
    return all(tuple_data)

tuple_data = (True, True, True, True)
if all_elements_true(tuple_data):
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")