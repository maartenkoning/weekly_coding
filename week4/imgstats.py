# Import statistics Library
from sklearn import preprocessing
import numpy as np
from PIL import Image, ImageMath, ImageStat, ImageChops
import matplotlib.pyplot as plt


im = Image.open("test1.jpg")
mask = Image.open("raw1.jpg")
#mask = ImageChops.invert(mask)

# The file format of the source file.
print(mask.format) # Output: JPEG

# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
print(mask.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(mask.size) # Output: (1920, 1280)

# Colour palette table, if any.
#print(im.palette) # Output: None

im = ImageChops.subtract(im, mask.convert("RGB"))
r, g, b = im.split()

#g = g.point(lambda i: i > 10 and 255)

#normalize
r = preprocessing.normalize(r) * 255
g = preprocessing.normalize(g) * 255
b = preprocessing.normalize(b) * 255

m = preprocessing.normalize(mask) * 255
print (m.size)
data_filter = m > 2

m = m[data_filter]
print (m.size)

data_filter = m < 255

m = m[data_filter]
#print (m.size)




#print (r)

#img = Image.merge("RGB", (r, b, g))
#img.save("out.jpg")
im.save("out.jpg")

out = ImageStat.Stat(im)

#filter out null values
# select regions where red is 126
#mask = r.point(lambda i: i == 126 and 255)
#mask.convert("RGB").save("mask.jpg")
#im.paste(im, (0, 0), mask)
#im.convert("RGB").save("out.jpg")
#r, g, b = im.split()
bins = list(range(20,50))

data_r, bo = np.histogram(r, bins)
data_g, bo = np.histogram(g, bins)
data_b, bo = np.histogram(b, bins)

#bins = list(range(255))
#bins = 10
data_m, bo = np.histogram(m, bins)

print (data_m)

#plt.plot(bins, data_r, 'r')
#plt.plot(bins, data_g, 'g')
#plt.plot(bins, data_b, 'b')
plt.hist(m, bins)
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.title("test")
plt.grid(True)
plt.savefig("im_histogram_01.jpg")
print(out.mean)
