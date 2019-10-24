from utils.image_utils import create_image, get_pixels


class Conway:
    def __init__(self, size, generations):
        self.size = size
        self.generations = generations
        self.population_size = int((max(size) / 3))

    def create(self):
        frames = []
        grid = self.create_grid()

        for generation in range(self.generations):
            print('Generation', generation)
            image = create_image(
                size=self.size,
                background=(0, 0, 0, 0),
                mode='RGBA'
            )

            pixels = get_pixels(image)
            next_generation = grid.copy()
            assert list(next_generation.values()).count(None) == 0

            for cell in grid:
                neighbours = self.get_neighbours(cell, grid)
                neighbour_values = [
                    grid[neighbour] for neighbour in neighbours
                ]

                next_state = self.determine_next_state(
                    grid, cell, neighbour_values
                )

                next_generation[cell] = next_state

                if next_state == 1:
                    pixels[cell] = (50, 169, 105, 0)

            grid = next_generation

            frames.append(image)

        return frames

    def create_grid(self, populate=True):
        grid = {}
        width, height = self.size

        for row in range(width):
            for column in range(height):
                grid[(row, column)] = 0

        if populate:
            grid = self.populate_grid(grid)

        return grid

    def populate_grid(self, grid):
        glider = {
            (0, 0): 0, (1, 0): 1, (2, 0): 0,
            (0, 1): 0, (1, 1): 1, (2, 1): 1,
            (0, 2): 1, (1, 2): 1, (2, 2): 1,
        }

        if self.size == (3, 3):
            return glider

        width, height = self.size

        for position in glider:
            x, y = position
            new_x = int(x + (width - 3) / 2)
            new_y = int(y + (height - 3) / 2)
            grid[new_x, new_y] = glider[position]
            print(x + (width - 3) / 2, y + (height - 3) / 2)

        return grid

    @staticmethod
    def get_neighbours(cell, grid):
        x, y = cell

        neighbours = []
        offsets = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (-1, -1), (1, 0), (1, 1)
        ]

        for offset in offsets:
            offset_x, offset_y = offset
            neighbour = x + offset_x, y + offset_y

            if neighbour in grid:
                neighbours.append(neighbour)

        return neighbours

    @staticmethod
    def determine_next_state(grid, cell, neighbour_values):
        # Birth: dead cell is adjacent to exactly 3 live cells
        if grid[cell] == 0 and neighbour_values.count(1) == 3:
            return 1
        # Death by isolation: cell is alive and has one or fewer
        # live neighbours
        elif grid[cell] == 1 and neighbour_values.count(1) <= 1:
            return 0
        # Death by overpopulation: cell is alive and has four or
        # more live neighbours
        elif grid[cell] == 1 and neighbour_values.count(1) >= 4:
            return 0
        # Survive: cell is alive and has either two or three
        # alive neighbours
        elif grid[cell] == 1 and neighbour_values.count(1) in [2, 3]:
            return 1

        return 0
