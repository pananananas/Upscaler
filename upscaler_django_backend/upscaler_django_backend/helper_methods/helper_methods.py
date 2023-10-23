import os

def clear_data_folders():
    # delete every item in folders:
    folder = [                              # TODO: Usuń foldery z listy, eby obrazy zapisywały się w bazie danych
              'images',                     #
              'images/output', 
              'images/enlargedLR', 
              'images/greyscaleSR', 
              'upscaled_images',            #
              'upscaled_images/bilinear',   #
              'upscaled_images/dwsr',       #   
              'upscaled_images/esrgan'      #
              ]
    
    for f in folder:
        for file in os.listdir(f):
            file_path = os.path.join(f, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)


def clear_helper_folders():
    folder = ['images/enlargedLR', 
              'images/greyscaleSR']
    # delete folders:
    for f in folder:
        for file in os.listdir(f):
            file_path = os.path.join(f, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)