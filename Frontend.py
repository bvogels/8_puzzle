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
        print("(1) Misplaced tiles (Hamming)")
        print("(2) Manhattan distance")
        print("(3) Run both heuristics")
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

    def statistics(self, data):
        print("++++++++++++++++ Some statistics of the current grid ++++++++++++++++")
        print("Start grid ", data[0])
        print("Goal grid  ", data[1])
        print("---------------------------------------------------------------------")
        print("Misplaced Tiles (Hamming)")
        print("Expanded Nodes: ", data[2][1][1])
        print("Elapsed Time: ", int(data[2][1][0] * 1000), "ms")
        print("Consumed Memory: ", data[2][1][2][1] / 1000, "Memory units")
        print("---------------------------------------------------------------------")
        print("Manhattan Distance")
        print("Expanded Nodes: ", data[2][2][1])
        print("Elapsed Time: ", int(data[2][2][0] * 1000), "ms")
        print("Consumed Memory: ", data[2][2][2][1] / 1000, "Memory units")
