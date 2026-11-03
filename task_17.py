def merge_dicts(dict1, dict2):
    for key in dict2:
        if key not in dict1:
            dict1[key] = dict2[key]
        else:
            if type(dict2[key]) == dict and type(dict1[key]) == dict:
                merge_dicts(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print(dict_a)
print(dict_b)
merge_dicts(dict_a, dict_b)
print(f"Слияние: {dict_a}")