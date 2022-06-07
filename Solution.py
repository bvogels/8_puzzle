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
    heuristic = 100
    search_path = {}
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
        self.search_path.clear()
        self.heuristic = 100
        self.tiles.queue.clear()
        start_grid = copy.deepcopy(self.grid)
        grid = copy.deepcopy(self.grid)
        self.tiles.put(start_grid)
        self.search_path[self.heuristic_method(self.grid)] = [start_grid]
        while grid != self.default_goal_state:
            if self.tiles.qsize() != 0:
                grid = self.peek()
            else:
                grid = copy.deepcopy(start_grid)
            self.heuristic = self.heuristic_method(grid)
            # self.explore(grid)
            grid = copy.deepcopy(self.explore(grid))  # The calculated next state is obtained.
            self.count += 1
            self.heuristic = self.heuristic_method(grid)
            print("Count: ", self.count, "; Grid: ", grid, "; Heuristic: ", self.heuristic)
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
        null_position_grid = self.get_tile(0, self.peek())  # Null position of current state is determined
        to_move = self.grid[null_position_intermediate_grid[0]][
            null_position_intermediate_grid[1]]  # The number to move is determined
        self.peek()[null_position_grid[0]][null_position_grid[1]] = to_move  # Place new number in null position
        self.peek()[null_position_intermediate_grid[0]][
            null_position_intermediate_grid[1]] = 0  # Place null in old position
        return intermediate_grid

    ###
    ###### Calculate heuristic depending on the chosen methodology.
    #########
    ######
    ###

    def heuristic_method(self, grid):
        heuristic = 0
        for row in zip(grid, self.default_goal_state):
            for col in zip(row[0], row[1]):
                if col[0] != col[1] and col[0] != 0:
                    if self.heuristic_choice == 1:  # misplaced tiles
                        heuristic += 1
                    if self.heuristic_choice == 2:  # manhattan distance
                        source_position = self.get_tile(col[0], grid)
                        target_position = self.get_tile(col[0], self.default_goal_state)
                        heuristic += abs(source_position[0] - target_position[0]) + abs(
                            source_position[1] - target_position[1])
        return heuristic

    ###
    ###### Explores the vicinity around the null position
    #########
    ######
    ###

    def explore(self, grid):
        null_position = self.get_tile(0, grid)
        if null_position[0] == 0:
            if null_position[1] == 0:
                to_move_coords = [[0, 1], [1, 0]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 1:
                to_move_coords = [[0, 0], [0, 2], [1, 1]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 2:
                to_move_coords = [[0, 1], [1, 2]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
        if null_position[0] == 1:
            if null_position[1] == 0:
                to_move_coords = [[0, 0], [1, 1], [2, 0]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 1:
                to_move_coords = [[0, 1], [1, 0], [1, 2], [2, 1]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 2:
                to_move_coords = [[0, 2], [1, 1], [2, 2]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
        if null_position[0] == 2:
            if null_position[1] == 0:
                to_move_coords = [[1, 0], [2, 1]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 1:
                to_move_coords = [[2, 0], [1, 1], [2, 2]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)
            elif null_position[1] == 2:
                to_move_coords = [[2, 1], [1, 2]]
                return self.calculate_heuristic(to_move_coords, null_position, grid)

    ###
    ###### Calculates the heuristic for the possible next states (misplaced tiles)
    #########
    ######
    ###

    def calculate_heuristic(self, to_move_coords, null_position, grid):
        candidates = {}  # Here, all the candidates are saved.
        for coords in to_move_coords:  # Possible candidates are checked
            candidate = copy.deepcopy(grid)  # A copy of the current state is generated
            candidate[null_position[0]][null_position[1]] = candidate[coords[0]][
                coords[1]]  # A test with the new state is initiated
            candidate[coords[0]][coords[1]] = 0  # Null is inserted where a the number was swapped
            heuristic = self.heuristic_method(
                candidate)  # Heuristic is calculated. How many tiles are in the new state misplaced?
            if heuristic not in candidates:
                candidates[heuristic] = [candidate]
            else:
                candidates[heuristic].append(candidate)  # The candidate is saved.
        return self.elect_next_state(candidates)

    ###
    ###### Picks the next state from a list of candidates.
    #########
    ######
    ###

    def elect_next_state(self, candidates):
        # if min(candidates.keys()) <= self.heuristic:
        for heuristic in sorted(candidates):
            for candidate in candidates[heuristic]:
                if heuristic not in self.search_path:
                    self.search_path[heuristic] = []
                if candidate not in self.search_path[heuristic]:
                    self.search_path[heuristic].append(candidate)
                    self.tiles.put(candidate)
                    self.level += 1
                    return candidate
        self.level -= 1
        self.tiles.get()
        print("Grid removed")
        print("Queue size: ", self.tiles.qsize())
        return self.tiles.get()
