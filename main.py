from PIL import Image

base_image = input('ベースとなる画像パスを指定してください')
icon_path = '/Users/nishiki/Documents/Personal Dev/py-image-edit/nh.jpeg'
icon = Image.open(icon_path).copy()
w,h=icon.size

print(w)
print(h)

icon = icon.resize(size=(252, 252), resample=Image.ANTIALIAS)