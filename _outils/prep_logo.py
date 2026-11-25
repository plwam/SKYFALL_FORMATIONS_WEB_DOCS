from PIL import Image, ImageChops
src = r'D:\smarta\gesi formation\Logo-gesi_065336.png'
dst = r'D:\smarta\gesi formation\module-django-gesibiblio\images\logo-gesi.png'
im = Image.open(src).convert('RGB')
bg = Image.new('RGB', im.size, (255,255,255))
diff = ImageChops.difference(im, bg)
bbox = diff.getbbox()
print('taille source', im.size, 'bbox', bbox)
m = 18
box = (max(0,bbox[0]-m), max(0,bbox[1]-m), min(im.width,bbox[2]+m), min(im.height,bbox[3]+m))
im = im.crop(box)
im.save(dst, optimize=True)
print('taille finale', im.size)
