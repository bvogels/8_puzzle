import copy

import Grid


class Solution:
    def __init__(self, grid):
        self.grid = grid.grid

    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    count = 0
    heuristic = 0
    search_path = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    visited_states = []

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
        self.heuristic = 10
        intermediate_grid = self.explore()
        null_position_intermediate_grid = self.get_tile(0, intermediate_grid)
        null_position_grid = self.get_tile(0, self.grid)
        to_move = self.grid[null_position_intermediate_grid[0]][null_position_intermediate_grid[1]]
        self.grid[null_position_grid[0]][null_position_grid[1]] = to_move
        self.grid[null_position_intermediate_grid[0]][null_position_intermediate_grid[1]] = 0
        self.print_ascii_grid()
        self.count += 1
        print(self.count)
        self.solve_puzzle(self.grid)

    def print_ascii_grid(self):
        print("+---" * 3 + "+")
        print("|", self.grid[0][0], "|", self.grid[0][1], "|", self.grid[0][2], "|", )
        print("+---" * 3 + "+")
        print("|", self.grid[1][0], "|", self.grid[1][1], "|", self.grid[1][2], "|", )
        print("+---" * 3 + "+")
        print("|", self.grid[2][0], "|", self.grid[2][1], "|", self.grid[2][2], "|", )
        print("+---" * 3 + "+")

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
        candidates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        for coords in to_move_coords:
            candidate = copy.deepcopy(self.grid)
            candidate[null_position[0]][null_position[1]] = candidate[coords[0]][coords[1]]
            candidate[coords[0]][coords[1]] = 0
            heuristic = self.count_misplaced_tiles(candidate)
            candidates[heuristic] += candidate
        self.elect_next_state(candidates)

        #     if heuristic < self.heuristic: # worse heuristic is necessary if all other path are used
        #         self.heuristic = heuristic
        #         if candidate not in self.search_path[self.heuristic]:
        #             elective = copy.deepcopy(candidate)
        # x = self.search_path.get(self.heuristic)
        # x.append(elective)
        # return elective

    def elect_next_state(self, candidates):
        for heuristic in candidates.keys():
            if len(candidates[heuristic]) != 0:
                print()
        pass
