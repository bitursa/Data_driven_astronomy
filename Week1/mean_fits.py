import numpy as np
from astropy.io import fits

def mean_fits(filenames):
    res = np.zeros([200,200])
    for filename in filenames:
        hdulist = fits.open(filename)
        data = np.array(hdulist[0].data)
        res += data
    mean = res/len(filenames)
    return mean
if __name__ == '__main__':

    # Test your function with examples from the question
    data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])

    # You can also plot the result:
 #   import matplotlib.pyplot as plt
  #  plt.imshow(data, cmap=plt.cm.viridis)
  #  plt.colorbar()
  #  plt.show()