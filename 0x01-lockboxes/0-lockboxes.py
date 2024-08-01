#!/usr/bin/python3
"""
LockBoxes module
"""


def canUnlockAll(boxes):
    """ Check if boxes can be open or not
        Args:
            boxes (list of list): have one or more keys
        Return:
            True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    unlockStatus = {x: True if not x else False for x in range(len(boxes))}
    for box in boxes:
        viableKeys = list(filter(lambda x: all([x > 0, x < len(boxes),
                                                x != boxes.index(box)]), box))
        unlockStatus.update({x: True for x in viableKeys})
    return all(unlockStatus.values())
