# Write your import_bss function here.
# Write your import_bss function here.
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

def import_super():
    cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=range(0, 2))
    converted_cat = np.zeros(shape=(cat.shape[0], 3))
    for j, i in enumerate(cat):
        right_ascension = i[0]
        declination = i[1]
        converted_cat[j] = j + 1, right_ascension, declination
    return list(map(tuple, converted_cat))


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Output of the import_bss and import_super functions
    bss_cat = import_bss()
    super_cat = import_super()
    print(bss_cat)
    print(super_cat)
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Output of the import_bss and import_super functions
    bss_cat = import_bss()
    super_cat = import_super()
    print(bss_cat)
    print(super_cat)