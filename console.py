#!/usr/bin/python3
"""testing module"""
import cmd
from models.base_model import BaseModel
from models import storage
# from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class handling command interpreter"""
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]
    prompt = '(hbnb)'
    def do_quit(self, line):
        """Quit - command to exit the program
        """
        exit()

    def do_help(self, arg: str) -> bool | None:
        """Help - command to display command help
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """EOF - command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing when the line is empty"""
        pass

    def do_create(self, line):
        """Create - Creates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id. 
         Ex: $ create BaseModel
        """
        if (len(line) == 0):
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            my_model = eval(line)()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """Show - Prints the string representation of an instance
         based on the class name and id.
         Ex: $ show BaseModel 1234-1234-1234
          """
        if (len(line) == 0):
            print("** class name missing **")
        else:
            args = line.split()
            if (args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
            else:
                if (len(args) == 1):
                    print("** instance id missing **")
                else:
                    instance = args[0]+"."+args[1]
                    models = storage.all()
                    if (instance in models):
                        print(models[instance])
                    else:
                        print("** no instance found **")

    def do_destroy(self, line):
        """Destroy - Deletes an instance based on the class name and
         id (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234"""
        if (len(line) == 0):
            print("** class name missing **")
        else:
            args = line.split()
            if (args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
            else:
                if (len(args) == 1):
                    print("** instance id missing **")
                else:
                    instance = args[0]+"."+args[1]
                    models = storage.all()
                    if (instance in models):
                        del models[instance]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """All - Prints all string representation of all instances
          based or not on the class name.
          Ex: $ all BaseModel or $ all"""
        if (len(line) == 0):
            models = storage.all()
            list_models = []
            for i in models.values():
                list_models.append(str(i))
            print(list_models)
        elif line in HBNBCommand.classes:
            models = storage.all()
            list_models = []
            for i in models.values():
                if i.__class__.__name__ == line:
                    list_models.append(str(i))
            print(list_models)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update - Updates an instance based on the class name and
          id by adding or updating attribute (save the change into the JSON file).
          Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" """
        print("update")
        if (len(line) == 0):
            print("** class name missing **")
            return
        args = line.split()
        print(args)
        if (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
            return
        if (len(args) == 1):
            print("** instance id missing **")
            return
        instance = args[0]+"."+args[1]
        objects = storage.all()
        if (instance not in objects):
            print("** no instance found **")
            return
        if (len(args) == 2):
            print("** attribute name missing **")
            return
        if (len(args) == 3):
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return
        attr = args[2]
        attr_array = line.split('"')
        try:
            value = getattr(objects[instance], attr)
            mtype = type(value)
            setattr(objects[instance], attr, mtype(attr_array[1]))
        except:
            setattr(objects[instance], attr, attr_array[1])
        storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()