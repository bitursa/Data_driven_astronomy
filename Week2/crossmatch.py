# Write your crossmatch function here.
import numpy as np
def hms2dec(h,m,s):
    return (15 * (h + m/60 + s/(60 * 60)))

def dms2dec(d,m,s):
    if d > 0:
        dec = (d + m/60 + s/(60 * 60))
    else:
        dec = (-1*(-d + m/60 + s/(60 * 60)))
    return dec

def import_bss():
    cat = np.loadtxt('bss.dat', usecols=range(1, 7))
    converted_cat = np.zeros(shape=(cat.shape[0], 3))
    for j, i in enumerate(cat):
        right_ascension = hms2dec(i[0], i[1], i[2])
        declination = dms2dec(i[3], i[4], i[5])
        converted_cat[j] = j + 1, right_ascension, declination
    return list(map(tuple, converted_cat))

def import_super():
    cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=range(0, 2))
    converted_cat = np.zeros(shape=(cat.shape[0], 3))
    for j, i in enumerate(cat):
        right_ascension = i[0]
        declination = i[1]
        converted_cat[j] = j + 1, right_ascension, declination
    return list(map(tuple, converted_cat))


def angular_dist(r1, d1, r2, d2):
    d1 = np.radians(d1)
    d2 = np.radians(d2)
    r1 = np.radians(r1)
    r2 = np.radians(r2)
    b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2) ** 2
    a = np.sin(np.abs(d1 - d2) / 2) ** 2
    d = 2 * np.arcsin(np.sqrt(a + b))
    d = np.degrees(d)
    return d

def crossmatch(bss_cat, super_cat, max_dist):
        matches = []
        no_matches = []
        for id1, ra1, dec1 in bss_cat:
            closest_dist = np.inf
            closest_id2 = None
            for id2, ra2, dec2 in super_cat:
                dist = angular_dist(ra1, dec1, ra2, dec2)
                if dist < closest_dist:
                    closest_id2 = id2
                    closest_dist = dist
            # Ignore match if it's outside the maximum radius
            if closest_dist > max_dist:
                no_matches.append(id1)
            else:
                matches.append((id1, closest_id2, closest_dist))
        return matches, no_matches, time_taken
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

