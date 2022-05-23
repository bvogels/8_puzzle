class Frontend:
    def main_menu(self):
        print("+++++++++++++++++++++++")
        print("+++ 8 puzzle solver +++")
        print("+++++++++++++++++++++++")
        print()
        print("Choose an option:")
        print("(1) Solve random puzzle")
        print("(2) Enter own puzzle")
        choice = int(input("Choice: "))
        return choice

    def messages(self, message, info):
        m = {
            1: "Please enter grid as continuous sequence of ints (e. g. 012345678): ",
            2: "Grid has no solution.",
            3: "Not a valid grid.",
            4: "Grid to short/long",
            5: "Path ends here.",
            6: "Heuristic is now"
        }
        return m[message]
