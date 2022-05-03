from PIL import Image
from IPython.display import display
import numpy as np

im = Image.open('chris.tiff')
im1 = Image.open('vera.tif')
display(im)
display(im1)
arraim = np.array(im)
arraim1 = np.array(im1)
print(arraim)
print(arraim1)

mask = np.full(arraim.shape, 255)
mask1 = np.full(arraim1.shape, 255)
print(mask)
print(mask1)

modified_array = arraim1 - mask1
modified_array = modified_array * -1
modified_array = modified_array.astype(np.uint8)
print(modified_array)
display(Image.fromarray(modified_array))

reshaped = np.reshape(modified_array, (847, 1275))
print(reshaped.shape)
display(Image.fromarray(reshaped).show())
