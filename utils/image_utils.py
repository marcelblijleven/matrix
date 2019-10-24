from PIL import Image

ANTIALIAS = Image.ANTIALIAS

def create_image(size, background=(0, 0, 0), mode='RGB'):
    return Image.new(mode, size, background)


def open_image(file, mode='r'):
    return Image.open(file, mode)


def get_pixels(image):
    return image.load()


def save_frames(frames, file, duration=1000, loop=0, optimize=False):
    first_frame = frames[0]
    first_frame.save(
        file,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
        optimize=optimize
    )
