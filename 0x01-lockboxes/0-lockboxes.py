#!/usr/bin/env python3
"""function to check if all boxes can be opened"""


def canUnlockAll(boxes):
    my_set = {0}
    my_keys = boxes[0]
    
    while my_keys and len(my_set) < len(boxes):
        key = my_keys.pop()

        if key in my_set or key >= len(boxes):
            continue
        my_set.add(key)
        my_keys.extend(boxes[key])
        
    return len(my_set) == len(boxes)