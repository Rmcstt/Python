import os
from PIL import Image


def main(main_images_folder):
  if not os.path.isdir(main_images_folder):
    raise NotADirectoryError(f'{main_images_folder} nao existe.')

  for root, dirs, files in os.walk(main_images_folder):
    for file in files:
      file_full_path = os.path.join(root, file)
      file_name, extension = os.path.splitext(file)
      new_file = 'new_' + file_name + extension
      new_file_full_path = os.path.join(root, new_file)
      
      if 'new_' in file_full_path:
        continue

      img_pillow = Image.open(file_full_path)
      width, height = img_pillow.size
      print(f'width: {width}, height: {height}')

      img_pillow.close()

if __name__ == '__main__':
  main_images_folder = '/Users/renatomota/Desktop/testafoto'
  main(main_images_folder)