class Frontend:
    def main_menu(self):
        print("+++++++++++++++++++++++")
        print("+++ 8 puzzle solver +++")
        print("+++++++++++++++++++++++")
        print()
        print("Choose an option:")
        print("(1) Solve random puzzle")
        print("(2) Enter own puzzle")
        print("(3) Choose pre-defined puzzle")
        print("(4) Quit")
        choice = int(input("Choice: "))
        return choice

    def messages(self, message, info):
        m = {
            1: "Please enter grid as continuous sequence of ints (e. g. 012345678): ",
            2: "Grid has no solution.",
            3: "Not a valid grid.",
            4: "Grid to short/long",
            5: "Path ends here.",
            6: "Heuristic is now",
            7: "Loop encountered in valid grid while solving."
        }
        return m[message]

    def choose_heuristic(self):
        print("Choose heuristic:")
        print("(1) Misplaced tiles")
        print("(2) Manhattan distance")
        heuristic = int(input("Choice: "))
        return heuristic

    def goal_state(self):
        print("Choose or enter goal state:")
        print("(1) Default goal state (0-1-2-3-4-5-6-7-8)")
        print("(2) Random goal state")
        print("(3) Pre-defined goal state")
        print("(4) Enter own goal state")
        gstate = int(input("Choice: "))
        return gstate

    def statistics(self, paths, nodes, branching_level, runtime):
        print("+++++ Some statistics of the current grid +++++")
        #print("Worst heuristic: ", worst_heuristic)
        #print("Paths explored: ", paths)
        print("Nodes expanded: ", nodes)
        print("Branching level: ", branching_level)
        print("Runtime in miliseconds: ", runtime * 1000)
