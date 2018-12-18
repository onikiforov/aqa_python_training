import random
import time


def get_current_timestamp():
    return int(time.time())


def get_random_priority():
    prio_min = 1
    prio_max = 5

    return random.randint(prio_min, prio_max)
