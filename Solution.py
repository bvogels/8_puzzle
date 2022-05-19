class Solution:
    def __init__(self, grid):
        self.grid = grid.grid

    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    costs = {0: 0, 1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9}

    def get_tile(self, tile, search_grid):
        null_coords = []
        for row in search_grid:
            if tile in row:
                null_coords.append(search_grid.index(row))
                null_coords.append(row.index(tile))
                return null_coords

    def solve_puzzle(self, grid):
        if self.grid == self.default_goal_state:
            return True
        self.calculate_cost()
        fringe = {key: value for (key, value) in self.costs.items() if value > 0}
        to_move = min(fringe, key = fringe.get)
        print("x")


    def calculate_cost(self):
        null_position = self.get_tile(0, self.grid)
        if null_position[0] == 0:
            if null_position[1] == 0:  # Calculate costs from 0 position than add 1
                to_move_coords = [[0, 1], [1, 0]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[0, 0], [0, 2], [1, 1]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[0, 1], [1, 2]]
                self.calculate_distance(to_move_coords, null_position)
        if null_position[0] == 1:
            if null_position[1] == 0:
                to_move_coords = [[0, 0], [1, 1], [2, 0]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[0, 1], [1, 0], [1, 2], [2, 1]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[0, 2], [1, 1], [2, 2]]
                self.calculate_distance(to_move_coords, null_position)
        if null_position[0] == 2:
            if null_position[1] == 0:
                to_move_coords = [[1, 0], [2, 1]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[2, 0], [1, 1], [2, 2]]
                self.calculate_distance(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[2, 1], [1, 2]]
                self.calculate_distance(to_move_coords, null_position)

    def calculate_distance(self, to_move_coords, null_position):
        for coords in to_move_coords:
            to_move = self.grid[coords[0]][coords[1]]
            target_position = self.get_tile(to_move, self.default_goal_state)
            self.costs[to_move] = abs(null_position[1] - target_position[1]) + abs(
                null_position[0] - target_position[0]) + 1

    def right(self, row, col):
        self.grid[row][col + 1] = self.grid[row][col]
        self.grid[row][col] = 0

    def left(self, row, col):
        self.grid[row][col - 1] = self.grid[row][col]
        self.grid[row][col] = 0

    def up(self, row, col):
        self.grid[row - 1][col] = self.grid[row][col]
        self.grid[row][col] = 0

    def down(self, row, col):
        self.grid[row + 1][col] = self.grid[row][col]
        self.grid[row][col] = 0
