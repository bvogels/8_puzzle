import copy


class Solution:
    def __init__(self, grid):
        self.grid = grid.grid  # The actual grid
        self.g = grid  # The grid object. Only used for printing the grid, e. g. having access to the grid functions.

    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    count = 0
    heuristic = 10
    search_path = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    paths = 0

    def get_tile(self, tile, search_grid):
        null_coords = []
        for row in search_grid:
            if tile in row:
                null_coords.append(search_grid.index(row))
                null_coords.append(row.index(tile))
                return null_coords

    ###
    ###### Solves the puzzle through a recursive call.
    #########
    ######
    ###

    def solve_puzzle(self, grid):
        while self.grid != self.default_goal_state:
            if self.count == 0: # calculate initial heuristic
                self.heuristic = self.count_misplaced_tiles(self.grid)
            intermediate_grid = self.explore()  # The calculated next state is obtained.
            null_position_intermediate_grid = self.get_tile(0,
                                                            intermediate_grid)  # Null position of the next state is determined.
            null_position_grid = self.get_tile(0, self.grid)  # Null position of current state is determined
            to_move = self.grid[null_position_intermediate_grid[0]][
                null_position_intermediate_grid[1]]  # The number to move is determined
            self.grid[null_position_grid[0]][null_position_grid[1]] = to_move  # Place new number in null position
            self.grid[null_position_intermediate_grid[0]][
                null_position_intermediate_grid[1]] = 0  # Place null in old position
            #if self.count % 50 == 0:  # Print the grid all 50 recursions
            self.g.print_ascii_grid()
            self.count += 1
            print(self.count)
        self.g.print_ascii_grid()
        print(self.paths, "paths expanded.")
        return True

    ###
    ###### Counts the misplaced titles in order to calculate the heuristic.
    #########
    ######
    ###

    def count_misplaced_tiles(self, grid):
        misplaced_tiles = 0
        for t, g in zip(grid, self.default_goal_state):
            row = 0
            while row < 3:
                if t[row] != g[row] and t[row] != 0:
                    misplaced_tiles += 1
                row += 1
        return misplaced_tiles

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
        candidates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [],
                      9: []}  # Here, all the candidates are saved.
        for coords in to_move_coords:  # Possible candidates are checked
            candidate = copy.deepcopy(self.grid)  # A copy of the current state is generated
            candidate[null_position[0]][null_position[1]] = candidate[coords[0]][
                coords[1]]  # A test with the new state is initiated
            candidate[coords[0]][coords[1]] = 0  # Null is inserted where a the number was swapped
            heuristic = self.count_misplaced_tiles(
                candidate)  # Heuristic is calculated. How many tiles are in the new state misplaced?
            candidates[heuristic].append(candidate)  # The candidate is saved.
        return self.elect_next_state(candidates)

    ###
    ###### Picks the next state from a list of candidates.
    #########
    ######
    ###

    def elect_next_state(self, candidates):
        for heuristic in candidates.keys():  # Every heuristic is now checked for which is best
            if len(candidates[heuristic]) != 0:# and heuristic <= self.heuristic:  # Only where a heurisic has been saved
                for e in candidates[heuristic]:  # Since the states are in a list, this list is iterated through
                    if e not in self.search_path[heuristic]:  # If the state has not been in the search path, it is the One!
                        self.search_path[heuristic].append(e)  # The state is inserted in the search path to avoid loops. It cannot be used again.
                        if self.heuristic < heuristic:
                            print("Path ends here.")
                            self.paths += 1
                        self.heuristic = heuristic
                        print("Heuristic is now: ", self.heuristic)
                        return e
