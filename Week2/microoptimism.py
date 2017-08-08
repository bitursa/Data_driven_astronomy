# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
    b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2) ** 2
    a = np.sin(np.abs(d1 - d2) / 2) ** 2
    d = 2 * np.arcsin(np.sqrt(a + b))
    d = np.degrees(d)
    return d

def crossmatch(cat1, cat2, max_dist):
        new_cat1 = []
        new_cat2 = []
        matches = []
        no_matches = []
        for i, x in enumerate(cat1):
            new_RA = np.radians(x[0])
            new_Dec = np.radians(x[1])
            new_cat1.append((i, new_RA, new_Dec))

        for j, y in enumerate(cat2):
            new_RA_cat2 = np.radians(y[0])
            new_Dec_cat2 = np.radians(y[1])
            new_cat2.append((j, new_RA_cat2, new_Dec_cat2))

        start = time.perf_counter()
        for id1, ra1, dec1 in new_cat1:
            closest_dist = np.inf
            closest_id2 = None
            for id2, ra2, dec2 in new_cat2:
                dist = angular_dist(ra1, dec1, ra2, dec2)
                if dist < closest_dist:
                    closest_id2 = id2
                    closest_dist = dist

            if closest_dist > max_dist:
                no_matches.append(id1)
            else:
                matches.append((id1, closest_id2, closest_dist))
        time_taken = time.perf_counter() - start
        return matches, no_matches, time_taken



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
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 15)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

