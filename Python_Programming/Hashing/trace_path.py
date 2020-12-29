def trace_path(dict_path):
    not_in_items = []
    results = []
    count = 1
    for from_city, to_city in dict_path.items():
        connection = True
        while connection:
            if count > len(dict_path):
                break
            if to_city in dict_path:
                results.append([from_city, to_city])
                from_city = to_city
                to_city = dict_path[to_city]
            else:
                not_in_items.append([from_city, to_city])
                connection = False
            count += 1
    results.append(not_in_items.pop())
    return results


dict = {
    "NewYork": "Chicago",
    "Boston": "Texas",
    "Missouri": "NewYork",
    "Texas": "Missouri"
}

print(trace_path(dict))
