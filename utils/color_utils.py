import random


def hex_to_rgb(hex_string):
    hex_string = hex_string.replace('#')
    red = int(hex_string[0:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)

    return red, green, blue


def complementing_rgb(rgb):
    m = min(rgb) + max(rgb)
    return tuple(m - v for v in rgb)


def random_rgb():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return r, g, b


def rgb_gradient(start_rgb, end_rgb, step_size):
    step_size = step_size - 2

    if step_size < 2:
        return [start_rgb, end_rgb]

    r1, g1, b1 = start_rgb
    r2, g2, b2 = end_rgb

    r_step = (r2 - r1) / step_size
    g_step = (g2 - g1) / step_size
    b_step = (b2 - b1) / step_size

    rgb_list = [start_rgb]

    for i in range(step_size + 1):
        r = round(r1 + r_step * i)
        g = round(g1 + g_step * i)
        b = round(b1 + b_step * i)
        rgb_list.append((r, g, b))

    return rgb_list
