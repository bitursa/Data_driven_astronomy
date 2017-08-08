# Write your find_closest function here
import numpy as np
def hms2dec(h, m, s):
    return (15 * (h + m / 60 + s / (60 * 60)))

def dms2dec(d, m, s):
    if d > 0:
        dec = (d + m / 60 + s / (60 * 60))
    else:
        dec = (-1 * (-d + m / 60 + s / (60 * 60)))
    return dec

def import_bss():
    cat = np.loadtxt('bss.dat', usecols=range(1, 7))
    converted_cat = np.zeros(shape=(cat.shape[0], 3))
    for j, i in enumerate(cat):
        right_ascension = hms2dec(i[0], i[1], i[2])
        declination = dms2dec(i[3], i[4], i[5])
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

def find_closest(cat, ra, dec):
    min_id = None
    min_dist = np.inf
    for src in cat:
        if min_dist > angular_dist(ra, dec, src[1], src[2]):
            min_dist = angular_dist(ra, dec, src[1], src[2])
            min_id = src[0]
    return (min_id, min_dist)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    cat = import_bss()

    # First example from the question
    print(find_closest(cat, 175.3, -32.5))

    # Second example in the question
    print(find_closest(cat, 32.2, 40.7))

