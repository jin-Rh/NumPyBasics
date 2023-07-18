import numpy as np
import random


def count_bug_life():
    # steps are between 0 to 6 and -1, 7 steps means bug is dead
    walk = np.random.randint(0, 7)  # find initial step between 0 and 6
    i = 0
    alive = True
    while alive:
        walk += random.choice([-1, 1])  # select either 1 or -1 for walk
        i += 1
        if walk == -1 or walk == 7:
            alive = False

    return i


# list with all death steps count
bug_death = [count_bug_life() for n in range(100)]

print(f'Bug is dead in {bug_death} steps')