#!/usr/bin/python3
"""
This module contains the canUnlockAll function
which determines if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List where each element is a list of keys
                                    inside that box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = boxes[0]  # Start with the keys from the first box

    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])  # Add keys from the newly unlocked box

    # Iterate to ensure all reachable boxes are unlocked
    for i in range(1, len(boxes)):
        if not unlocked[i]:
            return False
    return True
