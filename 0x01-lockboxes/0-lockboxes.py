#!/usr/bin/python3
"""Scripts then will unlock list of lists"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked."""
    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    return len(keys) == len(boxes)
