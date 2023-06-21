import sys
from PIL import Image
sys.argv.pop(0)
for i in sys.argv:
        Image.open(str(i).split('\\')[len(str(i).split('\\')) - 1]).save(str(i).split('\\')[len(str(i).split('\\')) - 1].split('.')[0] + '.png')

