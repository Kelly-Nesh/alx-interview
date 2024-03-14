#!/usr/bin/python3
"""Lockboxes alx interview prep"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    # Iterate over each box in the list
    for i, box in enumerate(boxes):
        # If the current box is empty, check if the next box can be unlocked
        if not box:
            if canUnlockAll(boxes[i + 1:]):
                return True

        # Check if the current box contains any keys that can unlock other boxes
        for key in box:
            # Check if there is a box with the same number as the key
            if key in boxes and canUnlockAll([box for box in boxes if box!= key]):
                return True

    # If no keys were found, return False
    return False