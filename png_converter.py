import os, sys
from PIL import Image

parent_dir = './'

given = sys.argv[1]
new = sys.argv[2]

if not os.path.isdir(given):
    print('There is no such directory exists.')
elif given == new:
        print('Two directories share same name.')
else:
    if not os.path.isdir(new):
        os.mkdir(new)
    for img in os.listdir(given):
        if (img.endswith('.jpeg')) or (img.endswith('.jpg')):
            clean_name = os.path.splitext(img)[0]

            i = Image.open(f'{given}/{img}')
            if os.path.isfile(f'{new}/{clean_name}.png'):
                continue

            i.save(f'{new}/{clean_name}.png', 'png')

    print('All done successfully!')