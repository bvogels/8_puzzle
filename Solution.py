import copy
import queue
import math


class Solution:
    def __init__(self, grid, heuristic_choice):
        self.grid = grid.grid  # The actual grid
        self.heuristic_choice = heuristic_choice
        self.g = grid  # The grid object. Only used for printing the grid, e. g. having access to the grid functions.

    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    count = 0
    heuristic = 10
    search_path = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    level = 0
    tiles = queue.LifoQueue()

    ###
    ###### Gets the coordinates of a given grid.
    #########
    ######
    ###

    def get_tile(self, tile, search_grid):
        null_coords = []
        for row in search_grid:
            if tile in row:
                null_coords.append(search_grid.index(row))
                null_coords.append(row.index(tile))
                return null_coords

    ###
    ###### Solves the puzzle.
    #########
    ######
    ###

    def solve_puzzle(self):
        start_grid = copy.deepcopy(self.grid)
        self.tiles.put(start_grid)
        self.search_path[self.count_misplaced_tiles(self.grid)].append(self.grid)
        while self.grid != self.default_goal_state:
            self.grid = self.peek()
            if self.heuristic_choice == 1:
                self.heuristic = self.count_misplaced_tiles(self.grid)
            elif self.heuristic_choice == 2:
                self.heuristic = self.calculate_manhattan_distance(self.grid)
            self.reconfigure_grid(self.explore())  # The calculated next state is obtained.
            self.count += 1
            print("Count: ", self.count, "; Grid: ", self.grid, "; Heuristic: ", self.heuristic)
        # self.g.print_ascii_grid()
        print("Solved")
        # for config, step in enumerate(range(self.tiles.qsize())):
        #    print(step, self.tiles.get())
        return True

    ###
    ###### This function has a look at what grid is to be considered next.
    #########
    ######
    ###

    def peek(self):
        g = self.tiles.get()
        self.tiles.put(g)
        return g

    ###
    ###### Reconfigures the self.grid to become the new grid
    #########
    ######
    ###

    def reconfigure_grid(self, intermediate_grid):
        null_position_intermediate_grid = self.get_tile(0,
                                                        intermediate_grid)  # Null position of the next state is determined.
        null_position_grid = self.get_tile(0, self.grid)  # Null position of current state is determined
        to_move = self.grid[null_position_intermediate_grid[0]][
            null_position_intermediate_grid[1]]  # The number to move is determined
        self.grid[null_position_grid[0]][null_position_grid[1]] = to_move  # Place new number in null position
        self.grid[null_position_intermediate_grid[0]][
            null_position_intermediate_grid[1]] = 0  # Place null in old position

    ###
    ###### Counts the misplaced titles in order to calculate the heuristic.
    #########
    ######
    ###

    def count_misplaced_tiles(self, grid):
        misplaced_tiles = 0
        for t, g in zip(grid, self.default_goal_state):
            tile = 0
            while tile < 3:
                if t[tile] != g[tile] and t[tile] != 0:
                    misplaced_tiles += 1
                tile += 1
        return misplaced_tiles

    ###
    ###### Manhattan Distance
    ###### The sum of the vertical and horizontal distance from the blocks to the goal position
    #########
    ######
    ###
    def alternative_manhattan_distance(self, grid):  ## initial state = grid?
        initial_config = grid
        man_dist = 0
        for i, item in enumerate(initial_config):
            prev_row, prev_col = int(i / 3), i % 3  ## previous position
            goal_row, goal_col = int(item / 3), item % 3  ## goal position
            man_dist += abs(prev_row - goal_row) + abs(prev_col - goal_col)
        return man_dist

    def calculate_manhattan_distance(self, grid):
        manhattan_distance = 0
        for t, g in zip(grid, self.default_goal_state):
            tile = 0
            while tile < 3:
                if t[tile] != g[tile] and t[tile] != 0:


        for tile in grid:
            for col in tile:
                if grid[tile][col] != self.default_goal_state[tile][col]:
                    target_destination = self.get_tile(grid[tile][col], self.default_goal_state)
                    manhattan_distance += abs(grid.index(tile) - target_destination[0]) + abs(grid.index(col) - target_destination[1])
        return manhattan_distance

    ###
    ###### Explores the vicinity around the null position
    #########
    ######
    ###

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

    ###
    ###### Calculates the heuristic for the possible next states (misplaced tiles)
    #########
    ######
    ###

    def calculate_heuristic(self, to_move_coords, null_position):
        candidates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
                      8: []}  # Here, all the candidates are saved.
        for coords in to_move_coords:  # Possible candidates are checked
            candidate = copy.deepcopy(self.grid)  # A copy of the current state is generated
            candidate[null_position[0]][null_position[1]] = candidate[coords[0]][
                coords[1]]  # A test with the new state is initiated
            candidate[coords[0]][coords[1]] = 0  # Null is inserted where a the number was swapped
            if self.heuristic_choice == 1:
                heuristic = self.count_misplaced_tiles(
                    candidate)  # Heuristic is calculated. How many tiles are in the new state misplaced?
            elif self.heuristic_choice == 2:
                heuristic = self.calculate_manhattan_distance(candidate)
            candidates[heuristic].append(candidate)  # The candidate is saved.
        return self.elect_next_state(candidates)

    ###
    ###### Picks the next state from a list of candidates.
    #########
    ######
    ###

    def elect_next_state(self, candidates):
        for heuristic in candidates.keys():
            if len(candidates[heuristic]) != 0:  # and heuristic <= self.heuristic:
                for candidate in candidates[heuristic]:
                    if candidate not in self.search_path[heuristic]:
                        self.search_path[heuristic].append(candidate)
                        self.tiles.put(candidate)
                        self.level += 1
                        self.grid = candidate
                        return self.grid
        self.level -= 1
        # e = self.tiles.get()
        print("Grid removed")
        print("Queue size: ", self.tiles.qsize())
        return self.tiles.get()
