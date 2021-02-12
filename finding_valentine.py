import glob
import imagehash
from PIL import Image

my_img_url = './me.jpg'
my_hash = imagehash.average_hash(Image.open(my_img_url))

girls_images = glob.glob('./girls/*.jpg')
selected = girls_images[0]
accepted_variance = 1000
for girl in girls_images:
    girl_hash = imagehash.average_hash(Image.open(girl))
    variance = girl_hash - my_hash
    if variance < accepted_variance:
        selected = girl
        accepted_variance = variance

bf_img = Image.open(my_img_url)
gf_img = Image.open(selected)
couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
couple_img.paste(bf_img, (0, 0))
couple_img.paste(gf_img, (bf_img.width, 0))
couple_img.save('my_valentine.jpg')
couple_img.show()