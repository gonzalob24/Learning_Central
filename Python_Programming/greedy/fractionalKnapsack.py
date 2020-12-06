import math
import collections


def fractionalKnapsack(listObejct, maxWeight):
    # iterate listObject and add a density value to each object
    for item in listObejct:
        # storing density increases space complexity
        item["density"] = item["value"] / item["weight"]

    sortedListObject = sorted(listObejct, key=lambda d: d["density"])[::-1]

    totalvalue = 0
    for item in sortedListObject:
        if item["weight"] < maxWeight:
            totalvalue += item["value"]
        if item["weight"] > maxWeight:
            totalvalue += ((maxWeight / item["weight"]) * item["value"])
            break
        maxWeight -= item["weight"]
    return totalvalue


obj = [{"name": "item1", "weight": 6, "value": 6},
       {"name": "item2", "weight": 10, "value": 2},
       {"name": "item3", "weight": 3, "value": 1},
       {"name": "item4", "weight": 5, "value": 8},
       {"name": "item5", "weight": 1, "value": 3},
       {"name": "item6", "weight": 3, "value": 5}
       ]

print(fractionalKnapsack(obj, 10))
