# import required libraries
import os
import sys
from PIL import Image
import glob

# first argument for folder, second for quality
#folder = sys.argv[1]
#quality = sys.argv[2]
folder = '/home/harti/Pictures/2021/p03/'
quality = 10

# TODO auto-adjust quality to get total size of 10MB

# compression function
def comp(file, verbose=False):


    # open the image
    picture = Image.open(file)
    file_split = (file.split('/'))

    # compress image
    picture.save(folder + "c_" + file_split[-1],
                 "JPEG",
                 optimize=True,
                 quality=quality)
    return

# Define a main function
def main():
    # only use following formats
    formats = ('*.jpg', '*.jpeg', '*.JPG', '*.JPEG')
    # create list with all image files
    files = []
    for f in formats:
        files = files + glob.glob(folder + f)

    # total number of files
    num = len(files)
    # compress files
    i = 0
    for file in files:
        #print('compressing', file)
        comp(file)
        i+=1
        print('processing ' + str(i) +'/' + str(num))

        # TODO add progress bar

    print("Done")


# Driver code
if __name__ == "__main__":
    main()
