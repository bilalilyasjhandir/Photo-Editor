from PIL import Image, ImageEnhance, ImageFilter
import os

pathIn = './images'
pathOut = './editedImages'

for filename in os.listdir(pathIn):
    img = Image.open(f"{pathIn}/{filename}")
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    cleanName = os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{cleanName}_edited.jpg")