#AirBnB_clone - The Console

Command interpreter to manage the AirBnB objects
****
The AirBnB_clone is the first step towards building our first full web application.\

## How it works
**The console:**
 - Displays the prompt (default prompt: "(cmd)", our prompt: "(hbnb)") and waits for user input.
 - Reads the entered command and the argument.
 - Looks for the function of the command. For example: entering the command "all", makes the console looks for "do_all(self, arg)" function.
 - Executes the function.
 - If the typed command (the function) doesn't exist, the console prints an Error message.
 - Quits when the user enters "quit" or "EOF" or presses Ctrl+d.

## USAGE
You can run this program on your local machine by following these steps:
> **Step 1:** Clone our repository using this command, (you need to have git and python3 installed on your machine first)
````
git clone https://github.com/yasmineholb/AirBnB_clone.git
````
> **Step 2:** Change directory to AirBnB_clone:
````
cd AirBnB_clone
````
> **Step 3:** Execute the console in this way:
````
./console.py
````
> **Step 4:** enter your command (In this example, our command is "help")
````
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
````
**Exiting the program**
When you want to exit the program, you can use one of the following methods:
> **1: Enter "quit" or "EOF"**
````
(hbnb) quit
````
> **2: Press on Ctrl d**
****