# Write your crossmatch function here.
import numpy as np
import time


def angular_dist(r1, d1, r2, d2):
    b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2) ** 2
    a = np.sin(np.abs(d1 - d2) / 2) ** 2
    d = 2 * np.arcsin(np.sqrt(a + b))
    return d


# return angular_dist in degrees
def crossmatch(cat1, cat2, max_rad):
    start = time.perf_counter()
    unmatched = []
    matches = []

    max_rad = np.radians(max_rad)
    for i, x in enumerate(cat1):
        ra1 = np.radians(x[0])
        d1 = np.radians(x[1])

        ra2s = np.radians(cat2[:, 0])
        d2s = np.radians(cat2[:, 1])
        dists = angular_dist(ra1, d1, ra2s, d2s)
        min_id = np.argmin(dists)
        min_dist = dists[min_id]

        if min_dist > max_rad:
            unmatched.append(i)
        else:
            matches.append((i, min_id, np.degrees(min_dist)))

    time_taken = time.perf_counter() - start
    return matches, unmatched, time_taken


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # The example in the question
    cat1 = np.array([[180, 30], [45, 10], [300, -45]])
    cat2 = np.array([[180, 32], [55, 10], [302, -44]])
    matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
    print('matches:', matches)
    print('unmatched:', no_matches)
    print('time taken:', time_taken)


    # A function to create a random catalogue of size n
    def create_cat(n):
        ras = np.random.uniform(0, 360, size=(n, 1))
        decs = np.random.uniform(-90, 90, size=(n, 1))
        return np.hstack((ras, decs))


    # Test your function on random inputs
    np.random.seed(0)
    cat1 = create_cat(10)
    cat2 = create_cat(20)
    matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
    print('matches:', matches)
    print('unmatched:', no_matches)
    print('time taken:', time_taken)

