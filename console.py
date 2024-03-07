#!/usr/bin/python3
# This contains the entry point of the command interpreter
# In it, we define all commands that users can use to
# interact with and manage the objects
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """exits the program"""
        return True
    def do_EOF(self, line):
        """exits the program"""
        return True
    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        It does not repeat the last non-empty command entered.
        """
        return None
    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        model.storage.new(self)
        if self.__class__.__name__ == None:
            print("** class name is missing **")
        elif not self.__class__.__name__:
            print("** class doesn't exist **")
        else:
            print(self.id)
        print(self.id)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
