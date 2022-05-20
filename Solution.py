import copy

import Grid


class Solution:
    def __init__(self, grid):
        self.grid = grid.grid

    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    costs = {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9}
    count = 0
    heuristic = 9
    search_path = {}

    def get_tile(self, tile, search_grid):
        null_coords = []
        for row in search_grid:
            if tile in row:
                null_coords.append(search_grid.index(row))
                null_coords.append(row.index(tile))
                return null_coords

    def solve_puzzle(self, grid):
        if self.count == 20:
            return
        if self.grid == self.default_goal_state:
            return True
        intermediate_grid = self.explore()
        x = self.get_tile(0, self, grid)
        to_move = self.grid[]
        # to_move = min(fringe, key=fringe.get)
        # to_move_coords = self.get_tile(to_move, self.grid)
        # null_position = self.get_tile(0, self.grid)
        # self.grid[null_position[0]][null_position[1]] = to_move
        # self.grid[to_move_coords[0]][to_move_coords[1]] = 0
        # grid.print_ascii_grid()
        # self.count += 1
        # self.solve_puzzle(grid)

    def count_misplaced_tiles(self, grid):
        misplaced_tiles = 0
        for t, g in zip(grid, self.default_goal_state):
            row = 0
            while row < 3:
                if t[row] != g[row]:
                    misplaced_tiles += 1
                row += 1
        return misplaced_tiles

    def determine_candidates(self):
        pass

    def explore(self):
        null_position = self.get_tile(0, self.grid)
        if null_position[0] == 0:
            if null_position[1] == 0:
                to_move_coords = [[0, 1], [1, 0]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[0, 0], [0, 2], [1, 1]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[0, 1], [1, 2]]
                return self.calculate_heuristic(to_move_coords, null_position)
        if null_position[0] == 1:
            if null_position[1] == 0:
                to_move_coords = [[0, 0], [1, 1], [2, 0]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[0, 1], [1, 0], [1, 2], [2, 1]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[0, 2], [1, 1], [2, 2]]
                return self.calculate_heuristic(to_move_coords, null_position)
        if null_position[0] == 2:
            if null_position[1] == 0:
                to_move_coords = [[1, 0], [2, 1]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 1:
                to_move_coords = [[2, 0], [1, 1], [2, 2]]
                return self.calculate_heuristic(to_move_coords, null_position)
            elif null_position[1] == 2:
                to_move_coords = [[2, 1], [1, 2]]
                return self.calculate_heuristic(to_move_coords, null_position)

    def calculate_heuristic(self, to_move_coords, null_position):
        for coords in to_move_coords:
            visited_states, elective = [], []
            candidate = copy.deepcopy(self.grid)
            candidate[null_position[0]][null_position[1]] = candidate[coords[0]][coords[1]]
            candidate[coords[0]][coords[1]] = 0
            heuristic = self.count_misplaced_tiles(candidate)
            if heuristic < self.heuristic:
                self.heuristic = heuristic
                elective = copy.deepcopy(candidate)
            visited_states.append(elective)
            self.search_path[self.heuristic] = visited_states
            return elective


            # to_move = self.grid[coords[0]][coords[1]]
            # if self.get_tile(to_move, self.grid) != self.get_tile(to_move, self.default_goal_state):
            #     target_position = self.get_tile(to_move, self.default_goal_state)
            #     self.costs[to_move] = abs(null_position[1] - target_position[1]) + abs(
            #         null_position[0] - target_position[0]) + 1
            # else:
            #    self.costs[to_move] = 0
