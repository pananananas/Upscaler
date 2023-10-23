import os

def clear_output_folders():
    # delete every item in folders:
    folder = ['images', 'images/output', 'images/enlargedLR', 'images/greyscaleSR']
    for f in folder:
        for file in os.listdir(f):
            file_path = os.path.join(f, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)