def unique_elements(lst):
    unique = []
    for element in lst:
        if isinstance(element, list):
            for n in unique_elements(element):
                if n not in unique:
                    unique.append(n)
        else:
            if element not in unique:
                unique.append(element)

    return unique
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))