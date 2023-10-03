#!/usr/bin/python3
"""function module"""


def canUnlockAll(boxes):
    """function to check if all boxes can be opened"""
    if boxes is None or len(boxes) == 0:
        return False
    # get number of boxes
    number_of_boxes = len(boxes)
    # initialize box switch to keep track of open boxes.
    # note that the box switch is of the same size as number of
    # boxes
    box_switch = [False] * number_of_boxes
    # initially the first box is open
    box_switch[0] = True

    # initialize an index stack to add keys in individual boxes.
    # remember the first box is open.
    # iterate through the boxes starting with the first box.
    # get the integers in each box - these are the keys.
    # check key_index against the corresponding box_switch value to check
    # if the box is open (True). If not, open it.
    # finally, push the key to the stack to open other boxes
    index_stack = [0]
    while index_stack:
        current_box_index = index_stack.pop()
        current_box = boxes[current_box_index]

        for key_index in current_box:
            if not box_switch[key_index]:
                box_switch[key_index] = True
                index_stack.append(key_index)

    return all(box_switch)
