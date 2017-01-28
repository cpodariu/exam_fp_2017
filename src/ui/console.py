class Console:
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def __ui_print_current_state(self):
        sentence, points = self.__ctrl.get_current_state()
        if sentence == self.__ctrl.unscrambled:
            print("You won with a score of: ", points)
            return False
        if points == 0:
            print("Game over!")
            return False
        print(sentence,", Score: " ,points)
        return True

    def __ui_get_command(self):
        try:
            command = str(input())
        except:
            raise ValueError("Invalid command")

        command = command.split(" ")
        if command[0] == "swap":
            try:
                command[1] = int(command[1])
                command[2] = int(command[2])
                command[4] = int(command[4])
                command[5] = int(command[5])
            except:
                raise ValueError("Swap arguments must be integers")
            self.__ctrl.swap_letters(int(command[1]), int(command[2]), int(command[4]), int(command[5]))
            return True
        if command[0] == "undo":
            self.__ctrl.remember_history()
            return True
        print("Unknown command")
        return True

    def run(self):
        print("Unscrambled sentence:")
        print(self.__ctrl.unscrambled)
        OK = True
        while OK:
            self.__ctrl.make_history()
            self.__ui_print_current_state()
            try:
                OK = self.__ui_get_command()
            except ValueError as f:
                print(f)
            except IndexError as f:
                print(f)