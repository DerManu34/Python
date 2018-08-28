# from PIL import Image
# import pytesseract
# image = Image.open('beispielbild.jpg') 
# # Open image object using PIL print 
# image_to_string(image) 
# # Run tesseract.exe on image fnord print 
# image_file_to_string('beispielbild.jpg')


from pytesseract import image_to_string
from PIL import Image

im = Image.open(r'beispielbild.jpg')
print(im)

print(image_to_string(im))