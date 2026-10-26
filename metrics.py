import numpy as np

def calculate (original, new):
    bombs = original.sum()
    bombs_detected = new.sum()
    percentage = bombs_detected/bombs

    return bombs, bombs_detected, percentage

