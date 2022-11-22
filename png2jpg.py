# starting snippet from https://stackoverflow.com/a/43258974

import os

from PIL import Image



def main():
  for file in os.listdir('.'):
    if ".png" in file:
      with Image.open(file) as img:
        rbg = img.convert('RGB')
        lower = file.lower()
        no_spaces = lower.replace(' ', '')
        filename = no_spaces.split('.')[0]
        rbg.save(filename + ".jpg")

if __name__ == '__main__':
    main()
