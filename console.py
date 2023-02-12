#!/usr/bin/env python3
"""
console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """Overwriting the emptyline method"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
