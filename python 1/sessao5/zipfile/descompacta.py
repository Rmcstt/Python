
from zipfile import ZipFile
import os

with ZipFile('/Users/renatomota/Desktop/test.zip', 'r') as zip:
    zip.extractall('/Users/renatomota/Desktop/descompactado')
  