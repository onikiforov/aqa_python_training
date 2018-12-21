import random
import time


def get_current_timestamp():
    return int(time.time())


def get_random_priority():
    priority_min = 1
    priority_max = 5

    return random.randint(priority_min, priority_max)
