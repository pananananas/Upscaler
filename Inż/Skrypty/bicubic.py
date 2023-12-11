from PIL import Image

def bicubic_interpolation(image_path, scale_factor):
    """
    Perform bicubic interpolation on an image with a specified scale factor.

    :param image_path: Path to the input image.
    :param scale_factor: The factor by which the image will be scaled.
    :return: Scaled image.
    """
    # Open the image
    img = Image.open(image_path)

    # Calculate new size
    new_width = int(img.width * scale_factor)
    new_height = int(img.height * scale_factor)

    # Resize the image using bicubic interpolation
    resized_img = img.resize((new_width, new_height), Image.BICUBIC)

    # Save the resized image
    resized_img.save("resized_image.png")

    return resized_img

# Example usage
bicubic_interpolation("comic.png", 4)


