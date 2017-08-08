from astropy.io import fits
import numpy as np


def load_fits(file):
    hdulist = fits.open(file)
    data = hdulist[0].data
    arg = np.argmax(data)
    row = hdulist[0].header['NAXIS1']

    a = arg / row
    b = arg % row

    return a, b


if __name__ == '__main__':
    bright = load_fits('20170719_1611323.00flat.fits')

    print(bright)
