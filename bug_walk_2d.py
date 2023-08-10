import numpy as np
import random

def count_bug_life_2d():
    walk_x = np.random.randint(0, 7)
    walk_y = np.random.randint(0, 7)
    # initial random place
    walk = np.array([walk_x, walk_y])
    alive = True
    i = 0
    while alive:
        # random 1 step in each direction
        choice = random.choice(np.array([[0, 1], [0, -1], [1, 0], [-1, 0]]))
        walk = np.sum([walk, choice], axis=0)
        i += 1
        # die when it reaches on the edge of island
        if walk[0] == -1 or walk[0] == 7 or walk[1] == -1 or walk[1] == 7:
            alive = False
    return i


# Testing the function
bug_deaths = (count_bug_life_2d() for _ in range(20))

for k, v in enumerate(bug_deaths):
    print(f'Bug in the 2D island is dead in {v} steps')
