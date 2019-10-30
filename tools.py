from PIL import Image
import numpy as np

def save_image(X_final, name, nb_colors):
    im = Image.fromarray((X_final * 255).astype(np.uint8))
    name = name.split(".")[0]
    file_name = name + "_" + str(nb_colors) + ".jpeg"
    im.save(file_name)
    return file_name


def usage():
    print("Usage :\npython main.py [image_file] [number_of_colors](optional, 16 by default)")