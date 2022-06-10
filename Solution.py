import copy
import queue
import time



class Solution:
    def __init__(self, grid, heuristic_choice, goal_state):
        self.grid = grid  # The actual grid
        self.heuristic_choice = heuristic_choice
        self.goal_state = goal_state
        self.g = grid  # The grid object. Only used for printing the grid, e. g. having access to the grid functions.

    visited_nodes = 0 # Saves the number of visited nodes
    heuristic = 100 # Heuristic (100 is just a dummy value)
    search_path = {} # Saves the already visited nodes
    level = 0 # The level of the search tree
    tiles = queue.LifoQueue() # Tiles that are visited but not fully explored





    ###
    ###### Solves the puzzle.
    #########
    ######
    ###

    def solve_puzzle(self):

        # Helper function to reset global values (see below)
        self.reset()

        # One needs to copies of the start grid in order to address the same grid under different names.
        start_grid = copy.deepcopy(self.grid)
        grid = copy.deepcopy(self.grid)

        # The start grid is the bottom element of the queue and the search path
        self.tiles.put(start_grid)
        self.search_path[self.heuristic_method(self.grid)] = [start_grid]

        # This is the stop condition. The loop is executed as long the grid is not equal to the goal state.
        while grid != self.goal_state:

            # If the backtracking reaches the bottom of the queue (qsize() == 0), the start grid has to be re-queued.
            if self.tiles.qsize() != 0:
                grid = self.peek()
            else:
                grid = copy.deepcopy(start_grid)

            # The heuristic for the current grid is determined.
            self.heuristic = self.heuristic_method(grid)

            # The next grid is determined and subsequently becomes the new current grid.
            grid = copy.deepcopy(self.explore(grid))

            # Number of visited nodes is incremented.
            self.visited_nodes += 1

            # Some printouts
            print("Count: ", self.visited_nodes, "; Grid: ", grid, "; Heuristic: ", self.heuristic)
        return True



    ###
    ###### Calculate heuristic depending on the chosen methodology.
    #########
    ######
    ###

    def heuristic_method(self, grid):
        heuristic = 0
        for row in zip(grid, self.goal_state):
            for col in zip(row[0], row[1]):
                if col[0] != col[1] and col[0] != 0:
                    if self.heuristic_choice == 1:  # misplaced tiles
                        heuristic += 1
                    if self.heuristic_choice == 2:  # manhattan distance
                        source_position = self.get_tile(col[0], grid)
                        target_position = self.get_tile(col[0], self.goal_state)
                        heuristic += abs(source_position[0] - target_position[0]) + abs(
                            source_position[1] - target_position[1])
        return heuristic



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
    ###### Picks the next state from a list of candidates. See documentation for further explainations
    #########
    ######
    ###

    def elect_next_state(self, candidates):
        #if min(candidates.keys()) <= self.heuristic:
        for heuristic in sorted(candidates):
            for candidate in candidates[heuristic]:
                #if heuristic <= self.heuristic:
                if heuristic not in self.search_path:
                    self.search_path[heuristic] = []
                if candidate not in self.search_path[heuristic]:
                    self.search_path[heuristic].append(candidate)
                    self.tiles.put(candidate)
                    self.level += 1
                    return candidate
        self.level -= 1
        return self.tiles.get()



    ############################
    ##### HELPER FUNCTIONS #####
    ############################

    ###
    ###### Resets global values
    #########
    ######
    ###

    def reset(self):
        self.search_path.clear()
        self.heuristic = 100
        self.tiles.queue.clear()

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
    ###### This function has a look at what grid is to be considered next.
    #########
    ######
    ###

    def peek(self):
        g = self.tiles.get()
        self.tiles.put(g)
        return g

    ###
    ###### Gets the coordinates of a tile in a given grid.
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