def hex_to_rgb(hex_string):
    hex_string = hex_string.replace('#')
    red = int(hex_string[0:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)

    return red, green, blue


def complementing_rgb(rgb):
    m = min(rgb) + max(rgb)
    return tuple(m - v for v in rgb)
