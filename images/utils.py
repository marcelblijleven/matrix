from PIL import Image


def create_image(size, background=(0, 0, 0), mode='RGB'):
    return Image.new(mode, size, background)


def get_pixels(image):
    return image.load()
