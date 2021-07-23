import os
import random
from random import sample
import glob

while True:
    dir_name = input("Please, enter the folder path here :  ")  # User's path input
    found_files = glob.glob(os.path.join(dir_name, '**'))  # list all the files
    isDirectory = os.path.isdir(dir_name)  # return bool from user's path input

    if not isDirectory:  # Condition to check if the dir is invalid
        print('Invalid Path......>> Insert a new Path, please')

    elif len(found_files) == 1 or len(found_files) == 0:  # condition to check if folder has 1 or 0 files
        print('Folder has only one file or empty')

    elif len(found_files) % 2 == 0:   # condition to check if sum of files is even
        files_random = random.sample(found_files, (len(found_files)) // 2)  # Choice half of the universe randomly
        for i in files_random:   # loop over the files chosen randomly to remove
            os.remove(i)
        print('Your order has been completed')
        ask = input('Would you like to perform other order (y/n)?: ')   # ask user if want to redo the order again
        if ask.lower() == 'y':
            continue
        else:
            break

    elif len(found_files) % 2 != 0:  # condition to check if sum of files is odd
        files_random = random.sample(found_files, (len(found_files) - 1) // 2)  # choice(half of the universe-1)randomly
        for i in files_random:   # loop over the files chosen randomly to remove
            os.remove(i)
        print('Your order has completed')
        ask = input('Would you like to perform another order (y/n)?: ')    # ask user if want to redo the order again
        if ask.lower() == 'y':
            continue
        else:
            break
