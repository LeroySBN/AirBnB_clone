#!/usr/bin/python3
"""console module"""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }
class_list = []
for key in classes:
    class_list.append(key)


class HBNBCommand(cmd.Cmd):
    """HBNB Console"""
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                new_instance = classes[args]()
                print(new_instance.id)
                new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                print(storage.all())

    def do_update(self, arg):
        """Updates an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(storage.all()[key],
                                        args[2], args[3])
                                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
