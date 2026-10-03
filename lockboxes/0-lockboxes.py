#!/usr/bin/python3
"""Lockboxes: check whether all boxes can be opened."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes: list of lists, where boxes[i] holds the keys found in box i.

    Returns:
        True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = {0}
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if 0 <= new_key < n and new_key not in opened:
                opened.add(new_key)
                keys.append(new_key)

    return len(opened) == n
