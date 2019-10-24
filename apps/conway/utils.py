def load_pattern(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        pattern = {}

        for y, line in enumerate(lines):
            for x, character in enumerate(line):
                if character in ['.', 'O']:
                    pattern[(x, y)] = 0 if character == '.' else 1

        return pattern


def print_grid(size, grid):
    width, height = size

    for y in range(height):
        row = ''
        for x in range(width):
            row += f'{grid[(x, y)]} '

        print(row)
    print()
