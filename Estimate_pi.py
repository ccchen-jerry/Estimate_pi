# %%
import random


def estimate_pi(num_points):
    points_in_circle = 0
    points_of_total = 0

    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            points_in_circle += 1
        points_of_total += 1

    return 4 * points_in_circle/points_of_total


# %%
estimate_pi(100)
# %%
estimate_pi(10000)

# %%
estimate_pi(1000000)

# %%
estimate_pi(10000000)
# %%
