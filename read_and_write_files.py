import os

check_file = True
path_to_file = 'secrets.txt'

while check_file:
    file_exists = os.path.exists(path_to_file)
    if file_exists:
        print("File exists in given path!")

        # Open file in read and append mode
        my_file = open(path_to_file, 'r+')
        for line in my_file:
            print(line)

        my_file.write('This file has been read!')    
        my_file.close()

        check_file = False
