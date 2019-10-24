import sys
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from utils.color_utils import (
    random_rgb, complementing_rgb, rgb_gradient
)
from utils.image_utils import (
    create_image, get_pixels, open_image, ANTIALIAS
)


class Visualizer:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        columns, rows = grid_size

        options = RGBMatrixOptions
        options.rows = rows
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        self.matrix = RGBMatrix(options=options)

    def show_image(self, file):
        image = open_image(file)

        image_width, image_height = image.size

        # Resize if needed
        if (image_width != self.matrix.width
                or image_height != self.matrix.height):
            image.thumbnail(
                (self.matrix.width, self.matrix.height), ANTIALIAS
            )

        # Convert image to RGB
        image.convert('RGB')

        # Set image
        self.matrix.SetImage(image)

        try:
            print("Press CTRL-C to stop.")
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            sys.exit(0)

    def show_random_complementary(self):
        # Create simple image to reduce complexity when drawing pixels
        image = create_image((2, 1))

        color_a = random_rgb()
        color_b = complementing_rgb(color_a)

        pixels = get_pixels(image)
        pixels[0, 0] = color_a
        pixels[1, 0] = color_b

        # Resize to matrix
        image = image.resize((self.matrix.width, self.matrix.height))
        self.matrix.SetImage(image)

    def show_random_gradient(self):
        # Create simple image to set gradient
        image = create_image((1, self.matrix.height))
        color_a = random_rgb()
        color_b = complementing_rgb(color_a)

        rgb_list = rgb_gradient(color_a, color_b, self.matrix.height)
        pixels = get_pixels(image)

        for i in range(self.matrix.height):
            pixels[0, i] = rgb_list[i]

        # Resize to matrix
        image = image.resize((self.matrix.width, self.matrix.height))
        self.matrix.SetImage(image)
