import os
import re
from PIL import Image
import argparse



def resize(root, file, new_width, new_img_name):
    original_img_paht = os.path.join(root, file)
    new_img_path = os.path.join(root, new_img_name)

    img_pillow = Image.open(original_img_paht)
    width, height = img_pillow.size

    new_height = round((new_width * height) / width)

    new_img = img_pillow.resize((new_width, new_height), Image.LANCZOS)
    
    new_img.save(new_img_path, optimize=True, quality=80, exif=img_pillow.info.get('exif'))

    print(f'imagem salva em {new_img_path}')
    


def is_image(extension):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))


def file_check(root, file):
    filename, extension = os.path.splitext(file)
    if not is_image(extension):
        return

    flag = '_new'

    if flag in file:
        return

    new_img_name = filename + flag + extension

    resize(root=root, file=file, new_width=720, new_img_name=new_img_name)


def files_loop(root, files):
    for file in files:
        file_check(root, file)


def  main(root_path):
    for root, dirs, files in os.walk(root_path):
        files_loop(root, files)
        
            
        


if __name__ == '__main__':
    root_path = '/Users/renatomota/Desktop/testafoto'
    main(root_path)
